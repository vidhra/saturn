# get-recommendation-preferencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-preferences.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-preferences.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-recommendation-preferences

## Description

Returns existing recommendation preferences, such as enhanced infrastructure metrics.

Use the `scope` parameter to specify which preferences to return. You can specify to return preferences for an organization, a specific account ID, or a specific EC2 instance or Auto Scaling group Amazon Resource Name (ARN).

For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetRecommendationPreferences)

`get-recommendation-preferences` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `recommendationPreferencesDetails`

## Synopsis

```
get-recommendation-preferences
--resource-type <value>
[--scope <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--resource-type` (string)

The target resource type of the recommendation preference for which to return preferences.

The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.

Possible values:

- `Ec2Instance`
- `AutoScalingGroup`
- `EbsVolume`
- `LambdaFunction`
- `NotApplicable`
- `EcsService`
- `License`
- `RdsDBInstance`
- `Idle`

`--scope` (structure)

An object that describes the scope of the recommendation preference to return.

You can return recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

name -> (string)

The name of the scope.

The following scopes are possible:

- `Organization` - Specifies that the recommendation preference applies at the organization level, for all member accounts of an organization.
- `AccountId` - Specifies that the recommendation preference applies at the account level, for all resources of a given resource type in an account.
- `ResourceArn` - Specifies that the recommendation preference applies at the individual resource level.

value -> (string)

The value of the scope.

If you specified the `name` of the scope as:

- `Organization` - The `value` must be `ALL_ACCOUNTS` .
- `AccountId` - The `value` must be a 12-digit Amazon Web Services account ID.
- `ResourceArn` - The `value` must be the Amazon Resource Name (ARN) of an EC2 instance or an Auto Scaling group.

Only EC2 instance and Auto Scaling group ARNs are currently supported.

Shorthand Syntax:

```
name=string,value=string
```

JSON Syntax:

```
{
  "name": "Organization"|"AccountId"|"ResourceArn",
  "value": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

nextToken -> (string)

The token to use to advance to the next page of recommendation preferences.

This value is null when there are no more pages of recommendation preferences to return.

recommendationPreferencesDetails -> (list)

An array of objects that describe recommendation preferences.

(structure)

Describes a recommendation preference.

scope -> (structure)

An object that describes the scope of the recommendation preference.

Recommendation preferences can be created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

name -> (string)

The name of the scope.

The following scopes are possible:

- `Organization` - Specifies that the recommendation preference applies at the organization level, for all member accounts of an organization.
- `AccountId` - Specifies that the recommendation preference applies at the account level, for all resources of a given resource type in an account.
- `ResourceArn` - Specifies that the recommendation preference applies at the individual resource level.

value -> (string)

The value of the scope.

If you specified the `name` of the scope as:

- `Organization` - The `value` must be `ALL_ACCOUNTS` .
- `AccountId` - The `value` must be a 12-digit Amazon Web Services account ID.
- `ResourceArn` - The `value` must be the Amazon Resource Name (ARN) of an EC2 instance or an Auto Scaling group.

Only EC2 instance and Auto Scaling group ARNs are currently supported.

resourceType -> (string)

The target resource type of the recommendation preference to create.

The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.

enhancedInfrastructureMetrics -> (string)

The status of the enhanced infrastructure metrics recommendation preference.

When the recommendations page is refreshed, a status of `Active` confirms that the preference is applied to the recommendations, and a status of `Inactive` confirms that the preference isnât yet applied to recommendations.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

inferredWorkloadTypes -> (string)

The status of the inferred workload types recommendation preference.

When the recommendations page is refreshed, a status of `Active` confirms that the preference is applied to the recommendations, and a status of `Inactive` confirms that the preference isnât yet applied to recommendations.

externalMetricsPreference -> (structure)

An object that describes the external metrics recommendation preference.

If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isnât applied to the recommendations already, then this object doesnât appear in the response.

source -> (string)

Contains the source options for external metrics preferences.

lookBackPeriod -> (string)

The preference to control the number of days the utilization metrics of the Amazon Web Services resource are analyzed. If the preference isnât set, this object is null.

utilizationPreferences -> (list)

The preference to control the resourceâs CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. If the preference isnât set, this object is null.

### Note

This preference is only available for the Amazon EC2 instance resource type.

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

The preference to control which resource type values are considered when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. If the preference isnât set, this object is null.

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

savingsEstimationMode -> (string)

Describes the savings estimation mode used for calculating savings opportunity.

Only the account manager or delegated administrator of your organization can activate this preference.