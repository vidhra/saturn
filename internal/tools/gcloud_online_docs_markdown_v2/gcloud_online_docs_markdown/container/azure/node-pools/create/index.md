# gcloud container azure node-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create)*

**NAME**

: **gcloud container azure node-pools create - create a node pool in an Anthos cluster on Azure**

**SYNOPSIS**

: **`gcloud container azure node-pools create` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--location)`=`LOCATION`) `[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE` `[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--node-version)`=`NODE_VERSION` `[--ssh-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--ssh-public-key)`=`SSH_PUBLIC_KEY` `[--subnet-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--subnet-id)`=`SUBNET_ID` (`[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--min-nodes)`=`MIN_NODES`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#ANNOTATION)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--async)`] [`[--azure-availability-zone](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--azure-availability-zone)`=`AZURE_AVAILABILITY_ZONE`] [`[--config-encryption-key-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--config-encryption-key-id)`=`CONFIG_ENCRYPTION_KEY_ID`] [`[--config-encryption-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--config-encryption-public-key)`=`CONFIG_ENCRYPTION_PUBLIC_KEY`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--enable-autorepair)`] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--node-labels)`=`NODE_LABEL`,[`[NODE_LABEL](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#NODE_LABEL)`,…]] [`[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--node-taints)`=`NODE_TAINT`,[`[NODE_TAINT](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#NODE_TAINT)`,…]] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#TAG)`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--validate-only)`] [`[--vm-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--vm-size)`=`VM_SIZE`] [`[--proxy-resource-group-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--proxy-resource-group-id)`=`PROXY_RESOURCE_GROUP_ID` `[--proxy-secret-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--proxy-secret-id)`=`PROXY_SECRET_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Create a node pool in an Anthos cluster on Azure.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To create a node pool named ``my-node-pool`` in
a cluster named ``my-cluster`` managed in
location ``us-west1``, run:

```
gcloud container azure node-pools create my-node-pool --cluster=my-cluster --location=us-west1 --node-version=NODE_VERSION --ssh-public-key=SSH_PUBLIC_KEY --subnet-id=SUBNET_ID
```

**POSITIONAL ARGUMENTS**

: **Nodepool resource - node pool to create. The arguments in this group can be used
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

**REQUIRED FLAGS**

: **--max-pods-per-node**:
Maximum number of pods per node.

**--node-version**:
Kubernetes version to use for the node pool.

**--ssh-public-key**:
SSH public key to use for authentication.

**--subnet-id**:
Subnet ID of an existing VNET to use for the node pool.

**--max-nodes**

**OPTIONAL FLAGS**

: **--annotations**:
Annotations for the node pool.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--azure-availability-zone**:
Azure availability zone where the node pool will be created.

**--config-encryption-key-id**:
URL the of the Azure Key Vault key (with its version) to use to encrypt /
decrypt config data.

**--config-encryption-public-key**:
RSA key of the Azure Key Vault public key to use for encrypting config data.

**--enable-autorepair**:
Enable node autorepair feature for a node pool. Use --no-enable-autorepair to
disable.

```
gcloud container azure node-pools create --enable-autorepair
```

Node autorepair is disabled by default.

**--node-labels**:
Labels assigned to the node pool's nodes.

**--node-taints**:
Taints assigned to nodes of the node pool. Node taint is of format
key=value:effect. Effect must be one of: NoExecute, NoSchedule,
PreferNoSchedule.

**--root-volume-size**:
Size of the root volume. The value must be a whole number followed by a size
unit of `GB` for gigabyte, or `TB` for terabyte. If no
size unit is specified, GB is assumed.

**--tags**:
Applies the given tags (comma separated) on the node pool. Example:

```
gcloud container azure node-pools create EXAMPLE_NODE_POOL --tags=tag1=one,tag2=two
```

**--validate-only**:
Validate the creation of the node pool, but don't actually perform it.

**--vm-size**:
Azure Virtual Machine Size (e.g. Standard_DS1_v).

**--proxy-resource-group-id**

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
gcloud alpha container azure node-pools create
```