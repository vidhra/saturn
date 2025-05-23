# get-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-instance

## Description

Returns information about a specific Amazon Lightsail instance, which is a virtual private server.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstance)

## Synopsis

```
get-instance
--instance-name <value>
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

`--instance-name` (string)

The name of the instance.

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

**To get information about an instance**

The following `get-instance` example displays details about the instance `MEAN-1`.

```
aws lightsail get-instance \
    --instance-name MEAN-1
```

Output:

```
{
    "instance": {
        "name": "MEAN-1",
        "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd470fc5-a68b-44c5-8dbc-EXAMPLE4bada",
        "supportCode": "6EXAMPLE3362/i-05EXAMPLE407c97d3",
        "createdAt": 1570635023.124,
        "location": {
            "availabilityZone": "us-west-2a",
            "regionName": "us-west-2"
        },
        "resourceType": "Instance",
        "tags": [],
        "blueprintId": "mean",
        "blueprintName": "MEAN",
        "bundleId": "medium_3_0",
        "isStaticIp": false,
        "privateIpAddress": "192.0.2.0",
        "publicIpAddress": "192.0.2.0",
        "hardware": {
            "cpuCount": 2,
            "disks": [
                {
                    "createdAt": 1570635023.124,
                    "sizeInGb": 80,
                    "isSystemDisk": true,
                    "iops": 240,
                    "path": "/dev/xvda",
                    "attachedTo": "MEAN-1",
                    "attachmentState": "attached"
                }
            ],
            "ramSizeInGb": 4.0
        },
        "networking": {
            "monthlyTransfer": {
                "gbPerMonthAllocated": 4096
            },
            "ports": [
                {
                    "fromPort": 80,
                    "toPort": 80,
                    "protocol": "tcp",
                    "accessFrom": "Anywhere (0.0.0.0/0)",
                    "accessType": "public",
                    "commonName": "",
                    "accessDirection": "inbound"
                },
                {
                    "fromPort": 22,
                    "toPort": 22,
                    "protocol": "tcp",
                    "accessFrom": "Anywhere (0.0.0.0/0)",
                    "accessType": "public",
                    "commonName": "",
                    "accessDirection": "inbound"
                },
                {
                    "fromPort": 443,
                    "toPort": 443,
                    "protocol": "tcp",
                    "accessFrom": "Anywhere (0.0.0.0/0)",
                    "accessType": "public",
                    "commonName": "",
                    "accessDirection": "inbound"
                }
            ]
        },
        "state": {
            "code": 16,
            "name": "running"
        },
        "username": "bitnami",
        "sshKeyName": "MyKey"
    }
}
```

## Output

instance -> (structure)

An array of key-value pairs containing information about the specified instance.

name -> (string)

The name the user gave the instance (`Amazon_Linux_2023-1` ).

arn -> (string)

The Amazon Resource Name (ARN) of the instance (`arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE` ).

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The timestamp when the instance was created (`1479734909.17` ) in Unix time format.

location -> (structure)

The region name and Availability Zone where the instance is located.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The type of resource (usually `Instance` ).

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

blueprintId -> (string)

The blueprint ID (`amazon_linux_2023` ).

blueprintName -> (string)

The friendly name of the blueprint (`Amazon Linux 2023` ).

bundleId -> (string)

The bundle for the instance (`micro_x_x` ).

addOns -> (list)

An array of objects representing the add-ons enabled on the instance.

(structure)

Describes an add-on that is enabled for an Amazon Lightsail resource.

name -> (string)

The name of the add-on.

status -> (string)

The status of the add-on.

snapshotTimeOfDay -> (string)

The daily time when an automatic snapshot is created.

The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).

The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay -> (string)

The next daily time an automatic snapshot will be created.

The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).

The snapshot is automatically created between the time shown and up to 45 minutes after.

threshold -> (string)

The trigger threshold of the action.

### Warning

This add-on only applies to Lightsail for Research resources.

duration -> (string)

The amount of idle time in minutes after which your virtual computer will automatically stop.

### Warning

This add-on only applies to Lightsail for Research resources.

isStaticIp -> (boolean)

A Boolean value indicating whether this instance has a static IP assigned to it.

privateIpAddress -> (string)

The private IP address of the instance.

publicIpAddress -> (string)

The public IP address of the instance.

ipv6Addresses -> (list)

The IPv6 addresses of the instance.

(string)

ipAddressType -> (string)

The IP address type of the instance.

The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.

hardware -> (structure)

The size of the vCPU and the amount of RAM for the instance.

cpuCount -> (integer)

The number of vCPUs the instance has.

disks -> (list)

The disks attached to the instance.

(structure)

Describes a block storage disk.

name -> (string)

The unique name of the disk.

arn -> (string)

The Amazon Resource Name (ARN) of the disk.

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The date when the disk was created.

location -> (structure)

The AWS Region and Availability Zone where the disk is located.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type (`Disk` ).

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

addOns -> (list)

An array of objects representing the add-ons enabled on the disk.

(structure)

Describes an add-on that is enabled for an Amazon Lightsail resource.

name -> (string)

The name of the add-on.

status -> (string)

The status of the add-on.

snapshotTimeOfDay -> (string)

The daily time when an automatic snapshot is created.

The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).

The snapshot is automatically created between the time shown and up to 45 minutes after.

nextSnapshotTimeOfDay -> (string)

The next daily time an automatic snapshot will be created.

The time shown is in `HH:00` format, and in Coordinated Universal Time (UTC).

The snapshot is automatically created between the time shown and up to 45 minutes after.

threshold -> (string)

The trigger threshold of the action.

### Warning

This add-on only applies to Lightsail for Research resources.

duration -> (string)

The amount of idle time in minutes after which your virtual computer will automatically stop.

### Warning

This add-on only applies to Lightsail for Research resources.

sizeInGb -> (integer)

The size of the disk in GB.

isSystemDisk -> (boolean)

A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

iops -> (integer)

The input/output operations per second (IOPS) of the disk.

path -> (string)

The disk path.

state -> (string)

Describes the status of the disk.

attachedTo -> (string)

The resources to which the disk is attached.

isAttached -> (boolean)

A Boolean value indicating whether the disk is attached.

attachmentState -> (string)

(Discontinued) The attachment state of the disk.

### Note

In releases prior to November 14, 2017, this parameter returned `attached` for system disks in the API response. It is now discontinued, but still included in the response. Use `isAttached` instead.

gbInUse -> (integer)

(Discontinued) The number of GB in use by the disk.

### Note

In releases prior to November 14, 2017, this parameter was not included in the API response. It is now discontinued.

autoMountStatus -> (string)

The status of automatically mounting a storage disk to a virtual computer.

### Warning

This parameter only applies to Lightsail for Research resources.

ramSizeInGb -> (float)

The amount of RAM in GB on the instance (`1.0` ).

networking -> (structure)

Information about the public ports and monthly data transfer rates for the instance.

monthlyTransfer -> (structure)

The amount of data in GB allocated for monthly data transfers.

gbPerMonthAllocated -> (integer)

The amount allocated per month (in GB).

ports -> (list)

An array of key-value pairs containing information about the ports on the instance.

(structure)

Describes information about ports for an Amazon Lightsail instance.

fromPort -> (integer)

The first port in a range of open ports on an instance.

Allowed ports:

- TCP and UDP - `0` to `65535`
- ICMP - The ICMP type for IPv4 addresses. For example, specify `8` as the `fromPort` (ICMP type), and `-1` as the `toPort` (ICMP code), to enable ICMP Ping. For more information, see [Control Messages](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages) on *Wikipedia* .
- ICMPv6 - The ICMP type for IPv6 addresses. For example, specify `128` as the `fromPort` (ICMPv6 type), and `0` as `toPort` (ICMPv6 code). For more information, see [Internet Control Message Protocol for IPv6](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6) .

toPort -> (integer)

The last port in a range of open ports on an instance.

Allowed ports:

- TCP and UDP - `0` to `65535`
- ICMP - The ICMP code for IPv4 addresses. For example, specify `8` as the `fromPort` (ICMP type), and `-1` as the `toPort` (ICMP code), to enable ICMP Ping. For more information, see [Control Messages](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages) on *Wikipedia* .
- ICMPv6 - The ICMP code for IPv6 addresses. For example, specify `128` as the `fromPort` (ICMPv6 type), and `0` as `toPort` (ICMPv6 code). For more information, see [Internet Control Message Protocol for IPv6](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6) .

protocol -> (string)

The IP protocol name.

The name can be one of the following:

- `tcp` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesnât require reliable data stream service, use UDP instead.
- `all` - All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on *Wikipedia* .
- `udp` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that donât require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
- `icmp` - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify `icmp` as the `protocol` , you must specify the ICMP type using the `fromPort` parameter, and ICMP code using the `toPort` parameter.
- `icmp6` - Internet Control Message Protocol (ICMP) for IPv6. When you specify `icmp6` as the `protocol` , you must specify the ICMP type using the `fromPort` parameter, and ICMP code using the `toPort` parameter.

accessFrom -> (string)

The location from which access is allowed. For example, `Anywhere (0.0.0.0/0)` , or `Custom` if a specific IP address or range of IP addresses is allowed.

accessType -> (string)

The type of access (`Public` or `Private` ).

commonName -> (string)

The common name of the port information.

accessDirection -> (string)

The access direction (`inbound` or `outbound` ).

### Note

Lightsail currently supports only `inbound` access direction.

cidrs -> (list)

The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.

### Note

The `ipv6Cidrs` parameter lists the IPv6 addresses that are allowed to connect to an instance.

For more information about CIDR block notation, see [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) on *Wikipedia* .

(string)

ipv6Cidrs -> (list)

The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used.

### Note

The `cidrs` parameter lists the IPv4 addresses that are allowed to connect to an instance.

For more information about CIDR block notation, see [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) on *Wikipedia* .

(string)

cidrListAliases -> (list)

An alias that defines access for a preconfigured range of IP addresses.

The only alias currently supported is `lightsail-connect` , which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.

(string)

state -> (structure)

The status code and the state (`running` ) for the instance.

code -> (integer)

The status code for the instance.

name -> (string)

The state of the instance (`running` or `pending` ).

username -> (string)

The user name for connecting to the instance (`ec2-user` ).

sshKeyName -> (string)

The name of the SSH key being used to connect to the instance (`LightsailDefaultKeyPair` ).

metadataOptions -> (structure)

The metadata options for the Amazon Lightsail instance.

state -> (string)

The state of the metadata option changes.

The following states are possible:

- `pending` - The metadata options are being updated. The instance is not yet ready to process metadata traffic with the new selection.
- `applied` - The metadata options have been successfully applied to the instance.

httpTokens -> (string)

The state of token usage for your instance metadata requests.

If the state is `optional` , you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.

If the state is `required` , you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.

### Warning

Not all instance blueprints in Lightsail support version 2.0 credentials. Use the `MetadataNoToken` instance metric to track the number of calls to the instance metadata service that are using version 1.0 credentials. For more information, see [Viewing instance metrics in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-health-metrics) in the *Amazon Lightsail Developer Guide* .

httpEndpoint -> (string)

Indicates whether the HTTP metadata endpoint on your instances is enabled or disabled.

If the value is `disabled` , you cannot access your instance metadata.

httpPutResponseHopLimit -> (integer)

The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther.

httpProtocolIpv6 -> (string)

Indicates whether the IPv6 endpoint for the instance metadata service is enabled or disabled.