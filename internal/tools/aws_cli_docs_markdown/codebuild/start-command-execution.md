# start-command-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-command-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-command-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# start-command-execution

## Description

Starts a command execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StartCommandExecution)

## Synopsis

```
start-command-execution
--sandbox-id <value>
--command <value>
[--type <value>]
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

`--sandbox-id` (string)

A `sandboxId` or `sandboxArn` .

`--command` (string)

The command that needs to be executed.

`--type` (string)

The command type.

Possible values:

- `SHELL`

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

commandExecution -> (structure)

Information about the requested command executions.

id -> (string)

The ID of the command execution.

sandboxId -> (string)

A `sandboxId` .

submitTime -> (timestamp)

When the command execution process was initially submitted, expressed in Unix time format.

startTime -> (timestamp)

When the command execution process started, expressed in Unix time format.

endTime -> (timestamp)

When the command execution process ended, expressed in Unix time format.

status -> (string)

The status of the command execution.

command -> (string)

The command that needs to be executed.

type -> (string)

The command type.

exitCode -> (string)

The exit code to return upon completion.

standardOutputContent -> (string)

The text written by the command to stdout.

standardErrContent -> (string)

The text written by the command to stderr.

logs -> (structure)

Information about build logs in CloudWatch Logs.

groupName -> (string)

The name of the CloudWatch Logs group for the build logs.

streamName -> (string)

The name of the CloudWatch Logs stream for the build logs.

deepLink -> (string)

The URL to an individual build log in CloudWatch Logs. The log stream is created during the PROVISIONING phase of a build and the `deeplink` will not be valid until it is created.

s3DeepLink -> (string)

The URL to a build log in an S3 bucket.

cloudWatchLogsArn -> (string)

The ARN of the CloudWatch Logs stream for a build execution. Its format is `arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}` . The CloudWatch Logs stream is created during the PROVISIONING phase of a build and the ARN will not be valid until it is created. For more information, see [Resources Defined by CloudWatch Logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies) .

s3LogsArn -> (string)

The ARN of S3 logs for a build project. Its format is `arn:${Partition}:s3:::${BucketName}/${ObjectName}` . For more information, see [Resources Defined by Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies) .

cloudWatchLogs -> (structure)

Information about CloudWatch Logs for a build project.

status -> (string)

The current status of the logs in CloudWatch Logs for a build project. Valid values are:

- `ENABLED` : CloudWatch Logs are enabled for this build project.
- `DISABLED` : CloudWatch Logs are not enabled for this build project.

groupName -> (string)

The group name of the logs in CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

streamName -> (string)

The prefix of the stream name of the CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

s3Logs -> (structure)

Information about S3 logs for a build project.

status -> (string)

The current status of the S3 build logs. Valid values are:

- `ENABLED` : S3 build logs are enabled for this build project.
- `DISABLED` : S3 build logs are not enabled for this build project.

location -> (string)

The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is `my-bucket` , and your path prefix is `build-log` , then acceptable formats are `my-bucket/build-log` or `arn:aws:s3:::my-bucket/build-log` .

encryptionDisabled -> (boolean)

Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

sandboxArn -> (string)

A `sandboxArn` .