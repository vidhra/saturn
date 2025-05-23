# create-license-server-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/create-license-server-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/create-license-server-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager-user-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/index.html#cli-aws-license-manager-user-subscriptions) ]

# create-license-server-endpoint

## Description

Creates a network endpoint for the Remote Desktop Services (RDS) license server.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-user-subscriptions-2018-05-10/CreateLicenseServerEndpoint)

## Synopsis

```
create-license-server-endpoint
--identity-provider-arn <value>
--license-server-settings <value>
[--tags <value>]
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

`--identity-provider-arn` (string)

The Amazon Resource Name (ARN) that identifies the `IdentityProvider` resource that contains details about a registered identity provider. In the case of Active Directory, that can be a self-managed Active Directory or an Amazon Web Services Managed Active Directory that contains user identity details.

`--license-server-settings` (structure)

The `LicenseServerSettings` resource to create for the endpoint. The settings include the type of license server and the Secrets Manager secret that enables administrators to add or remove users associated with the license server.

ServerSettings -> (tagged union structure)

The `ServerSettings` resource contains the settings for your server.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RdsSalSettings`.

RdsSalSettings -> (structure)

The `RdsSalSettings` resource contains settings to configure a specific Remote Desktop Services (RDS) license server.

RdsSalCredentialsProvider -> (tagged union structure)

The `CredentialsProvider` resource contains a reference to the credentials provider thatâs used for RDS license server user administration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SecretsManagerCredentialsProvider`.

SecretsManagerCredentialsProvider -> (structure)

Identifies the Secrets Manager secret that contains credentials needed for user administration in the Active Directory.

SecretId -> (string)

The ID of the Secrets Manager secret that contains credentials.

ServerType -> (string)

The type of license server.

JSON Syntax:

```
{
  "ServerSettings": {
    "RdsSalSettings": {
      "RdsSalCredentialsProvider": {
        "SecretsManagerCredentialsProvider": {
          "SecretId": "string"
        }
      }
    }
  },
  "ServerType": "RDS_SAL"
}
```

`--tags` (map)

The tags that apply for the license server endpoint.

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

## Output

IdentityProviderArn -> (string)

The Amazon Resource Name (ARN) of the identity provider specified in the request.

LicenseServerEndpointArn -> (string)

The ARN of the `LicenseServerEndpoint` resource.