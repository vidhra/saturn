# modify-subnet-attributeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-subnet-attribute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-subnet-attribute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-subnet-attribute

## Description

Modifies a subnet attribute. You can only modify one attribute at a time.

Use this action to modify subnets on Amazon Web Services Outposts.

- To modify a subnet on an Outpost rack, set both `MapCustomerOwnedIpOnLaunch` and `CustomerOwnedIpv4Pool` . These two parameters act as a single attribute.
- To modify a subnet on an Outpost server, set either `EnableLniAtDeviceIndex` or `DisableLniAtDeviceIndex` .

For more information about Amazon Web Services Outposts, see the following:

- [Outpost servers](https://docs.aws.amazon.com/outposts/latest/userguide/how-servers-work.html)
- [Outpost racks](https://docs.aws.amazon.com/outposts/latest/userguide/how-racks-work.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifySubnetAttribute)

## Synopsis

```
modify-subnet-attribute
[--assign-ipv6-address-on-creation | --no-assign-ipv6-address-on-creation]
[--map-public-ip-on-launch | --no-map-public-ip-on-launch]
--subnet-id <value>
[--map-customer-owned-ip-on-launch | --no-map-customer-owned-ip-on-launch]
[--customer-owned-ipv4-pool <value>]
[--enable-dns64 | --no-enable-dns64]
[--private-dns-hostname-type-on-launch <value>]
[--enable-resource-name-dns-a-record-on-launch | --no-enable-resource-name-dns-a-record-on-launch]
[--enable-resource-name-dns-aaaa-record-on-launch | --no-enable-resource-name-dns-aaaa-record-on-launch]
[--enable-lni-at-device-index <value>]
[--disable-lni-at-device-index | --no-disable-lni-at-device-index]
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

`--assign-ipv6-address-on-creation` | `--no-assign-ipv6-address-on-creation` (structure)

Specify `true` to indicate that network interfaces created in the specified subnet should be assigned an IPv6 address. This includes a network interface thatâs created when launching an instance into the subnet (the instance therefore receives an IPv6 address).

If you enable the IPv6 addressing feature for your subnet, your network interface or instance only receives an IPv6 address if itâs created using version `2016-11-15` or later of the Amazon EC2 API.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--map-public-ip-on-launch` | `--no-map-public-ip-on-launch` (structure)

Specify `true` to indicate that network interfaces attached to instances created in the specified subnet should be assigned a public IPv4 address.

Amazon Web Services charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the [Amazon VPC pricing page](http://aws.amazon.com/vpc/pricing/) .

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--subnet-id` (string)

The ID of the subnet.

`--map-customer-owned-ip-on-launch` | `--no-map-customer-owned-ip-on-launch` (structure)

Specify `true` to indicate that network interfaces attached to instances created in the specified subnet should be assigned a customer-owned IPv4 address.

When this value is `true` , you must specify the customer-owned IP pool using `CustomerOwnedIpv4Pool` .

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--customer-owned-ipv4-pool` (string)

The customer-owned IPv4 address pool associated with the subnet.

You must set this value when you specify `true` for `MapCustomerOwnedIpOnLaunch` .

`--enable-dns64` | `--no-enable-dns64` (structure)

Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations.

You must first configure a NAT gateway in a public subnet (separate from the subnet containing the IPv6-only workloads). For example, the subnet containing the NAT gateway should have a `0.0.0.0/0` route pointing to the internet gateway. For more information, see [Configure DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html#nat-gateway-nat64-dns64-walkthrough) in the *Amazon VPC User Guide* .

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--private-dns-hostname-type-on-launch` (string)

The type of hostname to assign to instances in the subnet at launch. For IPv4-only and dual-stack (IPv4 and IPv6) subnets, an instance DNS name can be based on the instance IPv4 address (ip-name) or the instance ID (resource-name). For IPv6 only subnets, an instance DNS name must be based on the instance ID (resource-name).

Possible values:

- `ip-name`
- `resource-name`

`--enable-resource-name-dns-a-record-on-launch` | `--no-enable-resource-name-dns-a-record-on-launch` (structure)

Indicates whether to respond to DNS queries for instance hostnames with DNS A records.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--enable-resource-name-dns-aaaa-record-on-launch` | `--no-enable-resource-name-dns-aaaa-record-on-launch` (structure)

Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

`--enable-lni-at-device-index` (integer)

Indicates the device position for local network interfaces in this subnet. For example, `1` indicates local network interfaces in this subnet are the secondary network interface (eth1). A local network interface cannot be the primary network interface (eth0).

`--disable-lni-at-device-index` | `--no-disable-lni-at-device-index` (structure)

Specify `true` to indicate that local network interfaces at the current position should be disabled.

Value -> (boolean)

The attribute value. The valid values are `true` or `false` .

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

**To change a subnetâs public IPv4 addressing behavior**

This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned a public IPv4 address. If the command succeeds, no output is returned.

Command:

```
aws ec2 modify-subnet-attribute --subnet-id subnet-1a2b3c4d --map-public-ip-on-launch
```

**To change a subnetâs IPv6 addressing behavior**

This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned an IPv6 address from the range of the subnet.

Command:

```
aws ec2 modify-subnet-attribute --subnet-id subnet-1a2b3c4d --assign-ipv6-address-on-creation
```

For more information, see [IP Addressing in Your VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-ip-addressing.html) in the *AWS Virtual Private Cloud User Guide*.

## Output

None