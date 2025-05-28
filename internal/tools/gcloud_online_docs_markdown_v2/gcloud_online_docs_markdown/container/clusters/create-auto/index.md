# gcloud container clusters create-auto  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto)*

**NAME**

: **gcloud container clusters create-auto - create an Autopilot cluster for running containers**

**SYNOPSIS**

: **`gcloud container clusters create-auto` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--async)`] [`[--auto-monitoring-scope](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--auto-monitoring-scope)`=`AUTO_MONITORING_SCOPE`] [`[--autoprovisioning-enable-insecure-kubelet-readonly-port](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--autoprovisioning-enable-insecure-kubelet-readonly-port)`] [`[--autoprovisioning-network-tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--autoprovisioning-network-tags)`=`TAGS`,[`[TAGS](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#TAGS)`,…]] [`[--autoprovisioning-resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--autoprovisioning-resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY`] [`[--cluster-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-ipv4-cidr)`=`CLUSTER_IPV4_CIDR`] [`[--cluster-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-secondary-range-name)`=`NAME`] [`[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-version)`=`CLUSTER_VERSION`] [`[--containerd-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--containerd-config-from-file)`=`PATH_TO_FILE`] [`[--create-subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--create-subnetwork)`=[`KEY`=`VALUE`,…]] [`[--database-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--database-encryption-key)`=`DATABASE_ENCRYPTION_KEY`] [`[--disable-l4-lb-firewall-reconciliation](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--disable-l4-lb-firewall-reconciliation)`] [`[--enable-authorized-networks-on-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-authorized-networks-on-private-endpoint)`] [`[--enable-backup-restore](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-backup-restore)`] [`[--enable-cilium-clusterwide-network-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-cilium-clusterwide-network-policy)`] [`[--enable-dns-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-dns-access)`] [`[--enable-fleet](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-fleet)`] [`[--enable-google-cloud-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-google-cloud-access)`] [`[--enable-ip-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-ip-access)`] [`[--enable-kubernetes-unstable-apis](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-kubernetes-unstable-apis)`=`API`,[`[API](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#API)`,…]] [`[--enable-master-global-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-master-global-access)`] [`[--enable-multi-networking](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-multi-networking)`] [`[--enable-ray-cluster-logging](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-ray-cluster-logging)`] [`[--enable-ray-cluster-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-ray-cluster-monitoring)`] [`[--enable-ray-operator](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-ray-operator)`] [`[--enable-secret-manager](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-secret-manager)`] [`[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--fleet-project)`=`PROJECT_ID_OR_NUMBER`] [`[--hpa-profile](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--hpa-profile)`=`HPA_PROFILE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--labels)`=[`KEY`=`VALUE`,…]] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--logging)`=[`COMPONENT`,…]] [`[--monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--monitoring)`=[`COMPONENT`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--network)`=`NETWORK`] [`[--private-endpoint-subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--private-endpoint-subnetwork)`=`NAME`] [`[--release-channel](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--release-channel)`=[`CHANNEL`]] [`[--security-group](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--security-group)`=`SECURITY_GROUP`] [`[--security-posture](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--security-posture)`=`SECURITY_POSTURE`] [`[--services-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--services-ipv4-cidr)`=`CIDR`] [`[--services-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--services-secondary-range-name)`=`NAME`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--subnetwork)`=`SUBNETWORK`] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--tier)`=`TIER`] [`[--workload-policies](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-policies)`=`WORKLOAD_POLICIES`] [`[--workload-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--workload-vulnerability-scanning)`=`WORKLOAD_VULNERABILITY_SCANNING`] [`[--additive-vpc-scope-dns-domain](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--additive-vpc-scope-dns-domain)`=`ADDITIVE_VPC_SCOPE_DNS_DOMAIN`     | `[--disable-additive-vpc-scope](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--disable-additive-vpc-scope)`] [`[--aggregation-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--aggregation-ca)`=`CA_POOL_PATH` `[--cluster-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-ca)`=`CA_POOL_PATH` `[--control-plane-disk-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--control-plane-disk-encryption-key)`=`KEY` `[--etcd-api-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--etcd-api-ca)`=`CA_POOL_PATH` `[--etcd-peer-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--etcd-peer-ca)`=`CA_POOL_PATH` `[--gkeops-etcd-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--gkeops-etcd-backup-encryption-key)`=`KEY` `[--service-account-signing-keys](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--service-account-signing-keys)`=`KEY_VERSION`,[`[KEY_VERSION](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#KEY_VERSION)`,…] `[--service-account-verification-keys](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--service-account-verification-keys)`=`KEY_VERSION`,[`[KEY_VERSION](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#KEY_VERSION)`,…]] [`[--dataplane-v2-observability-mode](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--dataplane-v2-observability-mode)`=`DATAPLANE_V2_OBSERVABILITY_MODE`     | `[--disable-dataplane-v2-flow-observability](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--disable-dataplane-v2-flow-observability)`     | `[--enable-dataplane-v2-flow-observability](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-dataplane-v2-flow-observability)`] [`[--enable-insecure-binding-system-authenticated](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-insecure-binding-system-authenticated)` `[--enable-insecure-binding-system-unauthenticated](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-insecure-binding-system-unauthenticated)`] [`[--enable-master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-master-authorized-networks)` `[--master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--master-authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#NETWORK)`,…]] [`[--enable-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-private-endpoint)` `[--enable-private-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--enable-private-nodes)` `[--master-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--master-ipv4-cidr)`=`MASTER_IPV4_CIDR`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#ZONE)`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--scopes)`=[`SCOPE`,…]; default="gke-default" `[--service-account](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--service-account)`=`SERVICE_ACCOUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Autopilot cluster for running containers.

**EXAMPLES**

: To create a cluster with the default configuration, run:

```
gcloud container clusters create-auto sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the cluster to create.
The name may contain only lowercase alphanumerics and '-', must start with a
letter and end with an alphanumeric, and must be no longer than 40 characters.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-monitoring-scope**:
Enables Auto-Monitoring for a specific scope within the cluster. ALL: Enables
Auto-Monitoring for all supported workloads within the cluster. NONE: Disables
Auto-Monitoring. `AUTO_MONITORING_SCOPE` must be one of:
`ALL`, `NONE`.

**--autoprovisioning-enable-insecure-kubelet-readonly-port**:
Enables the Kubelet's insecure read only port for Autoprovisioned Node Pools.
If not set, the value from nodePoolDefaults.nodeConfigDefaults will be used.
To disable the readonly port
`--no-autoprovisioning-enable-insecure-kubelet-readonly-port`.

**--autoprovisioning-network-tags**:
Applies the given Compute Engine tags (comma separated) on all nodes in the
auto-provisioned node pools of the new Standard cluster or the new Autopilot
cluster.
Examples:

```
gcloud container clusters create-auto example-cluster --autoprovisioning-network-tags=tag1,tag2
```

New nodes in auto-provisioned node pools, including ones created by resize or
recreate, will have these tags on the Compute Engine API instance object and can
be used in firewall rules. See [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)
for examples.

**--autoprovisioning-resource-manager-tags**:
Applies the specified comma-separated resource manager tags that has the
GCE_FIREWALL purpose to all nodes in the new Autopilot cluster or all
auto-provisioned nodes in the new Standard cluster.
Examples:

```
gcloud container clusters create-auto example-cluster --autoprovisioning-resource-manager-tags=tagKeys/1234=tagValues/2345
gcloud container clusters create-auto example-cluster --autoprovisioning-resource-manager-tags=my-project/key1=value1
gcloud container clusters create-auto example-cluster --autoprovisioning-resource-manager-tags=12345/key1=value1,23456/key2=value2
gcloud container clusters create-auto example-cluster --autoprovisioning-resource-manager-tags=
```

All nodes in an Autopilot cluster or all auto-provisioned nodes in a Standard
cluster, including nodes that are resized or re-created, will have the specified
tags on the corresponding Instance object in the Compute Engine API. You can
reference these tags in network firewall policy rules. For instructions, see [https://cloud.google.com/firewall/docs/use-tags-for-firewalls](https://cloud.google.com/firewall/docs/use-tags-for-firewalls).

**--binauthz-evaluation-mode**

**--boot-disk-kms-key**:
The Customer Managed Encryption Key used to encrypt the boot disk attached to
each node in the node pool. This should be of the form
projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME].
For more information about protecting resources with Cloud KMS Keys please see:
[https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)

**--cluster-ipv4-cidr**:
The IP address range for the pods in this cluster in CIDR notation (e.g.
10.0.0.0/14). Prior to Kubernetes version 1.7.0 this must be a subset of
10.0.0.0/8; however, starting with version 1.7.0 can be any RFC 1918 IP range.
If you omit this option, a range is chosen automatically. The automatically
chosen range is randomly selected from 10.0.0.0/8 and will not include IP
address ranges allocated to VMs, existing routes, or ranges allocated to other
clusters. The automatically chosen range might conflict with reserved IP
addresses, dynamic routes, or routes within VPCs that peer with this cluster.
You should specify `--cluster-ipv4-cidr` to prevent conflicts.
This field is not applicable in a Shared VPC setup where the IP address range
for the pods must be specified with `--cluster-secondary-range-name`

**--cluster-secondary-range-name**:
Set the secondary range to be used as the source for pod IPs. Alias ranges will
be allocated from this secondary range. NAME must be the name of an existing
secondary range in the cluster subnetwork.
Cannot be used with '--create-subnetwork' option.

**--cluster-version**:
The Kubernetes version to use for the master and nodes. Defaults to
server-specified.
The default Kubernetes version is available using the following command.

```
gcloud container get-server-config
```

**--containerd-config-from-file**:
Path of the YAML file that contains containerd configuration entries like
configuring access to private image registries.
For detailed information on the configuration usage, please refer to [https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration](https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
Note: Updating the containerd configuration of an existing cluster or node pool
requires recreation of the existing nodes, which might cause disruptions in
running workloads.
Use a full or relative path to a local file containing the value of
containerd_config.

**--create-subnetwork**:
Create a new subnetwork for the cluster. The name and range of the subnetwork
can be customized via optional 'name' and 'range' key-value pairs.
'name' specifies the name of the subnetwork to be created.
'range' specifies the IP range for the new subnetwork. This can either be a
netmask size (e.g. '/20') or a CIDR range (e.g. '10.0.0.0/20'). If a netmask
size is specified, the IP is automatically taken from the free space in the
cluster's network.
Examples:
Create a new subnetwork with a default name and size.

```
gcloud container clusters create-auto --create-subnetwork ""
```

Create a new subnetwork named "my-subnet" with netmask of size 21.

```
gcloud container clusters create-auto --create-subnetwork name=my-subnet,range=/21
```

Create a new subnetwork with a default name with the primary range of
10.100.0.0/16.

```
gcloud container clusters create-auto --create-subnetwork range=10.100.0.0/16
```

Create a new subnetwork with the name "my-subnet" with a default range.

```
gcloud container clusters create-auto --create-subnetwork name=my-subnet
```

Cannot be used in conjunction with '--subnetwork' option.

**--database-encryption-key**:
Enable Database Encryption.
Enable database encryption that will be used to encrypt Kubernetes Secrets at
the application layer. The key provided should be the resource ID in the format
of
`projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]`.
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets](https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

**--disable-l4-lb-firewall-reconciliation**:
Disable reconciliation on the cluster for L4 Load Balancer VPC firewalls
targeting ingress traffic.

**--enable-authorized-networks-on-private-endpoint**:
Enable enforcement of --master-authorized-networks CIDR ranges for traffic
reaching cluster's control plane via private IP.

**--enable-backup-restore**:
Enable the Backup for GKE add-on. This add-on is disabled by default. To learn
more, see the Backup for GKE overview: [https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke](https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).

**--enable-cilium-clusterwide-network-policy**:
Enable Cilium Clusterwide Network Policies on the cluster. Disabled by default.

**--enable-dns-access**:
Enable access to the cluster's control plane over DNS-based endpoint.
DNS-based control plane access is recommended.

**--enable-fleet**:
Set cluster project as the fleet host project. This will register the cluster to
the same project. To register the cluster to a fleet in a different project,
please use `--fleet-project=FLEET_HOST_PROJECT`. Example: $ gcloud
container clusters create-auto --enable-fleet

**--enable-google-cloud-access**:
When you enable Google Cloud Access, any public IP addresses owned by Google
Cloud can reach the public control plane endpoint of your cluster.

**--enable-ip-access**:
Enable access to the cluster's control plane over private IP and public IP if
--enable-private-endpoint is not enabled.

**--enable-kubernetes-unstable-apis**:
Enable Kubernetes beta API features on this cluster. Beta APIs are not expected
to be production ready and should be avoided in production-grade environments.

**--enable-master-global-access**:
Use with private clusters to allow access to the master's private endpoint from
any Google Cloud region or on-premises environment regardless of the private
cluster's region.

**--enable-multi-networking**:
Enables multi-networking on the cluster. Multi-networking is disabled by
default.

**--enable-ray-cluster-logging**:
Enable automatic log processing sidecar for Ray clusters.

**--enable-ray-cluster-monitoring**:
Enable automatic metrics collection for Ray clusters.

**--enable-ray-operator**:
Enable the Ray Operator GKE add-on. This add-on is disabled by default.

**--enable-secret-manager**

**--fleet-project**:
Sets fleet host project for the cluster. If specified, the current cluster will
be registered as a fleet membership under the fleet host project.
Example: $ gcloud container clusters create-auto --fleet-project=my-project

**--hpa-profile**:
Set Horizontal Pod Autoscaler behavior. Accepted values are: none, performance.
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).

**--labels**:
Labels to apply to the Google Cloud resources in use by the Kubernetes Engine
cluster. These are unrelated to Kubernetes labels.
Examples:

```
gcloud container clusters create-auto example-cluster --labels=label_a=value1,label_b=,label_c=value3
```

**--logging**:
Set the components that have logging enabled. Valid component values are:
`SYSTEM`, `WORKLOAD`, `API_SERVER`,
`CONTROLLER_MANAGER`, `SCHEDULER`
The default is `SYSTEM,WORKLOAD`. If this flag is set, then
`SYSTEM` must be included.
For more information, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
Examples:

```
gcloud container clusters create-auto --logging=SYSTEM
gcloud container clusters create-auto --logging=SYSTEM,WORKLOAD
gcloud container clusters create-auto --logging=SYSTEM,WORKLOAD,API_SERVER,CONTROLLER_MANAGER,SCHEDULER
```

**--monitoring**:
Set the components that have monitoring enabled. Valid component values are:
`SYSTEM`, `WORKLOAD` (Deprecated), `NONE`,
`API_SERVER`, `CONTROLLER_MANAGER`,
`SCHEDULER`, `DAEMONSET`, `DEPLOYMENT`,
`HPA`, `POD`, `STATEFULSET`,
`STORAGE`, `CADVISOR`, `KUBELET`,
`DCGM`, `JOBSET`
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics)
Examples:

```
gcloud container clusters create-auto --monitoring=SYSTEM,API_SERVER,POD,DCGM
gcloud container clusters create-auto --monitoring=SYSTEM
```

**--network**:
The Compute Engine Network that the cluster will connect to. Google Kubernetes
Engine will use this network when creating routes and firewalls for the
clusters. Defaults to the 'default' network.

**--private-endpoint-subnetwork**:
Sets the subnetwork GKE uses to provision the control plane's private endpoint.

**--release-channel**:
Release channel a cluster is subscribed to.
If left unspecified and a version is specified, the cluster is enrolled in the
most mature release channel where the version is available (first checking
STABLE, then REGULAR, and finally RAPID). Otherwise, if no release channel and
no version is specified, the cluster is enrolled in the REGULAR channel with its
default version. When a cluster is subscribed to a release channel, Google
maintains both the master version and the node version. Node auto-upgrade is
enabled by default for release channel clusters and can be controlled via [upgrade-scope
exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude).
CHANNEL must be one of:
`rapid`

```
'rapid' channel is offered on an early access basis for customers
who want to test new releases.
```

```
WARNING: Versions available in the 'rapid' channel may be subject
to unresolved issues with no known workaround and are not subject
to any SLAs.
```

`regular`

```
Clusters subscribed to 'regular' receive versions that are
considered GA quality. 'regular' is intended for production users
who want to take advantage of new features.
```

`extended`

```
Clusters subscribed to 'extended' can remain on a minor version for 24 months
from when the minor version is made available in the Regular channel.
```

`stable`

```
Clusters subscribed to 'stable' receive versions that are known to
be stable and reliable in production.
```

`CHANNEL` must be one of: `rapid`,
`regular`, `extended`, `stable`.

**--security-group**:
The name of the RBAC security group for use with Google security groups in
Kubernetes RBAC (https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
To include group membership as part of the claims issued by Google during
authentication, a group must be designated as a security group by including it
as a direct member of this group.
If unspecified, no groups will be returned for use with RBAC.

**--security-posture**:
Sets the mode of the Kubernetes security posture API's off-cluster features.
To enable advanced mode explicitly set the flag to
`--security-posture=enterprise`.
To enable in standard mode explicitly set the flag to
`--security-posture=standard`
To disable in an existing cluster, explicitly set the flag to
`--security-posture=disabled`.
For more information on enablement, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement](https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement).
`SECURITY_POSTURE` must be one of: `disabled`,
`standard`, `enterprise`.

**--services-ipv4-cidr**:
Set the IP range for the services IPs.
Can be specified as a netmask size (e.g. '/20') or as in CIDR notion (e.g.
'10.100.0.0/20'). If given as a netmask size, the IP range will be chosen
automatically from the available space in the network.
If unspecified, the services CIDR range will be chosen with a default mask size.

**--services-secondary-range-name**:
Set the secondary range to be used for services (e.g. ClusterIPs). NAME must be
the name of an existing secondary range in the cluster subnetwork.
Cannot be used with '--create-subnetwork' option.

**--subnetwork**:
The Google Compute Engine subnetwork
(https://cloud.google.com/compute/docs/subnetworks) to which the cluster is
connected. The subnetwork must belong to the network specified by --network.
Cannot be used with the "--create-subnetwork" option.

**--tier**:
Set the desired tier for the cluster. `TIER` must be one
of: `standard`, `enterprise`.

**--workload-policies**:
Add Autopilot workload policies to the cluster.
Examples:

```
gcloud container clusters create-auto example-cluster --workload-policies=allow-net-admin
```

The only supported workload policy is 'allow-net-admin'.

**--workload-vulnerability-scanning**:
Sets the mode of the Kubernetes security posture API's workload vulnerability
scanning.
To enable Advanced vulnerability insights mode explicitly set the flag to
`--workload-vulnerability-scanning=enterprise`.
To enable in standard mode explicitly set the flag to
`--workload-vulnerability-scanning=standard`.
To disable in an existing cluster, explicitly set the flag to
`--workload-vulnerability-scanning=disabled`.
For more information on enablement, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement](https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement).
`WORKLOAD_VULNERABILITY_SCANNING` must be one of:
`disabled`, `standard`, `enterprise`.

**--additive-vpc-scope-dns-domain**

**--aggregation-ca**

**--dataplane-v2-observability-mode**

**--enable-insecure-binding-system-authenticated**:
Allow using `system:authenticated` as a subject in
ClusterRoleBindings and RoleBindings. Allowing bindings that reference
`system:authenticated` is a security risk and is not recommended.
To disallow binding `system:authenticated` in a cluster, explicitly
set the `--no-enable-insecure-binding-system-authenticated` flag
instead.

**--enable-insecure-binding-system-unauthenticated**:
Allow using `system:unauthenticated` and
`system:anonymous` as subjects in ClusterRoleBindings and
RoleBindings. Allowing bindings that reference
`system:unauthenticated` and `system:anonymous` are a
security risk and is not recommended.
To disallow binding `system:authenticated` in a cluster, explicitly
set the `--no-enable-insecure-binding-system-unauthenticated` flag
instead.

**--enable-master-authorized-networks**

**--enable-private-endpoint**

**--location**

**--scopes**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha container clusters create-auto
```

```
gcloud beta container clusters create-auto
```