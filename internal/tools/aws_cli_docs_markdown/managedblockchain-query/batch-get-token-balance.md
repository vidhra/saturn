# batch-get-token-balanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/batch-get-token-balance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/batch-get-token-balance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain-query/index.html#cli-aws-managedblockchain-query) ]

# batch-get-token-balance

## Description

Gets the token balance for a batch of tokens by using the `BatchGetTokenBalance` action for every token in the request.

### Note

Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-query-2023-05-04/BatchGetTokenBalance)

## Synopsis

```
batch-get-token-balance
[--get-token-balance-inputs <value>]
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

`--get-token-balance-inputs` (list)

An array of `BatchGetTokenBalanceInputItem` objects whose balance is being requested.

(structure)

The container for the input for getting a token balance.

tokenIdentifier -> (structure)

The container for the identifier for the token including the unique token ID and its blockchain network.

### Note

Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

network -> (string)

The blockchain network of the token.

contractAddress -> (string)

This is the tokenâs contract address.

tokenId -> (string)

The unique identifier of the token.

### Note

For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the `tokenId` in the 64 character hexadecimal `tokenid` format.

ownerIdentifier -> (structure)

The container for the owner identifier.

address -> (string)

The contract or wallet address for the owner.

atBlockchainInstant -> (structure)

The container for time.

time -> (timestamp)

The container of the `Timestamp` of the blockchain instant.

### Note

This `timestamp` will only be recorded up to the second.

Shorthand Syntax:

```
tokenIdentifier={network=string,contractAddress=string,tokenId=string},ownerIdentifier={address=string},atBlockchainInstant={time=timestamp} ...
```

JSON Syntax:

```
[
  {
    "tokenIdentifier": {
      "network": "ETHEREUM_MAINNET"|"ETHEREUM_SEPOLIA_TESTNET"|"BITCOIN_MAINNET"|"BITCOIN_TESTNET",
      "contractAddress": "string",
      "tokenId": "string"
    },
    "ownerIdentifier": {
      "address": "string"
    },
    "atBlockchainInstant": {
      "time": timestamp
    }
  }
  ...
]
```

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

tokenBalances -> (list)

An array of `BatchGetTokenBalanceOutputItem` objects returned by the response.

(structure)

The container for the properties of a token balance output.

ownerIdentifier -> (structure)

The container for the owner identifier.

address -> (string)

The contract or wallet address for the owner.

tokenIdentifier -> (structure)

The container for the identifier for the token including the unique token ID and its blockchain network.

### Note

Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

network -> (string)

The blockchain network of the token.

contractAddress -> (string)

This is the tokenâs contract address.

tokenId -> (string)

The unique identifier of the token.

### Note

For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the `tokenId` in the 64 character hexadecimal `tokenid` format.

balance -> (string)

The container for the token balance.

atBlockchainInstant -> (structure)

The container for time.

time -> (timestamp)

The container of the `Timestamp` of the blockchain instant.

### Note

This `timestamp` will only be recorded up to the second.

lastUpdatedTime -> (structure)

The container for time.

time -> (timestamp)

The container of the `Timestamp` of the blockchain instant.

### Note

This `timestamp` will only be recorded up to the second.

errors -> (list)

An array of `BatchGetTokenBalanceErrorItem` objects returned from the request.

(structure)

Error generated from a failed `BatchGetTokenBalance` request.

tokenIdentifier -> (structure)

The container for the identifier for the token including the unique token ID and its blockchain network.

### Note

Only the native tokens BTC and ETH, and the ERC-20, ERC-721, and ERC 1155 token standards are supported.

network -> (string)

The blockchain network of the token.

contractAddress -> (string)

This is the tokenâs contract address.

tokenId -> (string)

The unique identifier of the token.

### Note

For native tokens, use the 3 character abbreviation that best matches your token. For example, btc for Bitcoin, eth for Ether, etc. For all other token types you must specify the `tokenId` in the 64 character hexadecimal `tokenid` format.

ownerIdentifier -> (structure)

The container for the owner identifier.

address -> (string)

The contract or wallet address for the owner.

atBlockchainInstant -> (structure)

The container for time.

time -> (timestamp)

The container of the `Timestamp` of the blockchain instant.

### Note

This `timestamp` will only be recorded up to the second.

errorCode -> (string)

The error code associated with the error.

errorMessage -> (string)

The message associated with the error.

errorType -> (string)

The type of error.