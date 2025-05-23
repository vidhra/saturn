# configure-agentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/configure-agent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/configure-agent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguruprofiler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html#cli-aws-codeguruprofiler) ]

# configure-agent

## Description

Used by profiler agents to report their current state and to receive remote configuration updates. For example, `ConfigureAgent` can be used to tell an agent whether to profile or not and for how long to return profiling data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguruprofiler-2019-07-18/ConfigureAgent)

## Synopsis

```
configure-agent
[--fleet-instance-id <value>]
[--metadata <value>]
--profiling-group-name <value>
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

`--fleet-instance-id` (string)

A universally unique identifier (UUID) for a profiling instance. For example, if the profiling instance is an Amazon EC2 instance, it is the instance ID. If it is an AWS Fargate container, it is the containerâs task ID.

`--metadata` (map)

Metadata captured about the compute platform the agent is running on. It includes information about sampling and reporting. The valid fields are:

- `COMPUTE_PLATFORM` - The compute platform on which the agent is running
- `AGENT_ID` - The ID for an agent instance.
- `AWS_REQUEST_ID` - The AWS request ID of a Lambda invocation.
- `EXECUTION_ENVIRONMENT` - The execution environment a Lambda function is running on.
- `LAMBDA_FUNCTION_ARN` - The Amazon Resource Name (ARN) that is used to invoke a Lambda function.
- `LAMBDA_MEMORY_LIMIT_IN_MB` - The memory allocated to a Lambda function.
- `LAMBDA_REMAINING_TIME_IN_MILLISECONDS` - The time in milliseconds before execution of a Lambda function times out.
- `LAMBDA_TIME_GAP_BETWEEN_INVOKES_IN_MILLISECONDS` - The time in milliseconds between two invocations of a Lambda function.
- `LAMBDA_PREVIOUS_EXECUTION_TIME_IN_MILLISECONDS` - The time in milliseconds for the previous Lambda invocation.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  ComputePlatform
  AgentId
  AwsRequestId
  ExecutionEnvironment
  LambdaFunctionArn
  LambdaMemoryLimitInMB
  LambdaRemainingTimeInMilliseconds
  LambdaTimeGapBetweenInvokesInMilliseconds
  LambdaPreviousExecutionTimeInMilliseconds
```

JSON Syntax:

```
{"ComputePlatform"|"AgentId"|"AwsRequestId"|"ExecutionEnvironment"|"LambdaFunctionArn"|"LambdaMemoryLimitInMB"|"LambdaRemainingTimeInMilliseconds"|"LambdaTimeGapBetweenInvokesInMilliseconds"|"LambdaPreviousExecutionTimeInMilliseconds": "string"
  ...}
```

`--profiling-group-name` (string)

The name of the profiling group for which the configured agent is collecting profiling data.

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

configuration -> (structure)

An ` `AgentConfiguration` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration).html`__ object that specifies if an agent profiles or not and for how long to return profiling data.

agentParameters -> (map)

Parameters used by the profiler. The valid parameters are:

- `MaxStackDepth` - The maximum depth of the stacks in the code that is represented in the profile. For example, if CodeGuru Profiler finds a method `A` , which calls method `B` , which calls method `C` , which calls method `D` , then the depth is 4. If the `maxDepth` is set to 2, then the profiler evaluates `A` and `B` .
- `MemoryUsageLimitPercent` - The percentage of memory that is used by the profiler.
- `MinimumTimeForReportingInMilliseconds` - The minimum time in milliseconds between sending reports.
- `ReportingIntervalInMilliseconds` - The reporting interval in milliseconds used to report profiles.
- `SamplingIntervalInMilliseconds` - The sampling interval in milliseconds that is used to profile samples.

key -> (string)

value -> (string)

periodInSeconds -> (integer)

How long a profiling agent should send profiling data using ` `ConfigureAgent` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent).html`__ . For example, if this is set to 300, the profiling agent calls ` `ConfigureAgent` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent).html`__ every 5 minutes to submit the profiled data collected during that period.

shouldProfile -> (boolean)

A `Boolean` that specifies whether the profiling agent collects profiling data or not. Set to `true` to enable profiling.