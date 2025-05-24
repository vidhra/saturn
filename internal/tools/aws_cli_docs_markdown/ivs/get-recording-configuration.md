# get-recording-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-recording-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-recording-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/index.html#cli-aws-ivs) ]

# get-recording-configuration

## Description

Gets the recording configuration for the specified ARN.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-2020-07-14/GetRecordingConfiguration)

## Synopsis

```
get-recording-configuration
--arn <value>
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

`--arn` (string)

ARN of the recording configuration to be retrieved.

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

**To get information about a RecordingConfiguration resource**

The following `get-recording-configuration` example gets information about the RecordingConfiguration resource for the specified ARN.

```
aws ivs get-recording-configuration \
    --arn "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ"
```

Output:

```
{
    "recordingConfiguration": {
        "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ",
        "destinationConfiguration": {
            "s3": {
                "bucketName": "demo-recording-bucket"
            }
        },
        "name": "test-recording-config",
        "recordingReconnectWindowSeconds": 60,
        "state": "ACTIVE",
        "tags": {
            "key1" : "value1",
            "key2" : "value2"
        },
        "thumbnailConfiguration": {
            "recordingMode": "INTERVAL",
            "targetIntervalSeconds": 1,
            "resolution": "LOWEST_RESOLUTION",
            "storage": [
                "LATEST"
            ]
        },
        "renditionConfiguration": {
            "renditionSelection": "CUSTOM",
            "renditions": [
                "HD"
            ]
        }
    }
}
```

For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html) in the *Amazon Interactive Video Service User Guide*.

## Output

recordingConfiguration -> (structure)

arn -> (string)

Recording-configuration ARN.

destinationConfiguration -> (structure)

A complex type that contains information about where recorded video will be stored.

s3 -> (structure)

An S3 destination configuration where recorded videos will be stored.

bucketName -> (string)

Location (S3 bucket name) where recorded videos will be stored.

name -> (string)

Recording-configuration name. The value does not need to be unique.

recordingReconnectWindowSeconds -> (integer)

If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.

renditionConfiguration -> (structure)

Object that describes which renditions should be recorded for a stream.

renditionSelection -> (string)

Indicates which set of renditions are recorded for a stream. For `BASIC` channels, the `CUSTOM` value has no effect. If `CUSTOM` is specified, a set of renditions must be specified in the `renditions` field. Default: `ALL` .

renditions -> (list)

Indicates which renditions are recorded for a stream, if `renditionSelection` is `CUSTOM` ; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html) .

(string)

state -> (string)

Indicates the current state of the recording configuration. When the state is `ACTIVE` , the configuration is ready for recording a channel stream.

tags -> (map)

Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS has no service-specific constraints beyond what is documented there.

key -> (string)

value -> (string)

thumbnailConfiguration -> (structure)

A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.

recordingMode -> (string)

Thumbnail recording mode. Default: `INTERVAL` .

resolution -> (string)

Indicates the desired resolution of recorded thumbnails. Thumbnails are recorded at the selected resolution if the corresponding rendition is available during the stream; otherwise, they are recorded at source resolution. For more information about resolution values and their corresponding height and width dimensions, see [Auto-Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html) . Default: Null (source resolution is returned).

storage -> (list)

Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails directory. `LATEST` saves the latest thumbnail in media/latest_thumbnail/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds` . You can enable both `SEQUENTIAL` and `LATEST` . Default: `SEQUENTIAL` .

(string)

targetIntervalSeconds -> (long)

The targeted thumbnail-generation interval in seconds. This is configurable (and required) only if `recordingMode` is `INTERVAL` . Default: 60.

**Important:** For the `BASIC` channel type, or the `STANDARD` channel type with multitrack input, setting a value for `targetIntervalSeconds` does not guarantee that thumbnails are generated at the specified interval. For thumbnails to be generated at the `targetIntervalSeconds` interval, the `IDR/Keyframe` value for the input video must be less than the `targetIntervalSeconds` value. See [Amazon IVS Streaming Configuration](https://docs.aws.amazon.com/ivs/latest/userguide/streaming-config.html) for information on setting `IDR/Keyframe` to the recommended value in video-encoder settings.