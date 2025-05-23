# admin-respond-to-auth-challengeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-respond-to-auth-challenge.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-respond-to-auth-challenge.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# admin-respond-to-auth-challenge

## Description

Some API operations in a user pool generate a challenge, like a prompt for an MFA code, for device authentication that bypasses MFA, or for a custom authentication challenge. An `AdminRespondToAuthChallenge` API request provides the answer to that challenge, like a code or a secure remote password (SRP). The parameters of a response to an authentication challenge vary with the type of challenge.

For more information about custom authentication challenges, see [Custom authentication challenge Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html) .

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminRespondToAuthChallenge)

## Synopsis

```
admin-respond-to-auth-challenge
--user-pool-id <value>
--client-id <value>
--challenge-name <value>
[--challenge-responses <value>]
[--session <value>]
[--analytics-metadata <value>]
[--context-data <value>]
[--client-metadata <value>]
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

The ID of the user pool where you want to respond to an authentication challenge.

`--client-id` (string)

The ID of the app client where you initiated sign-in.

`--challenge-name` (string)

The name of the challenge that you are responding to.

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

Possible values:

- `SMS_MFA`
- `EMAIL_OTP`
- `SOFTWARE_TOKEN_MFA`
- `SELECT_MFA_TYPE`
- `MFA_SETUP`
- `PASSWORD_VERIFIER`
- `CUSTOM_CHALLENGE`
- `SELECT_CHALLENGE`
- `DEVICE_SRP_AUTH`
- `DEVICE_PASSWORD_VERIFIER`
- `ADMIN_NO_SRP_AUTH`
- `NEW_PASSWORD_REQUIRED`
- `SMS_OTP`
- `PASSWORD`
- `WEB_AUTHN`
- `PASSWORD_SRP`

`--challenge-responses` (map)

The responses to the challenge that you received in the previous request. Each challenge has its own required response parameters. The following examples are partial JSON request bodies that highlight challenge-response parameters.

### Warning

You must provide a SECRET_HASH parameter in all challenge responses to an app client that has a client secret. Include a `DEVICE_KEY` for device authentication.

SELECT_CHALLENGE

`"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "USERNAME": "[username]", "ANSWER": "[Challenge name]"}`

Available challenges are `PASSWORD` , `PASSWORD_SRP` , `EMAIL_OTP` , `SMS_OTP` , and `WEB_AUTHN` .

Complete authentication in the `SELECT_CHALLENGE` response for `PASSWORD` , `PASSWORD_SRP` , and `WEB_AUTHN` :

