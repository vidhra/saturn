# describe-risk-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-risk-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-risk-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# describe-risk-configuration

## Description

Given an app client or user pool ID where threat protection is configured, describes the risk configuration. This operation returns details about adaptive authentication, compromised credentials, and IP-address allow- and denylists. For more information about threat protection, see [Threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/DescribeRiskConfiguration)

## Synopsis

```
describe-risk-configuration
--user-pool-id <value>
[--client-id <value>]
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

`--user-pool-id` (string)

The ID of the user pool with the risk configuration that you want to inspect. You can apply default risk configuration at the user pool level and further customize it from user pool defaults at the app-client level. Specify `ClientId` to inspect client-level configuration, or `UserPoolId` to inspect pool-level configuration.

`--client-id` (string)

The ID of the app client with the risk configuration that you want to inspect. You can apply default risk configuration at the user pool level and further customize it from user pool defaults at the app-client level. Specify `ClientId` to inspect client-level configuration, or `UserPoolId` to inspect pool-level configuration.

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

**To describe a risk configuration**

This example describes the risk configuration associated with pool us-west-2_aaaaaaaaa.

Command:

```
aws cognito-idp describe-risk-configuration --user-pool-id us-west-2_aaaaaaaaa
```

Output:

```
{
  "RiskConfiguration": {
      "UserPoolId": "us-west-2_aaaaaaaaa",
      "CompromisedCredentialsRiskConfiguration": {
          "EventFilter": [
              "SIGN_IN",
              "SIGN_UP",
              "PASSWORD_CHANGE"
          ],
          "Actions": {
              "EventAction": "BLOCK"
          }
      },
      "AccountTakeoverRiskConfiguration": {
          "NotifyConfiguration": {
              "From": "diego@example.com",
              "ReplyTo": "diego@example.com",
              "SourceArn": "arn:aws:ses:us-east-1:111111111111:identity/diego@example.com",
              "BlockEmail": {
                  "Subject": "Blocked sign-in attempt",
                  "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                  "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
              },
              "NoActionEmail": {
                  "Subject": "New sign-in attempt",
                  "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                  "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
              },
              "MfaEmail": {
                  "Subject": "New sign-in attempt",
                  "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                  "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
              }
          },
          "Actions": {
              "LowAction": {
                  "Notify": true,
                  "EventAction": "NO_ACTION"
              },
              "MediumAction": {
                  "Notify": true,
                  "EventAction": "MFA_IF_CONFIGURED"
              },
              "HighAction": {
                  "Notify": true,
                  "EventAction": "MFA_IF_CONFIGURED"
              }
          }
      }
  }
}
```

## Output

RiskConfiguration -> (structure)

The details of the requested risk configuration.

UserPoolId -> (string)

The ID of the user pool that has the risk configuration applied.

ClientId -> (string)

The app client where this configuration is applied. When this parameter isnât present, the risk configuration applies to all user pool app clients that donât have client-level settings.

CompromisedCredentialsRiskConfiguration -> (structure)

Settings for compromised-credentials actions and authentication types with threat protection in full-function `ENFORCED` mode.

EventFilter -> (list)

Settings for the sign-in activity where you want to configure compromised-credentials actions. Defaults to all events.

(string)

Actions -> (structure)

Settings for the actions that you want your user pool to take when Amazon Cognito detects compromised credentials.

EventAction -> (string)

The action that Amazon Cognito takes when it detects compromised credentials.

AccountTakeoverRiskConfiguration -> (structure)

The settings for automated responses and notification templates for adaptive authentication with threat protection.

NotifyConfiguration -> (structure)

The settings for composing and sending an email message when threat protection assesses a risk level with adaptive authentication. When you choose to notify users in `AccountTakeoverRiskConfiguration` , Amazon Cognito sends an email message using the method and template that you set with this data type.

From -> (string)

The email address that sends the email message. The address must be either individually verified with Amazon Simple Email Service, or from a domain that has been verified with Amazon SES.

ReplyTo -> (string)

The reply-to email address of an email template.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the identity that is associated with the sending authorization policy. This identity permits Amazon Cognito to send for the email address specified in the `From` parameter.

BlockEmail -> (structure)

The template for the email message that your user pool sends when a detected risk event is blocked.

Subject -> (string)

The subject of the threat protection email notification.

HtmlBody -> (string)

The body of an email notification formatted in HTML. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

TextBody -> (string)

The body of an email notification formatted in plaintext. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

NoActionEmail -> (structure)

The template for the email message that your user pool sends when no action is taken in response to a detected risk.

Subject -> (string)

The subject of the threat protection email notification.

HtmlBody -> (string)

The body of an email notification formatted in HTML. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

TextBody -> (string)

The body of an email notification formatted in plaintext. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

MfaEmail -> (structure)

The template for the email message that your user pool sends when MFA is challenged in response to a detected risk.

Subject -> (string)

The subject of the threat protection email notification.

HtmlBody -> (string)

The body of an email notification formatted in HTML. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

TextBody -> (string)

The body of an email notification formatted in plaintext. Choose an `HtmlBody` or a `TextBody` to send an HTML-formatted or plaintext message, respectively.

Actions -> (structure)

A list of account-takeover actions for each level of risk that Amazon Cognito might assess with threat protection.

LowAction -> (structure)

The action that you assign to a low-risk assessment by threat protection.

Notify -> (boolean)

Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a userâs session at the associated risk level.

EventAction -> (string)

The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:

- `BLOCK` : Block the request.
- `MFA_IF_CONFIGURED` : Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesnât have a phone number attribute, MFA setup isnât possible. If MFA setup isnât possible, allow the request.
- `MFA_REQUIRED` : Present an MFA challenge if possible. Block the request if a user hasnât set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.
- `NO_ACTION` : Take no action. Permit sign-in.

MediumAction -> (structure)

The action that you assign to a medium-risk assessment by threat protection.

Notify -> (boolean)

Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a userâs session at the associated risk level.

EventAction -> (string)

The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:

- `BLOCK` : Block the request.
- `MFA_IF_CONFIGURED` : Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesnât have a phone number attribute, MFA setup isnât possible. If MFA setup isnât possible, allow the request.
- `MFA_REQUIRED` : Present an MFA challenge if possible. Block the request if a user hasnât set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.
- `NO_ACTION` : Take no action. Permit sign-in.

HighAction -> (structure)

The action that you assign to a high-risk assessment by threat protection.

Notify -> (boolean)

Determines whether Amazon Cognito sends a user a notification message when your user pools assesses a userâs session at the associated risk level.

EventAction -> (string)

The action to take for the attempted account takeover action for the associated risk level. Valid values are as follows:

- `BLOCK` : Block the request.
- `MFA_IF_CONFIGURED` : Present an MFA challenge if possible. MFA is possible if the user pool has active MFA methods that the user can set up. For example, if the user pool only supports SMS message MFA but the user doesnât have a phone number attribute, MFA setup isnât possible. If MFA setup isnât possible, allow the request.
- `MFA_REQUIRED` : Present an MFA challenge if possible. Block the request if a user hasnât set up MFA. To sign in with required MFA, users must have an email address or phone number attribute, or a registered TOTP factor.
- `NO_ACTION` : Take no action. Permit sign-in.

RiskExceptionConfiguration -> (structure)

Exceptions to the risk evaluation configuration, including always-allow and always-block IP address ranges.

BlockedIPRangeList -> (list)

An always-block IP address list. Overrides the risk decision and always blocks authentication requests. This parameter is displayed and set in CIDR notation.

(string)

SkippedIPRangeList -> (list)

An always-allow IP address list. Risk detection isnât performed on the IP addresses in this range list. This parameter is displayed and set in CIDR notation.

(string)

LastModifiedDate -> (timestamp)

The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.