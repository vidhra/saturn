# get-effective-recommendation-preferencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-effective-recommendation-preferences.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-effective-recommendation-preferences.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-effective-recommendation-preferences

## Description

Returns the recommendation preferences that are in effect for a given resource, such as enhanced infrastructure metrics. Considers all applicable preferences that you might have set at the resource, account, and organization level.

When you create a recommendation preference, you can set its status to `Active` or `Inactive` . Use this action to view the recommendation preferences that are in effect, or `Active` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetEffectiveRecommendationPreferences)

## Synopsis

```
get-effective-recommendation-preferences
--resource-arn <value>
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

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the resource for which to confirm effective recommendation preferences. Only EC2 instance and Auto Scaling group ARNs are currently supported.

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

enhancedInfrastructureMetrics -> (string)

The status of the enhanced infrastructure metrics recommendation preference. Considers all applicable preferences that you might have set at the resource, account, and organization level.

A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that itâs not yet applied to recommendations.

To validate whether the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the  GetAutoScalingGroupRecommendations and  GetEC2InstanceRecommendations actions.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

externalMetricsPreference -> (structure)

The provider of the external metrics recommendation preference. Considers all applicable preferences that you might have set at the account and organization level.

If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isnât applied to the recommendations already, then this object doesnât appear in the response.

To validate whether the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the  GetEC2InstanceRecommendations actions.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html) in the *Compute Optimizer User Guide* .

source -> (string)

Contains the source options for external metrics preferences.

lookBackPeriod -> (string)

The number of days the utilization metrics of the Amazon Web Services resource are analyzed.

To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.

utilizationPreferences -> (list)

The resourceâs CPU and memory utilization preferences, such as threshold and headroom, that were used to generate rightsizing recommendations. It considers all applicable preferences that you set at the resource, account, and organization level.

To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.

(structure)

The preference to control the resourceâs CPU utilization threshold, CPU utilization headroom, and memory utilization headroom.

### Note

This preference is only available for the Amazon EC2 instance resource type.

metricName -> (string)

The name of the resource utilization metric name to customize.

metricParameters -> (structure)

The parameters to set when customizing the resource utilization thresholds.

threshold -> (string)

The threshold value used for the specified metric parameter.

### Note

You can only specify the threshold value for CPU utilization.

headroom -> (string)

The headroom value in percentage used for the specified metric parameter.

The following lists the valid values for CPU and memory utilization.

- CPU utilization: `PERCENT_30 | PERCENT_20 | PERCENT_0`
- Memory utilization: `PERCENT_30 | PERCENT_20 | PERCENT_10`

preferredResources -> (list)

The resource type values that are considered as candidates when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. It also considers all applicable preferences that you set at the resource, account, and organization level.

To validate that the preference is applied to your last generated set of recommendations, review the `effectiveRecommendationPreferences` value in the response of the GetAutoScalingGroupRecommendations or GetEC2InstanceRecommendations actions.

(structure)

Describes the effective preferred resources that Compute Optimizer considers as rightsizing recommendation candidates.

### Note

Compute Optimizer only supports Amazon EC2 instance types.

name -> (string)

The name of the preferred resource list.

includeList -> (list)

The list of preferred resource values that you want considered as rightsizing recommendation candidates.

(string)

effectiveIncludeList -> (list)

The expanded version of your preferred resourceâs include list.

(string)

excludeList -> (list)

The list of preferred resources values that you want excluded from rightsizing recommendation candidates.

(string)