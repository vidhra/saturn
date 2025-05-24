# describe-vod-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/describe-vod-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/describe-vod-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediatailor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/index.html#cli-aws-mediatailor) ]

# describe-vod-source

## Description

Provides details about a specific video on demand (VOD) source in a specific source location.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediatailor-2018-04-23/DescribeVodSource)

## Synopsis

```
describe-vod-source
--source-location-name <value>
--vod-source-name <value>
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

`--source-location-name` (string)

The name of the source location associated with this VOD Source.

`--vod-source-name` (string)

The name of the VOD Source.

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

AdBreakOpportunities -> (list)

The ad break opportunities within the VOD source.

(structure)

A location at which a zero-duration ad marker was detected in a VOD source manifest.

OffsetMillis -> (long)

The offset in milliseconds from the start of the VOD source at which an ad marker was detected.

Arn -> (string)

The ARN of the VOD source.

CreationTime -> (timestamp)

The timestamp that indicates when the VOD source was created.

HttpPackageConfigurations -> (list)

The HTTP package configurations.

(structure)

The HTTP package configuration properties for the requested VOD source.

Path -> (string)

The relative path to the URL for this VOD source. This is combined with `SourceLocation::HttpConfiguration::BaseUrl` to form a valid URL.

SourceGroup -> (string)

The name of the source group. This has to match one of the `Channel::Outputs::SourceGroup` .

Type -> (string)

The streaming protocol for this package configuration. Supported values are `HLS` and `DASH` .

LastModifiedTime -> (timestamp)

The last modified time of the VOD source.

SourceLocationName -> (string)

The name of the source location associated with the VOD source.

Tags -> (map)

The tags assigned to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html) .

key -> (string)

value -> (string)

VodSourceName -> (string)

The name of the VOD source.