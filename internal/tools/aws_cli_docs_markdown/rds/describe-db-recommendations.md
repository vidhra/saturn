# describe-db-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-db-recommendations

## Description

Describes the recommendations to resolve the issues for your DB instances, DB clusters, and DB parameter groups.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeDBRecommendations)

`describe-db-recommendations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DBRecommendations`

## Synopsis

```
describe-db-recommendations
[--last-updated-after <value>]
[--last-updated-before <value>]
[--locale <value>]
[--filters <value>]
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

`--last-updated-after` (timestamp)

A filter to include only the recommendations that were updated after this specified time.

`--last-updated-before` (timestamp)

A filter to include only the recommendations that were updated before this specified time.

`--locale` (string)

The language that you choose to return the list of recommendations.

Valid values:

- `en`
- `en_UK`
- `de`
- `es`
- `fr`
- `id`
- `it`
- `ja`
- `ko`
- `pt_BR`
- `zh_TW`
- `zh_CN`

`--filters` (list)

A filter that specifies one or more recommendations to describe.

Supported Filters:

- `recommendation-id` - Accepts a list of recommendation identifiers. The results list only includes the recommendations whose identifier is one of the specified filter values.
- `status` - Accepts a list of recommendation statuses. Valid values:
- `active` - The recommendations which are ready for you to apply.
- `pending` - The applied or scheduled recommendations which are in progress.
- `resolved` - The recommendations which are completed.
- `dismissed` - The recommendations that you dismissed.

The results list only includes the recommendations whose status is one of the specified filter values.

- `severity` - Accepts a list of recommendation severities. The results list only includes the recommendations whose severity is one of the specified filter values. Valid values:
- `high`
- `medium`
- `low`
- `informational`
- `type-id` - Accepts a list of recommendation type identifiers. The results list only includes the recommendations whose type is one of the specified filter values.
- `dbi-resource-id` - Accepts a list of database resource identifiers. The results list only includes the recommendations that generated for the specified databases.
- `cluster-resource-id` - Accepts a list of cluster resource identifiers. The results list only includes the recommendations that generated for the specified clusters.
- `pg-arn` - Accepts a list of parameter group ARNs. The results list only includes the recommendations that generated for the specified parameter groups.
- `cluster-pg-arn` - Accepts a list of cluster parameter group ARNs. The results list only includes the recommendations that generated for the specified cluster parameter groups.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.

### Note

Currently, wildcards are not supported in filters.

The following actions can be filtered:

- `DescribeDBClusterBacktracks`
- `DescribeDBClusterEndpoints`
- `DescribeDBClusters`
- `DescribeDBInstances`
- `DescribeDBRecommendations`
- `DescribeDBShardGroups`
- `DescribePendingMaintenanceActions`

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

One or more filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To list all DB recommendations**

The following `describe-db-recommendations` example lists all DB recommendations in your AWS account.

```
aws rds describe-db-recommendations
```

Output:

```
{
    "DBRecommendations": [
        {
            "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm",
            "TypeId": "config_recommendation::old_minor_version",
            "Severity": "informational",
            "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1",
            "Status": "active",
            "CreatedTime": "2024-02-21T23:14:19.292000+00:00",
            "UpdatedTime": "2024-02-21T23:14:19+00:00",
            "Detection": "**[resource-name]** is not running the latest minor DB engine version",
            "Recommendation": "Upgrade to latest engine version",
            "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.",
            "RecommendedActions": [
                {
                    "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678",
                    "Operation": "modifyDbInstance",
                    "Parameters": [
                        {
                            "Key": "EngineVersion",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "DBInstanceIdentifier",
                            "Value": "database-1"
                        }
                    ],
                    "ApplyModes": [
                        "immediately",
                        "next-maintenance-window"
                    ],
                    "Status": "ready",
                    "ContextAttributes": [
                        {
                            "Key": "Recommended value",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "Current engine version",
                            "Value": "5.7.42"
                        }
                    ]
                }
            ],
            "Category": "security",
            "Source": "RDS",
            "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version",
            "TypeRecommendation": "Upgrade to latest engine version",
            "Impact": "Reduced database performance and data security at risk",
            "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.",
            "Links": [
                {
                    "Text": "Upgrading an RDS DB instance engine version",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html"
                }
            ]
        }
    ]
}
```

For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html) in the *Amazon RDS User Guide* and [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html) in the *Amazon Aurora User Guide*.

**Example 2: To list high severity DB recommendations**

The following `describe-db-recommendations` example lists high severity DB recommendations in your AWS account.

```
aws rds describe-db-recommendations \
    --filters Name=severity,Values=high
