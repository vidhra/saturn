# get-networkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-network.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-network.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# get-network

## Description

Returns detailed information about a network.

Applies to Hyperledger Fabric and Ethereum.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/GetNetwork)

## Synopsis

```
get-network
--network-id <value>
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

`--network-id` (string)

The unique identifier of the network to get information about.

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

Network -> (structure)

An object containing network configuration parameters.

Id -> (string)

The unique identifier of the network.

Name -> (string)

The name of the network.

Description -> (string)

Attributes of the blockchain framework for the network.

Framework -> (string)

The blockchain framework that the network uses.

FrameworkVersion -> (string)

The version of the blockchain framework that the network uses.

FrameworkAttributes -> (structure)

Attributes of the blockchain framework that the network uses.

Fabric -> (structure)

Attributes of Hyperledger Fabric for a Managed Blockchain network that uses Hyperledger Fabric.

OrderingServiceEndpoint -> (string)

The endpoint of the ordering service for the network.

Edition -> (string)

The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more information, see [Amazon Managed Blockchain Pricing](http://aws.amazon.com/managed-blockchain/pricing/) .

Ethereum -> (structure)

Attributes of an Ethereum network for Managed Blockchain resources participating in an Ethereum network.

ChainId -> (string)

The Ethereum `CHAIN_ID` associated with the Ethereum network. Chain IDs are as follows:

- mainnet = `1`

VpcEndpointServiceName -> (string)

The VPC endpoint service name of the VPC endpoint service of the network. Members use the VPC endpoint service name to create a VPC endpoint to access network resources.

VotingPolicy -> (structure)

The voting rules that the network uses to decide if a proposal is accepted.

ApprovalThresholdPolicy -> (structure)

Defines the rules for the network for voting on proposals, such as the percentage of `YES` votes required for the proposal to be approved and the duration of the proposal. The policy applies to all proposals and is specified when the network is created.

ThresholdPercentage -> (integer)

The percentage of votes among all members that must be `YES` for a proposal to be approved. For example, a `ThresholdPercentage` value of `50` indicates 50%. The `ThresholdComparator` determines the precise comparison. If a `ThresholdPercentage` value of `50` is specified on a network with 10 members, along with a `ThresholdComparator` value of `GREATER_THAN` , this indicates that 6 `YES` votes are required for the proposal to be approved.

ProposalDurationInHours -> (integer)

The duration from the time that a proposal is created until it expires. If members cast neither the required number of `YES` votes to approve the proposal nor the number of `NO` votes required to reject it before the duration expires, the proposal is `EXPIRED` and `ProposalActions` arenât carried out.

ThresholdComparator -> (string)

Determines whether the vote percentage must be greater than the `ThresholdPercentage` or must be greater than or equal to the `ThresholdPercentage` to be approved.

Status -> (string)

The current status of the network.

CreationDate -> (timestamp)

The date and time that the network was created.

Tags -> (map)

Tags assigned to the network. Each tag consists of a key and optional value.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide* , or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

key -> (string)

value -> (string)

Arn -> (string)

The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .