# get-proposalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-proposal.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-proposal.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# get-proposal

## Description

Returns detailed information about a proposal.

Applies only to Hyperledger Fabric.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/GetProposal)

## Synopsis

```
get-proposal
--network-id <value>
--proposal-id <value>
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

The unique identifier of the network for which the proposal is made.

`--proposal-id` (string)

The unique identifier of the proposal.

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

Proposal -> (structure)

Information about a proposal.

ProposalId -> (string)

The unique identifier of the proposal.

NetworkId -> (string)

The unique identifier of the network for which the proposal is made.

Description -> (string)

The description of the proposal.

Actions -> (structure)

The actions to perform on the network if the proposal is `APPROVED` .

Invitations -> (list)

The actions to perform for an `APPROVED` proposal to invite an Amazon Web Services account to create a member and join the network.

(structure)

An action to invite a specific Amazon Web Services account to create a member and join the network. The `InviteAction` is carried out when a `Proposal` is `APPROVED` .

Applies only to Hyperledger Fabric.

Principal -> (string)

The Amazon Web Services account ID to invite.

Removals -> (list)

The actions to perform for an `APPROVED` proposal to remove a member from the network, which deletes the member and all associated member resources from the network.

(structure)

An action to remove a member from a Managed Blockchain network as the result of a removal proposal that is `APPROVED` . The member and all associated resources are deleted from the network.

Applies only to Hyperledger Fabric.

MemberId -> (string)

The unique identifier of the member to remove.

ProposedByMemberId -> (string)

The unique identifier of the member that created the proposal.

ProposedByMemberName -> (string)

The name of the member that created the proposal.

Status -> (string)

The status of the proposal. Values are as follows:

- `IN_PROGRESS` - The proposal is active and open for member voting.
- `APPROVED` - The proposal was approved with sufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network` . The specified proposal actions are carried out.
- `REJECTED` - The proposal was rejected with insufficient `YES` votes among members according to the `VotingPolicy` specified for the `Network` . The specified `ProposalActions` arenât carried out.
- `EXPIRED` - Members didnât cast the number of votes required to determine the proposal outcome before the proposal expired. The specified `ProposalActions` arenât carried out.
- `ACTION_FAILED` - One or more of the specified `ProposalActions` in a proposal that was approved couldnât be completed because of an error. The `ACTION_FAILED` status occurs even if only one ProposalAction fails and other actions are successful.

CreationDate -> (timestamp)

The date and time that the proposal was created.

ExpirationDate -> (timestamp)

The date and time that the proposal expires. This is the `CreationDate` plus the `ProposalDurationInHours` that is specified in the `ProposalThresholdPolicy` . After this date and time, if members havenât cast enough votes to determine the outcome according to the voting policy, the proposal is `EXPIRED` and `Actions` arenât carried out.

YesVoteCount -> (integer)

The current total of `YES` votes cast on the proposal by members.

NoVoteCount -> (integer)

The current total of `NO` votes cast on the proposal by members.

OutstandingVoteCount -> (integer)

The number of votes remaining to be cast on the proposal by members. In other words, the number of members minus the sum of `YES` votes and `NO` votes.

Tags -> (map)

Tags assigned to the proposal. Each tag consists of a key and optional value.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide* , or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

key -> (string)

value -> (string)

Arn -> (string)

The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .