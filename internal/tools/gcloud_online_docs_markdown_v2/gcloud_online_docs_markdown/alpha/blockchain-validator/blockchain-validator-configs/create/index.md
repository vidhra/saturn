# gcloud alpha blockchain-validator blockchain-validator-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create)*

**NAME**

: **gcloud alpha blockchain-validator blockchain-validator-configs create - create a blockchain validator configuration**

**SYNOPSIS**

: **`gcloud alpha blockchain-validator blockchain-validator-configs create` `[BLOCKCHAIN_VALIDATOR_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#BLOCKCHAIN_VALIDATOR_CONFIG)` `[--blockchain-type](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--blockchain-type)`=`BLOCKCHAIN_TYPE` `[--key-source](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--key-source)`=`KEY_SOURCE` `[--[no-]validation-work-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--<span>[no-]</span>validation-work-enabled)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--async)`] [`[--blockchain-node-id](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--blockchain-node-id)`=`BLOCKCHAIN_NODE_ID`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--labels)`=[`LABELS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--location)`=`LOCATION`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--request-id)`=`REQUEST_ID`] [`[--ethereum-protocol-details-gas-limit](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--ethereum-protocol-details-gas-limit)`=`ETHEREUM_PROTOCOL_DETAILS_GAS_LIMIT` `[--ethereum-protocol-details-graffiti](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--ethereum-protocol-details-graffiti)`=`ETHEREUM_PROTOCOL_DETAILS_GRAFFITI` `[--ethereum-protocol-details-suggested-fee-recipient](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--ethereum-protocol-details-suggested-fee-recipient)`=`ETHEREUM_PROTOCOL_DETAILS_SUGGESTED_FEE_RECIPIENT` `[--ethereum-protocol-details-use-block-builder-proposals](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--ethereum-protocol-details-use-block-builder-proposals)`] [[`[--existing-seed-phrase-reference-secret](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--existing-seed-phrase-reference-secret)`=`EXISTING_SEED_PHRASE_REFERENCE_SECRET` : `[--existing-seed-phrase-reference-derivation-index](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--existing-seed-phrase-reference-derivation-index)`=`EXISTING_SEED_PHRASE_REFERENCE_DERIVATION_INDEX`]     | [`[--remote-web3-signer-voting-public-key](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--remote-web3-signer-voting-public-key)`=`REMOTE_WEB3_SIGNER_VOTING_PUBLIC_KEY` `[--remote-web3-signer-web3signer-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--remote-web3-signer-web3signer-uri)`=`REMOTE_WEB3_SIGNER_WEB3SIGNER_URI` : `[--remote-web3-signer-timeout-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--remote-web3-signer-timeout-duration)`=`REMOTE_WEB3_SIGNER_TIMEOUT_DURATION`]     | [`[--seed-phrase-reference-secret](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--seed-phrase-reference-secret)`=`SEED_PHRASE_REFERENCE_SECRET` : `[--seed-phrase-reference-export](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#--seed-phrase-reference-export)`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a blockchain validator configuration on a blockchain
node managed by Blockchain Node Engine.

**EXAMPLES**

: To create an Ethereum validator configuration `my-validator` in the
project `my-project` and location `us-central1`, using a
new seed phrase which is exported to Secret Manager, and deploy it to the
blockchain node `my-node`, run:
$ [gcloud
alpha blockchain-validator blockchain-validator-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator/blockchain-validator-configs) \
```
create my-validator --location=us-central1 \
--project=my-project --validation-work-enabled=false \
--blockchain-type=ETHEREUM --key-source=SEED_PHRASE_REFERENCE \
--seed-phrase-reference-secret=projects/my-project/secrets/\
my-seed-phrase --seed-phrase-reference-export=true \
    --blockchain-node-id=projects/my-project/locations/us-central1/\
blockchainNodes/my-node
```

**POSITIONAL ARGUMENTS**

: **BlockchainValidatorConfig resource - Blockchain Validator Config Name The name
of the Blockchain Validator Config. The fully specified name must have the
format
projects/{project}/locations/{location}/blockchainValidatorConfigs/{validator}.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `blockchain_validator_config` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `blockchain_validator_config` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`BLOCKCHAIN_VALIDATOR_CONFIG`**:
ID of the blockchainValidatorConfig or fully qualified identifier for the
blockchainValidatorConfig.
To set the `blockchain_validator_config` attribute:

- provide the argument `blockchain_validator_config` on the command
line.**

**REQUIRED FLAGS**

: **--blockchain-type**:
The blockchain type of the validator. `BLOCKCHAIN_TYPE`
must be (only one value is supported):

**`ethereum`**:
The blockchain type is Ethereum.

**--key-source**:
The source of the voting key for the blockchain validator.
`KEY_SOURCE` must be one of:

**`existing-seed-phrase-reference`**:
Derive voting keys from existing seed material.

**`remote-web3-signer`**:
The voting key is stored in a remote signing service (Web3Signer) and signing
requests are delegated.

**`seed-phrase-reference`**:
Derive voting keys from new seed material.

**--[no-]validation-work-enabled**:
True if the blockchain node requests and signs attestations and blocks on behalf
of this validator, false if not. This does NOT define whether the blockchain
expects work to occur, only whether the blockchain node specified above is
carrying out validation tasks. This should be enabled under normal conditions,
but may be useful when migrating validators to/from Blockchain Node Engine,
where the validator may be paused during the migration. Use
`--validation-work-enabled` to enable and
`--no-validation-work-enabled` to disable.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--blockchain-node-id**

**--labels**:
Labels as key value pairs.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--location**:
For resources [blockchainValidatorConfig, secret], provides fallback value for
resource location attribute. When the resource's full URI path is not provided,
location will fallback to this flag value.

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

**--ethereum-protocol-details-gas-limit**

**Arguments for the key source config.
At most one of these can be specified:

**Location of existing seed material, and derivation path used to generate the
voting key.

**Secret resource - Reference into Secret Manager for where the seed phrase is
stored. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--existing-seed-phrase-reference-secret` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--existing-seed-phrase-reference-secret` on the
command line with a fully specified name;
- provide the argument `--location` on the command line. This resource
can be one of the following types:
[blockchainvalidatormanager.projects.locations.secrets,
blockchainvalidatormanager.projects.secrets].

This must be specified.

**--existing-seed-phrase-reference-secret**:
ID of the secret or fully qualified identifier for the secret.
To set the `secret` attribute:

- provide the argument `--existing-seed-phrase-reference-secret` on the
command line.**

**--existing-seed-phrase-reference-derivation-index**:
The index to derive the voting key at, used as part of a derivation path. The
derivation path is built from this as
"m/12381/3600/<derivation_index>/0/0" See also [https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters](https://eips.ethereum.org/EIPS/eip-2334#eth2-specific-parameters)**

**--remote-web3-signer-voting-public-key**

**Derivation path used to generate the voting key, and optionally Secret Manager
secret to backup the seed phrase to.

**Secret resource - Reference into Secret Manager for where the seed phrase is
stored. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--seed-phrase-reference-secret` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--seed-phrase-reference-secret` on the command
line with a fully specified name;
- provide the argument `--location` on the command line. This resource
can be one of the following types:
[blockchainvalidatormanager.projects.locations.secrets,
blockchainvalidatormanager.projects.secrets].

This must be specified.

**--seed-phrase-reference-secret**:
ID of the secret or fully qualified identifier for the secret.
To set the `secret` attribute:

- provide the argument `--seed-phrase-reference-secret` on the command
line.**

**--seed-phrase-reference-export**:
True to export the seed phrase to Secret Manager.****

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