```

Output:

```
{
    "DBRecommendations": [
        {
            "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm",
            "TypeId": "config_recommendation::rds_extended_support",
            "Severity": "high",
            "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1",
            "Status": "active",
            "CreatedTime": "2024-02-21T23:14:19.392000+00:00",
            "UpdatedTime": "2024-02-21T23:14:19+00:00",
            "Detection": "Your databases will be auto-enrolled to RDS Extended Support on February 29",
            "Recommendation": "Upgrade your major version before February 29, 2024 to avoid additional charges",
            "Description": "Your PostgreSQL 11 and MySQL 5.7 databases will be automatically enrolled into RDS Extended Support on February 29, 2024. To avoid the increase in charges due to RDS Extended Support, we recommend upgrading your databases to a newer major engine version before February 29, 2024.\nTo learn more about the RDS Extended Support pricing, refer to the pricing page.",
            "RecommendedActions": [
                {
                    "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678",
                    "Parameters": [],
                    "ApplyModes": [
                        "manual"
                    ],
                    "Status": "ready",
                    "ContextAttributes": []
                }
            ],
            "Category": "cost optimization",
            "Source": "RDS",
            "TypeDetection": "Your database will be auto-enrolled to RDS Extended Support on February 29",
            "TypeRecommendation": "Upgrade your major version before February 29, 2024 to avoid additional charges",
            "Impact": "Increase in charges due to RDS Extended Support",
            "AdditionalInfo": "With Amazon RDS Extended Support, you can continue running your database on a major engine version past the RDS end of standard support date for an additional cost. This paid feature gives you more time to upgrade to a supported major engine version.\nDuring Extended Support, Amazon RDS will supply critical CVE patches and bug fixes.",
            "Links": [
                {
                    "Text": "Amazon RDS Extended Support pricing for RDS for MySQL",
                    "Url": "https://aws.amazon.com/rds/mysql/pricing/"
                },
                {
                    "Text": "Amazon RDS Extended Support for RDS for MySQL and PostgreSQL databases",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html"
                },
                {
                    "Text": "Amazon RDS Extended Support pricing for Amazon Aurora PostgreSQL",
                    "Url": "https://aws.amazon.com/rds/aurora/pricing/"
                },
                {
                    "Text": "Amazon RDS Extended Support for Aurora PostgreSQL databases",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html"
                },
                {
                    "Text": "Amazon RDS Extended Support pricing for RDS for PostgreSQL",
                    "Url": "https://aws.amazon.com/rds/postgresql/pricing/"
                }
            ]
        }
    ]
}
```

For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html) in the *Amazon RDS User Guide* and [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html) in the *Amazon Aurora User Guide*.

**Example 3: To list DB recommendations for a specified DB instance**

The following `describe-db-recommendations` example lists all DB recommendations for a specified DB instance.

```
aws rds describe-db-recommendations \
    --filters Name=dbi-resource-id,Values=database-1
```

Output:

```
{
    "DBRecommendations": [
        {
            "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm",
            "TypeId": "config_recommendation::old_minor_version",
            "Severity": "informational",
            "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1",
            "Status": "active",
            "CreatedTime": "2024-02-21T23:14:19.292000+00:00",
            "UpdatedTime": "2024-02-21T23:14:19+00:00",
            "Detection": "**[resource-name]** is not running the latest minor DB engine version",
            "Recommendation": "Upgrade to latest engine version",
            "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.",
            "RecommendedActions": [
                {
                    "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678",
                    "Operation": "modifyDbInstance",
                    "Parameters": [
                        {
                            "Key": "EngineVersion",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "DBInstanceIdentifier",
                            "Value": "database-1"
                        }
                    ],
                    "ApplyModes": [
                        "immediately",
                        "next-maintenance-window"
                    ],
                    "Status": "ready",
                    "ContextAttributes": [
                        {
                            "Key": "Recommended value",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "Current engine version",
                            "Value": "5.7.42"
                        }
                    ]
                }
            ],
            "Category": "security",
            "Source": "RDS",
            "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version",
            "TypeRecommendation": "Upgrade to latest engine version",
            "Impact": "Reduced database performance and data security at risk",
            "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.",
            "Links": [
                {
                    "Text": "Upgrading an RDS DB instance engine version",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html"
                }
            ]
        }
    ]
}
```

For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html) in the *Amazon RDS User Guide* and [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html) in the *Amazon Aurora User Guide*.

**Example 4: To list all active DB recommendations**

The following `describe-db-recommendations` example lists all active DB recommendations in your AWS account.

```
aws rds describe-db-recommendations \
    --filters Name=status,Values=active
