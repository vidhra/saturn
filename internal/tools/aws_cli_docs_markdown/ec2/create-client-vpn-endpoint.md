# create-client-vpn-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-client-vpn-endpoint

## Description

Creates a Client VPN endpoint. A Client VPN endpoint is the resource you create and configure to enable and manage client VPN sessions. It is the destination endpoint at which all client VPN sessions are terminated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateClientVpnEndpoint)

## Synopsis

```
create-client-vpn-endpoint
--client-cidr-block <value>
--server-certificate-arn <value>
--authentication-options <value>
--connection-log-options <value>
[--dns-servers <value>]
[--transport-protocol <value>]
[--vpn-port <value>]
[--description <value>]
[--split-tunnel | --no-split-tunnel]
[--dry-run | --no-dry-run]
[--client-token <value>]
[--tag-specifications <value>]
[--security-group-ids <value>]
[--vpc-id <value>]
[--self-service-portal <value>]
[--client-connect-options <value>]
[--session-timeout-hours <value>]
[--client-login-banner-options <value>]
[--client-route-enforcement-options <value>]
[--disconnect-on-session-timeout | --no-disconnect-on-session-timeout]
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

`--client-cidr-block` (string)

The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. Client CIDR range must have a size of at least /22 and must not be greater than /12.

`--server-certificate-arn` (string)

The ARN of the server certificate. For more information, see the [Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/) .

`--authentication-options` (list)

Information about the authentication method to be used to authenticate clients.

(structure)

Describes the authentication method to be used by a Client VPN endpoint. For more information, see [Authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/authentication-authrization.html#client-authentication) in the *Client VPN Administrator Guide* .

Type -> (string)

The type of client authentication to be used.

ActiveDirectory -> (structure)

Information about the Active Directory to be used, if applicable. You must provide this information if **Type** is `directory-service-authentication` .

DirectoryId -> (string)

The ID of the Active Directory to be used for authentication.

MutualAuthentication -> (structure)

Information about the authentication certificates to be used, if applicable. You must provide this information if **Type** is `certificate-authentication` .

ClientRootCertificateChainArn -> (string)

The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in Certificate Manager (ACM).

FederatedAuthentication -> (structure)

Information about the IAM SAML identity provider to be used, if applicable. You must provide this information if **Type** is `federated-authentication` .

SAMLProviderArn -> (string)

The Amazon Resource Name (ARN) of the IAM SAML identity provider.

SelfServiceSAMLProviderArn -> (string)

The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.

Shorthand Syntax:

```
Type=string,ActiveDirectory={DirectoryId=string},MutualAuthentication={ClientRootCertificateChainArn=string},FederatedAuthentication={SAMLProviderArn=string,SelfServiceSAMLProviderArn=string} ...
```

JSON Syntax:

```
[
  {
    "Type": "certificate-authentication"|"directory-service-authentication"|"federated-authentication",
    "ActiveDirectory": {
      "DirectoryId": "string"
    },
    "MutualAuthentication": {
      "ClientRootCertificateChainArn": "string"
    },
    "FederatedAuthentication": {
      "SAMLProviderArn": "string",
      "SelfServiceSAMLProviderArn": "string"
    }
  }
  ...
]
```

`--connection-log-options` (structure)

Information about the client connection logging options.

If you enable client connection logging, data about client connections is sent to a Cloudwatch Logs log stream. The following information is logged:

- Client connection requests
- Client connection results (successful and unsuccessful)
- Reasons for unsuccessful client connection requests
- Client connection termination time

Enabled -> (boolean)

Indicates whether connection logging is enabled.

CloudwatchLogGroup -> (string)

The name of the CloudWatch Logs log group. Required if connection logging is enabled.

CloudwatchLogStream -> (string)

The name of the CloudWatch Logs log stream to which the connection data is published.

Shorthand Syntax:

```
Enabled=boolean,CloudwatchLogGroup=string,CloudwatchLogStream=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "CloudwatchLogGroup": "string",
  "CloudwatchLogStream": "string"
}
```

`--dns-servers` (list)

Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address configured on the device is used for the DNS server.

(string)

Syntax:

```
"string" "string" ...
```

`--transport-protocol` (string)

The transport protocol to be used by the VPN session.

Default value: `udp`

Possible values:

- `tcp`
- `udp`

`--vpn-port` (integer)

The port number to assign to the Client VPN endpoint for TCP and UDP traffic.

Valid Values: `443` | `1194`

Default Value: `443`

`--description` (string)

A brief description of the Client VPN endpoint.

`--split-tunnel` | `--no-split-tunnel` (boolean)

Indicates whether split-tunnel is enabled on the Client VPN endpoint.

By default, split-tunnel on a VPN endpoint is disabled.

For information about split-tunnel VPN endpoints, see [Split-tunnel Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the *Client VPN Administrator Guide* .

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--tag-specifications` (list)

