# gcloud bigtable clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create)*

**NAME**

: **gcloud bigtable clusters create - create a bigtable cluster**

**SYNOPSIS**

: **`gcloud bigtable clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#CLUSTER)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--instance)`=`INSTANCE`) `[--zone](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--zone)`=`ZONE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--async)`] [`[--node-scaling-factor](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--node-scaling-factor)`=`NODE_SCALING_FACTOR`; default="node-scaling-factor-1x"] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--kms-project)`=`KMS_PROJECT`] [`[--num-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--num-nodes)`=`NUM_NODES`; default=3     | [`[--autoscaling-cpu-target](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--autoscaling-cpu-target)`=`AUTOSCALING_CPU_TARGET` `[--autoscaling-max-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--autoscaling-max-nodes)`=`AUTOSCALING_MAX_NODES` `[--autoscaling-min-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--autoscaling-min-nodes)`=`AUTOSCALING_MIN_NODES` : `[--autoscaling-storage-target](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#--autoscaling-storage-target)`=`AUTOSCALING_STORAGE_TARGET`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a bigtable cluster.

**EXAMPLES**

: To add a cluster in zone `us-east1-c` to the instance with id
`my-instance-id`, run:

```
gcloud bigtable clusters create my-cluster-id --instance=my-instance-id --zone=us-east1-c
```

To add a cluster with `10` nodes, run:

```
gcloud bigtable clusters create my-cluster-id --instance=my-instance-id --zone=us-east1-c --num-nodes=10
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The cluster to describe. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

**--instance**:
Bigtable instance for the cluster.
To set the `instance` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

**REQUIRED FLAGS**

: **--zone**:
ID of the zone where the cluster is located. Supported zones are listed at [https://cloud.google.com/bigtable/docs/locations](https://cloud.google.com/bigtable/docs/locations).

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--node-scaling-factor**:
Node scaling factor for the cluster. `NODE_SCALING_FACTOR`
must be one of: `node-scaling-factor-1x`,
`node-scaling-factor-2x`.

**--kms-key**

**--num-nodes**

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
gcloud alpha bigtable clusters create
```

```
gcloud beta bigtable clusters create
```