# get-aws-default-service-quotaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-aws-default-service-quota.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-aws-default-service-quota.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [service-quotas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/index.html#cli-aws-service-quotas) ]

# get-aws-default-service-quota

## Description

Retrieves the default value for the specified quota. The default value does not reflect any quota increases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/GetAWSDefaultServiceQuota)

## Synopsis

```
get-aws-default-service-quota
--service-code <value>
--quota-code <value>
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

`--service-code` (string)

Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the  ListServices operation.

`--quota-code` (string)

Specifies the quota identifier. To find the quota code for a specific quota, use the  ListServiceQuotas operation, and look for the `QuotaCode` response in the output for the quota you want.

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

**To describe a default service quota**

The following `get-aws-default-service-quota` example displays details for the specified quota.

```
aws service-quotas get-aws-default-service-quota \
    --service-code ec2 \
    --quota-code L-1216C47A
```

Output:

```
{
    "Quota": {
        "ServiceCode": "ec2",
        "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)",
        "QuotaArn": "arn:aws:servicequotas:us-east-2::ec2/L-1216C47A",
        "QuotaCode": "L-1216C47A",
        "QuotaName": "Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances",
        "Value": 5.0,
        "Unit": "None",
        "Adjustable": true,
        "GlobalQuota": false,
        "UsageMetric": {
            "MetricNamespace": "AWS/Usage",
            "MetricName": "ResourceCount",
            "MetricDimensions": {
                "Class": "Standard/OnDemand",
                "Resource": "vCPU",
                "Service": "EC2",
                "Type": "Resource"
            },
            "MetricStatisticRecommendation": "Maximum"
        }
    }
}
```

## Output

Quota -> (structure)

Information about the quota.

ServiceCode -> (string)

Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the  ListServices operation.

ServiceName -> (string)

Specifies the service name.

QuotaArn -> (string)

The Amazon Resource Name (ARN) of the quota.

QuotaCode -> (string)

Specifies the quota identifier. To find the quota code for a specific quota, use the  ListServiceQuotas operation, and look for the `QuotaCode` response in the output for the quota you want.

QuotaName -> (string)

Specifies the quota name.

Value -> (double)

The quota value.

Unit -> (string)

The unit of measurement.

Adjustable -> (boolean)

Indicates whether the quota value can be increased.

GlobalQuota -> (boolean)

Indicates whether the quota is global.

UsageMetric -> (structure)

Information about the measurement.

MetricNamespace -> (string)

The namespace of the metric.

MetricName -> (string)

The name of the metric.

MetricDimensions -> (map)

The metric dimension. This is a name/value pair that is part of the identity of a metric.

key -> (string)

value -> (string)

MetricStatisticRecommendation -> (string)

The metric statistic that we recommend you use when determining quota usage.

Period -> (structure)

The period of time.

PeriodValue -> (integer)

The value associated with the reported `PeriodUnit` .

PeriodUnit -> (string)

The time unit.

ErrorReason -> (structure)

The error code and error reason.

ErrorCode -> (string)

Service Quotas returns the following error values:

- `DEPENDENCY_ACCESS_DENIED_ERROR` - The caller does not have the required permissions to complete the action. To resolve the error, you must have permission to access the Amazon Web Services service or quota.
- `DEPENDENCY_THROTTLING_ERROR` - The Amazon Web Services service is throttling Service Quotas.
- `DEPENDENCY_SERVICE_ERROR` - The Amazon Web Services service is not available.
- `SERVICE_QUOTA_NOT_AVAILABLE_ERROR` - There was an error in Service Quotas.

ErrorMessage -> (string)

The error message.

QuotaAppliedAtLevel -> (string)

Filters the response to return applied quota values for the `ACCOUNT` , `RESOURCE` , or `ALL` levels. `ACCOUNT` is the default.

QuotaContext -> (structure)

The context for this service quota.

ContextScope -> (string)

Specifies the scope to which the quota value is applied. If the scope is `RESOURCE` , the quota value is applied to each resource in the Amazon Web Services account. If the scope is `ACCOUNT` , the quota value is applied to the Amazon Web Services account.

ContextScopeType -> (string)

Specifies the resource type to which the quota can be applied.

ContextId -> (string)

Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-aws-default-service-quota.html#id1). If the value is an ARN, the quota value applies to that resource. If the value is [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-aws-default-service-quota.html#id3), then the quota value applies to all resources listed in the `ContextScopeType` field. The quota value applies to all resources for which you havenât previously applied a quota value, and any new resources you create in your Amazon Web Services account.

Description -> (string)

The quota description.