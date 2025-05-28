# gcloud vmware private-clouds create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create)*

**NAME**

: **gcloud vmware private-clouds create - create a VMware Engine private cloud**

**SYNOPSIS**

: **`gcloud vmware private-clouds create` (`[PRIVATE_CLOUD](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#PRIVATE_CLOUD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--location)`=`LOCATION`) `[--cluster](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--cluster)`=`CLUSTER` `[--management-range](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--management-range)`=`MANAGEMENT_RANGE` `[--node-type-config](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--node-type-config)`=[`count`=`COUNT`],[`custom-core-count`=`CUSTOM-CORE-COUNT`],[`type`=`TYPE`] `[--vmware-engine-network](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--vmware-engine-network)`=`VMWARE_ENGINE_NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--description)`=`DESCRIPTION`] [`[--preferred-zone](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--preferred-zone)`=`PREFERRED_ZONE`] [`[--secondary-zone](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--secondary-zone)`=`SECONDARY_ZONE`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#--type)`=`TYPE`; default="STANDARD"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a VMware Engine private cloud. Private cloud creation is considered
finished when the private cloud is in READY state. Check the progress of a
private cloud using `[gcloud vmware
private-clouds list](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/list)`.

**EXAMPLES**

: To create a private cloud in the `us-west2-a` zone using
`standard-72` nodes that connects to the `my-network`
VMware Engine network, run:

```
gcloud vmware private-clouds create my-private-cloud --location=us-west2-a --project=my-project --cluster=my-management-cluster --node-type-config=type=standard-72,count=3 --management-range=192.168.0.0/24 --vmware-engine-network=my-network
```

Or:

```
gcloud vmware private-clouds create my-private-cloud --cluster=my-management-cluster --node-type-config=type=standard-72,count=3 --management-range=192.168.0.0/24 --vmware-engine-network=my-network
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/zone.
To create a stretched private cloud in the `us-west2` region using
`us-west2-a` zone as preferred and `us-west2-b` zone as
secondary

```
gcloud vmware private-clouds create my-private-cloud --project=sample-project --location=us-west2 --cluster=my-management-cluster --node-type-config=type=standard-72,count=6 --management-range=192.168.0.0/24 --vmware-engine-network=my-network --type=STRETCHED --preferred-zone=us-west2-a --secondary-zone=us-west2-b
```

The project is taken from gcloud properties core/project.

**POSITIONAL ARGUMENTS**

: **Private cloud resource - private_cloud. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `private_cloud` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PRIVATE_CLOUD`**:
ID of the private cloud or fully qualified identifier for the private cloud.
To set the `private-cloud` attribute:

- provide the argument `private_cloud` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `private_cloud` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

**REQUIRED FLAGS**

: **Cluster resource - cluster. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- set the property `compute/zone`.

To set the `private-cloud` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name.

This must be specified.

**--cluster**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `--cluster` on the command line.**

**--management-range**:
IP address range in the private cloud to use for management appliances, in CIDR
format. Use an IP address range that meets the [VMware
Engine networking requirements](https://cloud.google.com/vmware-engine/docs/quickstart-networking-requirements).

**--node-type-config**:
Information about the type and number of nodes associated with the cluster.
type (required): canonical identifier of the node type.
count (required): number of nodes of this type in the cluster.
custom-core-count (optional): customized number of cores available to each node
of the type. To get a list of valid values for your node type, run the gcloud
vmware node-types describe command and reference the availableCustomCoreCounts
field in the output.

**--vmware-engine-network**:
Resource ID of the VMware Engine network attached to the private cloud.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Text describing the private cloud.

**--preferred-zone**:
Zone that will remain operational when connection between the two zones is lost.
Specify the resource name of a zone that belongs to the region of the private
cloud.

**--secondary-zone**:
Additional zone for a higher level of availability and load balancing. Specify
the resource name of a zone that belongs to the region of the private cloud.

**--type**:
Type of the private cloud. `TYPE` must be one of:

**`STANDARD`**:
Standard private is a zonal resource, with 3 or more nodes nodes. Default type.

**`STRETCHED`**:
Stretched private cloud is a regional resource with redundancy, with a minimum
of 6 nodes, nodes count has to be even.

**`TIME_LIMITED`**:
Time limited private cloud is a zonal resource, can have only 1 node and has
limited life span. Will be deleted after defined period of time, can be
converted into standard private cloud by expanding it up to 3 or more nodes.

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