# put-playback-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/put-playback-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/put-playback-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# put-playback-configuration

## Description

Creates a playback configuration. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/PutPlaybackConfiguration)

## Synopsis

```
put-playback-configuration
[--ad-decision-server-url <value>]
[--avail-suppression <value>]
[--bumper <value>]
[--cdn-configuration <value>]
[--configuration-aliases <value>]
[--dash-configuration <value>]
[--insertion-mode <value>]
[--live-pre-roll-configuration <value>]
[--manifest-processing-rules <value>]
--name <value>
[--personalization-threshold-seconds <value>]
[--slate-ad-url <value>]
[--tags <value>]
[--transcode-profile-name <value>]
[--video-content-source-url <value>]
[--ad-conditioning-configuration <value>]
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

`--ad-decision-server-url` (string)

The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

`--avail-suppression` (structure)

The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) .

Mode -> (string)

Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to `BEHIND_LIVE_EDGE` , ad suppression is active and MediaTailor wonât fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to `AFTER_LIVE_EDGE` , ad suppression is active and MediaTailor wonât fill ad breaks that are within the live edge plus the avail suppression value.

Value -> (string)

A live edge offset time in HH:MM:SS. MediaTailor wonât fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor wonât fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor wonât fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but wonât fill ad breaks on or behind 45 minutes behind the live edge.

FillPolicy -> (string)

Defines the policy to apply to the avail suppression mode. `BEHIND_LIVE_EDGE` will always use the full avail suppression policy. `AFTER_LIVE_EDGE` mode can be used to invoke partial ad break fills when a session starts mid-break.

Shorthand Syntax:

```
Mode=string,Value=string,FillPolicy=string
```

JSON Syntax:

```
{
  "Mode": "OFF"|"BEHIND_LIVE_EDGE"|"AFTER_LIVE_EDGE",
  "Value": "string",
  "FillPolicy": "FULL_AVAIL_ONLY"|"PARTIAL_AVAIL"
}
```

`--bumper` (structure)

The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html) .

EndUrl -> (string)

The URL for the end bumper asset.

StartUrl -> (string)

The URL for the start bumper asset.

Shorthand Syntax:

```
EndUrl=string,StartUrl=string
```

JSON Syntax:

```
{
  "EndUrl": "string",
  "StartUrl": "string"
}
```

`--cdn-configuration` (structure)

The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

AdSegmentUrlPrefix -> (string)

A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor.*<region>* .amazonaws.com. Then specify the ruleâs name in this `AdSegmentUrlPrefix` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

ContentSegmentUrlPrefix -> (string)

A content delivery network (CDN) to cache content segments, so that content requests donât always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the ruleâs name in this `ContentSegmentUrlPrefix` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.

Shorthand Syntax:

```
AdSegmentUrlPrefix=string,ContentSegmentUrlPrefix=string
```

JSON Syntax:

```
{
  "AdSegmentUrlPrefix": "string",
  "ContentSegmentUrlPrefix": "string"
}
```

`--configuration-aliases` (map)

The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html) .

key -> (string)

The dynamic variable that has aliases.

value -> (map)

Map of aliases to the value to be used at request time.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=KeyName1=string,KeyName2=string,KeyName2=KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": {"string": "string"
      ...}
  ...}
```

`--dash-configuration` (structure)

The configuration for DASH content.

MpdLocation -> (string)

The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that donât support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are `DISABLED` and `EMT_DEFAULT` . The `EMT_DEFAULT` setting enables the inclusion of the tag and is the default value.

OriginManifestType -> (string)

The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to `SINGLE_PERIOD` . The default setting is `MULTI_PERIOD` . For multi-period manifests, omit this setting or set it to `MULTI_PERIOD` .

Shorthand Syntax:

```
MpdLocation=string,OriginManifestType=string
```

JSON Syntax:

```
{
  "MpdLocation": "string",
  "OriginManifestType": "SINGLE_PERIOD"|"MULTI_PERIOD"
}
```

`--insertion-mode` (string)

The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY` , forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.

Possible values:

- `STITCHED_ONLY`
- `PLAYER_SELECT`

`--live-pre-roll-configuration` (structure)

The configuration for pre-roll ad insertion.

AdDecisionServerUrl -> (string)

The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

MaxDurationSeconds -> (integer)

The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor wonât play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

Shorthand Syntax:

```
AdDecisionServerUrl=string,MaxDurationSeconds=integer
```

JSON Syntax:

```
{
  "AdDecisionServerUrl": "string",
  "MaxDurationSeconds": integer
}
```

`--manifest-processing-rules` (structure)

The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

AdMarkerPassthrough -> (structure)

For HLS, when set to `true` , MediaTailor passes through `EXT-X-CUE-IN` , `EXT-X-CUE-OUT` , and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.

No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60` , but no ads are filled for that ad break, MediaTailor will not set the value to `0` .

