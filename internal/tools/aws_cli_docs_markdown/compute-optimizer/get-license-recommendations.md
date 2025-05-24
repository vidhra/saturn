# get-license-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-license-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-license-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [compute-optimizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html#cli-aws-compute-optimizer) ]

# get-license-recommendations

## Description

Returns license recommendations for Amazon EC2 instances that run on a specific license.

Compute Optimizer generates recommendations for licenses that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the *Compute Optimizer User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/compute-optimizer-2019-11-01/GetLicenseRecommendations)

## Synopsis

```
get-license-recommendations
[--resource-arns <value>]
[--next-token <value>]
[--max-results <value>]
[--filters <value>]
[--account-ids <value>]
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

`--resource-arns` (list)

The ARN that identifies the Amazon EC2 instance.

The following is the format of the ARN:

`arn:aws:ec2:region:aws_account_id:instance/instance-id`

(string)

Syntax:

```
"string" "string" ...
```

`--next-token` (string)

The token to advance to the next page of license recommendations.

`--max-results` (integer)

The maximum number of license recommendations to return with a single request.

To retrieve the remaining results, make another request with the returned `nextToken` value.

`--filters` (list)

An array of objects to specify a filter that returns a more specific list of license recommendations.

(structure)

Describes a filter that returns a more specific list of license recommendations. Use this filter with the `GetLicenseRecommendation` action.

name -> (string)

The name of the filter.

Specify `Finding` to return recommendations with a specific finding classification.

Specify `FindingReasonCode` to return recommendations with a specific finding reason code.

You can filter your license recommendations by `tag:key` and `tag-key` tags.

A `tag:key` is a key and value combination of a tag assigned to your license recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all license recommendations that have a tag with the key of `Owner` and the value of `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.

A `tag-key` is the key of a tag assigned to your license recommendations. Use this filter to find all of your license recommendations that have a tag with a specific key. This doesnât consider the tag value. For example, you can find your license recommendations with a tag key value of `Owner` or without any tag keys assigned.

values -> (list)

The value of the filter.

The valid values for this parameter are as follows, depending on what you specify for the `name` parameter:

- If you specify the `name` parameter as `Finding` , then specify `Optimized` , `NotOptimized` , or `InsufficentMetrics` .
- If you specify the `name` parameter as `FindingReasonCode` , then specify `Optimized` , `LicenseOverprovisioned` , `InvalidCloudwatchApplicationInsights` , or `CloudwatchApplicationInsightsError` .

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "Finding"|"FindingReasonCode"|"LicenseName",
    "values": ["string", ...]
  }
  ...
]
```

`--account-ids` (list)

The ID of the Amazon Web Services account for which to return license recommendations.

If your account is the management account of an organization, use this parameter to specify the member account for which you want to return license recommendations.

Only one account ID can be specified per request.

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

## Output

nextToken -> (string)

The token to use to advance to the next page of license recommendations.

licenseRecommendations -> (list)

An array of objects that describe license recommendations.

(structure)

Describes a license recommendation for an EC2 instance.

resourceArn -> (string)

The ARN that identifies the Amazon EC2 instance.

accountId -> (string)

The Amazon Web Services account ID of the license.

currentLicenseConfiguration -> (structure)

An object that describes the current configuration of an instance that runs on a license.

numberOfCores -> (integer)

The current number of cores associated with the instance.

instanceType -> (string)

The instance type used in the license.

operatingSystem -> (string)

The operating system of the instance.

licenseEdition -> (string)

The edition of the license for the application that runs on the instance.

licenseName -> (string)

The name of the license for the application that runs on the instance.

licenseModel -> (string)

The license type associated with the instance.

licenseVersion -> (string)

The version of the license for the application that runs on the instance.

metricsSource -> (list)

The list of metric sources required to generate recommendations for commercial software licenses.

(structure)

The list of metric sources required to generate recommendations for commercial software licenses.

provider -> (string)

The name of the metric source provider.

providerArn -> (string)

The ARN of the metric source provider.

lookbackPeriodInDays -> (double)

The number of days for which utilization metrics were analyzed for an instance that runs on a license.

lastRefreshTimestamp -> (timestamp)

The timestamp of when the license recommendation was last generated.

finding -> (string)

The finding classification for an instance that runs on a license.

Findings include:

- `InsufficentMetrics` â When Compute Optimizer detects that your CloudWatch Application Insights isnât enabled or is enabled with insufficient permissions.
- `NotOptimized` â When Compute Optimizer detects that your EC2 infrastructure isnât using any of the SQL server license features youâre paying for, a license is considered not optimized.
- `Optimized` â When Compute Optimizer detects that all specifications of your license meet the performance requirements of your workload.

findingReasonCodes -> (list)

The reason for the finding classification for an instance that runs on a license.

Finding reason codes include:

- `Optimized` â All specifications of your license meet the performance requirements of your workload.
- `LicenseOverprovisioned` â A license is considered over-provisioned when your license can be downgraded while still meeting the performance requirements of your workload.
- `InvalidCloudwatchApplicationInsights` â CloudWatch Application Insights isnât configured properly.
- `CloudwatchApplicationInsightsError` â There is a CloudWatch Application Insights error.

(string)

licenseRecommendationOptions -> (list)

An array of objects that describe the license recommendation options.

(structure)

Describes the recommendation options for licenses.

rank -> (integer)

The rank of the license recommendation option.

The top recommendation option is ranked as `1` .

operatingSystem -> (string)

The operating system of a license recommendation option.

licenseEdition -> (string)

The recommended edition of the license for the application that runs on the instance.

licenseModel -> (string)

The recommended license type associated with the instance.

savingsOpportunity -> (structure)

Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.

Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.

### Warning

Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide* .

savingsOpportunityPercentage -> (double)

The estimated monthly savings possible as a percentage of monthly cost by adopting Compute Optimizer recommendations for a given resource.

estimatedMonthlySavings -> (structure)

An object that describes the estimated monthly savings amount possible by adopting Compute Optimizer recommendations for a given resource. This is based on the On-Demand instance pricing..

currency -> (string)

The currency of the estimated monthly savings.

value -> (double)

The value of the estimated monthly savings.

tags -> (list)

A list of tags assigned to an EC2 instance.

(structure)

A list of tag key and value pairs that you define.

key -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

value -> (string)

One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.

errors -> (list)

An array of objects that describe errors of the request.

(structure)

Describes an error experienced when getting recommendations.

For example, an error is returned if you request recommendations for an unsupported Auto Scaling group, or if you request recommendations for an instance of an unsupported instance family.

identifier -> (string)

The ID of the error.

code -> (string)

The error code.

message -> (string)

The message, or reason, for the error.