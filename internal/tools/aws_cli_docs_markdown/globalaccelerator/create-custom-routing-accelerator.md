# create-custom-routing-acceleratorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-accelerator.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-accelerator.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# create-custom-routing-accelerator

## Description

Create a custom routing accelerator. A custom routing accelerator directs traffic to one of possibly thousands of Amazon EC2 instance destinations running in a single or multiple virtual private clouds (VPC) subnet endpoints.

Be aware that, by default, all destination EC2 instances in a VPC subnet endpoint cannot receive traffic. To enable all destinations to receive traffic, or to specify individual port mappings that can receive traffic, see the [AllowCustomRoutingTraffic](https://docs.aws.amazon.com/global-accelerator/latest/api/API_AllowCustomRoutingTraffic.html) operation.

### Warning

Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify `--region us-west-2` on Amazon Web Services CLI commands.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/CreateCustomRoutingAccelerator)

## Synopsis

```
create-custom-routing-accelerator
--name <value>
[--ip-address-type <value>]
[--ip-addresses <value>]
[--enabled | --no-enabled]
[--idempotency-token <value>]
[--tags <value>]
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

`--name` (string)

The name of a custom routing accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

`--ip-address-type` (string)

The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.

Possible values:

- `IPV4`
- `DUAL_STACK`

`--ip-addresses` (list)

Optionally, if youâve added your own IP address pool to Global Accelerator (BYOIP), you can choose an IPv4 address from your own pool to use for the acceleratorâs static IPv4 address when you create an accelerator.

After you bring an address range to Amazon Web Services, it appears in your account as an address pool. When you create an accelerator, you can assign one IPv4 address from your range to it. Global Accelerator assigns you a second static IPv4 address from an Amazon IP address range. If you bring two IPv4 address ranges to Amazon Web Services, you can assign one IPv4 address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.

You can specify one or two addresses, separated by a space. Do not include the /32 suffix.

Note that you canât update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the *Global Accelerator Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--enabled` | `--no-enabled` (boolean)

Indicates whether an accelerator is enabled. The value is true or false. The default value is true.

If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.

`--idempotency-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotencyâthat is, the uniquenessâof the request.

`--tags` (list)

Create tags for an accelerator.

For more information, see [Tagging in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the *Global Accelerator Developer Guide* .

(structure)

A complex type that contains a `Tag` key and `Tag` value.

Key -> (string)

A string that contains a `Tag` key.

Value -> (string)

A string that contains a `Tag` value.

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

**To create a custom routing accelerator**

The following `create-custom-routing-accelerator` example creates a custom routing accelerator with the tags `Name` and `Project`.

```
aws globalaccelerator create-custom-routing-accelerator \
    --name ExampleCustomRoutingAccelerator \
    --tags Key="Name",Value="Example Name" Key="Project",Value="Example Project" \
    --ip-addresses 192.0.2.250 198.51.100.52
```

Output:

```
{
    "Accelerator": {
        "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh",
        "IpAddressType": "IPV4",
        "Name": "ExampleCustomRoutingAccelerator",
        "Enabled": true,
        "Status": "IN_PROGRESS",
        "IpSets": [
            {
                "IpAddresses": [
                    "192.0.2.250",
                    "198.51.100.52"
                ],
                "IpFamily": "IPv4"
            }
        ],
        "DnsName":"a1234567890abcdef.awsglobalaccelerator.com",
        "CreatedTime": 1542394847.0,
        "LastModifiedTime": 1542394847.0
    }
}
```

For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html) in the *AWS Global Accelerator Developer Guide*.

## Output

Accelerator -> (structure)

The accelerator that is created.

AcceleratorArn -> (string)

The Amazon Resource Name (ARN) of the custom routing accelerator.

Name -> (string)

The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType -> (string)

The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.

Enabled -> (boolean)

Indicates whether the accelerator is enabled. The value is true or false. The default value is true.

If the value is set to true, the accelerator cannot be deleted. If set to false, accelerator can be deleted.

IpSets -> (list)

The static IP addresses that Global Accelerator associates with the accelerator.

(structure)

A complex type for the set of IP addresses for an accelerator.

IpFamily -> (string)

IpFamily is deprecated and has been replaced by IpAddressFamily.

IpAddresses -> (list)

The array of IP addresses in the IP address set. An IP address set can have a maximum of two IP addresses.

(string)

IpAddressFamily -> (string)

The types of IP addresses included in this IP set.

DnsName -> (string)

The Domain Name System (DNS) name that Global Accelerator creates that points to an acceleratorâs static IPv4 addresses.

The naming convention for the DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.

If you have a dual-stack accelerator, you also have a second DNS name, `DualStackDnsName` , that points to both the A record and the AAAA record for all four static addresses for the accelerator: two IPv4 addresses and two IPv6 addresses.

For more information about the default DNS name, see [Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) in the *Global Accelerator Developer Guide* .

Status -> (string)

Describes the deployment status of the accelerator.

CreatedTime -> (timestamp)

The date and time that the accelerator was created.

LastModifiedTime -> (timestamp)

The date and time that the accelerator was last modified.