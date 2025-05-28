# gcloud bigtable instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create)*

**NAME**

: **gcloud bigtable instances create - create a new Bigtable instance**

**SYNOPSIS**

: **`gcloud bigtable instances create` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#INSTANCE)` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--display-name)`=`DISPLAY_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--async)`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--cluster)`=`CLUSTER`] [`[--cluster-config](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--cluster-config)`=[`id`=`ID`,`zone`=`ZONE`,[`nodes`=`NODES`],[`node-scaling-factor`=`NODE_SCALING_FACTOR`],[`kms-key`=`KMS_KEY`],[`autoscaling-min-nodes`=`AUTOSCALING_MIN_NODES`,`autoscaling-max-nodes`=`AUTOSCALING_MAX_NODES`,`autoscaling-cpu-target`=`AUTOSCALING_CPU_TARGET`,`autoscaling-storage-target`=`AUTOSCALING_STORAGE_TARGET`],…]] [`[--cluster-num-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--cluster-num-nodes)`=`CLUSTER_NUM_NODES`] [`[--cluster-storage-type](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--cluster-storage-type)`=`CLUSTER_STORAGE_TYPE`; default="ssd"] [`[--cluster-zone](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--cluster-zone)`=`CLUSTER_ZONE`] [`[--instance-type](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#--instance-type)`=`INSTANCE_TYPE`; default="PRODUCTION"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Bigtable instance.

**EXAMPLES**

: To create an instance with id `my-instance-id` with a cluster located
in `us-east1-c`, run:

```
gcloud bigtable instances create my-instance-id --display-name="My Instance" --cluster-config=id=my-cluster-id,zone=us-east1-c
```

To create an instance with multiple clusters, run:

```
gcloud bigtable instances create my-instance-id --display-name="My Instance" --cluster-config=id=my-cluster-id-1,zone=us-east1-c --cluster-config=id=my-cluster-id-2,zone=us-west1-c,nodes=3
```

To create an instance with `HDD` storage and `10` nodes,
run:

```
gcloud bigtable instances create my-hdd-instance --display-name="HDD Instance" --cluster-storage-type=HDD --cluster-config=id=my-cluster-id,zone=us-east1-c,nodes=10
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The instance to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
Friendly name of the instance.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster**:
(DEPRECATED) ID of the cluster
The --cluster argument is deprecated; use --cluster-config instead.

**--cluster-config**:
`Repeatable`. Specify cluster config as a key-value dictionary.
This is the recommended argument for specifying cluster configurations.
Keys can be:

```
*id*: Required. The ID of the cluster.
```

```
*zone*: Required. ID of the zone where the cluster is located. Supported zones are listed at https://cloud.google.com/bigtable/docs/locations.
```

```
*nodes*: The number of nodes in the cluster. Default=1.
```

```
*node-scaling-factor*: The node scaling factor for the cluster. Default=node-scaling-factor-1x. NODE_SCALING_FACTOR must be one of: node-scaling-factor-1x, node-scaling-factor-2x.
```

```
*kms-key*: The Cloud KMS (Key Management Service) cryptokey that will be used to protect the cluster.
```

```
*autoscaling-min-nodes*: The minimum number of nodes for autoscaling.
```

```
*autoscaling-max-nodes*: The maximum number of nodes for autoscaling.
```

```
*autoscaling-cpu-target*: The target CPU utilization percentage for autoscaling. Accepted values are from 10 to 80.
```

```
*autoscaling-storage-target*: The target storage utilization gibibytes per node for autoscaling. Accepted values are from 2560 to 5120 for SSD clusters and 8192 to 16384 for HDD clusters.
```

If this argument is specified, the deprecated arguments for configuring a single
cluster will be ignored, including `--cluster`,
`--cluster-zone`, `--cluster-num-nodes`.
See `EXAMPLES` section.

**--cluster-num-nodes**:
(DEPRECATED) Number of nodes to serve.
The --cluster-num-nodes argument is deprecated; use --cluster-config instead.

**--cluster-storage-type**:
Storage class for the cluster. `CLUSTER_STORAGE_TYPE` must
be one of: `hdd`, `ssd`.

**--cluster-zone**:
(DEPRECATED) ID of the zone where the cluster is located. Supported zones are
listed at [https://cloud.google.com/bigtable/docs/locations](https://cloud.google.com/bigtable/docs/locations).
The --cluster-zone argument is deprecated; use --cluster-config instead.

**--instance-type**:
(DEPRECATED) The type of instance to create.
The --instance-type argument is deprecated. DEVELOPMENT instances are no longer
offered. All instances are of type PRODUCTION.
`INSTANCE_TYPE` must be one of:

**`DEVELOPMENT`**:
Development instances are low-cost instances meant for development and testing
only. They do not provide high availability and no service level agreement
applies.

**`PRODUCTION`**:
Production instances provide high availability and are suitable for applications
in production. Production instances created with the --instance-type argument
have 3 nodes if a value is not provided for --cluster-num-nodes.

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
gcloud alpha bigtable instances create
```

```
gcloud beta bigtable instances create
```