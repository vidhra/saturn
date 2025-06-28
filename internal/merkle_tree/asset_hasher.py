"""
Asset Hasher for File-Based Resources

This module provides consistent hashing strategies for different types of asset files
to ensure reliable drift detection and state comparison. Works with any file format
and is vendor/cloud agnostic.
"""

import hashlib
import json
import yaml
import os
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Union
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
import re


class FileFormat(Enum):
    """Supported file formats"""
    JSON = "json"
    YAML = "yaml" 
    YML = "yml"
    TEXT = "text"
    UNKNOWN = "unknown"


class AssetHashingStrategy(ABC):
    """Abstract base class for asset hashing strategies"""
    
    @abstractmethod
    def normalize_content(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize asset content for consistent hashing"""
        pass
    
    @abstractmethod
    def get_ignored_fields(self) -> Set[str]:
        """Get the set of fields that should be ignored during hashing (timestamps, etc.)"""
        pass


class GenericAssetHashingStrategy(AssetHashingStrategy):
    """Generic hashing strategy for any asset file"""
    
    def __init__(self, ignore_timestamps: bool = True, ignore_metadata: bool = True):
        self.ignore_timestamps = ignore_timestamps
        self.ignore_metadata = ignore_metadata
    
    def normalize_content(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize asset content for consistent hashing"""
        normalized = {}
        
        # Sort keys and handle nested structures
        for key, value in sorted(content.items()):
            if key in self.get_ignored_fields():
                continue
                
            # Skip timestamp fields if configured
            if self.ignore_timestamps and self._is_timestamp_field(key, value):
                continue
            
            # Normalize lists (sort them for consistency)
            if isinstance(value, list):
                normalized[key] = self._normalize_list(value)
            
            # Normalize dictionaries recursively
            elif isinstance(value, dict):
                normalized[key] = self._normalize_dict(value)
            
            # Convert everything else to string for consistency
            else:
                normalized[key] = str(value) if value is not None else ""
        
        return normalized
    
    def get_ignored_fields(self) -> Set[str]:
        """Get fields that should be ignored during hashing"""
        ignored = set()
        
        if self.ignore_metadata:
            # Common metadata fields across different systems
            ignored.update({
                'metadata', 'meta', '_metadata',
                'etag', 'version', 'generation', 'metageneration',
                'selfLink', 'id', 'uid', 'resourceVersion',
                'lastModified', 'lastUpdate', 'updated', 'modified',
                'creationTimestamp', 'createTime', 'created',
                'state', 'status', 'phase', 'conditions'
            })
        
        if self.ignore_timestamps:
            ignored.update({
                'timestamp', 'time', 'date',
                'createdAt', 'updatedAt', 'deletedAt',
                'lastAccessed', 'lastUsed', 'lastSeen'
            })
        
        return ignored
    
    def _normalize_list(self, items: List[Any]) -> List[Any]:
        """Normalize list items"""
        normalized_items = []
        for item in items:
            if isinstance(item, dict):
                normalized_items.append(self._normalize_dict(item))
            elif isinstance(item, list):
                normalized_items.append(self._normalize_list(item))
            else:
                normalized_items.append(str(item) if item is not None else "")
        
        # Sort for consistency (convert to strings for sorting if needed)
        try:
            return sorted(normalized_items)
        except TypeError:
            # If items are not comparable, convert to strings and sort
            return sorted([str(item) for item in normalized_items])
    
    def _normalize_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively normalize dictionary"""
        normalized = {}
        for key, value in sorted(data.items()):
            if key in self.get_ignored_fields():
                continue
                
            if isinstance(value, dict):
                normalized_value = self._normalize_dict(value)
                if normalized_value:  # Only include non-empty dicts
                    normalized[key] = normalized_value
            elif isinstance(value, list):
                normalized[key] = self._normalize_list(value)
            else:
                normalized[key] = str(value) if value is not None else ""
        return normalized
    
    def _is_timestamp_field(self, key: str, value: Any) -> bool:
        """Check if a field contains timestamp data"""
        if not isinstance(value, (str, int, float)):
            return False
        
        # Check key name patterns
        timestamp_key_patterns = [
            r'.*time.*', r'.*date.*', r'.*timestamp.*',
            r'.*created.*', r'.*updated.*', r'.*modified.*'
        ]
        
        key_lower = key.lower()
        if any(re.match(pattern, key_lower, re.IGNORECASE) for pattern in timestamp_key_patterns):
            return True
        
        # Check value patterns for timestamps
        if isinstance(value, str):
            timestamp_patterns = [
                r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',  # ISO format
                r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',   # SQL format
                r'\d{4}/\d{2}/\d{2}',                     # Date format
            ]
            return any(re.match(pattern, str(value)) for pattern in timestamp_patterns)
        
        # Check for Unix timestamps (10-13 digits)
        if isinstance(value, (int, float)) and 1000000000 <= value <= 9999999999999:
            return True
        
        return False


class FileAssetHasher:
    """File-based asset hasher that works with any file format"""
    
    def __init__(self, strategy: AssetHashingStrategy = None):
        self.strategy = strategy or GenericAssetHashingStrategy()
    
    def hash_file(self, file_path: Union[str, Path]) -> str:
        """Hash a file and return the hash string"""
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"Asset file not found: {file_path}")
        
        # Get file format
        file_format = self._detect_file_format(file_path)
        
        # Read and parse file content
        content = self._read_file_content(file_path, file_format)
        
        # Include file metadata in hash
        file_info = {
            'name': file_path.name,
            'size': file_path.stat().st_size,
            'format': file_format.value,
            'content': content
        }
        
        return self.hash_content(file_info)
    
    def hash_content(self, content: Dict[str, Any]) -> str:
        """Hash arbitrary content and return the hash string"""
        # Normalize the content
        normalized = self.strategy.normalize_content(content)
        
        # Convert to JSON string with sorted keys for consistency
        content_str = json.dumps(normalized, sort_keys=True, separators=(',', ':'))
        
        # Generate SHA-256 hash
        return hashlib.sha256(content_str.encode('utf-8')).hexdigest()
    
    def compare_files(self, file1: Union[str, Path], file2: Union[str, Path]) -> Dict[str, Any]:
        """Compare two files and return detailed comparison"""
        file1_path = Path(file1)
        file2_path = Path(file2)
        
        # Hash both files
        hash1 = self.hash_file(file1_path)
        hash2 = self.hash_file(file2_path)
        
        # Read content for detailed comparison
        format1 = self._detect_file_format(file1_path)
        format2 = self._detect_file_format(file2_path)
        
        content1 = self._read_file_content(file1_path, format1)
        content2 = self._read_file_content(file2_path, format2)
        
        return {
            'files_identical': hash1 == hash2,
            'hash1': hash1,
            'hash2': hash2,
            'file1': str(file1_path),
            'file2': str(file2_path),
            'format1': format1.value,
            'format2': format2.value,
            'content_diff': self._get_content_diff(content1, content2),
            'comparison_time': datetime.now().isoformat()
        }
    
    def get_file_fingerprint(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Get a detailed fingerprint of a file"""
        file_path = Path(file_path)
        file_format = self._detect_file_format(file_path)
        content = self._read_file_content(file_path, file_format)
        
        # Get file stats
        stats = file_path.stat()
        
        return {
            'path': str(file_path),
            'name': file_path.name,
            'format': file_format.value,
            'size': stats.st_size,
            'hash': self.hash_file(file_path),
            'content_hash': self.hash_content(content),
            'structure_summary': self._get_structure_summary(content),
            'fingerprint_time': datetime.now().isoformat()
        }
    
    def _detect_file_format(self, file_path: Path) -> FileFormat:
        """Detect the format of a file based on extension and content"""
        suffix = file_path.suffix.lower()
        
        if suffix == '.json':
            return FileFormat.JSON
        elif suffix in ['.yaml', '.yml']:
            return FileFormat.YAML
        elif suffix == '.yml':
            return FileFormat.YML
        else:
            # Try to detect by content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content.startswith(('{', '[')):
                        return FileFormat.JSON
                    elif content.startswith(('---', 'apiVersion:', 'kind:')):
                        return FileFormat.YAML
            except:
                pass
            
            return FileFormat.TEXT
    
    def _read_file_content(self, file_path: Path, file_format: FileFormat) -> Any:
        """Read and parse file content based on format"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if file_format == FileFormat.JSON:
                return json.loads(content)
            elif file_format in [FileFormat.YAML, FileFormat.YML]:
                return yaml.safe_load(content)
            else:
                # Return as text for non-structured formats
                return {'text_content': content}
                
        except Exception as e:
            # If parsing fails, return raw content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return {'raw_content': f.read(), 'parse_error': str(e)}
    
    def _get_content_diff(self, content1: Any, content2: Any) -> Dict[str, Any]:
        """Get differences between two content objects"""
        if content1 == content2:
            return {'has_differences': False}
        
        diff_info = {'has_differences': True}
        
        if isinstance(content1, dict) and isinstance(content2, dict):
            # Find added, removed, and changed keys
            keys1 = set(content1.keys())
            keys2 = set(content2.keys())
            
            diff_info.update({
                'added_keys': list(keys2 - keys1),
                'removed_keys': list(keys1 - keys2),
                'common_keys': list(keys1 & keys2),
                'changed_values': []
            })
            
            # Check for changed values in common keys
            for key in keys1 & keys2:
                if content1[key] != content2[key]:
                    diff_info['changed_values'].append(key)
        
        return diff_info
    
    def _get_structure_summary(self, content: Any) -> Dict[str, Any]:
        """Get a summary of the content structure"""
        if isinstance(content, dict):
            return {
                'type': 'dict',
                'key_count': len(content),
                'keys': list(content.keys())[:10],  # First 10 keys
                'nested_levels': self._count_nested_levels(content)
            }
        elif isinstance(content, list):
            return {
                'type': 'list',
                'item_count': len(content),
                'item_types': list(set(type(item).__name__ for item in content[:10]))
            }
        else:
            return {
                'type': type(content).__name__,
                'value_preview': str(content)[:100] if content else None
            }
    
    def _count_nested_levels(self, obj: Any, current_level: int = 0) -> int:
        """Count the maximum nesting level in a data structure"""
        if isinstance(obj, dict):
            if not obj:
                return current_level
            return max(self._count_nested_levels(v, current_level + 1) for v in obj.values())
        elif isinstance(obj, list):
            if not obj:
                return current_level
            return max(self._count_nested_levels(item, current_level + 1) for item in obj)
        else:
            return current_level


# Factory function for easy usage
def create_asset_hasher(ignore_timestamps: bool = True, ignore_metadata: bool = True) -> FileAssetHasher:
    """Create a file asset hasher with the specified configuration"""
    strategy = GenericAssetHashingStrategy(
        ignore_timestamps=ignore_timestamps,
        ignore_metadata=ignore_metadata
    )
    return FileAssetHasher(strategy)


# Convenience functions
def hash_asset_file(file_path: Union[str, Path]) -> str:
    """Quick function to hash a single asset file"""
    hasher = create_asset_hasher()
    return hasher.hash_file(file_path)


def compare_asset_files(file1: Union[str, Path], file2: Union[str, Path]) -> Dict[str, Any]:
    """Quick function to compare two asset files"""
    hasher = create_asset_hasher()
    return hasher.compare_files(file1, file2)
