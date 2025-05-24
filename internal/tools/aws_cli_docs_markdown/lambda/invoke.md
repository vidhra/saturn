# invokeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html#cli-aws-lambda) ]

# invoke

## Description

Invokes a Lambda function. You can invoke a function synchronously (and wait for the response), or asynchronously. By default, Lambda invokes your function synchronously (i.e. the``InvocationType`` is `RequestResponse` ). To invoke a function asynchronously, set `InvocationType` to `Event` . Lambda passes the `ClientContext` object to your function for synchronous invocations only.

For [synchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html) , details about the function response, including errors, are included in the response body and headers. For either invocation type, you can find more information in the [execution log](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html) and [trace](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html) .

When an error occurs, your function may be invoked multiple times. Retry behavior varies by error type, client, event source, and invocation type. For example, if you invoke a function asynchronously and it returns an error, Lambda executes the function up to two more times. For more information, see [Error handling and automatic retries in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html) .

For [asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) , Lambda adds events to a queue before sending them to your function. If your function does not have enough capacity to keep up with the queue, events may be lost. Occasionally, your function may receive the same event multiple times, even if no error occurs. To retain events that were not processed, configure your function with a [dead-letter queue](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq) .

The status code in the API response doesnât reflect function errors. Error codes are reserved for errors that prevent your function from executing, such as permissions errors, [quota](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) errors, or issues with your functionâs code and configuration. For example, Lambda returns `TooManyRequestsException` if running the function would cause you to exceed a concurrency limit at either the account level (`ConcurrentInvocationLimitExceeded` ) or function level (`ReservedFunctionConcurrentInvocationLimitExceeded` ).

For functions with a long timeout, your client might disconnect during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings.

This operation requires permission for the [lambda:InvokeFunction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awslambda.html) action. For details on how to set up permissions for cross-account invocations, see [Granting function access to other accounts](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html#permissions-resource-xaccountinvoke) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/Invoke)

## Synopsis

```
invoke
--function-name <value>
[--invocation-type <value>]
[--log-type <value>]
[--client-context <value>]
[--payload <value>]
[--qualifier <value>]
<outfile>
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

The name or ARN of the Lambda function, version, or alias.

**Name formats**

- **Function name** â `my-function` (name-only), `my-function:v1` (with alias).
- **Function ARN** â `arn:aws:lambda:us-west-2:123456789012:function:my-function` .
- **Partial ARN** â `123456789012:function:my-function` .

You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

`--invocation-type` (string)

Choose from the following options.

- `RequestResponse` (default) â Invoke the function synchronously. Keep the connection open until the function returns a response or times out. The API response includes the function response and additional data.
- `Event` â Invoke the function asynchronously. Send events that fail multiple times to the functionâs dead-letter queue (if one is configured). The API response only includes a status code.
- `DryRun` â Validate parameter values and verify that the user or role has permission to invoke the function.

Possible values:

- `Event`
- `RequestResponse`
- `DryRun`

`--log-type` (string)

Set to `Tail` to include the execution log in the response. Applies to synchronously invoked functions only.

Possible values:

- `None`
- `Tail`

`--client-context` (string)

Up to 3,583 bytes of base64-encoded data about the invoking client to pass to the function in the context object. Lambda passes the `ClientContext` object to your function for synchronous invocations only.

`--payload` (blob)

The JSON that you want to provide to your Lambda function as input.

You can enter the JSON directly. For example, `--payload '{ "key": "value" }'` . You can also specify a file path. For example, `--payload file://payload.json` .

`--qualifier` (string)

Specify a version or alias to invoke a published version of the function.

`outfile` (string)
Filename where the content will be saved

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

**Example 1: To invoke a Lambda function synchronously**

The following `invoke` example invokes the `my-function` function synchronously. The `cli-binary-format` option is required if youâre using AWS CLI version 2. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide*.

```
aws lambda invoke \
    --function-name my-function \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "name": "Bob" }' \
    response.json
```

Output:

```
{
    "ExecutedVersion": "$LATEST",
    "StatusCode": 200
}
```

For more information, see [Invoke a Lambda function synchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html) in the *AWS Lambda Developer Guide*.

**Example 2: To invoke a Lambda function asynchronously**

The following `invoke` example invokes the `my-function` function asynchronously. The `cli-binary-format` option is required if youâre using AWS CLI version 2. For more information, see [AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list) in the *AWS Command Line Interface User Guide*.

```
aws lambda invoke \
    --function-name my-function \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "name": "Bob" }' \
    response.json
```

Output:

```
{
    "StatusCode": 202
}
```

For more information, see [Invoking a Lambda function asynchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) in the *AWS Lambda Developer Guide*.

## Output

StatusCode -> (integer)

The HTTP status code is in the 200 range for a successful request. For the `RequestResponse` invocation type, this status code is 200. For the `Event` invocation type, this status code is 202. For the `DryRun` invocation type, the status code is 204.

FunctionError -> (string)

If present, indicates that an error occurred during function execution. Details about the error are included in the response payload.

LogResult -> (string)

The last 4 KB of the execution log, which is base64-encoded.

Payload -> (blob)

The response from the function, or an error object.

ExecutedVersion -> (string)

The version of the function that executed. When you invoke a function with an alias, this indicates which version the alias resolved to.