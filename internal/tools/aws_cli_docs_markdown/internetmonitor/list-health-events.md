# list-health-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-health-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/list-health-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [internetmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html#cli-aws-internetmonitor) ]

# list-health-events

## Description

Lists all health events for a monitor in Amazon CloudWatch Internet Monitor. Returns information for health events including the event start and end times, and the status.

### Note

Health events that have start times during the time frame that is requested are not included in the list of health events.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/internetmonitor-2021-06-03/ListHealthEvents)

`list-health-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `HealthEvents`

## Synopsis

```
list-health-events
--monitor-name <value>
[--start-time <value>]
[--end-time <value>]
[--event-status <value>]
[--linked-account-id <value>]
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

`--monitor-name` (string)

The name of the monitor.

`--start-time` (timestamp)

The time when a health event started.

`--end-time` (timestamp)

The time when a health event ended. If the health event is still ongoing, then the end time is not set.

`--event-status` (string)

The status of a health event.

Possible values:

- `ACTIVE`
- `RESOLVED`

`--linked-account-id` (string)

The account ID for an account that youâve set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Amazon CloudWatch Internet Monitor User Guide.

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

HealthEvents -> (list)

A list of health events.

(structure)

Information about a health event created in a monitor in Amazon CloudWatch Internet Monitor.

EventArn -> (string)

The Amazon Resource Name (ARN) of the event.

EventId -> (string)

The internally-generated identifier of a specific network traffic impairment health event.

StartedAt -> (timestamp)

When a health event started.

EndedAt -> (timestamp)

The time when a health event ended. If the health event is still active, then the end time is not set.

CreatedAt -> (timestamp)

When the health event was created.

LastUpdatedAt -> (timestamp)

When the health event was last updated.

ImpactedLocations -> (list)

The locations impacted by the health event.

(structure)

Information about a location impacted by a health event in Amazon CloudWatch Internet Monitor.

Geographic regions are hierarchically categorized into country, subdivision, metro and city geographic granularities. The geographic region is identified based on the IP address used at the client locations.

ASName -> (string)

The name of the internet service provider (ISP) or network (ASN).

ASNumber -> (long)

The Autonomous System Number (ASN) of the network at an impacted location.

Country -> (string)

The name of the country where the health event is located.

Subdivision -> (string)

The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).

Metro -> (string)

The metro area where the health event is located.

Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.

City -> (string)

The name of the city where the health event is located.

Latitude -> (double)

The latitude where the health event is located.

Longitude -> (double)

The longitude where the health event is located.

CountryCode -> (string)

The country code where the health event is located. The ISO 3166-2 codes for the country is provided, when available.

SubdivisionCode -> (string)

The subdivision code where the health event is located. The ISO 3166-2 codes for country subdivisions is provided, when available.

ServiceLocation -> (string)

The service location where the health event is located.

Status -> (string)

The status of the health event at an impacted location.

CausedBy -> (structure)

The cause of the impairment. There are two types of network impairments: Amazon Web Services network issues or internet issues. Internet issues are typically a problem with a network provider, like an internet service provider (ISP).

Networks -> (list)

The networks that could be impacted by a network impairment event.

(structure)

An internet service provider (ISP) or network (ASN) in Amazon CloudWatch Internet Monitor.

ASName -> (string)

The name of the internet service provider (ISP) or network (ASN).

ASNumber -> (long)

The Autonomous System Number (ASN) of the internet provider or network.

AsPath -> (list)

The combination of the Autonomous System Number (ASN) of the network and the name of the network.

(structure)

An internet service provider (ISP) or network (ASN) in Amazon CloudWatch Internet Monitor.

ASName -> (string)

The name of the internet service provider (ISP) or network (ASN).

ASNumber -> (long)

The Autonomous System Number (ASN) of the internet provider or network.

NetworkEventType -> (string)

The type of network impairment.

InternetHealth -> (structure)

The calculated health at a specific location.

Availability -> (structure)

Availability in Internet Monitor represents the estimated percentage of traffic that is not seeing an availability drop. For example, an availability score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing an availability drop for that pair.

For more information, see [How Internet Monitor calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

ExperienceScore -> (double)

Experience scores, or health scores are calculated for different geographic and network provider combinations (that is, different granularities) and also summed into global scores. If you view performance or availability scores without filtering for any specific geography or service provider, Amazon CloudWatch Internet Monitor provides global health scores.

The Amazon CloudWatch Internet Monitor chapter in the *CloudWatch User Guide* includes detailed information about how Internet Monitor calculates health scores, including performance and availability scores, and when it creates and resolves health events. For more information, see [How Amazon Web Services calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

PercentOfTotalTrafficImpacted -> (double)

The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.

For information about how Internet Monitor calculates impact, see [How Internet Monitor works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html) in the Amazon CloudWatch Internet Monitor section of the Amazon CloudWatch User Guide.

PercentOfClientLocationImpacted -> (double)

The percentage of impact caused by a health event for client location traffic globally.

For information about how Internet Monitor calculates impact, see [Inside Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html) in the Amazon CloudWatch Internet Monitor section of the Amazon CloudWatch User Guide.

Performance -> (structure)

Performance in Internet Monitor represents the estimated percentage of traffic that is not seeing a performance drop. For example, a performance score of 99% for an end user and service location pair is equivalent to 1% of the traffic experiencing a performance drop for that pair.

For more information, see [How Internet Monitor calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

ExperienceScore -> (double)

Experience scores, or health scores, are calculated for different geographic and network provider combinations (that is, different granularities) and also totaled into global scores. If you view performance or availability scores without filtering for any specific geography or service provider, Amazon CloudWatch Internet Monitor provides global health scores.

The Amazon CloudWatch Internet Monitor chapter in the CloudWatch User Guide includes detailed information about how Internet Monitor calculates health scores, including performance and availability scores, and when it creates and resolves health events. For more information, see [How Amazon Web Services calculates performance and availability scores](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMExperienceScores) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

PercentOfTotalTrafficImpacted -> (double)

The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.

For more information, see [When Amazon Web Services creates and resolves health events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

PercentOfClientLocationImpacted -> (double)

How much performance impact was caused by a health event at a client location. For performance, this is the percentage of how much latency increased during the event compared to typical performance for traffic, from this client location to an Amazon Web Services location, using a specific client network.

For more information, see [When Amazon Web Services creates and resolves health events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

RoundTripTime -> (structure)

This is the percentage of how much round-trip time increased during the event compared to typical round-trip time for your application for traffic.

For more information, see [When Amazon Web Services creates and resolves health events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-inside-internet-monitor.html#IMHealthEventStartStop) in the Amazon CloudWatch Internet Monitor section of the *CloudWatch User Guide* .

P50 -> (double)

RTT at the 50th percentile (p50).

P90 -> (double)

RTT at the 90th percentile (p90).

P95 -> (double)

RTT at the 95th percentile (p95).

Ipv4Prefixes -> (list)

The IPv4 prefixes at the client location that was impacted by the health event.

(string)

Status -> (string)

The status of a health event.

PercentOfTotalTrafficImpacted -> (double)

The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.

ImpactType -> (string)

The type of impairment for a health event.

HealthScoreThreshold -> (double)

The value of the threshold percentage for performance or availability that was configured when Amazon CloudWatch Internet Monitor created the health event.

NextToken -> (string)

The token for the next set of results. You receive this token from a previous call.