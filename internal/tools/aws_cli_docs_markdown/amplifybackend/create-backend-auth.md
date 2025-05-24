# create-backend-authÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-auth.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/create-backend-auth.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplifybackend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifybackend/index.html#cli-aws-amplifybackend) ]

# create-backend-auth

## Description

Creates a new backend authentication resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplifybackend-2020-08-11/CreateBackendAuth)

## Synopsis

```
create-backend-auth
--app-id <value>
--backend-environment-name <value>
--resource-config <value>
--resource-name <value>
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

`--app-id` (string)

The app ID.

`--backend-environment-name` (string)

The name of the backend environment.

`--resource-config` (structure)

The resource configuration for this request object.

AuthResources -> (string)

Defines whether you want to configure only authentication or both authentication and authorization settings.

IdentityPoolConfigs -> (structure)

Describes the authorization configuration for the Amazon Cognito identity pool, provisioned as a part of your auth resource in the Amplify project.

IdentityPoolName -> (string)

Name of the Amazon Cognito identity pool used for authorization.

UnauthenticatedLogin -> (boolean)

Set to true or false based on whether you want to enable guest authorization to your Amplify app.

Service -> (string)

Defines the service name to use when configuring an authentication resource in your Amplify project.

UserPoolConfigs -> (structure)

Describes authentication configuration for the Amazon Cognito user pool, provisioned as a part of your auth resource in the Amplify project.

ForgotPassword -> (structure)

**(DEPRECATED)** Describes the forgotten password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.

DeliveryMethod -> (string)

**(DEPRECATED)** Describes which mode to use (either SMS or email) to deliver messages to app users who want to recover their password.

EmailSettings -> (structure)

**(DEPRECATED)** The configuration for the email sent when an app user forgets their password.

EmailMessage -> (string)

The contents of the email message.

EmailSubject -> (string)

The contents of the subject line of the email message.

SmsSettings -> (structure)

**(DEPRECATED)** The configuration for the SMS message sent when an app user forgets their password.

SmsMessage -> (string)

The contents of the SMS message.

Mfa -> (structure)

Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project.

MFAMode -> (string)

Describes whether MFA should be [ON, OFF, or OPTIONAL] for authentication in your Amplify project.

Settings -> (structure)

Describes the configuration settings and methods for your Amplify app users to use MFA.

MfaTypes -> (list)

The supported MFA types.

(string)

SmsMessage -> (string)

The body of the SMS message.

OAuth -> (structure)

Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project.

DomainPrefix -> (string)

The domain prefix for your Amplify app.

OAuthGrantType -> (string)

The OAuth grant type that you use to allow app users to authenticate from your Amplify app.

OAuthScopes -> (list)

List of OAuth-related flows used to allow your app users to authenticate from your Amplify app.

(string)

RedirectSignInURIs -> (list)

The redirected URI for signing in to your Amplify app.

(string)

RedirectSignOutURIs -> (list)

Redirect URLs that OAuth uses when a user signs out of an Amplify app.

(string)

SocialProviderSettings -> (structure)

The settings for using social providers to access your Amplify app.

Facebook -> (structure)

Describes third-party social federation configurations for allowing your app users to sign in using OAuth.

ClientId -> (string)

Describes the client_id, which can be obtained from the third-party social federation provider.

ClientSecret -> (string)

Describes the client_secret, which can be obtained from third-party social federation providers.

Google -> (structure)

Describes third-party social federation configurations for allowing your app users to sign in using OAuth.

ClientId -> (string)

Describes the client_id, which can be obtained from the third-party social federation provider.

ClientSecret -> (string)

Describes the client_secret, which can be obtained from third-party social federation providers.

LoginWithAmazon -> (structure)

Describes third-party social federation configurations for allowing your app users to sign in using OAuth.

ClientId -> (string)

Describes the client_id, which can be obtained from the third-party social federation provider.

ClientSecret -> (string)

Describes the client_secret, which can be obtained from third-party social federation providers.

SignInWithApple -> (structure)

Describes Apple social federation configurations for allowing your app users to sign in using OAuth.

ClientId -> (string)

Describes the client_id (also called Services ID) that comes from Apple.

KeyId -> (string)

Describes the key_id that comes from Apple.

PrivateKey -> (string)

Describes the private_key that comes from Apple.

TeamId -> (string)

Describes the team_id that comes from Apple.

PasswordPolicy -> (structure)

Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.

AdditionalConstraints -> (list)

Additional constraints for the password used to access the backend of your Amplify project.

(string)

MinimumLength -> (double)

The minimum length of the password used to access the backend of your Amplify project.

RequiredSignUpAttributes -> (list)

The required attributes to sign up new users in the user pool.

(string)

SignInMethod -> (string)

Describes the sign-in methods that your Amplify app users use to log in using the Amazon Cognito user pool, configured as a part of your Amplify project.

UserPoolName -> (string)

The Amazon Cognito user pool name.

VerificationMessage -> (structure)

Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project.

DeliveryMethod -> (string)

The type of verification message to send.

EmailSettings -> (structure)

The settings for the email message.

EmailMessage -> (string)

The contents of the email message.

EmailSubject -> (string)

The contents of the subject line of the email message.

SmsSettings -> (structure)

The settings for the SMS message.

SmsMessage -> (string)

The contents of the SMS message.

JSON Syntax:

```
{
  "AuthResources": "USER_POOL_ONLY"|"IDENTITY_POOL_AND_USER_POOL",
  "IdentityPoolConfigs": {
    "IdentityPoolName": "string",
    "UnauthenticatedLogin": true|false
  },
  "Service": "COGNITO",
  "UserPoolConfigs": {
    "ForgotPassword": {
      "DeliveryMethod": "EMAIL"|"SMS",
      "EmailSettings": {
        "EmailMessage": "string",
        "EmailSubject": "string"
      },
      "SmsSettings": {
        "SmsMessage": "string"
      }
    },
    "Mfa": {
      "MFAMode": "ON"|"OFF"|"OPTIONAL",
      "Settings": {
        "MfaTypes": ["SMS"|"TOTP", ...],
        "SmsMessage": "string"
      }
    },
    "OAuth": {
      "DomainPrefix": "string",
      "OAuthGrantType": "CODE"|"IMPLICIT",
      "OAuthScopes": ["PHONE"|"EMAIL"|"OPENID"|"PROFILE"|"AWS_COGNITO_SIGNIN_USER_ADMIN", ...],
      "RedirectSignInURIs": ["string", ...],
      "RedirectSignOutURIs": ["string", ...],
      "SocialProviderSettings": {
        "Facebook": {
          "ClientId": "string",
          "ClientSecret": "string"
        },
        "Google": {
          "ClientId": "string",
          "ClientSecret": "string"
        },
        "LoginWithAmazon": {
          "ClientId": "string",
          "ClientSecret": "string"
        },
        "SignInWithApple": {
          "ClientId": "string",
          "KeyId": "string",
          "PrivateKey": "string",
          "TeamId": "string"
        }
      }
    },
    "PasswordPolicy": {
      "AdditionalConstraints": ["REQUIRE_DIGIT"|"REQUIRE_LOWERCASE"|"REQUIRE_SYMBOL"|"REQUIRE_UPPERCASE", ...],
      "MinimumLength": double
    },
    "RequiredSignUpAttributes": ["ADDRESS"|"BIRTHDATE"|"EMAIL"|"FAMILY_NAME"|"GENDER"|"GIVEN_NAME"|"LOCALE"|"MIDDLE_NAME"|"NAME"|"NICKNAME"|"PHONE_NUMBER"|"PICTURE"|"PREFERRED_USERNAME"|"PROFILE"|"UPDATED_AT"|"WEBSITE"|"ZONE_INFO", ...],
    "SignInMethod": "EMAIL"|"EMAIL_AND_PHONE_NUMBER"|"PHONE_NUMBER"|"USERNAME",
    "UserPoolName": "string",
    "VerificationMessage": {
      "DeliveryMethod": "EMAIL"|"SMS",
      "EmailSettings": {
        "EmailMessage": "string",
        "EmailSubject": "string"
      },
      "SmsSettings": {
        "SmsMessage": "string"
      }
    }
  }
}
```

`--resource-name` (string)

The name of this resource.

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

AppId -> (string)

The app ID.

BackendEnvironmentName -> (string)

The name of the backend environment.

Error -> (string)

If the request fails, this error is returned.

JobId -> (string)

The ID for the job.

Operation -> (string)

The name of the operation.

Status -> (string)

The current status of the request.