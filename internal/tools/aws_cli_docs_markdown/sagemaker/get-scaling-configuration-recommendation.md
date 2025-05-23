# get-scaling-configuration-recommendationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/get-scaling-configuration-recommendation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/get-scaling-configuration-recommendation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# get-scaling-configuration-recommendation

## Description

Starts an Amazon SageMaker Inference Recommender autoscaling recommendation job. Returns recommendations for autoscaling policies that you can apply to your SageMaker endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/GetScalingConfigurationRecommendation)

## Synopsis

```
get-scaling-configuration-recommendation
--inference-recommendations-job-name <value>
[--recommendation-id <value>]
[--endpoint-name <value>]
[--target-cpu-utilization-per-core <value>]
[--scaling-policy-objective <value>]
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

`--inference-recommendations-job-name` (string)

The name of a previously completed Inference Recommender job.

`--recommendation-id` (string)

The recommendation ID of a previously completed inference recommendation. This ID should come from one of the recommendations returned by the job specified in the `InferenceRecommendationsJobName` field.

Specify either this field or the `EndpointName` field.

`--endpoint-name` (string)

The name of an endpoint benchmarked during a previously completed inference recommendation job. This name should come from one of the recommendations returned by the job specified in the `InferenceRecommendationsJobName` field.

Specify either this field or the `RecommendationId` field.

`--target-cpu-utilization-per-core` (integer)

The percentage of how much utilization you want an instance to use before autoscaling. The default value is 50%.

`--scaling-policy-objective` (structure)

An object where you specify the anticipated traffic pattern for an endpoint.

MinInvocationsPerMinute -> (integer)

The minimum number of expected requests to your endpoint per minute.

MaxInvocationsPerMinute -> (integer)

The maximum number of expected requests to your endpoint per minute.

Shorthand Syntax:

```
MinInvocationsPerMinute=integer,MaxInvocationsPerMinute=integer
```

JSON Syntax:

```
{
  "MinInvocationsPerMinute": integer,
  "MaxInvocationsPerMinute": integer
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

InferenceRecommendationsJobName -> (string)

The name of a previously completed Inference Recommender job.

RecommendationId -> (string)

The recommendation ID of a previously completed inference recommendation.

EndpointName -> (string)

The name of an endpoint benchmarked during a previously completed Inference Recommender job.

TargetCpuUtilizationPerCore -> (integer)

The percentage of how much utilization you want an instance to use before autoscaling, which you specified in the request. The default value is 50%.

ScalingPolicyObjective -> (structure)

An object representing the anticipated traffic pattern for an endpoint that you specified in the request.

MinInvocationsPerMinute -> (integer)

The minimum number of expected requests to your endpoint per minute.

MaxInvocationsPerMinute -> (integer)

The maximum number of expected requests to your endpoint per minute.

Metric -> (structure)

An object with a list of metrics that were benchmarked during the previously completed Inference Recommender job.

InvocationsPerInstance -> (integer)

The number of invocations sent to a model, normalized by `InstanceCount` in each ProductionVariant. `1/numberOfInstances` is sent as the value on each request, where `numberOfInstances` is the number of active instances for the ProductionVariant behind the endpoint at the time of the request.

ModelLatency -> (integer)

The interval of time taken by a model to respond as viewed from SageMaker. This interval includes the local communication times taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.

DynamicScalingConfiguration -> (structure)

An object with the recommended values for you to specify when creating an autoscaling policy.

MinCapacity -> (integer)

The recommended minimum capacity to specify for your autoscaling policy.

MaxCapacity -> (integer)

The recommended maximum capacity to specify for your autoscaling policy.

ScaleInCooldown -> (integer)

The recommended scale in cooldown time for your autoscaling policy.

ScaleOutCooldown -> (integer)

The recommended scale out cooldown time for your autoscaling policy.

ScalingPolicies -> (list)

An object of the scaling policies for each metric.

(tagged union structure)

An object containing a recommended scaling policy.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `TargetTracking`.

TargetTracking -> (structure)

A target tracking scaling policy. Includes support for predefined or customized metrics.

MetricSpecification -> (tagged union structure)

An object containing information about a metric.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Predefined`, `Customized`.

Predefined -> (structure)

Information about a predefined metric.

PredefinedMetricType -> (string)

The metric type. You can only apply SageMaker metric types to SageMaker endpoints.

Customized -> (structure)

Information about a customized metric.

MetricName -> (string)

The name of the customized metric.

Namespace -> (string)

The namespace of the customized metric.

Statistic -> (string)

The statistic of the customized metric.

TargetValue -> (double)

The recommended target value to specify for the metric when creating a scaling policy.