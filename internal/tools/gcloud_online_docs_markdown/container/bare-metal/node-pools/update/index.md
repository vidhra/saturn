# gcloud container bare-metal node-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update)*

**NAME**

: **gcloud container bare-metal node-pools update - update a node pool in an Anthos cluster on bare metal**

**SYNOPSIS**

: **`gcloud container bare-metal node-pools update` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--location)`=`LOCATION`) [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--display-name)`=`DISPLAY_NAME`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--validate-only)`] [`[--node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--node-labels)`=[`KEY`=`VALUE`,…] `[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#EFFECT)`,…] `[--registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--registry-burst)`=`REGISTRY_BURST` `[--registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--registry-pull-qps)`=`REGISTRY_PULL_QPS` `[--disable-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--disable-serialize-image-pulls)`     | `[--enable-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#--enable-serialize-image-pulls)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a node pool in an Anthos cluster on bare metal.

**EXAMPLES**

: To update a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container bare-metal node-pools update my-node-pool --cluster=my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - node pool to update The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_POOL`**:
ID of the node_pool or fully qualified identifier for the node_pool.
To set the `node_pool` attribute:

- provide the argument `node_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
cluster of the node_pool.
To set the `cluster` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
Google Cloud location for the node_pool.
To set the `location` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_bare_metal/location`.**

**FLAGS**

: **--allow-missing**:
If set, and the Anthos cluster on bare metal is not found, the update request
will try to create a new cluster with the provided configuration.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
Display name for the resource.

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

**--node-configs**

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
gcloud alpha container bare-metal node-pools update
```

```
gcloud beta container bare-metal node-pools update
```