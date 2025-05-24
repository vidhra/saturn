# create-practice-run-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/create-practice-run-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/create-practice-run-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [arc-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html#cli-aws-arc-zonal-shift) ]

# create-practice-run-configuration

## Description

A practice run configuration for zonal autoshift is required when you enable zonal autoshift. A practice run configuration includes specifications for blocked dates and blocked time windows, and for Amazon CloudWatch alarms that you create to use with practice runs. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting.

When a resource has a practice run configuration, ARC starts zonal shifts for the resource weekly, to shift traffic for practice runs. Practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.

For more information, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/arc-zonal-shift-2022-10-30/CreatePracticeRunConfiguration)

## Synopsis

```
create-practice-run-configuration
[--blocked-dates <value>]
[--blocked-windows <value>]
[--blocking-alarms <value>]
--outcome-alarms <value>
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

Optionally, you can block ARC from starting practice runs for a resource on specific calendar dates.

The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.

For example, if you have an application update scheduled to launch on May 1, 2024, and you donât want practice runs to shift traffic away at that time, you could set a blocked date for `2024-05-01` .

(string)

Syntax:

```
"string" "string" ...
```

`--blocked-windows` (list)

Optionally, you can block ARC from starting practice runs for specific windows of days and times.

The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.

For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: `MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30` .

(string)

Syntax:

```
"string" "string" ...
```

`--blocking-alarms` (list)

An Amazon CloudWatch alarm that you can specify for zonal autoshift practice runs. This alarm blocks ARC from starting practice run zonal shifts, and ends a practice run thatâs in progress, when the alarm is in an `ALARM` state.

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

The *outcome alarm* for practice runs is a required Amazon CloudWatch alarm that you specify that ends a practice run when the alarm is in an `ALARM` state.

Configure the alarm to monitor the health of your application when traffic is shifted away from an Availability Zone during each practice run. You should configure the alarm to go into an `ALARM` state if your application is impacted by the zonal shift, and you want to stop the zonal shift, to let traffic for the resource return to the Availability Zone.

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

The identifier of the resource that Amazon Web Services shifts traffic for with a practice run zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.

At this time, supported resources are Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.

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

The Amazon Resource Name (ARN) of the resource that you configured the practice run for.

name -> (string)

The name of the resource that you configured the practice run for.

practiceRunConfiguration -> (structure)

A practice run configuration for a resource. Configurations include the outcome alarm that you specify for practice runs, and, optionally, a blocking alarm and blocking dates and windows.

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

The status for zonal autoshift for a resource. When you specify `ENABLED` for the autoshift status, Amazon Web Services shifts traffic away from shifts away application resource traffic from an Availability Zone, on your behalf, when internal telemetry indicates that there is an Availability Zone impairment that could potentially impact customers.

When you enable zonal autoshift, you must also configure practice runs for the resource.