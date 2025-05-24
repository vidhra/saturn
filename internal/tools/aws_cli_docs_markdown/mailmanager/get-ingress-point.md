# get-ingress-pointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/get-ingress-point.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/get-ingress-point.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mailmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/index.html#cli-aws-mailmanager) ]

# get-ingress-point

## Description

Fetch ingress endpoint resource attributes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mailmanager-2023-10-17/GetIngressPoint)

## Synopsis

```
get-ingress-point
--ingress-point-id <value>
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

`--ingress-point-id` (string)

The identifier of an ingress endpoint.

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

## Output

ARecord -> (string)

The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager.

CreatedTimestamp -> (timestamp)

The timestamp of when the ingress endpoint was created.

IngressPointArn -> (string)

The Amazon Resource Name (ARN) of the ingress endpoint resource.

IngressPointAuthConfiguration -> (structure)

The authentication configuration of the ingress endpoint resource.

IngressPointPasswordConfiguration -> (structure)

The ingress endpoint password configuration for the ingress endpoint resource.

PreviousSmtpPasswordExpiryTimestamp -> (timestamp)

The previous password expiry timestamp of the ingress endpoint resource.

PreviousSmtpPasswordVersion -> (string)

The previous password version of the ingress endpoint resource.

SmtpPasswordVersion -> (string)

The current password expiry timestamp of the ingress endpoint resource.

SecretArn -> (string)

The ingress endpoint SecretsManager::Secret ARN configuration for the ingress endpoint resource.

IngressPointId -> (string)

The identifier of an ingress endpoint resource.

IngressPointName -> (string)

A user friendly name for the ingress endpoint.

LastUpdatedTimestamp -> (timestamp)

The timestamp of when the ingress endpoint was last updated.

NetworkConfiguration -> (tagged union structure)

The network configuration for the ingress point.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PrivateNetworkConfiguration`, `PublicNetworkConfiguration`.

PrivateNetworkConfiguration -> (structure)

Specifies the network configuration for the private ingress point.

VpcEndpointId -> (string)

The identifier of the VPC endpoint to associate with this private ingress point.

PublicNetworkConfiguration -> (structure)

Specifies the network configuration for the public ingress point.

IpType -> (string)

The IP address type for the public ingress point. Valid values are IPV4 and DUAL_STACK.

RuleSetId -> (string)

The identifier of a rule set resource associated with the ingress endpoint.

Status -> (string)

The status of the ingress endpoint resource.

TrafficPolicyId -> (string)

The identifier of the traffic policy resource associated with the ingress endpoint.

Type -> (string)

The type of ingress endpoint.