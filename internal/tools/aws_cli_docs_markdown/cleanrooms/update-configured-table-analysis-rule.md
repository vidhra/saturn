# update-configured-table-analysis-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/update-configured-table-analysis-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/update-configured-table-analysis-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# update-configured-table-analysis-rule

## Description

Updates a configured table analysis rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/UpdateConfiguredTableAnalysisRule)

## Synopsis

```
update-configured-table-analysis-rule
--configured-table-identifier <value>
--analysis-rule-type <value>
--analysis-rule-policy <value>
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

`--configured-table-identifier` (string)

The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.

`--analysis-rule-type` (string)

The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.

Possible values:

- `AGGREGATION`
- `LIST`
- `CUSTOM`

`--analysis-rule-policy` (tagged union structure)

The new analysis rule policy for the configured table analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

Controls on the query specifications that can be run on a configured table.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

Analysis rule type that enables only list queries on a configured table.

joinColumns -> (list)

Columns that can be used to join a configured table with the table of the member who can query and other membersâ configured tables.

(string)

allowedJoinOperators -> (list)

The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is `AND` .

(string)

listColumns -> (list)

Columns that can be listed in the output.

(string)

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

aggregation -> (structure)

Analysis rule type that enables only aggregation queries on a configured table.

aggregateColumns -> (list)

The columns that query runners are allowed to use in aggregation queries.

(structure)

Column in configured table that can be used in aggregate function in query.

columnNames -> (list)

Column names in configured table of aggregate columns.

(string)

function -> (string)

Aggregation function that can be applied to aggregate column in query.

joinColumns -> (list)

Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.

(string)

joinRequired -> (string)

Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

allowedJoinOperators -> (list)

Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is `AND` .

(string)

dimensionColumns -> (list)

The columns that query runners are allowed to select, group by, or filter by.

(string)

scalarFunctions -> (list)

Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.

(string)

outputConstraints -> (list)

Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.

(structure)

Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

columnName -> (string)

Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.

minimum -> (integer)

The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.

type -> (string)

The type of aggregation the constraint allows. The only valid value is currently COUNT_DISTINCT.

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

The `additionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList` ) and the custom analysis rule (`AnalysisRuleCustom` ).

custom -> (structure)

A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

allowedAnalyses -> (list)

The ARN of the analysis templates that are allowed by the custom analysis rule.

(string)

allowedAnalysisProviders -> (list)

The IDs of the Amazon Web Services accounts that are allowed to query by the custom analysis rule. Required when `allowedAnalyses` is `ANY_QUERY` .

(string)

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

disallowedOutputColumns -> (list)

A list of columns that arenât allowed to be shown in the query output.

(string)

differentialPrivacy -> (structure)

The differential privacy configuration.

columns -> (list)

The name of the column (such as user_id) that contains the unique identifier of your users whose privacy you want to protect. If you want to turn on diï¬erential privacy for two or more tables in a collaboration, you must conï¬gure the same column as the user identiï¬er column in both analysis rules.

(structure)

Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

name -> (string)

The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

JSON Syntax:

```
{
  "v1": {
    "list": {
      "joinColumns": ["string", ...],
      "allowedJoinOperators": ["OR"|"AND", ...],
      "listColumns": ["string", ...],
      "additionalAnalyses": "ALLOWED"|"REQUIRED"|"NOT_ALLOWED"
    },
    "aggregation": {
      "aggregateColumns": [
        {
          "columnNames": ["string", ...],
          "function": "SUM"|"SUM_DISTINCT"|"COUNT"|"COUNT_DISTINCT"|"AVG"
        }
        ...
      ],
      "joinColumns": ["string", ...],
      "joinRequired": "QUERY_RUNNER",
      "allowedJoinOperators": ["OR"|"AND", ...],
      "dimensionColumns": ["string", ...],
      "scalarFunctions": ["ABS"|"CAST"|"CEILING"|"COALESCE"|"CONVERT"|"CURRENT_DATE"|"DATEADD"|"EXTRACT"|"FLOOR"|"GETDATE"|"LN"|"LOG"|"LOWER"|"ROUND"|"RTRIM"|"SQRT"|"SUBSTRING"|"TO_CHAR"|"TO_DATE"|"TO_NUMBER"|"TO_TIMESTAMP"|"TRIM"|"TRUNC"|"UPPER", ...],
      "outputConstraints": [
        {
          "columnName": "string",
          "minimum": integer,
          "type": "COUNT_DISTINCT"
        }
        ...
      ],
      "additionalAnalyses": "ALLOWED"|"REQUIRED"|"NOT_ALLOWED"
    },
    "custom": {
      "allowedAnalyses": ["string", ...],
      "allowedAnalysisProviders": ["string", ...],
      "additionalAnalyses": "ALLOWED"|"REQUIRED"|"NOT_ALLOWED",
      "disallowedOutputColumns": ["string", ...],
      "differentialPrivacy": {
        "columns": [
          {
            "name": "string"
          }
          ...
        ]
      }
    }
  }
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

analysisRule -> (structure)

The entire updated analysis rule.

configuredTableId -> (string)

The unique ID for the configured table.

configuredTableArn -> (string)

The unique ARN for the configured table.

policy -> (tagged union structure)

The policy that controls SQL query rules.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

Controls on the query specifications that can be run on a configured table.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

Analysis rule type that enables only list queries on a configured table.

joinColumns -> (list)

Columns that can be used to join a configured table with the table of the member who can query and other membersâ configured tables.

(string)

allowedJoinOperators -> (list)

The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is `AND` .

(string)

listColumns -> (list)

Columns that can be listed in the output.

(string)

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

aggregation -> (structure)

Analysis rule type that enables only aggregation queries on a configured table.

aggregateColumns -> (list)

The columns that query runners are allowed to use in aggregation queries.

(structure)

Column in configured table that can be used in aggregate function in query.

columnNames -> (list)

Column names in configured table of aggregate columns.

(string)

function -> (string)

Aggregation function that can be applied to aggregate column in query.

joinColumns -> (list)

Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.

(string)

joinRequired -> (string)

Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

allowedJoinOperators -> (list)

Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is `AND` .

(string)

dimensionColumns -> (list)

The columns that query runners are allowed to select, group by, or filter by.

(string)

scalarFunctions -> (list)

Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.

(string)

outputConstraints -> (list)

Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.

(structure)

Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

columnName -> (string)

Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.

minimum -> (integer)

The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.

type -> (string)

The type of aggregation the constraint allows. The only valid value is currently COUNT_DISTINCT.

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

The `additionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList` ) and the custom analysis rule (`AnalysisRuleCustom` ).

custom -> (structure)

A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

allowedAnalyses -> (list)

The ARN of the analysis templates that are allowed by the custom analysis rule.

(string)

allowedAnalysisProviders -> (list)

The IDs of the Amazon Web Services accounts that are allowed to query by the custom analysis rule. Required when `allowedAnalyses` is `ANY_QUERY` .

(string)

additionalAnalyses -> (string)

An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query.

disallowedOutputColumns -> (list)

A list of columns that arenât allowed to be shown in the query output.

(string)

differentialPrivacy -> (structure)

The differential privacy configuration.

columns -> (list)

The name of the column (such as user_id) that contains the unique identifier of your users whose privacy you want to protect. If you want to turn on diï¬erential privacy for two or more tables in a collaboration, you must conï¬gure the same column as the user identiï¬er column in both analysis rules.

(structure)

Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

name -> (string)

The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

type -> (string)

The type of configured table analysis rule.

createTime -> (timestamp)

The time the configured table analysis rule was created.

updateTime -> (timestamp)

The time the configured table analysis rule was last updated.