# put-lifecycle-hookÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/index.html#cli-aws-autoscaling) ]

# put-lifecycle-hook

## Description

Creates or updates a lifecycle hook for the specified Auto Scaling group.

Lifecycle hooks let you create solutions that are aware of events in the Auto Scaling instance lifecycle, and then perform a custom action on instances when the corresponding lifecycle event occurs.

This step is a part of the procedure for adding a lifecycle hook to an Auto Scaling group:

- (Optional) Create a launch template or launch configuration with a user data script that runs while an instance is in a wait state due to a lifecycle hook.
- (Optional) Create a Lambda function and a rule that allows Amazon EventBridge to invoke your Lambda function when an instance is put into a wait state due to a lifecycle hook.
- (Optional) Create a notification target and an IAM role. The target can be either an Amazon SQS queue or an Amazon SNS topic. The role allows Amazon EC2 Auto Scaling to publish lifecycle notifications to the target.
- **Create the lifecycle hook. Specify whether the hook is used when the instances launch or terminate.**
- If you need more time, record the lifecycle action heartbeat to keep the instance in a wait state using the [RecordLifecycleActionHeartbeat](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RecordLifecycleActionHeartbeat.html) API call.
- If you finish before the timeout period ends, send a callback by using the [CompleteLifecycleAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CompleteLifecycleAction.html) API call.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide* .

If you exceed your maximum limit of lifecycle hooks, which by default is 50 per Auto Scaling group, the call fails.

You can view the lifecycle hooks for an Auto Scaling group using the [DescribeLifecycleHooks](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeLifecycleHooks.html) API call. If you are no longer using a lifecycle hook, you can delete it by calling the [DeleteLifecycleHook](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteLifecycleHook.html) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/PutLifecycleHook)

## Synopsis

```
put-lifecycle-hook
--lifecycle-hook-name <value>
--auto-scaling-group-name <value>
[--lifecycle-transition <value>]
[--role-arn <value>]
[--notification-target-arn <value>]
[--notification-metadata <value>]
[--heartbeat-timeout <value>]
[--default-result <value>]
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

`--lifecycle-hook-name` (string)

The name of the lifecycle hook.

`--auto-scaling-group-name` (string)

The name of the Auto Scaling group.

`--lifecycle-transition` (string)

The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.

- To create a lifecycle hook for scale-out events, specify `autoscaling:EC2_INSTANCE_LAUNCHING` .
- To create a lifecycle hook for scale-in events, specify `autoscaling:EC2_INSTANCE_TERMINATING` .

Required for new lifecycle hooks, but optional when updating existing hooks.

`--role-arn` (string)

The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.

Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue. Required for new lifecycle hooks, but optional when updating existing hooks.

`--notification-target-arn` (string)

The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling uses to notify you when an instance is in a wait state for the lifecycle hook. You can specify either an Amazon SNS topic or an Amazon SQS queue.

If you specify an empty string, this overrides the current ARN.

This operation uses the JSON format when sending notifications to an Amazon SQS queue, and an email key-value pair format when sending notifications to an Amazon SNS topic.

When you specify a notification target, Amazon EC2 Auto Scaling sends it a test message. Test messages contain the following additional key-value pair: `"Event": "autoscaling:TEST_NOTIFICATION"` .

`--notification-metadata` (string)

Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.

`--heartbeat-timeout` (integer)

The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from `30` to `7200` seconds. The default value is `3600` seconds (1 hour).

`--default-result` (string)

The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is `ABANDON` .

Valid values: `CONTINUE` | `ABANDON`

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

**Example 1: To create a lifecycle hook**

This example creates a lifecycle hook that will invoke on any newly launched instances, with a timeout of 4800 seconds. This is useful for keeping the instances in a wait state until the user data scripts have finished, or for invoking an AWS Lambda function using EventBridge.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name my-asg \
    --lifecycle-hook-name my-launch-hook \
    --lifecycle-transition autoscaling:EC2_INSTANCE_LAUNCHING \
    --heartbeat-timeout 4800
```

This command produces no output.  If a lifecycle hook with the same name already exists, it will be overwritten by the new lifecycle hook.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 2: To send an Amazon SNS email message to notify you of instance state transitions**

This example creates a lifecycle hook with the Amazon SNS topic and IAM role to use to receive notification at instance launch.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name my-asg \
    --lifecycle-hook-name my-launch-hook \
    --lifecycle-transition autoscaling:EC2_INSTANCE_LAUNCHING \
    --notification-target-arn arn:aws:sns:us-west-2:123456789012:my-sns-topic \
    --role-arn arn:aws:iam::123456789012:role/my-auto-scaling-role
```

This command produces no output.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

**Example 3: To publish a message to an Amazon SQS queue**

This example creates a lifecycle hook that publishes a message with metadata to the specified Amazon SQS queue.

```
aws autoscaling put-lifecycle-hook \
    --auto-scaling-group-name my-asg \
    --lifecycle-hook-name my-launch-hook \
    --lifecycle-transition autoscaling:EC2_INSTANCE_LAUNCHING \
    --notification-target-arn arn:aws:sqs:us-west-2:123456789012:my-sqs-queue \
    --role-arn arn:aws:iam::123456789012:role/my-notification-role \
    --notification-metadata "SQS message metadata"
```

This command produces no output.

For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Output

None