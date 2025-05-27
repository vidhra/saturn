# gcloud container node-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete)*

**NAME**

: **gcloud container node-pools delete - delete an existing node pool in a running cluster**

**SYNOPSIS**

: **`gcloud container node-pools delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#--async)`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#--cluster)`=`CLUSTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud container node-pools delete` deletes a node pool from a
Google Kubernetes Engine (GKE) cluster. When you delete a node pool, GKE drains
all the nodes in the node pool. The draining process involves GKE deleting Pods
on each node in the node pool. Each node in a node pool is drained by deleting
Pods with an allotted graceful termination period of `MAX_POD`.
`MAX_POD` is the maximum `terminationGracePeriodSeconds`
set on the Pods scheduled to the node with a cap of one hour.

**EXAMPLES**

: To delete the "node-pool-1" node pool from the cluster "sample-cluster", run:

```
gcloud container node-pools delete node-pool-1 --cluster=sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the node pool to delete.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster**:
The cluster from which to delete the node pool. Overrides the default
`container/cluster` property value for this command invocation.

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
gcloud alpha container node-pools delete
```

```
gcloud beta container node-pools delete
```