# put-bucket-notification-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3api](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html#cli-aws-s3api) ]

# put-bucket-notification-configuration

## Description

### Note

This operation is not supported for directory buckets.

Enables notifications of specified events for a bucket. For more information about event notifications, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) .

Using this API, you can replace an existing notification configuration. The configuration is an XML file that defines the event types that you want Amazon S3 to publish and the destination where you want Amazon S3 to publish an event notification when it detects an event of the specified type.

By default, your bucket has no event notifications configured. That is, the notification configuration will be an empty `NotificationConfiguration` .

`<NotificationConfiguration>`

`</NotificationConfiguration>`

This action replaces the existing notification configuration with the configuration you include in the request body.

After Amazon S3 receives this request, it first verifies that any Amazon Simple Notification Service (Amazon SNS) or Amazon Simple Queue Service (Amazon SQS) destination exists, and that the bucket owner has permission to publish to it by sending a test notification. In the case of Lambda destinations, Amazon S3 verifies that the Lambda function permissions grant Amazon S3 permission to invoke the function from the Amazon S3 bucket. For more information, see [Configuring Notifications for Amazon S3 Events](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) .

You can disable notifications by adding the empty NotificationConfiguration element.

For more information about the number of event notification configurations that you can create per bucket, see [Amazon S3 service quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3) in *Amazon Web Services General Reference* .

By default, only the bucket owner can configure notifications on a bucket. However, bucket owners can use a bucket policy to grant permission to other users to set this configuration with the required `s3:PutBucketNotification` permission.

### Note

The PUT notification is an atomic operation. For example, suppose your notification configuration includes SNS topic, SQS queue, and Lambda function configurations. When you send a PUT request with this configuration, Amazon S3 sends test messages to your SNS topic. If the message fails, the entire PUT action will fail, and Amazon S3 will not add the configuration to your bucket.

If the configuration in the request body includes only one `TopicConfiguration` specifying only the `s3:ReducedRedundancyLostObject` event type, the response will also include the `x-amz-sns-test-message-id` header containing the message ID of the test notification sent to the topic.

The following action is related to `PutBucketNotificationConfiguration` :

- [GetBucketNotificationConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/PutBucketNotificationConfiguration)

## Synopsis

