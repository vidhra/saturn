# describe-scheduled-instance-availabilityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instance-availability.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instance-availability.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-scheduled-instance-availability

## Description

Finds available schedules that meet the specified criteria.

You can search for an available schedule no more than 3 months in advance. You must meet the minimum required duration of 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.

After you find a schedule that meets your needs, call  PurchaseScheduledInstances to purchase Scheduled Instances with that schedule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeScheduledInstanceAvailability)

`describe-scheduled-instance-availability` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ScheduledInstanceAvailabilitySet`

## Synopsis

```
describe-scheduled-instance-availability
[--dry-run | --no-dry-run]
[--filters <value>]
--first-slot-start-time-range <value>
[--max-slot-duration-in-hours <value>]
[--min-slot-duration-in-hours <value>]
--recurrence <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters.

- `availability-zone` - The Availability Zone (for example, `us-west-2a` ).
- `instance-type` - The instance type (for example, `c4.large` ).
- `platform` - The platform (`Linux/UNIX` or `Windows` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--first-slot-start-time-range` (structure)

The time period for the first schedule to start.

EarliestTime -> (timestamp)

The earliest date and time, in UTC, for the Scheduled Instance to start.

LatestTime -> (timestamp)

The latest date and time, in UTC, for the Scheduled Instance to start. This value must be later than or equal to the earliest date and at most three months in the future.

Shorthand Syntax:

```
EarliestTime=timestamp,LatestTime=timestamp
```

JSON Syntax:

```
{
  "EarliestTime": timestamp,
  "LatestTime": timestamp
}
```

`--max-slot-duration-in-hours` (integer)

The maximum available duration, in hours. This value must be greater than `MinSlotDurationInHours` and less than 1,720.

`--min-slot-duration-in-hours` (integer)

The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.

`--recurrence` (structure)

The schedule recurrence.

Frequency -> (string)

The frequency (`Daily` , `Weekly` , or `Monthly` ).

Interval -> (integer)

The interval quantity. The interval unit depends on the value of `Frequency` . For example, every 2 weeks or every 2 months.

OccurrenceDays -> (list)

The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You canât specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.

(integer)

OccurrenceRelativeToEnd -> (boolean)

Indicates whether the occurrence is relative to the end of the specified week or month. You canât specify this value with a daily schedule.

OccurrenceUnit -> (string)

The unit for `OccurrenceDays` (`DayOfWeek` or `DayOfMonth` ). This value is required for a monthly schedule. You canât specify `DayOfWeek` with a weekly schedule. You canât specify this value with a daily schedule.

Shorthand Syntax:

```
Frequency=string,Interval=integer,OccurrenceDays=integer,integer,OccurrenceRelativeToEnd=boolean,OccurrenceUnit=string
```

JSON Syntax:

```
{
  "Frequency": "string",
  "Interval": integer,
  "OccurrenceDays": [integer, ...],
  "OccurrenceRelativeToEnd": true|false,
  "OccurrenceUnit": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To describe an available schedule**

This example describes a schedule that occurs every week on Sunday, starting on the specified date.

Command:

```
aws ec2 describe-scheduled-instance-availability --recurrence Frequency=Weekly,Interval=1,OccurrenceDays=[1] --first-slot-start-time-range EarliestTime=2016-01-31T00:00:00Z,LatestTime=2016-01-31T04:00:00Z
```

Output:

```
{
  "ScheduledInstanceAvailabilitySet": [
    {
        "AvailabilityZone": "us-west-2b",
        "TotalScheduledInstanceHours": 1219,
        "PurchaseToken": "eyJ2IjoiMSIsInMiOjEsImMiOi...",
        "MinTermDurationInDays": 366,
        "AvailableInstanceCount": 20,
        "Recurrence": {
            "OccurrenceDaySet": [
                1
            ],
            "Interval": 1,
            "Frequency": "Weekly",
            "OccurrenceRelativeToEnd": false
        },
        "Platform": "Linux/UNIX",
        "FirstSlotStartTime": "2016-01-31T00:00:00Z",
        "MaxTermDurationInDays": 366,
        "SlotDurationInHours": 23,
        "NetworkPlatform": "EC2-VPC",
        "InstanceType": "c4.large",
        "HourlyPrice": "0.095"
    },
    ...
  ]
}
```

To narrow the results, you can add filters that specify the operating system, network, and instance type.

Command:

âfilters Name=platform,Values=Linux/UNIX Name=network-platform,Values=EC2-VPC Name=instance-type,Values=c4.large

## Output

NextToken -> (string)

The token required to retrieve the next set of results. This value is `null` when there are no more results to return.

ScheduledInstanceAvailabilitySet -> (list)

Information about the available Scheduled Instances.

(structure)

Describes a schedule that is available for your Scheduled Instances.

AvailabilityZone -> (string)

The Availability Zone.

AvailableInstanceCount -> (integer)

The number of available instances.

FirstSlotStartTime -> (timestamp)

The time period for the first schedule to start.

HourlyPrice -> (string)

The hourly price for a single instance.

InstanceType -> (string)

The instance type. You can specify one of the C3, C4, M4, or R3 instance types.

MaxTermDurationInDays -> (integer)

The maximum term. The only possible value is 365 days.

MinTermDurationInDays -> (integer)

The minimum term. The only possible value is 365 days.

NetworkPlatform -> (string)

The network platform.

Platform -> (string)

The platform (`Linux/UNIX` or `Windows` ).

PurchaseToken -> (string)

The purchase token. This token expires in two hours.

Recurrence -> (structure)

The schedule recurrence.

Frequency -> (string)

The frequency (`Daily` , `Weekly` , or `Monthly` ).

Interval -> (integer)

The interval quantity. The interval unit depends on the value of `frequency` . For example, every 2 weeks or every 2 months.

OccurrenceDaySet -> (list)

The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).

(integer)

OccurrenceRelativeToEnd -> (boolean)

Indicates whether the occurrence is relative to the end of the specified week or month.

OccurrenceUnit -> (string)

The unit for `occurrenceDaySet` (`DayOfWeek` or `DayOfMonth` ).

SlotDurationInHours -> (integer)

The number of hours in the schedule.

TotalScheduledInstanceHours -> (integer)

The total number of hours for a single instance for the entire term.