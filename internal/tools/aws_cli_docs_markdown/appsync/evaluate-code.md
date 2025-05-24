# evaluate-codeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/evaluate-code.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/evaluate-code.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# evaluate-code

## Description

Evaluates the given code and returns the response. The code definition requirements depend on the specified runtime. For `APPSYNC_JS` runtimes, the code defines the request and response functions. The request function takes the incoming request after a GraphQL operation is parsed and converts it into a request configuration for the selected data source operation. The response function interprets responses from the data source and maps it to the shape of the GraphQL field output type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/EvaluateCode)

## Synopsis

```
evaluate-code
--runtime <value>
--code <value>
--context <value>
[--function <value>]
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

`--runtime` (structure)

The runtime to be used when evaluating the code. Currently, only the `APPSYNC_JS` runtime is supported.

name -> (string)

The `name` of the runtime to use. Currently, the only allowed value is `APPSYNC_JS` .

runtimeVersion -> (string)

The `version` of the runtime to use. Currently, the only allowed version is `1.0.0` .

Shorthand Syntax:

```
name=string,runtimeVersion=string
```

JSON Syntax:

```
{
  "name": "APPSYNC_JS",
  "runtimeVersion": "string"
}
```

`--code` (string)

The code definition to be evaluated. Note that `code` and `runtime` are both required for this action. The `runtime` value must be `APPSYNC_JS` .

`--context` (string)

The map that holds all of the contextual information for your resolver invocation. A `context` is required for this action.

`--function` (string)

The function within the code to be evaluated. If provided, the valid values are `request` and `response` .

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

evaluationResult -> (string)

The result of the evaluation operation.

error -> (structure)

Contains the payload of the response error.

message -> (string)

The error payload.

codeErrors -> (list)

Contains the list of `CodeError` objects.

(structure)

Describes an AppSync error.

errorType -> (string)

The type of code error.

Examples include, but arenât limited to: `LINT_ERROR` , `PARSER_ERROR` .

value -> (string)

A user presentable error.

Examples include, but arenât limited to: `Parsing error: Unterminated string literal` .

location -> (structure)

The line, column, and span location of the error in the code.

line -> (integer)

The line number in the code. Defaults to `0` if unknown.

column -> (integer)

The column number in the code. Defaults to `0` if unknown.

span -> (integer)

The span/length of the error. Defaults to `-1` if unknown.

logs -> (list)

A list of logs that were generated by calls to `util.log.info` and `util.log.error` in the evaluated code.

(string)

stash -> (string)

An object available inside each resolver and function handler. A single `stash` object lives through a single resolver run. Therefore, you can use the stash to pass arbitrary data across request and response handlers and across functions in a pipeline resolver.

outErrors -> (string)

The list of runtime errors that are added to the GraphQL operation response.