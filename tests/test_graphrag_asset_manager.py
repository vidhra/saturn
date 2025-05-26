import os
import json
import pytest
from unittest.mock import Mock, patch, AsyncMock
from datetime import datetime
import networkx as nx

from internal.assets.graphrag_asset_manager import GraphRAGAssetManager
from saturn.rag_engine import RAGEngine

@pytest.fixture
def mock_asset_client():
    """Mock GCP Asset client."""
    with patch('google.cloud.asset_v1.AssetServiceClient') as mock:
        yield mock

@pytest.fixture
def mock_rag_engine():
    """Mock RAG engine."""
    engine = Mock(spec=RAGEngine)
    engine.ingest_and_build_index = Mock()
    engine.query_docs = Mock(return_value="Asset information")
    return engine

@pytest.fixture
def sample_asset():
    """Sample GCP asset for testing."""
    return Mock(
        name="projects/test-project/assets/test-asset",
        asset_type="compute.googleapis.com/Instance",
        resource=Mock(
            data={
                "name": "test-instance",
                "network": "projects/test-project/networks/test-network",
                "serviceAccount": "test-service@test-project.iam.gserviceaccount.com"
            }
        )
    )

@pytest.fixture
def asset_manager(mock_asset_client, mock_rag_engine, tmp_path):
    """Create GraphRAGAssetManager instance for testing."""
    return GraphRAGAssetManager(
        project_id="test-project",
        rag_engine=mock_rag_engine,
        output_dir=str(tmp_path),
        gcp_creds_path=None
    )

def test_initialization(asset_manager, tmp_path):
    """Test GraphRAGAssetManager initialization."""
    assert asset_manager.project_id == "test-project"
    assert asset_manager.output_dir == str(tmp_path)
    assert os.path.exists(tmp_path)

def test_discover_assets(asset_manager, mock_asset_client, sample_asset):
    """Test asset discovery functionality."""
    # Mock asset listing
    mock_asset_client.return_value.list_assets.return_value = [sample_asset]
    
    # Discover assets
    result = asset_manager.discover_assets()
    
    # Verify results
    assert "nodes" in result
    assert "relationships" in result
    assert len(result["nodes"]) == 1
    assert result["nodes"][0]["asset_type"] == "compute.googleapis.com/Instance"
    
    # Verify files were created
    assert os.path.exists(os.path.join(asset_manager.output_dir, "nodes.json"))
    assert os.path.exists(os.path.join(asset_manager.output_dir, "relationships.json"))

def test_transform_asset_to_node(asset_manager, sample_asset):
    """Test asset to node transformation."""
    node = asset_manager._transform_asset_to_node(sample_asset)
    
    assert node["id"] == "projects/test-project/assets/test-asset"
    assert node["asset_type"] == "compute.googleapis.com/Instance"
    assert "test-instance" in node["resource_data"]["name"]

def test_build_relationships(asset_manager):
    """Test relationship building between nodes."""
    nodes = [
        {
            "id": "projects/test-project/assets/instance-1",
            "asset_type": "compute.googleapis.com/Instance",
            "location": "us-central1",
            "resource_data": {
                "network": "projects/test-project/networks/test-network",
                "serviceAccount": "test-service@test-project.iam.gserviceaccount.com"
            }
        },
        {
            "id": "projects/test-project/assets/service-account-1",
            "asset_type": "iam.googleapis.com/ServiceAccount",
            "display_name": "test-service@test-project.iam.gserviceaccount.com"
        }
    ]
    
    relationships = asset_manager._build_relationships(nodes)
    
    # Verify relationships
    assert len(relationships) >= 2  # At least location and service account relationships
    assert any(r["relation_type"] == "LOCATED_IN" for r in relationships)
    assert any(r["relation_type"] == "USES_SERVICE_ACCOUNT" for r in relationships)

def test_update_rag_engine(asset_manager, mock_rag_engine):
    """Test RAG engine update with graph data."""
    nodes = [{"id": "test-node", "asset_type": "test-type", "display_name": "Test Node"}]
    relationships = [{"source_id": "test-node", "target_id": "test-target", "relation_type": "TEST"}]
    
    asset_manager._update_rag_engine(nodes, relationships)
    
    # Verify RAG engine was updated
    mock_rag_engine.ingest_and_build_index.assert_called_once()
    call_args = mock_rag_engine.ingest_and_build_index.call_args[0]
    assert len(call_args[0]) == 2  # One document for node, one for relationship

