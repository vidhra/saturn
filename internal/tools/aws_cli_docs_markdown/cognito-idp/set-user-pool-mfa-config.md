# set-user-pool-mfa-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-pool-mfa-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-pool-mfa-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# set-user-pool-mfa-config

## Description

Sets user pool multi-factor authentication (MFA) and passkey configuration. For more information about user pool MFA, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) . For more information about WebAuthn passkeys see [Authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey) .

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SetUserPoolMfaConfig)

## Synopsis

```
set-user-pool-mfa-config
--user-pool-id <value>
[--sms-mfa-configuration <value>]
[--software-token-mfa-configuration <value>]
[--email-mfa-configuration <value>]
[--mfa-configuration <value>]
[--web-authn-configuration <value>]
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

The user pool ID.

`--sms-mfa-configuration` (structure)

Configures user pool SMS messages for MFA. Sets the message template and the SMS message sending configuration for Amazon SNS.

SmsAuthenticationMessage -> (string)

The SMS authentication message that will be sent to users with the code they must sign in with. The message must contain the `{####}` placeholder. Your user pool replaces the placeholder with the MFA code. If this parameter isnât provided, your user pool sends a default message.

SmsConfiguration -> (structure)

User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account.

You can set `SmsConfiguration` in `CreateUserPool` and `UpdateUserPool` , or in `SetUserPoolMfaConfig` .

SnsCallerArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your Amazon Web Services account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a [spending limit](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html) .

ExternalId -> (string)

The external ID provides additional security for your IAM role. You can use an `ExternalId` with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an `ExternalId` , your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the `ExternalID` . If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the `ExternalId` .

For more information about the `ExternalId` of a role, see [How to use an external ID when granting access to your Amazon Web Services resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) .

SnsRegion -> (string)

The Amazon Web Services Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported **Legacy Amazon SNS alternate Region** .

Amazon Cognito resources in the Asia Pacific (Seoul) Amazon Web Services Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) .

Shorthand Syntax:

```
SmsAuthenticationMessage=string,SmsConfiguration={SnsCallerArn=string,ExternalId=string,SnsRegion=string}
```

JSON Syntax:

```
{
  "SmsAuthenticationMessage": "string",
  "SmsConfiguration": {
    "SnsCallerArn": "string",
    "ExternalId": "string",
    "SnsRegion": "string"
  }
}
```

`--software-token-mfa-configuration` (structure)

Configures a user pool for time-based one-time password (TOTP) MFA. Enables or disables TOTP.

Enabled -> (boolean)

The activation state of TOTP MFA.

Shorthand Syntax:

```
Enabled=boolean
```

JSON Syntax:

```
{
  "Enabled": true|false
}
```

`--email-mfa-configuration` (structure)

Sets configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

Message -> (string)

The template for the email messages that your user pool sends to users with codes for MFA and sign-in with email OTPs. The message must contain the `{####}` placeholder. In the message, Amazon Cognito replaces this placeholder with the code. If you donât provide this parameter, Amazon Cognito sends messages in the default format.

Subject -> (string)

The subject of the email messages that your user pool sends to users with codes for MFA and email OTP sign-in.

Shorthand Syntax:

```
Message=string,Subject=string
```

JSON Syntax:

```
{
  "Message": "string",
  "Subject": "string"
}
```

`--mfa-configuration` (string)

