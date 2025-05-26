# Sample GCP Assets

## Compute Instance
- asset_id: compute-instance-1
- name: test-instance-1
- type: compute.googleapis.com/Instance
- zone: us-central1-a
- machine_type: e2-medium
- status: RUNNING

## Network
- asset_id: network-1
- name: default-network
- type: compute.googleapis.com/Network
- region: us-central1
- auto_create_subnetworks: true

## Subnetwork
- asset_id: subnet-1
- name: default-subnet
- type: compute.googleapis.com/Subnetwork
- region: us-central1
- ip_cidr_range: 10.0.0.0/24

## Firewall Rule
- asset_id: firewall-1
- name: allow-ssh
- type: compute.googleapis.com/Firewall
- network: default-network
- direction: INGRESS
- allowed: tcp:22

## Relationships
- compute-instance-1 -> network-1: CONNECTED_TO
- network-1 -> subnet-1: CONTAINS
- network-1 -> firewall-1: HAS_RULE
- compute-instance-1 -> subnet-1: IN_SUBNET 