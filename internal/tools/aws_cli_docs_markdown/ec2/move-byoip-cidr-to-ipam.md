# move-byoip-cidr-to-ipamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-byoip-cidr-to-ipam.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-byoip-cidr-to-ipam.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# move-byoip-cidr-to-ipam

## Description

Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool.

If you already have a BYOIPv4 CIDR with Amazon Web Services, you can move the CIDR to IPAM from a public IPv4 pool. You cannot move an IPv6 CIDR to IPAM. If you are bringing a new IP address to Amazon Web Services for the first time, complete the steps in [Tutorial: BYOIP address CIDRs to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/MoveByoipCidrToIpam)

## Synopsis

```
move-byoip-cidr-to-ipam
[--dry-run | --no-dry-run]
--cidr <value>
--ipam-pool-id <value>
--ipam-pool-owner <value>
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

A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--cidr` (string)

The BYOIP CIDR.

`--ipam-pool-id` (string)

The IPAM pool ID.

`--ipam-pool-owner` (string)

The Amazon Web Services account ID of the owner of the IPAM pool.

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

**To transfer a BYOIP CIDR to IPAM**

The following `move-byoip-cidr-to-ipam` example transfers a BYOIP CIDR to IPAM.

(Linux):

```
aws ec2 move-byoip-cidr-to-ipam \
    --region us-west-2 \
    --ipam-pool-id ipam-pool-0a03d430ca3f5c035 \
    --ipam-pool-owner 111111111111 \
    --cidr 130.137.249.0/24
```

(Windows):

```
aws ec2 move-byoip-cidr-to-ipam ^
    --region us-west-2 ^
    --ipam-pool-id ipam-pool-0a03d430ca3f5c035 ^
    --ipam-pool-owner 111111111111 ^
    --cidr 130.137.249.0/24
```

Output:

```
{
    "ByoipCidr": {
        "Cidr": "130.137.249.0/24",
        "State": "pending-transfer"
    }
}
```

For more information, see [Tutorial: Transfer an existing BYOIP IPv4 CIDR to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-transfer-ipv4.html) in the *Amazon VPC IPAM User Guide*.

## Output

ByoipCidr -> (structure)

The BYOIP CIDR.

Cidr -> (string)

The address range, in CIDR notation.

Description -> (string)

The description of the address range.

AsnAssociations -> (list)

The BYOIP CIDR associations with ASNs.

(structure)

An Autonomous System Number (ASN) and BYOIP CIDR association.

Asn -> (string)

The associationâs ASN.

Cidr -> (string)

The associationâs CIDR.

StatusMessage -> (string)

The associationâs status message.

State -> (string)

The associationâs state.

StatusMessage -> (string)

Upon success, contains the ID of the address pool. Otherwise, contains an error message.

State -> (string)

The state of the address range.

- `advertised` : The address range is being advertised to the internet by Amazon Web Services.
- `deprovisioned` : The address range is deprovisioned.
- `failed-deprovision` : The request to deprovision the address range was unsuccessful. Ensure that all EIPs from the range have been deallocated and try again.
- `failed-provision` : The request to provision the address range was unsuccessful.
- `pending-deprovision` : Youâve submitted a request to deprovision an address range and itâs pending.
- `pending-provision` : Youâve submitted a request to provision an address range and itâs pending.
- `provisioned` : The address range is provisioned and can be advertised. The range is not currently advertised.
- `provisioned-not-publicly-advertisable` : The address range is provisioned and cannot be advertised.

NetworkBorderGroup -> (string)

If you have [Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html) enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.

You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:

- us-east-1-dfw-2
- us-west-2-lax-1
- us-west-2-phx-2

### Note

You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.