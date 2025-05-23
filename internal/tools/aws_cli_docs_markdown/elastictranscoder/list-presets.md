# list-presetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elastictranscoder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/index.html#cli-aws-elastictranscoder) ]

# list-presets

## Description

The ListPresets operation gets a list of the default presets included with Elastic Transcoder and the presets that youâve added in an AWS region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elastictranscoder-2012-09-25/ListPresets)

`list-presets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Presets`

## Synopsis

```
list-presets
[--ascending <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--ascending` (string)

To list presets in chronological order by the date and time that they were created, enter `true` . To list presets in reverse chronological order, enter `false` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve a list of ElasticTranscoder presets**

This example retrieves a list of ElasticTranscoder presets.

Command:

```
aws elastictranscoder list-presets --max-items 2
```

Output:

```
{
  "Presets": [
      {
          "Container": "mp4",
          "Name": "KindleFireHD-preset",
          "Video": {
              "Resolution": "1280x720",
              "FrameRate": "30",
              "KeyframesMaxDist": "90",
              "FixedGOP": "false",
              "Codec": "H.264",
              "Watermarks": [],
              "CodecOptions": {
                  "Profile": "main",
                  "MaxReferenceFrames": "3",
                  "ColorSpaceConversionMode": "None",
                  "InterlacedMode": "Progressive",
                  "Level": "4"
              },
              "AspectRatio": "16:9",
              "BitRate": "2200"
          },
          "Audio": {
              "Channels": "2",
              "CodecOptions": {
                  "Profile": "AAC-LC"
              },
              "SampleRate": "48000",
              "Codec": "AAC",
              "BitRate": "160"
          },
          "Type": "Custom",
          "Id": "3333333333333-abcde2",
          "Arn": "arn:aws:elastictranscoder:us-west-2:123456789012:preset/3333333333333-abcde2",
          "Thumbnails": {
              "AspectRatio": "16:9",
              "Interval": "60",
              "Resolution": "192x108",
              "Format": "png"
          }
      },
      {
          "Thumbnails": {
              "AspectRatio": "16:9",
              "Interval": "60",
              "Resolution": "192x108",
              "Format": "png"
          },
          "Container": "mp4",
          "Description": "Custom preset for transcoding jobs",
          "Video": {
              "Resolution": "1280x720",
              "FrameRate": "30",
              "KeyframesMaxDist": "90",
              "FixedGOP": "false",
              "Codec": "H.264",
              "Watermarks": [],
              "CodecOptions": {
                  "Profile": "main",
                  "MaxReferenceFrames": "3",
                  "ColorSpaceConversionMode": "None",
                  "InterlacedMode": "Progressive",
                  "Level": "3.1"
              },
              "AspectRatio": "16:9",
              "BitRate": "2200"
          },
          "Audio": {
              "Channels": "2",
              "CodecOptions": {
                  "Profile": "AAC-LC"
              },
              "SampleRate": "44100",
              "Codec": "AAC",
              "BitRate": "160"
          },
          "Type": "Custom",
          "Id": "3333333333333-abcde3",
          "Arn": "arn:aws:elastictranscoder:us-west-2:123456789012:preset/3333333333333-abcde3",
          "Name": "Roman's Preset"
      }
  ],
  "NextToken": "eyJQYWdlVG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
```

## Output

Presets -> (list)

An array of `Preset` objects.

(structure)

Presets are templates that contain most of the settings for transcoding media files from one format to another. Elastic Transcoder includes some default presets for common formats, for example, several iPod and iPhone versions. You can also create your own presets for formats that arenât included among the default presets. You specify which preset you want to use when you create a job.

Id -> (string)

Identifier for the new preset. You use this value to get settings for the preset or to delete it.

Arn -> (string)

The Amazon Resource Name (ARN) for the preset.

Name -> (string)

The name of the preset.

Description -> (string)

A description of the preset.

Container -> (string)

The container type for the output file. Valid values include `flac` , `flv` , `fmp4` , `gif` , `mp3` , `mp4` , `mpg` , `mxf` , `oga` , `ogg` , `ts` , and `webm` .

Audio -> (structure)

A section of the response body that provides information about the audio preset values.

Codec -> (string)

The audio codec for the output file. Valid values include `aac` , `flac` , `mp2` , `mp3` , `pcm` , and `vorbis` .

