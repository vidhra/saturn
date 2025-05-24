# set-load-based-auto-scalingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-load-based-auto-scaling.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/set-load-based-auto-scaling.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opsworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/index.html#cli-aws-opsworks) ]

# set-load-based-auto-scaling

## Description

Specify the load-based auto scaling configuration for a specified layer. For more information, see [Managing Load with Time-based and Load-based Instances](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autoscaling.html) .

### Note

To use load-based auto scaling, you must create a set of load-based auto scaling instances. Load-based auto scaling operates only on the instances from that set, so you must ensure that you have created enough instances to handle the maximum anticipated load.

**Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see [Managing User Permissions](https://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/SetLoadBasedAutoScaling)

## Synopsis

```
set-load-based-auto-scaling
--layer-id <value>
[--enable | --no-enable]
[--up-scaling <value>]
[--down-scaling <value>]
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

`--layer-id` (string)

The layer ID.

`--enable` | `--no-enable` (boolean)

Enables load-based auto scaling for the layer.

`--up-scaling` (structure)

An `AutoScalingThresholds` object with the upscaling threshold configuration. If the load exceeds these thresholds for a specified amount of time, OpsWorks Stacks starts a specified number of instances.

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

Shorthand Syntax:

```
InstanceCount=integer,ThresholdsWaitTime=integer,IgnoreMetricsTime=integer,CpuThreshold=double,MemoryThreshold=double,LoadThreshold=double,Alarms=string,string
```

JSON Syntax:

```
{
  "InstanceCount": integer,
  "ThresholdsWaitTime": integer,
  "IgnoreMetricsTime": integer,
  "CpuThreshold": double,
  "MemoryThreshold": double,
  "LoadThreshold": double,
  "Alarms": ["string", ...]
}
```

`--down-scaling` (structure)

An `AutoScalingThresholds` object with the downscaling threshold configuration. If the load falls below these thresholds for a specified amount of time, OpsWorks Stacks stops a specified number of instances.

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

Shorthand Syntax:

```
InstanceCount=integer,ThresholdsWaitTime=integer,IgnoreMetricsTime=integer,CpuThreshold=double,MemoryThreshold=double,LoadThreshold=double,Alarms=string,string
```

JSON Syntax:

```
{
  "InstanceCount": integer,
  "ThresholdsWaitTime": integer,
  "IgnoreMetricsTime": integer,
  "CpuThreshold": double,
  "MemoryThreshold": double,
  "LoadThreshold": double,
  "Alarms": ["string", ...]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To set the load-based scaling configuration for a layer**

The following example enables load-based scaling for a specified layer and sets the configuration
for that layer.
You must use `create-instance` to add load-based instances to the layer.

```
aws opsworks --region us-east-1 set-load-based-auto-scaling --layer-id 523569ae-2faf-47ac-b39e-f4c4b381f36d --enable --up-scaling file://upscale.json --down-scaling file://downscale.json
```

The example puts the upscaling threshold settings in a separate file in the working directory named `upscale.json`, which contains the following.

```
{
  "InstanceCount": 2,
  "ThresholdsWaitTime": 3,
  "IgnoreMetricsTime": 3,
  "CpuThreshold": 85,
  "MemoryThreshold": 85,
  "LoadThreshold": 85
}
```

The example puts the downscaling threshold settings in a separate file in the working directory named `downscale.json`, which contains the following.

```
{
"InstanceCount": 2,
"ThresholdsWaitTime": 3,
"IgnoreMetricsTime": 3,
"CpuThreshold": 35,
"MemoryThreshold": 30,
"LoadThreshold": 30
}
```

*Output*: None.

**More Information**

For more information, see [Using Automatic Load-based Scaling](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autoscaling-loadbased.html) in the *AWS OpsWorks User Guide*.

## Output

None