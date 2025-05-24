# list-sessionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-sessions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-sessions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# list-sessions

## Description

Retrieve a list of sessions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListSessions)

## Synopsis

```
list-sessions
[--next-token <value>]
[--max-results <value>]
[--tags <value>]
[--request-origin <value>]
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

`--next-token` (string)

The token for the next set of results, or null if there are no more result.

`--max-results` (integer)

The maximum number of results.

`--tags` (map)

Tags belonging to the session.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--request-origin` (string)

The origin of the request.

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

Ids -> (list)

Returns the ID of the session.

(string)

Sessions -> (list)

Returns the session object.

(structure)

The period in which a remote Spark runtime environment is running.

Id -> (string)

The ID of the session.

CreatedOn -> (timestamp)

The time and date when the session was created.

Status -> (string)

The session status.

ErrorMessage -> (string)

The error message displayed during the session.

Description -> (string)

The description of the session.

Role -> (string)

The name or Amazon Resource Name (ARN) of the IAM role associated with the Session.

Command -> (structure)

The command object.See SessionCommand.

Name -> (string)

Specifies the name of the SessionCommand. Can be âglueetlâ or âgluestreamingâ.

PythonVersion -> (string)

Specifies the Python version. The Python version indicates the version supported for jobs of type Spark.

DefaultArguments -> (map)

A map array of key-value pairs. Max is 75 pairs.

key -> (string)

value -> (string)

Connections -> (structure)

The number of connections used for the session.

Connections -> (list)

A list of connections used by the job.

(string)

Progress -> (double)

The code execution progress of the session.

MaxCapacity -> (double)

The number of Glue data processing units (DPUs) that can be allocated when the job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB memory.

SecurityConfiguration -> (string)

The name of the SecurityConfiguration structure to be used with the session.

GlueVersion -> (string)

The Glue version determines the versions of Apache Spark and Python that Glue supports. The GlueVersion must be greater than 2.0.

NumberOfWorkers -> (integer)

The number of workers of a defined `WorkerType` to use for the session.

WorkerType -> (string)

The type of predefined worker that is allocated when a session runs. Accepts a value of `G.1X` , `G.2X` , `G.4X` , or `G.8X` for Spark sessions. Accepts the value `Z.2X` for Ray sessions.

CompletedOn -> (timestamp)

The date and time that this session is completed.

ExecutionTime -> (double)

The total time the session ran for.

DPUSeconds -> (double)

The DPUs consumed by the session (formula: ExecutionTime * MaxCapacity).

IdleTimeout -> (integer)

The number of minutes when idle before the session times out.

ProfileName -> (string)

The name of an Glue usage profile associated with the session.

NextToken -> (string)

The token for the next set of results, or null if there are no more result.