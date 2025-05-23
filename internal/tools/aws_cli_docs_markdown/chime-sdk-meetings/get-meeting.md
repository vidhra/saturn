# get-meetingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/get-meeting.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/get-meeting.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-meetings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-meetings/index.html#cli-aws-chime-sdk-meetings) ]

# get-meeting

## Description

Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see [Using the Amazon Chime SDK](https://docs.aws.amazon.com/chime/latest/dg/meetings-sdk.html) in the *Amazon Chime Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-meetings-2021-07-15/GetMeeting)

## Synopsis

```
get-meeting
--meeting-id <value>
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

`--meeting-id` (string)

The Amazon Chime SDK meeting ID.

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

Meeting -> (structure)

The Amazon Chime SDK meeting information.

MeetingId -> (string)

The Amazon Chime SDK meeting ID.

MeetingHostId -> (string)

Reserved.

ExternalMeetingId -> (string)

The external meeting ID.

Pattern: `[-_&@+=,(){}\[\]\/Â«Â».:|'"#a-zA-Z0-9Ã-Ã¿\s]*`

Values that begin with `aws:` are reserved. You canât configure a value that uses this prefix. Case insensitive.

MediaRegion -> (string)

The Region in which you create the meeting. Available values: `af-south-1` , `ap-northeast-1` , `ap-northeast-2` , `ap-south-1` , `ap-southeast-1` , `ap-southeast-2` , `ca-central-1` , `eu-central-1` , `eu-north-1` , `eu-south-1` , `eu-west-1` , `eu-west-2` , `eu-west-3` , `sa-east-1` , `us-east-1` , `us-east-2` , `us-west-1` , `us-west-2` .

Available values in Amazon Web Services GovCloud (US) Regions: `us-gov-east-1` , `us-gov-west-1` .

MediaPlacement -> (structure)

The media placement for the meeting.

AudioHostUrl -> (string)

The audio host URL.

AudioFallbackUrl -> (string)

The audio fallback URL.

SignalingUrl -> (string)

The signaling URL.

TurnControlUrl -> (string)

The turn control URL.

### Warning

**This parameter is deprecated and no longer used by the Amazon Chime SDK.**

ScreenDataUrl -> (string)

The screen data URL.

### Warning

**This parameter is deprecated and no longer used by the Amazon Chime SDK.**

ScreenViewingUrl -> (string)

The screen viewing URL.

### Warning

**This parameter is deprecated and no longer used by the Amazon Chime SDK.**

ScreenSharingUrl -> (string)

The screen sharing URL.

### Warning

**This parameter is deprecated and no longer used by the Amazon Chime SDK.**

EventIngestionUrl -> (string)

The event ingestion URL.

MeetingFeatures -> (structure)

The features available to a meeting, such as echo reduction.

Audio -> (structure)

The configuration settings for the audio features available to a meeting.

EchoReduction -> (string)

Makes echo reduction available to clients who connect to the meeting.

Video -> (structure)

The configuration settings for the video features available to a meeting.

MaxResolution -> (string)

The maximum video resolution for the meeting. Applies to all attendees.

### Note

Defaults to `HD` . To use `FHD` , you must also provide a `MeetingFeatures:Attendee:MaxCount` value and override the default size limit of 250 attendees.

Content -> (structure)

The configuration settings for the content features available to a meeting.

MaxResolution -> (string)

The maximum resolution for the meeting content.

### Note

Defaults to `FHD` . To use `UHD` , you must also provide a `MeetingFeatures:Attendee:MaxCount` value and override the default size limit of 250 attendees.

Attendee -> (structure)

The configuration settings for the attendee features available to a meeting.

MaxCount -> (integer)

The maximum number of attendees allowed into the meeting.

PrimaryMeetingId -> (string)

When specified, replicates the media from the primary meeting to this meeting.

TenantIds -> (list)

Array of strings.

(string)

MeetingArn -> (string)

The ARN of the meeting.