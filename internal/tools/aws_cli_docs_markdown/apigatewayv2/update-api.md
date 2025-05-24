# update-apiÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigatewayv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/index.html#cli-aws-apigatewayv2) ]

# update-api

## Description

Updates an Api resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/UpdateApi)

## Synopsis

```
update-api
--api-id <value>
[--api-key-selection-expression <value>]
[--cors-configuration <value>]
[--credentials-arn <value>]
[--description <value>]
[--disable-schema-validation | --no-disable-schema-validation]
[--disable-execute-api-endpoint | --no-disable-execute-api-endpoint]
[--ip-address-type <value>]
[--name <value>]
[--route-key <value>]
[--route-selection-expression <value>]
[--target <value>]
[--api-version <value>]
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

`--api-id` (string)

The API identifier.

`--api-key-selection-expression` (string)

An API key selection expression. Supported only for WebSocket APIs. See [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions) .

`--cors-configuration` (structure)

A CORS configuration. Supported only for HTTP APIs.

AllowCredentials -> (boolean)

Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders -> (list)

Represents a collection of allowed headers. Supported only for HTTP APIs.

(string)

AllowMethods -> (list)

Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string)

A string with a length between [1-64].

AllowOrigins -> (list)

Represents a collection of allowed origins. Supported only for HTTP APIs.

(string)

ExposeHeaders -> (list)

Represents a collection of exposed headers. Supported only for HTTP APIs.

(string)

MaxAge -> (integer)

The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.

Shorthand Syntax:

```
AllowCredentials=boolean,AllowHeaders=string,string,AllowMethods=string,string,AllowOrigins=string,string,ExposeHeaders=string,string,MaxAge=integer
```

JSON Syntax:

```
{
  "AllowCredentials": true|false,
  "AllowHeaders": ["string", ...],
  "AllowMethods": ["string", ...],
  "AllowOrigins": ["string", ...],
  "ExposeHeaders": ["string", ...],
  "MaxAge": integer
}
```

`--credentials-arn` (string)

This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the roleâs Amazon Resource Name (ARN). To require that the callerâs identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, donât specify this parameter. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs.

`--description` (string)

The description of the API.

`--disable-schema-validation` | `--no-disable-schema-validation` (boolean)

Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

`--disable-execute-api-endpoint` | `--no-disable-execute-api-endpoint` (boolean)

Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default [https:/](https://awscli.amazonaws.com/)/{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.

`--ip-address-type` (string)

The IP address types that can invoke your API or domain name.

Possible values:

- `ipv4`
- `dualstack`

`--name` (string)

The name of the API.

`--route-key` (string)

This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs.

`--route-selection-expression` (string)

The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

`--target` (string)

This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you canât remove it from an API. Supported only for HTTP APIs.

`--api-version` (string)

A version identifier for the API.

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

**To enable CORS for an HTTP API**

The following `update-api` example updates the specified APIâs CORS configuration to allow requests from `https://www.example.com`.

```
aws apigatewayv2 update-api \
    --api-id a1b2c3d4 \
    --cors-configuration AllowOrigins=https://www.example.com
```

Output:

```
{
    "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com",
    "ApiId": "a1b2c3d4",
    "ApiKeySelectionExpression": "$request.header.x-api-key",
    "CorsConfiguration": {
        "AllowCredentials": false,
        "AllowHeaders": [
            "header1",
            "header2"
        ],
        "AllowMethods": [
            "GET",
            "OPTIONS"
        ],
        "AllowOrigins": [
            "https://www.example.com"
        ]
    },
    "CreatedDate": "2020-04-08T18:39:37+00:00",
    "Name": "my-http-api",
    "ProtocolType": "HTTP",
    "RouteSelectionExpression": "$request.method $request.path",
    "Tags": {},
    "Version": "v1.0"
}
```

For more information, see [Configuring CORS for an HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) in the *Amazon API Gateway Developer Guide*.

## Output

ApiEndpoint -> (string)

The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The stage name is typically appended to this URI to form a complete path to a deployed API stage.

ApiGatewayManaged -> (boolean)

Specifies whether an API is managed by API Gateway. You canât update or delete a managed API by using API Gateway. A managed API can be deleted only through the tooling or service that created it.

ApiId -> (string)

The API ID.

ApiKeySelectionExpression -> (string)

An API key selection expression. Supported only for WebSocket APIs. See [API Key Selection Expressions](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions) .

CorsConfiguration -> (structure)

A CORS configuration. Supported only for HTTP APIs.

AllowCredentials -> (boolean)

Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.

AllowHeaders -> (list)

Represents a collection of allowed headers. Supported only for HTTP APIs.

(string)

AllowMethods -> (list)

Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.

(string)

A string with a length between [1-64].

AllowOrigins -> (list)

Represents a collection of allowed origins. Supported only for HTTP APIs.

(string)

ExposeHeaders -> (list)

Represents a collection of exposed headers. Supported only for HTTP APIs.

(string)

MaxAge -> (integer)

The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.

CreatedDate -> (timestamp)

The timestamp when the API was created.

Description -> (string)

The description of the API.

DisableSchemaValidation -> (boolean)

Avoid validating models when creating a deployment. Supported only for WebSocket APIs.

DisableExecuteApiEndpoint -> (boolean)

Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default [https:/](https://awscli.amazonaws.com/)/{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.

ImportInfo -> (list)

The validation information during API import. This may include particular properties of your OpenAPI definition which are ignored during import. Supported only for HTTP APIs.

(string)

IpAddressType -> (string)

The IP address types that can invoke the API.

Name -> (string)

The name of the API.

ProtocolType -> (string)

The API protocol.

RouteSelectionExpression -> (string)

The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

Tags -> (map)

A collection of tags associated with the API.

key -> (string)

value -> (string)

A string with a length between [0-1600].

Version -> (string)

A version identifier for the API.

Warnings -> (list)

The warning messages reported when failonwarnings is turned on during API import.

(string)