Enabled -> (boolean)

Enables ad marker passthrough for your configuration.

Shorthand Syntax:

```
AdMarkerPassthrough={Enabled=boolean}
```

JSON Syntax:

```
{
  "AdMarkerPassthrough": {
    "Enabled": true|false
  }
}
```

`--name` (string)

The identifier for the playback configuration.

`--personalization-threshold-seconds` (integer)

Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) .

`--slate-ad-url` (string)

The URL for a high-quality video asset to transcode and use to fill in time thatâs not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

`--tags` (map)

The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--transcode-profile-name` (string)

The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

`--video-content-source-url` (string)

The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.

`--ad-conditioning-configuration` (structure)

The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.

StreamingMediaFileConditioning -> (string)

For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. `TRANSCODE` indicates that MediaTailor must transcode the ads. `NONE` indicates that you have already transcoded the ads outside of MediaTailor and donât need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see [Using preconditioned ads](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) in the Elemental MediaTailor user guide.

Shorthand Syntax:

```
StreamingMediaFileConditioning=string
```

JSON Syntax:

```
{
  "StreamingMediaFileConditioning": "TRANSCODE"|"NONE"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a configuration**

The following `put-playback-configuration` creates a configuration named `campaign_short`.

```
aws mediatailor put-playback-configuration \
    --name campaign_short \
    --ad-decision-server-url http://your.ads.url \
    --video-content-source-url http://video.bucket/index.m3u8
```

Output:

```
{
    "AdDecisionServerUrl": "http://your.ads.url",
    "CdnConfiguration": {},
    "DashConfiguration": {
         "ManifestEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/dash/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/",
         "MpdLocation": "EMT_DEFAULT",
         "OriginManifestType": "MULTI_PERIOD"
    },
    "HlsConfiguration": {
        "ManifestEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/master/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/"
    },
    "Name": "campaign_short",
    "PlaybackConfigurationArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/campaign_short",
    "PlaybackEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com",
    "SessionInitializationEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/session/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/",
    "Tags": {},
    "VideoContentSourceUrl": "http://video.bucket/index.m3u8"
}
```

For more information, see [Creating a Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-create.html) in the *AWS Elemental MediaTailor User Guide*.

## Output

AdDecisionServerUrl -> (string)

The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.

AvailSuppression -> (structure)

The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) .

Mode -> (string)

Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to `BEHIND_LIVE_EDGE` , ad suppression is active and MediaTailor wonât fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to `AFTER_LIVE_EDGE` , ad suppression is active and MediaTailor wonât fill ad breaks that are within the live edge plus the avail suppression value.

Value -> (string)

A live edge offset time in HH:MM:SS. MediaTailor wonât fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor wonât fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor wonât fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but wonât fill ad breaks on or behind 45 minutes behind the live edge.

FillPolicy -> (string)

Defines the policy to apply to the avail suppression mode. `BEHIND_LIVE_EDGE` will always use the full avail suppression policy. `AFTER_LIVE_EDGE` mode can be used to invoke partial ad break fills when a session starts mid-break.

Bumper -> (structure)

The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see [Bumpers](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html) .

EndUrl -> (string)

The URL for the end bumper asset.

StartUrl -> (string)

The URL for the start bumper asset.

CdnConfiguration -> (structure)

The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.

AdSegmentUrlPrefix -> (string)

A non-default content delivery network (CDN) to serve ad segments. By default, AWS Elemental MediaTailor uses Amazon CloudFront with default cache settings as its CDN for ad segments. To set up an alternate CDN, create a rule in your CDN for the origin ads.mediatailor.*<region>* .amazonaws.com. Then specify the ruleâs name in this `AdSegmentUrlPrefix` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for ad segments.

ContentSegmentUrlPrefix -> (string)

A content delivery network (CDN) to cache content segments, so that content requests donât always have to go to the origin server. First, create a rule in your CDN for the content segment origin server. Then specify the ruleâs name in this `ContentSegmentUrlPrefix` . When AWS Elemental MediaTailor serves a manifest, it reports your CDN as the source for content segments.

ConfigurationAliases -> (map)

The player parameters and aliases used as dynamic variables during session initialization. For more information, see [Domain Variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html) .

key -> (string)

The dynamic variable that has aliases.

value -> (map)

Map of aliases to the value to be used at request time.

key -> (string)

value -> (string)

DashConfiguration -> (structure)

The configuration for DASH content.

ManifestEndpointPrefix -> (string)

The URL generated by MediaTailor to initiate a playback session. The session uses server-side reporting. This setting is ignored in PUT operations.

