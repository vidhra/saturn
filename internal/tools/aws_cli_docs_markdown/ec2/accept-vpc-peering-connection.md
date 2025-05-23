# accept-vpc-peering-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-peering-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-peering-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# accept-vpc-peering-connection

## Description

Accept a VPC peering connection request. To accept a request, the VPC peering connection must be in the `pending-acceptance` state, and you must be the owner of the peer VPC. Use  DescribeVpcPeeringConnections to view your outstanding VPC peering connection requests.

For an inter-Region VPC peering connection request, you must accept the VPC peering connection in the Region of the accepter VPC.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AcceptVpcPeeringConnection)

## Synopsis

```
accept-vpc-peering-connection
[--dry-run | --no-dry-run]
--vpc-peering-connection-id <value>
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--vpc-peering-connection-id` (string)

The ID of the VPC peering connection. You must specify this parameter in the request.

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

**To accept a VPC peering connection**

This example accepts the specified VPC peering connection request.

Command:

```
aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id pcx-1a2b3c4d
```

Output:

```
{
  "VpcPeeringConnection": {
    "Status": {
      "Message": "Provisioning",
      "Code": "provisioning"
    },
    "Tags": [],
    "AccepterVpcInfo": {
      "OwnerId": "444455556666",
      "VpcId": "vpc-44455566",
      "CidrBlock": "10.0.1.0/28"
    },
    "VpcPeeringConnectionId": "pcx-1a2b3c4d",
    "RequesterVpcInfo": {
      "OwnerId": "444455556666",
      "VpcId": "vpc-111abc45",
      "CidrBlock": "10.0.0.0/28"
    }
  }
}
```

## Output

VpcPeeringConnection -> (structure)

Information about the VPC peering connection.

AccepterVpcInfo -> (structure)

Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.

CidrBlock -> (string)

The IPv4 CIDR block for the VPC.

Ipv6CidrBlockSet -> (list)

The IPv6 CIDR block for the VPC.

(structure)

Describes an IPv6 CIDR block.

Ipv6CidrBlock -> (string)

The IPv6 CIDR block.

CidrBlockSet -> (list)

Information about the IPv4 CIDR blocks for the VPC.

(structure)

Describes an IPv4 CIDR block.

CidrBlock -> (string)

The IPv4 CIDR block.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the VPC.

PeeringOptions -> (structure)

Information about the VPC peering connection options for the accepter or requester VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.

VpcId -> (string)

The ID of the VPC.

Region -> (string)

The Region in which the VPC is located.

ExpirationTime -> (timestamp)

The time that an unaccepted VPC peering connection will expire.

RequesterVpcInfo -> (structure)

Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.

CidrBlock -> (string)

The IPv4 CIDR block for the VPC.

Ipv6CidrBlockSet -> (list)

The IPv6 CIDR block for the VPC.

(structure)

Describes an IPv6 CIDR block.

Ipv6CidrBlock -> (string)

The IPv6 CIDR block.

CidrBlockSet -> (list)

Information about the IPv4 CIDR blocks for the VPC.

(structure)

Describes an IPv4 CIDR block.

CidrBlock -> (string)

The IPv4 CIDR block.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the VPC.

PeeringOptions -> (structure)

Information about the VPC peering connection options for the accepter or requester VPC.

AllowDnsResolutionFromRemoteVpc -> (boolean)

Indicates whether a local VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.

AllowEgressFromLocalClassicLinkToRemoteVpc -> (boolean)

Deprecated.

AllowEgressFromLocalVpcToRemoteClassicLink -> (boolean)

Deprecated.

VpcId -> (string)

The ID of the VPC.

Region -> (string)

The Region in which the VPC is located.

Status -> (structure)

The status of the VPC peering connection.

Code -> (string)

The status of the VPC peering connection.

Message -> (string)

A message that provides more information about the status, if applicable.

Tags -> (list)

Any tags assigned to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VpcPeeringConnectionId -> (string)

The ID of the VPC peering connection.