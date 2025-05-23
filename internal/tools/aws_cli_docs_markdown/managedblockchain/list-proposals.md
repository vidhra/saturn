# list-proposalsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposals.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-proposals.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# list-proposals

## Description

Returns a list of proposals for the network.

Applies only to Hyperledger Fabric.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/ListProposals)

## Synopsis

```
list-proposals
--network-id <value>
[--max-results <value>]
[--next-token <value>]
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

The unique identifier of the network.

`--max-results` (integer)

The maximum number of proposals to return.

`--next-token` (string)

The pagination token that indicates the next set of results to retrieve.

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

Proposals -> (list)

The summary of each proposal made on the network.

(structure)

Properties of a proposal.

Applies only to Hyperledger Fabric.

ProposalId -> (string)

The unique identifier of the proposal.

Description -> (string)

The description of the proposal.

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
- `ACTION_FAILED` - One or more of the specified `ProposalActions` in a proposal that was approved couldnât be completed because of an error.

CreationDate -> (timestamp)

The date and time that the proposal was created.

ExpirationDate -> (timestamp)

The date and time that the proposal expires. This is the `CreationDate` plus the `ProposalDurationInHours` that is specified in the `ProposalThresholdPolicy` . After this date and time, if members havenât cast enough votes to determine the outcome according to the voting policy, the proposal is `EXPIRED` and `Actions` arenât carried out.

Arn -> (string)

The Amazon Resource Name (ARN) of the proposal. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

NextToken -> (string)

The pagination token that indicates the next set of results to retrieve.