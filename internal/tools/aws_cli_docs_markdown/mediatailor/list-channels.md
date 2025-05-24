# list-channelsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-channels.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-channels.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# list-channels

## Description

Retrieves information about the channels that are associated with the current AWS account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/ListChannels)

`list-channels` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-channels
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

A list of channels that are associated with this account.

(structure)

The configuration parameters for a channel. For information about MediaTailor channels, see [Working with channels](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html) in the *MediaTailor User Guide* .

Arn -> (string)

The ARN of the channel.

ChannelName -> (string)

The name of the channel.

ChannelState -> (string)

Returns the state whether the channel is running or not.

CreationTime -> (timestamp)

The timestamp of when the channel was created.

FillerSlate -> (structure)

The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the `LINEAR` `PlaybackMode` . MediaTailor doesnât support filler slate for channels using the `LOOP` `PlaybackMode` .

SourceLocationName -> (string)

The name of the source location where the slate VOD source is stored.

VodSourceName -> (string)

The slate VOD source name. The VOD source must already exist in a source location before it can be used for slate.

LastModifiedTime -> (timestamp)

The timestamp of when the channel was last modified.

Outputs -> (list)

The channelâs output properties.

(structure)

The output item response.

DashPlaylistSettings -> (structure)

DASH manifest configuration settings.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.

MinBufferTimeSeconds -> (integer)

Minimum amount of content (measured in seconds) that a player must keep available in the buffer. Minimum value: `2` seconds. Maximum value: `60` seconds.

MinUpdatePeriodSeconds -> (integer)

Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.

SuggestedPresentationDelaySeconds -> (integer)

Amount of time (in seconds) that the player should be from the live point at the end of the manifest. Minimum value: `2` seconds. Maximum value: `60` seconds.

HlsPlaylistSettings -> (structure)

HLS manifest configuration settings.

ManifestWindowSeconds -> (integer)

The total duration (in seconds) of each manifest. Minimum value: `30` seconds. Maximum value: `3600` seconds.

AdMarkupType -> (list)

Determines the type of SCTE 35 tags to use in ad markup. Specify `DATERANGE` to use `DATERANGE` tags (for live or VOD content). Specify `SCTE35_ENHANCED` to use `EXT-X-CUE-OUT` and `EXT-X-CUE-IN` tags (for VOD content only).

(string)

ManifestName -> (string)

The name of the manifest for the channel that will appear in the channel outputâs playback URL.

PlaybackUrl -> (string)

The URL used for playback by content players.

SourceGroup -> (string)

A string used to associate a package configuration source group with a channel output.

PlaybackMode -> (string)

The type of playback mode for this channel.

`LINEAR` - Programs play back-to-back only once.

`LOOP` - Programs play back-to-back in an endless loop. When the last program in the schedule plays, playback loops back to the first program in the schedule.

Tags -> (map)

The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

Tier -> (string)

The tier for this channel. STANDARD tier channels can contain live programs.

LogConfiguration -> (structure)

The log configuration.

LogTypes -> (list)

The log types.

(string)

Audiences -> (list)

The list of audiences defined in channel.

(string)

NextToken -> (string)

Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.