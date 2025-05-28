# gcloud edge-cloud container clusters node-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update)*

**NAME**

: **gcloud edge-cloud container clusters node-pools update - updates an Edge Container node pool**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters node-pools update` (`[NODE_POOL](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#NODE_POOL)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--cluster)`=`CLUSTER` `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--async)`] [`[--local-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--local-disk-kms-key)`=`LOCAL_DISK_KMS_KEY`] [`[--lro-timeout](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--lro-timeout)`=`LRO_TIMEOUT`] [`[--machine-filter](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--machine-filter)`=`MACHINE_FILTER`] [`[--node-count](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--node-count)`=`NODE_COUNT`] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--node-labels)`=[`KEY`=`VALUE`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--use-google-managed-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--use-google-managed-key)`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an Edge Container node pool.

**EXAMPLES**

: To update the number of nodes in a node pool called `my-node-pool` in
region `us-central1`, run:

```
gcloud edge-cloud container clusters node-pools update my-node-pool --location=us-central1 --cluster=<my-cluster> --node-count=<new-count>
```

**POSITIONAL ARGUMENTS**

: **Node pool resource - Edge Container node pool to update. The arguments in this
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

**--node-count**:
Default nodeCount used by this node pool.

**--node-labels**:
Comma-delimited list of key-value pairs that comprise labels for the individual
nodes in the node pool. This flag updates the Kubernetes labels, unlike
`--update-labels`, `--remove-labels`, and
`--clear-labels` which update the cloud resource labels.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--use-google-managed-key**:
Once specified, a Google-managed key will be used for the control plane disk
encryption.

**--clear-labels**

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
gcloud alpha edge-cloud container clusters node-pools update
```