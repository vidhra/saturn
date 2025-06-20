# sign-upÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# sign-up

## Description

Registers a user with an app client and requests a user name, password, and user attributes in the user pool.

### Note

Amazon Cognito doesnât evaluate Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you canât use IAM credentials to authorize requests, and you canât grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) .

### Note

This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/) . Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.

If you have never used SMS text messages with Amazon Cognito or any other Amazon Web Services service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) * , you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide* .

You might receive a `LimitExceeded` exception in response to this request if you have exceeded a rate quota for email or SMS messages, and if your user pool automatically verifies email addresses or phone numbers. When you get this exception in the response, the user is successfully created and is in an `UNCONFIRMED` state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/SignUp)

## Synopsis

```
sign-up
--client-id <value>
[--secret-hash <value>]
--username <value>
[--password <value>]
[--user-attributes <value>]
[--validation-data <value>]
[--analytics-metadata <value>]
[--user-context-data <value>]
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

`--client-id` (string)

The ID of the app client where the user wants to sign up.

`--secret-hash` (string)

A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message. For more information about `SecretHash` , see [Computing secret hash values](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash) .

`--username` (string)

The username of the user that you want to sign up. The value of this parameter is typically a username, but can be any alias attribute in your user pool.

`--password` (string)

The userâs proposed password. The password must comply with the [password requirements](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html) of your user pool.

Users can sign up without a password when your user pool supports passwordless sign-in with email or SMS OTPs. To create a user with no password, omit this parameter or submit a blank value. You can only create a passwordless user when passwordless sign-in is available.

`--user-attributes` (list)

An array of name-value pairs representing user attributes.

For custom attributes, include a `custom:` prefix in the attribute name, for example `custom:department` .

(structure)

The name and value of a user attribute.

Name -> (string)

The name of the attribute.

Value -> (string)

The value of the attribute.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--validation-data` (list)

Temporary user attributes that contribute to the outcomes of your pre sign-up Lambda trigger. This set of key-value pairs are for custom validation of information that you collect from your users but donât need to retain.

Your Lambda function can analyze this additional data and act on it. Your function can automatically confirm and verify select users or perform external API operations like logging user attributes and validation data to Amazon CloudWatch Logs.

For more information about the pre sign-up Lambda trigger, see [Pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) .

(structure)

The name and value of a user attribute.

Name -> (string)

The name of the attribute.

Value -> (string)

The value of the attribute.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
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

`--client-metadata` (map)

A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers.

You create custom workflows by assigning Lambda functions to user pool triggers. When you use the SignUp API action, Amazon Cognito invokes any functions that are assigned to the following triggers: *pre sign-up* , *custom message* , and *post confirmation* . When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a `clientMetadata` attribute, which provides the data that you assigned to the ClientMetadata parameter in your SignUp request. In your function code in Lambda, you can process the `clientMetadata` value to enhance your workflow for your specific needs.

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

**To sign up a user**

This example signs up [jane@example.com](mailto:jane%40example.com).

Command:

```
aws cognito-idp sign-up --client-id 3n4b5urk1ft4fl3mg5e62d9ado --username jane@example.com --password PASSWORD --user-attributes Name="email",Value="jane@example.com" Name="name",Value="Jane"
```

Output:

```
{
  "UserConfirmed": false,
  "UserSub": "e04d60a6-45dc-441c-a40b-e25a787d4862"
}
```

## Output

UserConfirmed -> (boolean)

Indicates whether the user was automatically confirmed. You can auto-confirm users with a [pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) .

CodeDeliveryDetails -> (structure)

In user pools that automatically verify and confirm new users, Amazon Cognito sends users a message with a code or link that confirms ownership of the phone number or email address that they entered. The `CodeDeliveryDetails` object is information about the delivery destination for that link or code.

Destination -> (string)

The email address or phone number destination where Amazon Cognito sent the code.

DeliveryMedium -> (string)

The method that Amazon Cognito used to send the code.

AttributeName -> (string)

The name of the attribute that Amazon Cognito verifies with the code.

UserSub -> (string)

The unique identifier of the new user, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` .

Session -> (string)

A session Id that you can pass to `ConfirmSignUp` when you want to immediately sign in your user with the `USER_AUTH` flow after they complete sign-up.