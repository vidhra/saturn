# list-contactsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-contacts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-contacts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [groundstation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/index.html#cli-aws-groundstation) ]

# list-contacts

## Description

Returns a list of contacts.

If `statusList` contains AVAILABLE, the request must include `groundStation` , `missionprofileArn` , and `satelliteArn` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/ListContacts)

`list-contacts` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `contactList`

## Synopsis

```
list-contacts
--end-time <value>
[--ground-station <value>]
[--mission-profile-arn <value>]
[--satellite-arn <value>]
--start-time <value>
--status-list <value>
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

`--end-time` (timestamp)

End time of a contact in UTC.

`--ground-station` (string)

Name of a ground station.

`--mission-profile-arn` (string)

ARN of a mission profile.

`--satellite-arn` (string)

ARN of a satellite.

`--start-time` (timestamp)

Start time of a contact in UTC.

`--status-list` (list)

Status of a contact reservation.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  SCHEDULING
  FAILED_TO_SCHEDULE
  SCHEDULED
  CANCELLED
  AWS_CANCELLED
  PREPASS
  PASS
  POSTPASS
  COMPLETED
  FAILED
  AVAILABLE
  CANCELLING
  AWS_FAILED
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

contactList -> (list)

List of contacts.

(structure)

Data describing a contact.

contactId -> (string)

UUID of a contact.

contactStatus -> (string)

Status of a contact.

endTime -> (timestamp)

End time of a contact in UTC.

errorMessage -> (string)

Error message of a contact.

groundStation -> (string)

Name of a ground station.

maximumElevation -> (structure)

Maximum elevation angle of a contact.

unit -> (string)

Elevation angle units.

value -> (double)

Elevation angle value.

missionProfileArn -> (string)

ARN of a mission profile.

postPassEndTime -> (timestamp)

Amount of time after a contact ends that youâd like to receive a CloudWatch event indicating the pass has finished.

prePassStartTime -> (timestamp)

Amount of time prior to contact start youâd like to receive a CloudWatch event indicating an upcoming pass.

region -> (string)

Region of a contact.

satelliteArn -> (string)

ARN of a satellite.

startTime -> (timestamp)

Start time of a contact in UTC.

tags -> (map)

Tags assigned to a contact.

key -> (string)

value -> (string)

visibilityEndTime -> (timestamp)

Projected time in UTC your satellite will set below the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html) . This time is based on the satelliteâs current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. *This field is not present for contacts with a ``SCHEDULING`` or ``SCHEDULED`` status.*

visibilityStartTime -> (timestamp)

Projected time in UTC your satellite will rise above the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html) . This time is based on the satelliteâs current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts. *This field is not present for contacts with a ``SCHEDULING`` or ``SCHEDULED`` status.*

nextToken -> (string)

Next token returned in the response of a previous `ListContacts` call. Used to get the next page of results.