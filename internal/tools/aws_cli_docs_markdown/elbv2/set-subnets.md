# set-subnetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-subnets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-subnets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# set-subnets

## Description

Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer, Network Load Balancer or Gateway Load Balancer. The specified subnets replace the previously enabled subnets.

When you specify subnets for a Network Load Balancer, or Gateway Load Balancer you must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/SetSubnets)

## Synopsis

```
set-subnets
--load-balancer-arn <value>
[--subnets <value>]
[--subnet-mappings <value>]
[--ip-address-type <value>]
[--enable-prefix-for-ipv6-source-nat <value>]
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

`--load-balancer-arn` (string)

The Amazon Resource Name (ARN) of the load balancer.

`--subnets` (list)

The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

[Application Load Balancers] You must specify subnets from at least two Availability Zones.

[Application Load Balancers on Outposts] You must specify one Outpost subnet.

[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.

[Network Load Balancers and Gateway Load Balancers] You can specify subnets from one or more Availability Zones.

(string)

Syntax:

```
"string" "string" ...
```

`--subnet-mappings` (list)

The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.

[Application Load Balancers] You must specify subnets from at least two Availability Zones. You canât specify Elastic IP addresses for your subnets.

[Application Load Balancers on Outposts] You must specify one Outpost subnet.

[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.

[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.

[Gateway Load Balancers] You can specify subnets from one or more Availability Zones.

(structure)

Information about a subnet mapping.

SubnetId -> (string)

The ID of the subnet.

AllocationId -> (string)

[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.

PrivateIPv4Address -> (string)

[Network Load Balancers] The private IPv4 address for an internal load balancer.

IPv6Address -> (string)

[Network Load Balancers] The IPv6 address.

SourceNatIpv6Prefix -> (string)

[Network Load Balancers with UDP listeners] The IPv6 prefix to use for source NAT. Specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or `auto_assigned` to use an IPv6 prefix selected at random from the subnet CIDR block.

Shorthand Syntax:

```
SubnetId=string,AllocationId=string,PrivateIPv4Address=string,IPv6Address=string,SourceNatIpv6Prefix=string ...
```

JSON Syntax:

```
[
  {
    "SubnetId": "string",
    "AllocationId": "string",
    "PrivateIPv4Address": "string",
    "IPv6Address": "string",
    "SourceNatIpv6Prefix": "string"
  }
  ...
]
```

`--ip-address-type` (string)

The IP address type.

[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).

[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).

Possible values:

- `ipv4`
- `dualstack`
- `dualstack-without-public-ipv4`

`--enable-prefix-for-ipv6-source-nat` (string)

[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be `dualstack` . The default value is `off` .

Possible values:

- `on`
- `off`

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

**To enable Availability Zones for a load balancer**

This example enables the Availability Zone for the specified subnet for the specified load balancer.

Command:

```
aws elbv2 set-subnets --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188 --subnets subnet-8360a9e7 subnet-b7d581c0
```

Output:

```
{
  "AvailabilityZones": [
      {
          "SubnetId": "subnet-8360a9e7",
          "ZoneName": "us-west-2a"
      },
      {
          "SubnetId": "subnet-b7d581c0",
          "ZoneName": "us-west-2b"
      }
  ]
}
```

## Output

AvailabilityZones -> (list)

Information about the subnets.

(structure)

Information about an Availability Zone.

ZoneName -> (string)

The name of the Availability Zone.

SubnetId -> (string)

The ID of the subnet. You can specify one subnet per Availability Zone.

OutpostId -> (string)

[Application Load Balancers on Outposts] The ID of the Outpost.

LoadBalancerAddresses -> (list)

[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.

(structure)

Information about a static IP address for a load balancer.

IpAddress -> (string)

The static IP address.

AllocationId -> (string)

[Network Load Balancers] The allocation ID of the Elastic IP address for an internal-facing load balancer.

PrivateIPv4Address -> (string)

[Network Load Balancers] The private IPv4 address for an internal load balancer.

IPv6Address -> (string)

[Network Load Balancers] The IPv6 address.

SourceNatIpv6Prefixes -> (list)

[Network Load Balancers with UDP listeners] The IPv6 prefixes to use for source NAT. For each subnet, specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or `auto_assigned` to use an IPv6 prefix selected at random from the subnet CIDR block.

(string)

IpAddressType -> (string)

The IP address type.

EnablePrefixForIpv6SourceNat -> (string)

[Network Load Balancers] Indicates whether to use an IPv6 prefix from each subnet for source NAT.