"""
Merkle Tree Implementation for Saturn AI Assistant

Features:
- Cloud resource state hashing (AWS, GCP, Azure)
- Infrastructure drift detection  
- Efficient state comparison and change tracking
- Tree serialization/deserialization for persistence
- Support for multi-cloud asset fingerprinting
"""

from .merkle_tree import MerkleTree, MerkleNode
from .asset_hasher import FileAssetHasher, AssetHashingStrategy, create_asset_hasher
from .drift_detector import DriftDetector

__all__ = [
    'MerkleTree',
    'MerkleNode', 
    'AssetHasher',
    'CloudAssetHashingStrategy',
    'DriftDetector'
]

__version__ = '1.0.0' 