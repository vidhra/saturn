# describe-activity-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [swf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html#cli-aws-swf) ]

# describe-activity-type

## Description

Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.

**Access Control**

You can use IAM policies to control this actionâs access to Amazon SWF resources as follows:

- Use a `Resource` element with the domain name to limit the action to only specified domains.
- Use an `Action` element to allow or deny permission to call this action.
- Constrain the following parameters by using a `Condition` element with the appropriate keys.
- `activityType.name` : String constraint. The key is `swf:activityType.name` .
- `activityType.version` : String constraint. The key is `swf:activityType.version` .

If the caller doesnât have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attributeâs `cause` parameter is set to `OPERATION_NOT_PERMITTED` . For details and example IAM policies, see [Using IAM to Manage Access to Amazon SWF Workflows](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) in the *Amazon SWF Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/swf-2012-01-25/DescribeActivityType)

## Synopsis

```
describe-activity-type
--domain <value>
--activity-type <value>
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

The name of the domain in which the activity type is registered.

`--activity-type` (structure)

The activity type to get information about. Activity types are identified by the `name` and `version` that were supplied when the activity was registered.

name -> (string)

The name of this activity.

### Note

The combination of activity type name and version must be unique within a domain.

version -> (string)

The version of this activity.

### Note

The combination of activity type name and version must be unique with in a domain.

Shorthand Syntax:

```
name=string,version=string
```

JSON Syntax:

```
{
  "name": "string",
  "version": "string"
}
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

typeInfo -> (structure)

General information about the activity type.

The status of activity type (returned in the ActivityTypeInfo structure) can be one of the following.

- `REGISTERED` â The type is registered and available. Workers supporting this type should be running.
- `DEPRECATED` â The type was deprecated using  DeprecateActivityType , but is still in use. You should keep workers supporting this type running. You cannot create new tasks of this type.

activityType -> (structure)

The  ActivityType type structure representing the activity type.

name -> (string)

The name of this activity.

### Note

The combination of activity type name and version must be unique within a domain.

version -> (string)

The version of this activity.

### Note

The combination of activity type name and version must be unique with in a domain.

status -> (string)

The current status of the activity type.

description -> (string)

The description of the activity type provided in  RegisterActivityType .

creationDate -> (timestamp)

The date and time this activity type was created through  RegisterActivityType .

deprecationDate -> (timestamp)

If DEPRECATED, the date and time  DeprecateActivityType was called.

configuration -> (structure)

The configuration settings registered with the activity type.

defaultTaskStartToCloseTimeout -> (string)

The default maximum duration for tasks of an activity type specified when registering the activity type. You can override this default when scheduling a task through the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

defaultTaskHeartbeatTimeout -> (string)

The default maximum time, in seconds, before which a worker processing a task must report progress by calling  RecordActivityTaskHeartbeat .

You can specify this value only when *registering* an activity type. The registered default value can be overridden when you schedule a task through the `ScheduleActivityTask`   Decision . If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an `UnknownResource` fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

defaultTaskList -> (structure)

The default task list specified for this activity type at registration. This default is used if a task list isnât provided when a task is scheduled through the `ScheduleActivityTask`   Decision . You can override the default registered task list when scheduling a task through the `ScheduleActivityTask`   Decision .

name -> (string)

The name of the task list.

defaultTaskPriority -> (string)

The default task priority for tasks of this activity type, specified at registration. If not set, then `0` is used as the default priority. This default can be overridden when scheduling an activity task.

Valid values are integers that range from Javaâs `Integer.MIN_VALUE` (-2147483648) to `Integer.MAX_VALUE` (2147483647). Higher numbers indicate higher priority.

For more information about setting task priority, see [Setting Task Priority](https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html) in the *Amazon SWF Developer Guide* .

defaultTaskScheduleToStartTimeout -> (string)

The default maximum duration, specified when registering the activity type, that a task of an activity type can wait before being assigned to a worker. You can override this default when scheduling a task through the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.

defaultTaskScheduleToCloseTimeout -> (string)

The default maximum duration, specified when registering the activity type, for tasks of this activity type. You can override this default when scheduling a task through the `ScheduleActivityTask`   Decision .

The duration is specified in seconds, an integer greater than or equal to `0` . You can use `NONE` to specify unlimited duration.