# modify-vpn-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-vpn-connection

## Description

Modifies the customer gateway or the target gateway of an Amazon Web Services Site-to-Site VPN connection. To modify the target gateway, the following migration options are available:

- An existing virtual private gateway to a new virtual private gateway
- An existing virtual private gateway to a transit gateway
- An existing transit gateway to a new transit gateway
- An existing transit gateway to a virtual private gateway

Before you perform the migration to the new gateway, you must configure the new gateway. Use  CreateVpnGateway to create a virtual private gateway, or  CreateTransitGateway to create a transit gateway.

This step is required when you migrate from a virtual private gateway with static routes to a transit gateway.

You must delete the static routes before you migrate to the new gateway.

Keep a copy of the static route before you delete it. You will need to add back these routes to the transit gateway after the VPN connection migration is complete.

After you migrate to the new gateway, you might need to modify your VPC route table. Use  CreateRoute and  DeleteRoute to make the changes described in [Update VPC route tables](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-target.html#step-update-routing) in the *Amazon Web Services Site-to-Site VPN User Guide* .

When the new gateway is a transit gateway, modify the transit gateway route table to allow traffic between the VPC and the Amazon Web Services Site-to-Site VPN connection. Use  CreateTransitGatewayRoute to add the routes.

If you deleted VPN static routes, you must add the static routes to the transit gateway route table.

After you perform this operation, the VPN endpointâs IP addresses on the Amazon Web Services side and the tunnel options remain intact. Your Amazon Web Services Site-to-Site VPN connection will be temporarily unavailable for a brief period while we provision the new endpoints.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyVpnConnection)

## Synopsis

```
modify-vpn-connection
--vpn-connection-id <value>
[--transit-gateway-id <value>]
[--customer-gateway-id <value>]
[--vpn-gateway-id <value>]
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

`--vpn-connection-id` (string)

The ID of the VPN connection.

`--transit-gateway-id` (string)

The ID of the transit gateway.

`--customer-gateway-id` (string)

The ID of the customer gateway at your end of the VPN connection.

`--vpn-gateway-id` (string)

The ID of the virtual private gateway at the Amazon Web Services side of the VPN connection.

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

**To modify a VPN connection**

The following `modify-vpn-connection` example changes the target gateway for VPN connection `vpn-12345678901234567` to virtual private gateway `vgw-11223344556677889`:

```
aws ec2 modify-vpn-connection \
    --vpn-connection-id vpn-12345678901234567 \
    --vpn-gateway-id vgw-11223344556677889
```

Output:

```
{
    "VpnConnection": {
        "CustomerGatewayConfiguration": "...configuration information...",
        "CustomerGatewayId": "cgw-aabbccddee1122334",
        "Category": "VPN",
        "State": "modifying",
        "Type": "ipsec.1",
        "VpnConnectionId": "vpn-12345678901234567",
        "VpnGatewayId": "vgw-11223344556677889",
        "Options": {
            "StaticRoutesOnly": false
        },
        "VgwTelemetry": [
            {
                "AcceptedRouteCount": 0,
                "LastStatusChange": "2019-07-17T07:34:00.000Z",
                "OutsideIpAddress": "18.210.3.222",
                "Status": "DOWN",
                "StatusMessage": "IPSEC IS DOWN"
            },
            {
                "AcceptedRouteCount": 0,
                "LastStatusChange": "2019-07-20T21:20:16.000Z",
                "OutsideIpAddress": "34.193.129.33",
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