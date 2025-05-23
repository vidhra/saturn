# get-transactionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/get-transaction.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/get-transaction.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/index.html#cli-aws-managedblockchain-query) ]

# get-transaction

## Description

Gets the details of a transaction.

### Note

This action will return transaction details for all transactions that are *confirmed* on the blockchain, even if they have not reached [finality](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-query-2023-05-04/GetTransaction)

## Synopsis

```
get-transaction
[--transaction-hash <value>]
[--transaction-id <value>]
--network <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--transaction-hash` (string)

The hash of a transaction. It is generated when a transaction is created.

`--transaction-id` (string)

The identifier of a Bitcoin transaction. It is generated when a transaction is created.

### Note

`transactionId` is only supported on the Bitcoin networks.

`--network` (string)

The blockchain network where the transaction occurred.

Possible values:

- `ETHEREUM_MAINNET`
- `ETHEREUM_SEPOLIA_TESTNET`
- `BITCOIN_MAINNET`
- `BITCOIN_TESTNET`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

transaction -> (structure)

Contains the details of the transaction.

network -> (string)

The blockchain network where the transaction occurred.

blockHash -> (string)

The block hash is a unique identifier for a block. It is a fixed-size string that is calculated by using the information in the block. The block hash is used to verify the integrity of the data in the block.

transactionHash -> (string)

The hash of a transaction. It is generated when a transaction is created.

blockNumber -> (string)

The block number in which the transaction is recorded.

transactionTimestamp -> (timestamp)

The `Timestamp` of the transaction.

transactionIndex -> (long)

The index of the transaction within a blockchain.

numberOfTransactions -> (long)

The number of transactions in the block.

to -> (string)

The identifier of the transaction. It is generated whenever a transaction is verified and added to the blockchain.

from -> (string)

The initiator of the transaction. It is either in the form a public key or a contract address.

contractAddress -> (string)

The blockchain address for the contract.

gasUsed -> (string)

The amount of gas used for the transaction.

cumulativeGasUsed -> (string)

The amount of gas used up to the specified point in the block.

effectiveGasPrice -> (string)

The effective gas price.

signatureV -> (integer)

The signature of the transaction. The Z coordinate of a point V.

signatureR -> (string)

The signature of the transaction. The X coordinate of a point R.

signatureS -> (string)

The signature of the transaction. The Y coordinate of a point S.

transactionFee -> (string)

The transaction fee.

transactionId -> (string)

The identifier of a Bitcoin transaction. It is generated when a transaction is created.

confirmationStatus -> (string)

Specifies whether the transaction has reached Finality.

executionStatus -> (string)

Identifies whether the transaction has succeeded or failed.