# list-transaction-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/list-transaction-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/list-transaction-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/index.html#cli-aws-managedblockchain-query) ]

# list-transaction-events

## Description

Lists all the transaction events for a transaction

### Note

This action will return transaction details for all transactions that are *confirmed* on the blockchain, even if they have not reached [finality](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/key-concepts.html#finality) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-query-2023-05-04/ListTransactionEvents)

`list-transaction-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

```
list-transaction-events
[--transaction-hash <value>]
[--transaction-id <value>]
--network <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The blockchain network where the transaction events occurred.

Possible values:

- `ETHEREUM_MAINNET`
- `ETHEREUM_SEPOLIA_TESTNET`
- `BITCOIN_MAINNET`
- `BITCOIN_TESTNET`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

events -> (list)

An array of `TransactionEvent` objects. Each object contains details about the transaction events.

(structure)

The container for the properties of a transaction event.

network -> (string)

The blockchain network where the transaction occurred.

transactionHash -> (string)

The hash of a transaction. It is generated when a transaction is created.

eventType -> (string)

The type of transaction event.

from -> (string)

The wallet address initiating the transaction. It can either be a public key or a contract.

to -> (string)

The wallet address receiving the transaction. It can either be a public key or a contract.

value -> (string)

The value that was transacted.

contractAddress -> (string)

The blockchain address for the contract

tokenId -> (string)

The unique identifier for the token involved in the transaction.

transactionId -> (string)

The identifier of a Bitcoin transaction. It is generated when a transaction is created.

voutIndex -> (integer)

The position of the transaction output in the transaction output list.

voutSpent -> (boolean)

Specifies if the transaction output is spent or unspent. This is only returned for BITCOIN_VOUT event types.

### Note

This is only returned for `BITCOIN_VOUT` event types.

spentVoutTransactionId -> (string)

The transactionId that *created* the spent transaction output.

### Note

This is only returned for `BITCOIN_VIN` event types.

spentVoutTransactionHash -> (string)

The transactionHash that *created* the spent transaction output.

### Note

This is only returned for `BITCOIN_VIN` event types.

spentVoutIndex -> (integer)

The position of the spent transaction output in the output list of the *creating transaction* .

### Note

This is only returned for `BITCOIN_VIN` event types.

blockchainInstant -> (structure)

The container for time.

time -> (timestamp)

The container of the `Timestamp` of the blockchain instant.

### Note

This `timestamp` will only be recorded up to the second.

confirmationStatus -> (string)

This container specifies whether the transaction has reached Finality.

nextToken -> (string)

The pagination token that indicates the next set of results to retrieve.