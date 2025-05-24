# create-vpc-attachmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-vpc-attachment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# create-vpc-attachment

## Description

Creates a VPC attachment on an edge location of a core network.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/CreateVpcAttachment)

## Synopsis

```
create-vpc-attachment
--core-network-id <value>
--vpc-arn <value>
--subnet-arns <value>
[--options <value>]
[--tags <value>]
[--client-token <value>]
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

`--core-network-id` (string)

The ID of a core network for the VPC attachment.

`--vpc-arn` (string)

The ARN of the VPC.

`--subnet-arns` (list)

The subnet ARN of the VPC attachment.

(string)

Syntax:

```
"string" "string" ...
```

`--options` (structure)

Options for the VPC attachment.

Ipv6Support -> (boolean)

Indicates whether IPv6 is supported.

ApplianceModeSupport -> (boolean)

Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is `false` .

Shorthand Syntax:

```
Ipv6Support=boolean,ApplianceModeSupport=boolean
```

JSON Syntax:

```
{
  "Ipv6Support": true|false,
  "ApplianceModeSupport": true|false
}
```

`--tags` (list)

The key-value tags associated with the request.

(structure)

Describes a tag.

Key -> (string)

The tag key.

Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.

Constraints: Maximum length of 256 characters.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--client-token` (string)

The client token associated with the request.

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

**To create a VPC attachment**

The following `create-vpc-attachment` example creates a VPC attachment with IPv6 support in a core network.

```
aws networkmanager create-vpc-attachment \
    --core-network-id core-network-0fab62fe438d94db6 \
    --vpc-arn arn:aws:ec2:us-east-1:987654321012:vpc/vpc-09f37f69e2786eeb8  \
    --subnet-arns arn:aws:ec2:us-east-1:987654321012:subnet/subnet-04ca4e010857e7bb7 \
    --Ipv6Support=true
```

Output:

```
{
    "VpcAttachment": {
        "Attachment": {
            "CoreNetworkId": "core-network-0fab62fe438d94db6",
            "AttachmentId": "attachment-05e1da6eba87a06e6",
            "OwnerAccountId": "987654321012",
            "AttachmentType": "VPC",
            "State": "CREATING",
            "EdgeLocation": "us-east-1",
            "ResourceArn": "arn:aws:ec2:us-east-1:987654321012:vpc/vpc-09f37f69e2786eeb8",
            "Tags": [],
            "CreatedAt": "2022-03-10T20:59:14+00:00",
            "UpdatedAt": "2022-03-10T20:59:14+00:00"
        },
        "SubnetArns": [
            "arn:aws:ec2:us-east-1:987654321012:subnet/subnet-04ca4e010857e7bb7"
        ],
        "Options": {
            "Ipv6Support": true
        }
    }
}
```

For more information, see [Create an attachment](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-create-attachment.html) in the *Cloud WAN User Guide*.

## Output

VpcAttachment -> (structure)

Provides details about the VPC attachment.

Attachment -> (structure)

Provides details about the VPC attachment.

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

SubnetArns -> (list)

The subnet ARNs.

(string)

Options -> (structure)

Provides details about the VPC attachment.

Ipv6Support -> (boolean)

Indicates whether IPv6 is supported.

ApplianceModeSupport -> (boolean)

Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is `false` .