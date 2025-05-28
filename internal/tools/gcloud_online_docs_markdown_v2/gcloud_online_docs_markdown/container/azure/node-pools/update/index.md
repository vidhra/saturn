# gcloud container azure node-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update)*

**NAME**

: **gcloud container azure node-pools update - update a node pool in an Anthos cluster on Azure**

**SYNOPSIS**

: **`gcloud container azure node-pools update` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--async)`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--enable-autorepair)`] [`[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--node-version)`=`NODE_VERSION`] [`[--ssh-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--ssh-public-key)`=`SSH_PUBLIC_KEY`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--validate-only)`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#ANNOTATION)`,…]     | `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--clear-annotations)`] [`[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#--min-nodes)`=`MIN_NODES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Update a node pool in an Anthos cluster on Azure.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To update a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container azure node-pools update my-node-pool --cluster=my-cluster --location=us-west1 --node-version=NODE_VERSION
```

**POSITIONAL ARGUMENTS**

: **Nodepool resource - node pool to update. The arguments in this group can be used
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

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-autorepair**:
Enable node autorepair feature for a node pool. Use --no-enable-autorepair to
disable.

```
gcloud container azure node-pools update --enable-autorepair
```

**--node-version**:
Kubernetes version to use for the node pool.

**--ssh-public-key**:
SSH public key to use for authentication.

**--validate-only**:
Validate the update of the node pool, but don't actually perform it.

**--annotations**

**--max-nodes**

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
gcloud alpha container azure node-pools update
```