import os
import json
import logging
from google.cloud import asset_v1
from google.protobuf.json_format import MessageToDict
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pre-defined list of common GCP asset types (can be expanded)
# This list is a starting point. For a truly dynamic discovery,
# one might need to use more advanced methods or a maintained list.
COMMON_ASSET_TYPES = [
    "cloudresourcemanager.googleapis.com/Project",
    "cloudresourcemanager.googleapis.com/Folder",
    "cloudresourcemanager.googleapis.com/Organization",
    "compute.googleapis.com/Instance",
    "compute.googleapis.com/Disk",
    "compute.googleapis.com/Network",
    "compute.googleapis.com/Subnetwork",
    "compute.googleapis.com/Firewall",
    "compute.googleapis.com/Address",
    "compute.googleapis.com/ForwardingRule",
    "compute.googleapis.com/InstanceGroup",
    "compute.googleapis.com/InstanceTemplate",
    "compute.googleapis.com/RegionBackendService",
    "compute.googleapis.com/GlobalBackendService",
    "compute.googleapis.com/UrlMap",
    "compute.googleapis.com/TargetHttpProxy",
    "compute.googleapis.com/TargetHttpsProxy",
    "storage.googleapis.com/Bucket",
    "sqladmin.googleapis.com/Instance", # Cloud SQL
    "iam.googleapis.com/ServiceAccount",
    "pubsub.googleapis.com/Topic",
    "pubsub.googleapis.com/Subscription",
    "monitoring.googleapis.com/MetricDescriptor", # Example, might be too granular
    "logging.googleapis.com/LogSink",
    "run.googleapis.com/Service", # Cloud Run
    "container.googleapis.com/Cluster", # GKE
    "bigquery.googleapis.com/Dataset",
    "bigquery.googleapis.com/Table",
    # Add more types as needed
]

def get_gcp_assets(scope: str, types_to_fetch: list, credentials_path: str = None):
    """
    Fetches assets from GCP for the given scope and asset types.

    Args:
        scope (str): The GCP scope (e.g., "projects/your-project-id").
        types_to_fetch (list): A list of asset types to fetch.
                               If empty, fetches all available assets for the scope.
        credentials_path (str, optional): Path to GCP service account key file.
                                          If None, uses default environment authentication.

    Returns:
        list: A list of asset dictionaries.
    """
    if credentials_path:
        client = asset_v1.AssetServiceClient.from_service_account_file(credentials_path)
    else:
        client = asset_v1.AssetServiceClient()

    all_assets = []
    logging.info(f"Starting asset fetching for scope: {scope}")

    if not types_to_fetch:  # Empty list means fetch all available types
        logging.info(f"Fetching all available asset types for scope: {scope} in a single API call.")
        try:
            request = asset_v1.types.ListAssetsRequest(
                parent=scope,
                asset_types=[],  # Empty list tells API to return all types
                content_type=asset_v1.ContentType.RESOURCE,
                page_size=1000  # Adjust as needed, max is 1000
            )
            page_result = client.list_assets(request=request)
            
            count = 0
            for asset in page_result:
                all_assets.append(asset)
                count += 1
            logging.info(f"Fetched {count} assets of various types in the single call.")
        except Exception as e:
            logging.error(f"Error fetching all asset types: {e}")
    else:  # Specific list of asset types provided
        for asset_type in types_to_fetch:
            logging.info(f"Fetching assets of type: {asset_type}")
            try:
                request = asset_v1.types.ListAssetsRequest(
                    parent=scope,
                    asset_types=[asset_type],
                    content_type=asset_v1.ContentType.RESOURCE,
                    page_size=1000
                )
                page_result = client.list_assets(request=request)
                
                count = 0
                for asset in page_result:
                    all_assets.append(asset)
                    count += 1
                logging.info(f"Fetched {count} assets of type {asset_type}.")
            except Exception as e:
                logging.error(f"Error fetching asset type {asset_type}: {e}")
                continue
            
    logging.info(f"Total assets fetched: {len(all_assets)}")
    return all_assets

