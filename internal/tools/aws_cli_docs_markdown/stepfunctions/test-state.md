# test-stateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/test-state.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/test-state.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# test-state

## Description

Accepts the definition of a single state and executes it. You can test a state without creating a state machine or updating an existing state machine. Using this API, you can test the following:

- A stateâs [input and output processing](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-input-output-dataflow) data flow
- An [Amazon Web Services service integration](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-services.html) request and response
- An [HTTP Task](https://docs.aws.amazon.com/step-functions/latest/dg/connect-third-party-apis.html) request and response

You can call this API on only one state at a time. The states that you can test include the following:

- [All Task types](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html#task-types) except [Activity](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html)
- [Pass](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-pass-state.html)
- [Wait](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html)
- [Choice](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-choice-state.html)
- [Succeed](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-succeed-state.html)
- [Fail](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-fail-state.html)

The `TestState` API assumes an IAM role which must contain the required IAM permissions for the resources your state is accessing. For information about the permissions a state might need, see [IAM permissions to test a state](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions) .

The `TestState` API can run for up to five minutes. If the execution of a state exceeds this duration, it fails with the `States.Timeout` error.

`TestState` doesnât support [Activity tasks](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html) , `.sync` or `.waitForTaskToken` [service integration patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) , [Parallel](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html) , or [Map](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-map-state.html) states.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/TestState)

## Synopsis

```
test-state
--definition <value>
[--role-arn <value>]
[--input <value>]
[--inspection-level <value>]
[--reveal-secrets | --no-reveal-secrets]
[--variables <value>]
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

`--definition` (string)

The [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) (ASL) definition of the state.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the execution role with the required IAM permissions for the state.

`--input` (string)

A string that contains the JSON input data for the state.

`--inspection-level` (string)

Determines the values to return when a state is tested. You can specify one of the following types:

- `INFO` : Shows the final state output. By default, Step Functions sets `inspectionLevel` to `INFO` if you donât specify a level.
- `DEBUG` : Shows the final state output along with the input and output data processing result.
- `TRACE` : Shows the HTTP request and response for an HTTP Task. This level also shows the final state output along with the input and output data processing result.

Each of these levels also provide information about the status of the state execution and the next state to transition to.

Possible values:

- `INFO`
- `DEBUG`
- `TRACE`

`--reveal-secrets` | `--no-reveal-secrets` (boolean)

Specifies whether or not to include secret information in the test result. For HTTP Tasks, a secret includes the data that an EventBridge connection adds to modify the HTTP request headers, query parameters, and body. Step Functions doesnât omit any information included in the state definition or the HTTP response.

If you set `revealSecrets` to `true` , you must make sure that the IAM user that calls the `TestState` API has permission for the `states:RevealSecrets` action. For an example of IAM policy that sets the `states:RevealSecrets` permission, see [IAM permissions to test a state](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions) . Without this permission, Step Functions throws an access denied error.

By default, `revealSecrets` is set to `false` .

`--variables` (string)

JSON object literal that sets variables used in the state under test. Object keys are the variable names and values are the variable values.

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

output -> (string)

The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.

error -> (string)

The error returned when the execution of a state fails.

cause -> (string)

A detailed explanation of the cause for the error when the execution of a state fails.

inspectionData -> (structure)

Returns additional details about the stateâs execution, including its input and output data processing flow, and HTTP request and response information. The `inspectionLevel` request parameter specifies which details are returned.

input -> (string)

The raw state input.

afterArguments -> (string)

The input after Step Functions applies an Arguments filter. This event will only be present when QueryLanguage for the state machine or individual states is set to JSONata. For more info, see [Transforming data with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/data-transform.html) .

afterInputPath -> (string)

The input after Step Functions applies the [InputPath](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-inputpath) filter. Not populated when QueryLanguage is JSONata.

afterParameters -> (string)

The effective input after Step Functions applies the [Parameters](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters) filter. Not populated when QueryLanguage is JSONata.

result -> (string)

The stateâs raw result.

afterResultSelector -> (string)

The effective result after Step Functions applies the [ResultSelector](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector) filter. Not populated when QueryLanguage is JSONata.

afterResultPath -> (string)

The effective result combined with the raw state input after Step Functions applies the [ResultPath](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultpath.html) filter. Not populated when QueryLanguage is JSONata.

request -> (structure)

The raw HTTP request that is sent when you test an HTTP Task.

protocol -> (string)

The protocol used to make the HTTP request.

method -> (string)

The HTTP method used for the HTTP request.

url -> (string)

The API endpoint used for the HTTP request.

headers -> (string)

The request headers associated with the HTTP request.

body -> (string)

The request body for the HTTP request.

response -> (structure)

The raw HTTP response that is returned when you test an HTTP Task.

protocol -> (string)

The protocol used to return the HTTP response.

statusCode -> (string)

The HTTP response status code for the HTTP response.

statusMessage -> (string)

The message associated with the HTTP status code.

headers -> (string)

The response headers associated with the HTTP response.

body -> (string)

The HTTP response returned.

variables -> (string)

JSON string that contains the set of workflow variables after execution of the state. The set will include variables assigned in the state and variables set up as test state input.

nextState -> (string)

The name of the next state to transition to. If you havenât defined a next state in your definition or if the execution of the state fails, this ï¬eld doesnât contain a value.

status -> (string)

The execution status of the state.