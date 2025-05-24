# set-risk-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-risk-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-risk-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# set-risk-configuration

## Description

Configures threat protection for a user pool or app client. Sets configuration for the following.

- Responses to risks with adaptive authentication
- Responses to vulnerable passwords with compromised-credentials detection
- Notifications to users who have had risky activity detected
- IP-address denylist and allowlist

To set the risk configuration for the user pool to defaults, send this request with only the `UserPoolId` parameter. To reset the threat protection settings of an app client to be inherited from the user pool, send `UserPoolId` and `ClientId` parameters only. To change threat protection to audit-only or off, update the value of `UserPoolAddOns` in an `UpdateUserPool` request. To activate this setting, your user pool must be on the [Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetRiskConfiguration)

## Synopsis

```
set-risk-configuration
--user-pool-id <value>
[--client-id <value>]
[--compromised-credentials-risk-configuration <value>]
[--account-takeover-risk-configuration <value>]
[--risk-exception-configuration <value>]
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

The ID of the user pool where you want to set a risk configuration. If you include `UserPoolId` in your request, donât include `ClientId` . When the client ID is null, the same risk configuration is applied to all the clients in the userPool. When you include both `ClientId` and `UserPoolId` , Amazon Cognito maps the configuration to the app client only.

`--client-id` (string)

The ID of the app client where you want to set a risk configuration. If `ClientId` is null, then the risk configuration is mapped to `UserPoolId` . When the client ID is null, the same risk configuration is applied to all the clients in the userPool.

When you include a `ClientId` parameter, Amazon Cognito maps the configuration to the app client. When you include both `ClientId` and `UserPoolId` , Amazon Cognito maps the configuration to the app client only.

`--compromised-credentials-risk-configuration` (structure)

The configuration of automated reactions to detected compromised credentials. Includes settings for blocking future sign-in requests and for the types of password-submission events you want to monitor.

EventFilter -> (list)

Settings for the sign-in activity where you want to configure compromised-credentials actions. Defaults to all events.

(string)

Actions -> (structure)

Settings for the actions that you want your user pool to take when Amazon Cognito detects compromised credentials.

EventAction -> (string)

The action that Amazon Cognito takes when it detects compromised credentials.

Shorthand Syntax:

```
EventFilter=string,string,Actions={EventAction=string}
```

JSON Syntax:

```
{
  "EventFilter": ["SIGN_IN"|"PASSWORD_CHANGE"|"SIGN_UP", ...],
  "Actions": {
    "EventAction": "BLOCK"|"NO_ACTION"
  }
}
```

`--account-takeover-risk-configuration` (structure)

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

Shorthand Syntax:

```
NotifyConfiguration={From=string,ReplyTo=string,SourceArn=string,BlockEmail={Subject=string,HtmlBody=string,TextBody=string},NoActionEmail={Subject=string,HtmlBody=string,TextBody=string},MfaEmail={Subject=string,HtmlBody=string,TextBody=string}},Actions={LowAction={Notify=boolean,EventAction=string},MediumAction={Notify=boolean,EventAction=string},HighAction={Notify=boolean,EventAction=string}}
```

JSON Syntax:

```
{
  "NotifyConfiguration": {
    "From": "string",
    "ReplyTo": "string",
    "SourceArn": "string",
    "BlockEmail": {
      "Subject": "string",
      "HtmlBody": "string",
      "TextBody": "string"
    },
    "NoActionEmail": {
      "Subject": "string",
      "HtmlBody": "string",
      "TextBody": "string"
    },
    "MfaEmail": {
      "Subject": "string",
      "HtmlBody": "string",
      "TextBody": "string"
    }
  },
  "Actions": {
    "LowAction": {
      "Notify": true|false,
      "EventAction": "BLOCK"|"MFA_IF_CONFIGURED"|"MFA_REQUIRED"|"NO_ACTION"
    },
    "MediumAction": {
      "Notify": true|false,
      "EventAction": "BLOCK"|"MFA_IF_CONFIGURED"|"MFA_REQUIRED"|"NO_ACTION"
    },
    "HighAction": {
      "Notify": true|false,
      "EventAction": "BLOCK"|"MFA_IF_CONFIGURED"|"MFA_REQUIRED"|"NO_ACTION"
    }
  }
}
```

`--risk-exception-configuration` (structure)

A set of IP-address overrides to threat protection. You can set up IP-address always-block and always-allow lists.

BlockedIPRangeList -> (list)

An always-block IP address list. Overrides the risk decision and always blocks authentication requests. This parameter is displayed and set in CIDR notation.

(string)

SkippedIPRangeList -> (list)

An always-allow IP address list. Risk detection isnât performed on the IP addresses in this range list. This parameter is displayed and set in CIDR notation.

(string)

Shorthand Syntax:

```
BlockedIPRangeList=string,string,SkippedIPRangeList=string,string
```

JSON Syntax:

```
{
  "BlockedIPRangeList": ["string", ...],
  "SkippedIPRangeList": ["string", ...]
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

**To set the threat protection risk configuration**

The following `set-risk-configuration` example configures threat protection messages and actions, compromised credentials, and IP address exceptions in the requested app client. Because of the complexity of the NotifyConfiguration object, JSON input is a best practice for this command.

```
aws cognito-idp set-risk-configuration \
    --cli-input-json file://set-risk-configuration.json
```

Contents of `set-risk-configuration.json`:

```
{
    "AccountTakeoverRiskConfiguration": {
        "Actions": {
            "HighAction": {
                "EventAction": "MFA_REQUIRED",
                "Notify": true
            },
            "LowAction": {
                "EventAction": "NO_ACTION",
                "Notify": true
            },
            "MediumAction": {
                "EventAction": "MFA_IF_CONFIGURED",
                "Notify": true
            }
        },
        "NotifyConfiguration": {
            "BlockEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "Blocked sign-in attempt",
                "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "From": "admin@example.com",
            "MfaEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "New sign-in attempt",
                "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "NoActionEmail": {
                "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                "Subject": "New sign-in attempt",
                "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
            },
            "ReplyTo": "admin@example.com",
            "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com"
        }
    },
    "ClientId": "1example23456789",
    "CompromisedCredentialsRiskConfiguration": {
        "Actions": {
            "EventAction": "BLOCK"
        },
        "EventFilter": [
            "PASSWORD_CHANGE",
            "SIGN_UP",
            "SIGN_IN"
        ]
    },
    "RiskExceptionConfiguration": {
        "BlockedIPRangeList": [
            "192.0.2.1/32",
            "192.0.2.2/32"
        ],
        "SkippedIPRangeList": [
            "203.0.113.1/32",
            "203.0.113.2/32"
        ]
    },
    "UserPoolId": "us-west-2_EXAMPLE"
}
```

Output:

```
{
    "RiskConfiguration": {
        "AccountTakeoverRiskConfiguration": {
            "Actions": {
                "HighAction": {
                    "EventAction": "MFA_REQUIRED",
                    "Notify": true
                },
                "LowAction": {
                    "EventAction": "NO_ACTION",
                    "Notify": true
                },
                "MediumAction": {
                    "EventAction": "MFA_IF_CONFIGURED",
                    "Notify": true
                }
            },
            "NotifyConfiguration": {
                "BlockEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "Blocked sign-in attempt",
                    "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "From": "admin@example.com",
                "MfaEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "New sign-in attempt",
                    "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "NoActionEmail": {
                    "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>",
                    "Subject": "New sign-in attempt",
                    "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know"
                },
                "ReplyTo": "admin@example.com",
                "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com"
            }
        },
        "ClientId": "1example23456789",
        "CompromisedCredentialsRiskConfiguration": {
            "Actions": {
                "EventAction": "BLOCK"
            },
            "EventFilter": [
                "PASSWORD_CHANGE",
                "SIGN_UP",
                "SIGN_IN"
            ]
        },
        "RiskExceptionConfiguration": {
            "BlockedIPRangeList": [
                "192.0.2.1/32",
                "192.0.2.2/32"
            ],
            "SkippedIPRangeList": [
                "203.0.113.1/32",
                "203.0.113.2/32"
            ]
        },
        "UserPoolId": "us-west-2_EXAMPLE"
    }
}
```

For more information, see [Threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html) in the *Amazon Cognito Developer Guide*.

## Output

RiskConfiguration -> (structure)

The API response that contains the risk configuration that you set and the timestamp of the most recent change.

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