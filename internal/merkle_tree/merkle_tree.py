"""
Core Merkle Tree Implementation for Cloud Asset Tracking

This module provides the fundamental Merkle tree data structure for efficiently
tracking cloud infrastructure states and detecting drift.
"""

import hashlib
import json
from typing import Dict, List, Optional, Union, Any, Set
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime


class NodeType(Enum):
    """Types of nodes in the Merkle tree"""
    ROOT = "root"
    PROVIDER = "provider"  # AWS, GCP, Azure
    SERVICE = "service"    # EC2, S3, Compute Engine, etc.
    RESOURCE = "resource"  # Individual cloud resources
    LEAF = "leaf"         # Actual asset data


@dataclass
class MerkleNode:
    """
    A node in the Merkle tree representing cloud infrastructure state
    
    Each node contains:
    - hash: SHA-256 hash of the node's content
    - node_type: Type of cloud entity this node represents
    - identifier: Unique identifier (resource ID, service name, etc.)
    - metadata: Additional information about the cloud asset
    - children: Child nodes in the tree
    - parent_hash: Hash of the parent node for verification
    """
    hash: str
    node_type: NodeType
    identifier: str
    metadata: Dict[str, Any]
    children: List['MerkleNode']
    parent_hash: Optional[str] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()
    
    def add_child(self, child: 'MerkleNode') -> None:
        """Add a child node and update its parent hash"""
        child.parent_hash = self.hash
        self.children.append(child)
        # Recompute hash after adding child
        self._recompute_hash()
    
    def remove_child(self, child_hash: str) -> bool:
        """Remove a child node by hash"""
        for i, child in enumerate(self.children):
            if child.hash == child_hash:
                del self.children[i]
                self._recompute_hash()
                return True
        return False
    
    def _recompute_hash(self) -> None:
        """Recompute the hash for this node based on its content and children"""
        content = {
            'node_type': self.node_type.value,
            'identifier': self.identifier,
            'metadata': self.metadata,
            'children_hashes': [child.hash for child in self.children],
            'parent_hash': self.parent_hash
        }
        
        # Create deterministic hash
        content_str = json.dumps(content, sort_keys=True, separators=(',', ':'))
        self.hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()
    
    def find_child(self, identifier: str) -> Optional['MerkleNode']:
        """Find a direct child by identifier"""
        for child in self.children:
            if child.identifier == identifier:
                return child
        return None
    
    def find_descendant(self, path: List[str]) -> Optional['MerkleNode']:
        """Find a descendant node by following a path of identifiers"""
        if not path:
            return self
        
        child = self.find_child(path[0])
        if child is None:
            return None
        
        if len(path) == 1:
            return child
        
        return child.find_descendant(path[1:])
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary for serialization"""
        return {
            'hash': self.hash,
            'node_type': self.node_type.value,
            'identifier': self.identifier,
            'metadata': self.metadata,
            'children': [child.to_dict() for child in self.children],
            'parent_hash': self.parent_hash,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MerkleNode':
        """Create node from dictionary"""
        children = [cls.from_dict(child_data) for child_data in data.get('children', [])]
        
        timestamp = None
        if data.get('timestamp'):
            timestamp = datetime.fromisoformat(data['timestamp'])
        
        return cls(
            hash=data['hash'],
            node_type=NodeType(data['node_type']),
            identifier=data['identifier'],
            metadata=data['metadata'],
            children=children,
            parent_hash=data.get('parent_hash'),
            timestamp=timestamp
        )


class MerkleTree:
    """
    Merkle Tree for Cloud Infrastructure State Tracking
    
    This tree structure allows for efficient comparison of cloud infrastructure
    states to detect drift, unauthorized changes, and resource modifications.
    """
    
    def __init__(self, root_identifier: str = "cloud_infrastructure"):
        """Initialize with a root node representing the entire cloud infrastructure"""
        self.root = MerkleNode(
            hash="",
            node_type=NodeType.ROOT,
            identifier=root_identifier,
            metadata={"created_at": datetime.utcnow().isoformat()},
            children=[]
        )
        self.root._recompute_hash()
        self._node_cache: Dict[str, MerkleNode] = {self.root.hash: self.root}
    
    def add_provider(self, provider_name: str, metadata: Dict[str, Any] = None) -> MerkleNode:
        """Add a cloud provider (AWS, GCP, Azure) to the tree"""
        if metadata is None:
            metadata = {}
        
        # Check if provider already exists
        existing = self.root.find_child(provider_name)
        if existing:
            return existing
        
        provider_node = MerkleNode(
            hash="",
            node_type=NodeType.PROVIDER,
            identifier=provider_name,
            metadata={
                "provider": provider_name,
                **metadata
            },
            children=[]
        )
        provider_node._recompute_hash()
        
        self.root.add_child(provider_node)
        self._node_cache[provider_node.hash] = provider_node
        
        return provider_node
    
    def add_service(self, provider_name: str, service_name: str, metadata: Dict[str, Any] = None) -> MerkleNode:
        """Add a cloud service (EC2, S3, etc.) under a provider"""
        if metadata is None:
            metadata = {}
        
        provider_node = self.root.find_child(provider_name)
        if not provider_node:
            provider_node = self.add_provider(provider_name)
        
        # Check if service already exists
        existing = provider_node.find_child(service_name)
        if existing:
            return existing
        
        service_node = MerkleNode(
            hash="",
            node_type=NodeType.SERVICE,
            identifier=service_name,
            metadata={
                "provider": provider_name,
                "service": service_name,
                **metadata
            },
            children=[]
        )
        service_node._recompute_hash()
        
        provider_node.add_child(service_node)
        self._node_cache[service_node.hash] = service_node
        
        return service_node
    
    def add_resource(self, provider_name: str, service_name: str, resource_id: str, 
                    resource_data: Dict[str, Any]) -> MerkleNode:
        """Add a cloud resource under a service"""
        service_node = self.root.find_descendant([provider_name, service_name])
        if not service_node:
            service_node = self.add_service(provider_name, service_name)
        
        # Check if resource already exists and update it
        existing = service_node.find_child(resource_id)
        if existing:
            # Update existing resource
            existing.metadata.update(resource_data)
            existing.timestamp = datetime.utcnow()
            existing._recompute_hash()
            return existing
        
        resource_node = MerkleNode(
            hash="",
            node_type=NodeType.RESOURCE,
            identifier=resource_id,
            metadata={
                "provider": provider_name,
                "service": service_name,
                "resource_id": resource_id,
                **resource_data
            },
            children=[]
        )
        resource_node._recompute_hash()
        
        service_node.add_child(resource_node)
        self._node_cache[resource_node.hash] = resource_node
        
        return resource_node
    
    def remove_resource(self, provider_name: str, service_name: str, resource_id: str) -> bool:
        """Remove a resource from the tree"""
        service_node = self.root.find_descendant([provider_name, service_name])
        if not service_node:
            return False
        
        resource_node = service_node.find_child(resource_id)
        if not resource_node:
            return False
        
        # Remove from cache
        if resource_node.hash in self._node_cache:
            del self._node_cache[resource_node.hash]
        
        return service_node.remove_child(resource_node.hash)
    
    def get_node_by_hash(self, node_hash: str) -> Optional[MerkleNode]:
        """Retrieve a node by its hash"""
        return self._node_cache.get(node_hash)
    
    def get_resource(self, provider_name: str, service_name: str, resource_id: str) -> Optional[MerkleNode]:
        """Get a specific resource node"""
        return self.root.find_descendant([provider_name, service_name, resource_id])
    
    def get_all_resources(self, provider_name: str = None, service_name: str = None) -> List[MerkleNode]:
        """Get all resources, optionally filtered by provider and/or service"""
        resources = []
        
        def traverse(node: MerkleNode):
            if node.node_type == NodeType.RESOURCE:
                # Apply filters
                if provider_name and node.metadata.get('provider') != provider_name:
                    return
                if service_name and node.metadata.get('service') != service_name:
                    return
                resources.append(node)
            
            for child in node.children:
                traverse(child)
        
        traverse(self.root)
        return resources
    
    def compare_trees(self, other: 'MerkleTree') -> Dict[str, List[str]]:
        """
        Compare this tree with another tree to detect changes
        
        Returns:
            Dict with 'added', 'removed', 'modified' lists of resource paths
        """
        changes = {
            'added': [],
            'removed': [],
            'modified': []
        }
        
        current_resources = {f"{r.metadata.get('provider', '')}/{r.metadata.get('service', '')}/{r.identifier}": r 
                           for r in self.get_all_resources()}
        other_resources = {f"{r.metadata.get('provider', '')}/{r.metadata.get('service', '')}/{r.identifier}": r 
                          for r in other.get_all_resources()}
        
        # Find added resources
        for path in other_resources:
            if path not in current_resources:
                changes['added'].append(path)
        
        # Find removed resources
        for path in current_resources:
            if path not in other_resources:
                changes['removed'].append(path)
        
        # Find modified resources
        for path in current_resources:
            if path in other_resources:
                if current_resources[path].hash != other_resources[path].hash:
                    changes['modified'].append(path)
        
        return changes
    
    def get_state_fingerprint(self) -> str:
        """Get the root hash representing the entire infrastructure state"""
        return self.root.hash
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize the entire tree to a dictionary"""
        return {
            'root': self.root.to_dict(),
            'metadata': {
                'created_at': datetime.utcnow().isoformat(),
                'total_nodes': len(self._node_cache)
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MerkleTree':
        """Deserialize a tree from a dictionary"""
        tree = cls.__new__(cls)
        tree.root = MerkleNode.from_dict(data['root'])
        tree._node_cache = {}
        
        # Rebuild cache
        def rebuild_cache(node: MerkleNode):
            tree._node_cache[node.hash] = node
            for child in node.children:
                rebuild_cache(child)
        
        rebuild_cache(tree.root)
        return tree
    
    def save_to_file(self, filepath: str) -> None:
        """Save the tree to a JSON file"""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filepath: str) -> 'MerkleTree':
        """Load a tree from a JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
    
    def print_tree(self, max_depth: int = None) -> None:
        """Print a visual representation of the tree"""
        def print_node(node: MerkleNode, depth: int = 0, prefix: str = ""):
            if max_depth is not None and depth > max_depth:
                return
            
            indent = "  " * depth
            type_symbol = {
                NodeType.ROOT: "🌍",
                NodeType.PROVIDER: "☁️",
                NodeType.SERVICE: "⚙️", 
                NodeType.RESOURCE: "📦"
            }.get(node.node_type, "📄")
            
            print(f"{indent}{prefix}{type_symbol} {node.identifier} ({node.hash[:8]}...)")
            
            for i, child in enumerate(node.children):
                is_last = i == len(node.children) - 1
                child_prefix = "└── " if is_last else "├── "
                print_node(child, depth + 1, child_prefix)
        
        print_node(self.root) 