SampleRate -> (string)

The sample rate of the audio stream in the output file, in Hertz. Valid values include:

`auto` , `22050` , `32000` , `44100` , `48000` , `96000`

If you specify `auto` , Elastic Transcoder automatically detects the sample rate.

BitRate -> (string)

The bit rate of the audio stream in the output file, in kilobits/second. Enter an integer between 64 and 320, inclusive.

Channels -> (string)

The number of audio channels in the output file. The following values are valid:

`auto` , `0` , `1` , `2`

One channel carries the information played by a single speaker. For example, a stereo track with two channels sends one channel to the left speaker, and the other channel to the right speaker. The output channels are organized into tracks. If you want Elastic Transcoder to automatically detect the number of audio channels in the input file and use that value for the output file, select `auto` .

The output of a specific channel value and inputs are as follows:

- `auto` **channel specified, with any input:** Pass through up to eight input channels.
- `0` **channels specified, with any input:** Audio omitted from the output.
- `1` **channel specified, with at least one input channel:** Mono sound.
- `2` **channels specified, with any input:** Two identical mono channels or stereo. For more information about tracks, see `Audio:AudioPackingMode.`

For more information about how Elastic Transcoder organizes channels and tracks, see `Audio:AudioPackingMode` .

AudioPackingMode -> (string)

The method of organizing audio channels and tracks. Use `Audio:Channels` to specify the number of channels in your output, and `Audio:AudioPackingMode` to specify the number of tracks and their relation to the channels. If you do not specify an `Audio:AudioPackingMode` , Elastic Transcoder uses `SingleTrack` .

The following values are valid:

`SingleTrack` , `OneChannelPerTrack` , and `OneChannelPerTrackWithMosTo8Tracks`

When you specify `SingleTrack` , Elastic Transcoder creates a single track for your output. The track can have up to eight channels. Use `SingleTrack` for all non-`mxf` containers.

The outputs of `SingleTrack` for a specific channel value and inputs are as follows:

- `0` **channels with any input:** Audio omitted from the output
- `1, 2, or auto` **channels with no audio input:** Audio omitted from the output
- `1` **channel with any input with audio:** One track with one channel, downmixed if necessary
- `2` **channels with one track with one channel:** One track with two identical channels
- `2 or auto` **channels with two tracks with one channel each:** One track with two channels
- `2 or auto` **channels with one track with two channels:** One track with two channels
- `2` **channels with one track with multiple channels:** One track with two channels
- `auto` **channels with one track with one channel:** One track with one channel
- `auto` **channels with one track with multiple channels:** One track with multiple channels

When you specify `OneChannelPerTrack` , Elastic Transcoder creates a new track for every channel in your output. Your output can have up to eight single-channel tracks.

The outputs of `OneChannelPerTrack` for a specific channel value and inputs are as follows:

- `0` **channels with any input:** Audio omitted from the output
- `1, 2, or auto` **channels with no audio input:** Audio omitted from the output
- `1` **channel with any input with audio:** One track with one channel, downmixed if necessary
- `2` **channels with one track with one channel:** Two tracks with one identical channel each
- `2 or auto` **channels with two tracks with one channel each:** Two tracks with one channel each
- `2 or auto` **channels with one track with two channels:** Two tracks with one channel each
- `2` **channels with one track with multiple channels:** Two tracks with one channel each
- `auto` **channels with one track with one channel:** One track with one channel
- `auto` **channels with one track with multiple channels:** Up to eight tracks with one channel each

When you specify `OneChannelPerTrackWithMosTo8Tracks` , Elastic Transcoder creates eight single-channel tracks for your output. All tracks that do not contain audio data from an input channel are MOS, or Mit Out Sound, tracks.

The outputs of `OneChannelPerTrackWithMosTo8Tracks` for a specific channel value and inputs are as follows:

- `0` **channels with any input:** Audio omitted from the output
- `1, 2, or auto` **channels with no audio input:** Audio omitted from the output
- `1` **channel with any input with audio:** One track with one channel, downmixed if necessary, plus six MOS tracks
- `2` **channels with one track with one channel:** Two tracks with one identical channel each, plus six MOS tracks
- `2 or auto` **channels with two tracks with one channel each:** Two tracks with one channel each, plus six MOS tracks
- `2 or auto` **channels with one track with two channels:** Two tracks with one channel each, plus six MOS tracks
- `2` **channels with one track with multiple channels:** Two tracks with one channel each, plus six MOS tracks
- `auto` **channels with one track with one channel:** One track with one channel, plus seven MOS tracks
- `auto` **channels with one track with multiple channels:** Up to eight tracks with one channel each, plus MOS tracks until there are eight tracks in all

