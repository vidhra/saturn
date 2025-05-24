# list-preview-rotation-shiftsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-preview-rotation-shifts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-preview-rotation-shifts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-contacts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/index.html#cli-aws-ssm-contacts) ]

# list-preview-rotation-shifts

## Description

Returns a list of shifts based on rotation configuration parameters.

### Note

The Incident Manager primarily uses this operation to populate the **Preview** calendar. It is not typically run by end users.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-contacts-2021-05-03/ListPreviewRotationShifts)

`list-preview-rotation-shifts` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `RotationShifts`

## Synopsis

```
list-preview-rotation-shifts
[--rotation-start-time <value>]
[--start-time <value>]
--end-time <value>
--members <value>
--time-zone-id <value>
--recurrence <value>
[--overrides <value>]
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

`--rotation-start-time` (timestamp)

The date and time a rotation would begin. The first shift is calculated from this date and time.

`--start-time` (timestamp)

Used to filter the range of calculated shifts before sending the response back to the user.

`--end-time` (timestamp)

The date and time a rotation shift would end.

`--members` (list)

The contacts that would be assigned to a rotation.

(string)

Syntax:

```
"string" "string" ...
```

`--time-zone-id` (string)

The time zone the rotationâs activity would be based on, in Internet Assigned Numbers Authority (IANA) format. For example: âAmerica/Los_Angelesâ, âUTCâ, or âAsia/Seoulâ.

`--recurrence` (structure)

Information about how long a rotation would last before restarting at the beginning of the shift order.

MonthlySettings -> (list)

Information about on-call rotations that recur monthly.

(structure)

Information about on-call rotations that recur monthly.

DayOfMonth -> (integer)

The day of the month when monthly recurring on-call rotations begin.

HandOffTime -> (structure)

The time of day when a monthly recurring on-call shift rotation begins.

HourOfDay -> (integer)

The hour when an on-call rotation shift begins or ends.

MinuteOfHour -> (integer)

The minute when an on-call rotation shift begins or ends.

WeeklySettings -> (list)

Information about on-call rotations that recur weekly.

(structure)

Information about rotations that recur weekly.

DayOfWeek -> (string)

The day of the week when weekly recurring on-call shift rotations begins.

HandOffTime -> (structure)

The time of day when a weekly recurring on-call shift rotation begins.

HourOfDay -> (integer)

The hour when an on-call rotation shift begins or ends.

MinuteOfHour -> (integer)

The minute when an on-call rotation shift begins or ends.

DailySettings -> (list)

Information about on-call rotations that recur daily.

(structure)

Details about when an on-call rotation shift begins or ends.

HourOfDay -> (integer)

The hour when an on-call rotation shift begins or ends.

MinuteOfHour -> (integer)

The minute when an on-call rotation shift begins or ends.

NumberOfOnCalls -> (integer)

The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule containing ten contacts, a value of `2` designates that two of them are on call at any given time.

ShiftCoverages -> (map)

Information about the days of the week included in on-call rotation coverage.

key -> (string)

value -> (list)

(structure)

Information about when an on-call shift begins and ends.

Start -> (structure)

Information about when the on-call rotation shift begins.

HourOfDay -> (integer)

The hour when an on-call rotation shift begins or ends.

MinuteOfHour -> (integer)

The minute when an on-call rotation shift begins or ends.

End -> (structure)

Information about when the on-call rotation shift ends.

HourOfDay -> (integer)

The hour when an on-call rotation shift begins or ends.

MinuteOfHour -> (integer)

The minute when an on-call rotation shift begins or ends.

RecurrenceMultiplier -> (integer)

The number of days, weeks, or months a single rotation lasts.

JSON Syntax:

```
{
  "MonthlySettings": [
    {
      "DayOfMonth": integer,
      "HandOffTime": {
        "HourOfDay": integer,
        "MinuteOfHour": integer
      }
    }
    ...
  ],
  "WeeklySettings": [
    {
      "DayOfWeek": "MON"|"TUE"|"WED"|"THU"|"FRI"|"SAT"|"SUN",
      "HandOffTime": {
        "HourOfDay": integer,
        "MinuteOfHour": integer
      }
    }
    ...
  ],
  "DailySettings": [
    {
      "HourOfDay": integer,
      "MinuteOfHour": integer
    }
    ...
  ],
  "NumberOfOnCalls": integer,
  "ShiftCoverages": {"MON"|"TUE"|"WED"|"THU"|"FRI"|"SAT"|"SUN": [
        {
          "Start": {
            "HourOfDay": integer,
            "MinuteOfHour": integer
          },
          "End": {
            "HourOfDay": integer,
            "MinuteOfHour": integer
          }
        }
        ...
      ]
    ...},
  "RecurrenceMultiplier": integer
}
```

`--overrides` (list)

Information about changes that would be made in a rotation override.

(structure)

Information about contacts and times that an on-call override replaces.

NewMembers -> (list)

Information about contacts to add to an on-call rotation override.

(string)

StartTime -> (timestamp)

Information about the time a rotation override would begin.

EndTime -> (timestamp)

Information about the time a rotation override would end.

Shorthand Syntax:

```
NewMembers=string,string,StartTime=timestamp,EndTime=timestamp ...
```

JSON Syntax:

```
[
  {
    "NewMembers": ["string", ...],
    "StartTime": timestamp,
    "EndTime": timestamp
  }
  ...
]
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

## Output

RotationShifts -> (list)

Details about a rotation shift, including times, types, and contacts.

(structure)

Information about a shift that belongs to an on-call rotation.

ContactIds -> (list)

The Amazon Resource Names (ARNs) of the contacts who are part of the shift rotation.

(string)

StartTime -> (timestamp)

The time a shift rotation begins.

EndTime -> (timestamp)

The time a shift rotation ends.

Type -> (string)

The type of shift rotation.

ShiftDetails -> (structure)

Additional information about an on-call rotation shift.

OverriddenContactIds -> (list)

The Amazon Resources Names (ARNs) of the contacts who were replaced in a shift when an override was created. If the override is deleted, these contacts are restored to the shift.

(string)

NextToken -> (string)

The token for the next set of items to return. This token is used to get the next set of results.