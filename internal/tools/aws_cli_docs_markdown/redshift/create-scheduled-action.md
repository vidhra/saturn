# create-scheduled-actionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# create-scheduled-action

## Description

Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the `ResizeCluster` API operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateScheduledAction)

## Synopsis

```
create-scheduled-action
--scheduled-action-name <value>
--target-action <value>
--schedule <value>
--iam-role <value>
[--scheduled-action-description <value>]
[--start-time <value>]
[--end-time <value>]
[--enable | --no-enable]
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

`--scheduled-action-name` (string)

The name of the scheduled action. The name must be unique within an account. For more information about this parameter, see  ScheduledAction .

`--target-action` (structure)

A JSON format string of the Amazon Redshift API operation with input parameters. For more information about this parameter, see  ScheduledAction .

ResizeCluster -> (structure)

An action that runs a `ResizeCluster` API operation.

ClusterIdentifier -> (string)

The unique identifier for the cluster to resize.

ClusterType -> (string)

The new cluster type for the specified cluster.

NodeType -> (string)

The new node type for the nodes you are adding. If not specified, the clusterâs current node type is used.

NumberOfNodes -> (integer)

The new number of nodes for the cluster. If not specified, the clusterâs current number of nodes is used.

Classic -> (boolean)

A boolean value indicating whether the resize operation is using the classic resize process. If you donât provide this parameter or set the value to `false` , the resize type is elastic.

ReservedNodeId -> (string)

The identifier of the reserved node.

TargetReservedNodeOfferingId -> (string)

The identifier of the target reserved node offering.

PauseCluster -> (structure)

An action that runs a `PauseCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be paused.

ResumeCluster -> (structure)

An action that runs a `ResumeCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be resumed.

Shorthand Syntax:

```
ResizeCluster={ClusterIdentifier=string,ClusterType=string,NodeType=string,NumberOfNodes=integer,Classic=boolean,ReservedNodeId=string,TargetReservedNodeOfferingId=string},PauseCluster={ClusterIdentifier=string},ResumeCluster={ClusterIdentifier=string}
```

JSON Syntax:

```
{
  "ResizeCluster": {
    "ClusterIdentifier": "string",
    "ClusterType": "string",
    "NodeType": "string",
    "NumberOfNodes": integer,
    "Classic": true|false,
    "ReservedNodeId": "string",
    "TargetReservedNodeOfferingId": "string"
  },
  "PauseCluster": {
    "ClusterIdentifier": "string"
  },
  "ResumeCluster": {
    "ClusterIdentifier": "string"
  }
}
```

`--schedule` (string)

The schedule in `at( )` or `cron( )` format. For more information about this parameter, see  ScheduledAction .

`--iam-role` (string)

The IAM role to assume to run the target action. For more information about this parameter, see  ScheduledAction .

`--scheduled-action-description` (string)

The description of the scheduled action.

`--start-time` (timestamp)

The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger. For more information about this parameter, see  ScheduledAction .

`--end-time` (timestamp)

The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger. For more information about this parameter, see  ScheduledAction .

`--enable` | `--no-enable` (boolean)

If true, the schedule is enabled. If false, the scheduled action does not trigger. For more information about `state` of the scheduled action, see  ScheduledAction .

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

ScheduledActionName -> (string)

The name of the scheduled action.

TargetAction -> (structure)

A JSON format string of the Amazon Redshift API operation with input parameters.

â`{\"ResizeCluster\":{\"NodeType\":\"ra3.4xlarge\",\"ClusterIdentifier\":\"my-test-cluster\",\"NumberOfNodes\":3}}` â.

ResizeCluster -> (structure)

An action that runs a `ResizeCluster` API operation.

ClusterIdentifier -> (string)

The unique identifier for the cluster to resize.

ClusterType -> (string)

The new cluster type for the specified cluster.

NodeType -> (string)

The new node type for the nodes you are adding. If not specified, the clusterâs current node type is used.

NumberOfNodes -> (integer)

The new number of nodes for the cluster. If not specified, the clusterâs current number of nodes is used.

Classic -> (boolean)

A boolean value indicating whether the resize operation is using the classic resize process. If you donât provide this parameter or set the value to `false` , the resize type is elastic.

ReservedNodeId -> (string)

The identifier of the reserved node.

TargetReservedNodeOfferingId -> (string)

The identifier of the target reserved node offering.

PauseCluster -> (structure)

An action that runs a `PauseCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be paused.

ResumeCluster -> (structure)

An action that runs a `ResumeCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be resumed.

Schedule -> (string)

The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.

Format of at expressions is â`at(yyyy-mm-ddThh:mm:ss)` â. For example, â`at(2016-03-04T17:27:00)` â.

Format of cron expressions is â`cron(Minutes Hours Day-of-month Month Day-of-week Year)` â. For example, â`cron(0 10 ? * MON *)` â. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

IamRole -> (string)

The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the *Amazon Redshift Cluster Management Guide* .

ScheduledActionDescription -> (string)

The description of the scheduled action.

State -> (string)

The state of the scheduled action. For example, `DISABLED` .

NextInvocations -> (list)

List of times when the scheduled action will run.

(timestamp)

StartTime -> (timestamp)

The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

EndTime -> (timestamp)

The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.