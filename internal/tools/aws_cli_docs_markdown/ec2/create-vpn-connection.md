# create-vpn-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-vpn-connection

## Description

Creates a VPN connection between an existing virtual private gateway or transit gateway and a customer gateway. The supported connection type is `ipsec.1` .

The response includes information that you need to give to your network administrator to configure your customer gateway.

### Warning

We strongly recommend that you use HTTPS when calling this operation because the response contains sensitive cryptographic information for configuring your customer gateway device.

If you decide to shut down your VPN connection for any reason and later create a new VPN connection, you must reconfigure your customer gateway with the new information returned from this call.

This is an idempotent operation. If you perform the operation more than once, Amazon EC2 doesnât return an error.

For more information, see [Amazon Web Services Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *Amazon Web Services Site-to-Site VPN User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVpnConnection)

## Synopsis

```
create-vpn-connection
--customer-gateway-id <value>
--type <value>
[--vpn-gateway-id <value>]
[--transit-gateway-id <value>]
[--tag-specifications <value>]
[--dry-run | --no-dry-run]
[--options <value>]
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

`--customer-gateway-id` (string)

The ID of the customer gateway.

`--type` (string)

The type of VPN connection (`ipsec.1` ).

`--vpn-gateway-id` (string)

The ID of the virtual private gateway. If you specify a virtual private gateway, you cannot specify a transit gateway.

`--transit-gateway-id` (string)

The ID of the transit gateway. If you specify a transit gateway, you cannot specify a virtual private gateway.

`--tag-specifications` (list)

The tags to apply to the VPN connection.

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--options` (structure)

The options for the VPN connection.

EnableAcceleration -> (boolean)

Indicate whether to enable acceleration for the VPN connection.

Default: `false`

TunnelInsideIpVersion -> (string)

Indicate whether the VPN tunnels process IPv4 or IPv6 traffic.

Default: `ipv4`

TunnelOptions -> (list)

The tunnel options for the VPN connection.

(structure)

The tunnel options for a single VPN tunnel.

TunnelInsideCidr -> (string)

The range of inside IPv4 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway.

Constraints: A size /30 CIDR block from the `169.254.0.0/16` range. The following CIDR blocks are reserved and cannot be used:

- `169.254.0.0/30`
- `169.254.1.0/30`
- `169.254.2.0/30`
- `169.254.3.0/30`
- `169.254.4.0/30`
- `169.254.5.0/30`
- `169.254.169.252/30`

TunnelInsideIpv6Cidr -> (string)

The range of inside IPv6 addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same transit gateway.

Constraints: A size /126 CIDR block from the local `fd00::/8` range.

PreSharedKey -> (string)

The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.

Constraints: Allowed characters are alphanumeric characters, periods (.), and underscores (_). Must be between 8 and 64 characters in length and cannot start with zero (0).

Phase1LifetimeSeconds -> (integer)

The lifetime for phase 1 of the IKE negotiation, in seconds.

Constraints: A value between 900 and 28,800.

Default: `28800`

Phase2LifetimeSeconds -> (integer)

The lifetime for phase 2 of the IKE negotiation, in seconds.

Constraints: A value between 900 and 3,600. The value must be less than the value for `Phase1LifetimeSeconds` .

Default: `3600`

RekeyMarginTimeSeconds -> (integer)

The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for `RekeyFuzzPercentage` .

Constraints: A value between 60 and half of `Phase2LifetimeSeconds` .

Default: `270`

RekeyFuzzPercentage -> (integer)

The percentage of the rekey window (determined by `RekeyMarginTimeSeconds` ) during which the rekey time is randomly selected.

Constraints: A value between 0 and 100.

Default: `100`

ReplayWindowSize -> (integer)

The number of packets in an IKE replay window.

Constraints: A value between 64 and 2048.

Default: `1024`

DPDTimeoutSeconds -> (integer)

The number of seconds after which a DPD timeout occurs.

Constraints: A value greater than or equal to 30.

Default: `30`

DPDTimeoutAction -> (string)

The action to take after DPD timeout occurs. Specify `restart` to restart the IKE initiation. Specify `clear` to end the IKE session.

Valid Values: `clear` | `none` | `restart`

Default: `clear`

Phase1EncryptionAlgorithms -> (list)

One or more encryption algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.

Valid values: `AES128` | `AES256` | `AES128-GCM-16` | `AES256-GCM-16`

(structure)

Specifies the encryption algorithm for the VPN tunnel for phase 1 IKE negotiations.

Value -> (string)

The value for the encryption algorithm.

Phase2EncryptionAlgorithms -> (list)

One or more encryption algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.

