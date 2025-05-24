# modify-transit-gatewayÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-transit-gateway

## Description

Modifies the specified transit gateway. When you modify a transit gateway, the modified options are applied to new transit gateway attachments only. Your existing transit gateway attachments are not modified.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyTransitGateway)

## Synopsis

```
modify-transit-gateway
--transit-gateway-id <value>
[--description <value>]
[--options <value>]
[--dry-run | --no-dry-run]
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

`--transit-gateway-id` (string)

The ID of the transit gateway.

`--description` (string)

The description for the transit gateway.

`--options` (structure)

The options to modify.

AddTransitGatewayCidrBlocks -> (list)

Adds IPv4 or IPv6 CIDR blocks for the transit gateway. Must be a size /24 CIDR block or larger for IPv4, or a size /64 CIDR block or larger for IPv6.

(string)

RemoveTransitGatewayCidrBlocks -> (list)

Removes CIDR blocks for the transit gateway.

(string)

VpnEcmpSupport -> (string)

Enable or disable Equal Cost Multipath Protocol support.

DnsSupport -> (string)

Enable or disable DNS support.

SecurityGroupReferencingSupport -> (string)

Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.

This option is disabled by default.

For more information about security group referencing, see [Security group referencing](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#vpc-attachment-security) in the *Amazon Web Services Transit Gateways Guide* .

AutoAcceptSharedAttachments -> (string)

Enable or disable automatic acceptance of attachment requests.

DefaultRouteTableAssociation -> (string)

Enable or disable automatic association with the default association route table.

AssociationDefaultRouteTableId -> (string)

The ID of the default association route table.

DefaultRouteTablePropagation -> (string)

Enable or disable automatic propagation of routes to the default propagation route table.

PropagationDefaultRouteTableId -> (string)

The ID of the default propagation route table.

AmazonSideAsn -> (long)

A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.

The modify ASN operation is not allowed on a transit gateway if it has the following attachments:

- Dynamic VPN
- Static VPN
- Direct Connect Gateway
- Connect

You must first delete all transit gateway attachments configured prior to modifying the ASN on the transit gateway.

Shorthand Syntax:

```
AddTransitGatewayCidrBlocks=string,string,RemoveTransitGatewayCidrBlocks=string,string,VpnEcmpSupport=string,DnsSupport=string,SecurityGroupReferencingSupport=string,AutoAcceptSharedAttachments=string,DefaultRouteTableAssociation=string,AssociationDefaultRouteTableId=string,DefaultRouteTablePropagation=string,PropagationDefaultRouteTableId=string,AmazonSideAsn=long
```

JSON Syntax:

```
{
  "AddTransitGatewayCidrBlocks": ["string", ...],
  "RemoveTransitGatewayCidrBlocks": ["string", ...],
  "VpnEcmpSupport": "enable"|"disable",
  "DnsSupport": "enable"|"disable",
  "SecurityGroupReferencingSupport": "enable"|"disable",
  "AutoAcceptSharedAttachments": "enable"|"disable",
  "DefaultRouteTableAssociation": "enable"|"disable",
  "AssociationDefaultRouteTableId": "string",
  "DefaultRouteTablePropagation": "enable"|"disable",
  "PropagationDefaultRouteTableId": "string",
  "AmazonSideAsn": long
}
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To modify a transit gateway**

The following `modify-transit-gateway` example modifies the specified transit gateway by enabling ECMP support for VPN attachments.

```
aws ec2 modify-transit-gateway \
    --transit-gateway-id tgw-111111222222aaaaa \
    --options VpnEcmpSupport=enable
```

Output:

```
{
    "TransitGateway": {
        "TransitGatewayId": "tgw-111111222222aaaaa",
        "TransitGatewayArn": "64512",
        "State": "modifying",
        "OwnerId": "123456789012",
        "CreationTime": "2020-04-30T08:41:37.000Z",
        "Options": {
            "AmazonSideAsn": 64512,
            "AutoAcceptSharedAttachments": "disable",
            "DefaultRouteTableAssociation": "enable",
            "AssociationDefaultRouteTableId": "tgw-rtb-0123456789abcd123",
            "DefaultRouteTablePropagation": "enable",
            "PropagationDefaultRouteTableId": "tgw-rtb-0123456789abcd123",
            "VpnEcmpSupport": "enable",
            "DnsSupport": "enable"
        }
    }
}
```

For more information, see [Transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html) in the *Transit Gateways Guide*.

## Output

TransitGateway -> (structure)

Information about the transit gateway.

TransitGatewayId -> (string)

The ID of the transit gateway.

TransitGatewayArn -> (string)

The Amazon Resource Name (ARN) of the transit gateway.

State -> (string)

The state of the transit gateway.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the transit gateway.

Description -> (string)

The description of the transit gateway.

CreationTime -> (timestamp)

The creation time.

Options -> (structure)

The transit gateway options.

AmazonSideAsn -> (long)

A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.

TransitGatewayCidrBlocks -> (list)

The transit gateway CIDR blocks.

(string)

AutoAcceptSharedAttachments -> (string)

Indicates whether attachment requests are automatically accepted.

DefaultRouteTableAssociation -> (string)

Indicates whether resource attachments are automatically associated with the default association route table. Enabled by default. If `defaultRouteTableAssociation` is set to `enable` , Amazon Web Services Transit Gateway will create the default transit gateway route table.

AssociationDefaultRouteTableId -> (string)

The ID of the default association route table.

DefaultRouteTablePropagation -> (string)

Indicates whether resource attachments automatically propagate routes to the default propagation route table. Enabled by default. If `defaultRouteTablePropagation` is set to `enable` , Amazon Web Services Transit Gateway will create the default transit gateway route table.

PropagationDefaultRouteTableId -> (string)

The ID of the default propagation route table.

VpnEcmpSupport -> (string)

Indicates whether Equal Cost Multipath Protocol support is enabled.

DnsSupport -> (string)

Indicates whether DNS support is enabled.

SecurityGroupReferencingSupport -> (string)

Enables you to reference a security group across VPCs attached to a transit gateway to simplify security group management.

This option is disabled by default.

MulticastSupport -> (string)

Indicates whether multicast is enabled on the transit gateway

Tags -> (list)

The tags for the transit gateway.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.