def transform_asset_to_node(asset: asset_v1.types.Asset, project_id_override: str = None) -> dict:
    """
    Transforms a GCP asset object into a generic graph node dictionary.

    Args:
        asset (asset_v1.types.Asset): The GCP asset object.
        project_id_override (str, optional): Project ID to use if parsing from asset.name fails.

    Returns:
        dict: A dictionary representing the graph node.
    """
    # Convert proto-plus Asset message to a dictionary
    # asset_dict = MessageToDict(asset) # Old method, caused DESCRIPTOR error
    try:
        asset_json = asset_v1.types.Asset.to_json(asset) 
        asset_dict = json.loads(asset_json)
    except Exception as e:
        logging.error(f"Error converting asset to dict: {asset.name} - {e}")
        # Fallback or return a minimal representation if conversion fails
        return {
            "id": asset.name,
            "asset_type": asset.asset_type,
            "display_name": asset.name.split('/')[-1],
            "project_id": None, # Or try to parse from asset.name
            "location": None,
            "resource_data_json": "{}",
            "update_time": None,
            "parent_asset_name": asset_dict.get('parentAssetName'),
            "conversion_error": True
        }
    
    node_id = asset.name
    asset_type = asset.asset_type
    
    display_name = None
    if asset.resource and asset.resource.data:
        resource_data = asset_dict.get('resource', {}).get('data', {})
        display_name = resource_data.get('displayName', resource_data.get('name', None))
        # For some assets, the name might be directly under data, e.g. service accounts
        if not display_name and 'name' in resource_data:
             if isinstance(resource_data['name'], str) and not resource_data['name'].startswith('projects/'): # Avoid full resource names
                display_name = resource_data['name']


    # Attempt to parse project_id from asset.name
    parsed_project_id = None
    if "projects/" in node_id:
        try:
            parsed_project_id = node_id.split("projects/")[1].split("/")[0]
        except IndexError:
            logging.warning(f"Could not parse project_id from asset name: {node_id}")
            parsed_project_id = project_id_override # Fallback

    location = asset_dict.get('location') # Some assets have top-level location
    if not location and asset.resource and asset.resource.data:
        resource_data = asset_dict.get('resource', {}).get('data', {})
        # Common location fields, might need expansion
        location = resource_data.get('location', resource_data.get('region', resource_data.get('zone')))


    resource_data_json = "{}"
    if asset_dict.get('resource') and asset_dict.get('resource', {}).get('data'):
        resource_data_json = json.dumps(asset_dict.get('resource', {}).get('data', {}))

    # update_time is usually an RFC3339 string after .to_json() conversion
    update_time_str = asset_dict.get('updateTime') 

    # Fallback for update_time (less likely needed)
    if not update_time_str and hasattr(asset, 'update_time') and asset.update_time:
        try:
            dt_object = datetime.fromtimestamp(asset.update_time.seconds + asset.update_time.nanos / 1e9)
            update_time_str = dt_object.isoformat() + "Z"
        except AttributeError:
            logging.warning(f"Could not parse update_time from original asset object for {node_id}.")
            if isinstance(asset.update_time, str):
                update_time_str = asset.update_time
            else:
                 logging.warning(f"update_time for {node_id} is of an unexpected type: {type(asset.update_time)}")
                 update_time_str = None

    parent_name = asset_dict.get('parentAssetName')

    return {
        "id": node_id,
        "asset_type": asset_type,
        "display_name": display_name if display_name else node_id.split('/')[-1],
        "project_id": parsed_project_id if parsed_project_id else project_id_override,
        "location": location,
        "resource_data_json": resource_data_json,
        "update_time": update_time_str,
        "parent_asset_name": parent_name, 
    }