The tags to apply to the Client VPN endpoint during creation.

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

`--security-group-ids` (list)

The IDs of one or more security groups to apply to the target network. You must also specify the ID of the VPC that contains the security groups.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-id` (string)

The ID of the VPC to associate with the Client VPN endpoint. If no security group IDs are specified in the request, the default security group for the VPC is applied.

`--self-service-portal` (string)

Specify whether to enable the self-service portal for the Client VPN endpoint.

Default Value: `enabled`

Possible values:

- `enabled`
- `disabled`

`--client-connect-options` (structure)

The options for managing connection authorization for new client connections.

Enabled -> (boolean)

Indicates whether client connect options are enabled. The default is `false` (not enabled).

LambdaFunctionArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.

Shorthand Syntax:

```
Enabled=boolean,LambdaFunctionArn=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "LambdaFunctionArn": "string"
}
```

`--session-timeout-hours` (integer)

The maximum VPN session duration time in hours.

Valid values: `8 | 10 | 12 | 24`

Default value: `24`

`--client-login-banner-options` (structure)

Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.

Enabled -> (boolean)

Enable or disable a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.

Valid values: `true | false`

Default value: `false`

BannerText -> (string)

Customizable text that will be displayed in a banner on Amazon Web Services provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

Shorthand Syntax:

```
Enabled=boolean,BannerText=string
```

JSON Syntax:

```
{
  "Enabled": true|false,
  "BannerText": "string"
}
```

`--client-route-enforcement-options` (structure)

Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.

Enforced -> (boolean)

Enable or disable Client Route Enforcement. The state can either be `true` (enabled) or `false` (disabled). The default is `false` .

Valid values: `true | false`

Default value: `false`

Shorthand Syntax:

```
Enforced=boolean
```

JSON Syntax:

```
{
  "Enforced": true|false
}
```

`--disconnect-on-session-timeout` | `--no-disconnect-on-session-timeout` (boolean)

Indicates whether the client VPN session is disconnected after the maximum timeout specified in `SessionTimeoutHours` is reached. If `true` , users are prompted to reconnect client VPN. If `false` , client VPN attempts to reconnect automatically. The default value is `true` .

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

**To create a Client VPN endpoint**

The following `create-client-vpn-endpoint` example creates a Client VPN endpoint that uses mutual authentication and specifies a value for the client CIDR block.

```
aws ec2 create-client-vpn-endpoint \
    --client-cidr-block "172.31.0.0/16" \
    --server-certificate-arn arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE} \
    --connection-log-options Enabled=false
```

Output:

```
{
    "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde",
    "Status": {
        "Code": "pending-associate"
    },
    "DnsName": "cvpn-endpoint-123456789123abcde.prod.clientvpn.ap-south-1.amazonaws.com"
}
```

For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html) in the *AWS Client VPN Administrator Guide*.

## Output

ClientVpnEndpointId -> (string)

The ID of the Client VPN endpoint.

Status -> (structure)

The current state of the Client VPN endpoint.

Code -> (string)

The state of the Client VPN endpoint. Possible states include:

- `pending-associate` - The Client VPN endpoint has been created but no target networks have been associated. The Client VPN endpoint cannot accept connections.
- `available` - The Client VPN endpoint has been created and a target network has been associated. The Client VPN endpoint can accept connections.
- `deleting` - The Client VPN endpoint is being deleted. The Client VPN endpoint cannot accept connections.
- `deleted` - The Client VPN endpoint has been deleted. The Client VPN endpoint cannot accept connections.

Message -> (string)

A message about the status of the Client VPN endpoint.

DnsName -> (string)

The DNS name to be used by clients when establishing their VPN session.