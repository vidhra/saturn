# create-pluginÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-plugin.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/create-plugin.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# create-plugin

## Description

Creates an Amazon Q Business plugin.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/CreatePlugin)

## Synopsis

```
create-plugin
--application-id <value>
--display-name <value>
--type <value>
--auth-configuration <value>
[--server-url <value>]
[--custom-plugin-configuration <value>]
[--tags <value>]
[--client-token <value>]
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

`--application-id` (string)

The identifier of the application that will contain the plugin.

`--display-name` (string)

A the name for your plugin.

`--type` (string)

The type of plugin you want to create.

Possible values:

- `SERVICE_NOW`
- `SALESFORCE`
- `JIRA`
- `ZENDESK`
- `CUSTOM`
- `QUICKSIGHT`
- `SERVICENOW_NOW_PLATFORM`
- `JIRA_CLOUD`
- `SALESFORCE_CRM`
- `ZENDESK_SUITE`
- `ATLASSIAN_CONFLUENCE`
- `GOOGLE_CALENDAR`
- `MICROSOFT_TEAMS`
- `MICROSOFT_EXCHANGE`
- `PAGERDUTY_ADVANCE`
- `SMARTSHEET`
- `ASANA`

`--auth-configuration` (tagged union structure)

Authentication configuration information for an Amazon Q Business plugin.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `basicAuthConfiguration`, `oAuth2ClientCredentialConfiguration`, `noAuthConfiguration`, `idcAuthConfiguration`.

basicAuthConfiguration -> (structure)

Information about the basic authentication credentials used to configure a plugin.

secretArn -> (string)

The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..

roleArn -> (string)

The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.

oAuth2ClientCredentialConfiguration -> (structure)

Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

secretArn -> (string)

The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.

roleArn -> (string)

The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.

authorizationUrl -> (string)

The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.

tokenUrl -> (string)

The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.

noAuthConfiguration -> (structure)

Information about invoking a custom plugin without any authentication.

idcAuthConfiguration -> (structure)

Information about the IAM Identity Center Application used to configure authentication for a plugin.

idcApplicationArn -> (string)

The Amazon Resource Name (ARN) of the IAM Identity Center Application used to configure authentication.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role with permissions to perform actions on Amazon Web Services services on your behalf.

Shorthand Syntax:

```
basicAuthConfiguration={secretArn=string,roleArn=string},oAuth2ClientCredentialConfiguration={secretArn=string,roleArn=string,authorizationUrl=string,tokenUrl=string},noAuthConfiguration={},idcAuthConfiguration={idcApplicationArn=string,roleArn=string}
```

JSON Syntax:

```
{
  "basicAuthConfiguration": {
    "secretArn": "string",
    "roleArn": "string"
  },
  "oAuth2ClientCredentialConfiguration": {
    "secretArn": "string",
    "roleArn": "string",
    "authorizationUrl": "string",
    "tokenUrl": "string"
  },
  "noAuthConfiguration": {

  },
  "idcAuthConfiguration": {
    "idcApplicationArn": "string",
    "roleArn": "string"
  }
}
```

`--server-url` (string)

The source URL used for plugin configuration.

`--custom-plugin-configuration` (structure)

Contains configuration for a custom plugin.

description -> (string)

A description for your custom plugin configuration.

apiSchemaType -> (string)

The type of OpenAPI schema to use.

apiSchema -> (tagged union structure)

Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `payload`, `s3`.

payload -> (string)

The JSON or YAML-formatted payload defining the OpenAPI schema for a custom plugin.

s3 -> (structure)

Contains details about the S3 object containing the OpenAPI schema for a custom plugin. The schema could be in either JSON or YAML format.

bucket -> (string)

The name of the S3 bucket that contains the file.

key -> (string)

The name of the file.

Shorthand Syntax:

```
description=string,apiSchemaType=string,apiSchema={payload=string,s3={bucket=string,key=string}}
```

JSON Syntax:

```
{
  "description": "string",
  "apiSchemaType": "OPEN_API_V3",
  "apiSchema": {
    "payload": "string",
    "s3": {
      "bucket": "string",
      "key": "string"
    }
  }
}
```

`--tags` (list)

A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

(structure)

A list of key/value pairs that identify an index, FAQ, or data source. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the Amazon Q Business application or data source.

value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--client-token` (string)

A token that you provide to identify the request to create your Amazon Q Business plugin.

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

pluginId -> (string)

The identifier of the plugin created.

pluginArn -> (string)

The Amazon Resource Name (ARN) of a plugin.

buildStatus -> (string)

The current status of a plugin. A plugin is modified asynchronously.