CodecOptions -> (structure)

If you specified `AAC` for `Audio:Codec` , this is the `AAC` compression profile to use. Valid values include:

`auto` , `AAC-LC` , `HE-AAC` , `HE-AACv2`

If you specify `auto` , Elastic Transcoder chooses a profile based on the bit rate of the output file.

Profile -> (string)

You can only choose an audio profile when you specify AAC for the value of Audio:Codec.

Specify the AAC profile for the output file. Elastic Transcoder supports the following profiles:

- `auto` : If you specify `auto` , Elastic Transcoder selects the profile based on the bit rate selected for the output file.
- `AAC-LC` : The most common AAC profile. Use for bit rates larger than 64 kbps.
- `HE-AAC` : Not supported on some older players and devices. Use for bit rates between 40 and 80 kbps.
- `HE-AACv2` : Not supported on some players and devices. Use for bit rates less than 48 kbps.

All outputs in a `Smooth` playlist must have the same value for `Profile` .

### Note

If you created any presets before AAC profiles were added, Elastic Transcoder automatically updated your presets to use AAC-LC. You can change the value as required.

BitDepth -> (string)

You can only choose an audio bit depth when you specify `flac` or `pcm` for the value of Audio:Codec.

The bit depth of a sample is how many bits of information are included in the audio samples. The higher the bit depth, the better the audio, but the larger the file.

Valid values are `16` and `24` .

The most common bit depth is `24` .

BitOrder -> (string)

You can only choose an audio bit order when you specify `pcm` for the value of Audio:Codec.

The order the bits of a PCM sample are stored in.

The supported value is `LittleEndian` .

Signed -> (string)

You can only choose whether an audio sample is signed when you specify `pcm` for the value of Audio:Codec.

Whether audio samples are represented with negative and positive numbers (signed) or only positive numbers (unsigned).

The supported value is `Signed` .

Video -> (structure)

A section of the response body that provides information about the video preset values.

Codec -> (string)

The video codec for the output file. Valid values include `gif` , `H.264` , `mpeg2` , `vp8` , and `vp9` . You can only specify `vp8` and `vp9` when the container type is `webm` , `gif` when the container type is `gif` , and `mpeg2` when the container type is `mpg` .

CodecOptions -> (map)

**Profile (H.264/VP8/VP9 Only)**

The H.264 profile that you want to use for the output file. Elastic Transcoder supports the following profiles:

- `baseline` : The profile most commonly used for videoconferencing and for mobile applications.
- `main` : The profile used for standard-definition digital TV broadcasts.
- `high` : The profile used for high-definition digital TV broadcasts and for Blu-ray discs.

**Level (H.264 Only)**

The H.264 level that you want to use for the output file. Elastic Transcoder supports the following levels:

`1` , `1b` , `1.1` , `1.2` , `1.3` , `2` , `2.1` , `2.2` , `3` , `3.1` , `3.2` , `4` , `4.1`

**MaxReferenceFrames (H.264 Only)**

Applicable only when the value of Video:Codec is H.264. The maximum number of previously decoded frames to use as a reference for decoding future frames. Valid values are integers 0 through 16, but we recommend that you not use a value greater than the following:

`Min(Floor(Maximum decoded picture buffer in macroblocks * 256 / (Width in pixels * Height in pixels)), 16)`

where *Width in pixels* and *Height in pixels* represent either MaxWidth and MaxHeight, or Resolution. *Maximum decoded picture buffer in macroblocks* depends on the value of the `Level` object. See the list below. (A macroblock is a block of pixels measuring 16x16.)

- 1 - 396
- 1b - 396
- 1.1 - 900
- 1.2 - 2376
- 1.3 - 2376
- 2 - 2376
- 2.1 - 4752
- 2.2 - 8100
- 3 - 8100
- 3.1 - 18000
- 3.2 - 20480
- 4 - 32768
- 4.1 - 32768

