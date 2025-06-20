# enable-trust-anchorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/enable-trust-anchor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/enable-trust-anchor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rolesanywhere](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/index.html#cli-aws-rolesanywhere) ]

# enable-trust-anchor

## Description

Enables a trust anchor. When enabled, certificates in the trust anchor chain are authorized for trust validation.

**Required permissions:** `rolesanywhere:EnableTrustAnchor` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rolesanywhere-2018-05-10/EnableTrustAnchor)

## Synopsis

```
enable-trust-anchor
--trust-anchor-id <value>
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

`--trust-anchor-id` (string)

The unique identifier of the trust anchor.

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

trustAnchor -> (structure)

The state of the trust anchor after a read or write operation.

createdAt -> (timestamp)

The ISO-8601 timestamp when the trust anchor was created.

enabled -> (boolean)

Indicates whether the trust anchor is enabled.

name -> (string)

The name of the trust anchor.

notificationSettings -> (list)

A list of notification settings to be associated to the trust anchor.

(structure)

The state of a notification setting.

A notification setting includes information such as event name, threshold, status of the notification setting, and the channel to notify.

channel -> (string)

The specified channel of notification. IAM Roles Anywhere uses CloudWatch metrics, EventBridge, and Health Dashboard to notify for an event.

### Note

In the absence of a specific channel, IAM Roles Anywhere applies this setting to âALLâ channels.

configuredBy -> (string)

The principal that configured the notification setting. For default settings configured by IAM Roles Anywhere, the value is `rolesanywhere.amazonaws.com` , and for customized notifications settings, it is the respective account ID.

enabled -> (boolean)

Indicates whether the notification setting is enabled.

event -> (string)

The event to which this notification setting is applied.

threshold -> (integer)

The number of days before a notification event.

source -> (structure)

The trust anchor type and its related certificate data.

sourceData -> (tagged union structure)

The data field of the trust anchor depending on its type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `acmPcaArn`, `x509CertificateData`.

acmPcaArn -> (string)

The root certificate of the Private Certificate Authority specified by this ARN is used in trust validation for temporary credential requests. Included for trust anchors of type `AWS_ACM_PCA` .

x509CertificateData -> (string)

The PEM-encoded data for the certificate anchor. Included for trust anchors of type `CERTIFICATE_BUNDLE` .

sourceType -> (string)

The type of the trust anchor.

trustAnchorArn -> (string)

The ARN of the trust anchor.

trustAnchorId -> (string)

The unique identifier of the trust anchor.

updatedAt -> (timestamp)

The ISO-8601 timestamp when the trust anchor was last updated.