# get-managed-resourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/get-managed-resource.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/get-managed-resource.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [arc-zonal-shift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/arc-zonal-shift/index.html#cli-aws-arc-zonal-shift) ]

# get-managed-resource

## Description

Get information about a resource thatâs been registered for zonal shifts with Amazon Route 53 Application Recovery Controller in this Amazon Web Services Region. Resources that are registered for zonal shifts are managed resources in ARC. You can start zonal shifts and configure zonal autoshift for managed resources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/arc-zonal-shift-2022-10-30/GetManagedResource)

## Synopsis

```
get-managed-resource
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

`--resource-identifier` (string)

The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.

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

appliedWeights -> (map)

A collection of key-value pairs that indicate whether resources are active in Availability Zones or not. The key name is the Availability Zone where the resource is deployed. The value is 1 or 0.

key -> (string)

value -> (float)

arn -> (string)

The Amazon Resource Name (ARN) for the resource.

autoshifts -> (list)

An array of the autoshifts that are active for the resource.

(structure)

A complex structure that lists an autoshift that is currently active for a managed resource and information about the autoshift.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

appliedStatus -> (string)

The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED` . The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED` .

The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

awayFrom -> (string)

The Availability Zone (for example, `use1-az1` ) that traffic is shifted away from for a resource, when Amazon Web Services starts an autoshift. Until the autoshift ends, traffic for the resource is instead directed to other Availability Zones in the Amazon Web Services Region. An autoshift can end for a resource, for example, when Amazon Web Services ends the autoshift for the Availability Zone or when you disable zonal autoshift for the resource.

startTime -> (timestamp)

The time (UTC) when the autoshift started.

name -> (string)

The name of the resource.

practiceRunConfiguration -> (structure)

The practice run configuration for zonal autoshift thatâs associated with the resource.

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

The status for zonal autoshift for a resource. When the autoshift status is `ENABLED` , Amazon Web Services shifts traffic for a resource away from an Availability Zone, on your behalf, when Amazon Web Services determines that thereâs an issue in the Availability Zone that could potentially affect customers.

zonalShifts -> (list)

The zonal shifts that are currently active for a resource.

(structure)

A complex structure that lists the zonal shifts for a managed resource and their statuses for the resource.

appliedStatus -> (string)

The `appliedStatus` field specifies which application traffic shift is in effect for a resource when there is more than one active traffic shift. There can be more than one application traffic shift in progress at the same time - that is, practice run zonal shifts, customer-initiated zonal shifts, or an autoshift. The `appliedStatus` field for a shift that is in progress for a resource can have one of two values: `APPLIED` or `NOT_APPLIED` . The zonal shift or autoshift that is currently in effect for the resource has an `appliedStatus` set to `APPLIED` .

The overall principle for precedence is that zonal shifts that you start as a customer take precedence autoshifts, which take precedence over practice runs. That is, customer-initiated zonal shifts > autoshifts > practice run zonal shifts.

For more information, see [How zonal autoshift and practice runs work](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

awayFrom -> (string)

The Availability Zone (for example, `use1-az1` ) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.

comment -> (string)

A comment that you enter for a customer-initiated zonal shift. Only the latest comment is retained; no comment history is maintained. That is, a new comment overwrites any existing comment string.

expiryTime -> (timestamp)

The expiry time (expiration time) for a customer-initiated zonal shift. A zonal shift is temporary and must be set to expire when you start the zonal shift. You can initially set a zonal shift to expire in a maximum of three days (72 hours). However, you can update a zonal shift to set a new expiration at any time.

When you start a zonal shift, you specify how long you want it to be active, which ARC converts to an expiry time (expiration time). You can cancel a zonal shift when youâre ready to restore traffic to the Availability Zone, or just wait for it to expire. Or you can update the zonal shift to specify another length of time to expire in.

practiceRunOutcome -> (string)

The outcome, or end state, returned for a practice run. The following values can be returned:

- **PENDING:** Outcome value when a practice run is in progress.
- **SUCCEEDED:** Outcome value when the outcome alarm specified for the practice run configuration does not go into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed the expected 30 minute zonal shift.
- **INTERRUPTED:** Outcome value when the practice run was stopped before the expected 30 minute zonal shift duration, or there was another problem with the practice run that created an inconclusive outcome.
- **FAILED:** Outcome value when the outcome alarm specified for the practice run configuration goes into an `ALARM` state during the practice run, and the practice run was not interrupted before it completed.

For more information about practice run outcomes, see [Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.configure.html) in the Amazon Route 53 Application Recovery Controller Developer Guide.

resourceIdentifier -> (string)

The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.

At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.

shiftType -> (string)

Defines the zonal shift type.

startTime -> (timestamp)

The time (UTC) when the zonal shift starts.

zonalShiftId -> (string)

The identifier of a zonal shift.