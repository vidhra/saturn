# initiate-authÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/initiate-auth.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/initiate-auth.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# initiate-auth

## Description

Declares an authentication flow and initiates sign-in for a user in the Amazon Cognito user directory. Amazon Cognito might respond with an additional challenge or an `AuthenticationResult` that contains the outcome of a successful authentication. You canât sign in a user with a federated IdP with `InitiateAuth` . For more information, see [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html) .

### Note

Amazon Cognito doesnât evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you canât use IAM credentials to authorize requests, and you canât grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) .

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/InitiateAuth)

## Synopsis

```
initiate-auth
--auth-flow <value>
[--auth-parameters <value>]
[--client-metadata <value>]
--client-id <value>
[--analytics-metadata <value>]
[--user-context-data <value>]
[--session <value>]
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

`--auth-flow` (string)

The authentication flow that you want to initiate. Each `AuthFlow` has linked `AuthParameters` that you must submit. The following are some example flows.

USER_AUTH

The entry point for [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice) with passwords, one-time passwords, and WebAuthn authenticators. Request a preferred authentication type or review available authentication types. From the offered authentication types, select one in a challenge response and then authenticate with that method in an additional challenge response. To activate this setting, your user pool must be in the [Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.

USER_SRP_AUTH

Username-password authentication with the Secure Remote Password (SRP) protocol. For more information, see [Use SRP password verification in custom authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#Using-SRP-password-verification-in-custom-authentication-flow) .

REFRESH_TOKEN_AUTH and REFRESH_TOKEN

Receive new ID and access tokens when you pass a `REFRESH_TOKEN` parameter with a valid refresh token as the value. For more information, see [Using the refresh token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html) .

CUSTOM_AUTH

Custom authentication with Lambda triggers. For more information, see [Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

USER_PASSWORD_AUTH

Client-side username-password authentication with the password sent directly in the request. For more information about client-side and server-side authentication, see [SDK authorization models](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html) .

`ADMIN_USER_PASSWORD_AUTH` is a flow type of `AdminInitiateAuth` and isnât valid for InitiateAuth. `ADMIN_NO_SRP_AUTH` is a legacy server-side username-password flow and isnât valid for InitiateAuth.

Possible values:

- `USER_SRP_AUTH`
- `REFRESH_TOKEN_AUTH`
- `REFRESH_TOKEN`
- `CUSTOM_AUTH`
- `ADMIN_NO_SRP_AUTH`
- `USER_PASSWORD_AUTH`
- `ADMIN_USER_PASSWORD_AUTH`
- `USER_AUTH`

`--auth-parameters` (map)

The authentication parameters. These are inputs corresponding to the `AuthFlow` that youâre invoking.

The required values are specific to the  InitiateAuthRequest$AuthFlow .

The following are some authentication flows and their parameters. Add a `SECRET_HASH` parameter if your app client has a client secret.

- `USER_AUTH` : `USERNAME` (required), `PREFERRED_CHALLENGE` . If you donât provide a value for `PREFERRED_CHALLENGE` , Amazon Cognito responds with the `AvailableChallenges` parameter that specifies the available sign-in methods.
- `USER_SRP_AUTH` : `USERNAME` (required), `SRP_A` (required), `DEVICE_KEY` .
- `USER_PASSWORD_AUTH` : `USERNAME` (required), `PASSWORD` (required), `DEVICE_KEY` .
- `REFRESH_TOKEN_AUTH/REFRESH_TOKEN` : `REFRESH_TOKEN` (required), `DEVICE_KEY` .
- `CUSTOM_AUTH` : `USERNAME` (required), `SECRET_HASH` (if app client is configured with client secret), `DEVICE_KEY` . To start the authentication flow with password verification, include `ChallengeName: SRP_A` and `SRP_A: (The SRP_A Value)` .

For more information about `SECRET_HASH` , see [Computing secret hash values](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash) . For information about `DEVICE_KEY` , see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) .

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

`--client-metadata` (map)

A map of custom key-value pairs that you can provide as input for certain custom workflows that this action triggers.

You create custom workflows by assigning Lambda functions to user pool triggers. When you send an `InitiateAuth` request, Amazon Cognito invokes the Lambda functions that are specified for various triggers. The `ClientMetadata` value is passed as input to the functions for only the following triggers.

- Pre sign-up
- Pre authentication
- User migration

When Amazon Cognito invokes the functions for these triggers, it passes a JSON payload as input to the function. This payload contains a `validationData` attribute with the data that you assigned to the `ClientMetadata` parameter in your `InitiateAuth` request. In your function, `validationData` can contribute to operations that require data that isnât in the default payload.

`InitiateAuth` requests invokes the following triggers without `ClientMetadata` as input.

- Post authentication
- Custom message
- Pre token generation
- Create auth challenge
- Define auth challenge
- Custom email sender
- Custom SMS sender

For more information, see [Using Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html) in the *Amazon Cognito Developer Guide* .

### Note

When you use the `ClientMetadata` parameter, note that Amazon Cognito wonât do the following:

- Store the `ClientMetadata` value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesnât include triggers, the `ClientMetadata` parameter serves no purpose.
- Validate the `ClientMetadata` value.
- Encrypt the `ClientMetadata` value. Donât send sensitive information in this parameter.

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

`--client-id` (string)

The ID of the app client that your user wants to sign in to.

`--analytics-metadata` (structure)

Information that supports analytics outcomes with Amazon Pinpoint, including the userâs endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.

AnalyticsEndpointId -> (string)

The endpoint ID. Information that you want to pass to Amazon Pinpoint about where to send notifications.

Shorthand Syntax:

```
AnalyticsEndpointId=string
```

JSON Syntax:

```
{
  "AnalyticsEndpointId": "string"
}
```

`--user-context-data` (structure)

Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.

For more information, see [Collecting data for threat protection in applications](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html) .

IpAddress -> (string)

The source IP address of your userâs device.

EncodedData -> (string)

Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint) .

Shorthand Syntax:

```
IpAddress=string,EncodedData=string
```

JSON Syntax:

```
{
  "IpAddress": "string",
  "EncodedData": "string"
}
```

`--session` (string)

The optional session ID from a `ConfirmSignUp` API request. You can sign in a user directly from the sign-up process with the `USER_AUTH` authentication flow. When you pass the session ID to `InitiateAuth` , Amazon Cognito assumes the SMS or email message one-time verification password from `ConfirmSignUp` as the primary authentication factor. Youâre not required to submit this code a second time. This option is only valid for users who have confirmed their sign-up and are signing in for the first time within the authentication flow session duration of the session ID.

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

**To sign in a user**

The following `initiate-auth` example signs in a user with the basic username-password flow and no additional challenges.

```
aws cognito-idp initiate-auth \
    --auth-flow USER_PASSWORD_AUTH \
    --client-id 1example23456789 \
    --analytics-metadata AnalyticsEndpointId=d70b2ba36a8c4dc5a04a0451aEXAMPLE \
    --auth-parameters USERNAME=testuser,PASSWORD=[Password] --user-context-data EncodedData=mycontextdata --client-metadata MyTestKey=MyTestValue
