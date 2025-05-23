# start-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# start-session

## Description

Creates a session for running calculations within a workgroup. The session is ready when it reaches an `IDLE` state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/StartSession)

## Synopsis

```
start-session
[--description <value>]
--work-group <value>
--engine-configuration <value>
[--notebook-version <value>]
[--session-idle-timeout-in-minutes <value>]
[--client-request-token <value>]
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

`--description` (string)

The session description.

`--work-group` (string)

The workgroup to which the session belongs.

`--engine-configuration` (structure)

Contains engine data processing unit (DPU) configuration settings and parameter mappings.

CoordinatorDpuSize -> (integer)

The number of DPUs to use for the coordinator. A coordinator is a special executor that orchestrates processing work and manages other executors in a notebook session. The default is 1.

MaxConcurrentDpus -> (integer)

The maximum number of DPUs that can run concurrently.

DefaultExecutorDpuSize -> (integer)

The default number of DPUs to use for executors. An executor is the smallest unit of compute that a notebook session can request from Athena. The default is 1.

AdditionalConfigs -> (map)

Contains additional notebook engine `MAP<string, string>` parameter mappings in the form of key-value pairs. To specify an Athena notebook that the Jupyter server will download and serve, specify a value for the  StartSessionRequest$NotebookVersion field, and then add a key named `NotebookId` to `AdditionalConfigs` that has the value of the Athena notebook ID.

key -> (string)

value -> (string)

SparkProperties -> (map)

Specifies custom jar files and Spark properties for use cases like cluster encryption, table formats, and general Spark tuning.

key -> (string)

value -> (string)

Shorthand Syntax:

```
CoordinatorDpuSize=integer,MaxConcurrentDpus=integer,DefaultExecutorDpuSize=integer,AdditionalConfigs={KeyName1=string,KeyName2=string},SparkProperties={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "CoordinatorDpuSize": integer,
  "MaxConcurrentDpus": integer,
  "DefaultExecutorDpuSize": integer,
  "AdditionalConfigs": {"string": "string"
    ...},
  "SparkProperties": {"string": "string"
    ...}
}
```

`--notebook-version` (string)

The notebook version. This value is supplied automatically for notebook sessions in the Athena console and is not required for programmatic session access. The only valid notebook version is `Athena notebook version 1` . If you specify a value for `NotebookVersion` , you must also specify a value for `NotebookId` . See  EngineConfiguration$AdditionalConfigs .

`--session-idle-timeout-in-minutes` (integer)

The idle timeout in minutes for the session.

`--client-request-token` (string)

A unique case-sensitive string used to ensure the request to create the session is idempotent (executes only once). If another `StartSessionRequest` is received, the same response is returned and another session is not created. If a parameter has changed, an error is returned.

### Warning

This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.

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

SessionId -> (string)

The session ID.

State -> (string)

The state of the session. A description of each state follows.

`CREATING` - The session is being started, including acquiring resources.

`CREATED` - The session has been started.

`IDLE` - The session is able to accept a calculation.

`BUSY` - The session is processing another task and is unable to accept a calculation.

`TERMINATING` - The session is in the process of shutting down.

`TERMINATED` - The session and its resources are no longer running.

`DEGRADED` - The session has no healthy coordinators.

`FAILED` - Due to a failure, the session and its resources are no longer running.