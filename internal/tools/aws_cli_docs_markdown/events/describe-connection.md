# describe-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# describe-connection

## Description

Retrieves details about a connection.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/DescribeConnection)

## Synopsis

```
describe-connection
--name <value>
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

The name of the connection to retrieve.

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

The ARN of the connection retrieved.

Name -> (string)

The name of the connection retrieved.

Description -> (string)

The description for the connection retrieved.

InvocationConnectivityParameters -> (structure)

For connections to private APIs The parameters EventBridge uses to invoke the resource endpoint.

For more information, see [Connecting to private APIs](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html) in the * *Amazon EventBridge User Guide* * .

ResourceParameters -> (structure)

The parameters for EventBridge to use when invoking the resource endpoint.

ResourceConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the resource configuration for the private API.

ResourceAssociationArn -> (string)

For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private APIâs resource configuration.

For more information, see [Managing service network resource associations for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra) in the * *Amazon EventBridge User Guide* * .

ConnectionState -> (string)

The state of the connection retrieved.

StateReason -> (string)

The reason that the connection is in the current connection state.

AuthorizationType -> (string)

The type of authorization specified for the connection.

SecretArn -> (string)

The ARN of the secret created from the authorization parameters specified for the connection.

KmsKeyIdentifier -> (string)

The identifier of the KMS customer managed key for EventBridge to use to encrypt the connection, if one has been specified.

For more information, see [Encrypting connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections.html) in the *Amazon EventBridge User Guide* .

AuthParameters -> (structure)

The parameters to use for authorization for the connection.

BasicAuthParameters -> (structure)

The authorization parameters for Basic authorization.

Username -> (string)

The user name to use for Basic authorization.

OAuthParameters -> (structure)

The OAuth parameters to use for authorization.

ClientParameters -> (structure)

Details about the client parameters returned when OAuth is specified as the authorization type.

ClientID -> (string)

The client ID associated with the response to the connection request.

AuthorizationEndpoint -> (string)

The URL to the HTTP endpoint that authorized the request.

HttpMethod -> (string)

The method used to connect to the HTTP endpoint.

OAuthHttpParameters -> (structure)

The additional HTTP parameters used for the OAuth authorization request.

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

The API Key parameters to use for authorization.

ApiKeyName -> (string)

The name of the header to use for the `APIKeyValue` used for authorization.

InvocationHttpParameters -> (structure)

Additional parameters for the connection that are passed through with every invocation to the HTTP endpoint.

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

For private OAuth authentication endpoints. The parameters EventBridge uses to authenticate against the endpoint.

For more information, see [Authorization methods for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html) in the * *Amazon EventBridge User Guide* * .

ResourceParameters -> (structure)

The parameters for EventBridge to use when invoking the resource endpoint.

ResourceConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the resource configuration for the private API.

ResourceAssociationArn -> (string)

For connections to private APIs, the Amazon Resource Name (ARN) of the resource association EventBridge created between the connection and the private APIâs resource configuration.

For more information, see [Managing service network resource associations for connections](https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html#connection-private-snra) in the * *Amazon EventBridge User Guide* * .

CreationTime -> (timestamp)

A time stamp for the time that the connection was created.

LastModifiedTime -> (timestamp)

A time stamp for the time that the connection was last modified.

LastAuthorizedTime -> (timestamp)

A time stamp for the time that the connection was last authorized.