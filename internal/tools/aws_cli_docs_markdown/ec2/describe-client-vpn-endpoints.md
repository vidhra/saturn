# describe-client-vpn-endpointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-endpoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-endpoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-client-vpn-endpoints

## Description

Describes one or more Client VPN endpoints in the account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeClientVpnEndpoints)

`describe-client-vpn-endpoints` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ClientVpnEndpoints`

## Synopsis

```
describe-client-vpn-endpoints
[--client-vpn-endpoint-ids <value>]
[--filters <value>]
[--dry-run | --no-dry-run]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--client-vpn-endpoint-ids` (list)

The ID of the Client VPN endpoint.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

One or more filters. Filter names and values are case-sensitive.

- `endpoint-id` - The ID of the Client VPN endpoint.
- `transport-protocol` - The transport protocol (`tcp` | `udp` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe your Client VPN endpoints**

The following `describe-client-vpn-endpoints` example displays details about all of your Client VPN endpoints.

```
aws ec2 describe-client-vpn-endpoints
```

Output:

```
{
    "ClientVpnEndpoints": [
        {
            "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde",
            "Description": "Endpoint for Admin access",
            "Status": {
                "Code": "available"
            },
            "CreationTime": "2020-11-13T11:37:27",
            "DnsName": "*.cvpn-endpoint-123456789123abcde.prod.clientvpn.ap-south-1.amazonaws.com",
            "ClientCidrBlock": "172.31.0.0/16",
            "DnsServers": [
                "8.8.8.8"
            ],
            "SplitTunnel": false,
            "VpnProtocol": "openvpn",
            "TransportProtocol": "udp",
            "VpnPort": 443,
            "ServerCertificateArn": "arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "AuthenticationOptions": [
                {
                    "Type": "certificate-authentication",
                    "MutualAuthentication": {
                        "ClientRootCertificateChain": "arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE"
                    }
                }
            ],
            "ConnectionLogOptions": {
                "Enabled": true,
                "CloudwatchLogGroup": "Client-vpn-connection-logs",
                "CloudwatchLogStream": "cvpn-endpoint-123456789123abcde-ap-south-1-2020/11/13-FCD8HEMVaCcw"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Client VPN"
                }
            ],
            "SecurityGroupIds": [
                "sg-aabbcc11223344567"
            ],
            "VpcId": "vpc-a87f92c1",
            "SelfServicePortalUrl": "https://self-service.clientvpn.amazonaws.com/endpoints/cvpn-endpoint-123456789123abcde",
            "ClientConnectOptions": {
                 "Enabled": false
            }
        }
    ]
}
```

For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html) in the *AWS Client VPN Administrator Guide*.

## Output

ClientVpnEndpoints -> (list)

Information about the Client VPN endpoints.

(structure)

Describes a Client VPN endpoint.

ClientVpnEndpointId -> (string)

The ID of the Client VPN endpoint.

Description -> (string)

A brief description of the endpoint.

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

CreationTime -> (string)

The date and time the Client VPN endpoint was created.

DeletionTime -> (string)

The date and time the Client VPN endpoint was deleted, if applicable.

DnsName -> (string)

The DNS name to be used by clients when connecting to the Client VPN endpoint.

ClientCidrBlock -> (string)

The IPv4 address range, in CIDR notation, from which client IP addresses are assigned.

DnsServers -> (list)

Information about the DNS servers to be used for DNS resolution.

(string)

SplitTunnel -> (boolean)

Indicates whether split-tunnel is enabled in the Client VPN endpoint.

For information about split-tunnel VPN endpoints, see [Split-Tunnel Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the *Client VPN Administrator Guide* .

VpnProtocol -> (string)

The protocol used by the VPN session.

TransportProtocol -> (string)

The transport protocol used by the Client VPN endpoint.

VpnPort -> (integer)

The port number for the Client VPN endpoint.

AssociatedTargetNetworks -> (list)

Information about the associated target networks. A target network is a subnet in a VPC.

(structure)

Describes a target network that is associated with a Client VPN endpoint. A target network is a subnet in a VPC.

NetworkId -> (string)

The ID of the subnet.

NetworkType -> (string)

The target network type.

ServerCertificateArn -> (string)

The ARN of the server certificate.

AuthenticationOptions -> (list)

Information about the authentication method used by the Client VPN endpoint.

(structure)

Describes the authentication methods used by a Client VPN endpoint. For more information, see [Authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html) in the *Client VPN Administrator Guide* .

Type -> (string)

The authentication type used.

ActiveDirectory -> (structure)

Information about the Active Directory, if applicable.

DirectoryId -> (string)

The ID of the Active Directory used for authentication.

MutualAuthentication -> (structure)

Information about the authentication certificates, if applicable.

ClientRootCertificateChain -> (string)

The ARN of the client certificate.

FederatedAuthentication -> (structure)

Information about the IAM SAML identity provider, if applicable.

SamlProviderArn -> (string)

The Amazon Resource Name (ARN) of the IAM SAML identity provider.

SelfServiceSamlProviderArn -> (string)

The Amazon Resource Name (ARN) of the IAM SAML identity provider for the self-service portal.

ConnectionLogOptions -> (structure)

Information about the client connection logging options for the Client VPN endpoint.

Enabled -> (boolean)

Indicates whether client connection logging is enabled for the Client VPN endpoint.

CloudwatchLogGroup -> (string)

The name of the Amazon CloudWatch Logs log group to which connection logging data is published.

CloudwatchLogStream -> (string)

The name of the Amazon CloudWatch Logs log stream to which connection logging data is published.

Tags -> (list)

Any tags assigned to the Client VPN endpoint.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

SecurityGroupIds -> (list)

The IDs of the security groups for the target network.

(string)

VpcId -> (string)

The ID of the VPC.

SelfServicePortalUrl -> (string)

The URL of the self-service portal.

ClientConnectOptions -> (structure)

The options for managing connection authorization for new client connections.

Enabled -> (boolean)

Indicates whether client connect options are enabled.

LambdaFunctionArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.

Status -> (structure)

The status of any updates to the client connect options.

Code -> (string)

The status code.

Message -> (string)

The status message.

SessionTimeoutHours -> (integer)

The maximum VPN session duration time in hours.

Valid values: `8 | 10 | 12 | 24`

Default value: `24`

ClientLoginBannerOptions -> (structure)

Options for enabling a customizable text banner that will be displayed on Amazon Web Services provided clients when a VPN session is established.

Enabled -> (boolean)

Current state of text banner feature.

Valid values: `true | false`

BannerText -> (string)

Customizable text that will be displayed in a banner on Amazon Web Services provided clients when a VPN session is established. UTF-8 encoded characters only. Maximum of 1400 characters.

ClientRouteEnforcementOptions -> (structure)

Client route enforcement is a feature of the Client VPN service that helps enforce administrator defined routes on devices connected through the VPN. T his feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client route enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.

Enforced -> (boolean)

Status of the client route enforcement feature, indicating whether Client Route Enforcement is `true` (enabled) or `false` (disabled).

Valid values: `true | false`

Default value: `false`

DisconnectOnSessionTimeout -> (boolean)

Indicates whether the client VPN session is disconnected after the maximum `sessionTimeoutHours` is reached. If `true` , users are prompted to reconnect client VPN. If `false` , client VPN attempts to reconnect automatically. The default value is `true` .

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.