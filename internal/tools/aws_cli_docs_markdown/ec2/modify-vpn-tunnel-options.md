# modify-vpn-tunnel-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-tunnel-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-tunnel-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-vpn-tunnel-options

## Description

Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site VPN connection. You can modify multiple options for a tunnel in a single request, but you can only modify one tunnel at a time. For more information, see [Site-to-Site VPN tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html) in the *Amazon Web Services Site-to-Site VPN User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVpnTunnelOptions)

## Synopsis

```
modify-vpn-tunnel-options
--vpn-connection-id <value>
--vpn-tunnel-outside-ip-address <value>
--tunnel-options <value>
[--dry-run | --no-dry-run]
[--skip-tunnel-replacement | --no-skip-tunnel-replacement]
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

`--vpn-connection-id` (string)

The ID of the Amazon Web Services Site-to-Site VPN connection.

`--vpn-tunnel-outside-ip-address` (string)

The external IP address of the VPN tunnel.

`--tunnel-options` (structure)

The tunnel options to modify.

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

The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and the customer gateway.

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

The number of seconds after which a DPD timeout occurs. A DPD timeout of 40 seconds means that the VPN endpoint will consider the peer dead 30 seconds after the first failed keep-alive.

Constraints: A value greater than or equal to 30.

Default: `40`

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

Shorthand Syntax:

```
TunnelInsideCidr=string,TunnelInsideIpv6Cidr=string,PreSharedKey=string,Phase1LifetimeSeconds=integer,Phase2LifetimeSeconds=integer,RekeyMarginTimeSeconds=integer,RekeyFuzzPercentage=integer,ReplayWindowSize=integer,DPDTimeoutSeconds=integer,DPDTimeoutAction=string,Phase1EncryptionAlgorithms=[{Value=string},{Value=string}],Phase2EncryptionAlgorithms=[{Value=string},{Value=string}],Phase1IntegrityAlgorithms=[{Value=string},{Value=string}],Phase2IntegrityAlgorithms=[{Value=string},{Value=string}],Phase1DHGroupNumbers=[{Value=integer},{Value=integer}],Phase2DHGroupNumbers=[{Value=integer},{Value=integer}],IKEVersions=[{Value=string},{Value=string}],StartupAction=string,LogOptions={CloudWatchLogOptions={LogEnabled=boolean,LogGroupArn=string,LogOutputFormat=string}},EnableTunnelLifecycleControl=boolean
```

JSON Syntax:

```
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
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--skip-tunnel-replacement` | `--no-skip-tunnel-replacement` (boolean)

Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off `EnableTunnelLifecycleControl` .

Valid values: `True` | `False`

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

**To modify the tunnel options for a VPN connection**

The following `modify-vpn-tunnel-options` example updates the Diffie-Hellman groups that are permitted for the specified tunnel and VPN connection.

```
aws ec2 modify-vpn-tunnel-options \
    --vpn-connection-id vpn-12345678901234567 \
    --vpn-tunnel-outside-ip-address 203.0.113.17 \
    --tunnel-options Phase1DHGroupNumbers=[{Value=14},{Value=15},{Value=16},{Value=17},{Value=18}],Phase2DHGroupNumbers=[{Value=14},{Value=15},{Value=16},{Value=17},{Value=18}]
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "...configuration information...",
        "CustomerGatewayId": "cgw-aabbccddee1122334",
        "Category": "VPN",
        "State": "available",
        "Type": "ipsec.1",
        "VpnConnectionId": "vpn-12345678901234567",
        "VpnGatewayId": "vgw-11223344556677889",
        "Options": {
            "StaticRoutesOnly": false,
            "TunnelOptions": [
                {
                    "OutsideIpAddress": "203.0.113.17",
                    "Phase1DHGroupNumbers": [
                        {
                            "Value": 14
                        },
                        {
                            "Value": 15
                        },
                        {
                            "Value": 16
                        },
                        {
                            "Value": 17
                        },
                        {
                            "Value": 18
                        }
                    ],
                    "Phase2DHGroupNumbers": [
                        {
                            "Value": 14
                        },
                        {
                            "Value": 15
                        },
                        {
                            "Value": 16
                        },
                        {
                            "Value": 17
                        },
                        {
                            "Value": 18
                        }
                    ]
                },
                {
                    "OutsideIpAddress": "203.0.114.19"
                }
            ]
        },
        "VgwTelemetry": [
            {
                "AcceptedRouteCount": 0,
                "LastStatusChange": "2019-09-10T21:56:54.000Z",
                "OutsideIpAddress": "203.0.113.17",
                "Status": "DOWN",
                "StatusMessage": "IPSEC IS DOWN"
            },
            {
                "AcceptedRouteCount": 0,
                "LastStatusChange": "2019-09-10T21:56:43.000Z",
                "OutsideIpAddress": "203.0.114.19",
                "Status": "DOWN",
                "StatusMessage": "IPSEC IS DOWN"
            }
        ]
    }
}
```

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