```

Output:

```
{
    "AuthenticationResult": {
        "AccessToken": "eyJra456defEXAMPLE",
        "ExpiresIn": 3600,
        "TokenType": "Bearer",
        "RefreshToken": "eyJra123abcEXAMPLE",
        "IdToken": "eyJra789ghiEXAMPLE",
        "NewDeviceMetadata": {
            "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "DeviceGroupKey": "-v7w9UcY6"
        }
    }
}
```

For more information, see [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html) in the *Amazon Cognito Developer Guide*.

## Output

ChallengeName -> (string)

The name of an additional authentication challenge that you must respond to.

Possible challenges include the following:

### Note

All of the following challenges require `USERNAME` and, when the app client has a client secret, `SECRET_HASH` in the parameters.

- `WEB_AUTHN` : Respond to the challenge with the results of a successful authentication with a WebAuthn authenticator, or passkey. Examples of WebAuthn authenticators include biometric devices and security keys.
- `PASSWORD` : Respond with `USER_PASSWORD_AUTH` parameters: `USERNAME` (required), `PASSWORD` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY` .
- `PASSWORD_SRP` : Respond with `USER_SRP_AUTH` parameters: `USERNAME` (required), `SRP_A` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY` .
- `SELECT_CHALLENGE` : Respond to the challenge with `USERNAME` and an `ANSWER` that matches one of the challenge types in the `AvailableChallenges` response parameter.
- `SMS_MFA` : Respond with an `SMS_MFA_CODE` that your user pool delivered in an SMS message.
- `EMAIL_OTP` : Respond with an `EMAIL_OTP_CODE` that your user pool delivered in an email message.
- `PASSWORD_VERIFIER` : Respond with `PASSWORD_CLAIM_SIGNATURE` , `PASSWORD_CLAIM_SECRET_BLOCK` , and `TIMESTAMP` after client-side SRP calculations.
- `CUSTOM_CHALLENGE` : This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued. The parameters of the challenge are determined by your Lambda function.
- `DEVICE_SRP_AUTH` : Respond with the initial parameters of device SRP authentication. For more information, see [Signing in with a device](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device) .
- `DEVICE_PASSWORD_VERIFIER` : Respond with `PASSWORD_CLAIM_SIGNATURE` , `PASSWORD_CLAIM_SECRET_BLOCK` , and `TIMESTAMP` after client-side SRP calculations. For more information, see [Signing in with a device](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device) .
- `NEW_PASSWORD_REQUIRED` : For users who are required to change their passwords after successful first login. Respond to this challenge with `NEW_PASSWORD` and any required attributes that Amazon Cognito returned in the `requiredAttributes` parameter. You can also set values for attributes that arenât required by your user pool and that your app client can write. Amazon Cognito only returns this challenge for users who have temporary passwords. When you create passwordless users, you must provide values for all required attributes.

### Note

In a `NEW_PASSWORD_REQUIRED` challenge response, you canât modify a required attribute that already has a value. In `AdminRespondToAuthChallenge` or `RespondToAuthChallenge` , set a value for any keys that Amazon Cognito returned in the `requiredAttributes` parameter, then use the `AdminUpdateUserAttributes` or `UpdateUserAttributes` API operation to modify the value of any additional attributes.

- `MFA_SETUP` : For users who are required to setup an MFA factor before they can sign in. The MFA types activated for the user pool will be listed in the challenge parameters `MFAS_CAN_SETUP` value.  To set up time-based one-time password (TOTP) MFA, use the session returned in this challenge from `InitiateAuth` or `AdminInitiateAuth` as an input to `AssociateSoftwareToken` . Then, use the session returned by `VerifySoftwareToken` as an input to `RespondToAuthChallenge` or `AdminRespondToAuthChallenge` with challenge name `MFA_SETUP` to complete sign-in.  To set up SMS or email MFA, collect a `phone_number` or `email` attribute for the user. Then restart the authentication flow with an `InitiateAuth` or `AdminInitiateAuth` request.

Session -> (string)

The session identifier that links a challenge response to the initial authentication request. If the user must pass another challenge, Amazon Cognito returns a session ID and challenge parameters.

ChallengeParameters -> (map)

The required parameters of the `ChallengeName` challenge.

All challenges require `USERNAME` . They also require `SECRET_HASH` if your app client has a client secret.

key -> (string)

value -> (string)

AuthenticationResult -> (structure)

The result of a successful and complete authentication request. This result is only returned if the user doesnât need to pass another challenge. If they must pass another challenge before they get tokens, Amazon Cognito returns a challenge in `ChallengeName` , `ChallengeParameters` , and `Session` response parameters.

AccessToken -> (string)

Your userâs access token.

ExpiresIn -> (integer)

The expiration period of the authentication result in seconds.

TokenType -> (string)

The intended use of the token, for example `Bearer` .

RefreshToken -> (string)

Your userâs refresh token.

IdToken -> (string)

Your userâs ID token.

NewDeviceMetadata -> (structure)

The new device metadata from an authentication result.

DeviceKey -> (string)

The device key, an identifier used in generating the `DEVICE_PASSWORD_VERIFIER` for device SRP authentication.

DeviceGroupKey -> (string)

The device group key, an identifier used in generating the `DEVICE_PASSWORD_VERIFIER` for device SRP authentication.

AvailableChallenges -> (list)

This response parameter lists the available authentication challenges that users can select from in [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice) . For example, they might be able to choose between passkey authentication, a one-time password from an SMS message, and a traditional password.

(string)