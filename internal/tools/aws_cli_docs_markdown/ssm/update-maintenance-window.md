# update-maintenance-windowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# update-maintenance-window

## Description

Updates an existing maintenance window. Only specified parameters are modified.

### Note

The value you specify for `Duration` determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for `Cutoff` . For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for `Cutoff` is one hour, no maintenance window tasks can start after 5 PM.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateMaintenanceWindow)

## Synopsis

```
update-maintenance-window
--window-id <value>
[--name <value>]
[--description <value>]
[--start-date <value>]
[--end-date <value>]
[--schedule <value>]
[--schedule-timezone <value>]
[--schedule-offset <value>]
[--duration <value>]
[--cutoff <value>]
[--allow-unassociated-targets | --no-allow-unassociated-targets]
[--enabled | --no-enabled]
[--replace | --no-replace]
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

`--window-id` (string)

The ID of the maintenance window to update.

`--name` (string)

The name of the maintenance window.

`--description` (string)

An optional description for the update request.

`--start-date` (string)

The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. `StartDate` allows you to delay activation of the maintenance window until the specified future date.

### Note

When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date.

`--end-date` (string)

The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. `EndDate` allows you to set a date and time in the future when the maintenance window will no longer run.

`--schedule` (string)

The schedule of the maintenance window in the form of a cron or rate expression.

`--schedule-timezone` (string)

The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: âAmerica/Los_Angelesâ, âUTCâ, or âAsia/Seoulâ. For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.

`--schedule-offset` (integer)

The number of days to wait after the date and time specified by a cron expression before running the maintenance window.

For example, the following cron expression schedules a maintenance window to run the third Tuesday of every month at 11:30 PM.

`cron(30 23 ? * TUE#3 *)`

If the schedule offset is `2` , the maintenance window wonât run until two days later.

`--duration` (integer)

The duration of the maintenance window in hours.

`--cutoff` (integer)

The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.

`--allow-unassociated-targets` | `--no-allow-unassociated-targets` (boolean)

Whether targets must be registered with the maintenance window before tasks can be defined for those targets.

`--enabled` | `--no-enabled` (boolean)

Whether the maintenance window is enabled.

`--replace` | `--no-replace` (boolean)

If `True` , then all fields that are required by the  CreateMaintenanceWindow operation are also required for this API request. Optional fields that arenât specified are set to null.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To update a maintenance window**

The following `update-maintenance-window` example updates the name of a maintenance window.

```
aws ssm update-maintenance-window \
    --window-id "mw-1a2b3c4d5e6f7g8h9" \
    --name "My-Renamed-MW"
```

Output:

```
{
    "Cutoff": 1,
    "Name": "My-Renamed-MW",
    "Schedule": "cron(0 16 ? * TUE *)",
    "Enabled": true,
    "AllowUnassociatedTargets": true,
    "WindowId": "mw-1a2b3c4d5e6f7g8h9",
    "Duration": 4
}
```

**Example 2: To disable a maintenance window**

The following `update-maintenance-window` example disables a maintenance window.

```
aws ssm update-maintenance-window \
    --window-id "mw-1a2b3c4d5e6f7g8h9" \
    --no-enabled
```

**Example 3: To enable a maintenance window**

The following `update-maintenance-window` example enables a maintenance window.

```
aws ssm update-maintenance-window \
    --window-id "mw-1a2b3c4d5e6f7g8h9" \
    --enabled
```

For more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html) in the *AWS Systems Manager User Guide*.

## Output

WindowId -> (string)

The ID of the created maintenance window.

Name -> (string)

The name of the maintenance window.

Description -> (string)

An optional description of the update.

StartDate -> (string)

The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become active. The maintenance window wonât run before this specified time.

EndDate -> (string)

The date and time, in ISO-8601 Extended format, for when the maintenance window is scheduled to become inactive. The maintenance window wonât run after this specified time.

Schedule -> (string)

The schedule of the maintenance window in the form of a cron or rate expression.

ScheduleTimezone -> (string)

The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: âAmerica/Los_Angelesâ, âUTCâ, or âAsia/Seoulâ. For more information, see the [Time Zone Database](https://www.iana.org/time-zones) on the IANA website.

ScheduleOffset -> (integer)

The number of days to wait to run a maintenance window after the scheduled cron expression date and time.

Duration -> (integer)

The duration of the maintenance window in hours.

Cutoff -> (integer)

The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.

AllowUnassociatedTargets -> (boolean)

Whether targets must be registered with the maintenance window before tasks can be defined for those targets.

Enabled -> (boolean)

Whether the maintenance window is enabled.