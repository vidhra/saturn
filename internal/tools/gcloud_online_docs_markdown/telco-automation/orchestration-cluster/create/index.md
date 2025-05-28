# gcloud telco-automation orchestration-cluster create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create)*

**NAME**

: **gcloud telco-automation orchestration-cluster create - create a telco automation orchestration cluster**

**SYNOPSIS**

: **`gcloud telco-automation orchestration-cluster create` (`[ORCHESTRATION_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#ORCHESTRATION_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--async)`] [`[--cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--cidr-blocks)`=[`cidr-block`=`CIDR-BLOCK`],[`display-name`=`DISPLAY-NAME`]] [`[--cluster-cidr-block](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--cluster-cidr-block)`=`CLUSTER_CIDR_BLOCK`] [`[--cluster-named-range](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--cluster-named-range)`=`CLUSTER_NAMED_RANGE`] [`[--full-management-config](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--full-management-config)`] [`[--master-ipv4-cidr-block](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--master-ipv4-cidr-block)`=`MASTER_IPV4_CIDR_BLOCK`] [`[--services-cidr-block](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--services-cidr-block)`=`SERVICES_CIDR_BLOCK`] [`[--services-named-range](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--services-named-range)`=`SERVICES_NAMED_RANGE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--network)`=`NETWORK` : `[--subnet](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/telco-automation/orchestration-cluster/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new telco automation orchestration cluster.

**EXAMPLES**

: To create an orchestration cluster called `test-orchestrationCluster`
in location `us-central1`, run:

```
gcloud telco-automation orchestration-cluster create test-orchestrationCluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Orchestration Cluster resource - Telco automation orchestration cluster to
create. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `orchestration_cluster` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ORCHESTRATION_CLUSTER`**:
ID of the Orchestration Cluster or fully qualified identifier for the
Orchestration Cluster.
To set the `orchestration_cluster` attribute:

- provide the argument `orchestration_cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `orchestration_cluster` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cidr-blocks**:
Master Authorized Network that supports multiple CIDR blocks. Allows access to
the k8s master from multiple blocks.

**--cluster-cidr-block**:
IP address range for the cluster pod IPs. Set to blank to have a range chosen
with the default size. Set to /netmask (e.g. /14) to have a range chosen with a
specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918
private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a
specific range to use.

**--cluster-named-range**:
Name of the existing secondary range in the cluster's subnetwork to use for pod
IP addresses. Alternatively, cluster_cidr_block can be used to automatically
create a GKE-managed one.

**--full-management-config**:
This parameter is to marked true only if the management configuration arguments
which are provided, belong to full (Autopilot) cluster management.

**--master-ipv4-cidr-block**:
/28 network that the control plane will use.

**--services-cidr-block**:
IP address range for the cluster service IPs. Set to blank to have a range
chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen
with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the
RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.

**--services-named-range**:
Name of the existing secondary range in the cluster's subnetwork to use for
service ClusterIPs. Alternatively, services_cidr_block can be used to
automatically create a GKE-managed one.

**--network**:
Name of the VPC Network to put the GKE cluster and nodes in. The VPC will be
created if it doesn't exist.

**--subnet**:
Specifies the subnet that the interface will be part of. Network key must be
specified and the subnet must be a subnetwork of the specified network.

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

**API REFERENCE**

: This command uses the `telcoautomation/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native](https://cloud.google.com/blog/topics/telecommunications/network-automation-csps-linus-nephio-cloud-native)

**NOTES**

: This variant is also available:

```
gcloud alpha telco-automation orchestration-cluster create
```