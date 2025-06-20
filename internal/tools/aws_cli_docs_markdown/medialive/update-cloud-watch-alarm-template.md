# update-cloud-watch-alarm-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-cloud-watch-alarm-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-cloud-watch-alarm-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# update-cloud-watch-alarm-template

## Description

Updates the specified cloudwatch alarm template.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/UpdateCloudWatchAlarmTemplate)

## Synopsis

```
update-cloud-watch-alarm-template
[--comparison-operator <value>]
[--datapoints-to-alarm <value>]
[--description <value>]
[--evaluation-periods <value>]
[--group-identifier <value>]
--identifier <value>
[--metric-name <value>]
[--name <value>]
[--period <value>]
[--statistic <value>]
[--target-resource-type <value>]
[--threshold <value>]
[--treat-missing-data <value>]
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

`--comparison-operator` (string)
The comparison operator used to compare the specified statistic and the threshold.

Possible values:

- `GreaterThanOrEqualToThreshold`
- `GreaterThanThreshold`
- `LessThanThreshold`
- `LessThanOrEqualToThreshold`

`--datapoints-to-alarm` (integer)
The number of datapoints within the evaluation period that must be breaching to trigger the alarm.

`--description` (string)
A resourceâs optional description.

`--evaluation-periods` (integer)
The number of periods over which data is compared to the specified threshold.

`--group-identifier` (string)
A cloudwatch alarm template groupâs identifier. Can be either be its id or current name.

`--identifier` (string)
A cloudwatch alarm templateâs identifier. Can be either be its id or current name.

`--metric-name` (string)
The name of the metric associated with the alarm. Must be compatible with targetResourceType.

`--name` (string)
A resourceâs name. Names must be unique within the scope of a resource type in a specific region.

`--period` (integer)
The period, in seconds, over which the specified statistic is applied.

`--statistic` (string)
The statistic to apply to the alarmâs metric data.

Possible values:

- `SampleCount`
- `Average`
- `Sum`
- `Minimum`
- `Maximum`

`--target-resource-type` (string)
The resource type this template should dynamically generate cloudwatch metric alarms for.

Possible values:

- `CLOUDFRONT_DISTRIBUTION`
- `MEDIALIVE_MULTIPLEX`
- `MEDIALIVE_CHANNEL`
- `MEDIALIVE_INPUT_DEVICE`
- `MEDIAPACKAGE_CHANNEL`
- `MEDIAPACKAGE_ORIGIN_ENDPOINT`
- `MEDIACONNECT_FLOW`
- `S3_BUCKET`
- `MEDIATAILOR_PLAYBACK_CONFIGURATION`

`--threshold` (double)
The threshold value to compare with the specified statistic.

`--treat-missing-data` (string)
Specifies how missing data points are treated when evaluating the alarmâs condition.

Possible values:

- `notBreaching`
- `breaching`
- `ignore`
- `missing`

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

A cloudwatch alarm templateâs ARN (Amazon Resource Name)

ComparisonOperator -> (string)

The comparison operator used to compare the specified statistic and the threshold.

CreatedAt -> (timestamp)

Placeholder documentation for __timestampIso8601

DatapointsToAlarm -> (integer)

The number of datapoints within the evaluation period that must be breaching to trigger the alarm.

Description -> (string)

A resourceâs optional description.

EvaluationPeriods -> (integer)

The number of periods over which data is compared to the specified threshold.

GroupId -> (string)

A cloudwatch alarm template groupâs id. AWS provided template groups have ids that start with aws-

Id -> (string)

A cloudwatch alarm templateâs id. AWS provided templates have ids that start with aws-

MetricName -> (string)

The name of the metric associated with the alarm. Must be compatible with targetResourceType.

ModifiedAt -> (timestamp)

Placeholder documentation for __timestampIso8601

Name -> (string)

A resourceâs name. Names must be unique within the scope of a resource type in a specific region.

Period -> (integer)

The period, in seconds, over which the specified statistic is applied.

Statistic -> (string)

The statistic to apply to the alarmâs metric data.

Tags -> (map)

Represents the tags associated with a resource.

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string

TargetResourceType -> (string)

The resource type this template should dynamically generate cloudwatch metric alarms for.

Threshold -> (double)

The threshold value to compare with the specified statistic.

TreatMissingData -> (string)

Specifies how missing data points are treated when evaluating the alarmâs condition.