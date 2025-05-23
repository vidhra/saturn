# describe-campaignÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcampaignsv2/describe-campaign.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcampaignsv2/describe-campaign.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connectcampaignsv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcampaignsv2/index.html#cli-aws-connectcampaignsv2) ]

# describe-campaign

## Description

Describes the specific campaign.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connectcampaignsv2-2024-04-23/DescribeCampaign)

## Synopsis

```
describe-campaign
--id <value>
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

`--id` (string)

Identifier representing a Campaign

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

campaign -> (structure)

An Amazon Connect campaign.

id -> (string)

Identifier representing a Campaign

arn -> (string)

The resource name of an Amazon Connect campaign.

name -> (string)

The name of an Amazon Connect Campaign name.

connectInstanceId -> (string)

Amazon Connect Instance Id

channelSubtypeConfig -> (structure)

Campaign Channel Subtype config

telephony -> (structure)

Telephony Channel Subtype config

capacity -> (double)

Allocates outbound capacity for the specific channel subtype of this campaign between multiple active campaigns

connectQueueId -> (string)

The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number.

outboundMode -> (tagged union structure)

Telephony Outbound Mode

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `progressive`, `predictive`, `agentless`.

progressive -> (structure)

Progressive config

bandwidthAllocation -> (double)

The bandwidth allocation of a queue resource.

predictive -> (structure)

Predictive config

bandwidthAllocation -> (double)

The bandwidth allocation of a queue resource.

agentless -> (structure)

Agentless config

defaultOutboundConfig -> (structure)

Default Telephony Outbound config

connectContactFlowId -> (string)

The identifier of the contact flow for the outbound call.

connectSourcePhoneNumber -> (string)

The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.

answerMachineDetectionConfig -> (structure)

Answering Machine Detection config

enableAnswerMachineDetection -> (boolean)

Enable or disable answering machine detection

awaitAnswerMachinePrompt -> (boolean)

Enable or disable await answer machine prompt

sms -> (structure)

SMS Channel Subtype config

capacity -> (double)

Allocates outbound capacity for the specific channel subtype of this campaign between multiple active campaigns

outboundMode -> (tagged union structure)

SMS Outbound Mode

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agentless`.

agentless -> (structure)

Agentless config

defaultOutboundConfig -> (structure)

Default SMS Outbound config

connectSourcePhoneNumberArn -> (string)

Amazon Resource Names(ARN)

wisdomTemplateArn -> (string)

Amazon Resource Names(ARN)

email -> (structure)

Email Channel Subtype config

capacity -> (double)

Allocates outbound capacity for the specific channel subtype of this campaign between multiple active campaigns

outboundMode -> (tagged union structure)

Email Outbound Mode

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agentless`.

agentless -> (structure)

Agentless config

defaultOutboundConfig -> (structure)

Default Email Outbound config

connectSourceEmailAddress -> (string)

Source/Destination Email address used for Email messages

sourceEmailAddressDisplayName -> (string)

Display name for Email Address

wisdomTemplateArn -> (string)

Amazon Resource Names(ARN)

source -> (tagged union structure)

Source of the campaign

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `customerProfilesSegmentArn`, `eventTrigger`.

customerProfilesSegmentArn -> (string)

Amazon Resource Names(ARN)

eventTrigger -> (structure)

Event trigger of the campaign

customerProfilesDomainArn -> (string)

Amazon Resource Names(ARN)

connectCampaignFlowArn -> (string)

Amazon Resource Names(ARN)

schedule -> (structure)

Campaign schedule

startTime -> (timestamp)

Timestamp with no UTC offset or timezone

endTime -> (timestamp)

Timestamp with no UTC offset or timezone

refreshFrequency -> (string)

Time duration in ISO 8601 format

communicationTimeConfig -> (structure)

Campaign communication time config

localTimeZoneConfig -> (structure)

Local time zone config

defaultTimeZone -> (string)

Time Zone Id in the IANA format

localTimeZoneDetection -> (list)

Local TimeZone Detection method list

(string)

Local TimeZone Detection method.

telephony -> (structure)

Time window config

openHours -> (tagged union structure)

Open Hours config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dailyHours`.

dailyHours -> (map)

Daily Hours map

key -> (string)

Day of week enum

value -> (list)

List of time range

(structure)

Time range in 24 hour format

startTime -> (string)

Time in ISO 8601 format, e.g. T23:11

endTime -> (string)

Time in ISO 8601 format, e.g. T23:11

restrictedPeriods -> (tagged union structure)

Restricted period config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `restrictedPeriodList`.

restrictedPeriodList -> (list)

List of restricted period

(structure)

Restricted period

name -> (string)

The name of a restricted period.

startDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

endDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

sms -> (structure)

Time window config

openHours -> (tagged union structure)

Open Hours config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dailyHours`.

dailyHours -> (map)

Daily Hours map

key -> (string)

Day of week enum

value -> (list)

List of time range

(structure)

Time range in 24 hour format

startTime -> (string)

Time in ISO 8601 format, e.g. T23:11

endTime -> (string)

Time in ISO 8601 format, e.g. T23:11

restrictedPeriods -> (tagged union structure)

Restricted period config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `restrictedPeriodList`.

restrictedPeriodList -> (list)

List of restricted period

(structure)

Restricted period

name -> (string)

The name of a restricted period.

startDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

endDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

email -> (structure)

Time window config

openHours -> (tagged union structure)

Open Hours config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dailyHours`.

dailyHours -> (map)

Daily Hours map

key -> (string)

Day of week enum

value -> (list)

List of time range

(structure)

Time range in 24 hour format

startTime -> (string)

Time in ISO 8601 format, e.g. T23:11

endTime -> (string)

Time in ISO 8601 format, e.g. T23:11

restrictedPeriods -> (tagged union structure)

Restricted period config

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `restrictedPeriodList`.

restrictedPeriodList -> (list)

List of restricted period

(structure)

Restricted period

name -> (string)

The name of a restricted period.

startDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

endDate -> (string)

Date in ISO 8601 format, e.g. 2024-01-01

communicationLimitsOverride -> (structure)

Communication limits config

allChannelSubtypes -> (tagged union structure)

Communication limits

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `communicationLimitsList`.

communicationLimitsList -> (list)

List of communication limit

(structure)

Communication Limit

maxCountPerRecipient -> (integer)

Maximum number of contacts allowed for a given target within the given frequency.

frequency -> (integer)

The number of days to consider with regards to this limit.

unit -> (string)

The communication limit time unit.

tags -> (map)

Tag map with key and value.

key -> (string)

The key of tag.

value -> (string)

The value of tag.