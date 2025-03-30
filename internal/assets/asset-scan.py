import json
from collections import defaultdict

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
        # Print summary
        print_asset_type_summary(assets_by_type)
        
        # Print detailed information
        print_detailed_assets(assets_by_type)
        
        # Print location analysis
        analyze_asset_locations(assets_by_type)
        
        # Print total number of assets
        total_assets = sum(len(assets) for assets in assets_by_type.values())
        print(f"\nTotal number of assets: {total_assets}")

        # Print unique asset types for reference
        print("\nUnique Asset Types:")
        print("-" * 80)
        for asset_type in sorted(assets_by_type.keys()):
            print(asset_type)

if __name__ == "__main__":
    main()