Sets multi-factor authentication (MFA) to be on, off, or optional. When `ON` , all users must set up MFA before they can sign in. When `OPTIONAL` , your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL` .

When `MfaConfiguration` is `OPTIONAL` , managed login doesnât automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.

Possible values:

- `OFF`
- `ON`
- `OPTIONAL`

`--web-authn-configuration` (structure)

The configuration of your user pool for passkey, or WebAuthn, authentication and registration. You can set this configuration independent of the MFA configuration options in this operation.

RelyingPartyId -> (string)

Sets or displays the authentication domain, typically your user pool domain, that passkey providers must use as a relying party (RP) in their configuration.

Under the following conditions, the passkey relying party ID must be the fully-qualified domain name of your custom domain:

- The user pool is configured for passkey authentication.
- The user pool has a custom domain, whether or not it also has a prefix domain.
- Your application performs authentication with managed login or the classic hosted UI.

UserVerification -> (string)

When `required` , users can only register and sign in users with passkeys that are capable of [user verification](https://www.w3.org/TR/webauthn-2/#enum-userVerificationRequirement) . When `preferred` , your user pool doesnât require the use of authenticators with user verification but encourages it.

Shorthand Syntax:

```
RelyingPartyId=string,UserVerification=string
```

JSON Syntax:

```
{
  "RelyingPartyId": "string",
  "UserVerification": "required"|"preferred"
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

**To configure user pool MFA and WebAuthn**

The following `set-user-pool-mfa-config` example configures the requested user pool with optional MFA with all available MFA methods, and sets the WebAuthn configuration.

```
aws cognito-idp set-user-pool-mfa-config \
    --user-pool-id us-west-2_EXAMPLE \
    --sms-mfa-configuration "SmsAuthenticationMessage=\"Your OTP for MFA or sign-in: use {####}.\",SmsConfiguration={SnsCallerArn=arn:aws:iam::123456789012:role/service-role/test-SMS-Role,ExternalId=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,SnsRegion=us-west-2}" \
    --software-token-mfa-configuration Enabled=true \
    --email-mfa-configuration "Message=\"Your OTP for MFA or sign-in: use {####}\",Subject=\"OTP test\"" \
    --mfa-configuration OPTIONAL \
    --web-authn-configuration RelyingPartyId=auth.example.com,UserVerification=preferred
```

Output:

```
{
    "EmailMfaConfiguration": {
        "Message": "Your OTP for MFA or sign-in: use {####}",
        "Subject": "OTP test"
    },
    "MfaConfiguration": "OPTIONAL",
    "SmsMfaConfiguration": {
        "SmsAuthenticationMessage": "Your OTP for MFA or sign-in: use {####}.",
        "SmsConfiguration": {
            "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-SMS-Role",
            "SnsRegion": "us-west-2"
        }
    },
    "SoftwareTokenMfaConfiguration": {
        "Enabled": true
    },
    "WebAuthnConfiguration": {
        "RelyingPartyId": "auth.example.com",
        "UserVerification": "preferred"
    }
}
```

For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) and [Passkey sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey) in the *Amazon Cognito Developer Guide*.

## Output

SmsMfaConfiguration -> (structure)

Shows user pool SMS message configuration for MFA and sign-in with SMS-message OTPs. Includes the message template and the SMS message sending configuration for Amazon SNS.

SmsAuthenticationMessage -> (string)

The SMS authentication message that will be sent to users with the code they must sign in with. The message must contain the `{####}` placeholder. Your user pool replaces the placeholder with the MFA code. If this parameter isnât provided, your user pool sends a default message.

SmsConfiguration -> (structure)

User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account.

You can set `SmsConfiguration` in `CreateUserPool` and `UpdateUserPool` , or in `SetUserPoolMfaConfig` .

SnsCallerArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your Amazon Web Services account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a [spending limit](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html) .

ExternalId -> (string)

The external ID provides additional security for your IAM role. You can use an `ExternalId` with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an `ExternalId` , your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the `ExternalID` . If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the `ExternalId` .

For more information about the `ExternalId` of a role, see [How to use an external ID when granting access to your Amazon Web Services resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) .

SnsRegion -> (string)

The Amazon Web Services Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported **Legacy Amazon SNS alternate Region** .

Amazon Cognito resources in the Asia Pacific (Seoul) Amazon Web Services Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) .

SoftwareTokenMfaConfiguration -> (structure)

Shows user pool configuration for time-based one-time password (TOTP) MFA. Includes TOTP enabled or disabled state.

Enabled -> (boolean)

The activation state of TOTP MFA.

EmailMfaConfiguration -> (structure)

Shows configuration for user pool email message MFA and sign-in with one-time passwords (OTPs). Includes the subject and body of the email message template for sign-in and MFA messages. To activate this setting, your user pool must be in the [Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

Message -> (string)

The template for the email messages that your user pool sends to users with codes for MFA and sign-in with email OTPs. The message must contain the `{####}` placeholder. In the message, Amazon Cognito replaces this placeholder with the code. If you donât provide this parameter, Amazon Cognito sends messages in the default format.

Subject -> (string)

The subject of the email messages that your user pool sends to users with codes for MFA and email OTP sign-in.

MfaConfiguration -> (string)

Displays multi-factor authentication (MFA) as on, off, or optional. When `ON` , all users must set up MFA before they can sign in. When `OPTIONAL` , your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL` .

When `MfaConfiguration` is `OPTIONAL` , managed login doesnât automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.

WebAuthnConfiguration -> (structure)

The configuration of your user pool for passkey, or WebAuthn, sign-in with authenticators like biometric and security-key devices. Includes relying-party configuration and settings for user-verification requirements.

RelyingPartyId -> (string)

Sets or displays the authentication domain, typically your user pool domain, that passkey providers must use as a relying party (RP) in their configuration.

Under the following conditions, the passkey relying party ID must be the fully-qualified domain name of your custom domain:

- The user pool is configured for passkey authentication.
- The user pool has a custom domain, whether or not it also has a prefix domain.
- Your application performs authentication with managed login or the classic hosted UI.

UserVerification -> (string)

When `required` , users can only register and sign in users with passkeys that are capable of [user verification](https://www.w3.org/TR/webauthn-2/#enum-userVerificationRequirement) . When `preferred` , your user pool doesnât require the use of authenticators with user verification but encourages it.