- `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "WEB_AUTHN", "USERNAME": "[username]", "CREDENTIAL": "[AuthenticationResponseJSON]"}`   See [AuthenticationResponseJSON](https://www.w3.org/TR/WebAuthn-3/#dictdef-authenticationresponsejson) .
- `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD", "USERNAME": "[username]", "PASSWORD": "[password]"}`
- `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "PASSWORD_SRP", "USERNAME": "[username]", "SRP_A": "[SRP_A]"}`

For `SMS_OTP` and `EMAIL_OTP` , respond with the username and answer. Your user pool will send a code for the user to submit in the next challenge response.

- `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "SMS_OTP", "USERNAME": "[username]"}`
- `"ChallengeName": "SELECT_CHALLENGE", "ChallengeResponses": { "ANSWER": "EMAIL_OTP", "USERNAME": "[username]"}`

SMS_OTP

`"ChallengeName": "SMS_OTP", "ChallengeResponses": {"SMS_OTP_CODE": "[code]", "USERNAME": "[username]"}`

EMAIL_OTP

`"ChallengeName": "EMAIL_OTP", "ChallengeResponses": {"EMAIL_OTP_CODE": "[code]", "USERNAME": "[username]"}`

SMS_MFA

`"ChallengeName": "SMS_MFA", "ChallengeResponses": {"SMS_MFA_CODE": "[code]", "USERNAME": "[username]"}`

PASSWORD_VERIFIER

This challenge response is part of the SRP flow. Amazon Cognito requires that your application respond to this challenge within a few seconds. When the response time exceeds this period, your user pool returns a `NotAuthorizedException` error.

`"ChallengeName": "PASSWORD_VERIFIER", "ChallengeResponses": {"PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}`

Add `"DEVICE_KEY"` when you sign in with a remembered device.

CUSTOM_CHALLENGE

`"ChallengeName": "CUSTOM_CHALLENGE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[challenge_answer]"}`

Add `"DEVICE_KEY"` when you sign in with a remembered device.

NEW_PASSWORD_REQUIRED

`"ChallengeName": "NEW_PASSWORD_REQUIRED", "ChallengeResponses": {"NEW_PASSWORD": "[new_password]", "USERNAME": "[username]"}`

To set any required attributes that `InitiateAuth` returned in an `requiredAttributes` parameter, add `"userAttributes.[attribute_name]": "[attribute_value]"` . This parameter can also set values for writable attributes that arenât required by your user pool.

### Note

In a `NEW_PASSWORD_REQUIRED` challenge response, you canât modify a required attribute that already has a value. In `AdminRespondToAuthChallenge` or `RespondToAuthChallenge` , set a value for any keys that Amazon Cognito returned in the `requiredAttributes` parameter, then use the `AdminUpdateUserAttributes` or `UpdateUserAttributes` API operation to modify the value of any additional attributes.

SOFTWARE_TOKEN_MFA

`"ChallengeName": "SOFTWARE_TOKEN_MFA", "ChallengeResponses": {"USERNAME": "[username]", "SOFTWARE_TOKEN_MFA_CODE": [authenticator_code]}`

DEVICE_SRP_AUTH

`"ChallengeName": "DEVICE_SRP_AUTH", "ChallengeResponses": {"USERNAME": "[username]", "DEVICE_KEY": "[device_key]", "SRP_A": "[srp_a]"}`

DEVICE_PASSWORD_VERIFIER

`"ChallengeName": "DEVICE_PASSWORD_VERIFIER", "ChallengeResponses": {"DEVICE_KEY": "[device_key]", "PASSWORD_CLAIM_SIGNATURE": "[claim_signature]", "PASSWORD_CLAIM_SECRET_BLOCK": "[secret_block]", "TIMESTAMP": [timestamp], "USERNAME": "[username]"}`

MFA_SETUP

`"ChallengeName": "MFA_SETUP", "ChallengeResponses": {"USERNAME": "[username]"}, "SESSION": "[Session ID from VerifySoftwareToken]"`

SELECT_MFA_TYPE

`"ChallengeName": "SELECT_MFA_TYPE", "ChallengeResponses": {"USERNAME": "[username]", "ANSWER": "[SMS_MFA or SOFTWARE_TOKEN_MFA]"}`

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

`--session` (string)

The session identifier that maintains the state of authentication requests and challenge responses. If an `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API request results in a determination that your application must pass another challenge, Amazon Cognito returns a session with other challenge parameters. Send this session identifier, unmodified, to the next `AdminRespondToAuthChallenge` request.

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

`--client-metadata` (map)

A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.

You create custom workflows by assigning Lambda functions to user pool triggers. When you use the AdminRespondToAuthChallenge API action, Amazon Cognito invokes any functions that you have assigned to the following triggers:

- Pre sign-up
- custom message
- Post authentication
- User migration
- Pre token generation
- Define auth challenge
- Create auth challenge
- Verify auth challenge response

When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a `clientMetadata` attribute that provides the data that you assigned to the ClientMetadata parameter in your AdminRespondToAuthChallenge request. In your function code in Lambda, you can process the `clientMetadata` value to enhance your workflow for your specific needs.

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

**To respond to an authentication challenge**

There are many ways to respond to different authentication challenges, depending on your authentication flow, user pool configuration, and user settings. The following `admin-respond-to-auth-challenge` example provides a TOTP MFA code for [diego@example.com](mailto:diego%40example.com) and completes sign-in. This user pool has device remembering turned on, so the authentication result also returns a new device key.

```
aws cognito-idp admin-respond-to-auth-challenge \
    --user-pool-id us-west-2_EXAMPLE \
    --client-id 1example23456789 \
    --challenge-name SOFTWARE_TOKEN_MFA \
    --challenge-responses USERNAME=diego@example.com,SOFTWARE_TOKEN_MFA_CODE=000000 \
    --session AYABeExample...
```

Output:

```
{
    "ChallengeParameters": {},
    "AuthenticationResult": {
        "AccessToken": "eyJra456defEXAMPLE",
        "ExpiresIn": 3600,
        "TokenType": "Bearer",
        "RefreshToken": "eyJra123abcEXAMPLE",
        "IdToken": "eyJra789ghiEXAMPLE",
        "NewDeviceMetadata": {
            "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "DeviceGroupKey": "-ExAmPlE1"
        }
    }
}
```

For more information, see [Admin authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#amazon-cognito-user-pools-admin-authentication-flow) in the *Amazon Cognito Developer Guide*.

## Output

ChallengeName -> (string)

The name of the next challenge that you must respond to.

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

The session identifier that maintains the state of authentication requests and challenge responses. If an `AdminInitiateAuth` or `AdminRespondToAuthChallenge` API request results in a determination that your application must pass another challenge, Amazon Cognito returns a session with other challenge parameters. Send this session identifier, unmodified, to the next `AdminRespondToAuthChallenge` request.

ChallengeParameters -> (map)

The parameters that define your response to the next challenge.

key -> (string)

value -> (string)

AuthenticationResult -> (structure)

The outcome of a successful authentication process. After your application has passed all challenges, Amazon Cognito returns an `AuthenticationResult` with the JSON web tokens (JWTs) that indicate successful sign-in.

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