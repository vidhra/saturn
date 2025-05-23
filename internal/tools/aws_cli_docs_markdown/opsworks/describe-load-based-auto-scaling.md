# describe-load-based-auto-scalingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-load-based-auto-scaling.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-load-based-auto-scaling.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# describe-load-based-auto-scaling

## Description

Describes load-based auto scaling configurations for specified layers.

### Note

You must specify at least one of the parameters.

**Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information about user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLoadBasedAutoScaling)

## Synopsis

```
describe-load-based-auto-scaling
--layer-ids <value>
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

`--layer-ids` (list)

An array of layer IDs.

(string)

Syntax:

```
"string" "string" ...
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

**To describe a layerâs load-based scaling configuration**

The following example describes a specified layerâs load-based scaling configuration.
The layer is identified by its layer ID, which you can find on the layerâs
details page or by running `describe-layers`.

```
aws opsworks describe-load-based-auto-scaling --region us-east-1 --layer-ids 6bec29c9-c866-41a0-aba5-fa3e374ce2a1
```

*Output*: The example layer has a single load-based instance.

```
{
  "LoadBasedAutoScalingConfigurations": [
    {
      "DownScaling": {
        "IgnoreMetricsTime": 10,
        "ThresholdsWaitTime": 10,
        "InstanceCount": 1,
        "CpuThreshold": 30.0
      },
      "Enable": true,
      "UpScaling": {
        "IgnoreMetricsTime": 5,
        "ThresholdsWaitTime": 5,
        "InstanceCount": 1,
        "CpuThreshold": 80.0
      },
      "LayerId": "6bec29c9-c866-41a0-aba5-fa3e374ce2a1"
    }
  ]
}
```

**More Information**

For more information, see [How Automatic Load-based Scaling Works](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autoscaling.html#workinginstances-autoscaling-loadbased) in the *AWS OpsWorks User Guide*.

## Output

LoadBasedAutoScalingConfigurations -> (list)

An array of `LoadBasedAutoScalingConfiguration` objects that describe each layerâs configuration.

(structure)

Describes a layerâs load-based auto scaling configuration.

LayerId -> (string)

The layer ID.

Enable -> (boolean)

Whether load-based auto scaling is enabled for the layer.

UpScaling -> (structure)

An `AutoScalingThresholds` object that describes the upscaling configuration, which defines how and when OpsWorks Stacks increases the number of instances.

InstanceCount -> (integer)

The number of instances to add or remove when the load exceeds a threshold.

ThresholdsWaitTime -> (integer)

The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

IgnoreMetricsTime -> (integer)

The amount of time (in minutes) after a scaling event occurs that OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, OpsWorks Stacks adds new instances following an upscaling event but the instances wonât start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. `IgnoreMetricsTime` allows you to direct OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

CpuThreshold -> (double)

The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

MemoryThreshold -> (double)

The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

LoadThreshold -> (double)

The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see [Load (computing)](http://en.wikipedia.org/wiki/Load_%28computing%29) .

Alarms -> (list)

Custom CloudWatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

### Note

To use custom alarms, you must update your service role to allow `cloudwatch:DescribeAlarms` . You can either have OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see [Allowing OpsWorks Stacks to Act on Your Behalf](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html) .

(string)

DownScaling -> (structure)

An `AutoScalingThresholds` object that describes the downscaling configuration, which defines how and when OpsWorks Stacks reduces the number of instances.

InstanceCount -> (integer)

The number of instances to add or remove when the load exceeds a threshold.

ThresholdsWaitTime -> (integer)

The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

IgnoreMetricsTime -> (integer)

The amount of time (in minutes) after a scaling event occurs that OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, OpsWorks Stacks adds new instances following an upscaling event but the instances wonât start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. `IgnoreMetricsTime` allows you to direct OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

CpuThreshold -> (double)

The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

MemoryThreshold -> (double)

The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

LoadThreshold -> (double)

The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see [Load (computing)](http://en.wikipedia.org/wiki/Load_%28computing%29) .

Alarms -> (list)

Custom CloudWatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

### Note

To use custom alarms, you must update your service role to allow `cloudwatch:DescribeAlarms` . You can either have OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see [Allowing OpsWorks Stacks to Act on Your Behalf](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html) .

(string)