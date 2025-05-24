# modify-vpc-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-vpc-endpoint

## Description

Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the [Amazon Web Services PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVpcEndpoint)

## Synopsis

```
modify-vpc-endpoint
[--dry-run | --no-dry-run]
--vpc-endpoint-id <value>
[--reset-policy | --no-reset-policy]
[--policy-document <value>]
[--add-route-table-ids <value>]
[--remove-route-table-ids <value>]
[--add-subnet-ids <value>]
[--remove-subnet-ids <value>]
[--add-security-group-ids <value>]
[--remove-security-group-ids <value>]
[--ip-address-type <value>]
[--dns-options <value>]
[--private-dns-enabled | --no-private-dns-enabled]
[--subnet-configurations <value>]
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

`--vpc-endpoint-id` (string)

The ID of the endpoint.

`--reset-policy` | `--no-reset-policy` (boolean)

(Gateway endpoint) Specify `true` to reset the policy document to the default policy. The default policy allows full access to the service.

`--policy-document` (string)

(Interface and gateway endpoints) A policy to attach to the endpoint that controls access to the service. The policy must be in valid JSON format.

`--add-route-table-ids` (list)

(Gateway endpoint) The IDs of the route tables to associate with the endpoint.

(string)

Syntax:

```
"string" "string" ...
```

`--remove-route-table-ids` (list)

(Gateway endpoint) The IDs of the route tables to disassociate from the endpoint.

(string)

Syntax:

```
"string" "string" ...
```

`--add-subnet-ids` (list)

(Interface and Gateway Load Balancer endpoints) The IDs of the subnets in which to serve the endpoint. For a Gateway Load Balancer endpoint, you can specify only one subnet.

(string)

Syntax:

```
"string" "string" ...
```

`--remove-subnet-ids` (list)

(Interface endpoint) The IDs of the subnets from which to remove the endpoint.

(string)

Syntax:

```
"string" "string" ...
```

`--add-security-group-ids` (list)

(Interface endpoint) The IDs of the security groups to associate with the endpoint network interfaces.

(string)

Syntax:

```
"string" "string" ...
```

`--remove-security-group-ids` (list)

(Interface endpoint) The IDs of the security groups to disassociate from the endpoint network interfaces.

(string)

Syntax:

```
"string" "string" ...
```

`--ip-address-type` (string)

The IP address type for the endpoint.

Possible values:

- `ipv4`
- `dualstack`
- `ipv6`

`--dns-options` (structure)

The DNS options for the endpoint.

DnsRecordIpType -> (string)

The DNS records created for the endpoint.

PrivateDnsOnlyForInboundResolverEndpoint -> (boolean)

Indicates whether to enable private DNS only for inbound endpoints. This option is available only for services that support both gateway and interface endpoints. It routes traffic that originates from the VPC to the gateway endpoint and traffic that originates from on-premises to the interface endpoint.

Shorthand Syntax:

```
DnsRecordIpType=string,PrivateDnsOnlyForInboundResolverEndpoint=boolean
```

JSON Syntax:

```
{
  "DnsRecordIpType": "ipv4"|"dualstack"|"ipv6"|"service-defined",
  "PrivateDnsOnlyForInboundResolverEndpoint": true|false
}
```

`--private-dns-enabled` | `--no-private-dns-enabled` (boolean)

(Interface endpoint) Indicates whether a private hosted zone is associated with the VPC.

`--subnet-configurations` (list)

The subnet configurations for the endpoint.

(structure)

Describes the configuration of a subnet for a VPC endpoint.

SubnetId -> (string)

The ID of the subnet.

Ipv4 -> (string)

The IPv4 address to assign to the endpoint network interface in the subnet. You must provide an IPv4 address if the VPC endpoint supports IPv4.

If you specify an IPv4 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.

Ipv6 -> (string)

The IPv6 address to assign to the endpoint network interface in the subnet. You must provide an IPv6 address if the VPC endpoint supports IPv6.

If you specify an IPv6 address when modifying a VPC endpoint, we replace the existing endpoint network interface with a new endpoint network interface with this IP address. This process temporarily disconnects the subnet and the VPC endpoint.

Shorthand Syntax:

```
SubnetId=string,Ipv4=string,Ipv6=string ...
```

JSON Syntax:

```
[
  {
    "SubnetId": "string",
    "Ipv4": "string",
    "Ipv6": "string"
  }
  ...
]
```

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

**To modify a gateway endpoint**

This example modifies gateway endpoint `vpce-1a2b3c4d` by associating route table `rtb-aaa222bb` with the endpoint, and resetting the policy document.

Command:

```
aws ec2 modify-vpc-endpoint --vpc-endpoint-id vpce-1a2b3c4d --add-route-table-ids rtb-aaa222bb --reset-policy
```

Output:

```
{
  "Return": true
}
```

**To modify an interface endpoint**

This example modifies interface endpoint `vpce-0fe5b17a0707d6fa5` by adding subnet `subnet-d6fcaa8d` to the endpoint.

Command:

```
aws ec2 modify-vpc-endpoint --vpc-endpoint-id vpce-0fe5b17a0707d6fa5 --add-subnet-id subnet-d6fcaa8d
```

Output:

```
{
  "Return": true
}
```

## Output

Return -> (boolean)

Returns `true` if the request succeeds; otherwise, it returns an error.