**MaxBitRate (Optional, H.264/MPEG2/VP8/VP9 only)**

The maximum number of bits per second in a video buffer; the size of the buffer is specified by `BufferSize` . Specify a value between 16 and 62,500. You can reduce the bandwidth required to stream a video by reducing the maximum bit rate, but this also reduces the quality of the video.

**BufferSize (Optional, H.264/MPEG2/VP8/VP9 only)**

The maximum number of bits in any x seconds of the output video. This window is commonly 10 seconds, the standard segment duration when youâre using FMP4 or MPEG-TS for the container type of the output video. Specify an integer greater than 0. If you specify `MaxBitRate` and omit `BufferSize` , Elastic Transcoder sets `BufferSize` to 10 times the value of `MaxBitRate` .

**InterlacedMode (Optional, H.264/MPEG2 Only)**

The interlace mode for the output video.

Interlaced video is used to double the perceived frame rate for a video by interlacing two fields (one field on every other line, the other field on the other lines) so that the human eye registers multiple pictures per frame. Interlacing reduces the bandwidth required for transmitting a video, but can result in blurred images and flickering.

Valid values include `Progressive` (no interlacing, top to bottom), `TopFirst` (top field first), `BottomFirst` (bottom field first), and `Auto` .

If `InterlaceMode` is not specified, Elastic Transcoder uses `Progressive` for the output. If `Auto` is specified, Elastic Transcoder interlaces the output.

**ColorSpaceConversionMode (Optional, H.264/MPEG2 Only)**

The color space conversion Elastic Transcoder applies to the output video. Color spaces are the algorithms used by the computer to store information about how to render color. `Bt.601` is the standard for standard definition video, while `Bt.709` is the standard for high definition video.

Valid values include `None` , `Bt709toBt601` , `Bt601toBt709` , and `Auto` .

If you chose `Auto` for `ColorSpaceConversionMode` and your output is interlaced, your frame rate is one of `23.97` , `24` , `25` , `29.97` , `50` , or `60` , your `SegmentDuration` is null, and you are using one of the resolution changes from the list below, Elastic Transcoder applies the following color space conversions:

- *Standard to HD, 720x480 to 1920x1080* - Elastic Transcoder applies `Bt601ToBt709`
- *Standard to HD, 720x576 to 1920x1080* - Elastic Transcoder applies `Bt601ToBt709`
- *HD to Standard, 1920x1080 to 720x480* - Elastic Transcoder applies `Bt709ToBt601`
- *HD to Standard, 1920x1080 to 720x576* - Elastic Transcoder applies `Bt709ToBt601`

### Note

Elastic Transcoder may change the behavior of the `ColorspaceConversionMode` `Auto` mode in the future. All outputs in a playlist must use the same `ColorSpaceConversionMode` .

If you do not specify a `ColorSpaceConversionMode` , Elastic Transcoder does not change the color space of a file. If you are unsure what `ColorSpaceConversionMode` was applied to your output file, you can check the `AppliedColorSpaceConversion` parameter included in your job response. If your job does not have an `AppliedColorSpaceConversion` in its response, no `ColorSpaceConversionMode` was applied.

**ChromaSubsampling**

The sampling pattern for the chroma (color) channels of the output video. Valid values include `yuv420p` and `yuv422p` .

`yuv420p` samples the chroma information of every other horizontal and every other vertical line, `yuv422p` samples the color information of every horizontal line and every other vertical line.

**LoopCount (Gif Only)**

The number of times you want the output gif to loop. Valid values include `Infinite` and integers between `0` and `100` , inclusive.

key -> (string)

value -> (string)

KeyframesMaxDist -> (string)

Applicable only when the value of Video:Codec is one of `H.264` , `MPEG2` , or `VP8` .

The maximum number of frames between key frames. Key frames are fully encoded frames; the frames between key frames are encoded based, in part, on the content of the key frames. The value is an integer formatted as a string; valid values are between 1 (every frame is a key frame) and 100000, inclusive. A higher value results in higher compression but may also discernibly decrease video quality.

For `Smooth` outputs, the `FrameRate` must have a constant ratio to the `KeyframesMaxDist` . This allows `Smooth` playlists to switch between different quality levels while the file is being played.

