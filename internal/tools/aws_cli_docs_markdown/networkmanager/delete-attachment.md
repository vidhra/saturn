# delete-attachmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-attachment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-attachment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# delete-attachment

## Description

Deletes an attachment. Supports all attachment types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/DeleteAttachment)

## Synopsis

```
delete-attachment
--attachment-id <value>
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

`--attachment-id` (string)

The ID of the attachment to delete.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To delete an attachment**

The following `delete-attachment` example deletes a Connect attachment.

```
aws networkmanager delete-attachment \
    --attachment-id attachment-01feddaeae26ab68c
```

Output:

```
{
    "Attachment": {
        "CoreNetworkId": "core-network-0f4b0a9d5ee7761d1",
        "AttachmentId": "attachment-01feddaeae26ab68c",
        "OwnerAccountId": "987654321012",
        "AttachmentType": "CONNECT",
        "State": "DELETING",
        "EdgeLocation": "us-east-1",
        "ResourceArn": "arn:aws:networkmanager::987654321012:attachment/attachment-02c3964448fedf5aa",
        "CreatedAt": "2022-03-15T19:18:41+00:00",
        "UpdatedAt": "2022-03-15T19:28:59+00:00"
    }
}
```

For more information, see [Delete attachments](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-attachments-working-with.html#cloudwan-attachments-deleting) in the *Cloud WAN User Guide*.

## Output

Attachment -> (structure)

Information about the deleted attachment.

CoreNetworkId -> (string)

The ID of a core network.

CoreNetworkArn -> (string)

The ARN of a core network.

AttachmentId -> (string)

The ID of the attachment.

OwnerAccountId -> (string)

The ID of the attachment account owner.

AttachmentType -> (string)

The type of attachment.

State -> (string)

The state of the attachment.

EdgeLocation -> (string)

The Region where the edge is located. This is returned for all attachment types except a Direct Connect gateway attachment, which instead returns `EdgeLocations` .

EdgeLocations -> (list)

The edge locations that the Direct Connect gateway is associated with. This is returned only for Direct Connect gateway attachments. All other attachment types retrun `EdgeLocation` .

(string)

ResourceArn -> (string)

The attachment resource ARN.

AttachmentPolicyRuleNumber -> (integer)

The policy rule number associated with the attachment.

SegmentName -> (string)

The name of the segment attachment.

NetworkFunctionGroupName -> (string)

The name of the network function group.

Tags -> (list)

The tags associated with the attachment.

(structure)

Describes a tag.

Key -> (string)

The tag key.

Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.

Constraints: Maximum length of 256 characters.

ProposedSegmentChange -> (structure)

The attachment to move from one segment to another.

Tags -> (list)

The list of key-value tags that changed for the segment.

(structure)

Describes a tag.

Key -> (string)

The tag key.

Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.

Constraints: Maximum length of 256 characters.

AttachmentPolicyRuleNumber -> (integer)

The rule number in the policy document that applies to this change.

SegmentName -> (string)

The name of the segment to change.

ProposedNetworkFunctionGroupChange -> (structure)

Describes a proposed change to a network function group associated with the attachment.

Tags -> (list)

The list of proposed changes to the key-value tags associated with the network function group.

(structure)

Describes a tag.

Key -> (string)

The tag key.

Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.

Constraints: Maximum length of 256 characters.

AttachmentPolicyRuleNumber -> (integer)

The proposed new attachment policy rule number for the network function group.

NetworkFunctionGroupName -> (string)

The proposed name change for the network function group name.

CreatedAt -> (timestamp)

The timestamp when the attachment was created.

UpdatedAt -> (timestamp)

The timestamp when the attachment was last updated.

LastModificationErrors -> (list)

Describes the error associated with the attachment request.

(structure)

Describes the error associated with an attachment request.

Code -> (string)

The error code for the attachment request.

Message -> (string)

The message associated with the error `code` .

ResourceArn -> (string)

The ARN of the requested attachment resource.

RequestId -> (string)

The ID of the attachment request.