# get-experimentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-experiment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-experiment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# get-experiment

## Description

Returns the details about one experiment. You must already know the experiment name. To retrieve a list of experiments in your account, use [ListExperiments](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/GetExperiment)

## Synopsis

```
get-experiment
--experiment <value>
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

`--experiment` (string)

The name of the experiment that you want to see the details of.

`--project` (string)

The name or ARN of the project that contains the experiment.

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

experiment -> (structure)

A structure containing the configuration details of the experiment.

arn -> (string)

The ARN of the experiment.

createdTime -> (timestamp)

The date and time that the experiment is first created.

description -> (string)

A description of the experiment.

execution -> (structure)

A structure that contains the date and time that the experiment started and ended.

endedTime -> (timestamp)

The date and time that the experiment ended.

startedTime -> (timestamp)

The date and time that the experiment started.

lastUpdatedTime -> (timestamp)

The date and time that the experiment was most recently updated.

metricGoals -> (list)

An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal.

(structure)

A structure that tells Evidently whether higher or lower values are desired for a metric that is used in an experiment.

desiredChange -> (string)

`INCREASE` means that a variation with a higher number for this metric is performing better.

`DECREASE` means that a variation with a lower number for this metric is performing better.

metricDefinition -> (structure)

A structure that contains details about the metric.

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

The name of the experiment.

onlineAbDefinition -> (structure)

A structure that contains the configuration of which variation to use as the âcontrolâ version. The âcontrolâ version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

controlTreatmentName -> (string)

The name of the variation that is the default variation that the other variations are compared to.

treatmentWeights -> (map)

A set of key-value pairs. The keys are variation names, and the values are the portion of experiment traffic to be assigned to that variation. The traffic portion is specified in thousandths of a percent, so 20,000 for a variation would allocate 20% of the experiment traffic to that variation.

key -> (string)

value -> (long)

project -> (string)

The name or ARN of the project that contains this experiment.

randomizationSalt -> (string)

This value is used when Evidently assigns a particular user session to the experiment. It helps create a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and `randomizationSalt` .

samplingRate -> (long)

In thousandths of a percent, the amount of the available audience that is allocated to this experiment. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.

This is represented in thousandths of a percent, so a value of 10,000 is 10% of the available audience.

schedule -> (structure)

A structure that contains the time and date that Evidently completed the analysis of the experiment.

analysisCompleteTime -> (timestamp)

The time and date that Evidently completed the analysis of the experiment.

segment -> (string)

The audience segment being used for the experiment, if a segment is being used.

status -> (string)

The current state of the experiment.

statusReason -> (string)

If the experiment was stopped, this is the string that was entered by the person who stopped the experiment, to explain why it was stopped.

tags -> (map)

The list of tag keys and values associated with this experiment.

key -> (string)

value -> (string)

treatments -> (list)

An array of structures that describe the configuration of each feature variation used in the experiment.

(structure)

A structure that defines one treatment in an experiment. A treatment is a variation of the feature that you are including in the experiment.

description -> (string)

The description of the treatment.

featureVariations -> (map)

The feature variation used for this treatment. This is a key-value pair. The key is the feature name, and the value is the variation name.

key -> (string)

value -> (string)

name -> (string)

The name of this treatment.

type -> (string)

The type of this experiment. Currently, this value must be `aws.experiment.onlineab` .