For example, an input file can have a `FrameRate` of 30 with a `KeyframesMaxDist` of 90. The output file then needs to have a ratio of 1:3. Valid outputs would have `FrameRate` of 30, 25, and 10, and `KeyframesMaxDist` of 90, 75, and 30, respectively.

Alternately, this can be achieved by setting `FrameRate` to auto and having the same values for `MaxFrameRate` and `KeyframesMaxDist` .

FixedGOP -> (string)

Applicable only when the value of Video:Codec is one of `H.264` , `MPEG2` , or `VP8` .

Whether to use a fixed value for `FixedGOP` . Valid values are `true` and `false` :

- `true` : Elastic Transcoder uses the value of `KeyframesMaxDist` for the distance between key frames (the number of frames in a group of pictures, or GOP).
- `false` : The distance between key frames can vary.

### Warning

`FixedGOP` must be set to `true` for `fmp4` containers.

BitRate -> (string)

The bit rate of the video stream in the output file, in kilobits/second. Valid values depend on the values of `Level` and `Profile` . If you specify `auto` , Elastic Transcoder uses the detected bit rate of the input source. If you specify a value other than `auto` , we recommend that you specify a value less than or equal to the maximum H.264-compliant value listed for your level and profile:

*Level - Maximum video bit rate in kilobits/second (baseline and main Profile) : maximum video bit rate in kilobits/second (high Profile)*

- 1 - 64 : 80
- 1b - 128 : 160
- 1.1 - 192 : 240
- 1.2 - 384 : 480
- 1.3 - 768 : 960
- 2 - 2000 : 2500
- 3 - 10000 : 12500
- 3.1 - 14000 : 17500
- 3.2 - 20000 : 25000
- 4 - 20000 : 25000
- 4.1 - 50000 : 62500

FrameRate -> (string)

The frames per second for the video stream in the output file. Valid values include:

`auto` , `10` , `15` , `23.97` , `24` , `25` , `29.97` , `30` , `60`

If you specify `auto` , Elastic Transcoder uses the detected frame rate of the input source. If you specify a frame rate, we recommend that you perform the following calculation:

`Frame rate = maximum recommended decoding speed in luma samples/second / (width in pixels * height in pixels)`

where:

- *width in pixels* and *height in pixels* represent the Resolution of the output video.
- *maximum recommended decoding speed in Luma samples/second* is less than or equal to the maximum value listed in the following table, based on the value that you specified for Level.

The maximum recommended decoding speed in Luma samples/second for each level is described in the following list (*Level - Decoding speed* ):

- 1 - 380160
- 1b - 380160
- 1.1 - 76800
- 1.2 - 1536000
- 1.3 - 3041280
- 2 - 3041280
- 2.1 - 5068800
- 2.2 - 5184000
- 3 - 10368000
- 3.1 - 27648000
- 3.2 - 55296000
- 4 - 62914560
- 4.1 - 62914560

MaxFrameRate -> (string)

If you specify `auto` for `FrameRate` , Elastic Transcoder uses the frame rate of the input video for the frame rate of the output video. Specify the maximum frame rate that you want Elastic Transcoder to use when the frame rate of the input video is greater than the desired maximum frame rate of the output video. Valid values include: `10` , `15` , `23.97` , `24` , `25` , `29.97` , `30` , `60` .

Resolution -> (string)

### Warning

To better control resolution and aspect ratio of output videos, we recommend that you use the values `MaxWidth` , `MaxHeight` , `SizingPolicy` , `PaddingPolicy` , and `DisplayAspectRatio` instead of `Resolution` and `AspectRatio` . The two groups of settings are mutually exclusive. Do not use them together.

The width and height of the video in the output file, in pixels. Valid values are `auto` and *width* x *height* :

- `auto` : Elastic Transcoder attempts to preserve the width and height of the input file, subject to the following rules.
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html#id1)*width* x *height* `` : The width and height of the output video in pixels.

Note the following about specifying the width and height:

