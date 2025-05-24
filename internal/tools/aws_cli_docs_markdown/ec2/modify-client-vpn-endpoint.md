# modify-client-vpn-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-client-vpn-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-client-vpn-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-client-vpn-endpoint

## Description

Modifies the specified Client VPN endpoint. Modifying the DNS server resets existing client connections.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyClientVpnEndpoint)

## Synopsis

```
modify-client-vpn-endpoint
--client-vpn-endpoint-id <value>
[--server-certificate-arn <value>]
[--connection-log-options <value>]
[--dns-servers <value>]
[--vpn-port <value>]
[--description <value>]
[--split-tunnel | --no-split-tunnel]
[--dry-run | --no-dry-run]
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

`--client-vpn-endpoint-id` (string)

The ID of the Client VPN endpoint to modify.

`--server-certificate-arn` (string)

The ARN of the server certificate to be used. The server certificate must be provisioned in Certificate Manager (ACM).

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

`--dns-servers` (structure)

Information about the DNS servers to be used by Client VPN connections. A Client VPN endpoint can have up to two DNS servers.

CustomDnsServers -> (list)

The IPv4 address range, in CIDR notation, of the DNS servers to be used. You can specify up to two DNS servers. Ensure that the DNS servers can be reached by the clients. The specified values overwrite the existing values.

(string)

Enabled -> (boolean)

Indicates whether DNS servers should be used. Specify `False` to delete the existing DNS servers.

Shorthand Syntax:

```
CustomDnsServers=string,string,Enabled=boolean
```

JSON Syntax:

```
{
  "CustomDnsServers": ["string", ...],
  "Enabled": true|false
}
```

`--vpn-port` (integer)

The port number to assign to the Client VPN endpoint for TCP and UDP traffic.

Valid Values: `443` | `1194`

Default Value: `443`

`--description` (string)

A brief description of the Client VPN endpoint.

`--split-tunnel` | `--no-split-tunnel` (boolean)

Indicates whether the VPN is split-tunnel.

For information about split-tunnel VPN endpoints, see [Split-tunnel Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html) in the *Client VPN Administrator Guide* .

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--security-group-ids` (list)

The IDs of one or more security groups to apply to the target network.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-id` (string)

The ID of the VPC to associate with the Client VPN endpoint.

`--self-service-portal` (string)

Specify whether to enable the self-service portal for the Client VPN endpoint.

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

Indicates whether the client VPN session is disconnected after the maximum timeout specified in `sessionTimeoutHours` is reached. If `true` , users are prompted to reconnect client VPN. If `false` , client VPN attempts to reconnect automatically. The default value is `true` .

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

**To modify a Client VPN endpoint**

The following `modify-client-vpn-endpoint` example enables client connection logging for the specified Client VPN endpoint.

```
aws ec2 modify-client-vpn-endpoint \
    --client-vpn-endpoint-id cvpn-endpoint-123456789123abcde \
    --connection-log-options Enabled=true,CloudwatchLogGroup=ClientVPNLogs
```

Output:

```
{
    "Return": true
}
```

For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html) in the *AWS Client VPN Administrator Guide*.

## Output

Return -> (boolean)

Returns `true` if the request succeeds; otherwise, it returns an error.