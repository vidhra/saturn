# start-launchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/start-launch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/start-launch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# start-launch

## Description

Starts an existing launch. To create a launch, use [CreateLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateLaunch.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/StartLaunch)

## Synopsis

```
start-launch
--launch <value>
--project <value>
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

`--launch` (string)

The name of the launch to start.

`--project` (string)

The name or ARN of the project that contains the launch to start.

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

launch -> (structure)

A structure that contains information about the launch that was started.

arn -> (string)

The ARN of the launch.

createdTime -> (timestamp)

The date and time that the launch is created.

description -> (string)

The description of the launch.

execution -> (structure)

A structure that contains information about the start and end times of the launch.

endedTime -> (timestamp)

The date and time that the launch ended.

startedTime -> (timestamp)

The date and time that the launch started.

groups -> (list)

An array of structures that define the feature variations that are being used in the launch.

(structure)

A structure that defines one launch group in a launch. A launch group is a variation of the feature that you are including in the launch.

description -> (string)

A description of the launch group.

featureVariations -> (map)

The feature variation for this launch group. This is a key-value pair.

key -> (string)

value -> (string)

name -> (string)

The name of the launch group.

lastUpdatedTime -> (timestamp)

The date and time that the launch was most recently updated.

metricMonitors -> (list)

An array of structures that define the metrics that are being used to monitor the launch performance.

(structure)

A structure that defines a metric to be used to monitor performance of the variations during a launch.

metricDefinition -> (structure)

A structure that defines the metric.

entityIdKey -> (string)

The entity, such as a user or session, that does an action that causes a metric value to be recorded.

eventPattern -> (string)

The EventBridge event pattern that defines how the metric is recorded.

For more information about EventBridge event patterns, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html) .

name -> (string)

The name of the metric.

unitLabel -> (string)

The label for the units that the metric is measuring.

valueKey -> (string)

The value that is tracked to produce the metric.

name -> (string)

The name of the launch.

project -> (string)

The name or ARN of the project that contains the launch.

randomizationSalt -> (string)

This value is used when Evidently assigns a particular user session to the launch, to help create a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and `randomizationSalt` .

scheduledSplitsDefinition -> (structure)

An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.

steps -> (list)

An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch. This also defines the start time of each step.

(structure)

This structure defines the traffic allocation percentages among the feature variations during one step of a launch, and the start time of that step.

groupWeights -> (map)

The traffic allocation percentages among the feature variations during one step of a launch. This is a set of key-value pairs. The keys are variation names. The values represent the percentage of traffic to allocate to that variation during this step.

The values is expressed in thousandths of a percent, so assigning a weight of 50000 assigns 50% of traffic to that variation.

If the sum of the weights for all the variations in a segment override does not add up to 100,000, then the remaining traffic that matches this segment is not assigned by this segment override, and instead moves on to the next segment override or the default traffic split.

key -> (string)

value -> (long)

segmentOverrides -> (list)

Use this parameter to specify different traffic splits for one or more audience *segments* . A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.

This parameter is an array of up to six segment override objects. Each of these objects specifies a segment that you have already created, and defines the traffic split for that segment.

(structure)

This structure specifies a segment that you have already created, and defines the traffic split for that segment to be used in a launch.

evaluationOrder -> (long)

A number indicating the order to use to evaluate segment overrides, if there are more than one. Segment overrides with lower numbers are evaluated first.

segment -> (string)

The ARN of the segment to use.

weights -> (map)

The traffic allocation percentages among the feature variations to assign to this segment. This is a set of key-value pairs. The keys are variation names. The values represent the amount of traffic to allocate to that variation for this segment. This is expressed in thousandths of a percent, so a weight of 50000 represents 50% of traffic.

key -> (string)

value -> (long)

startTime -> (timestamp)

The date and time that this step of the launch starts.

status -> (string)

The current state of the launch.

statusReason -> (string)

If the launch was stopped, this is the string that was entered by the person who stopped the launch, to explain why it was stopped.

tags -> (map)

The list of tag keys and values associated with this launch.

key -> (string)

value -> (string)

type -> (string)

The type of launch.