MpdLocation -> (string)

The setting that controls whether MediaTailor includes the Location tag in DASH manifests. MediaTailor populates the Location tag with the URL for manifest update requests, to be used by players that donât support sticky redirects. Disable this if you have CDN routing rules set up for accessing MediaTailor manifests, and you are either using client-side reporting or your players support sticky HTTP redirects. Valid values are `DISABLED` and `EMT_DEFAULT` . The `EMT_DEFAULT` setting enables the inclusion of the tag and is the default value.

OriginManifestType -> (string)

The setting that controls whether MediaTailor handles manifests from the origin server as multi-period manifests or single-period manifests. If your origin server produces single-period manifests, set this to `SINGLE_PERIOD` . The default setting is `MULTI_PERIOD` . For multi-period manifests, omit this setting or set it to `MULTI_PERIOD` .

HlsConfiguration -> (structure)

The configuration for HLS content.

ManifestEndpointPrefix -> (string)

The URL that is used to initiate a playback session for devices that support Apple HLS. The session uses server-side reporting.

InsertionMode -> (string)

The setting that controls whether players can use stitched or guided ad insertion. The default, `STITCHED_ONLY` , forces all player sessions to use stitched (server-side) ad insertion. Choosing `PLAYER_SELECT` allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.

LivePreRollConfiguration -> (structure)

The configuration for pre-roll ad insertion.

AdDecisionServerUrl -> (string)

The URL for the ad decision server (ADS) for pre-roll ads. This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing, you can provide a static VAST URL. The maximum length is 25,000 characters.

MaxDurationSeconds -> (integer)

The maximum allowed duration for the pre-roll ad avail. AWS Elemental MediaTailor wonât play pre-roll ads to exceed this duration, regardless of the total duration of ads that the ADS returns.

LogConfiguration -> (structure)

The configuration that defines where AWS Elemental MediaTailor sends logs for the playback configuration.

PercentEnabled -> (integer)

The percentage of session logs that MediaTailor sends to your configured log destination. For example, if your playback configuration has 1000 sessions and `percentEnabled` is set to `60` , MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the [debug log mode](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html) .

Valid values: `0` - `100`

EnabledLoggingStrategies -> (list)

The method used for collecting logs from AWS Elemental MediaTailor. `LEGACY_CLOUDWATCH` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. `VENDED_LOGS` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.

(string)

AdsInteractionLog -> (structure)

Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).

PublishOptInEventTypes -> (list)

Indicates that MediaTailor emits `RAW_ADS_RESPONSE` logs for playback sessions that are initialized with this configuration.

(string)

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)

ManifestServiceInteractionLog -> (structure)

Settings for customizing what events are included in logs for interactions with the origin server.

ExcludeEventTypes -> (list)

Indicates that MediaTailor wonât emit the selected events in the logs for playback sessions that are initialized with this configuration.

(string)

ManifestProcessingRules -> (structure)

The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.

AdMarkerPassthrough -> (structure)

For HLS, when set to `true` , MediaTailor passes through `EXT-X-CUE-IN` , `EXT-X-CUE-OUT` , and `EXT-X-SPLICEPOINT-SCTE35` ad markers from the origin manifest to the MediaTailor personalized manifest.

No logic is applied to these ad markers. For example, if `EXT-X-CUE-OUT` has a value of `60` , but no ads are filled for that ad break, MediaTailor will not set the value to `0` .

Enabled -> (boolean)

Enables ad marker passthrough for your configuration.

Name -> (string)

The identifier for the playback configuration.

PersonalizationThresholdSeconds -> (integer)

Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to *ad replacement* in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see [Ad Behavior in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html) .

PlaybackConfigurationArn -> (string)

The Amazon Resource Name (ARN) associated with the playback configuration.

PlaybackEndpointPrefix -> (string)

The playback endpoint prefix associated with the playback configuration.

SessionInitializationEndpointPrefix -> (string)

The session initialization endpoint prefix associated with the playback configuration.

SlateAdUrl -> (string)

The URL for a high-quality video asset to transcode and use to fill in time thatâs not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.

Tags -> (map)

The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

TranscodeProfileName -> (string)

The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.

VideoContentSourceUrl -> (string)

The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.

AdConditioningConfiguration -> (structure)

The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.

StreamingMediaFileConditioning -> (string)

For ads that have media files with streaming delivery and supported file extensions, indicates what transcoding action MediaTailor takes when it first receives these ads from the ADS. `TRANSCODE` indicates that MediaTailor must transcode the ads. `NONE` indicates that you have already transcoded the ads outside of MediaTailor and donât need them transcoded as part of the ad insertion workflow. For more information about ad conditioning see [Using preconditioned ads](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html) in the Elemental MediaTailor user guide.