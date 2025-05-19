# gcloud alpha blockchain-node-engine nodes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/describe)*

**NAME**

: **gcloud alpha blockchain-node-engine nodes describe - describe a Blockchain Node Engine node**

**SYNOPSIS**

: **`gcloud alpha blockchain-node-engine nodes describe` (`[NODE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/describe#NODE_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Blockchain Node Engine node configuration and
state.

**EXAMPLES**

: To describe a blockchain node with id `my-node`, run:

```
gcloud alpha blockchain-node-engine nodes describe my-node
```

**POSITIONAL ARGUMENTS**

: **Node resource - Arguments and flags that specify the Blockchain Node Engine node
you want to describe. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_name` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_NAME`**:
ID of the node or fully qualified identifier for the node.
To set the `node_name` attribute:

- provide the argument `node_name` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the blockchain node resource.
To set the `location` attribute:

- provide the argument `node_name` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `web3/location`.**

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

: This command uses the `blockchainnodeengine/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blockchain-node-engine](https://cloud.google.com/blockchain-node-engine)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.