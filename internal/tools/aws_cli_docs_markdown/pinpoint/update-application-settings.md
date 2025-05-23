# update-application-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-application-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-application-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-application-settings

## Description

Updates the settings for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateApplicationSettings)

## Synopsis

```
update-application-settings
--application-id <value>
--write-application-settings-request <value>
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

`--write-application-settings-request` (structure)

Specifies the default settings for an application.

CampaignHook -> (structure)

The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application.

To override these settings and define custom settings for a specific campaign, use the CampaignHook object of the Campaignresource.

LambdaFunctionName -> (string)

The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.

Mode -> (string)

The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:

- FILTER - Invoke the function to customize the segment thatâs used by a campaign.
- DELIVERY - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the CustomDeliveryConfiguration and CampaignCustomMessage objects of the campaign.

WebUrl -> (string)

The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS.

CloudWatchMetricsEnabled -> (boolean)

Specifies whether to enable application-related alarms in Amazon CloudWatch.

EventTaggingEnabled -> (boolean)

Limits -> (structure)

The default sending limits for campaigns in the application. To override these limits and define custom limits for a specific campaign or journey, use the Campaignresource or the Journeyresource, respectively.

Daily -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100.

MaximumDuration -> (integer)

The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.

MessagesPerSecond -> (integer)

The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000.

Total -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100.

Session -> (integer)

The maximum total number of messages that the campaign can send per user session.

QuietTime -> (structure)

The default quiet time for campaigns in the application. Quiet time is a specific time range when messages arenât sent to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the application (or a campaign or journey that has custom quiet time settings).
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the application (or a campaign or journey that has custom quiet time settings).

If any of the preceding conditions isnât met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled.

To override the default quiet time settings for a specific campaign or journey, use the Campaignresource or the Journeyresource to define a custom quiet time for the campaign or journey.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

JourneyLimits -> (structure)

The default sending limits for journeys in the application. These limits apply to each journey for the application but can be overridden, on a per journey basis, with the JourneyLimits resource.

DailyCap -> (integer)

The daily number of messages that an endpoint can receive from all journeys. The maximum value is 100. If set to 0, this limit will not apply.

TimeframeCap -> (structure)

The default maximum number of messages that can be sent to an endpoint during the specified timeframe for all journeys.

Cap -> (integer)

The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply.

Days -> (integer)

The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply.

TotalCap -> (integer)

The default maximum number of messages that a single journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.

Shorthand Syntax:

```
CampaignHook={LambdaFunctionName=string,Mode=string,WebUrl=string},CloudWatchMetricsEnabled=boolean,EventTaggingEnabled=boolean,Limits={Daily=integer,MaximumDuration=integer,MessagesPerSecond=integer,Total=integer,Session=integer},QuietTime={End=string,Start=string},JourneyLimits={DailyCap=integer,TimeframeCap={Cap=integer,Days=integer},TotalCap=integer}
```

JSON Syntax:

```
{
  "CampaignHook": {
    "LambdaFunctionName": "string",
    "Mode": "DELIVERY"|"FILTER",
    "WebUrl": "string"
  },
  "CloudWatchMetricsEnabled": true|false,
  "EventTaggingEnabled": true|false,
  "Limits": {
    "Daily": integer,
    "MaximumDuration": integer,
    "MessagesPerSecond": integer,
    "Total": integer,
    "Session": integer
  },
  "QuietTime": {
    "End": "string",
    "Start": "string"
  },
  "JourneyLimits": {
    "DailyCap": integer,
    "TimeframeCap": {
      "Cap": integer,
      "Days": integer
    },
    "TotalCap": integer
  }
}
```

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

ApplicationSettingsResource -> (structure)

Provides information about an application, including the default settings for an application.

ApplicationId -> (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

CampaignHook -> (structure)

The settings for the AWS Lambda function to invoke by default as a code hook for campaigns in the application. You can use this hook to customize segments that are used by campaigns in the application.

LambdaFunctionName -> (string)

The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to customize a segment for a campaign.

Mode -> (string)

The mode that Amazon Pinpoint uses to invoke the AWS Lambda function. Possible values are:

- FILTER - Invoke the function to customize the segment thatâs used by a campaign.
- DELIVERY - (Deprecated) Previously, invoked the function to send a campaign through a custom channel. This functionality is not supported anymore. To send a campaign through a custom channel, use the CustomDeliveryConfiguration and CampaignCustomMessage objects of the campaign.

WebUrl -> (string)

The web URL that Amazon Pinpoint calls to invoke the AWS Lambda function over HTTPS.

LastModifiedDate -> (string)

The date and time, in ISO 8601 format, when the applicationâs settings were last modified.

Limits -> (structure)

The default sending limits for campaigns in the application.

Daily -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. For an application, this value specifies the default limit for the number of messages that campaigns and journeys can send to a single endpoint during a 24-hour period. The maximum value is 100.

MaximumDuration -> (integer)

The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.

MessagesPerSecond -> (integer)

The maximum number of messages that a campaign can send each second. For an application, this value specifies the default limit for the number of messages that campaigns can send each second. The minimum value is 1. The maximum value is 20,000.

Total -> (integer)

The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. If a campaign recurs, this setting applies to all runs of the campaign. The maximum value is 100.

Session -> (integer)

The maximum total number of messages that the campaign can send per user session.

QuietTime -> (structure)

The default quiet time for campaigns in the application. Quiet time is a specific time range when messages arenât sent to endpoints, if all the following conditions are met:

- The EndpointDemographic.Timezone property of the endpoint is set to a valid value.
- The current time in the endpointâs time zone is later than or equal to the time specified by the QuietTime.Start property for the application (or a campaign or journey that has custom quiet time settings).
- The current time in the endpointâs time zone is earlier than or equal to the time specified by the QuietTime.End property for the application (or a campaign or journey that has custom quiet time settings).

If any of the preceding conditions isnât met, the endpoint will receive messages from a campaign or journey, even if quiet time is enabled.

End -> (string)

The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

Start -> (string)

The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.

JourneyLimits -> (structure)

The default sending limits for journeys in the application. These limits apply to each journey for the application but can be overridden, on a per journey basis, with the JourneyLimits resource.

DailyCap -> (integer)

The daily number of messages that an endpoint can receive from all journeys. The maximum value is 100. If set to 0, this limit will not apply.

TimeframeCap -> (structure)

The default maximum number of messages that can be sent to an endpoint during the specified timeframe for all journeys.

Cap -> (integer)

The maximum number of messages that all journeys can send to an endpoint during the specified timeframe. The maximum value is 100. If set to 0, this limit will not apply.

Days -> (integer)

The length of the timeframe in days. The maximum value is 30. If set to 0, this limit will not apply.

TotalCap -> (integer)

The default maximum number of messages that a single journey can sent to a single endpoint. The maximum value is 100. If set to 0, this limit will not apply.