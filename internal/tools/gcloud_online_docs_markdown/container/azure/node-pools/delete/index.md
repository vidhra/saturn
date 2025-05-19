# gcloud container azure node-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete)*

**NAME**

: **gcloud container azure node-pools delete - delete a node pool in an Anthos cluster on Azure**

**SYNOPSIS**

: **`gcloud container azure node-pools delete` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#--location)`=`LOCATION`) [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#--async)`] [`[--ignore-errors](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#--ignore-errors)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Delete a node pool in an Anthos cluster on Azure.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To delete a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container azure node-pools delete my-node-pool --cluster=my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Nodepool resource - node pool to delete. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_POOL`**:
ID of the nodepool or fully qualified identifier for the nodepool.
To set the `nodepool` attribute:

- provide the argument `node_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
cluster of the nodepool.
To set the `cluster` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
Google Cloud location for the nodepool.
To set the `location` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_azure/location`.**

**FLAGS**

: **--allow-missing**:
Allow idempotent deletion of node pool. The request will still succeed in case
the node pool does not exist.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--ignore-errors**:
Force delete an Azure node pool. Deletion of the Azure node pool will succeed
even if errors occur during deleting in-node pool resources. Using this
parameter may result in orphaned resources in the node pool.

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

: This variant is also available:

```
gcloud alpha container azure node-pools delete
```