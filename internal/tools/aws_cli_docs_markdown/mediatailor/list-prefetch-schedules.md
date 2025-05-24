# list-prefetch-schedulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-prefetch-schedules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-prefetch-schedules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# list-prefetch-schedules

## Description

Lists the prefetch schedules for a playback configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListPrefetchSchedules)

`list-prefetch-schedules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-prefetch-schedules
--playback-configuration-name <value>
[--schedule-type <value>]
[--stream-id <value>]
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

`--playback-configuration-name` (string)

Retrieves the prefetch schedule(s) for a specific playback configuration.

`--schedule-type` (string)

The type of prefetch schedules that you want to list. `SINGLE` indicates that you want to list the configured single prefetch schedules. `RECURRING` indicates that you want to list the configured recurring prefetch schedules. `ALL` indicates that you want to list all configured prefetch schedules.

Possible values:

- `SINGLE`
- `RECURRING`
- `ALL`

`--stream-id` (string)

An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.

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

Items -> (list)

Lists the prefetch schedules. An empty `Items` list doesnât mean there arenât more items to fetch, just that that page was empty.

(structure)

A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide* .

Arn -> (string)

The Amazon Resource Name (ARN) of the prefetch schedule.

Consumption -> (structure)

Consumption settings determine how, and when, MediaTailor places the prefetched ads into ad breaks for single prefetch schedules. Ad consumption occurs within a span of time that you define, called a *consumption window* . You can designate which ad breaks that MediaTailor fills with prefetch ads by setting avail matching criteria.

AvailMatchingCriteria -> (list)

If you only want MediaTailor to insert prefetched ads into avails (ad breaks) that match specific dynamic variables, such as `scte.event_id` , set the avail matching criteria.

(structure)

MediaTailor only places (consumes) prefetched ads if the ad break meets the criteria defined by the dynamic variables. This gives you granular control over which ad break to place the prefetched ads into.

As an example, letâs say that you set `DynamicVariable` to `scte.event_id` and `Operator` to `EQUALS` , and your playback configuration has an ADS URL of `https://my.ads.server.com/path?&podId=[scte.avail_num]&event=[scte.event_id]&duration=[session.avail_duration_secs]` . And the prefetch request to the ADS contains these values `https://my.ads.server.com/path?&podId=3&event=my-awesome-event&duration=30` . MediaTailor will only insert the prefetched ads into the ad break if has a SCTE marker with an event id of `my-awesome-event` , since it must match the event id that MediaTailor uses to query the ADS.

You can specify up to five `AvailMatchingCriteria` . If you specify multiple `AvailMatchingCriteria` , MediaTailor combines them to match using a logical `AND` . You can model logical `OR` combinations by creating multiple prefetch schedules.

DynamicVariable -> (string)

The dynamic variable(s) that MediaTailor should use as avail matching criteria. MediaTailor only places the prefetched ads into the avail if the avail matches the criteria defined by the dynamic variable. For information about dynamic variables, see [Using dynamic ad variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) in the *MediaTailor User Guide* .

You can include up to 100 dynamic variables.

Operator -> (string)

For the `DynamicVariable` specified in `AvailMatchingCriteria` , the Operator that is used for the comparison.

EndTime -> (timestamp)

The time when MediaTailor no longer considers the prefetched ads for use in an ad break. MediaTailor automatically deletes prefetch schedules no less than seven days after the end time. If youâd like to manually delete the prefetch schedule, you can call `DeletePrefetchSchedule` .

StartTime -> (timestamp)

The time when prefetched ads are considered for use in an ad break. If you donât specify `StartTime` , the prefetched ads are available after MediaTailor retrieves them from the ad decision server.

Name -> (string)

The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.

PlaybackConfigurationName -> (string)

The name of the playback configuration to create the prefetch schedule for.

Retrieval -> (structure)

A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).

DynamicVariables -> (map)

The dynamic variables to use for substitution during prefetch requests to the ad decision server (ADS).

You initially configure [dynamic variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) for the ADS URL when you set up your playback configuration. When you specify `DynamicVariables` for prefetch retrieval, MediaTailor includes the dynamic variables in the request to the ADS.

key -> (string)

