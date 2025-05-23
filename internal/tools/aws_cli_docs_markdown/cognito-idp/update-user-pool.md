# update-user-poolÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# update-user-pool

## Description

Updates the configuration of a user pool. To avoid setting parameters to Amazon Cognito defaults, construct this API request to pass the existing configuration of your user pool, modified to include the changes that you want to make.

### Warning

If you donât provide a value for an attribute, Amazon Cognito sets it to its default value.

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateUserPool)

## Synopsis

```
update-user-pool
--user-pool-id <value>
[--policies <value>]
[--deletion-protection <value>]
[--lambda-config <value>]
[--auto-verified-attributes <value>]
[--sms-verification-message <value>]
[--email-verification-message <value>]
[--email-verification-subject <value>]
[--verification-message-template <value>]
[--sms-authentication-message <value>]
[--user-attribute-update-settings <value>]
[--mfa-configuration <value>]
[--device-configuration <value>]
[--email-configuration <value>]
[--sms-configuration <value>]
[--user-pool-tags <value>]
[--admin-create-user-config <value>]
[--user-pool-add-ons <value>]
[--account-recovery-setting <value>]
[--pool-name <value>]
[--user-pool-tier <value>]
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

The ID of the user pool you want to update.

`--policies` (structure)

The password policy and sign-in policy in the user pool. The password policy sets options like password complexity requirements and password history. The sign-in policy sets the options available to applications in [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice) .

PasswordPolicy -> (structure)

The password policy settings for a user pool, including complexity, history, and length requirements.

MinimumLength -> (integer)

The minimum length of the password in the policy that you have set. This value canât be less than 6.

RequireUppercase -> (boolean)

The requirement in a password policy that users must include at least one uppercase letter in their password.

RequireLowercase -> (boolean)

The requirement in a password policy that users must include at least one lowercase letter in their password.

RequireNumbers -> (boolean)

The requirement in a password policy that users must include at least one number in their password.

RequireSymbols -> (boolean)

The requirement in a password policy that users must include at least one symbol in their password.

PasswordHistorySize -> (integer)

The number of previous passwords that you want Amazon Cognito to restrict each user from reusing. Users canât set a password that matches any of `n` previous passwords, where `n` is the value of `PasswordHistorySize` .

TemporaryPasswordValidityDays -> (integer)

The number of days a temporary password is valid in the password policy. If the user doesnât sign in during this time, an administrator must reset their password. Defaults to `7` . If you submit a value of `0` , Amazon Cognito treats it as a null value and sets `TemporaryPasswordValidityDays` to its default value.

### Note

When you set `TemporaryPasswordValidityDays` for a user pool, you can no longer set a value for the legacy `UnusedAccountValidityDays` parameter in that user pool.

SignInPolicy -> (structure)

The policy for allowed types of authentication in a user pool.

AllowedFirstAuthFactors -> (list)

The sign-in methods that a user pool supports as the first factor. You can permit users to start authentication with a standard username and password, or with other one-time password and hardware factors.

(string)

Shorthand Syntax:

```
PasswordPolicy={MinimumLength=integer,RequireUppercase=boolean,RequireLowercase=boolean,RequireNumbers=boolean,RequireSymbols=boolean,PasswordHistorySize=integer,TemporaryPasswordValidityDays=integer},SignInPolicy={AllowedFirstAuthFactors=[string,string]}
```

JSON Syntax:

```
{
  "PasswordPolicy": {
    "MinimumLength": integer,
    "RequireUppercase": true|false,
    "RequireLowercase": true|false,
    "RequireNumbers": true|false,
    "RequireSymbols": true|false,
    "PasswordHistorySize": integer,
    "TemporaryPasswordValidityDays": integer
  },
  "SignInPolicy": {
    "AllowedFirstAuthFactors": ["PASSWORD"|"EMAIL_OTP"|"SMS_OTP"|"WEB_AUTHN", ...]
  }
}
```

`--deletion-protection` (string)

When active, `DeletionProtection` prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.

When you try to delete a protected user pool in a `DeleteUserPool` API request, Amazon Cognito returns an `InvalidParameterException` error. To delete a protected user pool, send a new `DeleteUserPool` request after you deactivate deletion protection in an `UpdateUserPool` API request.

Possible values:

- `ACTIVE`
- `INACTIVE`

`--lambda-config` (structure)

A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.

PreSignUp -> (string)

The configuration of a [pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) in a user pool. This trigger evaluates new users and can bypass confirmation, [link a federated user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html) , or block sign-up requests.

CustomMessage -> (string)

A custom message Lambda trigger. This trigger is an opportunity to customize all SMS and email messages from your user pool. When a custom message trigger is active, your user pool routes all messages to a Lambda function that returns a runtime-customized message subject and body for your user pool to deliver to a user.

PostConfirmation -> (string)

The configuration of a [post confirmation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html) in a user pool. This trigger can take custom actions after a user confirms their user account and their email address or phone number.

PreAuthentication -> (string)

The configuration of a [pre authentication trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html) in a user pool. This trigger can evaluate and modify user sign-in events.

PostAuthentication -> (string)

The configuration of a [post authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html) in a user pool. This trigger can take custom actions after a user signs in.

DefineAuthChallenge -> (string)

The configuration of a define auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

CreateAuthChallenge -> (string)

The configuration of a create auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

VerifyAuthChallengeResponse -> (string)

The configuration of a verify auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

PreTokenGeneration -> (string)

The legacy configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool.

Set this parameter for legacy purposes. If you also set an ARN in `PreTokenGenerationConfig` , its value must be identical to `PreTokenGeneration` . For new instances of pre token generation triggers, set the `LambdaArn` of `PreTokenGenerationConfig` .

UserMigration -> (string)

The configuration of a [migrate user Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) in a user pool. This trigger can create user profiles when users sign in or attempt to reset their password with credentials that donât exist yet.

PreTokenGenerationConfig -> (structure)

The detailed configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool. If you also set an ARN in `PreTokenGeneration` , its value must be identical to `PreTokenGenerationConfig` .

LambdaVersion -> (string)

The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.

LambdaArn -> (string)

The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.

This parameter and the `PreTokenGeneration` property of `LambdaConfig` have the same value. For new instances of pre token generation triggers, set `LambdaArn` .

CustomSMSSender -> (structure)

The configuration of a custom SMS sender Lambda trigger. This trigger routes all SMS notifications from a user pool to a Lambda function that delivers the message using custom logic.

LambdaVersion -> (string)

The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.

You must use a `LambdaVersion` of `V1_0` with a custom sender function.

LambdaArn -> (string)

The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.

CustomEmailSender -> (structure)

The configuration of a custom email sender Lambda trigger. This trigger routes all email notifications from a user pool to a Lambda function that delivers the message using custom logic.

LambdaVersion -> (string)

The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.

You must use a `LambdaVersion` of `V1_0` with a custom sender function.

LambdaArn -> (string)

The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.

KMSKeyID -> (string)

The ARN of an [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) . Amazon Cognito uses the key to encrypt codes and temporary passwords sent to custom sender Lambda triggers.

Shorthand Syntax:

```
PreSignUp=string,CustomMessage=string,PostConfirmation=string,PreAuthentication=string,PostAuthentication=string,DefineAuthChallenge=string,CreateAuthChallenge=string,VerifyAuthChallengeResponse=string,PreTokenGeneration=string,UserMigration=string,PreTokenGenerationConfig={LambdaVersion=string,LambdaArn=string},CustomSMSSender={LambdaVersion=string,LambdaArn=string},CustomEmailSender={LambdaVersion=string,LambdaArn=string},KMSKeyID=string
```

JSON Syntax:

```
{
  "PreSignUp": "string",
  "CustomMessage": "string",
  "PostConfirmation": "string",
  "PreAuthentication": "string",
  "PostAuthentication": "string",
  "DefineAuthChallenge": "string",
  "CreateAuthChallenge": "string",
  "VerifyAuthChallengeResponse": "string",
  "PreTokenGeneration": "string",
  "UserMigration": "string",
  "PreTokenGenerationConfig": {
    "LambdaVersion": "V1_0"|"V2_0"|"V3_0",
    "LambdaArn": "string"
  },
  "CustomSMSSender": {
    "LambdaVersion": "V1_0",
    "LambdaArn": "string"
  },
  "CustomEmailSender": {
    "LambdaVersion": "V1_0",
    "LambdaArn": "string"
  },
  "KMSKeyID": "string"
}
```

`--auto-verified-attributes` (list)

The attributes that you want your user pool to automatically verify. Possible values: **email** , **phone_number** . For more information see [Verifying contact information at sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#allowing-users-to-sign-up-and-confirm-themselves) .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  phone_number
  email
```

`--sms-verification-message` (string)

This parameter is no longer used.

`--email-verification-message` (string)

This parameter is no longer used.

`--email-verification-subject` (string)

This parameter is no longer used.

`--verification-message-template` (structure)

The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.

Set the email message type that corresponds to your `DefaultEmailOption` selection. For `CONFIRM_WITH_LINK` , specify an `EmailMessageByLink` and leave `EmailMessage` blank. For `CONFIRM_WITH_CODE` , specify an `EmailMessage` and leave `EmailMessageByLink` blank. When you supply both parameters with either choice, Amazon Cognito returns an error.

SmsMessage -> (string)

The template for SMS messages that Amazon Cognito sends to your users.

EmailMessage -> (string)

The template for email messages that Amazon Cognito sends to your users. You can set an `EmailMessage` template only if the value of [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` . When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` , your user pool sends email messages with your own Amazon SES configuration.

EmailSubject -> (string)

The subject line for the email message template. You can set an `EmailSubject` template only if the value of [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` . When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` , your user pool sends email messages with your own Amazon SES configuration.

EmailMessageByLink -> (string)

The email message template for sending a confirmation link to the user. You can set an `EmailMessageByLink` template only if the value of [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` . When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` , your user pool sends email messages with your own Amazon SES configuration.

EmailSubjectByLink -> (string)

The subject line for the email message template for sending a confirmation link to the user. You can set an `EmailSubjectByLink` template only if the value of [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` . When your [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is `DEVELOPER` , your user pool sends email messages with your own Amazon SES configuration.

DefaultEmailOption -> (string)

The configuration of verification emails to contain a clickable link or a verification code.

For link, your template body must contain link text in the format `{##Click here##}` . âClick hereâ in the example is a customizable string. For code, your template body must contain a code placeholder in the format `{####}` .

Shorthand Syntax:

```
SmsMessage=string,EmailMessage=string,EmailSubject=string,EmailMessageByLink=string,EmailSubjectByLink=string,DefaultEmailOption=string
```

JSON Syntax:

```
{
  "SmsMessage": "string",
  "EmailMessage": "string",
  "EmailSubject": "string",
  "EmailMessageByLink": "string",
  "EmailSubjectByLink": "string",
  "DefaultEmailOption": "CONFIRM_WITH_LINK"|"CONFIRM_WITH_CODE"
}
```

`--sms-authentication-message` (string)

The contents of the SMS message that your user pool sends to users in SMS authentication.

`--user-attribute-update-settings` (structure)

The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate` , a user-pool setting that tells Amazon Cognito how to handle changes to the value of your usersâ email address and phone number attributes. For more information, see [Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates) .

AttributesRequireVerificationBeforeUpdate -> (list)

Requires that your user verifies their email address, phone number, or both before Amazon Cognito updates the value of that attribute. When you update a user attribute that has this option activated, Amazon Cognito sends a verification message to the new phone number or email address. Amazon Cognito doesnât change the value of the attribute until your user responds to the verification message and confirms the new value.

When `AttributesRequireVerificationBeforeUpdate` is false, your user pool doesnât require that your users verify attribute changes before Amazon Cognito updates them. In a user pool where `AttributesRequireVerificationBeforeUpdate` is false, API operations that change attribute values can immediately update a userâs `email` or `phone_number` attribute.

(string)

Shorthand Syntax:

```
AttributesRequireVerificationBeforeUpdate=string,string
```

JSON Syntax:

```
{
  "AttributesRequireVerificationBeforeUpdate": ["phone_number"|"email", ...]
}
```

`--mfa-configuration` (string)

Sets multi-factor authentication (MFA) to be on, off, or optional. When `ON` , all users must set up MFA before they can sign in. When `OPTIONAL` , your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL` .

When `MfaConfiguration` is `OPTIONAL` , managed login doesnât automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.

Possible values:

- `OFF`
- `ON`
- `OPTIONAL`

`--device-configuration` (structure)

The device-remembering configuration for a user pool. Device remembering or device tracking is a âRemember me on this deviceâ option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) . A null value indicates that you have deactivated device remembering in your user pool.

### Note

When you provide a value for any `DeviceConfiguration` field, you activate the Amazon Cognito device-remembering feature. For more information, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) .

ChallengeRequiredOnNewDevice -> (boolean)

When true, a remembered device can sign in with device authentication instead of SMS and time-based one-time password (TOTP) factors for multi-factor authentication (MFA).

### Note

Whether or not `ChallengeRequiredOnNewDevice` is true, users who sign in with devices that have not been confirmed or remembered must still provide a second factor in a user pool that requires MFA.

DeviceOnlyRememberedOnUserPrompt -> (boolean)

When true, Amazon Cognito doesnât automatically remember a userâs device when your app sends a `ConfirmDevice` API request. In your app, create a prompt for your user to choose whether they want to remember their device. Return the userâs choice in an `UpdateDeviceStatus` API request.

When `DeviceOnlyRememberedOnUserPrompt` is `false` , Amazon Cognito immediately remembers devices that you register in a `ConfirmDevice` API request.

Shorthand Syntax:

```
ChallengeRequiredOnNewDevice=boolean,DeviceOnlyRememberedOnUserPrompt=boolean
```

JSON Syntax:

```
{
  "ChallengeRequiredOnNewDevice": true|false,
  "DeviceOnlyRememberedOnUserPrompt": true|false
}
```

`--email-configuration` (structure)

The email configuration of your user pool. The email configuration type sets your preferred sending method, Amazon Web Services Region, and sender for email invitation and verification messages from your user pool.

SourceArn -> (string)

The ARN of a verified email address or an address from a verified domain in Amazon SES. You can set a `SourceArn` email from a verified domain only with an API request. You can set a verified email address, but not an address in a verified domain, in the Amazon Cognito console. Amazon Cognito uses the email address that you provide in one of the following ways, depending on the value that you specify for the `EmailSendingAccount` parameter:

- If you specify `COGNITO_DEFAULT` , Amazon Cognito uses this address as the custom FROM address when it emails your users using its built-in email account.
- If you specify `DEVELOPER` , Amazon Cognito emails your users with this address by calling Amazon SES on your behalf.

The Region value of the `SourceArn` parameter must indicate a supported Amazon Web Services Region of your user pool. Typically, the Region in the `SourceArn` and the user pool Region are the same. For more information, see [Amazon SES email configuration regions](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-email.html#user-pool-email-developer-region-mapping) in the [Amazon Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) .

ReplyToEmailAddress -> (string)

The destination to which the receiver of the email should reply.

EmailSendingAccount -> (string)

Specifies whether Amazon Cognito uses its built-in functionality to send your users email messages, or uses your Amazon Simple Email Service email configuration. Specify one of the following values:

COGNITO_DEFAULT

When Amazon Cognito emails your users, it uses its built-in email functionality. When you use the default option, Amazon Cognito allows only a limited number of emails each day for your user pool. For typical production environments, the default email limit is less than the required delivery volume. To achieve a higher delivery volume, specify DEVELOPER to use your Amazon SES email configuration.

To look up the email delivery limit for the default option, see [Limits](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html) in the *Amazon Cognito Developer Guide* .

The default FROM address is `no-reply@verificationemail.com` . To customize the FROM address, provide the Amazon Resource Name (ARN) of an Amazon SES verified email address for the `SourceArn` parameter.

DEVELOPER

When Amazon Cognito emails your users, it uses your Amazon SES configuration. Amazon Cognito calls Amazon SES on your behalf to send email from your verified email address. When you use this option, the email delivery limits are the same limits that apply to your Amazon SES verified email address in your Amazon Web Services account.

If you use this option, provide the ARN of an Amazon SES verified email address for the `SourceArn` parameter.

Before Amazon Cognito can email your users, it requires additional permissions to call Amazon SES on your behalf. When you update your user pool with this option, Amazon Cognito creates a *service-linked role* , which is a type of role in your Amazon Web Services account. This role contains the permissions that allow you to access Amazon SES and send email messages from your email address. For more information about the service-linked role that Amazon Cognito creates, see [Using Service-Linked Roles for Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/using-service-linked-roles.html) in the *Amazon Cognito Developer Guide* .

From -> (string)

Either the senderâs email address or the senderâs name with their email address. For example, `testuser@example.com` or `Test User <testuser@example.com>` . This address appears before the body of the email.

ConfigurationSet -> (string)

The set of configuration rules that can be applied to emails sent using Amazon Simple Email Service. A configuration set is applied to an email by including a reference to the configuration set in the headers of the email. Once applied, all of the rules in that configuration set are applied to the email. Configuration sets can be used to apply the following types of rules to emails:

Event publishing

Amazon Simple Email Service can track the number of send, delivery, open, click, bounce, and complaint events for each email sent. Use event publishing to send information about these events to other Amazon Web Services services such as and Amazon CloudWatch

IP pool management

When leasing dedicated IP addresses with Amazon Simple Email Service, you can create groups of IP addresses, called dedicated IP pools. You can then associate the dedicated IP pools with configuration sets.

Shorthand Syntax:

```
SourceArn=string,ReplyToEmailAddress=string,EmailSendingAccount=string,From=string,ConfigurationSet=string
```

JSON Syntax:

```
{
  "SourceArn": "string",
  "ReplyToEmailAddress": "string",
  "EmailSendingAccount": "COGNITO_DEFAULT"|"DEVELOPER",
  "From": "string",
  "ConfigurationSet": "string"
}
```

`--sms-configuration` (structure)

The SMS configuration with the settings for your Amazon Cognito user pool to send SMS message with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account. For more information see [SMS message settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) .

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
SnsCallerArn=string,ExternalId=string,SnsRegion=string
```

JSON Syntax:

```
{
  "SnsCallerArn": "string",
  "ExternalId": "string",
  "SnsRegion": "string"
}
```

`--user-pool-tags` (map)

The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.

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

`--admin-create-user-config` (structure)

The configuration for administrative creation of users. Includes the template for the invitation message for new users, the duration of temporary passwords, and permitting self-service sign-up.

AllowAdminCreateUserOnly -> (boolean)

The setting for allowing self-service sign-up. When `true` , only administrators can create new user profiles. When `false` , users can register themselves and create a new user profile with the `SignUp` operation.

UnusedAccountValidityDays -> (integer)

This parameter is no longer in use.

The password expiration limit in days for administrator-created users. When this time expires, the user canât sign in with their temporary password. To reset the account after that time limit, you must call `AdminCreateUser` again, specifying `RESEND` for the `MessageAction` parameter.

The default value for this parameter is 7.

InviteMessageTemplate -> (structure)

The template for the welcome message to new users. This template must include the `{####}` temporary password placeholder if you are creating users with passwords. If your users donât have passwords, you can omit the placeholder.

See also [Customizing User Invitation Messages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization) .

SMSMessage -> (string)

The message template for SMS messages.

EmailMessage -> (string)

The message template for email messages. EmailMessage is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.

EmailSubject -> (string)

The subject line for email messages. EmailSubject is allowed only if [EmailSendingAccount](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount) is DEVELOPER.

Shorthand Syntax:

```
AllowAdminCreateUserOnly=boolean,UnusedAccountValidityDays=integer,InviteMessageTemplate={SMSMessage=string,EmailMessage=string,EmailSubject=string}
```

JSON Syntax:

```
{
  "AllowAdminCreateUserOnly": true|false,
  "UnusedAccountValidityDays": integer,
  "InviteMessageTemplate": {
    "SMSMessage": "string",
    "EmailMessage": "string",
    "EmailSubject": "string"
  }
}
```

`--user-pool-add-ons` (structure)

Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to `AUDIT` . To configure automatic security responses to potentially unwanted traffic to your user pool, set to `ENFORCED` .

For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html) . To activate this setting, your user pool must be on the [Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html) .

AdvancedSecurityMode -> (string)

The operating mode of threat protection for standard authentication types in your user pool, including username-password and secure remote password (SRP) authentication.

AdvancedSecurityAdditionalFlows -> (structure)

Threat protection configuration options for additional authentication types in your user pool, including custom authentication.

CustomAuthMode -> (string)

The operating mode of threat protection in custom authentication with [Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

Shorthand Syntax:

```
AdvancedSecurityMode=string,AdvancedSecurityAdditionalFlows={CustomAuthMode=string}
```

JSON Syntax:

```
{
  "AdvancedSecurityMode": "OFF"|"AUDIT"|"ENFORCED",
  "AdvancedSecurityAdditionalFlows": {
    "CustomAuthMode": "AUDIT"|"ENFORCED"
  }
}
```

`--account-recovery-setting` (structure)

The available verified method a user can use to recover their password when they call `ForgotPassword` . You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesnât qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.

RecoveryMechanisms -> (list)

The list of options and priorities for user message delivery in forgot-password operations. Sets or displays user pool preferences for email or SMS message priority, whether users should fall back to a second delivery method, and whether passwords should only be reset by administrators.

(structure)

A recovery option for a user. The `AccountRecoverySettingType` data type is an array of this object. Each `RecoveryOptionType` has a priority property that determines whether it is a primary or secondary option.

For example, if `verified_email` has a priority of `1` and `verified_phone_number` has a priority of `2` , your user pool sends account-recovery messages to a verified email address but falls back to an SMS message if the user has a verified phone number. The `admin_only` option prevents self-service account recovery.

Priority -> (integer)

Your priority preference for using the specified attribute in account recovery. The highest priority is `1` .

Name -> (string)

The recovery method that this object sets a recovery option for.

Shorthand Syntax:

```
RecoveryMechanisms=[{Priority=integer,Name=string},{Priority=integer,Name=string}]
```

JSON Syntax:

```
{
  "RecoveryMechanisms": [
    {
      "Priority": integer,
      "Name": "verified_email"|"verified_phone_number"|"admin_only"
    }
    ...
  ]
}
```

`--pool-name` (string)

The updated name of your user pool.

`--user-pool-tier` (string)

The user pool [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html) , or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to `ESSENTIALS` .

Possible values:

- `LITE`
- `ESSENTIALS`
- `PLUS`

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

**To update a user pool**

The following `update-user-pool` example modifies a user pool with example syntax for each of the available configuration options. To update a user pool, you must specify all previously-configured options or they will reset to a default value.

```
aws cognito-idp update-user-pool --user-pool-id us-west-2_EXAMPLE \
    --policies PasswordPolicy=\{MinimumLength=6,RequireUppercase=true,RequireLowercase=true,RequireNumbers=true,RequireSymbols=true,TemporaryPasswordValidityDays=7\} \
    --deletion-protection ACTIVE \
    --lambda-config PreSignUp="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-presignup-function",PreTokenGeneration="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-pretoken-function" \
    --auto-verified-attributes "phone_number" "email" \
    --verification-message-template \{\"SmsMessage\":\""Your code is {####}"\",\"EmailMessage\":\""Your code is {####}"\",\"EmailSubject\":\""Your verification code"\",\"EmailMessageByLink\":\""Click {##here##} to verify your email address."\",\"EmailSubjectByLink\":\""Your verification link"\",\"DefaultEmailOption\":\"CONFIRM_WITH_LINK\"\} \
    --sms-authentication-message "Your code is {####}" \
    --user-attribute-update-settings AttributesRequireVerificationBeforeUpdate="email","phone_number" \
    --mfa-configuration "OPTIONAL" \
    --device-configuration ChallengeRequiredOnNewDevice=true,DeviceOnlyRememberedOnUserPrompt=true \
    --email-configuration SourceArn="arn:aws:ses:us-west-2:123456789012:identity/admin@example.com",ReplyToEmailAddress="amdin+noreply@example.com",EmailSendingAccount=DEVELOPER,From="admin@amazon.com",ConfigurationSet="test-configuration-set" \
    --sms-configuration SnsCallerArn="arn:aws:iam::123456789012:role/service-role/SNS-SMS-Role",ExternalId="12345",SnsRegion="us-west-2" \
    --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \
    --user-pool-tags "Function"="MyMobileGame","Developers"="Berlin" \
    --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \
    --user-pool-add-ons AdvancedSecurityMode="AUDIT" \
    --account-recovery-setting RecoveryMechanisms=\[\{Priority=1,Name="verified_email"\},\{Priority=2,Name="verified_phone_number"\}\]
```

This command produces no output.

For more information, see [Updating user pool configuration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-updating.html) in the *Amazon Cognito Developer Guide*.

## Output

None