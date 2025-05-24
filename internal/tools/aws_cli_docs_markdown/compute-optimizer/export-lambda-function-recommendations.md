# export-lambda-function-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-lambda-function-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-lambda-function-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# export-lambda-function-recommendations

## Description

Exports optimization recommendations for Lambda functions.

Recommendations are exported in a comma-separated values (.csv) file, and its metadata in a JavaScript Object Notation (JSON) (.json) file, to an existing Amazon Simple Storage Service (Amazon S3) bucket that you specify. For more information, see [Exporting Recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html) in the *Compute Optimizer User Guide* .

You can have only one Lambda function export job in progress per Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/ExportLambdaFunctionRecommendations)

## Synopsis

```
export-lambda-function-recommendations
[--account-ids <value>]
[--filters <value>]
[--fields-to-export <value>]
--s3-destination-config <value>
[--file-format <value>]
[--include-member-accounts | --no-include-member-accounts]
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

`--account-ids` (list)

The IDs of the Amazon Web Services accounts for which to export Lambda function recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to export recommendations.

This parameter cannot be specified together with the include member accounts parameter. The parameters are mutually exclusive.

Recommendations for member accounts are not included in the export if this parameter, or the include member accounts parameter, is omitted.

You can specify multiple account IDs per request.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

An array of objects to specify a filter that exports a more specific set of Lambda function recommendations.

(structure)

Describes a filter that returns a more specific list of Lambda function recommendations. Use this filter with the  GetLambdaFunctionRecommendations action.

You can use `EBSFilter` with the  GetEBSVolumeRecommendations action, `JobFilter` with the  DescribeRecommendationExportJobs action, and `Filter` with the  GetAutoScalingGroupRecommendations and  GetEC2InstanceRecommendations actions.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification (for example, `NotOptimized` ).

Specify `FindingReasonCode` to return recommendations with a specific finding reason code (for example, `MemoryUnderprovisioned` ).

You can filter your Lambda function recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your Lambda function recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Lambda function recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your Lambda function recommendations. Use this filter to find all of your Lambda function recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your Lambda function recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values for this parameter are as follows, depending on what you specify for the `name` parameter:

- Specify `Optimized` , `NotOptimized` , or `Unavailable` if you specify the `name` parameter as `Finding` .
- Specify `MemoryOverprovisioned` , `MemoryUnderprovisioned` , `InsufficientData` , or `Inconclusive` if you specify the `name` parameter as `FindingReasonCode` .

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Finding"|"FindingReasonCode",
    "values": ["string", ...]
  }
  ...
]
```

`--fields-to-export` (list)

The recommendations data to include in the export file. For more information about the fields that can be exported, see [Exported files](https://docs.aws.amazon.com/compute-optimizer/latest/ug/exporting-recommendations.html#exported-files) in the *Compute Optimizer User Guide* .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AccountId
  FunctionArn
  FunctionVersion
  Finding
  FindingReasonCodes
  NumberOfInvocations
  UtilizationMetricsDurationMaximum
  UtilizationMetricsDurationAverage
  UtilizationMetricsMemoryMaximum
  UtilizationMetricsMemoryAverage
  LookbackPeriodInDays
  CurrentConfigurationMemorySize
  CurrentConfigurationTimeout
  CurrentCostTotal
  CurrentCostAverage
  RecommendationOptionsConfigurationMemorySize
  RecommendationOptionsCostLow
  RecommendationOptionsCostHigh
  RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound
  RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound
  RecommendationOptionsProjectedUtilizationMetricsDurationExpected
  LastRefreshTimestamp
  CurrentPerformanceRisk
  RecommendationOptionsSavingsOpportunityPercentage
  RecommendationOptionsEstimatedMonthlySavingsCurrency
  RecommendationOptionsEstimatedMonthlySavingsValue
  Tags
  EffectiveRecommendationPreferencesSavingsEstimationMode
  RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage
  RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts
  RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts
```

`--s3-destination-config` (structure)

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for a recommendations export job.

You must create the destination Amazon S3 bucket for your recommendations export before you create the export job. Compute Optimizer does not create the S3 bucket for you. After you create the S3 bucket, ensure that it has the required permission policy to allow Compute Optimizer to write the export file to it. If you plan to specify an object prefix when you create the export job, you must include the object prefix in the policy that you add to the S3 bucket. For more information, see [Amazon S3 Bucket Policy for Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/create-s3-bucket-policy-for-compute-optimizer.html) in the *Compute Optimizer User Guide* .

bucket -> (string)

The name of the Amazon S3 bucket to use as the destination for an export job.

keyPrefix -> (string)

The Amazon S3 bucket prefix for an export job.

Shorthand Syntax:

```
bucket=string,keyPrefix=string
```

JSON Syntax:

```
{
  "bucket": "string",
  "keyPrefix": "string"
}
```

`--file-format` (string)

The format of the export file.

The only export file format currently supported is `Csv` .

Possible values:

- `Csv`

`--include-member-accounts` | `--no-include-member-accounts` (boolean)

Indicates whether to include recommendations for resources in all member accounts of the organization if your account is the management account of an organization.

The member accounts must also be opted in to Compute Optimizer, and trusted access for Compute Optimizer must be enabled in the organization account. For more information, see [Compute Optimizer and Amazon Web Services Organizations trusted access](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#trusted-service-access) in the *Compute Optimizer User Guide* .

Recommendations for member accounts of the organization are not included in the export file if this parameter is omitted.

This parameter cannot be specified together with the account IDs parameter. The parameters are mutually exclusive.

Recommendations for member accounts are not included in the export if this parameter, or the account IDs parameter, is omitted.

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

jobId -> (string)

The identification number of the export job.

Use the  DescribeRecommendationExportJobs action, and specify the job ID to view the status of an export job.

s3Destination -> (structure)

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.

bucket -> (string)

The name of the Amazon S3 bucket used as the destination of an export file.

key -> (string)

The Amazon S3 bucket key of an export file.

The key uniquely identifies the object, or export file, in the S3 bucket.

metadataKey -> (string)

The Amazon S3 bucket key of a metadata file.

The key uniquely identifies the object, or metadata file, in the S3 bucket.