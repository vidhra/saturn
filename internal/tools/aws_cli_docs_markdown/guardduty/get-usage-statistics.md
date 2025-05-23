# get-usage-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-usage-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-usage-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# get-usage-statistics

## Description

Lists Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID. For newly enabled detectors or data sources, the cost returned will include only the usage so far under 30 days. This may differ from the cost metrics in the console, which project usage over 30 days to provide a monthly cost estimate. For more information, see [Understanding How Usage Costs are Calculated](https://docs.aws.amazon.com/guardduty/latest/ug/monitoring_costs.html#usage-calculations) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetUsageStatistics)

## Synopsis

```
get-usage-statistics
--detector-id <value>
--usage-statistic-type <value>
--usage-criteria <value>
[--unit <value>]
[--max-results <value>]
[--next-token <value>]
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

`--detector-id` (string)

The ID of the detector that specifies the GuardDuty service whose usage statistics you want to retrieve.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--usage-statistic-type` (string)

The type of usage statistics to retrieve.

Possible values:

- `SUM_BY_ACCOUNT`
- `SUM_BY_DATA_SOURCE`
- `SUM_BY_RESOURCE`
- `TOP_RESOURCES`
- `SUM_BY_FEATURES`
- `TOP_ACCOUNTS_BY_FEATURE`

`--usage-criteria` (structure)

Represents the criteria used for querying usage.

AccountIds -> (list)

The account IDs to aggregate usage statistics from.

(string)

DataSources -> (list)

The data sources to aggregate usage statistics from.

(string)

Resources -> (list)

The resources to aggregate usage statistics from. Only accepts exact resource names.

(string)

Features -> (list)

The features to aggregate usage statistics from.

(string)

Shorthand Syntax:

```
AccountIds=string,string,DataSources=string,string,Resources=string,string,Features=string,string
```

JSON Syntax:

```
{
  "AccountIds": ["string", ...],
  "DataSources": ["FLOW_LOGS"|"CLOUD_TRAIL"|"DNS_LOGS"|"S3_LOGS"|"KUBERNETES_AUDIT_LOGS"|"EC2_MALWARE_SCAN", ...],
  "Resources": ["string", ...],
  "Features": ["FLOW_LOGS"|"CLOUD_TRAIL"|"DNS_LOGS"|"S3_DATA_EVENTS"|"EKS_AUDIT_LOGS"|"EBS_MALWARE_PROTECTION"|"RDS_LOGIN_EVENTS"|"LAMBDA_NETWORK_LOGS"|"EKS_RUNTIME_MONITORING"|"FARGATE_RUNTIME_MONITORING"|"EC2_RUNTIME_MONITORING"|"RDS_DBI_PROTECTION_PROVISIONED"|"RDS_DBI_PROTECTION_SERVERLESS", ...]
}
```

`--unit` (string)

The currency unit you would like to view your usage statistics in. Current valid values are USD.

`--max-results` (integer)

The maximum number of results to return in the response.

`--next-token` (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.

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

UsageStatistics -> (structure)

The usage statistics object. If a UsageStatisticType was provided, the objects representing other types will be null.

SumByAccount -> (list)

The usage statistic sum organized by account ID.

(structure)

Contains information on the total of usage based on account IDs.

AccountId -> (string)

The Account ID that generated usage.

Total -> (structure)

Represents the total of usage for the Account ID.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

TopAccountsByFeature -> (list)

Lists the top 50 accounts by feature that have generated the most GuardDuty usage, in the order from most to least expensive.

Currently, this doesnât support `RDS_LOGIN_EVENTS` .

(structure)

Information about the usage statistics, calculated by top accounts by feature.

Feature -> (string)

Features by which you can generate the usage statistics.

`RDS_LOGIN_EVENTS` is currently not supported with `topAccountsByFeature` .

Accounts -> (list)

The accounts that contributed to the total usage cost.

(structure)

Contains information on the total of usage based on the topmost 50 account IDs.

AccountId -> (string)

The unique account ID.

Total -> (structure)

Contains the total usage with the corresponding currency unit for that value.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

SumByDataSource -> (list)

The usage statistic sum organized by on data source.

(structure)

Contains information on the result of usage based on data source type.

DataSource -> (string)

The data source type that generated usage.

Total -> (structure)

Represents the total of usage for the specified data source.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

SumByResource -> (list)

The usage statistic sum organized by resource.

(structure)

Contains information on the sum of usage based on an Amazon Web Services resource.

Resource -> (string)

The Amazon Web Services resource that generated usage.

Total -> (structure)

Represents the sum total of usage for the specified resource type.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

TopResources -> (list)

Lists the top 50 resources that have generated the most GuardDuty usage, in order from most to least expensive.

(structure)

Contains information on the sum of usage based on an Amazon Web Services resource.

Resource -> (string)

The Amazon Web Services resource that generated usage.

Total -> (structure)

Represents the sum total of usage for the specified resource type.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

SumByFeature -> (list)

The usage statistic sum organized by feature.

(structure)

Contains information about the result of the total usage based on the feature.

Feature -> (string)

The feature that generated the usage cost.

Total -> (structure)

Contains the total usage with the corresponding currency unit for that value.

Amount -> (string)

The total usage.

Unit -> (string)

The currency unit that the amount is given in.

NextToken -> (string)

The pagination parameter to be used on the next list operation to retrieve more items.