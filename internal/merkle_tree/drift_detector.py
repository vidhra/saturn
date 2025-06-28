"""
Cloud Infrastructure Drift Detector

This module provides high-level drift detection capabilities using Merkle trees
to efficiently track and compare cloud infrastructure states over time.
"""

import os
import json
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass
from enum import Enum

from .merkle_tree import MerkleTree, MerkleNode, NodeType
from .asset_hasher import FileAssetHasher, create_asset_hasher


class DriftSeverity(Enum):
    """Severity levels for drift detection"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ChangeType(Enum):
    """Types of changes detected"""
    ADDED = "added"
    REMOVED = "removed"
    MODIFIED = "modified"
    UNCHANGED = "unchanged"


@dataclass
class DriftAlert:
    """Represents a drift detection alert"""
    resource_path: str
    change_type: ChangeType
    severity: DriftSeverity
    provider: str
    service: str
    resource_id: str
    details: Dict[str, Any]
    timestamp: datetime
    old_hash: Optional[str] = None
    new_hash: Optional[str] = None


@dataclass
class DriftSummary:
    """Summary of drift detection results"""
    total_resources: int
    unchanged_resources: int
    added_resources: int
    removed_resources: int
    modified_resources: int
    critical_alerts: int
    high_severity_alerts: int
    medium_severity_alerts: int
    low_severity_alerts: int
    scan_timestamp: datetime
    scan_duration: float
    alerts: List[DriftAlert]


class DriftDetector:
    """
    Cloud Infrastructure Drift Detector
    
    Manages Merkle trees representing cloud infrastructure state and provides
    efficient drift detection by comparing tree states over time.
    """
    
    def __init__(self, cache_dir: str = None):
        """
        Initialize the drift detector
        
        Args:
            cache_dir: Directory to store Merkle tree snapshots
        """
        self.cache_dir = cache_dir or os.path.join(os.getcwd(), '.saturn_drift_cache')
        self.asset_hasher = create_asset_hasher()
        self.current_tree: Optional[MerkleTree] = None
        self.previous_tree: Optional[MerkleTree] = None
        
        # Ensure cache directory exists
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Configuration for drift severity assessment
        self.severity_config = {
            'critical_services': {'iam', 'security', 'kms', 'secrets'},
            'critical_changes': {
                'aws': {
                    'ec2': ['SecurityGroups', 'IamInstanceProfile', 'KeyName'],
                    's3': ['PublicAccessBlock', 'Encryption'],
                    'iam': ['PolicyDocument', 'AssumeRolePolicyDocument'],
                    'rds': ['VpcSecurityGroups', 'PubliclyAccessible']
                },
                'gcp': {
                    'compute': ['serviceAccounts', 'networkInterfaces'],
                    'storage': ['encryption', 'iamConfiguration'],
                    'sql': ['ipConfiguration', 'settings.userLabels']
                },
                'azure': {
                    'virtualmachines': ['osProfile', 'networkProfile'],
                    'storage': ['encryption', 'networkAcls']
                }
            }
        }
    
    def create_infrastructure_snapshot(self, cloud_assets: Dict[str, Dict[str, List[Dict[str, Any]]]]) -> MerkleTree:
        """
        Create a Merkle tree snapshot of current cloud infrastructure
        
        Args:
            cloud_assets: Nested dict structure:
                {
                    'provider_name': {
                        'service_name': [
                            {'resource_id': 'id', 'data': {...}},
                            ...
                        ]
                    }
                }
        
        Returns:
            MerkleTree representing the current infrastructure state
        """
        tree = MerkleTree(f"infrastructure_snapshot_{datetime.utcnow().isoformat()}")
        
        for provider_name, services in cloud_assets.items():
            provider_node = tree.add_provider(provider_name, {
                'total_services': len(services),
                'scan_timestamp': datetime.utcnow().isoformat()
            })
            
            for service_name, resources in services.items():
                service_node = tree.add_service(provider_name, service_name, {
                    'total_resources': len(resources),
                    'service_type': service_name
                })
                
                for resource in resources:
                    resource_id = resource.get('resource_id') or resource.get('id', 'unknown')
                    resource_data = resource.get('data', resource)
                    
                    # Create normalized hash for the resource
                    resource_content = {
                        'provider': provider_name,
                        'service': service_name,
                        'resource_id': resource_id,
                        'data': resource_data
                    }
                    asset_hash = self.asset_hasher.hash_content(resource_content)
                    
                    # Add resource to tree with hash and metadata
                    tree.add_resource(provider_name, service_name, resource_id, {
                        'asset_hash': asset_hash,
                        'raw_data': resource_data,
                        'last_updated': datetime.utcnow().isoformat(),
                        'resource_type': resource_data.get('type', service_name)
                    })
        
        return tree
    
    def save_snapshot(self, tree: MerkleTree, snapshot_name: str = None) -> str:
        """
        Save a Merkle tree snapshot to disk
        
        Args:
            tree: MerkleTree to save
            snapshot_name: Optional custom name, defaults to timestamp
            
        Returns:
            Path to saved snapshot file
        """
        if snapshot_name is None:
            snapshot_name = f"snapshot_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        
        snapshot_path = os.path.join(self.cache_dir, f"{snapshot_name}.json")
        tree.save_to_file(snapshot_path)
        
        # Also save a metadata file
        metadata = {
            'snapshot_name': snapshot_name,
            'created_at': datetime.utcnow().isoformat(),
            'root_hash': tree.get_state_fingerprint(),
            'total_resources': len(tree.get_all_resources()),
            'providers': list(set(r.metadata.get('provider') for r in tree.get_all_resources())),
            'services': list(set(r.metadata.get('service') for r in tree.get_all_resources()))
        }
        
        metadata_path = os.path.join(self.cache_dir, f"{snapshot_name}_metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return snapshot_path
    
    def load_snapshot(self, snapshot_name: str) -> MerkleTree:
        """Load a Merkle tree snapshot from disk"""
        snapshot_path = os.path.join(self.cache_dir, f"{snapshot_name}.json")
        if not os.path.exists(snapshot_path):
            raise FileNotFoundError(f"Snapshot not found: {snapshot_path}")
        
        return MerkleTree.load_from_file(snapshot_path)
    
    def list_snapshots(self) -> List[Dict[str, Any]]:
        """List all available snapshots with metadata"""
        snapshots = []
        
        for filename in os.listdir(self.cache_dir):
            if filename.endswith('_metadata.json'):
                metadata_path = os.path.join(self.cache_dir, filename)
                try:
                    with open(metadata_path, 'r') as f:
                        metadata = json.load(f)
                    snapshots.append(metadata)
                except Exception:
                    continue
        
        # Sort by creation time (newest first)
        snapshots.sort(key=lambda x: x.get('created_at', ''), reverse=True)
        return snapshots
    
    def detect_drift(self, current_assets: Dict[str, Dict[str, List[Dict[str, Any]]]] = None,
                    baseline_snapshot: str = None) -> DriftSummary:
        """
        Detect drift between current infrastructure and a baseline
        
        Args:
            current_assets: Current infrastructure state (if None, uses self.current_tree)
            baseline_snapshot: Name of baseline snapshot (if None, uses most recent)
            
        Returns:
            DriftSummary with detailed drift information
        """
        start_time = datetime.utcnow()
        
        # Get or create current tree
        if current_assets:
            current_tree = self.create_infrastructure_snapshot(current_assets)
            self.current_tree = current_tree
        elif self.current_tree:
            current_tree = self.current_tree
        else:
            raise ValueError("No current infrastructure state available")
        
        # Get baseline tree
        if baseline_snapshot:
            baseline_tree = self.load_snapshot(baseline_snapshot)
        elif self.previous_tree:
            baseline_tree = self.previous_tree
        else:
            # Use most recent snapshot as baseline
            snapshots = self.list_snapshots()
            if not snapshots:
                raise ValueError("No baseline snapshot available")
            baseline_tree = self.load_snapshot(snapshots[0]['snapshot_name'])
        
        # Compare trees to find changes
        changes = current_tree.compare_trees(baseline_tree)
        alerts = []
        
        # Analyze added resources
        for resource_path in changes['added']:
            alert = self._create_alert_for_added_resource(current_tree, resource_path)
            if alert:
                alerts.append(alert)
        
        # Analyze removed resources
        for resource_path in changes['removed']:
            alert = self._create_alert_for_removed_resource(baseline_tree, resource_path)
            if alert:
                alerts.append(alert)
        
        # Analyze modified resources
        for resource_path in changes['modified']:
            alert = self._create_alert_for_modified_resource(
                current_tree, baseline_tree, resource_path
            )
            if alert:
                alerts.append(alert)
        
        # Calculate summary statistics
        total_resources = len(current_tree.get_all_resources())
        scan_duration = (datetime.utcnow() - start_time).total_seconds()
        
        severity_counts = {
            DriftSeverity.CRITICAL: len([a for a in alerts if a.severity == DriftSeverity.CRITICAL]),
            DriftSeverity.HIGH: len([a for a in alerts if a.severity == DriftSeverity.HIGH]),
            DriftSeverity.MEDIUM: len([a for a in alerts if a.severity == DriftSeverity.MEDIUM]),
            DriftSeverity.LOW: len([a for a in alerts if a.severity == DriftSeverity.LOW])
        }
        
        return DriftSummary(
            total_resources=total_resources,
            unchanged_resources=total_resources - len(changes['added']) - len(changes['removed']) - len(changes['modified']),
            added_resources=len(changes['added']),
            removed_resources=len(changes['removed']),
            modified_resources=len(changes['modified']),
            critical_alerts=severity_counts[DriftSeverity.CRITICAL],
            high_severity_alerts=severity_counts[DriftSeverity.HIGH],
            medium_severity_alerts=severity_counts[DriftSeverity.MEDIUM],
            low_severity_alerts=severity_counts[DriftSeverity.LOW],
            scan_timestamp=start_time,
            scan_duration=scan_duration,
            alerts=alerts
        )
    
    def _create_alert_for_added_resource(self, tree: MerkleTree, resource_path: str) -> Optional[DriftAlert]:
        """Create alert for a newly added resource"""
        parts = resource_path.split('/')
        if len(parts) != 3:
            return None
        
        provider, service, resource_id = parts
        resource_node = tree.get_resource(provider, service, resource_id)
        
        if not resource_node:
            return None
        
        severity = self._assess_severity_for_new_resource(provider, service, resource_node.metadata)
        
        return DriftAlert(
            resource_path=resource_path,
            change_type=ChangeType.ADDED,
            severity=severity,
            provider=provider,
            service=service,
            resource_id=resource_id,
            details={
                'message': f"New {service} resource detected",
                'resource_data': resource_node.metadata.get('raw_data', {})
            },
            timestamp=datetime.utcnow(),
            new_hash=resource_node.metadata.get('asset_hash')
        )
    
    def _create_alert_for_removed_resource(self, tree: MerkleTree, resource_path: str) -> Optional[DriftAlert]:
        """Create alert for a removed resource"""
        parts = resource_path.split('/')
        if len(parts) != 3:
            return None
        
        provider, service, resource_id = parts
        resource_node = tree.get_resource(provider, service, resource_id)
        
        if not resource_node:
            return None
        
        severity = self._assess_severity_for_removed_resource(provider, service, resource_node.metadata)
        
        return DriftAlert(
            resource_path=resource_path,
            change_type=ChangeType.REMOVED,
            severity=severity,
            provider=provider,
            service=service,
            resource_id=resource_id,
            details={
                'message': f"{service} resource was deleted",
                'resource_data': resource_node.metadata.get('raw_data', {})
            },
            timestamp=datetime.utcnow(),
            old_hash=resource_node.metadata.get('asset_hash')
        )
    
    def _create_alert_for_modified_resource(self, current_tree: MerkleTree, 
                                          baseline_tree: MerkleTree, resource_path: str) -> Optional[DriftAlert]:
        """Create alert for a modified resource"""
        parts = resource_path.split('/')
        if len(parts) != 3:
            return None
        
        provider, service, resource_id = parts
        current_resource = current_tree.get_resource(provider, service, resource_id)
        baseline_resource = baseline_tree.get_resource(provider, service, resource_id)
        
        if not current_resource or not baseline_resource:
            return None
        
        # Compare the actual resource data
        current_data = current_resource.metadata.get('raw_data', {})
        baseline_data = baseline_resource.metadata.get('raw_data', {})
        
        comparison = self._compare_resource_data(provider, service, baseline_data, current_data)
        severity = self._assess_severity_for_modified_resource(provider, service, comparison)
        
        return DriftAlert(
            resource_path=resource_path,
            change_type=ChangeType.MODIFIED,
            severity=severity,
            provider=provider,
            service=service,
            resource_id=resource_id,
            details={
                'message': f"{service} resource configuration changed",
                'changes': comparison.get('changed_fields', []),
                'critical_changes': comparison.get('critical_changed_fields', []),
                'has_critical_changes': comparison.get('has_critical_changes', False)
            },
            timestamp=datetime.utcnow(),
            old_hash=baseline_resource.metadata.get('asset_hash'),
            new_hash=current_resource.metadata.get('asset_hash')
        )
    
    def _compare_resource_data(self, provider: str, service: str, 
                              baseline_data: Dict[str, Any], current_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compare two resource data objects and return detailed comparison
        
        Args:
            provider: Cloud provider name
            service: Service name
            baseline_data: Original resource data
            current_data: Current resource data
            
        Returns:
            Dict containing comparison details
        """
        if baseline_data == current_data:
            return {
                'has_differences': False,
                'changed_fields': [],
                'critical_changed_fields': [],
                'has_critical_changes': False
            }
        
        # Find changed fields
        changed_fields = []
        critical_changed_fields = []
        
        def compare_nested(base_obj, curr_obj, path=""):
            """Recursively compare nested objects"""
            if isinstance(base_obj, dict) and isinstance(curr_obj, dict):
                all_keys = set(base_obj.keys()) | set(curr_obj.keys())
                for key in all_keys:
                    key_path = f"{path}.{key}" if path else key
                    
                    if key not in base_obj:
                        changed_fields.append({'field': key_path, 'change': 'added', 'new_value': curr_obj[key]})
                    elif key not in curr_obj:
                        changed_fields.append({'field': key_path, 'change': 'removed', 'old_value': base_obj[key]})
                    elif base_obj[key] != curr_obj[key]:
                        if isinstance(base_obj[key], (dict, list)):
                            compare_nested(base_obj[key], curr_obj[key], key_path)
                        else:
                            changed_fields.append({
                                'field': key_path, 
                                'change': 'modified',
                                'old_value': base_obj[key],
                                'new_value': curr_obj[key]
                            })
            elif isinstance(base_obj, list) and isinstance(curr_obj, list):
                if base_obj != curr_obj:
                    changed_fields.append({
                        'field': path or 'list_content',
                        'change': 'modified',
                        'old_value': f"list with {len(base_obj)} items",
                        'new_value': f"list with {len(curr_obj)} items"
                    })
            else:
                changed_fields.append({
                    'field': path or 'value',
                    'change': 'modified',
                    'old_value': base_obj,
                    'new_value': curr_obj
                })
        
        compare_nested(baseline_data, current_data)
        
        # Determine critical changes based on service type
        critical_fields = self.severity_config['critical_changes'].get(provider.lower(), {}).get(service.lower(), [])
        
        for change in changed_fields:
            field_name = change['field'].split('.')[-1]  # Get the last part of the path
            if field_name in critical_fields:
                critical_changed_fields.append(change)
        
        return {
            'has_differences': len(changed_fields) > 0,
            'changed_fields': changed_fields,
            'critical_changed_fields': critical_changed_fields,
            'has_critical_changes': len(critical_changed_fields) > 0
        }
    
    def _assess_severity_for_new_resource(self, provider: str, service: str, metadata: Dict[str, Any]) -> DriftSeverity:
        """Assess severity for a newly added resource"""
        # Critical services are always high severity
        if service.lower() in self.severity_config['critical_services']:
            return DriftSeverity.HIGH
        
        # Public-facing resources are medium severity
        resource_data = metadata.get('raw_data', {})
        if self._is_public_facing(provider, service, resource_data):
            return DriftSeverity.MEDIUM
        
        return DriftSeverity.LOW
    
    def _assess_severity_for_removed_resource(self, provider: str, service: str, metadata: Dict[str, Any]) -> DriftSeverity:
        """Assess severity for a removed resource"""
        # Removed critical services are critical
        if service.lower() in self.severity_config['critical_services']:
            return DriftSeverity.CRITICAL
        
        # Any removed resource is at least medium severity
        return DriftSeverity.MEDIUM
    
    def _assess_severity_for_modified_resource(self, provider: str, service: str, 
                                             comparison: Dict[str, Any]) -> DriftSeverity:
        """Assess severity for a modified resource"""
        if comparison.get('has_critical_changes', False):
            return DriftSeverity.CRITICAL
        
        # Check if any changed fields are in our critical list
        critical_fields = self.severity_config['critical_changes'].get(provider.lower(), {}).get(service.lower(), [])
        changed_fields = [change['field'] for change in comparison.get('changed_fields', [])]
        
        if any(field in critical_fields for field in changed_fields):
            return DriftSeverity.HIGH
        
        # More than 5 changes is medium severity
        if len(changed_fields) > 5:
            return DriftSeverity.MEDIUM
        
        return DriftSeverity.LOW
    
    def _is_public_facing(self, provider: str, service: str, resource_data: Dict[str, Any]) -> bool:
        """Check if a resource is public-facing"""
        # This is a simplified check - in practice, you'd have more sophisticated logic
        if provider.lower() == 'aws':
            if service.lower() == 's3':
                return resource_data.get('PublicAccessBlock', {}).get('BlockPublicAcls', True) == False
            elif service.lower() == 'ec2':
                return bool(resource_data.get('PublicIpAddress'))
        
        return False
    
    def generate_drift_report(self, drift_summary: DriftSummary, format_type: str = 'text') -> str:
        """
        Generate a human-readable drift report
        
        Args:
            drift_summary: Drift detection results
            format_type: 'text', 'json', or 'html'
            
        Returns:
            Formatted report string
        """
        if format_type == 'json':
            return json.dumps({
                'summary': {
                    'total_resources': drift_summary.total_resources,
                    'unchanged': drift_summary.unchanged_resources,
                    'added': drift_summary.added_resources,
                    'removed': drift_summary.removed_resources,
                    'modified': drift_summary.modified_resources,
                    'scan_timestamp': drift_summary.scan_timestamp.isoformat(),
                    'scan_duration': drift_summary.scan_duration
                },
                'alerts': [
                    {
                        'resource_path': alert.resource_path,
                        'change_type': alert.change_type.value,
                        'severity': alert.severity.value,
                        'details': alert.details,
                        'timestamp': alert.timestamp.isoformat()
                    }
                    for alert in drift_summary.alerts
                ]
            }, indent=2)
        
        elif format_type == 'text':
            report = []
            report.append("="*60)
            report.append("🔍 CLOUD INFRASTRUCTURE DRIFT REPORT")
            report.append("="*60)
            report.append(f"Scan Time: {drift_summary.scan_timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}")
            report.append(f"Duration: {drift_summary.scan_duration:.2f} seconds")
            report.append("")
            
            # Summary
            report.append("📊 SUMMARY")
            report.append("-" * 20)
            report.append(f"Total Resources: {drift_summary.total_resources}")
            report.append(f"Unchanged: {drift_summary.unchanged_resources}")
            report.append(f"Added: {drift_summary.added_resources}")
            report.append(f"Removed: {drift_summary.removed_resources}")
            report.append(f"Modified: {drift_summary.modified_resources}")
            report.append("")
            
            # Alerts by severity
            if drift_summary.critical_alerts > 0:
                report.append(f"🚨 CRITICAL: {drift_summary.critical_alerts}")
            if drift_summary.high_severity_alerts > 0:
                report.append(f"⚠️  HIGH: {drift_summary.high_severity_alerts}")
            if drift_summary.medium_severity_alerts > 0:
                report.append(f"🔶 MEDIUM: {drift_summary.medium_severity_alerts}")
            if drift_summary.low_severity_alerts > 0:
                report.append(f"🔷 LOW: {drift_summary.low_severity_alerts}")
            
            report.append("")
            
            # Detailed alerts
            if drift_summary.alerts:
                report.append("🔍 DETAILED ALERTS")
                report.append("-" * 30)
                
                for alert in sorted(drift_summary.alerts, key=lambda x: (x.severity.value, x.resource_path)):
                    severity_icon = {
                        DriftSeverity.CRITICAL: "🚨",
                        DriftSeverity.HIGH: "⚠️",
                        DriftSeverity.MEDIUM: "🔶",
                        DriftSeverity.LOW: "🔷"
                    }[alert.severity]
                    
                    change_icon = {
                        ChangeType.ADDED: "➕",
                        ChangeType.REMOVED: "➖",
                        ChangeType.MODIFIED: "🔄"
                    }[alert.change_type]
                    
                    report.append(f"{severity_icon} {change_icon} {alert.resource_path}")
                    report.append(f"   {alert.details.get('message', 'No details')}")
                    
                    if alert.change_type == ChangeType.MODIFIED:
                        critical_changes = alert.details.get('critical_changes', [])
                        if critical_changes:
                            report.append(f"   Critical fields changed: {', '.join(critical_changes)}")
                    
                    report.append("")
            else:
                report.append("✅ No drift detected - infrastructure matches baseline")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format type: {format_type}")
    
    def cleanup_old_snapshots(self, keep_count: int = 10) -> int:
        """
        Clean up old snapshots, keeping only the most recent ones
        
        Args:
            keep_count: Number of snapshots to keep
            
        Returns:
            Number of snapshots deleted
        """
        snapshots = self.list_snapshots()
        
        if len(snapshots) <= keep_count:
            return 0
        
        to_delete = snapshots[keep_count:]
        deleted_count = 0
        
        for snapshot in to_delete:
            snapshot_name = snapshot['snapshot_name']
            
            # Delete both the snapshot and metadata files
            snapshot_path = os.path.join(self.cache_dir, f"{snapshot_name}.json")
            metadata_path = os.path.join(self.cache_dir, f"{snapshot_name}_metadata.json")
            
            try:
                if os.path.exists(snapshot_path):
                    os.remove(snapshot_path)
                if os.path.exists(metadata_path):
                    os.remove(metadata_path)
                deleted_count += 1
            except Exception:
                continue
        
        return deleted_count 