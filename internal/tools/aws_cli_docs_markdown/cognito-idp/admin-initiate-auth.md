# admin-initiate-authÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# admin-initiate-auth

## Description

Starts sign-in for applications with a server-side component, for example a traditional web application. This operation specifies the authentication flow that youâd like to begin. The authentication flow that you specify must be supported in your app client configuration. For more information about authentication flows, see [Authentication flows](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html) .

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminInitiateAuth)

## Synopsis

```
admin-initiate-auth
--user-pool-id <value>
--client-id <value>
--auth-flow <value>
[--auth-parameters <value>]
[--client-metadata <value>]
[--analytics-metadata <value>]
[--context-data <value>]
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

`--user-pool-id` (string)

The ID of the user pool where the user wants to sign in.

`--client-id` (string)

The ID of the app client where the user wants to sign in.

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

ADMIN_USER_PASSWORD_AUTH

Server-side username-password authentication with the password sent directly in the request. For more information about client-side and server-side authentication, see [SDK authorization models](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html) .

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

The authentication parameters. These are inputs corresponding to the `AuthFlow` that youâre invoking. The required values depend on the value of `AuthFlow` for example:

- For `USER_AUTH` : `USERNAME` (required), `PREFERRED_CHALLENGE` . If you donât provide a value for `PREFERRED_CHALLENGE` , Amazon Cognito responds with the `AvailableChallenges` parameter that specifies the available sign-in methods.
- For `USER_SRP_AUTH` : `USERNAME` (required), `SRP_A` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY` .
- For `ADMIN_USER_PASSWORD_AUTH` : `USERNAME` (required), `PASSWORD` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY` .
- For `REFRESH_TOKEN_AUTH/REFRESH_TOKEN` : `REFRESH_TOKEN` (required), `SECRET_HASH` (required if the app client is configured with a client secret), `DEVICE_KEY` .
- For `CUSTOM_AUTH` : `USERNAME` (required), `SECRET_HASH` (if app client is configured with client secret), `DEVICE_KEY` . To start the authentication flow with password verification, include `ChallengeName: SRP_A` and `SRP_A: (The SRP_A Value)` .

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

You create custom workflows by assigning Lambda functions to user pool triggers. When you use the AdminInitiateAuth API action, Amazon Cognito invokes the Lambda functions that are specified for various triggers. The ClientMetadata value is passed as input to the functions for only the following triggers:

- Pre signup
- Pre authentication
- User migration

When Amazon Cognito invokes the functions for these triggers, it passes a JSON payload, which the function receives as input. This payload contains a `validationData` attribute, which provides the data that you assigned to the ClientMetadata parameter in your AdminInitiateAuth request. In your function code in Lambda, you can process the `validationData` value to enhance your workflow for your specific needs.

When you use the AdminInitiateAuth API action, Amazon Cognito also invokes the functions for the following triggers, but it doesnât provide the ClientMetadata value as input:

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

`--context-data` (structure)

Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.

For more information, see [Collecting data for threat protection in applications](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html) .

IpAddress -> (string)

The source IP address of your userâs device.

ServerName -> (string)

The name of your applicationâs service endpoint.

ServerPath -> (string)

The path of your applicationâs service endpoint.

HttpHeaders -> (list)

The HTTP headers from your userâs authentication request.

(structure)

The HTTP header in the `ContextData` parameter.

headerName -> (string)

The header name.

headerValue -> (string)

The header value.

EncodedData -> (string)

Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see [Adding user device and session data to API requests](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint) .

Shorthand Syntax:

```
IpAddress=string,ServerName=string,ServerPath=string,HttpHeaders=[{headerName=string,headerValue=string},{headerName=string,headerValue=string}],EncodedData=string
```

JSON Syntax:

```
{
  "IpAddress": "string",
  "ServerName": "string",
  "ServerPath": "string",
  "HttpHeaders": [
    {
      "headerName": "string",
      "headerValue": "string"
    }
    ...
  ],
  "EncodedData": "string"
}
```

`--session` (string)

The optional session ID from a `ConfirmSignUp` API request. You can sign in a user directly from the sign-up process with an `AuthFlow` of `USER_AUTH` and `AuthParameters` of `EMAIL_OTP` or `SMS_OTP` , depending on how your user pool sent the confirmation-code message.

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

**To sign in a user as an admin**

The following `admin-initiate-auth` example signs in the user [diego@example.com](mailto:diego%40example.com). This example also includes metadata for threat protection and ClientMetadata for Lambda triggers. The user is configured for TOTP MFA and receives a challenge to provide a code from their authenticator app before they can complete authentication.

```
aws cognito-idp admin-initiate-auth \
    --user-pool-id us-west-2_EXAMPLE \
    --client-id 1example23456789 \
    --auth-flow ADMIN_USER_PASSWORD_AUTH \
    --auth-parameters USERNAME=diego@example.com,PASSWORD="My@Example$Password3!",SECRET_HASH=ExampleEncodedClientIdSecretAndUsername= \
    --context-data="{\"EncodedData\":\"abc123example\",\"HttpHeaders\":[{\"headerName\":\"UserAgent\",\"headerValue\":\"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\"}],\"IpAddress\":\"192.0.2.1\",\"ServerName\":\"example.com\",\"ServerPath\":\"/login\"}" \
    --client-metadata="{\"MyExampleKey\": \"MyExampleValue\"}"
```

Output:

```
{
    "ChallengeName": "SOFTWARE_TOKEN_MFA",
    "Session": "AYABeExample...",
    "ChallengeParameters": {
        "FRIENDLY_DEVICE_NAME": "MyAuthenticatorApp",
        "USER_ID_FOR_SRP": "diego@example.com"
    }
}
```

For more information, see [Admin authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#amazon-cognito-user-pools-admin-authentication-flow) in the *Amazon Cognito Developer Guide*.

## Output

ChallengeName -> (string)

The name of the challenge that youâre responding to with this call. This is returned in the `AdminInitiateAuth` response if you must pass another challenge.

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

The session that must be passed to challenge-response requests. If an `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API request results in another authentication challenge, Amazon Cognito returns a session ID and the parameters of the next challenge. Pass this session ID in the `Session` parameter of `AdminRespondToAuthChallenge` .

ChallengeParameters -> (map)

The parameters of an authentication challenge. Amazon Cognito returns challenge parameters as a guide to the responses your user or application must provide for the returned `ChallengeName` . Calculate responses to the challenge parameters and pass them in the `ChallengeParameters` of `AdminRespondToAuthChallenge` .

All challenges require `USERNAME` and, when the app client has a client secret, `SECRET_HASH` .

In SRP challenges, Amazon Cognito returns the `username` attribute in `USER_ID_FOR_SRP` instead of any email address, preferred username, or phone number alias that you might have specified in your `AdminInitiateAuth` request. You must use the username and not an alias in the `ChallengeResponses` of your challenge response.

key -> (string)

value -> (string)

AuthenticationResult -> (structure)

The outcome of successful authentication. This is only returned if the user pool has no additional challenges to return. If Amazon Cognito returns another challenge, the response includes `ChallengeName` , `ChallengeParameters` , and `Session` so that your user can answer the challenge.

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