```

Output:

```
{
    "DBRecommendations": [
        {
            "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm",
            "TypeId": "config_recommendation::old_minor_version",
            "Severity": "informational",
            "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1",
            "Status": "active",
            "CreatedTime": "2024-02-21T23:14:19.292000+00:00",
            "UpdatedTime": "2024-02-21T23:14:19+00:00",
            "Detection": "**[resource-name]** is not running the latest minor DB engine version",
            "Recommendation": "Upgrade to latest engine version",
            "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.",
            "RecommendedActions": [
                {
                    "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678",
                    "Operation": "modifyDbInstance",
                    "Parameters": [
                        {
                            "Key": "EngineVersion",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "DBInstanceIdentifier",
                            "Value": "database-1"
                        }
                    ],
                    "ApplyModes": [
                        "immediately",
                        "next-maintenance-window"
                    ],
                    "Status": "ready",
                    "ContextAttributes": [
                        {
                            "Key": "Recommended value",
                            "Value": "5.7.44"
                        },
                        {
                            "Key": "Current engine version",
                            "Value": "5.7.42"
                        }
                    ]
                }
            ],
            "Category": "security",
            "Source": "RDS",
            "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version",
            "TypeRecommendation": "Upgrade to latest engine version",
            "Impact": "Reduced database performance and data security at risk",
            "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.",
            "Links": [
                {
                    "Text": "Upgrading an RDS DB instance engine version",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html"
                },
                {
                    "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS",
                    "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html"
                }
            ]
        }
    ]
}
```

For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html) in the *Amazon RDS User Guide* and [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html) in the *Amazon Aurora User Guide*.

## Output

DBRecommendations -> (list)

A list of recommendations which is returned from `DescribeDBRecommendations` API request.

(structure)

The recommendation for your DB instances, DB clusters, and DB parameter groups.

RecommendationId -> (string)

The unique identifier of the recommendation.

TypeId -> (string)

A value that indicates the type of recommendation. This value determines how the description is rendered.

Severity -> (string)

The severity level of the recommendation. The severity level can help you decide the urgency with which to address the recommendation.

Valid values:

- `high`
- `medium`
- `low`
- `informational`

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the RDS resource associated with the recommendation.

Status -> (string)

The current status of the recommendation.

Valid values:

- `active` - The recommendations which are ready for you to apply.
- `pending` - The applied or scheduled recommendations which are in progress.
- `resolved` - The recommendations which are completed.
- `dismissed` - The recommendations that you dismissed.

CreatedTime -> (timestamp)

The time when the recommendation was created. For example, `2023-09-28T01:13:53.931000+00:00` .

UpdatedTime -> (timestamp)

The time when the recommendation was last updated.

Detection -> (string)

A short description of the issue identified for this recommendation. The description might contain markdown.

Recommendation -> (string)

A short description of the recommendation to resolve an issue. The description might contain markdown.

Description -> (string)

A detailed description of the recommendation. The description might contain markdown.

Reason -> (string)

The reason why this recommendation was created. The information might contain markdown.

RecommendedActions -> (list)

A list of recommended actions.

(structure)

The recommended actions to apply to resolve the issues associated with your DB instances, DB clusters, and DB parameter groups.

ActionId -> (string)

The unique identifier of the recommended action.

Title -> (string)

A short description to summarize the action. The description might contain markdown.

Description -> (string)

A detailed description of the action. The description might contain markdown.

Operation -> (string)

An API operation for the action.

Parameters -> (list)

The parameters for the API operation.

(structure)

A single parameter to use with the `RecommendedAction` API operation to apply the action.

Key -> (string)

The key of the parameter to use with the `RecommendedAction` API operation.

Value -> (string)

The value of the parameter to use with the `RecommendedAction` API operation.

ApplyModes -> (list)

The methods to apply the recommended action.

Valid values:

- `manual` - The action requires you to resolve the recommendation manually.
- `immediately` - The action is applied immediately.
- `next-maintainance-window` - The action is applied during the next scheduled maintainance.

(string)

Status -> (string)

The status of the action.

- `ready`
- `applied`
- `scheduled`
- `resolved`

IssueDetails -> (structure)

The details of the issue.

PerformanceIssueDetails -> (structure)

A detailed description of the issue when the recommendation category is `performance` .

StartTime -> (timestamp)

The time when the performance issue started.

EndTime -> (timestamp)

The time when the performance issue stopped.

Metrics -> (list)

The metrics that are relevant to the performance issue.

(structure)

The representation of a metric.

Name -> (string)

The name of a metric.

References -> (list)

A list of metric references (thresholds).

(structure)

The reference (threshold) for a metric.

Name -> (string)

The name of the metric reference.

ReferenceDetails -> (structure)

The details of a performance issue.

ScalarReferenceDetails -> (structure)

The metric reference details when the reference is a scalar.

Value -> (double)

The value of a scalar reference.

StatisticsDetails -> (string)

The details of different statistics for a metric. The description might contain markdown.

MetricQuery -> (structure)

The query to retrieve metric data points.

PerformanceInsightsMetricQuery -> (structure)

The Performance Insights query that you can use to retrieve Performance Insights metric data points.

GroupBy -> (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this list isnât included, then all of the dimensions in the group were requested, or are present in the response.

(string)

Group -> (string)

The available dimension groups for Performance Insights metric type.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid Values:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

Analysis -> (string)

The analysis of the performance issue. The information might contain markdown.

ContextAttributes -> (list)

The supporting attributes to explain the recommended action.

(structure)

The additional attributes of `RecommendedAction` data type.

Key -> (string)

The key of `ContextAttribute` .

Value -> (string)

The value of `ContextAttribute` .

Category -> (string)

The category of the recommendation.

Valid values:

- `performance efficiency`
- `security`
- `reliability`
- `cost optimization`
- `operational excellence`
- `sustainability`

Source -> (string)

The Amazon Web Services service that generated the recommendations.

TypeDetection -> (string)

A short description of the recommendation type. The description might contain markdown.

TypeRecommendation -> (string)

A short description that summarizes the recommendation to fix all the issues of the recommendation type. The description might contain markdown.

Impact -> (string)

A short description that explains the possible impact of an issue.

AdditionalInfo -> (string)

Additional information about the recommendation. The information might contain markdown.

Links -> (list)

A link to documentation that provides additional information about the recommendation.

(structure)

A link to documentation that provides additional information for a recommendation.

Text -> (string)

The text with the link to documentation for the recommendation.

Url -> (string)

The URL for the documentation for the recommendation.

IssueDetails -> (structure)

Details of the issue that caused the recommendation.

PerformanceIssueDetails -> (structure)

A detailed description of the issue when the recommendation category is `performance` .

StartTime -> (timestamp)

The time when the performance issue started.

EndTime -> (timestamp)

The time when the performance issue stopped.

Metrics -> (list)

The metrics that are relevant to the performance issue.

(structure)

The representation of a metric.

Name -> (string)

The name of a metric.

References -> (list)

A list of metric references (thresholds).

(structure)

The reference (threshold) for a metric.

Name -> (string)

The name of the metric reference.

ReferenceDetails -> (structure)

The details of a performance issue.

ScalarReferenceDetails -> (structure)

The metric reference details when the reference is a scalar.

Value -> (double)

The value of a scalar reference.

StatisticsDetails -> (string)

The details of different statistics for a metric. The description might contain markdown.

MetricQuery -> (structure)

The query to retrieve metric data points.

PerformanceInsightsMetricQuery -> (structure)

The Performance Insights query that you can use to retrieve Performance Insights metric data points.

GroupBy -> (structure)

A specification for how to aggregate the data points from a query result. You must specify a valid dimension group. Performance Insights will return all of the dimensions within that group, unless you provide the names of specific dimensions within that group. You can also request that Performance Insights return a limited number of values for a dimension.

Dimensions -> (list)

A list of specific dimensions from a dimension group. If this list isnât included, then all of the dimensions in the group were requested, or are present in the response.

(string)

Group -> (string)

The available dimension groups for Performance Insights metric type.

Limit -> (integer)

The maximum number of items to fetch for this dimension group.

Metric -> (string)

The name of a Performance Insights metric to be measured.

Valid Values:

- `db.load.avg` - A scaled representation of the number of active sessions for the database engine.
- `db.sampledload.avg` - The raw number of active sessions for the database engine.
- The counter metrics listed in [Performance Insights operating system counters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.OS) in the *Amazon Aurora User Guide* .

If the number of active sessions is less than an internal Performance Insights threshold, `db.load.avg` and `db.sampledload.avg` are the same value. If the number of active sessions is greater than the internal threshold, Performance Insights samples the active sessions, with `db.load.avg` showing the scaled values, `db.sampledload.avg` showing the raw values, and `db.sampledload.avg` less than `db.load.avg` . For most use cases, you can query `db.load.avg` only.

Analysis -> (string)

The analysis of the performance issue. The information might contain markdown.

Marker -> (string)

An optional pagination token provided by a previous `DBRecommendationsMessage` request. This token can be used later in a `DescribeDBRecomendations` request.