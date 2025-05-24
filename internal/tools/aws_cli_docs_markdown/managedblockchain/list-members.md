# list-membersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/list-members.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# list-members

## Description

Returns a list of the members in a network and properties of their configurations.

Applies only to Hyperledger Fabric.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/ListMembers)

## Synopsis

```
list-members
--network-id <value>
[--name <value>]
[--status <value>]
[--is-owned | --no-is-owned]
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

The unique identifier of the network for which to list members.

`--name` (string)

The optional name of the member to list.

`--status` (string)

An optional status specifier. If provided, only members currently in this status are listed.

Possible values:

- `CREATING`
- `AVAILABLE`
- `CREATE_FAILED`
- `UPDATING`
- `DELETING`
- `DELETED`
- `INACCESSIBLE_ENCRYPTION_KEY`

`--is-owned` | `--no-is-owned` (boolean)

An optional Boolean value. If provided, the request is limited either to members that the current Amazon Web Services account owns (`true` ) or that other Amazon Web Services accountsn own (`false` ). If omitted, all members are listed.

`--max-results` (integer)

The maximum number of members to return in the request.

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

Members -> (list)

An array of `MemberSummary` objects. Each object contains details about a network member.

(structure)

A summary of configuration properties for a member.

Applies only to Hyperledger Fabric.

Id -> (string)

The unique identifier of the member.

Name -> (string)

The name of the member.

Description -> (string)

An optional description of the member.

Status -> (string)

The status of the member.

- `CREATING` - The Amazon Web Services account is in the process of creating a member.
- `AVAILABLE` - The member has been created and can participate in the network.
- `CREATE_FAILED` - The Amazon Web Services account attempted to create a member and creation failed.
- `UPDATING` - The member is in the process of being updated.
- `DELETING` - The member and all associated resources are in the process of being deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
- `DELETED` - The member can no longer participate on the network and all associated resources are deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an `APPROVED` `PROPOSAL` to remove the member.
- `INACCESSIBLE_ENCRYPTION_KEY` - The member is impaired and might not function as expected because it cannot access the specified customer managed key in Key Management Service (KMS) for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked. The effect of disabling or deleting a key or of revoking a grant isnât immediate. It might take some time for the member resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.

CreationDate -> (timestamp)

The date and time that the member was created.

IsOwned -> (boolean)

An indicator of whether the member is owned by your Amazon Web Services account or a different Amazon Web Services account.

Arn -> (string)

The Amazon Resource Name (ARN) of the member. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

NextToken -> (string)

The pagination token that indicates the next set of results to retrieve.