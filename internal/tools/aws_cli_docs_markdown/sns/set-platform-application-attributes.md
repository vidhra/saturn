# set-platform-application-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-platform-application-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-platform-application-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/index.html#cli-aws-sns) ]

# set-platform-application-attributes

## Description

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM (Firebase Cloud Messaging). For more information, see [Using Amazon SNS Mobile Push Notifications](https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html) . For information on configuring attributes for message delivery status, see [Using Amazon SNS Application Attributes for Message Delivery Status](https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetPlatformApplicationAttributes)

## Synopsis

```
set-platform-application-attributes
--platform-application-arn <value>
--attributes <value>
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

`--platform-application-arn` (string)

`PlatformApplicationArn` for `SetPlatformApplicationAttributes` action.

`--attributes` (map)

A map of the platform application attributes. Attributes in this map include the following:

- `PlatformCredential` â The credential received from the notification service.
- For ADM, `PlatformCredential` is client secret.
- For Apple Services using certificate credentials, `PlatformCredential` is private key.
- For Apple Services using token credentials, `PlatformCredential` is signing key.
- For GCM (Firebase Cloud Messaging) using key credentials, there is no `PlatformPrincipal` . The `PlatformCredential` is `API key` .
- For GCM (Firebase Cloud Messaging) using token credentials, there is no `PlatformPrincipal` . The `PlatformCredential` is a JSON formatted private key file. When using the Amazon Web Services CLI, the file must be in string format and special characters must be ignored. To format the file correctly, Amazon SNS recommends using the following command: `SERVICE_JSON=`jq @json <<< cat service.json`` .
- `PlatformPrincipal` â The principal received from the notification service.
- For ADM, `PlatformPrincipal` is client id.
- For Apple Services using certificate credentials, `PlatformPrincipal` is SSL certificate.
- For Apple Services using token credentials, `PlatformPrincipal` is signing key ID.
- For GCM (Firebase Cloud Messaging), there is no `PlatformPrincipal` .
- `EventEndpointCreated` â Topic ARN to which `EndpointCreated` event notifications are sent.
- `EventEndpointDeleted` â Topic ARN to which `EndpointDeleted` event notifications are sent.
- `EventEndpointUpdated` â Topic ARN to which `EndpointUpdate` event notifications are sent.
- `EventDeliveryFailure` â Topic ARN to which `DeliveryFailure` event notifications are sent upon Direct Publish delivery failure (permanent) to one of the applicationâs endpoints.
- `SuccessFeedbackRoleArn` â IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
- `FailureFeedbackRoleArn` â IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.
- `SuccessFeedbackSampleRate` â Sample rate percentage (0-100) of successfully delivered messages.

The following attributes only apply to `APNs` token-based authentication:

- `ApplePlatformTeamID` â The identifier thatâs assigned to your Apple developer account team.
- `ApplePlatformBundleID` â The bundle identifier thatâs assigned to your iOS app.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To set platform application attributes**

The following `set-platform-application-attributes` example sets the `EventDeliveryFailure` attribute for the specified platform application to the ARN of the specified Amazon SNS topic.

```
aws sns set-platform-application-attributes \
    --platform-application-arn arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication \
    --attributes EventDeliveryFailure=arn:aws:sns:us-west-2:123456789012:AnotherTopic
```

This command produces no output.

## Output

None