Valid values: `AES128` | `AES256` | `AES128-GCM-16` | `AES256-GCM-16`

(structure)

Specifies the encryption algorithm for the VPN tunnel for phase 2 IKE negotiations.

Value -> (string)

The encryption algorithm.

Phase1IntegrityAlgorithms -> (list)

One or more integrity algorithms that are permitted for the VPN tunnel for phase 1 IKE negotiations.

Valid values: `SHA1` | `SHA2-256` | `SHA2-384` | `SHA2-512`

(structure)

Specifies the integrity algorithm for the VPN tunnel for phase 1 IKE negotiations.

Value -> (string)

The value for the integrity algorithm.

Phase2IntegrityAlgorithms -> (list)

One or more integrity algorithms that are permitted for the VPN tunnel for phase 2 IKE negotiations.

Valid values: `SHA1` | `SHA2-256` | `SHA2-384` | `SHA2-512`

(structure)

Specifies the integrity algorithm for the VPN tunnel for phase 2 IKE negotiations.

Value -> (string)

The integrity algorithm.

Phase1DHGroupNumbers -> (list)

One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 1 IKE negotiations.

Valid values: `2` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24`

(structure)

Specifies a Diffie-Hellman group number for the VPN tunnel for phase 1 IKE negotiations.

Value -> (integer)

The Diffie-Hellmann group number.

Phase2DHGroupNumbers -> (list)

One or more Diffie-Hellman group numbers that are permitted for the VPN tunnel for phase 2 IKE negotiations.

Valid values: `2` | `5` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24`

(structure)

Specifies a Diffie-Hellman group number for the VPN tunnel for phase 2 IKE negotiations.

Value -> (integer)

The Diffie-Hellmann group number.

IKEVersions -> (list)

The IKE versions that are permitted for the VPN tunnel.

Valid values: `ikev1` | `ikev2`

(structure)

The IKE version that is permitted for the VPN tunnel.

Value -> (string)

The IKE version.

StartupAction -> (string)

The action to take when the establishing the tunnel for the VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify `start` for Amazon Web Services to initiate the IKE negotiation.

Valid Values: `add` | `start`

Default: `add`

LogOptions -> (structure)

Options for logging VPN tunnel activity.

CloudWatchLogOptions -> (structure)

Options for sending VPN tunnel logs to CloudWatch.

LogEnabled -> (boolean)

Enable or disable VPN tunnel logging feature. Default value is `False` .

Valid values: `True` | `False`

LogGroupArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.

LogOutputFormat -> (string)

Set log format. Default format is `json` .

Valid values: `json` | `text`

EnableTunnelLifecycleControl -> (boolean)

Turn on or off tunnel endpoint lifecycle control feature.

LocalIpv4NetworkCidr -> (string)

The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.

Default: `0.0.0.0/0`

RemoteIpv4NetworkCidr -> (string)

The IPv4 CIDR on the Amazon Web Services side of the VPN connection.

Default: `0.0.0.0/0`

LocalIpv6NetworkCidr -> (string)

The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.

Default: `::/0`

RemoteIpv6NetworkCidr -> (string)

The IPv6 CIDR on the Amazon Web Services side of the VPN connection.

Default: `::/0`

OutsideIpAddressType -> (string)

The type of IPv4 address assigned to the outside interface of the customer gateway device.

Valid values: `PrivateIpv4` | `PublicIpv4`

Default: `PublicIpv4`

TransportTransitGatewayAttachmentId -> (string)

The transit gateway attachment ID to use for the VPN tunnel.

Required if `OutsideIpAddressType` is set to `PrivateIpv4` .

StaticRoutesOnly -> (boolean)

Indicate whether the VPN connection uses static routes only. If you are creating a VPN connection for a device that does not support BGP, you must specify `true` . Use  CreateVpnConnectionRoute to create a static route.

Default: `false`

JSON Syntax:

```
{
  "EnableAcceleration": true|false,
  "TunnelInsideIpVersion": "ipv4"|"ipv6",
  "TunnelOptions": [
    {
      "TunnelInsideCidr": "string",
      "TunnelInsideIpv6Cidr": "string",
      "PreSharedKey": "string",
      "Phase1LifetimeSeconds": integer,
      "Phase2LifetimeSeconds": integer,
      "RekeyMarginTimeSeconds": integer,
      "RekeyFuzzPercentage": integer,
      "ReplayWindowSize": integer,
      "DPDTimeoutSeconds": integer,
      "DPDTimeoutAction": "string",
      "Phase1EncryptionAlgorithms": [
        {
          "Value": "string"
        }
        ...
      ],
      "Phase2EncryptionAlgorithms": [
        {
          "Value": "string"
        }
        ...
      ],
      "Phase1IntegrityAlgorithms": [
        {
          "Value": "string"
        }
        ...
      ],
      "Phase2IntegrityAlgorithms": [
        {
          "Value": "string"
        }
        ...
      ],
      "Phase1DHGroupNumbers": [
        {
          "Value": integer
        }
        ...
      ],
      "Phase2DHGroupNumbers": [
        {
          "Value": integer
        }
        ...
      ],
      "IKEVersions": [
        {
          "Value": "string"
        }
        ...
      ],
      "StartupAction": "string",
      "LogOptions": {
        "CloudWatchLogOptions": {
          "LogEnabled": true|false,
          "LogGroupArn": "string",
          "LogOutputFormat": "string"
        }
      },
      "EnableTunnelLifecycleControl": true|false
    }
    ...
  ],
  "LocalIpv4NetworkCidr": "string",
  "RemoteIpv4NetworkCidr": "string",
  "LocalIpv6NetworkCidr": "string",
  "RemoteIpv6NetworkCidr": "string",
  "OutsideIpAddressType": "string",
  "TransportTransitGatewayAttachmentId": "string",
  "StaticRoutesOnly": true|false
}
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

**Example 1: To create a VPN connection with dynamic routing**

The following `create-vpn-connection` example creates a VPN connection between the specified virtual private gateway and the specified customer gateway, and applies tags to the VPN connection. The output includes the configuration information for your customer gateway device, in XML format.

```
aws ec2 create-vpn-connection \
    --type ipsec.1 \
    --customer-gateway-id cgw-001122334455aabbc \
    --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2 \
    --tag-specification 'ResourceType=vpn-connection,Tags=[{Key=Name,Value=BGP-VPN}]'
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "...configuration information...",
        "CustomerGatewayId": "cgw-001122334455aabbc",
        "Category": "VPN",
        "State": "pending",
        "VpnConnectionId": "vpn-123123123123abcab",
        "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",
        "Options": {
            "EnableAcceleration": false,
            "StaticRoutesOnly": false,
            "LocalIpv4NetworkCidr": "0.0.0.0/0",
            "RemoteIpv4NetworkCidr": "0.0.0.0/0",
            "TunnelInsideIpVersion": "ipv4",
            "TunnelOptions": [
                {},
                {}
            ]
        },
        "Routes": [],
        "Tags": [
             {
                "Key": "Name",
                "Value": "BGP-VPN"
            }
        ]
    }
}
```

For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) in the *AWS Site-to-Site VPN User Guide*.

**Example 2: To create a VPN connection with static routing**

The following `create-vpn-connection` example creates a VPN connection between the specified virtual private gateway and the specified customer gateway. The options specify static routing. The output includes the configuration information for your customer gateway device, in XML format.

```
aws ec2 create-vpn-connection \
    --type ipsec.1 \
    --customer-gateway-id cgw-001122334455aabbc \
    --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2 \
    --options "{\"StaticRoutesOnly\":true}"
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "..configuration information...",
        "CustomerGatewayId": "cgw-001122334455aabbc",
        "Category": "VPN",
        "State": "pending",
        "VpnConnectionId": "vpn-123123123123abcab",
        "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",
        "Options": {
            "EnableAcceleration": false,
            "StaticRoutesOnly": true,
            "LocalIpv4NetworkCidr": "0.0.0.0/0",
            "RemoteIpv4NetworkCidr": "0.0.0.0/0",
            "TunnelInsideIpVersion": "ipv4",
            "TunnelOptions": [
                {},
                {}
            ]
        },
        "Routes": [],
        "Tags": []
    }
}
```

For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) in the *AWS Site-to-Site VPN User Guide*.

**Example 3: To create a VPN connection and specify your own inside CIDR and pre-shared key**

The following `create-vpn-connection` example creates a VPN connection and specifies the inside IP address CIDR block and a custom pre-shared key for each tunnel. The specified values are returned in the `CustomerGatewayConfiguration` information.

```
aws ec2 create-vpn-connection \
    --type ipsec.1 \
    --customer-gateway-id cgw-001122334455aabbc \
    --vpn-gateway-id vgw-1a1a1a1a1a1a2b2b2 \
    --options TunnelOptions='[{TunnelInsideCidr=169.254.12.0/30,PreSharedKey=ExamplePreSharedKey1},{TunnelInsideCidr=169.254.13.0/30,PreSharedKey=ExamplePreSharedKey2}]'
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "..configuration information...",
        "CustomerGatewayId": "cgw-001122334455aabbc",
        "Category": "VPN",
        "State": "pending",
        "VpnConnectionId": "vpn-123123123123abcab",
        "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2",
        "Options": {
            "EnableAcceleration": false,
            "StaticRoutesOnly": false,
            "LocalIpv4NetworkCidr": "0.0.0.0/0",
            "RemoteIpv4NetworkCidr": "0.0.0.0/0",
            "TunnelInsideIpVersion": "ipv4",
            "TunnelOptions": [
                {
                    "OutsideIpAddress": "203.0.113.3",
                    "TunnelInsideCidr": "169.254.12.0/30",
                    "PreSharedKey": "ExamplePreSharedKey1"
                },
                {
                    "OutsideIpAddress": "203.0.113.5",
                    "TunnelInsideCidr": "169.254.13.0/30",
                    "PreSharedKey": "ExamplePreSharedKey2"
                }
            ]
        },
        "Routes": [],
        "Tags": []
    }
}
```

For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) in the *AWS Site-to-Site VPN User Guide*.

**Example 4: To create a VPN connection that supports IPv6 traffic**

The following `create-vpn-connection` example creates a VPN connection that supports IPv6 traffic between the specified transit gateway and specified customer gateway. The tunnel options for both tunnels specify that AWS must initiate the IKE negotiation.

```
aws ec2 create-vpn-connection \
    --type ipsec.1 \
    --transit-gateway-id tgw-12312312312312312 \
    --customer-gateway-id cgw-001122334455aabbc \
    --options TunnelInsideIpVersion=ipv6,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "..configuration information...",
        "CustomerGatewayId": "cgw-001122334455aabbc",
        "Category": "VPN",
        "State": "pending",
        "VpnConnectionId": "vpn-11111111122222222",
        "TransitGatewayId": "tgw-12312312312312312",
        "Options": {
            "EnableAcceleration": false,
            "StaticRoutesOnly": false,
            "LocalIpv6NetworkCidr": "::/0",
            "RemoteIpv6NetworkCidr": "::/0",
            "TunnelInsideIpVersion": "ipv6",
            "TunnelOptions": [
                {
                    "OutsideIpAddress": "203.0.113.3",
                    "StartupAction": "start"
                },
                {
                    "OutsideIpAddress": "203.0.113.5",
                    "StartupAction": "start"
                }
            ]
        },
        "Routes": [],
        "Tags": []
    }
}
```

For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html) in the *AWS Site-to-Site VPN User Guide*.

## Output

VpnConnection -> (structure)

Information about the VPN connection.

Category -> (string)

The category of the VPN connection. A value of `VPN` indicates an Amazon Web Services VPN connection. A value of `VPN-Classic` indicates an Amazon Web Services Classic VPN connection.

TransitGatewayId -> (string)

The ID of the transit gateway associated with the VPN connection.

CoreNetworkArn -> (string)

The ARN of the core network.

CoreNetworkAttachmentArn -> (string)

The ARN of the core network attachment.

GatewayAssociationState -> (string)

The current state of the gateway association.

Options -> (structure)

The VPN connection options.

EnableAcceleration -> (boolean)

Indicates whether acceleration is enabled for the VPN connection.

StaticRoutesOnly -> (boolean)

Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that donât support BGP.

LocalIpv4NetworkCidr -> (string)

The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.

RemoteIpv4NetworkCidr -> (string)

The IPv4 CIDR on the Amazon Web Services side of the VPN connection.

LocalIpv6NetworkCidr -> (string)

The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.

RemoteIpv6NetworkCidr -> (string)

The IPv6 CIDR on the Amazon Web Services side of the VPN connection.

OutsideIpAddressType -> (string)

The type of IPv4 address assigned to the outside interface of the customer gateway.

Valid values: `PrivateIpv4` | `PublicIpv4`

Default: `PublicIpv4`

TransportTransitGatewayAttachmentId -> (string)

The transit gateway attachment ID in use for the VPN tunnel.

TunnelInsideIpVersion -> (string)

Indicates whether the VPN tunnels process IPv4 or IPv6 traffic.

TunnelOptions -> (list)

Indicates the VPN tunnel options.

(structure)

The VPN tunnel options.

OutsideIpAddress -> (string)

The external IP address of the VPN tunnel.

TunnelInsideCidr -> (string)

The range of inside IPv4 addresses for the tunnel.

TunnelInsideIpv6Cidr -> (string)

The range of inside IPv6 addresses for the tunnel.

PreSharedKey -> (string)

The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and the customer gateway.

Phase1LifetimeSeconds -> (integer)

The lifetime for phase 1 of the IKE negotiation, in seconds.

Phase2LifetimeSeconds -> (integer)

The lifetime for phase 2 of the IKE negotiation, in seconds.

RekeyMarginTimeSeconds -> (integer)

The margin time, in seconds, before the phase 2 lifetime expires, during which the Amazon Web Services side of the VPN connection performs an IKE rekey.

RekeyFuzzPercentage -> (integer)

The percentage of the rekey window determined by `RekeyMarginTimeSeconds` during which the rekey time is randomly selected.

ReplayWindowSize -> (integer)

The number of packets in an IKE replay window.

DpdTimeoutSeconds -> (integer)

The number of seconds after which a DPD timeout occurs.

DpdTimeoutAction -> (string)

The action to take after a DPD timeout occurs.

Phase1EncryptionAlgorithms -> (list)

The permitted encryption algorithms for the VPN tunnel for phase 1 IKE negotiations.

(structure)

The encryption algorithm for phase 1 IKE negotiations.

Value -> (string)

The value for the encryption algorithm.

Phase2EncryptionAlgorithms -> (list)

The permitted encryption algorithms for the VPN tunnel for phase 2 IKE negotiations.

(structure)

The encryption algorithm for phase 2 IKE negotiations.

Value -> (string)

The encryption algorithm.

Phase1IntegrityAlgorithms -> (list)

The permitted integrity algorithms for the VPN tunnel for phase 1 IKE negotiations.

(structure)

The integrity algorithm for phase 1 IKE negotiations.

Value -> (string)

The value for the integrity algorithm.

Phase2IntegrityAlgorithms -> (list)

The permitted integrity algorithms for the VPN tunnel for phase 2 IKE negotiations.

(structure)

The integrity algorithm for phase 2 IKE negotiations.

Value -> (string)

The integrity algorithm.

Phase1DHGroupNumbers -> (list)

The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 1 IKE negotiations.

(structure)

The Diffie-Hellmann group number for phase 1 IKE negotiations.

Value -> (integer)

The Diffie-Hellmann group number.

Phase2DHGroupNumbers -> (list)

The permitted Diffie-Hellman group numbers for the VPN tunnel for phase 2 IKE negotiations.

(structure)

The Diffie-Hellmann group number for phase 2 IKE negotiations.

Value -> (integer)

The Diffie-Hellmann group number.

IkeVersions -> (list)

The IKE versions that are permitted for the VPN tunnel.

(structure)

The internet key exchange (IKE) version permitted for the VPN tunnel.

Value -> (string)

The IKE version.

StartupAction -> (string)

The action to take when the establishing the VPN tunnels for a VPN connection.

LogOptions -> (structure)

Options for logging VPN tunnel activity.

CloudWatchLogOptions -> (structure)

Options for sending VPN tunnel logs to CloudWatch.

LogEnabled -> (boolean)

Status of VPN tunnel logging feature. Default value is `False` .

Valid values: `True` | `False`

LogGroupArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.

LogOutputFormat -> (string)

Configured log format. Default format is `json` .

Valid values: `json` | `text`

EnableTunnelLifecycleControl -> (boolean)

Status of tunnel endpoint lifecycle control feature.

Routes -> (list)

The static routes associated with the VPN connection.

(structure)

Describes a static route for a VPN connection.

DestinationCidrBlock -> (string)

The CIDR block associated with the local subnet of the customer data center.

Source -> (string)

Indicates how the routes were provided.

State -> (string)

The current state of the static route.

Tags -> (list)

Any tags assigned to the VPN connection.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

VgwTelemetry -> (list)

Information about the VPN tunnel.

(structure)

Describes telemetry for a VPN tunnel.

AcceptedRouteCount -> (integer)

The number of accepted routes.

LastStatusChange -> (timestamp)

The date and time of the last change in status. This field is updated when changes in IKE (Phase 1), IPSec (Phase 2), or BGP status are detected.

OutsideIpAddress -> (string)

The Internet-routable IP address of the virtual private gatewayâs outside interface.

Status -> (string)

The status of the VPN tunnel.

StatusMessage -> (string)

If an error occurs, a description of the error.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the VPN tunnel endpoint certificate.

VpnConnectionId -> (string)

The ID of the VPN connection.

State -> (string)

The current state of the VPN connection.

CustomerGatewayConfiguration -> (string)

The configuration information for the VPN connectionâs customer gateway (in the native XML format). This element is always present in the  CreateVpnConnection response; however, itâs present in the  DescribeVpnConnections response only if the VPN connection is in the `pending` or `available` state.

Type -> (string)

The type of VPN connection.

CustomerGatewayId -> (string)

The ID of the customer gateway at your end of the VPN connection.

VpnGatewayId -> (string)

The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.