def infer_relationships(node: dict, all_nodes_map: dict) -> list:
    """
    Infers relationships for a given node.

    Args:
        node (dict): The node to infer relationships for.
        all_nodes_map (dict): A map of all node IDs to their data for quick lookup.

    Returns:
        list: A list of relationship dictionaries.
    """
    relationships = []
    source_id = node["id"]

    # 1. Structural/Parental
    if node.get("parent_asset_name"):
        parent_id = node["parent_asset_name"]
        # Ensure parent exists in our collected nodes for consistency
        if parent_id in all_nodes_map:
            relationships.append({
                "source_id": source_id,
                "target_id": parent_id,
                "relation_type": "CHILD_OF"
            })
            relationships.append({ # Add reciprocal relationship
                "source_id": parent_id,
                "target_id": source_id,
                "relation_type": "PARENT_OF"
            })


    # 2. Location-Based
    if node.get("location"):
        # Conceptual location node (could be represented differently, e.g., as properties)
        # For this example, we'll create a string target_id for location
        location_target_id = f"location:{node['location']}"
        relationships.append({
            "source_id": source_id,
            "target_id": location_target_id, # This target won't be in all_nodes_map unless we create location nodes
            "relation_type": "LOCATED_IN"
        })

    # 3. Embedded Resource Links (simplified example)
    try:
        resource_data = json.loads(node["resource_data_json"])
        
        # Example: Network interfaces for compute instances
        if node["asset_type"] == "compute.googleapis.com/Instance" and "networkInterfaces" in resource_data:
            for nic in resource_data.get("networkInterfaces", []):
                if "network" in nic:
                    network_uri = nic["network"]
                    if network_uri in all_nodes_map: # Check if network is a known asset
                         relationships.append({
                            "source_id": source_id,
                            "target_id": network_uri,
                            "relation_type": "USES_NETWORK"
                        })
                if "subnetwork" in nic:
                    subnetwork_uri = nic["subnetwork"]
                    if subnetwork_uri in all_nodes_map:
                        relationships.append({
                            "source_id": source_id,
                            "target_id": subnetwork_uri,
                            "relation_type": "USES_SUBNETWORK"
                        })
        
        # Example: Service accounts used by some resources
        if "serviceAccount" in resource_data and isinstance(resource_data["serviceAccount"], str):
            sa_email = resource_data["serviceAccount"]
            # Attempt to find a matching service account node by its email (or part of its name)
            # This is a simplification; full SA resource names are like projects/.../serviceAccounts/...
            for nid, n_data in all_nodes_map.items():
                if n_data["asset_type"] == "iam.googleapis.com/ServiceAccount" and \
                   (sa_email == n_data.get("display_name") or sa_email in nid) : # display_name might be email
                    relationships.append({
                        "source_id": source_id,
                        "target_id": nid,
                        "relation_type": "USES_SERVICE_ACCOUNT"
                    })
                    break # Assume first match is fine for this example

        # Example: GCS Bucket for Cloud Function
        if node["asset_type"] == "run.googleapis.com/Service" and "template" in resource_data: # Cloud Run often implies GCR
            if "containers" in resource_data["template"].get("spec",{}):
                for container in resource_data["template"]["spec"]["containers"]:
                    if "image" in container:
                        image_uri = container["image"] # e.g. gcr.io/project-id/image-name
                        # This is a very basic inference, could link to GCR artifact registry if it exists
                        relationships.append({
                            "source_id": source_id,
                            "target_id": image_uri, # This target_id is conceptual
                            "relation_type": "USES_CONTAINER_IMAGE"
                        })


    except json.JSONDecodeError:
        logging.warning(f"Could not parse resource_data_json for node {source_id}")
    except Exception as e:
        logging.error(f"Error inferring relationships from resource_data for {source_id}: {e}")


    # 4. Tag/Label Connections (simple example: shared 'app' label)
    # This requires parsing labels from resource_data_json
    try:
        resource_data = json.loads(node["resource_data_json"])
        labels = resource_data.get("labels", {})
        if "app" in labels:
            app_label_value = labels["app"]
            # Find other nodes with the same app label
            for other_node_id, other_node_data in all_nodes_map.items():
                if source_id == other_node_id:
                    continue # Don't link to self
                try:
                    other_resource_data = json.loads(other_node_data["resource_data_json"])
                    other_labels = other_resource_data.get("labels", {})
                    if other_labels.get("app") == app_label_value:
                        relationships.append({
                            "source_id": source_id,
                            "target_id": other_node_id,
                            "relation_type": f"SHARES_APP_LABEL ({app_label_value})"
                        })
                except (json.JSONDecodeError, KeyError):
                    continue # Skip if other node's labels can't be parsed
    except json.JSONDecodeError:
        pass # Handled above

    return relationships

