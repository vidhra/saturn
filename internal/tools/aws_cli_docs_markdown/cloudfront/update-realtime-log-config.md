# update-realtime-log-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-realtime-log-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-realtime-log-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# update-realtime-log-config

## Description

Updates a real-time log configuration.

When you update a real-time log configuration, all the parameters are updated with the values provided in the request. You cannot update some parameters independent of others. To update a real-time log configuration:

- Call `GetRealtimeLogConfig` to get the current real-time log configuration.
- Locally modify the parameters in the real-time log configuration that you want to update.
- Call this API (`UpdateRealtimeLogConfig` ) by providing the entire real-time log configuration, including the parameters that you modified and those that you didnât.

You cannot update a real-time log configurationâs `Name` or `ARN` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/UpdateRealtimeLogConfig)

## Synopsis

```
update-realtime-log-config
[--end-points <value>]
[--fields <value>]
[--name <value>]
[--arn <value>]
[--sampling-rate <value>]
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

`--end-points` (list)

Contains information about the Amazon Kinesis data stream where you are sending real-time log data.

(structure)

Contains information about the Amazon Kinesis data stream where youâre sending real-time log data in a real-time log configuration.

StreamType -> (string)

The type of data stream where you are sending real-time log data. The only valid value is `Kinesis` .

KinesisStreamConfig -> (structure)

Contains information about the Amazon Kinesis data stream where you are sending real-time log data in a real-time log configuration.

RoleARN -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFront can use to send real-time log data to your Kinesis data stream.

For more information the IAM role, see [Real-time log configuration IAM role](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role) in the *Amazon CloudFront Developer Guide* .

StreamARN -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending real-time log data.

Shorthand Syntax:

```
StreamType=string,KinesisStreamConfig={RoleARN=string,StreamARN=string} ...
```

JSON Syntax:

```
[
  {
    "StreamType": "string",
    "KinesisStreamConfig": {
      "RoleARN": "string",
      "StreamARN": "string"
    }
  }
  ...
]
```

`--fields` (list)

A list of fields to include in each real-time log record.

For more information about fields, see [Real-time log configuration fields](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) in the *Amazon CloudFront Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--name` (string)

The name for this real-time log configuration.

`--arn` (string)

The Amazon Resource Name (ARN) for this real-time log configuration.

`--sampling-rate` (long)

The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. You must provide an integer between 1 and 100, inclusive.

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

RealtimeLogConfig -> (structure)

A real-time log configuration.

ARN -> (string)

The Amazon Resource Name (ARN) of this real-time log configuration.

Name -> (string)

The unique name of this real-time log configuration.

SamplingRate -> (long)

The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. The sampling rate is an integer between 1 and 100, inclusive.

EndPoints -> (list)

Contains information about the Amazon Kinesis data stream where you are sending real-time log data for this real-time log configuration.

(structure)

Contains information about the Amazon Kinesis data stream where youâre sending real-time log data in a real-time log configuration.

StreamType -> (string)

The type of data stream where you are sending real-time log data. The only valid value is `Kinesis` .

KinesisStreamConfig -> (structure)

Contains information about the Amazon Kinesis data stream where you are sending real-time log data in a real-time log configuration.

RoleARN -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFront can use to send real-time log data to your Kinesis data stream.

For more information the IAM role, see [Real-time log configuration IAM role](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role) in the *Amazon CloudFront Developer Guide* .

StreamARN -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending real-time log data.

Fields -> (list)

A list of fields that are included in each real-time log record. In an API response, the fields are provided in the same order in which they are sent to the Amazon Kinesis data stream.

For more information about fields, see [Real-time log configuration fields](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields) in the *Amazon CloudFront Developer Guide* .

(string)