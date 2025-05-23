# update-scheduled-actionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/update-scheduled-action.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/update-scheduled-action.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# update-scheduled-action

## Description

Updates a scheduled action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/UpdateScheduledAction)

## Synopsis

```
update-scheduled-action
[--enabled | --no-enabled]
[--end-time <value>]
[--role-arn <value>]
[--schedule <value>]
[--scheduled-action-description <value>]
--scheduled-action-name <value>
[--start-time <value>]
[--target-action <value>]
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

`--enabled` | `--no-enabled` (boolean)

Specifies whether to enable the scheduled action.

`--end-time` (timestamp)

The end time in UTC of the scheduled action to update.

`--role-arn` (string)

The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Management Guide

`--schedule` (tagged union structure)

The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.

- Format of at timestamp is `yyyy-mm-ddThh:mm:ss` . For example, `2016-03-04T17:27:00` .
- Format of cron expression is `(Minutes Hours Day-of-month Month Day-of-week Year)` . For example, `"(0 10 ? * MON *)"` . For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `at`, `cron`.

at -> (timestamp)

The timestamp of when Amazon Redshift Serverless should run the scheduled action. Timestamp is in UTC. Format of at expression is `yyyy-mm-ddThh:mm:ss` . For example, `2016-03-04T17:27:00` .

cron -> (string)

The cron expression to use to schedule a recurring scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.

Format of cron expressions is `(Minutes Hours Day-of-month Month Day-of-week Year)` . For example, `"(0 10 ? * MON *)"` . For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

Shorthand Syntax:

```
at=timestamp,cron=string
```

JSON Syntax:

```
{
  "at": timestamp,
  "cron": "string"
}
```

`--scheduled-action-description` (string)

The descripion of the scheduled action to update to.

`--scheduled-action-name` (string)

The name of the scheduled action to update to.

`--start-time` (timestamp)

The start time in UTC of the scheduled action to update to.

`--target-action` (tagged union structure)

A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.

`"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `createSnapshot`.

createSnapshot -> (structure)

The parameters that you can use to configure a [scheduled action](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) to create a snapshot. For more information about creating a scheduled action, see [CreateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) .

namespaceName -> (string)

The name of the namespace for which you want to configure a scheduled action to create a snapshot.

retentionPeriod -> (integer)

The retention period of the snapshot created by the scheduled action.

snapshotNamePrefix -> (string)

A string prefix that is attached to the name of the snapshot created by the scheduled action. The final name of the snapshot is the string prefix appended by the date and time of when the snapshot was created.

tags -> (list)

An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the snapshot.

(structure)

A map of key-value pairs.

key -> (string)

The key to use in the tag.

value -> (string)

The value of the tag.

JSON Syntax:

```
{
  "createSnapshot": {
    "namespaceName": "string",
    "retentionPeriod": integer,
    "snapshotNamePrefix": "string",
    "tags": [
      {
        "key": "string",
        "value": "string"
      }
      ...
    ]
  }
}
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

scheduledAction -> (structure)

The ScheduledAction object that was updated.

endTime -> (timestamp)

The end time of

namespaceName -> (string)

The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.

nextInvocations -> (list)

An array of timestamps of when the next scheduled actions will trigger.

(timestamp)

roleArn -> (string)

The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Management Guide

schedule -> (tagged union structure)

The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.

- Format of at timestamp is `yyyy-mm-ddThh:mm:ss` . For example, `2016-03-04T17:27:00` .
- Format of cron expression is `(Minutes Hours Day-of-month Month Day-of-week Year)` . For example, `"(0 10 ? * MON *)"` . For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `at`, `cron`.

at -> (timestamp)

The timestamp of when Amazon Redshift Serverless should run the scheduled action. Timestamp is in UTC. Format of at expression is `yyyy-mm-ddThh:mm:ss` . For example, `2016-03-04T17:27:00` .

cron -> (string)

The cron expression to use to schedule a recurring scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.

Format of cron expressions is `(Minutes Hours Day-of-month Month Day-of-week Year)` . For example, `"(0 10 ? * MON *)"` . For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

scheduledActionDescription -> (string)

The description of the scheduled action.

scheduledActionName -> (string)

The name of the scheduled action.

scheduledActionUuid -> (string)

The uuid of the scheduled action.

startTime -> (timestamp)

The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

state -> (string)

The state of the scheduled action.

targetAction -> (tagged union structure)

A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.

`"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `createSnapshot`.

createSnapshot -> (structure)

The parameters that you can use to configure a [scheduled action](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) to create a snapshot. For more information about creating a scheduled action, see [CreateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) .

namespaceName -> (string)

The name of the namespace for which you want to configure a scheduled action to create a snapshot.

retentionPeriod -> (integer)

The retention period of the snapshot created by the scheduled action.

snapshotNamePrefix -> (string)

A string prefix that is attached to the name of the snapshot created by the scheduled action. The final name of the snapshot is the string prefix appended by the date and time of when the snapshot was created.

tags -> (list)

An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the snapshot.

(structure)

A map of key-value pairs.

key -> (string)

The key to use in the tag.

value -> (string)

The value of the tag.