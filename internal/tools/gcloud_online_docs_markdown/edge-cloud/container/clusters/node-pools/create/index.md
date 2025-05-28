# gcloud edge-cloud container clusters node-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create)*

**NAME**

: **gcloud edge-cloud container clusters node-pools create - create an Edge Container node pool**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters node-pools create` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--location)`=`LOCATION`) `[--node-count](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--node-count)`=`NODE_COUNT` `[--node-location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--node-location)`=`NODE_LOCATION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--local-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--local-disk-kms-key)`=`LOCAL_DISK_KMS_KEY`] [`[--lro-timeout](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--lro-timeout)`=`LRO_TIMEOUT`] [`[--machine-filter](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--machine-filter)`=`MACHINE_FILTER`] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--node-labels)`=[`KEY`=`VALUE`,…]] [`[--node-storage-schema](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#--node-storage-schema)`=`NODE_STORAGE_SCHEMA`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Edge Container node pool.

**EXAMPLES**

: To create a node pool called `my-nodePool`, containing 3 nodes in
region `us-central1`, run:

```
gcloud edge-cloud container clusters node-pools create my-nodePool --cluster=<my-cluster> --location=us-central1 --node-location=<my-node-location> --node-count=3
```

To create a node pool called `my-nodePool`, containing 3 nodes in
region `us-central1`, using only machine names matching a specific
pattern, run:

```
gcloud edge-cloud container clusters node-pools create my-nodePool --cluster=<my-cluster> --location=us-central1 --node-location=<my-node-location> --node-count=3 --machine-filter="name:<name>"
```

To create a node pool called `my-nodePool`, containing 3 nodes in
region `us-central1`, using only machine names NOT matching a
specific pattern, run:

```
gcloud edge-cloud container clusters node-pools create my-nodePool --cluster=<my-cluster> --location=us-central1 --node-location=<my-node-location> --node-count=3 --machine-filter="NOT name:<name>"
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - Edge Container node pool to create. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_POOL`**:
ID of the node pool or fully qualified identifier for the node pool.
To set the `nodePool` attribute:

- provide the argument `node_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
Cluster of the node pool.
To set the `cluster` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line.

**--location**:
Google Cloud location for the node pool.
To set the `location` attribute:

- provide the argument `node_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--node-count**:
Default nodeCount used by this node pool.

**--node-location**:
Google Edge Cloud zone where nodes in this node pool will be created.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--local-disk-kms-key**:
Google Cloud KMS key that will be used to secure local disks on nodes in this
node pool. The Edge Container service account for this project must have
`roles/cloudkms.cryptoKeyEncrypterDecrypter` on the key.
If not provided, a Google-managed key will be used instead.

**--lro-timeout**:
Overwrite the default LRO maximum timeout.

**--machine-filter**:
Only machines matching this filter will be allowed to join the node pool. The
filtering language accepts strings like "name=<name>", and is documented
in more detail at [https://google.aip.dev/160](https://google.aip.dev/160).

**--node-labels**:
Comma-delimited list of key-value pairs that comprise labels for the individual
nodes in the node pool. This flag sets the Kubernetes labels, unlike
`--labels` which sets the cloud resource labels.

**--node-storage-schema**:
Name for the storage schema of worker nodes.

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

**API REFERENCE**

: This command uses the edgecontainer/v1 API. The full documentation for this API
can be found at: [https://cloud.google.com/edge-cloud](https://cloud.google.com/edge-cloud)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud container clusters node-pools create
```