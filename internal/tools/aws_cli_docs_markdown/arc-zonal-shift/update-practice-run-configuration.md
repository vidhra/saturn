# update-practice-run-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-practice-run-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/update-practice-run-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [arc-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html#cli-aws-arc-zonal-shift) ]

# update-practice-run-configuration

## Description

Update a practice run configuration to change one or more of the following: add, change, or remove the blocking alarm; change the outcome alarm; or add, change, or remove blocking dates or time windows.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/arc-zonal-shift-2022-10-30/UpdatePracticeRunConfiguration)

## Synopsis

```
update-practice-run-configuration
[--blocked-dates <value>]
[--blocked-windows <value>]
[--blocking-alarms <value>]
[--outcome-alarms <value>]
--resource-identifier <value>
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

`--blocked-dates` (list)

Add, change, or remove blocked dates for a practice run in zonal autoshift.

Optionally, you can block practice runs for specific calendar dates. The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.

For example, if you have an application update scheduled to launch on May 1, 2024, and you donât want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01` .

(string)

Syntax:

```
"string" "string" ...
```

`--blocked-windows` (list)

Add, change, or remove windows of days and times for when you can, optionally, block ARC from starting a practice run for a resource.

The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.

For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30` .

(string)

Syntax:

```
"string" "string" ...
```

`--blocking-alarms` (list)

Add, change, or remove the Amazon CloudWatch alarm that you optionally specify as the blocking alarm for practice runs.

(structure)

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

alarmIdentifier -> (string)

The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.

type -> (string)

The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH` .

Shorthand Syntax:

```
alarmIdentifier=string,type=string ...
```

JSON Syntax:

```
[
  {
    "alarmIdentifier": "string",
    "type": "CLOUDWATCH"
  }
  ...
]
```

`--outcome-alarms` (list)

Specify a new the Amazon CloudWatch alarm as the outcome alarm for practice runs.

(structure)

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

alarmIdentifier -> (string)

The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.

type -> (string)

The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH` .

Shorthand Syntax:

```
alarmIdentifier=string,type=string ...
```

JSON Syntax:

```
[
  {
    "alarmIdentifier": "string",
    "type": "CLOUDWATCH"
  }
  ...
]
```

`--resource-identifier` (string)

The identifier for the resource that you want to update the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.

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

arn -> (string)

The Amazon Resource Name (ARN) of the resource that you updated the practice run for.

name -> (string)

The name of the resource that you updated the practice run for.

practiceRunConfiguration -> (structure)

The practice run configuration that was updated.

blockedDates -> (list)

An array of one or more dates that you can specify when Amazon Web Services does not start practice runs for a resource.

Specify blocked dates, in UTC, in the format `YYYY-MM-DD` , separated by spaces.

(string)

blockedWindows -> (list)

An array of one or more windows of days and times that you can block ARC from starting practice runs for a resource.

Specify the blocked windows in UTC, using the format `DAY:HH:MM-DAY:HH:MM` , separated by spaces. For example, `MON:18:30-MON:19:30 TUE:18:30-TUE:19:30` .

(string)

blockingAlarms -> (list)

The *blocking alarm* for practice runs is an optional alarm that you can specify that blocks practice runs when the alarm is in an `ALARM` state.

(structure)

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

alarmIdentifier -> (string)

The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.

type -> (string)

The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH` .

outcomeAlarms -> (list)

The *outcome alarm* for practice runs is an alarm that you specify that ends a practice run when the alarm is in an `ALARM` state.

(structure)

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

alarmIdentifier -> (string)

The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.

type -> (string)

The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH` .

zonalAutoshiftStatus -> (string)

The zonal autoshift status for the resource that you updated the practice run for.