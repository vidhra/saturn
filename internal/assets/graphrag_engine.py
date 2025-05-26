import os
import json
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
import networkx as nx
from neo4j import GraphDatabase

from saturn.rag_engine import RAGEngine
from .hybrid_graph_manager import HybridGraphManager

class GraphRAGEngine:
    """Manages asset discovery and monitoring using GraphRAG approach."""
    
    def __init__(self, 
                 project_id: str,
                 rag_engine: Optional[RAGEngine] = None,
                 output_dir: str = "./gcp_graph_data",
                 gcp_creds_path: Optional[str] = None,
                 neo4j_uri: str = "bolt://localhost:7687",
                 neo4j_user: str = "neo4j",
                 neo4j_password: str = "yourpassword"):
        """
        Initialize the GraphRAG Engine.
        
        Args:
            project_id: GCP project ID
            rag_engine: Optional RAGEngine instance for document querying
            output_dir: Directory to store graph data
            gcp_creds_path: Path to GCP credentials file
            neo4j_uri: Neo4j connection URI
            neo4j_user: Neo4j username
            neo4j_password: Neo4j password
        """
        self.project_id = project_id
        self.output_dir = output_dir
        self.gcp_creds_path = gcp_creds_path
        self.rag_engine = rag_engine
        
        # Initialize hybrid graph manager
        self.graph_manager = HybridGraphManager(
            neo4j_uri=neo4j_uri,
            neo4j_user=neo4j_user,
            neo4j_password=neo4j_password,
            graph_file=os.path.join(output_dir, "graph_data.json")
        )
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def discover_assets(self, asset_types: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Discover GCP assets and build a knowledge graph.
        
        Args:
            asset_types: Optional list of asset types to discover
            
        Returns:
            Dictionary containing nodes and relationships
        """
        self.logger.info(f"Starting asset discovery for project: {self.project_id}")
        
        # Use existing asset discovery code
        from .graphrag_system import get_gcp_assets, transform_asset_to_node, infer_relationships, COMMON_ASSET_TYPES
        
        scope = f"projects/{self.project_id}"
        assets = get_gcp_assets(scope, asset_types or COMMON_ASSET_TYPES, self.gcp_creds_path)
        
        # Transform assets into graph nodes
        nodes = []
        for asset in assets:
            node = transform_asset_to_node(asset, project_id_override=self.project_id)
            if node:  # Skip empty nodes
                nodes.append(node)
                # Add node to graph
                self.graph_manager.add_asset(
                    asset_id=node["id"],
                    properties={k: v for k, v in node.items() if k != "id"}
                )
            
        # Build relationships between nodes
        node_map = {node["id"]: node for node in nodes}
        relationships = []
        for node in nodes:
            node_relationships = infer_relationships(node, node_map)
            relationships.extend(node_relationships)
            # Add relationships to graph
            for rel in node_relationships:
                self.graph_manager.add_relationship(
                    source_id=rel["source_id"],
                    target_id=rel["target_id"],
                    relation_type=rel["relation_type"]
                )
        
        # Save graph data
        self._save_graph_data(nodes, relationships)
        
        # Update RAG engine if available
        if self.rag_engine:
            self._update_rag_engine(nodes, relationships)
            
        return {
            "nodes": nodes,
            "relationships": relationships
        }

    def _save_graph_data(self, nodes: List[Dict[str, Any]], relationships: List[Dict[str, Any]]):
        """Save graph data to files."""
        nodes_file = os.path.join(self.output_dir, "nodes.json")
        relationships_file = os.path.join(self.output_dir, "relationships.json")
        
        with open(nodes_file, 'w') as f:
            json.dump(nodes, f, indent=2)
            
        with open(relationships_file, 'w') as f:
            json.dump(relationships, f, indent=2)
            
        self.logger.info(f"Saved {len(nodes)} nodes and {len(relationships)} relationships")

    def _update_rag_engine(self, nodes: List[Dict[str, Any]], relationships: List[Dict[str, Any]]):
        """Update RAG engine with new graph data."""
        if not self.rag_engine:
            return
            
        # Convert graph data to documents for RAG
        documents = []
        
        # Add node documents with graph context
        for node in nodes:
            # Get neighboring nodes and relationships
            neighbors = list(self.graph_manager.graph.neighbors(node["id"]))
            incoming = list(self.graph_manager.graph.predecessors(node["id"]))
            
            # Build context from graph structure
            context = []
            for neighbor in neighbors:
                edge_data = self.graph_manager.graph.get_edge_data(node["id"], neighbor)
                context.append(f"Connects to {neighbor} via {edge_data['relation_type']}")
            for pred in incoming:
                edge_data = self.graph_manager.graph.get_edge_data(pred, node["id"])
                context.append(f"Connected from {pred} via {edge_data['relation_type']}")
            
            doc_text = f"""
            Asset: {node['display_name']}
            Type: {node['asset_type']}
            Location: {node.get('location', 'N/A')}
            Project: {node['project_id']}
            Last Updated: {node.get('update_time', 'N/A')}
            
            Graph Context:
            {chr(10).join(context)}
            
            Resource Data:
            {json.dumps(node.get('resource_data', {}), indent=2)}
            """
            documents.append({
                "text": doc_text,
                "metadata": {
                    "asset_id": node["id"],
                    "asset_type": node["asset_type"],
                    "is_node": True,
                    "neighbors": neighbors,
                    "incoming": incoming
                }
            })
            
        # Add relationship documents with graph context
        for rel in relationships:
            source_node = self.graph_manager.graph.nodes[rel["source_id"]]
            target_node = self.graph_manager.graph.nodes[rel["target_id"]]
            
            doc_text = f"""
            Relationship: {rel['relation_type']}
            From: {source_node.get('display_name', rel['source_id'])} ({rel['source_id']})
            To: {target_node.get('display_name', rel['target_id'])} ({rel['target_id']})
            
            Source Type: {source_node.get('asset_type', 'Unknown')}
            Target Type: {target_node.get('asset_type', 'Unknown')}
            """
            documents.append({
                "text": doc_text,
                "metadata": {
                    "source_id": rel["source_id"],
                    "target_id": rel["target_id"],
                    "relation_type": rel["relation_type"],
                    "is_relationship": True
                }
            })
            
        # Update RAG engine with new documents
        self.rag_engine.ingest_and_build_index(documents, force_rebuild=True)

    def monitor_asset(self, asset_id: str) -> Dict[str, Any]:
        """
        Monitor a specific asset using GraphRAG.
        
        Args:
            asset_id: ID of the asset to monitor
            
        Returns:
            Dictionary containing asset information and related data
        """
        if not self.rag_engine:
            raise ValueError("RAG engine not initialized")
            
        # Get graph-based context
        if asset_id in self.graph_manager.graph:
            node_data = self.graph_manager.graph.nodes[asset_id]
            neighbors = list(self.graph_manager.graph.neighbors(asset_id))
            incoming = list(self.graph_manager.graph.predecessors(asset_id))
            
            # Build graph context
            context = []
            for neighbor in neighbors:
                edge_data = self.graph_manager.graph.get_edge_data(asset_id, neighbor)
                neighbor_data = self.graph_manager.graph.nodes[neighbor]
                context.append(f"Connects to {neighbor_data.get('display_name', neighbor)} via {edge_data['relation_type']}")
            for pred in incoming:
                edge_data = self.graph_manager.graph.get_edge_data(pred, asset_id)
                pred_data = self.graph_manager.graph.nodes[pred]
                context.append(f"Connected from {pred_data.get('display_name', pred)} via {edge_data['relation_type']}")
            
            # Query RAG engine with graph context
            query = f"""
            Tell me about asset {asset_id} ({node_data.get('display_name', 'Unknown')}) and its relationships.
            Context from graph:
            {chr(10).join(context)}
            """
        else:
            query = f"Tell me about asset {asset_id} and its relationships"
            
        response = self.rag_engine.query_docs(query)
        
        return {
            "asset_id": asset_id,
            "information": response,
            "timestamp": datetime.utcnow().isoformat()
        }

    def get_asset_relationships(self, asset_id: str) -> List[Dict[str, Any]]:
        """
        Get relationships for a specific asset using NetworkX graph.
        
        Args:
            asset_id: ID of the asset
            
        Returns:
            List of relationships
        """
        if asset_id not in self.graph_manager.graph:
            return []
            
        relationships = []
        
        # Get outgoing relationships
        for neighbor in self.graph_manager.graph.neighbors(asset_id):
            edge_data = self.graph_manager.graph.get_edge_data(asset_id, neighbor)
            relationships.append({
                "source_id": asset_id,
                "target_id": neighbor,
                "relation_type": edge_data["relation_type"]
            })
            
        # Get incoming relationships
        for pred in self.graph_manager.graph.predecessors(asset_id):
            edge_data = self.graph_manager.graph.get_edge_data(pred, asset_id)
            relationships.append({
                "source_id": pred,
                "target_id": asset_id,
                "relation_type": edge_data["relation_type"]
            })
            
        return relationships

    def get_asset_path(self, source_id: str, target_id: str) -> List[Dict[str, Any]]:
        """
        Find the shortest path between two assets in the graph.
        
        Args:
            source_id: Source asset ID
            target_id: Target asset ID
            
        Returns:
            List of nodes and relationships in the path
        """
        try:
            path = nx.shortest_path(self.graph_manager.graph, source_id, target_id)
            result = []
            
            for i in range(len(path) - 1):
                current = path[i]
                next_node = path[i + 1]
                edge_data = self.graph_manager.graph.get_edge_data(current, next_node)
                
                result.append({
                    "from": {
                        "id": current,
                        "type": self.graph_manager.graph.nodes[current].get("asset_type"),
                        "name": self.graph_manager.graph.nodes[current].get("display_name")
                    },
                    "to": {
                        "id": next_node,
                        "type": self.graph_manager.graph.nodes[next_node].get("asset_type"),
                        "name": self.graph_manager.graph.nodes[next_node].get("display_name")
                    },
                    "relation": edge_data["relation_type"]
                })
                
            return result
        except nx.NetworkXNoPath:
            return []

    def close(self):
        """Close connections and save data."""
        if self.graph_manager:
            self.graph_manager.close() 