def test_monitor_asset(asset_manager, mock_rag_engine):
    """Test asset monitoring functionality."""
    result = asset_manager.monitor_asset("test-asset")
    
    assert result["asset_id"] == "test-asset"
    assert result["information"] == "Asset information"
    assert "timestamp" in result

def test_get_asset_relationships(asset_manager, tmp_path):
    """Test getting relationships for a specific asset."""
    # Create test relationships file
    relationships = [
        {"source_id": "test-asset", "target_id": "target-1", "relation_type": "TEST"},
        {"source_id": "other-asset", "target_id": "test-asset", "relation_type": "TEST"}
    ]
    
    with open(os.path.join(tmp_path, "relationships.json"), 'w') as f:
        json.dump(relationships, f)
    
    # Get relationships
    result = asset_manager.get_asset_relationships("test-asset")
    
    assert len(result) == 2
    assert all(r["source_id"] == "test-asset" or r["target_id"] == "test-asset" for r in result)

def test_error_handling(asset_manager, mock_asset_client):
    """Test error handling in asset discovery."""
    # Mock asset client to raise an exception
    mock_asset_client.return_value.list_assets.side_effect = Exception("Test error")
    
    # Discover assets should handle the error gracefully
    result = asset_manager.discover_assets()
    
    assert result["nodes"] == []
    assert result["relationships"] == []

@pytest.mark.asyncio
async def test_async_operations(asset_manager, mock_rag_engine):
    """Test async operations with the asset manager."""
    # Mock async RAG engine operations
    mock_rag_engine.query_docs = AsyncMock(return_value="Async asset information")
    
    # Test async monitoring
    result = await asset_manager.monitor_asset("test-asset")
    
    assert result["information"] == "Async asset information"
    mock_rag_engine.query_docs.assert_called_once()

def test_graph_initialization(asset_manager):
    """Test that NetworkX graph is properly initialized."""
    assert isinstance(asset_manager.graph, nx.DiGraph)
    assert len(asset_manager.graph.nodes) == 0
    assert len(asset_manager.graph.edges) == 0

def test_discover_assets_with_graph(asset_manager, mock_asset_client, sample_asset):
    """Test asset discovery with NetworkX graph integration."""
    # Mock asset listing
    mock_asset_client.return_value.list_assets.return_value = [sample_asset]
    
    # Discover assets
    result = asset_manager.discover_assets()
    
    # Verify graph structure
    assert len(asset_manager.graph.nodes) == 1
    assert asset_manager.graph.nodes[sample_asset.name]["asset_type"] == "compute.googleapis.com/Instance"
    
    # Verify results
    assert "nodes" in result
    assert "relationships" in result
    assert len(result["nodes"]) == 1
    assert result["nodes"][0]["asset_type"] == "compute.googleapis.com/Instance"

def test_get_asset_path(asset_manager):
    """Test finding paths between assets in the graph."""
    # Add test nodes and edges
    asset_manager.graph.add_node("asset1", asset_type="type1", display_name="Asset 1")
    asset_manager.graph.add_node("asset2", asset_type="type2", display_name="Asset 2")
    asset_manager.graph.add_node("asset3", asset_type="type3", display_name="Asset 3")
    
    asset_manager.graph.add_edge("asset1", "asset2", relation_type="CONNECTS_TO")
    asset_manager.graph.add_edge("asset2", "asset3", relation_type="CONNECTS_TO")
    
    # Test path finding
    path = asset_manager.get_asset_path("asset1", "asset3")
    
    assert len(path) == 2
    assert path[0]["from"]["id"] == "asset1"
    assert path[0]["to"]["id"] == "asset2"
    assert path[1]["from"]["id"] == "asset2"
    assert path[1]["to"]["id"] == "asset3"

def test_monitor_asset_with_graph_context(asset_manager, mock_rag_engine):
    """Test asset monitoring with graph context."""
    # Add test node and relationships
    asset_manager.graph.add_node("test-asset", 
                                asset_type="test-type",
                                display_name="Test Asset")
    asset_manager.graph.add_node("related-asset",
                                asset_type="related-type",
                                display_name="Related Asset")
    asset_manager.graph.add_edge("test-asset", "related-asset",
                                relation_type="RELATED_TO")
    
    # Test monitoring
    result = asset_manager.monitor_asset("test-asset")
    
    assert result["asset_id"] == "test-asset"
    assert "information" in result
    assert "timestamp" in result
    
    # Verify RAG engine was queried with graph context
    mock_rag_engine.query_docs.assert_called_once()
    query = mock_rag_engine.query_docs.call_args[0][0]
    assert "Test Asset" in query
    assert "Related Asset" in query
    assert "RELATED_TO" in query 