```
put-bucket-notification-configuration
--bucket <value>
--notification-configuration <value>
[--expected-bucket-owner <value>]
[--skip-destination-validation | --no-skip-destination-validation]
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

`--bucket` (string)

The name of the bucket.

`--notification-configuration` (structure)

A container for specifying the notification configuration of the bucket. If this element is empty, notifications are turned off for the bucket.

TopicConfigurations -> (list)

The topic to which notifications are sent and the events for which notifications are generated.

(structure)

A container for specifying the configuration for publication of messages to an Amazon Simple Notification Service (Amazon SNS) topic when Amazon S3 detects specified events.

Id -> (string)

An optional unique identifier for configurations in a notification configuration. If you donât provide one, Amazon S3 will assign an ID.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to which Amazon S3 publishes a message when it detects events of the specified type.

Events -> (list)

The Amazon S3 bucket event about which to send notifications. For more information, see [Supported Event Types](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

(string)

The bucket event for which to send notifications.

Filter -> (structure)

Specifies object key name filtering rules. For information about key name filtering, see [Configuring event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the *Amazon S3 User Guide* .

Key -> (structure)

A container for object key name prefix and suffix filtering rules.

FilterRules -> (list)

A list of containers for the key-value pair that defines the criteria for the filter rule.

(structure)

Specifies the Amazon S3 object key name to filter on. An object key name is the name assigned to an object in your Amazon S3 bucket. You specify whether to filter on the suffix or prefix of the object key name. A prefix is a specific string of characters at the beginning of an object key name, which you can use to organize objects. For example, you can start the key names of related objects with a prefix, such as `2023-` or `engineering/` . Then, you can use `FilterRule` to find objects in a bucket with key names that have the same prefix. A suffix is similar to a prefix, but it is at the end of the object key name instead of at the beginning.

Name -> (string)

The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

Value -> (string)

The value that the filter searches for in object key names.

QueueConfigurations -> (list)

The Amazon Simple Queue Service queues to publish messages to and the events for which to publish messages.

(structure)

Specifies the configuration for publishing messages to an Amazon Simple Queue Service (Amazon SQS) queue when Amazon S3 detects specified events.

Id -> (string)

An optional unique identifier for configurations in a notification configuration. If you donât provide one, Amazon S3 will assign an ID.

QueueArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.

Events -> (list)

A collection of bucket events for which to send notifications

(string)

The bucket event for which to send notifications.

Filter -> (structure)

Specifies object key name filtering rules. For information about key name filtering, see [Configuring event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the *Amazon S3 User Guide* .

Key -> (structure)

A container for object key name prefix and suffix filtering rules.

FilterRules -> (list)

A list of containers for the key-value pair that defines the criteria for the filter rule.

(structure)

Specifies the Amazon S3 object key name to filter on. An object key name is the name assigned to an object in your Amazon S3 bucket. You specify whether to filter on the suffix or prefix of the object key name. A prefix is a specific string of characters at the beginning of an object key name, which you can use to organize objects. For example, you can start the key names of related objects with a prefix, such as `2023-` or `engineering/` . Then, you can use `FilterRule` to find objects in a bucket with key names that have the same prefix. A suffix is similar to a prefix, but it is at the end of the object key name instead of at the beginning.

Name -> (string)

The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

Value -> (string)

The value that the filter searches for in object key names.

LambdaFunctionConfigurations -> (list)

Describes the Lambda functions to invoke and the events for which to invoke them.

(structure)

A container for specifying the configuration for Lambda notifications.

Id -> (string)

An optional unique identifier for configurations in a notification configuration. If you donât provide one, Amazon S3 will assign an ID.

LambdaFunctionArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function that Amazon S3 invokes when the specified event type occurs.

Events -> (list)

The Amazon S3 bucket event for which to invoke the Lambda function. For more information, see [Supported Event Types](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

(string)

The bucket event for which to send notifications.

Filter -> (structure)

Specifies object key name filtering rules. For information about key name filtering, see [Configuring event notifications using object key name filtering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-how-to-filtering.html) in the *Amazon S3 User Guide* .

Key -> (structure)

A container for object key name prefix and suffix filtering rules.

FilterRules -> (list)

A list of containers for the key-value pair that defines the criteria for the filter rule.

(structure)

Specifies the Amazon S3 object key name to filter on. An object key name is the name assigned to an object in your Amazon S3 bucket. You specify whether to filter on the suffix or prefix of the object key name. A prefix is a specific string of characters at the beginning of an object key name, which you can use to organize objects. For example, you can start the key names of related objects with a prefix, such as `2023-` or `engineering/` . Then, you can use `FilterRule` to find objects in a bucket with key names that have the same prefix. A suffix is similar to a prefix, but it is at the end of the object key name instead of at the beginning.

Name -> (string)

The object key name prefix or suffix identifying one or more objects to which the filtering rule applies. The maximum length is 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, see [Configuring Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html) in the *Amazon S3 User Guide* .

Value -> (string)

The value that the filter searches for in object key names.

EventBridgeConfiguration -> (structure)

Enables delivery of events to Amazon EventBridge.

JSON Syntax:

```
{
  "TopicConfigurations": [
    {
      "Id": "string",
      "TopicArn": "string",
      "Events": ["s3:ReducedRedundancyLostObject"|"s3:ObjectCreated:*"|"s3:ObjectCreated:Put"|"s3:ObjectCreated:Post"|"s3:ObjectCreated:Copy"|"s3:ObjectCreated:CompleteMultipartUpload"|"s3:ObjectRemoved:*"|"s3:ObjectRemoved:Delete"|"s3:ObjectRemoved:DeleteMarkerCreated"|"s3:ObjectRestore:*"|"s3:ObjectRestore:Post"|"s3:ObjectRestore:Completed"|"s3:Replication:*"|"s3:Replication:OperationFailedReplication"|"s3:Replication:OperationNotTracked"|"s3:Replication:OperationMissedThreshold"|"s3:Replication:OperationReplicatedAfterThreshold"|"s3:ObjectRestore:Delete"|"s3:LifecycleTransition"|"s3:IntelligentTiering"|"s3:ObjectAcl:Put"|"s3:LifecycleExpiration:*"|"s3:LifecycleExpiration:Delete"|"s3:LifecycleExpiration:DeleteMarkerCreated"|"s3:ObjectTagging:*"|"s3:ObjectTagging:Put"|"s3:ObjectTagging:Delete", ...],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "prefix"|"suffix",
              "Value": "string"
            }
            ...
          ]
        }
      }
    }
    ...
  ],
  "QueueConfigurations": [
    {
      "Id": "string",
      "QueueArn": "string",
      "Events": ["s3:ReducedRedundancyLostObject"|"s3:ObjectCreated:*"|"s3:ObjectCreated:Put"|"s3:ObjectCreated:Post"|"s3:ObjectCreated:Copy"|"s3:ObjectCreated:CompleteMultipartUpload"|"s3:ObjectRemoved:*"|"s3:ObjectRemoved:Delete"|"s3:ObjectRemoved:DeleteMarkerCreated"|"s3:ObjectRestore:*"|"s3:ObjectRestore:Post"|"s3:ObjectRestore:Completed"|"s3:Replication:*"|"s3:Replication:OperationFailedReplication"|"s3:Replication:OperationNotTracked"|"s3:Replication:OperationMissedThreshold"|"s3:Replication:OperationReplicatedAfterThreshold"|"s3:ObjectRestore:Delete"|"s3:LifecycleTransition"|"s3:IntelligentTiering"|"s3:ObjectAcl:Put"|"s3:LifecycleExpiration:*"|"s3:LifecycleExpiration:Delete"|"s3:LifecycleExpiration:DeleteMarkerCreated"|"s3:ObjectTagging:*"|"s3:ObjectTagging:Put"|"s3:ObjectTagging:Delete", ...],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "prefix"|"suffix",
              "Value": "string"
            }
            ...
          ]
        }
      }
    }
    ...
  ],
  "LambdaFunctionConfigurations": [
    {
      "Id": "string",
      "LambdaFunctionArn": "string",
      "Events": ["s3:ReducedRedundancyLostObject"|"s3:ObjectCreated:*"|"s3:ObjectCreated:Put"|"s3:ObjectCreated:Post"|"s3:ObjectCreated:Copy"|"s3:ObjectCreated:CompleteMultipartUpload"|"s3:ObjectRemoved:*"|"s3:ObjectRemoved:Delete"|"s3:ObjectRemoved:DeleteMarkerCreated"|"s3:ObjectRestore:*"|"s3:ObjectRestore:Post"|"s3:ObjectRestore:Completed"|"s3:Replication:*"|"s3:Replication:OperationFailedReplication"|"s3:Replication:OperationNotTracked"|"s3:Replication:OperationMissedThreshold"|"s3:Replication:OperationReplicatedAfterThreshold"|"s3:ObjectRestore:Delete"|"s3:LifecycleTransition"|"s3:IntelligentTiering"|"s3:ObjectAcl:Put"|"s3:LifecycleExpiration:*"|"s3:LifecycleExpiration:Delete"|"s3:LifecycleExpiration:DeleteMarkerCreated"|"s3:ObjectTagging:*"|"s3:ObjectTagging:Put"|"s3:ObjectTagging:Delete", ...],
      "Filter": {
        "Key": {
          "FilterRules": [
            {
              "Name": "prefix"|"suffix",
              "Value": "string"
            }
            ...
          ]
        }
      }
    }
    ...
  ],
  "EventBridgeConfiguration": {

  }
}
```

`--expected-bucket-owner` (string)

The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).

`--skip-destination-validation` | `--no-skip-destination-validation` (boolean)

Skips validation of Amazon SQS, Amazon SNS, and Lambda destinations. True or false value.

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

**To enable the specified notifications to a bucket**

The following `put-bucket-notification-configuration` example applies a notification configuration to a bucket named `amzn-s3-demo-bucket`. The file `notification.json` is a JSON document in the current folder that specifies an SNS topic and an event type to monitor.

```
aws s3api put-bucket-notification-configuration \
    --bucket amzn-s3-demo-bucket \
    --notification-configuration file://notification.json
```

Contents of `notification.json`:

```
{
    "TopicConfigurations": [
        {
            "TopicArn": "arn:aws:sns:us-west-2:123456789012:s3-notification-topic",
            "Events": [
                "s3:ObjectCreated:*"
            ]
        }
    ]
}
```

The SNS topic must have an IAM policy attached to it that allows Amazon S3 to publish to it.

```
{
    "Version": "2008-10-17",
    "Id": "example-ID",
    "Statement": [
        {
            "Sid": "example-statement-ID",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": [
                "SNS:Publish"
            ],
            "Resource": "arn:aws:sns:us-west-2:123456789012::s3-notification-topic",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:*:*:amzn-s3-demo-bucket"
                }
            }
        }
    ]
}
```

## Output

None