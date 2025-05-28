# gcloud container clusters resize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize)*

**NAME**

: **gcloud container clusters resize - resizes an existing cluster for running containers**

**SYNOPSIS**

: **`gcloud container clusters resize` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#NAME)` (`[--num-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--num-nodes)`=`NUM_NODES`     | `[--size](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--size)`=`NUM_NODES`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--async)`] [`[--node-pool](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--node-pool)`=`NODE_POOL`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/resize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Resize an existing cluster to a provided size.
If you have multiple node pools, you must specify which node pool to resize by
using the --node-pool flag. You are not required to use the flag if you have a
single node pool.
When increasing the size of a container cluster, the new instances are created
with the same configuration as the existing instances. Existing pods are not
moved onto the new instances, but new pods (such as those created by resizing a
replication controller) will be scheduled onto the new instances.
When decreasing a cluster, the nodes are drained. As a result, the pods running
on these nodes are gracefully terminated. If your pods are being managed by a
workload controller, the controller will attempt to reschedule them onto the
remaining instances. If your pods are not managed by a workload controller, they
will not be restarted. Note that when resizing down, instances running pods and
instances without pods are not differentiated. Resize will pick instances to
remove at random.
When you resize a node pool that spans multiple zones, the new size represents
the number of nodes in the node pool per zone. For example, if you have a node
pool of size 2 spanning two zones, the total node count is 4. If you resize the
node pool with `--num-nodes=4`, the total node count becomes 8.

**EXAMPLES**

: To resize the default node pool of an existing cluster, run:

```
gcloud container clusters resize sample-cluster --num-nodes=2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of this cluster.

**REQUIRED FLAGS**

: **--num-nodes**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--node-pool**:
The node pool to resize.

**--location**

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
gcloud alpha container clusters resize
```

```
gcloud beta container clusters resize
```