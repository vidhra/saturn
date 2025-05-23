# get-findings-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# get-findings-statistics

## Description

Lists GuardDuty findings statistics for the specified detector ID.

You must provide either `findingStatisticTypes` or `groupBy` parameter, and not both. You can use the `maxResults` and `orderBy` parameters only when using `groupBy` .

There might be regional differences because some flags might not be available in all the Regions where GuardDuty is currently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindingsStatistics)

## Synopsis

```
get-findings-statistics
--detector-id <value>
[--finding-statistic-types <value>]
[--finding-criteria <value>]
[--group-by <value>]
[--order-by <value>]
[--max-results <value>]
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

The ID of the detector whose findings statistics you want to retrieve.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--finding-statistic-types` (list)

The types of finding statistics to retrieve.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  COUNT_BY_SEVERITY
```

`--finding-criteria` (structure)

Represents the criteria that is used for querying findings.

Criterion -> (map)

Represents a map of finding properties that match specified conditions and values when querying findings.

key -> (string)

value -> (structure)

Contains information about the condition.

Eq -> (list)

Represents the *equal* condition to be applied to a single field when querying for findings.

(string)

Neq -> (list)

Represents the *not equal* condition to be applied to a single field when querying for findings.

(string)

Gt -> (integer)

Represents a *greater than* condition to be applied to a single field when querying for findings.

Gte -> (integer)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

Lt -> (integer)

Represents a *less than* condition to be applied to a single field when querying for findings.

Lte -> (integer)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Equals -> (list)

Represents an *equal*  condition to be applied to a single field when querying for findings.

(string)

NotEquals -> (list)

Represents a *not equal*  condition to be applied to a single field when querying for findings.

(string)

GreaterThan -> (long)

Represents a *greater than* condition to be applied to a single field when querying for findings.

GreaterThanOrEqual -> (long)

Represents a *greater than or equal* condition to be applied to a single field when querying for findings.

LessThan -> (long)

Represents a *less than* condition to be applied to a single field when querying for findings.

LessThanOrEqual -> (long)

Represents a *less than or equal* condition to be applied to a single field when querying for findings.

Shorthand Syntax:

```
Criterion={KeyName1={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long},KeyName2={Eq=[string,string],Neq=[string,string],Gt=integer,Gte=integer,Lt=integer,Lte=integer,Equals=[string,string],NotEquals=[string,string],GreaterThan=long,GreaterThanOrEqual=long,LessThan=long,LessThanOrEqual=long}}
```

JSON Syntax:

```
{
  "Criterion": {"string": {
        "Eq": ["string", ...],
        "Neq": ["string", ...],
        "Gt": integer,
        "Gte": integer,
        "Lt": integer,
        "Lte": integer,
        "Equals": ["string", ...],
        "NotEquals": ["string", ...],
        "GreaterThan": long,
        "GreaterThanOrEqual": long,
        "LessThan": long,
        "LessThanOrEqual": long
      }
    ...}
}
```

`--group-by` (string)

Displays the findings statistics grouped by one of the listed valid values.

Possible values:

- `ACCOUNT`
- `DATE`
- `FINDING_TYPE`
- `RESOURCE`
- `SEVERITY`

`--order-by` (string)

Displays the sorted findings in the requested order. The default value of `orderBy` is `DESC` .

You can use this parameter only with the `groupBy` parameter.

Possible values:

- `ASC`
- `DESC`

`--max-results` (integer)

The maximum number of results to be returned in the response. The default value is 25.

You can use this parameter only with the `groupBy` parameter.

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

FindingStatistics -> (structure)

The finding statistics object.

CountBySeverity -> (map)

Represents a list of map of severity to count statistics for a set of findings.

key -> (string)

value -> (integer)

GroupedByAccount -> (list)

Represents a list of map of accounts with a findings count associated with each account.

(structure)

Represents a list of map of accounts with the number of findings associated with each account.

AccountId -> (string)

The ID of the Amazon Web Services account.

LastGeneratedAt -> (timestamp)

The timestamp at which the finding for this account was last generated.

TotalFindings -> (integer)

The total number of findings associated with an account.

GroupedByDate -> (list)

Represents a list of map of dates with a count of total findings generated on each date per severity level.

(structure)

Represents list a map of dates with a count of total findings generated on each date.

Date -> (timestamp)

The timestamp when the total findings count is observed.

For example, `Date` would look like `"2024-09-05T17:00:00-07:00"` whereas `LastGeneratedAt` would look like 2024-09-05T17:12:29-07:00â.

LastGeneratedAt -> (timestamp)

The timestamp at which the last finding in the findings count, was generated.

Severity -> (double)

The severity of the findings generated on each date.

TotalFindings -> (integer)

The total number of findings that were generated per severity level on each date.

GroupedByFindingType -> (list)

Represents a list of map of finding types with a count of total findings generated for each type.

Based on the `orderBy` parameter, this request returns either the most occurring finding types or the least occurring finding types. If the `orderBy` parameter is `ASC` , this will represent the least occurring finding types in your account; otherwise, this will represent the most occurring finding types. The default value of `orderBy` is `DESC` .

(structure)

Information about each finding type associated with the `groupedByFindingType` statistics.

FindingType -> (string)

Name of the finding type.

LastGeneratedAt -> (timestamp)

The timestamp at which this finding type was last generated in your environment.

TotalFindings -> (integer)

The total number of findings associated with generated for each distinct finding type.

GroupedByResource -> (list)

Represents a list of map of top resources with a count of total findings.

(structure)

Information about each resource type associated with the `groupedByResource` statistics.

AccountId -> (string)

The ID of the Amazon Web Services account.

LastGeneratedAt -> (timestamp)

The timestamp at which the statistics for this resource was last generated.

ResourceId -> (string)

ID associated with each resource. The following list provides the mapping of the resource type and resource ID.

**Mapping of resource and resource ID**

- AccessKey - `resource.accessKeyDetails.accessKeyId`
- Container - `resource.containerDetails.id`
- ECSCluster - `resource.ecsClusterDetails.name`
- EKSCluster - `resource.eksClusterDetails.name`
- Instance - `resource.instanceDetails.instanceId`
- KubernetesCluster - `resource.kubernetesDetails.kubernetesWorkloadDetails.name`
- Lambda - `resource.lambdaDetails.functionName`
- RDSDBInstance - `resource.rdsDbInstanceDetails.dbInstanceIdentifier`
- S3Bucket - `resource.s3BucketDetails.name`
- S3Object - `resource.s3BucketDetails.name`

ResourceType -> (string)

The type of resource.

TotalFindings -> (integer)

The total number of findings associated with this resource.

GroupedBySeverity -> (list)

Represents a list of map of total findings for each severity level.

(structure)

Information about severity level for each finding type.

LastGeneratedAt -> (timestamp)

The timestamp at which a finding type for a specific severity was last generated.

Severity -> (double)

The severity level associated with each finding type.

TotalFindings -> (integer)

The total number of findings associated with this severity.

NextToken -> (string)

The pagination parameter to be used on the next list operation to retrieve more items.

This parameter is currently not supported.