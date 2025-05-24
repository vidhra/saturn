# update-table-replica-auto-scalingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table-replica-auto-scaling.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table-replica-auto-scaling.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dynamodb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html#cli-aws-dynamodb) ]

# update-table-replica-auto-scaling

## Description

Updates auto scaling settings on your global tables at once.

### Warning

For global tables, this operation only applies to global tables using Version 2019.11.21 (Current version).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dynamodb-2012-08-10/UpdateTableReplicaAutoScaling)

## Synopsis

```
update-table-replica-auto-scaling
[--global-secondary-index-updates <value>]
--table-name <value>
[--provisioned-write-capacity-auto-scaling-update <value>]
[--replica-updates <value>]
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

`--global-secondary-index-updates` (list)

Represents the auto scaling settings of the global secondary indexes of the replica to be updated.

(structure)

Represents the auto scaling settings of a global secondary index for a global table that will be modified.

IndexName -> (string)

The name of the global secondary index.

ProvisionedWriteCapacityAutoScalingUpdate -> (structure)

Represents the auto scaling settings to be modified for a global table or global secondary index.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring auto scaling policy.

ScalingPolicyUpdate -> (structure)

The scaling policy to apply for scaling target global table or global secondary index capacity units.

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

JSON Syntax:

```
[
  {
    "IndexName": "string",
    "ProvisionedWriteCapacityAutoScalingUpdate": {
      "MinimumUnits": long,
      "MaximumUnits": long,
      "AutoScalingDisabled": true|false,
      "AutoScalingRoleArn": "string",
      "ScalingPolicyUpdate": {
        "PolicyName": "string",
        "TargetTrackingScalingPolicyConfiguration": {
          "DisableScaleIn": true|false,
          "ScaleInCooldown": integer,
          "ScaleOutCooldown": integer,
          "TargetValue": double
        }
      }
    }
  }
  ...
]
```

`--table-name` (string)

The name of the global table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.

`--provisioned-write-capacity-auto-scaling-update` (structure)

Represents the auto scaling settings to be modified for a global table or global secondary index.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring auto scaling policy.

ScalingPolicyUpdate -> (structure)

The scaling policy to apply for scaling target global table or global secondary index capacity units.

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

Shorthand Syntax:

```
MinimumUnits=long,MaximumUnits=long,AutoScalingDisabled=boolean,AutoScalingRoleArn=string,ScalingPolicyUpdate={PolicyName=string,TargetTrackingScalingPolicyConfiguration={DisableScaleIn=boolean,ScaleInCooldown=integer,ScaleOutCooldown=integer,TargetValue=double}}
```

JSON Syntax:

```
{
  "MinimumUnits": long,
  "MaximumUnits": long,
  "AutoScalingDisabled": true|false,
  "AutoScalingRoleArn": "string",
  "ScalingPolicyUpdate": {
    "PolicyName": "string",
    "TargetTrackingScalingPolicyConfiguration": {
      "DisableScaleIn": true|false,
      "ScaleInCooldown": integer,
      "ScaleOutCooldown": integer,
      "TargetValue": double
    }
  }
}
```

`--replica-updates` (list)

Represents the auto scaling settings of replicas of the table that will be modified.

(structure)

Represents the auto scaling settings of a replica that will be modified.

RegionName -> (string)

The Region where the replica exists.

ReplicaGlobalSecondaryIndexUpdates -> (list)

Represents the auto scaling settings of global secondary indexes that will be modified.

(structure)

Represents the auto scaling settings of a global secondary index for a replica that will be modified.

IndexName -> (string)

The name of the global secondary index.

ProvisionedReadCapacityAutoScalingUpdate -> (structure)

Represents the auto scaling settings to be modified for a global table or global secondary index.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring auto scaling policy.

ScalingPolicyUpdate -> (structure)

The scaling policy to apply for scaling target global table or global secondary index capacity units.

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

ReplicaProvisionedReadCapacityAutoScalingUpdate -> (structure)

Represents the auto scaling settings to be modified for a global table or global secondary index.

MinimumUnits -> (long)

The minimum capacity units that a global table or global secondary index should be scaled down to.

MaximumUnits -> (long)

The maximum capacity units that a global table or global secondary index should be scaled up to.

AutoScalingDisabled -> (boolean)

Disabled auto scaling for this global table or global secondary index.

AutoScalingRoleArn -> (string)

Role ARN used for configuring auto scaling policy.

ScalingPolicyUpdate -> (structure)

The scaling policy to apply for scaling target global table or global secondary index capacity units.

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

JSON Syntax:

```
[
  {
    "RegionName": "string",
    "ReplicaGlobalSecondaryIndexUpdates": [
      {
        "IndexName": "string",
        "ProvisionedReadCapacityAutoScalingUpdate": {
          "MinimumUnits": long,
          "MaximumUnits": long,
          "AutoScalingDisabled": true|false,
          "AutoScalingRoleArn": "string",
          "ScalingPolicyUpdate": {
            "PolicyName": "string",
            "TargetTrackingScalingPolicyConfiguration": {
              "DisableScaleIn": true|false,
              "ScaleInCooldown": integer,
              "ScaleOutCooldown": integer,
              "TargetValue": double
            }
          }
        }
      }
      ...
    ],
    "ReplicaProvisionedReadCapacityAutoScalingUpdate": {
      "MinimumUnits": long,
      "MaximumUnits": long,
      "AutoScalingDisabled": true|false,
      "AutoScalingRoleArn": "string",
      "ScalingPolicyUpdate": {
        "PolicyName": "string",
        "TargetTrackingScalingPolicyConfiguration": {
          "DisableScaleIn": true|false,
          "ScaleInCooldown": integer,
          "ScaleOutCooldown": integer,
          "TargetValue": double
        }
      }
    }
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

**To update auto scaling settings across replicas of a global table**

The following `update-table-replica-auto-scaling` example updates write capacity auto scaling settings across replicas of the specified global table.

```
aws dynamodb update-table-replica-auto-scaling \
    --table-name MusicCollection \
    --provisioned-write-capacity-auto-scaling-update file://auto-scaling-policy.json
```

Contents of `auto-scaling-policy.json`:

```
{
    "MinimumUnits": 10,
    "MaximumUnits": 100,
    "AutoScalingDisabled": false,
    "ScalingPolicyUpdate": {
        "PolicyName": "DynamoDBWriteCapacityUtilization:table/MusicCollection",
        "TargetTrackingScalingPolicyConfiguration": {
            "TargetValue": 80
        }
    }
}
```

Output:

```
{
    "TableAutoScalingDescription": {
        "TableName": "MusicCollection",
        "TableStatus": "ACTIVE",
        "Replicas": [
            {
                "RegionName": "eu-central-1",
                "GlobalSecondaryIndexes": [],
                "ReplicaProvisionedReadCapacityAutoScalingSettings": {
                    "MinimumUnits": 5,
                    "MaximumUnits": 40000,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBReadCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 70.0
                            }
                        }
                    ]
                },
                "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
                    "MinimumUnits": 10,
                    "MaximumUnits": 100,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBWriteCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 80.0
                            }
                        }
                    ]
                },
                "ReplicaStatus": "ACTIVE"
            },
            {
                "RegionName": "us-east-1",
                "GlobalSecondaryIndexes": [],
                "ReplicaProvisionedReadCapacityAutoScalingSettings": {
                    "MinimumUnits": 5,
                    "MaximumUnits": 40000,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBReadCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 70.0
                            }
                        }
                    ]
                },
                "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
                    "MinimumUnits": 10,
                    "MaximumUnits": 100,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBWriteCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 80.0
                            }
                        }
                    ]
                },
                "ReplicaStatus": "ACTIVE"
            },
            {
                "RegionName": "us-east-2",
                "GlobalSecondaryIndexes": [],
                "ReplicaProvisionedReadCapacityAutoScalingSettings": {
                    "MinimumUnits": 5,
                    "MaximumUnits": 40000,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBReadCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 70.0
                            }
                        }
                    ]
                },
                "ReplicaProvisionedWriteCapacityAutoScalingSettings": {
                    "MinimumUnits": 10,
                    "MaximumUnits": 100,
                    "AutoScalingRoleArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable",
                    "ScalingPolicies": [
                        {
                            "PolicyName": "DynamoDBWriteCapacityUtilization:table/MusicCollection",
                            "TargetTrackingScalingPolicyConfiguration": {
                                "TargetValue": 80.0
                            }
                        }
                    ]
                },
                "ReplicaStatus": "ACTIVE"
            }
        ]
    }
}
```

For more information, see [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) in the *Amazon DynamoDB Developer Guide*.

## Output

TableAutoScalingDescription -> (structure)

Returns information about the auto scaling settings of a table with replicas.

TableName -> (string)

The name of the table.

TableStatus -> (string)

The current state of the table:

- `CREATING` - The table is being created.
- `UPDATING` - The table is being updated.
- `DELETING` - The table is being deleted.
- `ACTIVE` - The table is ready for use.

Replicas -> (list)

Represents replicas of the global table.

(structure)

Represents the auto scaling settings of the replica.

RegionName -> (string)

The Region where the replica exists.

GlobalSecondaryIndexes -> (list)

Replica-specific global secondary index auto scaling settings.

(structure)

Represents the auto scaling configuration for a replica global secondary index.

IndexName -> (string)

The name of the global secondary index.

IndexStatus -> (string)

The current state of the replica global secondary index:

- `CREATING` - The index is being created.
- `UPDATING` - The table/index configuration is being updated. The table/index remains available for data operations when `UPDATING`
- `DELETING` - The index is being deleted.
- `ACTIVE` - The index is ready for use.

ProvisionedReadCapacityAutoScalingSettings -> (structure)

Represents the auto scaling settings for a global table or global secondary index.

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

ProvisionedWriteCapacityAutoScalingSettings -> (structure)

Represents the auto scaling settings for a global table or global secondary index.

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

ReplicaProvisionedReadCapacityAutoScalingSettings -> (structure)

Represents the auto scaling settings for a global table or global secondary index.

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

ReplicaProvisionedWriteCapacityAutoScalingSettings -> (structure)

Represents the auto scaling settings for a global table or global secondary index.

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

ReplicaStatus -> (string)

The current state of the replica:

- `CREATING` - The replica is being created.
- `UPDATING` - The replica is being updated.
- `DELETING` - The replica is being deleted.
- `ACTIVE` - The replica is ready for use.