- The width must be an even integer between 128 and 4096, inclusive.
- The height must be an even integer between 96 and 3072, inclusive.
- If you specify a resolution that is less than the resolution of the input file, Elastic Transcoder rescales the output file to the lower resolution.
- If you specify a resolution that is greater than the resolution of the input file, Elastic Transcoder rescales the output to the higher resolution.
- We recommend that you specify a resolution for which the product of width and height is less than or equal to the applicable value in the following list (*List - Max width x height value* ):
- 1 - 25344
- 1b - 25344
- 1.1 - 101376
- 1.2 - 101376
- 1.3 - 101376
- 2 - 101376
- 2.1 - 202752
- 2.2 - 404720
- 3 - 404720
- 3.1 - 921600
- 3.2 - 1310720
- 4 - 2097152
- 4.1 - 2097152

AspectRatio -> (string)

### Warning

To better control resolution and aspect ratio of output videos, we recommend that you use the values `MaxWidth` , `MaxHeight` , `SizingPolicy` , `PaddingPolicy` , and `DisplayAspectRatio` instead of `Resolution` and `AspectRatio` . The two groups of settings are mutually exclusive. Do not use them together.

The display aspect ratio of the video in the output file. Valid values include:

`auto` , `1:1` , `4:3` , `3:2` , `16:9`

If you specify `auto` , Elastic Transcoder tries to preserve the aspect ratio of the input file.

If you specify an aspect ratio for the output file that differs from aspect ratio of the input file, Elastic Transcoder adds pillarboxing (black bars on the sides) or letterboxing (black bars on the top and bottom) to maintain the aspect ratio of the active region of the video.

MaxWidth -> (string)

The maximum width of the output video in pixels. If you specify `auto` , Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 128 and 4096.

MaxHeight -> (string)

The maximum height of the output video in pixels. If you specify `auto` , Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 96 and 3072.

DisplayAspectRatio -> (string)

The value that Elastic Transcoder adds to the metadata in the output file.

SizingPolicy -> (string)

Specify one of the following values to control scaling of the output video:

- `Fit` : Elastic Transcoder scales the output video so it matches the value that you specified in either `MaxWidth` or `MaxHeight` without exceeding the other value.
- `Fill` : Elastic Transcoder scales the output video so it matches the value that you specified in either `MaxWidth` or `MaxHeight` and matches or exceeds the other value. Elastic Transcoder centers the output video and then crops it in the dimension (if any) that exceeds the maximum value.
- `Stretch` : Elastic Transcoder stretches the output video to match the values that you specified for `MaxWidth` and `MaxHeight` . If the relative proportions of the input video and the output video are different, the output video will be distorted.
- `Keep` : Elastic Transcoder does not scale the output video. If either dimension of the input video exceeds the values that you specified for `MaxWidth` and `MaxHeight` , Elastic Transcoder crops the output video.
- `ShrinkToFit` : Elastic Transcoder scales the output video down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without exceeding either value. If you specify this option, Elastic Transcoder does not scale the video up.
- `ShrinkToFill` : Elastic Transcoder scales the output video down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without dropping below either value. If you specify this option, Elastic Transcoder does not scale the video up.

PaddingPolicy -> (string)

When you set `PaddingPolicy` to `Pad` , Elastic Transcoder may add black bars to the top and bottom and/or left and right sides of the output video to make the total size of the output video match the values that you specified for `MaxWidth` and `MaxHeight` .

Watermarks -> (list)

Settings for the size, location, and opacity of graphics that you want Elastic Transcoder to overlay over videos that are transcoded using this preset. You can specify settings for up to four watermarks. Watermarks appear in the specified size and location, and with the specified opacity for the duration of the transcoded video.

Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.

When you create a job that uses this preset, you specify the .png or .jpg graphics that you want Elastic Transcoder to include in the transcoded videos. You can specify fewer graphics in the job than you specify watermark settings in the preset, which allows you to use the same preset for up to four watermarks that have different dimensions.

(structure)

Settings for the size, location, and opacity of graphics that you want Elastic Transcoder to overlay over videos that are transcoded using this preset. You can specify settings for up to four watermarks. Watermarks appear in the specified size and location, and with the specified opacity for the duration of the transcoded video.

Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.

When you create a job that uses this preset, you specify the .png or .jpg graphics that you want Elastic Transcoder to include in the transcoded videos. You can specify fewer graphics in the job than you specify watermark settings in the preset, which allows you to use the same preset for up to four watermarks that have different dimensions.

Id -> (string)

A unique identifier for the settings for one watermark. The value of `Id` can be up to 40 characters long.

MaxWidth -> (string)

The maximum width of the watermark in one of the following formats:

