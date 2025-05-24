# get-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/get-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguruprofiler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html#cli-aws-codeguruprofiler) ]

# get-recommendations

## Description

Returns a list of ` `Recommendation` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation).html`__ objects that contain recommendations for a profiling group for a given time period. A list of ` `Anomaly` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly).html`__ objects that contains details about anomalies detected in the profiling group for the same time period is also returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguruprofiler-2019-07-18/GetRecommendations)

## Synopsis

```
get-recommendations
--end-time <value>
[--locale <value>]
--profiling-group-name <value>
--start-time <value>
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

`--end-time` (timestamp)

The start time of the profile to get analysis data about. You must specify `startTime` and `endTime` . This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

`--locale` (string)

The language used to provide analysis. Specify using a string that is one of the following `BCP 47` language codes.

- `de-DE` - German, Germany
- `en-GB` - English, United Kingdom
- `en-US` - English, United States
- `es-ES` - Spanish, Spain
- `fr-FR` - French, France
- `it-IT` - Italian, Italy
- `ja-JP` - Japanese, Japan
- `ko-KR` - Korean, Republic of Korea
- `pt-BR` - Portugese, Brazil
- `zh-CN` - Chinese, China
- `zh-TW` - Chinese, Taiwan

`--profiling-group-name` (string)

The name of the profiling group to get analysis data about.

`--start-time` (timestamp)

The end time of the profile to get analysis data about. You must specify `startTime` and `endTime` . This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

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

anomalies -> (list)

The list of anomalies that the analysis has found for this profile.

(structure)

Details about an anomaly in a specific metric of application profile. The anomaly is detected using analysis of the metric data over a period of time.

instances -> (list)

A list of the instances of the detected anomalies during the requested period.

(structure)

The specific duration in which the metric is flagged as anomalous.

endTime -> (timestamp)

The end time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

id -> (string)

The universally unique identifier (UUID) of an instance of an anomaly in a metric.

startTime -> (timestamp)

The start time of the period during which the metric is flagged as anomalous. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

userFeedback -> (structure)

Feedback type on a specific instance of anomaly submitted by the user.

type -> (string)

Optional `Positive` or `Negative` feedback submitted by the user about whether the recommendation is useful or not.

metric -> (structure)

Details about the metric that the analysis used when it detected the anomaly. The metric includes the name of the frame that was analyzed with the type and thread states used to derive the metric value for that frame.

frameName -> (string)

The name of the method that appears as a frame in any stack in a profile.

threadStates -> (list)

The list of application runtime thread states that is used to calculate the metric value for the frame.

(string)

type -> (string)

A type that specifies how a metric for a frame is analyzed. The supported value `AggregatedRelativeTotalTime` is an aggregation of the metric value for one frame that is calculated across the occurences of all frames in a profile.

reason -> (string)

The reason for which metric was flagged as anomalous.

profileEndTime -> (timestamp)

The end time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

profileStartTime -> (timestamp)

The start time of the profile the analysis data is about. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

profilingGroupName -> (string)

The name of the profiling group the analysis data is about.

recommendations -> (list)

The list of recommendations that the analysis found for this profile.

(structure)

A potential improvement that was found from analyzing the profiling data.

allMatchesCount -> (integer)

How many different places in the profile graph triggered a match.

allMatchesSum -> (double)

How much of the total sample count is potentially affected.

endTime -> (timestamp)

End time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

pattern -> (structure)

The pattern that analysis recognized in the profile to make this recommendation.

countersToAggregate -> (list)

A list of the different counters used to determine if there is a match.

(string)

description -> (string)

The description of the recommendation. This explains a potential inefficiency in a profiled application.

id -> (string)

The universally unique identifier (UUID) of this pattern.

name -> (string)

The name for this pattern.

resolutionSteps -> (string)

A string that contains the steps recommended to address the potential inefficiency.

targetFrames -> (list)

A list of frame names that were searched during the analysis that generated a recommendation.

(list)

(string)

thresholdPercent -> (double)

The percentage of time an application spends in one method that triggers a recommendation. The percentage of time is the same as the percentage of the total gathered sample counts during analysis.

startTime -> (timestamp)

The start time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

topMatches -> (list)

List of the matches with most impact.

(structure)

The part of a profile that contains a recommendation found during analysis.

frameAddress -> (string)

The location in the profiling graph that contains a recommendation found during analysis.

targetFramesIndex -> (integer)

The target frame that triggered a match.

thresholdBreachValue -> (double)

The value in the profile data that exceeded the recommendation threshold.