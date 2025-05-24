# configure-logs-for-playback-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/configure-logs-for-playback-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/configure-logs-for-playback-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# configure-logs-for-playback-configuration

## Description

Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ConfigureLogsForPlaybackConfiguration)

## Synopsis

```
configure-logs-for-playback-configuration
--percent-enabled <value>
--playback-configuration-name <value>
[--enabled-logging-strategies <value>]
[--ads-interaction-log <value>]
[--manifest-service-interaction-log <value>]
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

`--percent-enabled` (integer)

The percentage of session logs that MediaTailor sends to your CloudWatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to `60` , MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the [debug log mode](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html) .

Valid values: `0` - `100`

`--playback-configuration-name` (string)

The name of the playback configuration.

`--enabled-logging-strategies` (list)

The method used for collecting logs from AWS Elemental MediaTailor. To configure MediaTailor to send logs directly to Amazon CloudWatch Logs, choose `LEGACY_CLOUDWATCH` . To configure MediaTailor to send logs to CloudWatch, which then vends the logs to your destination of choice, choose `VENDED_LOGS` . Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.

To use vended logs, you must configure the delivery destination in Amazon CloudWatch, as described in [Enable logging from AWS services, Logging that requires additional permissions [V2]](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2) .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  VENDED_LOGS
  LEGACY_CLOUDWATCH
```

`--ads-interaction-log` (structure)

The event types that MediaTailor emits in logs for interactions with the ADS.

PublishOptInEventTypes -> (list)

Indicates that MediaTailor emits `RAW_ADS_RESPONSE` logs for playback sessions that are initialized with this configuration.

(string)

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)

Shorthand Syntax:

```
PublishOptInEventTypes=string,string,ExcludeEventTypes=string,string
```

JSON Syntax:

```
{
  "PublishOptInEventTypes": ["RAW_ADS_RESPONSE", ...],
  "ExcludeEventTypes": ["AD_MARKER_FOUND"|"NON_AD_MARKER_FOUND"|"MAKING_ADS_REQUEST"|"MODIFIED_TARGET_URL"|"VAST_REDIRECT"|"EMPTY_VAST_RESPONSE"|"EMPTY_VMAP_RESPONSE"|"VAST_RESPONSE"|"REDIRECTED_VAST_RESPONSE"|"FILLED_AVAIL"|"FILLED_OVERLAY_AVAIL"|"BEACON_FIRED"|"WARNING_NO_ADVERTISEMENTS"|"WARNING_VPAID_AD_DROPPED"|"WARNING_URL_VARIABLE_SUBSTITUTION_FAILED"|"ERROR_UNKNOWN"|"ERROR_UNKNOWN_HOST"|"ERROR_DISALLOWED_HOST"|"ERROR_ADS_IO"|"ERROR_ADS_TIMEOUT"|"ERROR_ADS_RESPONSE_PARSE"|"ERROR_ADS_RESPONSE_UNKNOWN_ROOT_ELEMENT"|"ERROR_ADS_INVALID_RESPONSE"|"ERROR_VAST_REDIRECT_EMPTY_RESPONSE"|"ERROR_VAST_REDIRECT_MULTIPLE_VAST"|"ERROR_VAST_REDIRECT_FAILED"|"ERROR_VAST_MISSING_MEDIAFILES"|"ERROR_VAST_MISSING_CREATIVES"|"ERROR_VAST_MISSING_OVERLAYS"|"ERROR_VAST_MISSING_IMPRESSION"|"ERROR_VAST_INVALID_VAST_AD_TAG_URI"|"ERROR_VAST_MULTIPLE_TRACKING_EVENTS"|"ERROR_VAST_MULTIPLE_LINEAR"|"ERROR_VAST_INVALID_MEDIA_FILE"|"ERROR_FIRING_BEACON_FAILED"|"ERROR_PERSONALIZATION_DISABLED"|"VOD_TIME_BASED_AVAIL_PLAN_VAST_RESPONSE_FOR_OFFSET"|"VOD_TIME_BASED_AVAIL_PLAN_SUCCESS"|"VOD_TIME_BASED_AVAIL_PLAN_WARNING_NO_ADVERTISEMENTS"|"INTERSTITIAL_VOD_SUCCESS"|"INTERSTITIAL_VOD_FAILURE", ...]
}
```

`--manifest-service-interaction-log` (structure)

The event types that MediaTailor emits in logs for interactions with the origin server.

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)

Shorthand Syntax:

```
ExcludeEventTypes=string,string
```

JSON Syntax:

```
{
  "ExcludeEventTypes": ["GENERATED_MANIFEST"|"ORIGIN_MANIFEST"|"SESSION_INITIALIZED"|"TRACKING_RESPONSE"|"CONFIG_SYNTAX_ERROR"|"CONFIG_SECURITY_ERROR"|"UNKNOWN_HOST"|"TIMEOUT_ERROR"|"CONNECTION_ERROR"|"IO_ERROR"|"UNKNOWN_ERROR"|"HOST_DISALLOWED"|"PARSING_ERROR"|"MANIFEST_ERROR"|"NO_MASTER_OR_MEDIA_PLAYLIST"|"NO_MASTER_PLAYLIST"|"NO_MEDIA_PLAYLIST"|"INCOMPATIBLE_HLS_VERSION"|"SCTE35_PARSING_ERROR"|"INVALID_SINGLE_PERIOD_DASH_MANIFEST"|"UNSUPPORTED_SINGLE_PERIOD_DASH_MANIFEST"|"LAST_PERIOD_MISSING_AUDIO"|"LAST_PERIOD_MISSING_AUDIO_WARNING"|"ERROR_ORIGIN_PREFIX_INTERPOLATION"|"ERROR_ADS_INTERPOLATION"|"ERROR_LIVE_PRE_ROLL_ADS_INTERPOLATION"|"ERROR_CDN_AD_SEGMENT_INTERPOLATION"|"ERROR_CDN_CONTENT_SEGMENT_INTERPOLATION"|"ERROR_SLATE_AD_URL_INTERPOLATION"|"ERROR_PROFILE_NAME_INTERPOLATION"|"ERROR_BUMPER_START_INTERPOLATION"|"ERROR_BUMPER_END_INTERPOLATION", ...]
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

PercentEnabled -> (integer)

The percentage of session logs that MediaTailor sends to your Cloudwatch Logs account.

PlaybackConfigurationName -> (string)

The name of the playback configuration.

EnabledLoggingStrategies -> (list)

The method used for collecting logs from AWS Elemental MediaTailor. `LEGACY_CLOUDWATCH` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. `VENDED_LOGS` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.

(string)

AdsInteractionLog -> (structure)

The event types that MediaTailor emits in logs for interactions with the ADS.

PublishOptInEventTypes -> (list)

Indicates that MediaTailor emits `RAW_ADS_RESPONSE` logs for playback sessions that are initialized with this configuration.

(string)

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)

ManifestServiceInteractionLog -> (structure)

The event types that MediaTailor emits in logs for interactions with the origin server.

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)