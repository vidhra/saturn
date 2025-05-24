# create-trailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# create-trail

## Description

Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/CreateTrail)

## Synopsis

```
create-trail
--name <value>
--s3-bucket-name <value>
[--s3-key-prefix <value>]
[--sns-topic-name <value>]
[--include-global-service-events | --no-include-global-service-events]
[--is-multi-region-trail | --no-is-multi-region-trail]
[--enable-log-file-validation | --no-enable-log-file-validation]
[--cloud-watch-logs-log-group-arn <value>]
[--cloud-watch-logs-role-arn <value>]
[--kms-key-id <value>]
[--is-organization-trail | --no-is-organization-trail]
[--tags-list <value>]
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

Specifies the name of the trail. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
- Start with a letter or number, and end with a letter or number
- Be between 3 and 128 characters
- Have no adjacent periods, underscores or dashes. Names like `my-_namespace` and `my--namespace` are not valid.
- Not be in IP address format (for example, 192.168.5.4)

`--s3-bucket-name` (string)

Specifies the name of the Amazon S3 bucket designated for publishing log files. For information about bucket naming rules, see [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the *Amazon Simple Storage Service User Guide* .

`--s3-key-prefix` (string)

Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files) . The maximum length is 200 characters.

`--sns-topic-name` (string)

Specifies the name or ARN of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

`--include-global-service-events` | `--no-include-global-service-events` (boolean)

Specifies whether the trail is publishing events from global services such as IAM to the log files.

`--is-multi-region-trail` | `--no-is-multi-region-trail` (boolean)

Specifies whether the trail is created in the current Region or in all Regions. The default is false, which creates a trail only in the Region where you are signed in. As a best practice, consider creating trails that log events in all Regions.

`--enable-log-file-validation` | `--no-enable-log-file-validation` (boolean)

Specifies whether log file integrity validation is enabled. The default is false.

### Note

When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.

`--cloud-watch-logs-log-group-arn` (string)

Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. You must use a log group that exists in your account.

Not required unless you specify `CloudWatchLogsRoleArn` .

`--cloud-watch-logs-role-arn` (string)

Specifies the role for the CloudWatch Logs endpoint to assume to write to a userâs log group. You must use a role that exists in your account.

`--kms-key-id` (string)

Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by `alias/` , a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.

CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see [Using multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

Examples:

- `alias/MyAliasName`
- `arn:aws:kms:us-east-2:123456789012:alias/MyAliasName`
- `arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`
- `12345678-1234-1234-1234-123456789012`

`--is-organization-trail` | `--no-is-organization-trail` (boolean)

Specifies whether the trail is created for all accounts in an organization in Organizations, or only for the current Amazon Web Services account. The default is false, and cannot be true unless the call is made on behalf of an Amazon Web Services account that is the management account or delegated administrator account for an organization in Organizations.

`--tags-list` (list)

A list of tags.

(structure)

A custom key-value pair associated with a resource such as a CloudTrail trail, event data store, dashboard, or channel.

Key -> (string)

The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.

Value -> (string)

The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

**To create a trail**

The following `create-trail` example creates a multi-region trail named `Trail1` and specifies an S3 bucket.

```
aws cloudtrail create-trail \
    --name Trail1 \
    --s3-bucket-name amzn-s3-demo-bucket \
    --is-multi-region-trail
```

Output:

```
{
    "IncludeGlobalServiceEvents": true,
    "Name": "Trail1",
    "TrailARN": "arn:aws:cloudtrail:us-west-2:123456789012:trail/Trail1",
    "LogFileValidationEnabled": false,
    "IsMultiRegionTrail": true,
    "S3BucketName": "amzn-s3-demo-bucket"
}
```

## Output

Name -> (string)

Specifies the name of the trail.

S3BucketName -> (string)

Specifies the name of the Amazon S3 bucket designated for publishing log files.

S3KeyPrefix -> (string)

Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see [Finding Your CloudTrail Log Files](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files) .

SnsTopicName -> (string)

This field is no longer in use. Use `SnsTopicARN` .

SnsTopicARN -> (string)

Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

`arn:aws:sns:us-east-2:123456789012:MyTopic`

IncludeGlobalServiceEvents -> (boolean)

Specifies whether the trail is publishing events from global services such as IAM to the log files.

IsMultiRegionTrail -> (boolean)

Specifies whether the trail exists in one Region or in all Regions.

TrailARN -> (string)

Specifies the ARN of the trail that was created. The format of a trail ARN is:

`arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`

LogFileValidationEnabled -> (boolean)

Specifies whether log file integrity validation is enabled.

CloudWatchLogsLogGroupArn -> (string)

Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.

CloudWatchLogsRoleArn -> (string)

Specifies the role for the CloudWatch Logs endpoint to assume to write to a userâs log group.

KmsKeyId -> (string)

Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.

`arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012`

IsOrganizationTrail -> (boolean)

Specifies whether the trail is an organization trail.