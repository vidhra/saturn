import json
from collections import defaultdict
import duckdb
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def setup_duckdb():
    """
    Sets up DuckDB with necessary tables.
    """
    # Connect to DuckDB
    conn = duckdb.connect('assets.duckdb')
    
    # Create table for assets without vector storage
    conn.execute("""
        CREATE TABLE IF NOT EXISTS assets (
            id VARCHAR,
            asset_type VARCHAR,
            name VARCHAR,
            display_name VARCHAR,
            location VARCHAR,
            project VARCHAR,
            state VARCHAR,
            create_time VARCHAR,
            metadata JSON,
            search_text VARCHAR,  -- Combined text for searching
            embedding FLOAT[384]
        )
    """)
    
    return conn

def store_assets_in_duckdb(assets_by_type):
    """
    Stores assets in DuckDB with searchable text.
    """
    conn = setup_duckdb()
    
    # Clear existing data
    
    # Process and store each asset
    for asset_type, assets in assets_by_type.items():
        for asset in assets:
            # Create search text from relevant fields
            embedding = None
            search_text = f"{asset['name']} {asset.get('displayName', '')} {asset_type} {asset.get('location', '')}"
            embedding = model.encode("asset_name:"+asset['name']+" asset_type:"+
                                         asset['assetType']+" location:"+asset['location'])
            if 'additionalAttributes' in asset:
                search_text += f" {str(asset['additionalAttributes'])}"

            
            # Prepare data for insertion
            conn.execute("""
                INSERT INTO assets (
                    id, asset_type, name, display_name, location, project,
                    state, create_time, metadata, search_text, embedding
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                asset['name'],  # Using name as ID
                asset_type,
                asset['name'],
                asset.get('displayName', None),
                asset.get('location', None),
                asset.get('project', None),
                asset.get('state', None),
                asset.get('createTime', None),
                json.dumps(asset),  # Store full metadata as JSON
                search_text.lower(),  # Store lowercase for case-insensitive search
                embedding
            ))
    
    # Create index for text search
    conn.execute("""
        CREATE INDEX IF NOT EXISTS asset_search_idx 
        ON assets(search_text);
    """)
    
    conn.close()

def search_similar_assets(query_text, top_k=5):
    """
    Search for similar assets using text matching.
    """
    conn = duckdb.connect('assets.duckdb')
    
    # Perform text-based search
    query_embedding = model.encode(query_text).tolist()

    # Retrieve documents ordered by similarity
    results = conn.execute('''
    SELECT name, asset_type, location, embedding, array_cosine_similarity(embedding::FLOAT[384], ?::FLOAT[384]) AS similarity
    FROM assets
    ORDER BY similarity DESC
    LIMIT 10
    ''', (query_embedding,)).fetchall()

    for result in results:
        print(f"Name: {result[0]}, Asset Type: {result[1]}, Location: {result[2]}, Similarity: {result[4]}")
    
    conn.close()
    return results

def read_asset_metadata(file_path: str = "asset_metadata.json"):
    """
    Reads asset metadata from a JSON file.
    
    Args:
        file_path (str): Path to the asset metadata JSON file
    
    Returns:
        dict: Assets grouped by asset type
    """
    try:
        with open(file_path, 'r') as f:
            assets = json.load(f)
        
        # Group assets by type
        assets_by_type = defaultdict(list)
        for asset in assets:
            assets_by_type[asset['assetType']].append(asset)
            
        return assets_by_type
    
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {file_path}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def print_asset_type_summary(assets_by_type):
    """Prints a summary of assets by type."""
    print("\nAsset Type Summary:")
    print("-" * 80)
    for asset_type, assets in sorted(assets_by_type.items()):
        print(f"{asset_type}: {len(assets)} assets")

def print_detailed_assets(assets_by_type, max_per_type=3):
    """Prints detailed information for each asset type."""
    print("\nDetailed Asset Information:")
    print("=" * 80)
    for asset_type, assets in sorted(assets_by_type.items()):
        print(f"\nAsset Type: {asset_type}")
        print("-" * 40)
        # Print details for up to max_per_type assets
        for i, asset in enumerate(assets[:max_per_type]):
            print(f"  Asset {i+1}:")
            print(f"    Name: {asset['name']}")
            print(f"    Display Name: {asset.get('displayName', 'N/A')}")
            print(f"    Location: {asset.get('location', 'N/A')}")
            print(f"    Project: {asset.get('project', 'N/A')}")
            if 'state' in asset:
                print(f"    State: {asset['state']}")
            if 'createTime' in asset:
                print(f"    Created: {asset['createTime']}")
            if 'additionalAttributes' in asset:
                print(f"    Additional Attributes: {asset['additionalAttributes']}")
            if i < len(assets) - 1:
                print()
        if len(assets) > max_per_type:
            print(f"  ... and {len(assets) - max_per_type} more assets")

def analyze_asset_locations(assets_by_type):
    """Analyzes and prints location distribution of assets."""
    print("\nLocation Distribution:")
    print("-" * 80)
    location_count = defaultdict(int)
    
    for assets in assets_by_type.values():
        for asset in assets:
            location = asset.get('location', 'unknown')
            location_count[location] += 1
    
    for location, count in sorted(location_count.items()):
        print(f"{location}: {count} assets")

def main():
    # Read assets from file
    assets_by_type = read_asset_metadata()
    
    if assets_by_type:
        # Store assets in DuckDB with searchable text
        store_assets_in_duckdb(assets_by_type)
        print("\nAssets have been stored in DuckDB with searchable text")
        
        # Example similarity search
        print("\nExample similarity search for 'cloud run functions':")
        similar_assets = search_similar_assets("billing accounts")
        for asset in similar_assets:
            print(f"Name: {asset[0]}")
            print(f"Type: {asset[1]}")
            print(f"Location: {asset[2]}")
            print("-" * 40)
        
        # Continue with existing analysis
        print_asset_type_summary(assets_by_type)
        print_detailed_assets(assets_by_type)
        analyze_asset_locations(assets_by_type)
        
        total_assets = sum(len(assets) for assets in assets_by_type.values())
        print(f"\nTotal number of assets: {total_assets}")

        # Print unique asset types for reference
        print("\nUnique Asset Types:")
        print("-" * 80)
        for asset_type in sorted(assets_by_type.keys()):
            print(asset_type)

if __name__ == "__main__":
    main()