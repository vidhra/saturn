# get-trailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# get-trail

## Description

Returns settings information for a specified trail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetTrail)

## Synopsis

```
get-trail
--name <value>
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

`--name` (string)

The name or the Amazon Resource Name (ARN) of the trail for which you want to retrieve settings information.

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

Trail -> (structure)

The settings for a trail.

Name -> (string)

Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

S3BucketName -> (string)

Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See [Amazon S3 Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) .

S3KeyPrefix -> (string)

Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files) . The maximum length is 200 characters.

SnsTopicName -> (string)

This field is no longer in use. Use `SnsTopicARN` .

SnsTopicARN -> (string)

Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.

`arn:aws:sns:us-east-2:123456789012:MyTopic`

IncludeGlobalServiceEvents -> (boolean)

Set to **True** to include Amazon Web Services API calls from Amazon Web Services global services such as IAM. Otherwise, **False** .

IsMultiRegionTrail -> (boolean)

Specifies whether the trail exists only in one Region or exists in all Regions.

HomeRegion -> (string)

The Region in which the trail was created.

TrailARN -> (string)

Specifies the ARN of the trail. The following is the format of a trail ARN.

`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`

LogFileValidationEnabled -> (boolean)

Specifies whether log file validation is enabled.

CloudWatchLogsLogGroupArn -> (string)

Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn -> (string)

Specifies the role for the CloudWatch Logs endpoint to assume to write to a userâs log group.

KmsKeyId -> (string)

Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.

`arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`

HasCustomEventSelectors -> (boolean)

Specifies if the trail has custom event selectors.

HasInsightSelectors -> (boolean)

Specifies whether a trail has insight types specified in an `InsightSelector` list.

IsOrganizationTrail -> (boolean)

Specifies whether the trail is an organization trail.