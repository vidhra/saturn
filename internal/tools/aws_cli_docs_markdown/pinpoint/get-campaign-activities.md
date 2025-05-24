# get-campaign-activitiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaign-activities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaign-activities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# get-campaign-activities

## Description

Retrieves information about all the activities for a campaign.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/GetCampaignActivities)

## Synopsis

```
get-campaign-activities
--application-id <value>
--campaign-id <value>
[--page-size <value>]
[--token <value>]
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--campaign-id` (string)

The unique identifier for the campaign.

`--page-size` (string)

The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.

`--token` (string)

The NextToken string that specifies which page of results to return in a paginated response.

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

ActivitiesResponse -> (structure)

Provides information about the activities that were performed by a campaign.

Item -> (list)

An array of responses, one for each activity that was performed by the campaign.

(structure)

Provides information about an activity that was performed by a campaign.

ApplicationId -> (string)

The unique identifier for the application that the campaign applies to.

CampaignId -> (string)

The unique identifier for the campaign that the activity applies to.

End -> (string)

The actual time, in ISO 8601 format, when the activity was marked CANCELLED or COMPLETED.

Id -> (string)

The unique identifier for the activity.

Result -> (string)

Specifies whether the activity succeeded. Possible values are SUCCESS and FAIL.

ScheduledStart -> (string)

The scheduled start time, in ISO 8601 format, for the activity.

Start -> (string)

The actual start time, in ISO 8601 format, of the activity.

State -> (string)

The current status of the activity. Possible values are: PENDING, INITIALIZING, RUNNING, PAUSED, CANCELLED, and COMPLETED.

SuccessfulEndpointCount -> (integer)

The total number of endpoints that the campaign successfully delivered messages to.

TimezonesCompletedCount -> (integer)

The total number of time zones that were completed.

TimezonesTotalCount -> (integer)

The total number of unique time zones that are in the segment for the campaign.

TotalEndpointCount -> (integer)

The total number of endpoints that the campaign attempted to deliver messages to.

TreatmentId -> (string)

The unique identifier for the campaign treatment that the activity applies to. A treatment is a variation of a campaign thatâs used for A/B testing of a campaign.

ExecutionMetrics -> (map)

A JSON object that contains metrics relating to the campaign execution for this campaign activity. For information about the structure and contents of the results, see [Standard Amazon Pinpoint analytics metrics](https://docs.aws.amazon.com//pinpoint/latest/developerguide/analytics-standard-metrics.html) in the *Amazon Pinpoint Developer Guide* .

key -> (string)

value -> (string)

NextToken -> (string)

The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages.