import argparse
from google.cloud import asset_v1
from google.protobuf.json_format import MessageToDict
import os
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vidhra-eb3e8152e0a2.json"

# Parse command-line argument for project ID
parser = argparse.ArgumentParser(
    description="List all resources in a GCP project along with their metadata using Cloud Asset Inventory API"
)
parser.add_argument("project_id", help="Google Cloud project ID to list resources from")
args = parser.parse_args()
project_id = args.project_id

# Initialize the AssetServiceClient (assumes authentication is already set up)
client = asset_v1.AssetServiceClient()

# Define the scope as the project (format: "projects/<PROJECT_ID>")
scope = f"projects/{project_id}"

# Retrieve resources from the project
resource_iterator = client.search_all_resources(scope=scope)

all_assets = []

print(f"Assets and their metadata in project '{project_id}':\n")
for asset in resource_iterator:
    try:
        # Try using the to_dict() method provided by the proto-plus wrapper
        asset_metadata = asset.to_dict()
    except AttributeError:
        # Fallback: convert using the underlying protobuf message
        asset_metadata = MessageToDict(asset._pb)
    
    all_assets.append(asset_metadata)

with open("asset_metadata.json", "w") as f:
    json.dump(all_assets, f, indent=4)