def main(project_id: str, asset_types_str: str = "ALL_AVAILABLE", output_dir: str = ".", gcp_creds_path: str = None):
    """
    Main function to orchestrate asset fetching, transformation, and relationship inference.

    Args:
        project_id (str): The GCP project ID.
        asset_types_str (str, optional): Controls asset type fetching.
                                         "ALL_AVAILABLE" (default): Fetches all types via API.
                                         "COMMON": Fetches from COMMON_ASSET_TYPES list.
                                         Comma-separated string (e.g., "type1,type2"): Fetches specific types.
        output_dir (str, optional): Directory to save the output JSON files.
        gcp_creds_path (str, optional): Path to GCP service account credentials JSON file.
    """
    scope = f"projects/{project_id}"
    
    api_asset_types_list = [] # Default to empty list for "ALL_AVAILABLE"

    if asset_types_str.upper() == "ALL_AVAILABLE":
        logging.info("Configuration: Fetching all available asset types from the API.")
        api_asset_types_list = [] # Empty list signals to ListAssets to get all
    elif asset_types_str.upper() == "COMMON":
        logging.info(f"Configuration: Fetching COMMON pre-defined asset types: {COMMON_ASSET_TYPES}")
        api_asset_types_list = COMMON_ASSET_TYPES
    else: # A specific comma-separated list
        api_asset_types_list = [s.strip() for s in asset_types_str.split(',')]
        logging.info(f"Configuration: Fetching user-specified asset types: {api_asset_types_list}")

    # 1. Fetch Assets
    raw_assets = get_gcp_assets(scope, api_asset_types_list, credentials_path=gcp_creds_path)
    if not raw_assets:
        logging.warning("No assets found or an error occurred during fetching. Exiting.")
        return

    # 2. Transform Assets to Nodes
    nodes = []
    for asset in raw_assets:
        # Pass the project_id from the main arg as a fallback if parsing fails
        node = transform_asset_to_node(asset, project_id_override=project_id)
        nodes.append(node)
    
    logging.info(f"Transformed {len(nodes)} assets into nodes.")

    # Create a map for quick node lookup during relationship inference
    all_nodes_map = {node["id"]: node for node in nodes}

    # 3. Infer Relationships
    all_relationships = []
    for node in nodes:
        rels = infer_relationships(node, all_nodes_map)
        all_relationships.extend(rels)
    
    logging.info(f"Inferred {len(all_relationships)} relationships.")

    # 4. Output
    os.makedirs(output_dir, exist_ok=True)
    nodes_file = os.path.join(output_dir, "nodes.json")
    relationships_file = os.path.join(output_dir, "relationships.json")

    with open(nodes_file, 'w') as f:
        json.dump(nodes, f, indent=2)
    logging.info(f"Nodes saved to {nodes_file}")

    with open(relationships_file, 'w') as f:
        json.dump(all_relationships, f, indent=2)
    logging.info(f"Relationships saved to {relationships_file}")

    logging.info("GraphRAG data generation complete.")


if __name__ == "__main__":
    # --- Configuration ---
    # Replace with your actual project ID
    # You can also set this via an environment variable or command-line argument
    TARGET_PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "vidhra") 
    
    # Optional: Specify path to your GCP service account key JSON file
    # If None, relies on Application Default Credentials (e.g., gcloud auth application-default login)
    GCP_CREDENTIALS_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", None)

    # Optional: Specify asset types as a comma-separated string.
    # "ALL_AVAILABLE" (default): Fetches all types the API can return for the scope.
    # "COMMON": Uses the pre-defined COMMON_ASSET_TYPES list.
    # Example: "compute.googleapis.com/Instance,storage.googleapis.com/Bucket"
    ASSET_TYPES_TO_FETCH = os.environ.get("GCP_ASSET_TYPES", "ALL_AVAILABLE") 
    
    OUTPUT_DIRECTORY = "./gcp_graph_data"

    # --- Execution ---
    if TARGET_PROJECT_ID == "your-gcp-project-id":
        print("ERROR: Please set the TARGET_PROJECT_ID variable in the script or the GCP_PROJECT_ID environment variable.")
    else:
        main(
            project_id=TARGET_PROJECT_ID,
            asset_types_str=ASSET_TYPES_TO_FETCH,
            output_dir=OUTPUT_DIRECTORY,
            gcp_creds_path=GCP_CREDENTIALS_PATH
        ) 