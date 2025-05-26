import networkx as nx
from neo4j import GraphDatabase
from typing import Dict, Any, List, Optional, Set
import logging
import json
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class HybridGraphManager:
    """
    Hybrid graph manager that combines NetworkX for fast in-memory operations
    and Neo4j for persistent storage.
    """
    
    def __init__(
        self,
        neo4j_uri: str = "bolt://localhost:7687",
        neo4j_user: str = "neo4j",
        neo4j_password: str = "yourpassword",
        graph_file: str = "graph_data.json"
    ):
        """
        Initialize the hybrid graph manager.
        
        Args:
            neo4j_uri: Neo4j connection URI
            neo4j_user: Neo4j username
            neo4j_password: Neo4j password
            graph_file: Path to JSON file for NetworkX graph persistence
        """
        # Initialize NetworkX graph
        self.graph = nx.DiGraph()
        self.graph_file = graph_file
        
        # Initialize Neo4j connection
        try:
            self.driver = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))
            self._verify_neo4j_connection()
            logger.info("Successfully connected to Neo4j")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            self.driver = None
        
        # Load existing graph data if available
        self._load_graph_data()
    
    def _verify_neo4j_connection(self):
        """Verify Neo4j connection and create constraints if needed."""
        with self.driver.session() as session:
            # Create constraints for asset IDs
            session.run("CREATE CONSTRAINT asset_id IF NOT EXISTS FOR (a:Asset) REQUIRE a.id IS UNIQUE")
    
    def _load_graph_data(self):
        """Load graph data from JSON file if it exists."""
        if os.path.exists(self.graph_file):
            try:
                with open(self.graph_file, 'r') as f:
                    data = json.load(f)
                    self.graph = nx.node_link_graph(data)
                logger.info(f"Loaded graph data from {self.graph_file}")
            except Exception as e:
                logger.error(f"Failed to load graph data: {e}")
    
    def _save_graph_data(self):
        """Save graph data to JSON file."""
        try:
            data = nx.node_link_data(self.graph)
            with open(self.graph_file, 'w') as f:
                json.dump(data, f)
            logger.info(f"Saved graph data to {self.graph_file}")
        except Exception as e:
            logger.error(f"Failed to save graph data: {e}")
    
    def add_asset(self, asset_id: str, properties: Dict[str, Any]):
        """
        Add an asset to both NetworkX and Neo4j graphs.
        
        Args:
            asset_id: Unique identifier for the asset
            properties: Dictionary of asset properties
        """
        # Add to NetworkX
        self.graph.add_node(asset_id, **properties)
        
        # Add to Neo4j if available
        if self.driver:
            try:
                with self.driver.session() as session:
                    session.run(
                        "MERGE (a:Asset {id: $id}) SET a += $props",
                        id=asset_id,
                        props=properties
                    )
            except Exception as e:
                logger.error(f"Failed to add asset to Neo4j: {e}")
        
        # Save NetworkX graph
        self._save_graph_data()
    
    def add_relationship(
        self,
        source_id: str,
        target_id: str,
        relation_type: str,
        properties: Optional[Dict[str, Any]] = None
    ):
        """
        Add a relationship between assets in both graphs.
        
        Args:
            source_id: Source asset ID
            target_id: Target asset ID
            relation_type: Type of relationship
            properties: Optional relationship properties
        """
        if properties is None:
            properties = {}
        
        # Add to NetworkX
        self.graph.add_edge(source_id, target_id, relation_type=relation_type, **properties)
        
        # Add to Neo4j if available
        if self.driver:
            try:
                with self.driver.session() as session:
                    session.run(
                        f"MATCH (a:Asset {{id: $source}}), (b:Asset {{id: $target}}) "
                        f"MERGE (a)-[r:{relation_type}]->(b) SET r += $props",
                        source=source_id,
                        target=target_id,
                        props=properties
                    )
            except Exception as e:
                logger.error(f"Failed to add relationship to Neo4j: {e}")
        
        # Save NetworkX graph
        self._save_graph_data()
    
    def get_asset(self, asset_id: str) -> Optional[Dict[str, Any]]:
        """
        Get asset information from NetworkX graph.
        
        Args:
            asset_id: Asset ID to retrieve
            
        Returns:
            Dictionary of asset properties or None if not found
        """
        if asset_id in self.graph:
            return dict(self.graph.nodes[asset_id])
        return None
    
    def get_asset_relationships(
        self,
        asset_id: str,
        direction: str = "both"
    ) -> List[Dict[str, Any]]:
        """
        Get relationships for an asset from NetworkX graph.
        
        Args:
            asset_id: Asset ID to get relationships for
            direction: "in", "out", or "both"
            
        Returns:
            List of relationship dictionaries
        """
        relationships = []
        
        if direction in ["out", "both"]:
            for target in self.graph.successors(asset_id):
                edge_data = self.graph.get_edge_data(asset_id, target)
                relationships.append({
                    "source": asset_id,
                    "target": target,
                    "type": edge_data.get("relation_type", "UNKNOWN"),
                    "direction": "out",
                    "properties": {k: v for k, v in edge_data.items() if k != "relation_type"}
                })
        
        if direction in ["in", "both"]:
            for source in self.graph.predecessors(asset_id):
                edge_data = self.graph.get_edge_data(source, asset_id)
                relationships.append({
                    "source": source,
                    "target": asset_id,
                    "type": edge_data.get("relation_type", "UNKNOWN"),
                    "direction": "in",
                    "properties": {k: v for k, v in edge_data.items() if k != "relation_type"}
                })
        
        return relationships
    
    def get_asset_path(
        self,
        source_id: str,
        target_id: str,
        max_depth: int = 3
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Find a path between two assets using NetworkX.
        
        Args:
            source_id: Source asset ID
            target_id: Target asset ID
            max_depth: Maximum path length to search
            
        Returns:
            List of nodes and edges in the path, or None if no path found
        """
        try:
            path = nx.shortest_path(
                self.graph,
                source=source_id,
                target=target_id,
                cutoff=max_depth
            )
            
            # Convert path to list of nodes and edges
            result = []
            for i in range(len(path) - 1):
                source = path[i]
                target = path[i + 1]
                edge_data = self.graph.get_edge_data(source, target)
                
                result.append({
                    "node": dict(self.graph.nodes[source]),
                    "edge": {
                        "type": edge_data.get("relation_type", "UNKNOWN"),
                        "properties": {k: v for k, v in edge_data.items() if k != "relation_type"}
                    }
                })
            
            # Add the final node
            result.append({
                "node": dict(self.graph.nodes[path[-1]]),
                "edge": None
            })
            
            return result
        except nx.NetworkXNoPath:
            return None
    
    def sync_to_neo4j(self):
        """
        Synchronize the entire NetworkX graph to Neo4j.
        This is useful for recovery or initial setup.
        """
        if not self.driver:
            logger.error("Cannot sync to Neo4j: No connection available")
            return
        
        try:
            with self.driver.session() as session:
                # Clear existing data
                session.run("MATCH (n) DETACH DELETE n")
                
                # Add all nodes
                for node_id, properties in self.graph.nodes(data=True):
                    session.run(
                        "CREATE (a:Asset {id: $id}) SET a += $props",
                        id=node_id,
                        props=properties
                    )
                
                # Add all edges
                for source, target, data in self.graph.edges(data=True):
                    relation_type = data.get("relation_type", "RELATES_TO")
                    properties = {k: v for k, v in data.items() if k != "relation_type"}
                    
                    session.run(
                        f"MATCH (a:Asset {{id: $source}}), (b:Asset {{id: $target}}) "
                        f"CREATE (a)-[r:{relation_type}]->(b) SET r += $props",
                        source=source,
                        target=target,
                        props=properties
                    )
                
            logger.info("Successfully synchronized graph to Neo4j")
        except Exception as e:
            logger.error(f"Failed to sync to Neo4j: {e}")
    
    def close(self):
        """Close Neo4j connection and save NetworkX graph."""
        if self.driver:
            self.driver.close()
        self._save_graph_data() 