# gcloud alpha blockchain-validator blockchain-validator-configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update)*

**NAME**

: **gcloud alpha blockchain-validator blockchain-validator-configs update - update the configuration of a single blockchain validator**

**SYNOPSIS**

: **`gcloud alpha blockchain-validator blockchain-validator-configs update` (`[BLOCKCHAIN_VALIDATOR_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#BLOCKCHAIN_VALIDATOR_CONFIG)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--async)`] [`[--blockchain-node-id](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--blockchain-node-id)`=`BLOCKCHAIN_NODE_ID`] [`[--ethereum-protocol-details-graffiti](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--ethereum-protocol-details-graffiti)`=`ETHEREUM_PROTOCOL_DETAILS_GRAFFITI`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--request-id)`=`REQUEST_ID`] [`[--[no-]validation-work-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--[no-]validation-work-enabled)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[--remote-web3-signer-timeout-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--remote-web3-signer-timeout-duration)`=`REMOTE_WEB3_SIGNER_TIMEOUT_DURATION` `[--remote-web3-signer-web3signer-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#--remote-web3-signer-web3signer-uri)`=`REMOTE_WEB3_SIGNER_WEB3SIGNER_URI`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update the configuration of a single blockchain validator.

**EXAMPLES**

: To enable validation work on a previously disabled blockchain validator
`my-validator` in the project `my-project` and location
`us-central1` run:
$ [gcloud
alpha blockchain-validator blockchain-validator-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs) \
```
update my-validator --location=us-central1 \
--project=my-project --validation-work-enabled=true
```

**POSITIONAL ARGUMENTS**

: **BlockchainValidatorConfig resource - Blockchain Validator Config Name The name
of the Blockchain Validator Config. The fully specified name must have the
format
projects/{project}/locations/{location}/blockchainValidatorConfigs/{validator}.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `blockchain_validator_config` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BLOCKCHAIN_VALIDATOR_CONFIG`**:
ID of the blockchainValidatorConfig or fully qualified identifier for the
blockchainValidatorConfig.
To set the `blockchain_validator_config` attribute:

- provide the argument `blockchain_validator_config` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the blockchainValidatorConfig resource.
To set the `location` attribute:

- provide the argument `blockchain_validator_config` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--blockchain-node-id**

**--ethereum-protocol-details-graffiti**

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--[no-]validation-work-enabled**:
True if the blockchain node requests and signs attestations and blocks on behalf
of this validator, false if not. This does NOT define whether the blockchain
expects work to occur, only whether the blockchain node specified above is
carrying out validation tasks. This should be enabled under normal conditions,
but may be useful when migrating validators to/from Blockchain Node Engine,
where the validator may be paused during the migration. Use
`--validation-work-enabled` to enable and
`--no-validation-work-enabled` to disable.

**--labels**

**--remote-web3-signer-timeout-duration**

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

: This command uses the `blockchainvalidatormanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/blockchain-node-engine/docs/create-node-ethereum#validator_configuration](https://cloud.google.com/blockchain-node-engine/docs/create-node-ethereum#validator_configuration)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.