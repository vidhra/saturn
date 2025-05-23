# describe-global-table-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# describe-global-table-settings

## Description

Describes Region-specific settings for a global table.

### Warning

This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).

To determine which version youâre using, see [Determining the global table version you are using](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html) . To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see [Upgrading global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/DescribeGlobalTableSettings)

## Synopsis

```
describe-global-table-settings
--global-table-name <value>
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

`--global-table-name` (string)

The name of the global table to describe.

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

**To get information about a DynamoDB global tableâs settings**

The following `describe-global-table-settings` example displays the settings for the `MusicCollection` global table.

```
aws dynamodb describe-global-table-settings \
    --global-table-name MusicCollection
```

Output:

```
{
    "GlobalTableName": "MusicCollection",
    "ReplicaSettings": [
        {
            "RegionName": "us-east-1",
            "ReplicaStatus": "ACTIVE",
            "ReplicaProvisionedReadCapacityUnits": 10,
            "ReplicaProvisionedReadCapacityAutoScalingSettings": {
                "AutoScalingDisabled": true
            },
            "ReplicaProvisionedWriteCapacityUnits": 5,
            "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
                "AutoScalingDisabled": true
            }
        },
        {
            "RegionName": "us-east-2",
            "ReplicaStatus": "ACTIVE",
            "ReplicaProvisionedReadCapacityUnits": 10,
            "ReplicaProvisionedReadCapacityAutoScalingSettings": {
                "AutoScalingDisabled": true
            },
            "ReplicaProvisionedWriteCapacityUnits": 5,
            "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
                "AutoScalingDisabled": true
            }
        }
    ]
}
```

For more information, see [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) in the *Amazon DynamoDB Developer Guide*.

## Output

GlobalTableName -> (string)

The name of the global table.

ReplicaSettings -> (list)

The Region-specific settings for the global table.

(structure)

Represents the properties of a replica.

RegionName -> (string)

The Region name of the replica.

ReplicaStatus -> (string)

The current state of the Region:

- `CREATING` - The Region is being created.
- `UPDATING` - The Region is being updated.
- `DELETING` - The Region is being deleted.
- `ACTIVE` - The Region is ready for use.

ReplicaBillingModeSummary -> (structure)

The read/write capacity mode of the replica.

BillingMode -> (string)

Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.

- `PROVISIONED` - Sets the read/write capacity mode to `PROVISIONED` . We recommend using `PROVISIONED` for predictable workloads.
- `PAY_PER_REQUEST` - Sets the read/write capacity mode to `PAY_PER_REQUEST` . We recommend using `PAY_PER_REQUEST` for unpredictable workloads.

LastUpdateToPayPerRequestDateTime -> (timestamp)

Represents the time when `PAY_PER_REQUEST` was last set as the read/write capacity mode.

ReplicaProvisionedReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput) in the *Amazon DynamoDB Developer Guide* .

ReplicaProvisionedReadCapacityAutoScalingSettings -> (structure)

Auto scaling settings for a global table replicaâs read capacity units.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring the auto scaling policy.

ScalingPolicies -> (list)

Information about the scaling policies.

(structure)

Represents the properties of the scaling policy.

PolicyName -> (string)

The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration -> (structure)

Represents a target tracking scaling policy configuration.

DisableScaleIn -> (boolean)

Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy wonât remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown -> (integer)

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your applicationâs availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown -> (integer)

The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue -> (double)

The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

ReplicaProvisionedWriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` . For more information, see [Specifying Read and Write Requirements](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#ProvisionedThroughput) in the *Amazon DynamoDB Developer Guide* .

ReplicaProvisionedWriteCapacityAutoScalingSettings -> (structure)

Auto scaling settings for a global table replicaâs write capacity units.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring the auto scaling policy.

ScalingPolicies -> (list)

Information about the scaling policies.

(structure)

Represents the properties of the scaling policy.

PolicyName -> (string)

The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration -> (structure)

Represents a target tracking scaling policy configuration.

DisableScaleIn -> (boolean)

Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy wonât remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown -> (integer)

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your applicationâs availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown -> (integer)

The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue -> (double)

The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

ReplicaGlobalSecondaryIndexSettings -> (list)

Replica global secondary index settings for the global table.

(structure)

Represents the properties of a global secondary index.

IndexName -> (string)

The name of the global secondary index. The name must be unique among all other indexes on this table.

IndexStatus -> (string)

The current status of the global secondary index:

- `CREATING` - The global secondary index is being created.
- `UPDATING` - The global secondary index is being updated.
- `DELETING` - The global secondary index is being deleted.
- `ACTIVE` - The global secondary index is ready for use.

ProvisionedReadCapacityUnits -> (long)

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException` .

ProvisionedReadCapacityAutoScalingSettings -> (structure)

Auto scaling settings for a global secondary index replicaâs read capacity units.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring the auto scaling policy.

ScalingPolicies -> (list)

Information about the scaling policies.

(structure)

Represents the properties of the scaling policy.

PolicyName -> (string)

The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration -> (structure)

Represents a target tracking scaling policy configuration.

DisableScaleIn -> (boolean)

Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy wonât remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown -> (integer)

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your applicationâs availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown -> (integer)

The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue -> (double)

The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

ProvisionedWriteCapacityUnits -> (long)

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException` .

ProvisionedWriteCapacityAutoScalingSettings -> (structure)

Auto scaling settings for a global secondary index replicaâs write capacity units.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring the auto scaling policy.

ScalingPolicies -> (list)

Information about the scaling policies.

(structure)

Represents the properties of the scaling policy.

PolicyName -> (string)

The name of the scaling policy.

TargetTrackingScalingPolicyConfiguration -> (structure)

Represents a target tracking scaling policy configuration.

DisableScaleIn -> (boolean)

Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy wonât remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.

ScaleInCooldown -> (integer)

The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your applicationâs availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application auto scaling scales out your scalable target immediately.

ScaleOutCooldown -> (integer)

The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.

TargetValue -> (double)

The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).

ReplicaTableClassSummary -> (structure)

Contains details of the table class.

TableClass -> (string)

The table class of the specified table. Valid values are `STANDARD` and `STANDARD_INFREQUENT_ACCESS` .

LastUpdateDateTime -> (timestamp)

The date and time at which the table class was last updated.