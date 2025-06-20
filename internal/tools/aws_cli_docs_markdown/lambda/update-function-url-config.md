# update-function-url-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-url-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-url-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html#cli-aws-lambda) ]

# update-function-url-config

## Description

Updates the configuration for a Lambda function URL.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionUrlConfig)

## Synopsis

```
update-function-url-config
--function-name <value>
[--qualifier <value>]
[--auth-type <value>]
[--cors <value>]
[--invoke-mode <value>]
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

`--function-name` (string)

The name or ARN of the Lambda function.

**Name formats**

- **Function name** â `my-function` .
- **Function ARN** â `arn:aws:lambda:us-west-2:123456789012:function:my-function` .
- **Partial ARN** â `123456789012:function:my-function` .

The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

`--qualifier` (string)

The alias name.

`--auth-type` (string)

The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Security and auth model for Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html) .

Possible values:

- `NONE`
- `AWS_IAM`

`--cors` (structure)

The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.

AllowCredentials -> (boolean)

Whether to allow cookies or other credentials in requests to your function URL. The default is `false` .

AllowHeaders -> (list)

The HTTP headers that origins can include in requests to your function URL. For example: `Date` , `Keep-Alive` , `X-Custom-Header` .

(string)

AllowMethods -> (list)

The HTTP methods that are allowed when calling your function URL. For example: `GET` , `POST` , `DELETE` , or the wildcard character (`*` ).

(string)

AllowOrigins -> (list)

The origins that can access your function URL. You can list any number of specific origins, separated by a comma. For example: `https://www.example.com` , `http://localhost:60905` .

Alternatively, you can grant access to all origins using the wildcard character (`*` ).

(string)

ExposeHeaders -> (list)

The HTTP headers in your function response that you want to expose to origins that call your function URL. For example: `Date` , `Keep-Alive` , `X-Custom-Header` .

(string)

MaxAge -> (integer)

The maximum amount of time, in seconds, that web browsers can cache results of a preflight request. By default, this is set to `0` , which means that the browser doesnât cache results.

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

`--invoke-mode` (string)

Use one of the following options:

- `BUFFERED` â This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
- `RESPONSE_STREAM` â Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 20 MB, however, you can [request a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) .

Possible values:

- `BUFFERED`
- `RESPONSE_STREAM`

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

FunctionUrl -> (string)

The HTTP URL endpoint for your function.

FunctionArn -> (string)

The Amazon Resource Name (ARN) of your function.

AuthType -> (string)

The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Security and auth model for Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html) .

Cors -> (structure)

The [cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) settings for your function URL.

AllowCredentials -> (boolean)

Whether to allow cookies or other credentials in requests to your function URL. The default is `false` .

AllowHeaders -> (list)

The HTTP headers that origins can include in requests to your function URL. For example: `Date` , `Keep-Alive` , `X-Custom-Header` .

(string)

AllowMethods -> (list)

The HTTP methods that are allowed when calling your function URL. For example: `GET` , `POST` , `DELETE` , or the wildcard character (`*` ).

(string)

AllowOrigins -> (list)

The origins that can access your function URL. You can list any number of specific origins, separated by a comma. For example: `https://www.example.com` , `http://localhost:60905` .

Alternatively, you can grant access to all origins using the wildcard character (`*` ).

(string)

ExposeHeaders -> (list)

The HTTP headers in your function response that you want to expose to origins that call your function URL. For example: `Date` , `Keep-Alive` , `X-Custom-Header` .

(string)

MaxAge -> (integer)

The maximum amount of time, in seconds, that web browsers can cache results of a preflight request. By default, this is set to `0` , which means that the browser doesnât cache results.

CreationTime -> (string)

When the function URL was created, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

LastModifiedTime -> (string)

When the function URL configuration was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD).

InvokeMode -> (string)

Use one of the following options:

- `BUFFERED` â This is the default option. Lambda invokes your function using the `Invoke` API operation. Invocation results are available when the payload is complete. The maximum payload size is 6 MB.
- `RESPONSE_STREAM` â Your function streams payload results as they become available. Lambda invokes your function using the `InvokeWithResponseStream` API operation. The maximum response payload size is 20 MB, however, you can [request a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) .