- number of pixels (px): The minimum value is 16 pixels, and the maximum value is the value of `MaxWidth` .
- integer percentage (%): The range of valid values is 0 to 100. Use the value of `Target` to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the calculation. If you specify the value in pixels, it must be less than or equal to the value of `MaxWidth` .

MaxHeight -> (string)

The maximum height of the watermark in one of the following formats:

- number of pixels (px): The minimum value is 16 pixels, and the maximum value is the value of `MaxHeight` .
- integer percentage (%): The range of valid values is 0 to 100. Use the value of `Target` to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the calculation.

If you specify the value in pixels, it must be less than or equal to the value of `MaxHeight` .

SizingPolicy -> (string)

A value that controls scaling of the watermark:

- **Fit** : Elastic Transcoder scales the watermark so it matches the value that you specified in either `MaxWidth` or `MaxHeight` without exceeding the other value.
- **Stretch** : Elastic Transcoder stretches the watermark to match the values that you specified for `MaxWidth` and `MaxHeight` . If the relative proportions of the watermark and the values of `MaxWidth` and `MaxHeight` are different, the watermark will be distorted.
- **ShrinkToFit** : Elastic Transcoder scales the watermark down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without exceeding either value. If you specify this option, Elastic Transcoder does not scale the watermark up.

HorizontalAlign -> (string)

The horizontal position of the watermark unless you specify a non-zero value for `HorizontalOffset` :

- **Left** : The left edge of the watermark is aligned with the left border of the video.
- **Right** : The right edge of the watermark is aligned with the right border of the video.
- **Center** : The watermark is centered between the left and right borders.

HorizontalOffset -> (string)

The amount by which you want the horizontal position of the watermark to be offset from the position specified by HorizontalAlign:

- number of pixels (px): The minimum value is 0 pixels, and the maximum value is the value of MaxWidth.
- integer percentage (%): The range of valid values is 0 to 100.

For example, if you specify Left for `HorizontalAlign` and 5px for `HorizontalOffset` , the left side of the watermark appears 5 pixels from the left border of the output video.

`HorizontalOffset` is only valid when the value of `HorizontalAlign` is `Left` or `Right` . If you specify an offset that causes the watermark to extend beyond the left or right border and Elastic Transcoder has not added black bars, the watermark is cropped. If Elastic Transcoder has added black bars, the watermark extends into the black bars. If the watermark extends beyond the black bars, it is cropped.

Use the value of `Target` to specify whether you want to include the black bars that are added by Elastic Transcoder, if any, in the offset calculation.

VerticalAlign -> (string)

The vertical position of the watermark unless you specify a non-zero value for `VerticalOffset` :

- **Top** : The top edge of the watermark is aligned with the top border of the video.
- **Bottom** : The bottom edge of the watermark is aligned with the bottom border of the video.
- **Center** : The watermark is centered between the top and bottom borders.

VerticalOffset -> (string)

`VerticalOffset`

The amount by which you want the vertical position of the watermark to be offset from the position specified by VerticalAlign:

- number of pixels (px): The minimum value is 0 pixels, and the maximum value is the value of `MaxHeight` .
- integer percentage (%): The range of valid values is 0 to 100.

For example, if you specify `Top` for `VerticalAlign` and `5px` for `VerticalOffset` , the top of the watermark appears 5 pixels from the top border of the output video.

`VerticalOffset` is only valid when the value of VerticalAlign is Top or Bottom.

If you specify an offset that causes the watermark to extend beyond the top or bottom border and Elastic Transcoder has not added black bars, the watermark is cropped. If Elastic Transcoder has added black bars, the watermark extends into the black bars. If the watermark extends beyond the black bars, it is cropped.

Use the value of `Target` to specify whether you want Elastic Transcoder to include the black bars that are added by Elastic Transcoder, if any, in the offset calculation.

Opacity -> (string)

A percentage that indicates how much you want a watermark to obscure the video in the location where it appears. Valid values are 0 (the watermark is invisible) to 100 (the watermark completely obscures the video in the specified location). The datatype of `Opacity` is float.

Elastic Transcoder supports transparent .png graphics. If you use a transparent .png, the transparent portion of the video appears as if you had specified a value of 0 for `Opacity` . The .jpg file format doesnât support transparency.

Target -> (string)

