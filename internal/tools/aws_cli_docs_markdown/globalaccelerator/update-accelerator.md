# update-acceleratorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [globalaccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/index.html#cli-aws-globalaccelerator) ]

# update-accelerator

## Description

Update an accelerator to make changes, such as the following:

- Change the name of the accelerator.
- Disable the accelerator so that it no longer accepts or routes traffic, or so that you can delete it.
- Enable the accelerator, if it is disabled.
- Change the IP address type to dual-stack if it is IPv4, or change the IP address type to IPv4 if itâs dual-stack.

Be aware that static IP addresses remain assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you delete the accelerator, you lose the static IP addresses that are assigned to it, so you can no longer route traffic by using them.

### Warning

Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify `--region us-west-2` on Amazon Web Services CLI commands.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/globalaccelerator-2018-08-08/UpdateAccelerator)

## Synopsis

```
update-accelerator
--accelerator-arn <value>
[--name <value>]
[--ip-address-type <value>]
[--ip-addresses <value>]
[--enabled | --no-enabled]
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

`--accelerator-arn` (string)

The Amazon Resource Name (ARN) of the accelerator to update.

`--name` (string)

The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.

`--ip-address-type` (string)

The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.

Possible values:

- `IPV4`
- `DUAL_STACK`

`--ip-addresses` (list)

The IP addresses for an accelerator.

(string)

Syntax:

```
"string" "string" ...
```

`--enabled` | `--no-enabled` (boolean)

Indicates whether an accelerator is enabled. The value is true or false. The default value is true.

If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.

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

**To update an accelerator**

The following `update-accelerator` example modifies an accelerator to change the accelerator name to `ExampleAcceleratorNew`. You must specify the `US-West-2 (Oregon)` Region to create or update accelerators.

```
aws globalaccelerator update-accelerator \
    --accelerator-arn arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh \
    --name ExampleAcceleratorNew
```

Output:

```
{
    "Accelerator": {
        "AcceleratorArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh",
        "IpAddressType": "IPV4",
        "Name": "ExampleAcceleratorNew",
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
        "CreatedTime": 1232394847,
        "LastModifiedTime": 1232395654
    }
}
```

For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html) in the *AWS Global Accelerator Developer Guide*.

## Output

Accelerator -> (structure)

Information about the updated accelerator.

AcceleratorArn -> (string)

The Amazon Resource Name (ARN) of the accelerator.

Name -> (string)

The name of the accelerator. The name must contain only alphanumeric characters or hyphens (-), and must not begin or end with a hyphen.

IpAddressType -> (string)

The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL_STACK.

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

The naming convention for the DNS name for an accelerator is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .awsglobalaccelerator.com. For example: a1234567890abcdef.awsglobalaccelerator.com.

If you have a dual-stack accelerator, you also have a second DNS name, `DualStackDnsName` , that points to both the A record and the AAAA record for all four static addresses for the accelerator: two IPv4 addresses and two IPv6 addresses.

For more information about the default DNS name, see [Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) in the *Global Accelerator Developer Guide* .

Status -> (string)

Describes the deployment status of the accelerator.

CreatedTime -> (timestamp)

The date and time that the accelerator was created.

LastModifiedTime -> (timestamp)

The date and time that the accelerator was last modified.

DualStackDnsName -> (string)

The Domain Name System (DNS) name that Global Accelerator creates that points to a dual-stack acceleratorâs four static IP addresses: two IPv4 addresses and two IPv6 addresses.

The naming convention for the dual-stack DNS name is the following: A lowercase letter a, followed by a 16-bit random hex string, followed by .dualstack.awsglobalaccelerator.com. For example: a1234567890abcdef.dualstack.awsglobalaccelerator.com.

Note: Global Accelerator also assigns a default DNS name, `DnsName` , to your accelerator that points just to the static IPv4 addresses.

For more information, see [Support for DNS addressing in Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html#about-accelerators.dns-addressing) in the *Global Accelerator Developer Guide* .

Events -> (list)

A history of changes that you make to an accelerator in Global Accelerator.

(structure)

A complex type that contains a `Timestamp` value and `Message` for changes that you make to an accelerator in Global Accelerator. Messages stored here provide progress or error information when you update an accelerator from IPv4 to dual-stack, or from dual-stack to IPv4. Global Accelerator stores a maximum of ten event messages.

Message -> (string)

A string that contains an `Event` message describing changes or errors when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.

Timestamp -> (timestamp)

A timestamp for when you update an accelerator in Global Accelerator from IPv4 to dual-stack, or dual-stack to IPv4.