# list-internet-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-internet-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-internet-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [internetmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html#cli-aws-internetmonitor) ]

# list-internet-events

## Description

Lists internet events that cause performance or availability issues for client locations. Amazon CloudWatch Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers.

You can constrain the list of internet events returned by providing a start time and end time to define a total time frame for events you want to list. Both start time and end time specify the time when an event started. End time is optional. If you donât include it, the default end time is the current time.

You can also limit the events returned to a specific status (`ACTIVE` or `RESOLVED` ) or type (`PERFORMANCE` or `AVAILABILITY` ).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/internetmonitor-2021-06-03/ListInternetEvents)

`list-internet-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InternetEvents`

## Synopsis

```
list-internet-events
[--start-time <value>]
[--end-time <value>]
[--event-status <value>]
[--event-type <value>]
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

`--start-time` (timestamp)

The start time of the time window that you want to get a list of internet events for.

`--end-time` (timestamp)

The end time of the time window that you want to get a list of internet events for.

`--event-status` (string)

The status of an internet event.

`--event-type` (string)

The type of network impairment.

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

InternetEvents -> (list)

A set of internet events returned for the list operation.

(structure)

A summary of information about an internet event in Amazon CloudWatch Internet Monitor. Internet events are issues that cause performance degradation or availability problems for impacted Amazon Web Services client locations. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers.

EventId -> (string)

The internally-generated identifier of an internet event.

EventArn -> (string)

The Amazon Resource Name (ARN) of the internet event.

StartedAt -> (timestamp)

The time when an internet event started.

EndedAt -> (timestamp)

The time when an internet event ended. If the event hasnât ended yet, this value is empty.

ClientLocation -> (structure)

The impacted location, such as a city, that Amazon Web Services clients access application resources from.

ASName -> (string)

The name of the internet service provider (ISP) or network (ASN).

ASNumber -> (long)

The Autonomous System Number (ASN) of the network at an impacted location.

Country -> (string)

The name of the country where the internet event is located.

Subdivision -> (string)

The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).

Metro -> (string)

The metro area where the health event is located.

Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.

City -> (string)

The name of the city where the internet event is located.

Latitude -> (double)

The latitude where the internet event is located.

Longitude -> (double)

The longitude where the internet event is located.

EventType -> (string)

The type of network impairment.

EventStatus -> (string)

The status of an internet event.

NextToken -> (string)

The token for the next set of results. You receive this token from a previous call.