# put-recommendation-preferencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/put-recommendation-preferences.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/put-recommendation-preferences.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# put-recommendation-preferences

## Description

Creates a new recommendation preference or updates an existing recommendation preference, such as enhanced infrastructure metrics.

For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/PutRecommendationPreferences)

## Synopsis

```
put-recommendation-preferences
--resource-type <value>
[--scope <value>]
[--enhanced-infrastructure-metrics <value>]
[--inferred-workload-types <value>]
[--external-metrics-preference <value>]
[--look-back-period <value>]
[--utilization-preferences <value>]
[--preferred-resources <value>]
[--savings-estimation-mode <value>]
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

`--resource-type` (string)

The target resource type of the recommendation preference to create.

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

An object that describes the scope of the recommendation preference to create.

You can create recommendation preferences at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

### Note

You cannot create recommendation preferences for Auto Scaling groups at the organization and account levels. You can create recommendation preferences for Auto Scaling groups only at the resource level by specifying a scope name of `ResourceArn` and a scope value of the Auto Scaling group Amazon Resource Name (ARN). This will configure the preference for all instances that are part of the specified Auto Scaling group. You also cannot create recommendation preferences at the resource level for instances that are part of an Auto Scaling group. You can create recommendation preferences at the resource level only for standalone instances.

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

`--enhanced-infrastructure-metrics` (string)

The status of the enhanced infrastructure metrics recommendation preference to create or update.

Specify the `Active` status to activate the preference, or specify `Inactive` to deactivate the preference.

For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the *Compute Optimizer User Guide* .

Possible values:

- `Active`
- `Inactive`

`--inferred-workload-types` (string)

The status of the inferred workload types recommendation preference to create or update.

### Note

The inferred workload type feature is active by default. To deactivate it, create a recommendation preference.

Specify the `Inactive` status to deactivate the feature, or specify `Active` to activate it.

For more information, see [Inferred workload types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-types.html) in the *Compute Optimizer User Guide* .

Possible values:

- `Active`
- `Inactive`

`--external-metrics-preference` (structure)

The provider of the external metrics recommendation preference to create or update.

Specify a valid provider in the `source` field to activate the preference. To delete this preference, see the  DeleteRecommendationPreferences action.

This preference can only be set for the `Ec2Instance` resource type.

For more information, see [External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html) in the *Compute Optimizer User Guide* .

source -> (string)

Contains the source options for external metrics preferences.

Shorthand Syntax:

```
source=string
```

JSON Syntax:

```
{
  "source": "Datadog"|"Dynatrace"|"NewRelic"|"Instana"
}
```

`--look-back-period` (string)

The preference to control the number of days the utilization metrics of the Amazon Web Services resource are analyzed. When this preference isnât specified, we use the default value `DAYS_14` .

You can only set this preference for the Amazon EC2 instance and Auto Scaling group resource types.

### Note

- Amazon EC2 instance lookback preferences can be set at the organization, account, and resource levels.
- Auto Scaling group lookback preferences can only be set at the resource level.

Possible values:

- `DAYS_14`
- `DAYS_32`
- `DAYS_93`

`--utilization-preferences` (list)

The preference to control the resourceâs CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. When this preference isnât specified, we use the following default values.

CPU utilization:

- `P99_5` for threshold
- `PERCENT_20` for headroom

Memory utilization:

- `PERCENT_20` for headroom

### Note

- You can only set CPU and memory utilization preferences for the Amazon EC2 instance resource type.
- The threshold setting isnât available for memory utilization.

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

Shorthand Syntax:

```
metricName=string,metricParameters={threshold=string,headroom=string} ...
```

JSON Syntax:

```
[
  {
    "metricName": "CpuUtilization"|"MemoryUtilization",
    "metricParameters": {
      "threshold": "P90"|"P95"|"P99_5",
      "headroom": "PERCENT_30"|"PERCENT_20"|"PERCENT_10"|"PERCENT_0"
    }
  }
  ...
]
```

`--preferred-resources` (list)

The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an `includeList` or `excludeList` . If the preference is an empty set of resource type values, an error occurs.

### Note

You can only set this preference for the Amazon EC2 instance and Auto Scaling group resource types.

(structure)

The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an `includeList` or `excludeList` . If the preference is an empty set of resource type values, an error occurs. For more information, see [Rightsizing recommendation preferences](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rightsizing-preferences.html) in the *Compute Optimizer User Guide* .

### Note

- This preference is only available for the Amazon EC2 instance and Auto Scaling group resource types.
- Compute Optimizer only supports the customization of `Ec2InstanceTypes` .

name -> (string)

The type of preferred resource to customize.

### Note

Compute Optimizer only supports the customization of `Ec2InstanceTypes` .

includeList -> (list)

The preferred resource type values to include in the recommendation candidates. You can specify the exact resource type value, such as m5.large, or use wild card expressions, such as m5. If this isnât specified, all supported resources are included by default. You can specify up to 1000 values in this list.

(string)

excludeList -> (list)

The preferred resource type values to exclude from the recommendation candidates. If this isnât specified, all supported resources are included by default. You can specify up to 1000 values in this list.

(string)

Shorthand Syntax:

```
name=string,includeList=string,string,excludeList=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Ec2InstanceTypes",
    "includeList": ["string", ...],
    "excludeList": ["string", ...]
  }
  ...
]
```

`--savings-estimation-mode` (string)

The status of the savings estimation mode preference to create or update.

Specify the `AfterDiscounts` status to activate the preference, or specify `BeforeDiscounts` to deactivate the preference.

Only the account manager or delegated administrator of your organization can activate this preference.

For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode.html) in the *Compute Optimizer User Guide* .

Possible values:

- `AfterDiscounts`
- `BeforeDiscounts`

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

None