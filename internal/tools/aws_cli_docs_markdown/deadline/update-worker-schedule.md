# update-worker-scheduleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-worker-schedule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-worker-schedule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# update-worker-schedule

## Description

Updates the schedule for a worker.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/UpdateWorkerSchedule)

## Synopsis

```
update-worker-schedule
--farm-id <value>
--fleet-id <value>
--worker-id <value>
[--updated-session-actions <value>]
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

`--farm-id` (string)

The farm ID to update.

`--fleet-id` (string)

The fleet ID to update.

`--worker-id` (string)

The worker ID to update.

`--updated-session-actions` (map)

The session actions associated with the worker schedule to update.

key -> (string)

value -> (structure)

The updated session action information as it relates to completion and progress of the session.

completedStatus -> (string)

The status of the session upon completion.

processExitCode -> (integer)

The process exit code. The default Deadline Cloud worker agent converts unsigned 32-bit exit codes to signed 32-bit exit codes.

progressMessage -> (string)

A message to indicate the progress of the updated session action.

startedAt -> (timestamp)

The date and time the resource started running.

endedAt -> (timestamp)

The date and time the resource ended running.

updatedAt -> (timestamp)

The updated time.

progressPercent -> (float)

The percentage completed.

Shorthand Syntax:

```
KeyName1=completedStatus=string,processExitCode=integer,progressMessage=string,startedAt=timestamp,endedAt=timestamp,updatedAt=timestamp,progressPercent=float,KeyName2=completedStatus=string,processExitCode=integer,progressMessage=string,startedAt=timestamp,endedAt=timestamp,updatedAt=timestamp,progressPercent=float
```

JSON Syntax:

```
{"string": {
      "completedStatus": "SUCCEEDED"|"FAILED"|"INTERRUPTED"|"CANCELED"|"NEVER_ATTEMPTED",
      "processExitCode": integer,
      "progressMessage": "string",
      "startedAt": timestamp,
      "endedAt": timestamp,
      "updatedAt": timestamp,
      "progressPercent": float
    }
  ...}
```

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

assignedSessions -> (map)

The assigned sessions to update.

key -> (string)

value -> (structure)

The assigned session for the worker.

queueId -> (string)

The queue ID of the assigned session.

jobId -> (string)

The job ID for the assigned session.

sessionActions -> (list)

The session actions to apply to the assigned session.

(structure)

The action for a session defined by the session action ID.

sessionActionId -> (string)

The session action ID for the assigned session.

definition -> (tagged union structure)

The definition of the assigned session action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `envEnter`, `envExit`, `taskRun`, `syncInputJobAttachments`.

envEnter -> (structure)

The environment a session starts on.

environmentId -> (string)

The environment ID of the assigned environment at the start of a session.

envExit -> (structure)

The environment a session exits from.

environmentId -> (string)

The environment ID of the assigned environment when exiting a session.

taskRun -> (structure)

The task run.

taskId -> (string)

The task ID.

stepId -> (string)

The step ID.

parameters -> (map)

The parameters to include.

key -> (string)

value -> (tagged union structure)

The data types for the task parameters.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `int`, `float`, `string`, `path`.

int -> (string)

A signed integer represented as a string.

float -> (string)

A double precision IEEE-754 floating point number represented as a string.

string -> (string)

A UTF-8 string.

path -> (string)

A file system path represented as a string.

syncInputJobAttachments -> (structure)

The job attachment to sync with an assigned session action.

stepId -> (string)

The step ID.

logConfiguration -> (structure)

The log configuration for the workerâs assigned session.

logDriver -> (string)

The log drivers for worker related logs.

options -> (map)

The options for a log driver.

key -> (string)

value -> (string)

parameters -> (map)

The parameters for the log configuration.

key -> (string)

value -> (string)

error -> (string)

The log configuration error details.

cancelSessionActions -> (map)

The session actions associated with the worker schedule to cancel.

key -> (string)

value -> (list)

(string)

desiredWorkerStatus -> (string)

The status to update the worker to.

updateIntervalSeconds -> (integer)

Updates the time interval (in seconds) for the schedule.