# gcloud vmware private-clouds clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update)*

**NAME**

: **gcloud vmware private-clouds clusters update - update a Google Cloud VMware Engine cluster**

**SYNOPSIS**

: **`gcloud vmware private-clouds clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--private-cloud)`=`PRIVATE_CLOUD`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--async)`] [`[--node-type-config](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--node-type-config)`=[[`count`=`COUNT`],[`type`=`TYPE`],…]] [`[--remove-autoscaling-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--remove-autoscaling-policy)`=`NAME`] [`[--remove-nodes-config](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--remove-nodes-config)`=`TYPE`] [`[--update-nodes-config](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--update-nodes-config)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--autoscaling-settings-from-file](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--autoscaling-settings-from-file)`=`AUTOSCALING_SETTINGS_FROM_FILE`     | `[--autoscaling-cool-down-period](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--autoscaling-cool-down-period)`=`AUTOSCALING_COOL_DOWN_PERIOD` `[--autoscaling-max-cluster-node-count](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--autoscaling-max-cluster-node-count)`=`AUTOSCALING_MAX_CLUSTER_NODE_COUNT` `[--autoscaling-min-cluster-node-count](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--autoscaling-min-cluster-node-count)`=`AUTOSCALING_MIN_CLUSTER_NODE_COUNT` `[--update-autoscaling-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#--update-autoscaling-policy)`=[`consumed-memory-thresholds-scale-in`=`CONSUMED-MEMORY-THRESHOLDS-SCALE-IN`],[`consumed-memory-thresholds-scale-out`=`CONSUMED-MEMORY-THRESHOLDS-SCALE-OUT`],[`cpu-thresholds-scale-in`=`CPU-THRESHOLDS-SCALE-IN`],[`cpu-thresholds-scale-out`=`CPU-THRESHOLDS-SCALE-OUT`],[`granted-memory-thresholds-scale-in`=`GRANTED-MEMORY-THRESHOLDS-SCALE-IN`],[`granted-memory-thresholds-scale-out`=`GRANTED-MEMORY-THRESHOLDS-SCALE-OUT`],[`max-node-count`=`MAX-NODE-COUNT`],[`min-node-count`=`MIN-NODE-COUNT`],[`name`=`NAME`],[`node-type-id`=`NODE-TYPE-ID`],[`scale-out-size`=`SCALE-OUT-SIZE`],[`storage-thresholds-scale-in`=`STORAGE-THRESHOLDS-SCALE-IN`],[`storage-thresholds-scale-out`=`STORAGE-THRESHOLDS-SCALE-OUT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Adjust the number of nodes in the VMware Engine cluster. Successful addition or
removal of a node results in a cluster in READY state. Check the progress of a
cluster using `[gcloud vmware
private-clouds clusters list](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/list)`.

**EXAMPLES**

: To resize a cluster called `my-cluster` in private cloud
`my-private-cloud` and zone `us-west2-a` to have
`3` nodes of type `standard-72`, run:

```
gcloud vmware private-clouds clusters update my-cluster --location=us-west2-a --project=my-project --private-cloud=my-private-cloud --update-nodes-config=type=standard-72,count=3
```

```
Or:
```

```
gcloud vmware private-clouds clusters update my-cluster --private-cloud=my-private-cloud --update-nodes-config=type=standard-72,count=3
```

```
In the second example, the project and location are taken from gcloud properties core/project and compute/zone.
```

To enable autoscale in a cluster called `my-cluster` in private cloud
`my-private-cloud` and zone `us-west2-a`, run:

```
gcloud vmware private-clouds clusters update my-cluster --location=us-west2-a --project=my-project --private-cloud=my-private-cloud --autoscaling-min-cluster-node-count=3 --autoscaling-max-cluster-node-count=5 --update-autoscaling-policy=name=custom-policy,node-type-id=standard-72,scale-out-size=1,storage-thresholds-scale-in=10,storage-thresholds-scale-out=80
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--private-cloud` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--node-type-config**:
(DEPRECATED) Information about the type and number of nodes associated with the
cluster.

```
type (required): canonical identifier of the node type.
```

```
count (required): number of nodes of this type in the cluster.
```

```
custom_core_count: can be passed, but the value will be ignored. Updating custom core count is not supported.
```

The --node-type-config option is deprecated; please use --update-nodes-config
and --remove-nodes-config instead.

**--remove-autoscaling-policy**:
Names of autoscaling policies that should be removed from the cluster

**--remove-nodes-config**:
Type of node that should be removed from the cluster

**--update-nodes-config**:
Information about the type and number of nodes associated with the cluster.
type (required): canonical identifier of the node type.
count (required): number of nodes of this type in the cluster.

**--autoscaling-settings-from-file**

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