A value that determines how Elastic Transcoder interprets values that you specified for `HorizontalOffset` , `VerticalOffset` , `MaxWidth` , and `MaxHeight` :

- **Content** : `HorizontalOffset` and `VerticalOffset` values are calculated based on the borders of the video excluding black bars added by Elastic Transcoder, if any. In addition, `MaxWidth` and `MaxHeight` , if specified as a percentage, are calculated based on the borders of the video excluding black bars added by Elastic Transcoder, if any.
- **Frame** : `HorizontalOffset` and `VerticalOffset` values are calculated based on the borders of the video including black bars added by Elastic Transcoder, if any. In addition, `MaxWidth` and `MaxHeight` , if specified as a percentage, are calculated based on the borders of the video including black bars added by Elastic Transcoder, if any.

Thumbnails -> (structure)

A section of the response body that provides information about the thumbnail preset values, if any.

Format -> (string)

The format of thumbnails, if any. Valid values are `jpg` and `png` .

You specify whether you want Elastic Transcoder to create thumbnails when you create a job.

Interval -> (string)

The approximate number of seconds between thumbnails. Specify an integer value.

Resolution -> (string)

### Warning

To better control resolution and aspect ratio of thumbnails, we recommend that you use the values `MaxWidth` , `MaxHeight` , `SizingPolicy` , and `PaddingPolicy` instead of `Resolution` and `AspectRatio` . The two groups of settings are mutually exclusive. Do not use them together.

The width and height of thumbnail files in pixels. Specify a value in the format `` *width* `` x `` *height* `` where both values are even integers. The values cannot exceed the width and height that you specified in the `Video:Resolution` object.

AspectRatio -> (string)

### Warning

To better control resolution and aspect ratio of thumbnails, we recommend that you use the values `MaxWidth` , `MaxHeight` , `SizingPolicy` , and `PaddingPolicy` instead of `Resolution` and `AspectRatio` . The two groups of settings are mutually exclusive. Do not use them together.

The aspect ratio of thumbnails. Valid values include:

`auto` , `1:1` , `4:3` , `3:2` , `16:9`

If you specify `auto` , Elastic Transcoder tries to preserve the aspect ratio of the video in the output file.

MaxWidth -> (string)

The maximum width of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1920 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 4096.

MaxHeight -> (string)

The maximum height of thumbnails in pixels. If you specify auto, Elastic Transcoder uses 1080 (Full HD) as the default value. If you specify a numeric value, enter an even integer between 32 and 3072.

SizingPolicy -> (string)

Specify one of the following values to control scaling of thumbnails:

- `Fit` : Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail MaxWidth or MaxHeight settings without exceeding the other value.
- `Fill` : Elastic Transcoder scales thumbnails so they match the value that you specified in thumbnail `MaxWidth` or `MaxHeight` settings and matches or exceeds the other value. Elastic Transcoder centers the image in thumbnails and then crops in the dimension (if any) that exceeds the maximum value.
- `Stretch` : Elastic Transcoder stretches thumbnails to match the values that you specified for thumbnail `MaxWidth` and `MaxHeight` settings. If the relative proportions of the input video and thumbnails are different, the thumbnails will be distorted.
- `Keep` : Elastic Transcoder does not scale thumbnails. If either dimension of the input video exceeds the values that you specified for thumbnail `MaxWidth` and `MaxHeight` settings, Elastic Transcoder crops the thumbnails.
- `ShrinkToFit` : Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of thumbnail `MaxWidth` and `MaxHeight` without exceeding either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.
- `ShrinkToFill` : Elastic Transcoder scales thumbnails down so that their dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without dropping below either value. If you specify this option, Elastic Transcoder does not scale thumbnails up.

PaddingPolicy -> (string)

When you set `PaddingPolicy` to `Pad` , Elastic Transcoder may add black bars to the top and bottom and/or left and right sides of thumbnails to make the total size of the thumbnails match the values that you specified for thumbnail `MaxWidth` and `MaxHeight` settings.

Type -> (string)

Whether the preset is a default preset provided by Elastic Transcoder (`System` ) or a preset that you have defined (`Custom` ).

NextPageToken -> (string)

A value that you use to access the second and subsequent pages of results, if any. When the presets fit on one page or when youâve reached the last page of results, the value of `NextPageToken` is `null` .