# gcloud container node-pools rollback  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback)*

**NAME**

: **gcloud container node-pools rollback - rollback a node-pool upgrade**

**SYNOPSIS**

: **`gcloud container node-pools rollback` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--async)`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--cluster)`=`CLUSTER`] [`[--respect-pdb](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--respect-pdb)`=`RESPECT_PDB`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Rollback a node-pool upgrade.
Rollback is a method used after a canceled or failed node-pool upgrade. It makes
a best-effort attempt to revert the pool back to its original state.

**EXAMPLES**

: To roll back a canceled or failed upgrade in "node-pool-1" in the cluster
"sample-cluster", run:

```
gcloud container node-pools rollback node-pool-1 --cluster=sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the node pool to rollback.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster**:
The cluster from which to rollback the node pool. Overrides the default
`container/cluster` property value for this command invocation.

**--respect-pdb**:
Indicates whether node pool rollbacks should respect pod disruption budgets.

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
gcloud alpha container node-pools rollback
```

```
gcloud beta container node-pools rollback
```