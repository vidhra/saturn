# get-schema-analysis-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-schema-analysis-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-schema-analysis-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# get-schema-analysis-rule

## Description

Retrieves a schema analysis rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/GetSchemaAnalysisRule)

## Synopsis

```
get-schema-analysis-rule
--collaboration-identifier <value>
--name <value>
--type <value>
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

`--collaboration-identifier` (string)

A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.

`--name` (string)

The name of the schema to retrieve the analysis rule for.

`--type` (string)

The type of the schema analysis rule to retrieve. Schema analysis rules are uniquely identified by a combination of the collaboration, the schema name, and their type.

Possible values:

- `AGGREGATION`
- `LIST`
- `CUSTOM`
- `ID_MAPPING_TABLE`

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

A specification about how data from the configured table can be used.

collaborationId -> (string)

The unique ID for the associated collaboration.

type -> (string)

The type of analysis rule.

name -> (string)

The name for the analysis rule.

createTime -> (timestamp)

The time the analysis rule was created.

updateTime -> (timestamp)

The time the analysis rule was last updated.

policy -> (tagged union structure)

A policy that describes the associated data usage limitations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

Controls on the query specifications that can be run on configured table.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`, `idMappingTable`.

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

Analysis rule type that enables custom SQL queries on a configured table.

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

idMappingTable -> (structure)

The ID mapping table.

joinColumns -> (list)

The columns that query runners are allowed to use in an INNER JOIN statement.

(string)

queryConstraints -> (list)

The query constraints of the analysis rule ID mapping table.

(tagged union structure)

Provides any necessary query constraint information.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `requireOverlap`.

requireOverlap -> (structure)

An array of column names that specifies which columns are required in the JOIN statement.

columns -> (list)

The columns that are required to overlap.

(string)

dimensionColumns -> (list)

The columns that query runners are allowed to select, group by, or filter by.

(string)

collaborationPolicy -> (tagged union structure)

Controls on the query specifications that can be run on an associated configured table.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

The policy for the configured table association analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

Analysis rule type that enables only list queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

aggregation -> (structure)

Analysis rule type that enables only aggregation queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

The `allowedAdditionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList` ) and the custom analysis rule (`AnalysisRuleCustom` ).

(string)

custom -> (structure)

Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

consolidatedPolicy -> (tagged union structure)

The consolidated policy for the analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

The consolidated policy version 1.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

The list of consolidated policies.

joinColumns -> (list)

The columns to join on.

(string)

allowedJoinOperators -> (list)

The allowed join operators in the consolidated policy list.

(string)

listColumns -> (list)

The columns in the consolidated policy list.

(string)

additionalAnalyses -> (string)

Additional analyses for the consolidated policy list.

allowedResultReceivers -> (list)

The allowed result receivers.

(string)

allowedAdditionalAnalyses -> (list)

The additional analyses allowed by the consolidated policy list.

(string)

aggregation -> (structure)

The aggregation setting for the consolidated policy.

aggregateColumns -> (list)

Aggregate columns in consolidated policy aggregation.

(structure)

Column in configured table that can be used in aggregate function in query.

columnNames -> (list)

Column names in configured table of aggregate columns.

(string)

function -> (string)

Aggregation function that can be applied to aggregate column in query.

joinColumns -> (list)

The columns to join on.

(string)

joinRequired -> (string)

Join required

allowedJoinOperators -> (list)

The allowed join operators.

(string)

dimensionColumns -> (list)

The dimension columns of the consolidated policy aggregation.

(string)

scalarFunctions -> (list)

The scalar functions.

(string)

outputConstraints -> (list)

The output constraints of the consolidated policy aggregation.

(structure)

Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

columnName -> (string)

Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.

minimum -> (integer)

The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.

type -> (string)

The type of aggregation the constraint allows. The only valid value is currently COUNT_DISTINCT.

additionalAnalyses -> (string)

Additional analyses for the consolidated policy aggregation.

allowedResultReceivers -> (list)

The allowed result receivers.

(string)

allowedAdditionalAnalyses -> (list)

The additional analyses allowed by the consolidated policy aggregation.

(string)

custom -> (structure)

Custom policy

allowedAnalyses -> (list)

The allowed analyses.

(string)

allowedAnalysisProviders -> (list)

The allowed analysis providers.

(string)

additionalAnalyses -> (string)

Additional analyses for the consolidated policy.

disallowedOutputColumns -> (list)

Disallowed output columns

(string)

differentialPrivacy -> (structure)

Specifies the unique identifier for your users.

columns -> (list)

The name of the column (such as user_id) that contains the unique identifier of your users whose privacy you want to protect. If you want to turn on diï¬erential privacy for two or more tables in a collaboration, you must conï¬gure the same column as the user identiï¬er column in both analysis rules.

(structure)

Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

name -> (string)

The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

allowedResultReceivers -> (list)

The allowed result receivers.

(string)

allowedAdditionalAnalyses -> (list)

The additional analyses allowed by the consolidated policy.

(string)