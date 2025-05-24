# create-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/create-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediapackagev2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/index.html#cli-aws-mediapackagev2) ]

# create-channel

## Description

Create a channel to start receiving content streams. The channel represents the input to MediaPackage for incoming live content from an encoder such as AWS Elemental MediaLive. The channel receives content, and after packaging it, outputs it through an origin endpoint to downstream devices (such as video players or CDNs) that request the content. You can create only one channel with each request. We recommend that you spread out channels between channel groups, such as putting redundant channels in the same AWS Region in different channel groups.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackagev2-2022-12-25/CreateChannel)

## Synopsis

```
create-channel
--channel-group-name <value>
--channel-name <value>
[--client-token <value>]
[--input-type <value>]
[--description <value>]
[--input-switch-configuration <value>]
[--output-header-configuration <value>]
[--tags <value>]
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

`--channel-group-name` (string)

The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.

`--channel-name` (string)

The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. You canât change the name after you create the channel.

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure the idempotency of the request.

`--input-type` (string)

The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.

The allowed values are:

- `HLS` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
- `CMAF` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).

Possible values:

- `HLS`
- `CMAF`

`--description` (string)

Enter any descriptive text that helps you to identify the channel.

`--input-switch-configuration` (structure)

The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when `InputType` is `CMAF` .

MQCSInputSwitching -> (boolean)

When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is true. This setting is valid only when `InputType` is `CMAF` .

Shorthand Syntax:

```
MQCSInputSwitching=boolean
```

JSON Syntax:

```
{
  "MQCSInputSwitching": true|false
}
```

`--output-header-configuration` (structure)

The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when `InputType` is `CMAF` .

PublishMQCS -> (boolean)

When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when `InputType` is `CMAF` .

Shorthand Syntax:

```
PublishMQCS=boolean
```

JSON Syntax:

```
{
  "PublishMQCS": true|false
}
```

`--tags` (map)

A comma-separated list of tag key:value pairs that you define. For example:

`"Key1": "Value1",`

`"Key2": "Value2"`

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

Arn -> (string)

The Amazon Resource Name (ARN) associated with the resource.

ChannelName -> (string)

The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.

ChannelGroupName -> (string)

The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.

CreatedAt -> (timestamp)

The date and time the channel was created.

ModifiedAt -> (timestamp)

The date and time the channel was modified.

Description -> (string)

The description for your channel.

IngestEndpoints -> (list)

The list of ingest endpoints.

(structure)

The ingest domain URL where the source stream should be sent.

Id -> (string)

The system-generated unique identifier for the IngestEndpoint.

Url -> (string)

The ingest domain URL where the source stream should be sent.

InputType -> (string)

The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.

The allowed values are:

- `HLS` - The HLS streaming specification (which defines M3U8 manifests and TS segments).
- `CMAF` - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).

ETag -> (string)

The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.

Tags -> (map)

The comma-separated list of tag key:value pairs assigned to the channel.

key -> (string)

value -> (string)

InputSwitchConfiguration -> (structure)

The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when `InputType` is `CMAF` .

MQCSInputSwitching -> (boolean)

When true, AWS Elemental MediaPackage performs input switching based on the MQCS. Default is true. This setting is valid only when `InputType` is `CMAF` .

OutputHeaderConfiguration -> (structure)

The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when `InputType` is `CMAF` .

PublishMQCS -> (boolean)

When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when `InputType` is `CMAF` .