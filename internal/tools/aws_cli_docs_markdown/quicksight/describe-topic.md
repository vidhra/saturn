# describe-topicÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-topic.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-topic.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# describe-topic

## Description

Describes a topic.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeTopic)

## Synopsis

```
describe-topic
--aws-account-id <value>
--topic-id <value>
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

`--aws-account-id` (string)

The Amazon Web Services account ID.

`--topic-id` (string)

The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

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

Arn -> (string)

The Amazon Resource Name (ARN) of the topic.

TopicId -> (string)

The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

Topic -> (structure)

The definition of a topic.

Name -> (string)

The name of the topic.

Description -> (string)

The description of the topic.

UserExperienceVersion -> (string)

The user experience version of a topic.

DataSets -> (list)

The data sets that the topic is associated with.

(structure)

A structure that represents a dataset.

DatasetArn -> (string)

The Amazon Resource Name (ARN) of the dataset.

DatasetName -> (string)

The name of the dataset.

DatasetDescription -> (string)

The description of the dataset.

DataAggregation -> (structure)

The definition of a data aggregation.

DatasetRowDateGranularity -> (string)

The level of time precision that is used to aggregate `DateTime` values.

DefaultDateColumnName -> (string)

The column name for the default date.

Filters -> (list)

The list of filter definitions.

(structure)

A structure that represents a filter used to select items for a topic.

FilterDescription -> (string)

A description of the filter used to select items for a topic.

FilterClass -> (string)

The class of the filter. Valid values for this structure are `ENFORCED_VALUE_FILTER` , `CONDITIONAL_VALUE_FILTER` , and `NAMED_VALUE_FILTER` .

FilterName -> (string)

The name of the filter.

FilterSynonyms -> (list)

The other names or aliases for the filter.

(string)

OperandFieldName -> (string)

The name of the field that the filter operates on.

FilterType -> (string)

The type of the filter. Valid values for this structure are `CATEGORY_FILTER` , `NUMERIC_EQUALITY_FILTER` , `NUMERIC_RANGE_FILTER` , `DATE_RANGE_FILTER` , and `RELATIVE_DATE_FILTER` .

CategoryFilter -> (structure)

The category filter that is associated with this filter.

CategoryFilterFunction -> (string)

The category filter function. Valid values for this structure are `EXACT` and `CONTAINS` .

CategoryFilterType -> (string)

The category filter type. This element is used to specify whether a filter is a simple category filter or an inverse category filter.

Constant -> (structure)

The constant used in a category filter.

ConstantType -> (string)

The type of category filter constant. This element is used to specify whether a constant is a singular or collective. Valid values are `SINGULAR` and `COLLECTIVE` .

SingularConstant -> (string)

A singular constant used in a category filter. This element is used to specify a single value for the constant.

CollectiveConstant -> (structure)

A collective constant used in a category filter. This element is used to specify a list of values for the constant.

ValueList -> (list)

A list of values for the collective constant.

(string)

Inverse -> (boolean)

A Boolean value that indicates if the filter is inverse.

NumericEqualityFilter -> (structure)

The numeric equality filter.

Constant -> (structure)

The constant used in a numeric equality filter.

ConstantType -> (string)

The type of the singular filter constant. Valid values for this structure are `SINGULAR` .

SingularConstant -> (string)

The value of the singular filter constant.

Aggregation -> (string)

An aggregation function that specifies how to calculate the value of a numeric field for a topic. Valid values for this structure are `NO_AGGREGATION` , `SUM` , `AVERAGE` , `COUNT` , `DISTINCT_COUNT` , `MAX` , `MEDIAN` , `MIN` , `STDEV` , `STDEVP` , `VAR` , and `VARP` .

NumericRangeFilter -> (structure)

The numeric range filter.

Inclusive -> (boolean)

A Boolean value that indicates whether the endpoints of the numeric range are included in the filter. If set to true, topics whose numeric field value is equal to the endpoint values will be included in the filter. If set to false, topics whose numeric field value is equal to the endpoint values will be excluded from the filter.

Constant -> (structure)

The constant used in a numeric range filter.

ConstantType -> (string)

The data type of the constant value that is used in a range filter. Valid values for this structure are `RANGE` .

RangeConstant -> (structure)

The value of the constant that is used to specify the endpoints of a range filter.

Minimum -> (string)

The minimum value for a range constant.

Maximum -> (string)

The maximum value for a range constant.

Aggregation -> (string)

An aggregation function that specifies how to calculate the value of a numeric field for a topic, Valid values for this structure are `NO_AGGREGATION` , `SUM` , `AVERAGE` , `COUNT` , `DISTINCT_COUNT` , `MAX` , `MEDIAN` , `MIN` , `STDEV` , `STDEVP` , `VAR` , and `VARP` .

DateRangeFilter -> (structure)

The date range filter.

Inclusive -> (boolean)

A Boolean value that indicates whether the date range filter should include the boundary values. If set to true, the filter includes the start and end dates. If set to false, the filter excludes them.

Constant -> (structure)

The constant used in a date range filter.

ConstantType -> (string)

The data type of the constant value that is used in a range filter. Valid values for this structure are `RANGE` .

RangeConstant -> (structure)

The value of the constant that is used to specify the endpoints of a range filter.

Minimum -> (string)

The minimum value for a range constant.

Maximum -> (string)

The maximum value for a range constant.

RelativeDateFilter -> (structure)

The relative date filter.

TimeGranularity -> (string)

The level of time precision that is used to aggregate `DateTime` values.

RelativeDateFilterFunction -> (string)

The function to be used in a relative date filter to determine the range of dates to include in the results. Valid values for this structure are `BEFORE` , `AFTER` , and `BETWEEN` .

Constant -> (structure)

The constant used in a relative date filter.

ConstantType -> (string)

The type of the singular filter constant. Valid values for this structure are `SINGULAR` .

SingularConstant -> (string)

The value of the singular filter constant.

Columns -> (list)

The list of column definitions.

(structure)

Represents a column in a dataset.

ColumnName -> (string)

The name of the column.

ColumnFriendlyName -> (string)

A user-friendly name for the column.

ColumnDescription -> (string)

A description of the column and its contents.

ColumnSynonyms -> (list)

The other names or aliases for the column.

(string)

ColumnDataRole -> (string)

The role of the column in the data. Valid values are `DIMENSION` and `MEASURE` .

Aggregation -> (string)

The type of aggregation that is performed on the column data when itâs queried.

IsIncludedInTopic -> (boolean)

A Boolean value that indicates whether the column is included in the query results.

DisableIndexing -> (boolean)

A Boolean value that indicates whether the column shows in the autocomplete functionality.

ComparativeOrder -> (structure)

The order in which data is displayed for the column when itâs used in a comparative context.

UseOrdering -> (string)

The ordering type for a column. Valid values for this structure are `GREATER_IS_BETTER` , `LESSER_IS_BETTER` and `SPECIFIED` .

SpecifedOrder -> (list)

The list of columns to be used in the ordering.

(string)

TreatUndefinedSpecifiedValues -> (string)

The treat of undefined specified values. Valid values for this structure are `LEAST` and `MOST` .

SemanticType -> (structure)

The semantic type of data contained in the column.

TypeName -> (string)

The semantic type name.

SubTypeName -> (string)

The semantic type sub type name.

TypeParameters -> (map)

The semantic type parameters.

key -> (string)

value -> (string)

TruthyCellValue -> (string)

The semantic type truthy cell value.

TruthyCellValueSynonyms -> (list)

The other names or aliases for the true cell value.

(string)

FalseyCellValue -> (string)

The semantic type falsey cell value.

FalseyCellValueSynonyms -> (list)

The other names or aliases for the false cell value.

(string)

TimeGranularity -> (string)

The level of time precision that is used to aggregate `DateTime` values.

AllowedAggregations -> (list)

The list of aggregation types that are allowed for the column. Valid values for this structure are `COUNT` , `DISTINCT_COUNT` , `MIN` , `MAX` , `MEDIAN` , `SUM` , `AVERAGE` , `STDEV` , `STDEVP` , `VAR` , `VARP` , and `PERCENTILE` .

(string)

NotAllowedAggregations -> (list)

The list of aggregation types that are not allowed for the column. Valid values for this structure are `COUNT` , `DISTINCT_COUNT` , `MIN` , `MAX` , `MEDIAN` , `SUM` , `AVERAGE` , `STDEV` , `STDEVP` , `VAR` , `VARP` , and `PERCENTILE` .

(string)

DefaultFormatting -> (structure)

The default formatting used for values in the column.

DisplayFormat -> (string)

The display format. Valid values for this structure are `AUTO` , `PERCENT` , `CURRENCY` , `NUMBER` , `DATE` , and `STRING` .

DisplayFormatOptions -> (structure)

The additional options for display formatting.

UseBlankCellFormat -> (boolean)

A Boolean value that indicates whether to use blank cell format.

BlankCellFormat -> (string)

Determines the blank cell format.

DateFormat -> (string)

Determines the `DateTime` format.

DecimalSeparator -> (string)

Determines the decimal separator.

GroupingSeparator -> (string)

Determines the grouping separator.

UseGrouping -> (boolean)

A Boolean value that indicates whether to use grouping.

FractionDigits -> (integer)

Determines the number of fraction digits.

Prefix -> (string)

The prefix value for a display format.

Suffix -> (string)

The suffix value for a display format.

UnitScaler -> (string)

The unit scaler. Valid values for this structure are: `NONE` , `AUTO` , `THOUSANDS` , `MILLIONS` , `BILLIONS` , and `TRILLIONS` .

NegativeFormat -> (structure)

The negative format.

Prefix -> (string)

The prefix for a negative format.

Suffix -> (string)

The suffix for a negative format.

CurrencySymbol -> (string)

The currency symbol, such as `USD` .

NeverAggregateInFilter -> (boolean)

A Boolean value that indicates whether to aggregate the column data when itâs used in a filter context.

CellValueSynonyms -> (list)

The other names or aliases for the column cell value.

(structure)

A structure that represents the cell value synonym.

CellValue -> (string)

The cell value.

Synonyms -> (list)

Other names or aliases for the cell value.

(string)

NonAdditive -> (boolean)

The non additive value for the column.

CalculatedFields -> (list)

The list of calculated field definitions.

(structure)

A structure that represents a calculated field.

CalculatedFieldName -> (string)

The calculated field name.

CalculatedFieldDescription -> (string)

The calculated field description.

Expression -> (string)

The calculated field expression.

CalculatedFieldSynonyms -> (list)

The other names or aliases for the calculated field.

(string)

IsIncludedInTopic -> (boolean)

A boolean value that indicates if a calculated field is included in the topic.

DisableIndexing -> (boolean)

A Boolean value that indicates if a calculated field is visible in the autocomplete.

ColumnDataRole -> (string)

The column data role for a calculated field. Valid values for this structure are `DIMENSION` and `MEASURE` .

TimeGranularity -> (string)

The level of time precision that is used to aggregate `DateTime` values.

DefaultFormatting -> (structure)

The default formatting definition.

DisplayFormat -> (string)

The display format. Valid values for this structure are `AUTO` , `PERCENT` , `CURRENCY` , `NUMBER` , `DATE` , and `STRING` .

DisplayFormatOptions -> (structure)

The additional options for display formatting.

UseBlankCellFormat -> (boolean)

A Boolean value that indicates whether to use blank cell format.

BlankCellFormat -> (string)

Determines the blank cell format.

DateFormat -> (string)

Determines the `DateTime` format.

DecimalSeparator -> (string)

Determines the decimal separator.

GroupingSeparator -> (string)

Determines the grouping separator.

UseGrouping -> (boolean)

A Boolean value that indicates whether to use grouping.

FractionDigits -> (integer)

Determines the number of fraction digits.

Prefix -> (string)

The prefix value for a display format.

Suffix -> (string)

The suffix value for a display format.

UnitScaler -> (string)

The unit scaler. Valid values for this structure are: `NONE` , `AUTO` , `THOUSANDS` , `MILLIONS` , `BILLIONS` , and `TRILLIONS` .

NegativeFormat -> (structure)

The negative format.

Prefix -> (string)

The prefix for a negative format.

Suffix -> (string)

The suffix for a negative format.

CurrencySymbol -> (string)

The currency symbol, such as `USD` .

Aggregation -> (string)

The default aggregation. Valid values for this structure are `SUM` , `MAX` , `MIN` , `COUNT` , `DISTINCT_COUNT` , and `AVERAGE` .

ComparativeOrder -> (structure)

The order in which data is displayed for the calculated field when itâs used in a comparative context.

UseOrdering -> (string)

The ordering type for a column. Valid values for this structure are `GREATER_IS_BETTER` , `LESSER_IS_BETTER` and `SPECIFIED` .

SpecifedOrder -> (list)

The list of columns to be used in the ordering.

(string)

TreatUndefinedSpecifiedValues -> (string)

The treat of undefined specified values. Valid values for this structure are `LEAST` and `MOST` .

SemanticType -> (structure)

The semantic type.

TypeName -> (string)

The semantic type name.

SubTypeName -> (string)

The semantic type sub type name.

TypeParameters -> (map)

The semantic type parameters.

key -> (string)

value -> (string)

TruthyCellValue -> (string)

The semantic type truthy cell value.

TruthyCellValueSynonyms -> (list)

The other names or aliases for the true cell value.

(string)

FalseyCellValue -> (string)

The semantic type falsey cell value.

FalseyCellValueSynonyms -> (list)

The other names or aliases for the false cell value.

(string)

AllowedAggregations -> (list)

The list of aggregation types that are allowed for the calculated field. Valid values for this structure are `COUNT` , `DISTINCT_COUNT` , `MIN` , `MAX` , `MEDIAN` , `SUM` , `AVERAGE` , `STDEV` , `STDEVP` , `VAR` , `VARP` , and `PERCENTILE` .

(string)

NotAllowedAggregations -> (list)

The list of aggregation types that are not allowed for the calculated field. Valid values for this structure are `COUNT` , `DISTINCT_COUNT` , `MIN` , `MAX` , `MEDIAN` , `SUM` , `AVERAGE` , `STDEV` , `STDEVP` , `VAR` , `VARP` , and `PERCENTILE` .

(string)

NeverAggregateInFilter -> (boolean)

A Boolean value that indicates whether to never aggregate calculated field in filters.

CellValueSynonyms -> (list)

The other names or aliases for the calculated field cell value.

(structure)

A structure that represents the cell value synonym.

CellValue -> (string)

The cell value.

Synonyms -> (list)

Other names or aliases for the cell value.

(string)

NonAdditive -> (boolean)

The non additive for the table style target.

NamedEntities -> (list)

The list of named entities definitions.

(structure)

A structure that represents a named entity.

EntityName -> (string)

The name of the named entity.

EntityDescription -> (string)

The description of the named entity.

EntitySynonyms -> (list)

The other names or aliases for the named entity.

(string)

SemanticEntityType -> (structure)

The type of named entity that a topic represents.

TypeName -> (string)

The semantic entity type name.

SubTypeName -> (string)

The semantic entity sub type name.

TypeParameters -> (map)

The semantic entity type parameters.

key -> (string)

value -> (string)

Definition -> (list)

The definition of a named entity.

(structure)

A structure that represents a named entity.

FieldName -> (string)

The name of the entity.

PropertyName -> (string)

The property name to be used for the named entity.

PropertyRole -> (string)

The property role. Valid values for this structure are `PRIMARY` and `ID` .

PropertyUsage -> (string)

The property usage. Valid values for this structure are `INHERIT` , `DIMENSION` , and `MEASURE` .

Metric -> (structure)

The definition of a metric.

Aggregation -> (string)

The aggregation of a named entity. Valid values for this structure are `SUM` , `MIN` , `MAX` , `COUNT` , `AVERAGE` , `DISTINCT_COUNT` , `STDEV` , `STDEVP` , `VAR` , `VARP` , `PERCENTILE` , `MEDIAN` , and `CUSTOM` .

AggregationFunctionParameters -> (map)

The additional parameters for an aggregation function.

key -> (string)

value -> (string)

ConfigOptions -> (structure)

Configuration options for a `Topic` .

QBusinessInsightsEnabled -> (boolean)

Enables Amazon Q Business Insights for a `Topic` .

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.