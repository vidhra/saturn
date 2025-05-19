# gcloud bigtable clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update)*

**NAME**

: **gcloud bigtable clusters update - update a Bigtable cluster's number of nodes**

**SYNOPSIS**

: **`gcloud bigtable clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#CLUSTER)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--instance)`=`INSTANCE`) (`[--autoscaling-cpu-target](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--autoscaling-cpu-target)`=`AUTOSCALING_CPU_TARGET` `[--autoscaling-max-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--autoscaling-max-nodes)`=`AUTOSCALING_MAX_NODES` `[--autoscaling-min-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--autoscaling-min-nodes)`=`AUTOSCALING_MIN_NODES` `[--autoscaling-storage-target](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--autoscaling-storage-target)`=`AUTOSCALING_STORAGE_TARGET`     | [`[--num-nodes](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--num-nodes)`=`NUM_NODES` : `[--disable-autoscaling](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--disable-autoscaling)`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Bigtable cluster's number of nodes.

**EXAMPLES**

: To update a cluster to `10` nodes, run:

```
gcloud bigtable clusters update my-cluster-id --instance=my-instance-id --num-nodes=10
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The cluster to update. The arguments in this group can be
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

: **--autoscaling-cpu-target**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha bigtable clusters update
```

```
gcloud beta bigtable clusters update
```