value -> (string)

EndTime -> (timestamp)

The time when prefetch retrieval ends for the ad break. Prefetching will be attempted for manifest requests that occur at or before this time.

StartTime -> (timestamp)

The time when prefetch retrievals can start for this break. Ad prefetching will be attempted for manifest requests that occur at or after this time. Defaults to the current time. If not specified, the prefetch retrieval starts as soon as possible.

TrafficShapingType -> (string)

Indicates if this configuration uses a retrieval window for traffic shaping and limiting the number of requests to the ADS at one time.

TrafficShapingRetrievalWindow -> (structure)

Configuration for spreading ADS traffic across a set window instead of sending ADS requests for all sessions at the same time.

RetrievalWindowDurationSeconds -> (integer)

The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.

ScheduleType -> (string)

The frequency that MediaTailor creates prefetch schedules. `SINGLE` indicates that this schedule applies to one ad break. `RECURRING` indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.

For more information about the prefetch types and when you might use each, see [Prefetching ads in Elemental MediaTailor.](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html)

RecurringPrefetchConfiguration -> (structure)

The settings that determine how and when MediaTailor prefetches ads and inserts them into ad breaks.

StartTime -> (timestamp)

The start time for the window that MediaTailor prefetches and inserts ads in a live event.

EndTime -> (timestamp)

The end time for the window that MediaTailor prefetches and inserts ads in a live event.

RecurringConsumption -> (structure)

The settings that determine how and when MediaTailor places prefetched ads into upcoming ad breaks for recurring prefetch scedules.

RetrievedAdExpirationSeconds -> (integer)

The number of seconds that an ad is available for insertion after it was prefetched.

AvailMatchingCriteria -> (list)

The configuration for the dynamic variables that determine which ad breaks that MediaTailor inserts prefetched ads in.

(structure)

MediaTailor only places (consumes) prefetched ads if the ad break meets the criteria defined by the dynamic variables. This gives you granular control over which ad break to place the prefetched ads into.

As an example, letâs say that you set `DynamicVariable` to `scte.event_id` and `Operator` to `EQUALS` , and your playback configuration has an ADS URL of `https://my.ads.server.com/path?&podId=[scte.avail_num]&event=[scte.event_id]&duration=[session.avail_duration_secs]` . And the prefetch request to the ADS contains these values `https://my.ads.server.com/path?&podId=3&event=my-awesome-event&duration=30` . MediaTailor will only insert the prefetched ads into the ad break if has a SCTE marker with an event id of `my-awesome-event` , since it must match the event id that MediaTailor uses to query the ADS.

You can specify up to five `AvailMatchingCriteria` . If you specify multiple `AvailMatchingCriteria` , MediaTailor combines them to match using a logical `AND` . You can model logical `OR` combinations by creating multiple prefetch schedules.

DynamicVariable -> (string)

The dynamic variable(s) that MediaTailor should use as avail matching criteria. MediaTailor only places the prefetched ads into the avail if the avail matches the criteria defined by the dynamic variable. For information about dynamic variables, see [Using dynamic ad variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) in the *MediaTailor User Guide* .

You can include up to 100 dynamic variables.

Operator -> (string)

For the `DynamicVariable` specified in `AvailMatchingCriteria` , the Operator that is used for the comparison.

RecurringRetrieval -> (structure)

The configuration for prefetch ad retrieval from the ADS.

DynamicVariables -> (map)

The dynamic variables to use for substitution during prefetch requests to the ADS.

key -> (string)

value -> (string)

DelayAfterAvailEndSeconds -> (integer)

The number of seconds that MediaTailor waits after an ad avail before prefetching ads for the next avail. If not set, the default is 0 (no delay).

TrafficShapingType -> (string)

Indicates if this configuration uses a retrieval window for traffic shaping and limiting the number of requests to the ADS at one time.

TrafficShapingRetrievalWindow -> (structure)

Configuration for spreading ADS traffic across a set window instead of sending ADS requests for all sessions at the same time.

RetrievalWindowDurationSeconds -> (integer)

The amount of time, in seconds, that MediaTailor spreads prefetch requests to the ADS.

StreamId -> (string)

An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.

NextToken -> (string)

Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.