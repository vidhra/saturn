# create-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# create-connection

## Description

Creates a connection. A connection defines the authorization type and credentials to use for authorization with an API destination HTTP endpoint.

For more information, see [Connections for endpoint targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection.html) in the *Amazon EventBridge User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/CreateConnection)

## Synopsis

```
create-connection
--name <value>
[--description <value>]
--authorization-type <value>
--auth-parameters <value>
[--invocation-connectivity-parameters <value>]
[--kms-key-identifier <value>]
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

`--name` (string)

The name for the connection to create.

`--description` (string)

A description for the connection to create.

`--authorization-type` (string)

The type of authorization to use for the connection.

### Note

OAUTH tokens are refreshed when a 401 or 407 response is returned.

Possible values:

- `BASIC`
- `OAUTH_CLIENT_CREDENTIALS`
- `API_KEY`

`--auth-parameters` (structure)

The authorization parameters to use to authorize with the endpoint.

You must include only authorization parameters for the `AuthorizationType` you specify.

BasicAuthParameters -> (structure)

The Basic authorization parameters to use for the connection.

Username -> (string)

The user name to use for Basic authorization.

Password -> (string)

The password associated with the user name to use for Basic authorization.

OAuthParameters -> (structure)

The OAuth authorization parameters to use for the connection.

ClientParameters -> (structure)

The client parameters for OAuth authorization.

ClientID -> (string)

The client ID to use for OAuth authorization for the connection.

ClientSecret -> (string)

The client secret associated with the client ID to use for OAuth authorization for the connection.

AuthorizationEndpoint -> (string)

The URL to the authorization endpoint when OAuth is specified as the authorization type.

HttpMethod -> (string)

The method to use for the authorization request.

OAuthHttpParameters -> (structure)

Details about the additional parameters to use for the connection.

HeaderParameters -> (list)

Any additional header parameters for the connection.

(structure)

Additional parameter included in the header. You can include up to 100 additional header parameters per request. An event payload cannot exceed 64 KB.

Key -> (string)

The key for the parameter.

Value -> (string)

The value associated with the key.

IsValueSecret -> (boolean)

Specifies whether the value is a secret.

QueryStringParameters -> (list)

Any additional query string parameters for the connection.

(structure)

Any additional query string parameter for the connection. You can include up to 100 additional query string parameters per request. Each additional parameter counts towards the event payload size, which cannot exceed 64 KB.

Key -> (string)

The key for a query string parameter.

Value -> (string)

The value associated with the key for the query string parameter.

IsValueSecret -> (boolean)

Specifies whether the value is secret.

BodyParameters -> (list)

Any additional body string parameters for the connection.

(structure)

Additional parameter included in the body. You can include up to 100 additional body parameters per request. An event payload cannot exceed 64 KB.

Key -> (string)

The key for the parameter.

Value -> (string)

The value associated with the key.

IsValueSecret -> (boolean)

Specifies whether the value is secret.

ApiKeyAuthParameters -> (structure)

The API key authorization parameters to use for the connection.

ApiKeyName -> (string)

The name of the API key to use for authorization.

ApiKeyValue -> (string)

The value for the API key to use for authorization.

InvocationHttpParameters -> (structure)

The API key authorization parameters to use for the connection. Note that if you include additional parameters for the target of a rule via `HttpParameters` , including query strings, the parameters added for the connection take precedence.

HeaderParameters -> (list)

Any additional header parameters for the connection.

(structure)

Additional parameter included in the header. You can include up to 100 additional header parameters per request. An event payload cannot exceed 64 KB.

Key -> (string)

The key for the parameter.

Value -> (string)

The value associated with the key.

IsValueSecret -> (boolean)

Specifies whether the value is a secret.

QueryStringParameters -> (list)

Any additional query string parameters for the connection.

(structure)

Any additional query string parameter for the connection. You can include up to 100 additional query string parameters per request. Each additional parameter counts towards the event payload size, which cannot exceed 64 KB.

Key -> (string)

The key for a query string parameter.

Value -> (string)

The value associated with the key for the query string parameter.

IsValueSecret -> (boolean)

Specifies whether the value is secret.

BodyParameters -> (list)

Any additional body string parameters for the connection.

(structure)

Additional parameter included in the body. You can include up to 100 additional body parameters per request. An event payload cannot exceed 64 KB.

Key -> (string)

The key for the parameter.

Value -> (string)

The value associated with the key.

IsValueSecret -> (boolean)

Specifies whether the value is secret.

ConnectivityParameters -> (structure)

If you specify a private OAuth endpoint, the parameters for EventBridge to use when authenticating against the endpoint.

For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* * .

ResourceParameters -> (structure)

The parameters for EventBridge to use when invoking the resource endpoint.

ResourceConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration for the resource endpoint.

JSON Syntax:

```
{
  "BasicAuthParameters": {
    "Username": "string",
    "Password": "string"
  },
  "OAuthParameters": {
    "ClientParameters": {
      "ClientID": "string",
      "ClientSecret": "string"
    },
    "AuthorizationEndpoint": "string",
    "HttpMethod": "GET"|"POST"|"PUT",
    "OAuthHttpParameters": {
      "HeaderParameters": [
        {
          "Key": "string",
          "Value": "string",
          "IsValueSecret": true|false
        }
        ...
      ],
      "QueryStringParameters": [
        {
          "Key": "string",
          "Value": "string",
          "IsValueSecret": true|false
        }
        ...
      ],
      "BodyParameters": [
        {
          "Key": "string",
          "Value": "string",
          "IsValueSecret": true|false
        }
        ...
      ]
    }
  },
  "ApiKeyAuthParameters": {
    "ApiKeyName": "string",
    "ApiKeyValue": "string"
  },
  "InvocationHttpParameters": {
    "HeaderParameters": [
      {
        "Key": "string",
        "Value": "string",
        "IsValueSecret": true|false
      }
      ...
    ],
    "QueryStringParameters": [
      {
        "Key": "string",
        "Value": "string",
        "IsValueSecret": true|false
      }
      ...
    ],
    "BodyParameters": [
      {
        "Key": "string",
        "Value": "string",
        "IsValueSecret": true|false
      }
      ...
    ]
  },
  "ConnectivityParameters": {
    "ResourceParameters": {
      "ResourceConfigurationArn": "string"
    }
  }
}
```

`--invocation-connectivity-parameters` (structure)

For connections to private APIs, the parameters to use for invoking the API.

For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* * .

ResourceParameters -> (structure)

The parameters for EventBridge to use when invoking the resource endpoint.

ResourceConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the Amazon VPC Lattice resource configuration for the resource endpoint.

Shorthand Syntax:

```
ResourceParameters={ResourceConfigurationArn=string}
```

JSON Syntax:

```
{
  "ResourceParameters": {
    "ResourceConfigurationArn": "string"
  }
}
```

`--kms-key-identifier` (string)

The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this connection. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.

If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt the connection.

For more information, see [Identify and view keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the *Key Management Service Developer Guide* .

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

ConnectionArn -> (string)

The ARN of the connection that was created by the request.

ConnectionState -> (string)

The state of the connection that was created by the request.

CreationTime -> (timestamp)

A time stamp for the time that the connection was created.

LastModifiedTime -> (timestamp)

A time stamp for the time that the connection was last updated.