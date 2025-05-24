# get-table-auto-scaling-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/get-table-auto-scaling-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/get-table-auto-scaling-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [keyspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html#cli-aws-keyspaces) ]

# get-table-auto-scaling-settings

## Description

Returns auto scaling related settings of the specified table in JSON format. If the table is a multi-Region table, the Amazon Web Services Region specific auto scaling settings of the table are included.

Amazon Keyspaces auto scaling helps you provision throughput capacity for variable workloads efficiently by increasing and decreasing your tableâs read and write capacity automatically in response to application traffic. For more information, see [Managing throughput capacity automatically with Amazon Keyspaces auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html) in the *Amazon Keyspaces Developer Guide* .

### Warning

`GetTableAutoScalingSettings` canât be used as an action in an IAM policy.

To define permissions for `GetTableAutoScalingSettings` , you must allow the following two actions in the IAM policy statementâs `Action` element:

- `application-autoscaling:DescribeScalableTargets`
- `application-autoscaling:DescribeScalingPolicies`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/keyspaces-2022-02-10/GetTableAutoScalingSettings)

## Synopsis

```
get-table-auto-scaling-settings
--keyspace-name <value>
--table-name <value>
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

`--keyspace-name` (string)

The name of the keyspace.

`--table-name` (string)

The name of the table.

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

keyspaceName -> (string)

The name of the keyspace.

tableName -> (string)

The name of the table.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the table.

autoScalingSpecification -> (structure)

The auto scaling settings of the table.

writeCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs write capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

readCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs read capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

replicaSpecifications -> (list)

The Amazon Web Services Region specific settings of a multi-Region table. Returns the settings for all Regions the table is replicated in.

(structure)

The auto scaling settings of a multi-Region table in the specified Amazon Web Services Region.

region -> (string)

The Amazon Web Services Region.

autoScalingSpecification -> (structure)

The auto scaling settings for a multi-Region table in the specified Amazon Web Services Region.

writeCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs write capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.

readCapacityAutoScaling -> (structure)

The auto scaling settings for the tableâs read capacity.

autoScalingDisabled -> (boolean)

This optional parameter enables auto scaling for the table if set to `false` .

minimumUnits -> (long)

The minimum level of throughput the table should always be ready to support. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

maximumUnits -> (long)

Manage costs by specifying the maximum amount of throughput to provision. The value must be between 1 and the max throughput per second quota for your account (40,000 by default).

scalingPolicy -> (structure)

Amazon Keyspaces supports the `target tracking` auto scaling policy. With this policy, Amazon Keyspaces auto scaling ensures that the tableâs ratio of consumed to provisioned capacity stays at or near the target value that you specify. You define the target value as a percentage between 20 and 90.

targetTrackingScalingPolicyConfiguration -> (structure)

Auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. A `double` between 20 and 90.

disableScaleIn -> (boolean)

Specifies if `scale-in` is enabled.

When auto scaling automatically decreases capacity for a table, the table *scales in* . When scaling policies are set, they canât scale in the table lower than its minimum capacity.

scaleInCooldown -> (integer)

Specifies a `scale-in` cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

scaleOutCooldown -> (integer)

Specifies a scale out cool down period.

A cooldown period in seconds between scaling activities that lets the table stabilize before another scaling activity starts.

targetValue -> (double)

Specifies the target value for the target tracking auto scaling policy.

Amazon Keyspaces auto scaling scales up capacity automatically when traffic exceeds this target utilization rate, and then back down when it falls below the target. This ensures that the ratio of consumed capacity to provisioned capacity stays at or near this value. You define `targetValue` as a percentage. A `double` between 20 and 90.