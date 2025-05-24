# create-ota-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/create-ota-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/create-ota-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot-managed-integrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-managed-integrations/index.html#cli-aws-iot-managed-integrations) ]

# create-ota-task

## Description

Create an over-the-air (OTA) task to update a device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-managed-integrations-2025-03-03/CreateOtaTask)

## Synopsis

```
create-ota-task
[--description <value>]
--s3-url <value>
[--protocol <value>]
[--target <value>]
[--task-configuration-id <value>]
[--ota-mechanism <value>]
--ota-type <value>
[--ota-target-query-string <value>]
[--client-token <value>]
[--ota-scheduling-config <value>]
[--ota-task-execution-retry-config <value>]
[--tags <value>]
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

The description of the over-the-air (OTA) task.

`--s3-url` (string)

The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.

`--protocol` (string)

The connection protocol the over-the-air (OTA) task uses to update the device.

Possible values:

- `HTTP`

`--target` (list)

The device targeted for the over-the-air (OTA) task.

(string)

Syntax:

```
"string" "string" ...
```

`--task-configuration-id` (string)

The identifier for the over-the-air (OTA) task configuration.

`--ota-mechanism` (string)

The deployment mechanism for the over-the-air (OTA) task.

Possible values:

- `PUSH`

`--ota-type` (string)

The frequency type for the over-the-air (OTA) task.

Possible values:

- `ONE_TIME`
- `CONTINUOUS`

`--ota-target-query-string` (string)

The query string to add things to the thing group.

`--client-token` (string)

An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.

`--ota-scheduling-config` (structure)

Over-the-air (OTA) task scheduling config.

EndBehavior -> (string)

Specifies the end behavior for all task executions after a task reaches the selected `endTime` . If `endTime` is not selected when creating the task, then `endBehavior` does not apply.

EndTime -> (string)

The time an over-the-air (OTA) task will stop.

MaintenanceWindows -> (list)

Maintenance window list for over-the-air (OTA) task scheduling config.

(structure)

Structure representing scheduling maintenance window.

DurationInMinutes -> (integer)

Displays the duration of the next maintenance window.

StartTime -> (string)

Displays the start time of the next maintenance window.

StartTime -> (string)

The time an over-the-air (OTA) task will start.

Shorthand Syntax:

```
EndBehavior=string,EndTime=string,MaintenanceWindows=[{DurationInMinutes=integer,StartTime=string},{DurationInMinutes=integer,StartTime=string}],StartTime=string
```

JSON Syntax:

```
{
  "EndBehavior": "STOP_ROLLOUT"|"CANCEL"|"FORCE_CANCEL",
  "EndTime": "string",
  "MaintenanceWindows": [
    {
      "DurationInMinutes": integer,
      "StartTime": "string"
    }
    ...
  ],
  "StartTime": "string"
}
```

`--ota-task-execution-retry-config` (structure)

Over-the-air (OTA) task retry config.

RetryConfigCriteria -> (list)

The list of retry config criteria.

(structure)

Structure representing one retry config criteria.

FailureType -> (string)

Over-the-air (OTA) retry criteria failure type.

MinNumberOfRetries -> (integer)

The number of retries allowed for a failure type for the over-the-air (OTA) task.

Shorthand Syntax:

```
RetryConfigCriteria=[{FailureType=string,MinNumberOfRetries=integer},{FailureType=string,MinNumberOfRetries=integer}]
```

JSON Syntax:

```
{
  "RetryConfigCriteria": [
    {
      "FailureType": "FAILED"|"TIMED_OUT"|"ALL",
      "MinNumberOfRetries": integer
    }
    ...
  ]
}
```

`--tags` (map)

A set of key/value pairs that are used to manage the over-the-air (OTA) task.

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

TaskId -> (string)

The identifier of the over-the-air (OTA) task.

TaskArn -> (string)

The Amazon Resource Name (ARN) of the over-the-air (OTA) task.

Description -> (string)

A description of the over-the-air (OTA) task.