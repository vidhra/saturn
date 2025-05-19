# gcloud alpha blockchain-node-engine nodes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create)*

**NAME**

: **gcloud alpha blockchain-node-engine nodes create - create a Blockchain Node Engine node**

**SYNOPSIS**

: **`gcloud alpha blockchain-node-engine nodes create` (`[NODE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#NODE_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--async)`] [`[--blockchain-type](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--blockchain-type)`=`BLOCKCHAIN_TYPE`; default="ETHEREUM"] [`[--consensus-client](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--consensus-client)`=`CONSENSUS_CLIENT`; default="LIGHTHOUSE"] [`[--execution-client](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--execution-client)`=`EXECUTION_CLIENT`; default="GETH"] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--network)`=`NETWORK`; default="MAINNET"] [`[--node-type](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#--node-type)`=`NODE_TYPE`; default="FULL"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine/nodes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new Blockchain Node Engine node with the given
name and configurations.
If run asynchronously with `--async`, exits after printing one
operation name that can be used to poll the status of the creation via:

```
gcloud operations describe
```

**EXAMPLES**

: To create a Blockchain Node Engine node with the name `my-node` in
location `us-central`, run:

```
gcloud alpha blockchain-node-engine nodes create my-node --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Node resource - Arguments and flags that specify the Blockchain Node Engine node
you want to create. The arguments in this group can be used to specify the
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--blockchain-type**:
Blockchain type the node will connect run on.
`BLOCKCHAIN_TYPE` must be (only one value is supported):

**`ethereum`**:
Ethereum blockchain.

**--consensus-client**:
Consensus client for Ethereum nodes. `CONSENSUS_CLIENT`
must be (only one value is supported):

**`lighthouse`**:
Lighthouse execution client.

**--execution-client**:
Execution client for Ethereum nodes. `EXECUTION_CLIENT`
must be (only one value is supported):

**`geth`**:
Geth execution client.

**--network**:
Blockchain network the node will connect to. `NETWORK`
must be one of:

**`goerli`**:
Goerli & Prater Ethereum test network.

**`holesky`**:
Holesky Ethereum test network.

**`mainnet`**:
Primary Ethereum network, often referred to as mainnet.

**`sepolia`**:
Sepolia Ethereum test network.

**--node-type**:
Node type - defines whether the node retains only recent data or an archival
history. `NODE_TYPE` must be (only one value is
supported):

**`full`**:
Node retains full history required for consensus validation, however does not
retain archival data beyond that.

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