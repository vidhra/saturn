# register-activity-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# register-activity-type

## Description

Registers a new *activity type* along with its configuration settings in the specified domain.

### Warning

A `TypeAlreadyExists` fault is returned if the type already exists in the domain. You cannot change any configuration settings of the type after its registration, and it must be registered as a new version.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- Constrain the following parameters by using a `Condition` element with the appropriate keys.
- `defaultTaskList.name` : String constraint. The key is `swf:defaultTaskList.name` .
- `name` : String constraint. The key is `swf:name` .
- `version` : String constraint. The key is `swf:version` .

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/RegisterActivityType)

## Synopsis

```
register-activity-type
--domain <value>
--name <value>
[--description <value>]
[--default-task-start-to-close-timeout <value>]
[--default-task-heartbeat-timeout <value>]
[--default-task-list <value>]
[--default-task-priority <value>]
[--default-task-schedule-to-start-timeout <value>]
[--default-task-schedule-to-close-timeout <value>]
--activity-version <value>
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

`--domain` (string)

The name of the domain in which this activity is to be registered.

`--name` (string)

The name of the activity type within the domain.

The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` | `\u007f-\u009f` ). Also, it must *not* be the literal string `arn` .

`--description` (string)

A textual description of the activity type.

`--default-task-start-to-close-timeout` (string)

If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

`--default-task-heartbeat-timeout` (string)

If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling  RecordActivityTaskHeartbeat . If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask`   Decision . If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an `UnknownResource` fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

`--default-task-list` (structure)

If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isnât provided when a task is scheduled through the `ScheduleActivityTask`   Decision .

name -> (string)

The name of the task list.

Shorthand Syntax:

```
name=string
```

JSON Syntax:

```
{
  "name": "string"
}
```

`--default-task-priority` (string)

The default task priority to assign to the activity type. If not assigned, then `0` is used. Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *in the *Amazon SWF Developer Guide* .* .

`--default-task-schedule-to-start-timeout` (string)

If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

`--default-task-schedule-to-close-timeout` (string)

If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

`--activity-version` (string)

The version of the activity type.

### Note

The activity type consists of the name and version, the combination of which must be unique within the domain.

The specified string must not contain a `:` (colon), `/` (slash), `|` (vertical bar), or any control characters (`\u0000-\u001f` | `\u007f-\u009f` ). Also, it must *not* be the literal string `arn` .

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

None