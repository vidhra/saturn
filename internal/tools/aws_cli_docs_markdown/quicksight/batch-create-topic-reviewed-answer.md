# batch-create-topic-reviewed-answerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/batch-create-topic-reviewed-answer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/batch-create-topic-reviewed-answer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# batch-create-topic-reviewed-answer

## Description

Creates new reviewed answers for a Q Topic.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/BatchCreateTopicReviewedAnswer)

## Synopsis

```
batch-create-topic-reviewed-answer
--aws-account-id <value>
--topic-id <value>
--answers <value>
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

The ID of the Amazon Web Services account that you want to create a reviewed answer in.

`--topic-id` (string)

The ID for the topic reviewed answer that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

`--answers` (list)

The definition of the Answers to be created.

(structure)

The definition for a `CreateTopicReviewedAnswer` .

AnswerId -> (string)

The answer ID for the `CreateTopicReviewedAnswer` .

DatasetArn -> (string)

The Dataset arn for the `CreateTopicReviewedAnswer` .

Question -> (string)

The Question to be created.

Mir -> (structure)

The Mir for the `CreateTopicReviewedAnswer` .

Metrics -> (list)

The metrics for the `TopicIR` .

(structure)

The definition for a `TopicIRMetric` .

MetricId -> (structure)

The metric ID for the `TopicIRMetric` .

Identity -> (string)

The identity of the identifier.

Function -> (structure)

The function for the `TopicIRMetric` .

Aggregation -> (string)

The aggregation of an Agg function.

AggregationFunctionParameters -> (map)

The aggregation parameters for an Agg function.

key -> (string)

value -> (string)

Period -> (string)

The period of an Agg function.

PeriodField -> (string)

The period field for an Agg function.

Operands -> (list)

The operands for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

ComparisonMethod -> (structure)

The comparison method for the `TopicIRMetric` .

Type -> (string)

The type for the `TopicIRComparisonMethod` .

Period -> (string)

The period for the `TopicIRComparisonMethod` .

WindowSize -> (integer)

The window size for the `TopicIRComparisonMethod` .

Expression -> (string)

The expression for the `TopicIRMetric` .

CalculatedFieldReferences -> (list)

The calculated field references for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

DisplayFormat -> (string)

The display format for the `TopicIRMetric` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRMetric` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

GroupByList -> (list)

The GroupBy list for the `TopicIR` .

(structure)

The definition for a `TopicIRGroupBy` .

FieldName -> (structure)

The field name for the `TopicIRGroupBy` .

Identity -> (string)

The identity of the identifier.

TimeGranularity -> (string)

The time granularity for the `TopicIRGroupBy` .

Sort -> (structure)

The sort for the `TopicIRGroupBy` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

DisplayFormat -> (string)

The display format for the `TopicIRGroupBy` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRGroupBy` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

Filters -> (list)

The filters for the `TopicIR` .

(list)

(structure)

The definition for a `TopicIRFilterOption` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Sort -> (structure)

The sort for the `TopicIR` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

ContributionAnalysis -> (structure)

The contribution analysis for the `TopicIR` .

Factors -> (list)

The factors for a `TopicIRContributionAnalysis` .

(structure)

The definition for the `ContributionAnalysisFactor` .

FieldName -> (string)

The field name of the `ContributionAnalysisFactor` .

TimeRanges -> (structure)

The time ranges for the `TopicIRContributionAnalysis` .

StartRange -> (structure)

The start range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

EndRange -> (structure)

The end range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Direction -> (string)

The direction for the `TopicIRContributionAnalysis` .

SortType -> (string)

The sort type for the `TopicIRContributionAnalysis` .

Visual -> (structure)

The visual for the `TopicIR` .

type -> (string)

The type for a `VisualOptions` .

PrimaryVisual -> (structure)

The `PrimaryVisual` for the `CreateTopicReviewedAnswer` .

VisualId -> (string)

The visual ID for the `TopicVisual` .

Role -> (string)

The role for the `TopicVisual` .

Ir -> (structure)

The ir for the `TopicVisual` .

Metrics -> (list)

The metrics for the `TopicIR` .

(structure)

The definition for a `TopicIRMetric` .

MetricId -> (structure)

The metric ID for the `TopicIRMetric` .

Identity -> (string)

The identity of the identifier.

Function -> (structure)

The function for the `TopicIRMetric` .

Aggregation -> (string)

The aggregation of an Agg function.

AggregationFunctionParameters -> (map)

The aggregation parameters for an Agg function.

key -> (string)

value -> (string)

Period -> (string)

The period of an Agg function.

PeriodField -> (string)

The period field for an Agg function.

Operands -> (list)

The operands for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

ComparisonMethod -> (structure)

The comparison method for the `TopicIRMetric` .

Type -> (string)

The type for the `TopicIRComparisonMethod` .

Period -> (string)

The period for the `TopicIRComparisonMethod` .

WindowSize -> (integer)

The window size for the `TopicIRComparisonMethod` .

Expression -> (string)

The expression for the `TopicIRMetric` .

CalculatedFieldReferences -> (list)

The calculated field references for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

DisplayFormat -> (string)

The display format for the `TopicIRMetric` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRMetric` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

GroupByList -> (list)

The GroupBy list for the `TopicIR` .

(structure)

The definition for a `TopicIRGroupBy` .

FieldName -> (structure)

The field name for the `TopicIRGroupBy` .

Identity -> (string)

The identity of the identifier.

TimeGranularity -> (string)

The time granularity for the `TopicIRGroupBy` .

Sort -> (structure)

The sort for the `TopicIRGroupBy` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

DisplayFormat -> (string)

The display format for the `TopicIRGroupBy` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRGroupBy` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

Filters -> (list)

The filters for the `TopicIR` .

(list)

(structure)

The definition for a `TopicIRFilterOption` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Sort -> (structure)

The sort for the `TopicIR` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

ContributionAnalysis -> (structure)

The contribution analysis for the `TopicIR` .

Factors -> (list)

The factors for a `TopicIRContributionAnalysis` .

(structure)

The definition for the `ContributionAnalysisFactor` .

FieldName -> (string)

The field name of the `ContributionAnalysisFactor` .

TimeRanges -> (structure)

The time ranges for the `TopicIRContributionAnalysis` .

StartRange -> (structure)

The start range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

EndRange -> (structure)

The end range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Direction -> (string)

The direction for the `TopicIRContributionAnalysis` .

SortType -> (string)

The sort type for the `TopicIRContributionAnalysis` .

Visual -> (structure)

The visual for the `TopicIR` .

type -> (string)

The type for a `VisualOptions` .

SupportingVisuals -> (list)

The supporting visuals for the `TopicVisual` .

(structure)

The definition for a `TopicVisual` .

VisualId -> (string)

The visual ID for the `TopicVisual` .

Role -> (string)

The role for the `TopicVisual` .

Ir -> (structure)

The ir for the `TopicVisual` .

Metrics -> (list)

The metrics for the `TopicIR` .

(structure)

The definition for a `TopicIRMetric` .

MetricId -> (structure)

The metric ID for the `TopicIRMetric` .

Identity -> (string)

The identity of the identifier.

Function -> (structure)

The function for the `TopicIRMetric` .

Aggregation -> (string)

The aggregation of an Agg function.

AggregationFunctionParameters -> (map)

The aggregation parameters for an Agg function.

key -> (string)

value -> (string)

Period -> (string)

The period of an Agg function.

PeriodField -> (string)

The period field for an Agg function.

Operands -> (list)

The operands for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

ComparisonMethod -> (structure)

The comparison method for the `TopicIRMetric` .

Type -> (string)

The type for the `TopicIRComparisonMethod` .

Period -> (string)

The period for the `TopicIRComparisonMethod` .

WindowSize -> (integer)

The window size for the `TopicIRComparisonMethod` .

Expression -> (string)

The expression for the `TopicIRMetric` .

CalculatedFieldReferences -> (list)

The calculated field references for the `TopicIRMetric` .

(structure)

The definition for the identifier.

Identity -> (string)

The identity of the identifier.

DisplayFormat -> (string)

The display format for the `TopicIRMetric` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRMetric` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

GroupByList -> (list)

The GroupBy list for the `TopicIR` .

(structure)

The definition for a `TopicIRGroupBy` .

FieldName -> (structure)

The field name for the `TopicIRGroupBy` .

Identity -> (string)

The identity of the identifier.

TimeGranularity -> (string)

The time granularity for the `TopicIRGroupBy` .

Sort -> (structure)

The sort for the `TopicIRGroupBy` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

DisplayFormat -> (string)

The display format for the `TopicIRGroupBy` .

DisplayFormatOptions -> (structure)

A structure that represents additional options for display formatting.

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

NamedEntity -> (structure)

The named entity for the `TopicIRGroupBy` .

NamedEntityName -> (string)

The `NamedEntityName` for the `NamedEntityRef` .

Filters -> (list)

The filters for the `TopicIR` .

(list)

(structure)

The definition for a `TopicIRFilterOption` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Sort -> (structure)

The sort for the `TopicIR` .

Operand -> (structure)

The operand for a `TopicSortClause` .

Identity -> (string)

The identity of the identifier.

SortDirection -> (string)

The sort direction for the `TopicSortClause` .

ContributionAnalysis -> (structure)

The contribution analysis for the `TopicIR` .

Factors -> (list)

The factors for a `TopicIRContributionAnalysis` .

(structure)

The definition for the `ContributionAnalysisFactor` .

FieldName -> (string)

The field name of the `ContributionAnalysisFactor` .

TimeRanges -> (structure)

The time ranges for the `TopicIRContributionAnalysis` .

StartRange -> (structure)

The start range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

EndRange -> (structure)

The end range for the `ContributionAnalysisTimeRanges` .

FilterType -> (string)

The filter type for the `TopicIRFilterOption` .

FilterClass -> (string)

The filter class for the `TopicIRFilterOption` .

OperandField -> (structure)

The operand field for the `TopicIRFilterOption` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `TopicIRFilterOption` .

Constant -> (structure)

The constant for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inverse -> (boolean)

The inverse for the `TopicIRFilterOption` .

NullFilter -> (string)

The null filter for the `TopicIRFilterOption` .

Aggregation -> (string)

The aggregation for the `TopicIRFilterOption` .

AggregationFunctionParameters -> (map)

The aggregation function parameters for the `TopicIRFilterOption` .

key -> (string)

value -> (string)

AggregationPartitionBy -> (list)

The `AggregationPartitionBy` for the `TopicIRFilterOption` .

(structure)

The definition of an `AggregationPartitionBy` .

FieldName -> (string)

The field Name for an `AggregationPartitionBy` .

TimeGranularity -> (string)

The `TimeGranularity` for an `AggregationPartitionBy` .

Range -> (structure)

The range for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

Inclusive -> (boolean)

The inclusive for the `TopicIRFilterOption` .

TimeGranularity -> (string)

The time granularity for the `TopicIRFilterOption` .

LastNextOffset -> (structure)

The last next offset for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

AggMetrics -> (list)

The agg metrics for the `TopicIRFilterOption` .

(structure)

The definition for the `FilterAggMetrics` .

MetricOperand -> (structure)

The metric operand of the `FilterAggMetrics` .

Identity -> (string)

The identity of the identifier.

Function -> (string)

The function for the `FilterAggMetrics` .

SortDirection -> (string)

The sort direction for `FilterAggMetrics` .

TopBottomLimit -> (structure)

The `TopBottomLimit` for the `TopicIRFilterOption` .

ConstantType -> (string)

The constant type of a `TopicConstantValue` .

Value -> (string)

The value of the `TopicConstantValue` .

Minimum -> (string)

The minimum for the `TopicConstantValue` .

Maximum -> (string)

The maximum for the `TopicConstantValue` .

ValueList -> (list)

The value list of the `TopicConstantValue` .

(structure)

The definition for a `CollectiveConstantEntry` .

ConstantType -> (string)

The `ConstantType` of a `CollectiveConstantEntry` .

Value -> (string)

The value of a `CollectiveConstantEntry` .

SortDirection -> (string)

The sort direction for the `TopicIRFilterOption` .

Anchor -> (structure)

The anchor for the `TopicIRFilterOption` .

AnchorType -> (string)

The `AnchorType` for the Anchor.

TimeGranularity -> (string)

The `TimeGranularity` of the Anchor.

Offset -> (integer)

The offset of the Anchor.

Direction -> (string)

The direction for the `TopicIRContributionAnalysis` .

SortType -> (string)

The sort type for the `TopicIRContributionAnalysis` .

Visual -> (structure)

The visual for the `TopicIR` .

type -> (string)

The type for a `VisualOptions` .

SupportingVisuals -> (list)

The supporting visuals for the `TopicVisual` .

( â¦ recursive â¦ )

Template -> (structure)

The template for the `CreateTopicReviewedAnswer` .

TemplateType -> (string)

The template type for the `TopicTemplate` .

Slots -> (list)

The slots for the `TopicTemplate` .

(structure)

The definition for the slot.

SlotId -> (string)

The slot ID of the slot.

VisualId -> (string)

The visual ID for the slot.

JSON Syntax:

```
[
  {
    "AnswerId": "string",
    "DatasetArn": "string",
    "Question": "string",
    "Mir": {
      "Metrics": [
        {
          "MetricId": {
            "Identity": "string"
          },
          "Function": {
            "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
            "AggregationFunctionParameters": {"string": "string"
              ...},
            "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
            "PeriodField": "string"
          },
          "Operands": [
            {
              "Identity": "string"
            }
            ...
          ],
          "ComparisonMethod": {
            "Type": "DIFF"|"PERC_DIFF"|"DIFF_AS_PERC"|"POP_CURRENT_DIFF_AS_PERC"|"POP_CURRENT_DIFF"|"POP_OVERTIME_DIFF_AS_PERC"|"POP_OVERTIME_DIFF"|"PERCENT_OF_TOTAL"|"RUNNING_SUM"|"MOVING_AVERAGE",
            "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
            "WindowSize": integer
          },
          "Expression": "string",
          "CalculatedFieldReferences": [
            {
              "Identity": "string"
            }
            ...
          ],
          "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
          "DisplayFormatOptions": {
            "UseBlankCellFormat": true|false,
            "BlankCellFormat": "string",
            "DateFormat": "string",
            "DecimalSeparator": "COMMA"|"DOT",
            "GroupingSeparator": "string",
            "UseGrouping": true|false,
            "FractionDigits": integer,
            "Prefix": "string",
            "Suffix": "string",
            "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
            "NegativeFormat": {
              "Prefix": "string",
              "Suffix": "string"
            },
            "CurrencySymbol": "string"
          },
          "NamedEntity": {
            "NamedEntityName": "string"
          }
        }
        ...
      ],
      "GroupByList": [
        {
          "FieldName": {
            "Identity": "string"
          },
          "TimeGranularity": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
          "Sort": {
            "Operand": {
              "Identity": "string"
            },
            "SortDirection": "ASCENDING"|"DESCENDING"
          },
          "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
          "DisplayFormatOptions": {
            "UseBlankCellFormat": true|false,
            "BlankCellFormat": "string",
            "DateFormat": "string",
            "DecimalSeparator": "COMMA"|"DOT",
            "GroupingSeparator": "string",
            "UseGrouping": true|false,
            "FractionDigits": integer,
            "Prefix": "string",
            "Suffix": "string",
            "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
            "NegativeFormat": {
              "Prefix": "string",
              "Suffix": "string"
            },
            "CurrencySymbol": "string"
          },
          "NamedEntity": {
            "NamedEntityName": "string"
          }
        }
        ...
      ],
      "Filters": [
        [
          {
            "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
            "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
            "OperandField": {
              "Identity": "string"
            },
            "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
            "Constant": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inverse": true|false,
            "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
            "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
            "AggregationFunctionParameters": {"string": "string"
              ...},
            "AggregationPartitionBy": [
              {
                "FieldName": "string",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
              }
              ...
            ],
            "Range": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inclusive": true|false,
            "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
            "LastNextOffset": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "AggMetrics": [
              {
                "MetricOperand": {
                  "Identity": "string"
                },
                "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                "SortDirection": "ASCENDING"|"DESCENDING"
              }
              ...
            ],
            "TopBottomLimit": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "SortDirection": "ASCENDING"|"DESCENDING",
            "Anchor": {
              "AnchorType": "TODAY",
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "Offset": integer
            }
          }
          ...
        ]
        ...
      ],
      "Sort": {
        "Operand": {
          "Identity": "string"
        },
        "SortDirection": "ASCENDING"|"DESCENDING"
      },
      "ContributionAnalysis": {
        "Factors": [
          {
            "FieldName": "string"
          }
          ...
        ],
        "TimeRanges": {
          "StartRange": {
            "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
            "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
            "OperandField": {
              "Identity": "string"
            },
            "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
            "Constant": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inverse": true|false,
            "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
            "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
            "AggregationFunctionParameters": {"string": "string"
              ...},
            "AggregationPartitionBy": [
              {
                "FieldName": "string",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
              }
              ...
            ],
            "Range": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inclusive": true|false,
            "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
            "LastNextOffset": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "AggMetrics": [
              {
                "MetricOperand": {
                  "Identity": "string"
                },
                "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                "SortDirection": "ASCENDING"|"DESCENDING"
              }
              ...
            ],
            "TopBottomLimit": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "SortDirection": "ASCENDING"|"DESCENDING",
            "Anchor": {
              "AnchorType": "TODAY",
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "Offset": integer
            }
          },
          "EndRange": {
            "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
            "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
            "OperandField": {
              "Identity": "string"
            },
            "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
            "Constant": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inverse": true|false,
            "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
            "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
            "AggregationFunctionParameters": {"string": "string"
              ...},
            "AggregationPartitionBy": [
              {
                "FieldName": "string",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
              }
              ...
            ],
            "Range": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "Inclusive": true|false,
            "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
            "LastNextOffset": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "AggMetrics": [
              {
                "MetricOperand": {
                  "Identity": "string"
                },
                "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                "SortDirection": "ASCENDING"|"DESCENDING"
              }
              ...
            ],
            "TopBottomLimit": {
              "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
              "Value": "string",
              "Minimum": "string",
              "Maximum": "string",
              "ValueList": [
                {
                  "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                  "Value": "string"
                }
                ...
              ]
            },
            "SortDirection": "ASCENDING"|"DESCENDING",
            "Anchor": {
              "AnchorType": "TODAY",
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "Offset": integer
            }
          }
        },
        "Direction": "INCREASE"|"DECREASE"|"NEUTRAL",
        "SortType": "ABSOLUTE_DIFFERENCE"|"CONTRIBUTION_PERCENTAGE"|"DEVIATION_FROM_EXPECTED"|"PERCENTAGE_DIFFERENCE"
      },
      "Visual": {
        "type": "string"
      }
    },
    "PrimaryVisual": {
      "VisualId": "string",
      "Role": "PRIMARY"|"COMPLIMENTARY"|"MULTI_INTENT"|"FALLBACK"|"FRAGMENT",
      "Ir": {
        "Metrics": [
          {
            "MetricId": {
              "Identity": "string"
            },
            "Function": {
              "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
              "AggregationFunctionParameters": {"string": "string"
                ...},
              "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
              "PeriodField": "string"
            },
            "Operands": [
              {
                "Identity": "string"
              }
              ...
            ],
            "ComparisonMethod": {
              "Type": "DIFF"|"PERC_DIFF"|"DIFF_AS_PERC"|"POP_CURRENT_DIFF_AS_PERC"|"POP_CURRENT_DIFF"|"POP_OVERTIME_DIFF_AS_PERC"|"POP_OVERTIME_DIFF"|"PERCENT_OF_TOTAL"|"RUNNING_SUM"|"MOVING_AVERAGE",
              "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
              "WindowSize": integer
            },
            "Expression": "string",
            "CalculatedFieldReferences": [
              {
                "Identity": "string"
              }
              ...
            ],
            "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
            "DisplayFormatOptions": {
              "UseBlankCellFormat": true|false,
              "BlankCellFormat": "string",
              "DateFormat": "string",
              "DecimalSeparator": "COMMA"|"DOT",
              "GroupingSeparator": "string",
              "UseGrouping": true|false,
              "FractionDigits": integer,
              "Prefix": "string",
              "Suffix": "string",
              "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
              "NegativeFormat": {
                "Prefix": "string",
                "Suffix": "string"
              },
              "CurrencySymbol": "string"
            },
            "NamedEntity": {
              "NamedEntityName": "string"
            }
          }
          ...
        ],
        "GroupByList": [
          {
            "FieldName": {
              "Identity": "string"
            },
            "TimeGranularity": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
            "Sort": {
              "Operand": {
                "Identity": "string"
              },
              "SortDirection": "ASCENDING"|"DESCENDING"
            },
            "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
            "DisplayFormatOptions": {
              "UseBlankCellFormat": true|false,
              "BlankCellFormat": "string",
              "DateFormat": "string",
              "DecimalSeparator": "COMMA"|"DOT",
              "GroupingSeparator": "string",
              "UseGrouping": true|false,
              "FractionDigits": integer,
              "Prefix": "string",
              "Suffix": "string",
              "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
              "NegativeFormat": {
                "Prefix": "string",
                "Suffix": "string"
              },
              "CurrencySymbol": "string"
            },
            "NamedEntity": {
              "NamedEntityName": "string"
            }
          }
          ...
        ],
        "Filters": [
          [
            {
              "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
              "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
              "OperandField": {
                "Identity": "string"
              },
              "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
              "Constant": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inverse": true|false,
              "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
              "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
              "AggregationFunctionParameters": {"string": "string"
                ...},
              "AggregationPartitionBy": [
                {
                  "FieldName": "string",
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                }
                ...
              ],
              "Range": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inclusive": true|false,
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "LastNextOffset": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "AggMetrics": [
                {
                  "MetricOperand": {
                    "Identity": "string"
                  },
                  "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "SortDirection": "ASCENDING"|"DESCENDING"
                }
                ...
              ],
              "TopBottomLimit": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "SortDirection": "ASCENDING"|"DESCENDING",
              "Anchor": {
                "AnchorType": "TODAY",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                "Offset": integer
              }
            }
            ...
          ]
          ...
        ],
        "Sort": {
          "Operand": {
            "Identity": "string"
          },
          "SortDirection": "ASCENDING"|"DESCENDING"
        },
        "ContributionAnalysis": {
          "Factors": [
            {
              "FieldName": "string"
            }
            ...
          ],
          "TimeRanges": {
            "StartRange": {
              "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
              "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
              "OperandField": {
                "Identity": "string"
              },
              "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
              "Constant": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inverse": true|false,
              "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
              "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
              "AggregationFunctionParameters": {"string": "string"
                ...},
              "AggregationPartitionBy": [
                {
                  "FieldName": "string",
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                }
                ...
              ],
              "Range": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inclusive": true|false,
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "LastNextOffset": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "AggMetrics": [
                {
                  "MetricOperand": {
                    "Identity": "string"
                  },
                  "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "SortDirection": "ASCENDING"|"DESCENDING"
                }
                ...
              ],
              "TopBottomLimit": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "SortDirection": "ASCENDING"|"DESCENDING",
              "Anchor": {
                "AnchorType": "TODAY",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                "Offset": integer
              }
            },
            "EndRange": {
              "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
              "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
              "OperandField": {
                "Identity": "string"
              },
              "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
              "Constant": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inverse": true|false,
              "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
              "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
              "AggregationFunctionParameters": {"string": "string"
                ...},
              "AggregationPartitionBy": [
                {
                  "FieldName": "string",
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                }
                ...
              ],
              "Range": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "Inclusive": true|false,
              "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
              "LastNextOffset": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "AggMetrics": [
                {
                  "MetricOperand": {
                    "Identity": "string"
                  },
                  "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "SortDirection": "ASCENDING"|"DESCENDING"
                }
                ...
              ],
              "TopBottomLimit": {
                "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                "Value": "string",
                "Minimum": "string",
                "Maximum": "string",
                "ValueList": [
                  {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string"
                  }
                  ...
                ]
              },
              "SortDirection": "ASCENDING"|"DESCENDING",
              "Anchor": {
                "AnchorType": "TODAY",
                "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                "Offset": integer
              }
            }
          },
          "Direction": "INCREASE"|"DECREASE"|"NEUTRAL",
          "SortType": "ABSOLUTE_DIFFERENCE"|"CONTRIBUTION_PERCENTAGE"|"DEVIATION_FROM_EXPECTED"|"PERCENTAGE_DIFFERENCE"
        },
        "Visual": {
          "type": "string"
        }
      },
      "SupportingVisuals": [
        {
          "VisualId": "string",
          "Role": "PRIMARY"|"COMPLIMENTARY"|"MULTI_INTENT"|"FALLBACK"|"FRAGMENT",
          "Ir": {
            "Metrics": [
              {
                "MetricId": {
                  "Identity": "string"
                },
                "Function": {
                  "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "AggregationFunctionParameters": {"string": "string"
                    ...},
                  "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
                  "PeriodField": "string"
                },
                "Operands": [
                  {
                    "Identity": "string"
                  }
                  ...
                ],
                "ComparisonMethod": {
                  "Type": "DIFF"|"PERC_DIFF"|"DIFF_AS_PERC"|"POP_CURRENT_DIFF_AS_PERC"|"POP_CURRENT_DIFF"|"POP_OVERTIME_DIFF_AS_PERC"|"POP_OVERTIME_DIFF"|"PERCENT_OF_TOTAL"|"RUNNING_SUM"|"MOVING_AVERAGE",
                  "Period": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
                  "WindowSize": integer
                },
                "Expression": "string",
                "CalculatedFieldReferences": [
                  {
                    "Identity": "string"
                  }
                  ...
                ],
                "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
                "DisplayFormatOptions": {
                  "UseBlankCellFormat": true|false,
                  "BlankCellFormat": "string",
                  "DateFormat": "string",
                  "DecimalSeparator": "COMMA"|"DOT",
                  "GroupingSeparator": "string",
                  "UseGrouping": true|false,
                  "FractionDigits": integer,
                  "Prefix": "string",
                  "Suffix": "string",
                  "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
                  "NegativeFormat": {
                    "Prefix": "string",
                    "Suffix": "string"
                  },
                  "CurrencySymbol": "string"
                },
                "NamedEntity": {
                  "NamedEntityName": "string"
                }
              }
              ...
            ],
            "GroupByList": [
              {
                "FieldName": {
                  "Identity": "string"
                },
                "TimeGranularity": "SECOND"|"MINUTE"|"HOUR"|"DAY"|"WEEK"|"MONTH"|"QUARTER"|"YEAR",
                "Sort": {
                  "Operand": {
                    "Identity": "string"
                  },
                  "SortDirection": "ASCENDING"|"DESCENDING"
                },
                "DisplayFormat": "AUTO"|"PERCENT"|"CURRENCY"|"NUMBER"|"DATE"|"STRING",
                "DisplayFormatOptions": {
                  "UseBlankCellFormat": true|false,
                  "BlankCellFormat": "string",
                  "DateFormat": "string",
                  "DecimalSeparator": "COMMA"|"DOT",
                  "GroupingSeparator": "string",
                  "UseGrouping": true|false,
                  "FractionDigits": integer,
                  "Prefix": "string",
                  "Suffix": "string",
                  "UnitScaler": "NONE"|"AUTO"|"THOUSANDS"|"MILLIONS"|"BILLIONS"|"TRILLIONS"|"LAKHS"|"CRORES",
                  "NegativeFormat": {
                    "Prefix": "string",
                    "Suffix": "string"
                  },
                  "CurrencySymbol": "string"
                },
                "NamedEntity": {
                  "NamedEntityName": "string"
                }
              }
              ...
            ],
            "Filters": [
              [
                {
                  "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
                  "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
                  "OperandField": {
                    "Identity": "string"
                  },
                  "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
                  "Constant": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inverse": true|false,
                  "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
                  "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "AggregationFunctionParameters": {"string": "string"
                    ...},
                  "AggregationPartitionBy": [
                    {
                      "FieldName": "string",
                      "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                    }
                    ...
                  ],
                  "Range": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inclusive": true|false,
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                  "LastNextOffset": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "AggMetrics": [
                    {
                      "MetricOperand": {
                        "Identity": "string"
                      },
                      "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                      "SortDirection": "ASCENDING"|"DESCENDING"
                    }
                    ...
                  ],
                  "TopBottomLimit": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "SortDirection": "ASCENDING"|"DESCENDING",
                  "Anchor": {
                    "AnchorType": "TODAY",
                    "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                    "Offset": integer
                  }
                }
                ...
              ]
              ...
            ],
            "Sort": {
              "Operand": {
                "Identity": "string"
              },
              "SortDirection": "ASCENDING"|"DESCENDING"
            },
            "ContributionAnalysis": {
              "Factors": [
                {
                  "FieldName": "string"
                }
                ...
              ],
              "TimeRanges": {
                "StartRange": {
                  "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
                  "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
                  "OperandField": {
                    "Identity": "string"
                  },
                  "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
                  "Constant": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inverse": true|false,
                  "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
                  "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "AggregationFunctionParameters": {"string": "string"
                    ...},
                  "AggregationPartitionBy": [
                    {
                      "FieldName": "string",
                      "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                    }
                    ...
                  ],
                  "Range": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inclusive": true|false,
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                  "LastNextOffset": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "AggMetrics": [
                    {
                      "MetricOperand": {
                        "Identity": "string"
                      },
                      "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                      "SortDirection": "ASCENDING"|"DESCENDING"
                    }
                    ...
                  ],
                  "TopBottomLimit": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "SortDirection": "ASCENDING"|"DESCENDING",
                  "Anchor": {
                    "AnchorType": "TODAY",
                    "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                    "Offset": integer
                  }
                },
                "EndRange": {
                  "FilterType": "CATEGORY_FILTER"|"NUMERIC_EQUALITY_FILTER"|"NUMERIC_RANGE_FILTER"|"DATE_RANGE_FILTER"|"RELATIVE_DATE_FILTER"|"TOP_BOTTOM_FILTER"|"EQUALS"|"RANK_LIMIT_FILTER"|"ACCEPT_ALL_FILTER",
                  "FilterClass": "ENFORCED_VALUE_FILTER"|"CONDITIONAL_VALUE_FILTER"|"NAMED_VALUE_FILTER",
                  "OperandField": {
                    "Identity": "string"
                  },
                  "Function": "CONTAINS"|"EXACT"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS_STRING"|"PREVIOUS"|"THIS"|"LAST"|"NEXT"|"NOW",
                  "Constant": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inverse": true|false,
                  "NullFilter": "ALL_VALUES"|"NON_NULLS_ONLY"|"NULLS_ONLY",
                  "Aggregation": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                  "AggregationFunctionParameters": {"string": "string"
                    ...},
                  "AggregationPartitionBy": [
                    {
                      "FieldName": "string",
                      "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND"
                    }
                    ...
                  ],
                  "Range": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "Inclusive": true|false,
                  "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                  "LastNextOffset": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "AggMetrics": [
                    {
                      "MetricOperand": {
                        "Identity": "string"
                      },
                      "Function": "SUM"|"MIN"|"MAX"|"COUNT"|"AVERAGE"|"DISTINCT_COUNT"|"STDEV"|"STDEVP"|"VAR"|"VARP"|"PERCENTILE"|"MEDIAN"|"PTD_SUM"|"PTD_MIN"|"PTD_MAX"|"PTD_COUNT"|"PTD_DISTINCT_COUNT"|"PTD_AVERAGE"|"COLUMN"|"CUSTOM",
                      "SortDirection": "ASCENDING"|"DESCENDING"
                    }
                    ...
                  ],
                  "TopBottomLimit": {
                    "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                    "Value": "string",
                    "Minimum": "string",
                    "Maximum": "string",
                    "ValueList": [
                      {
                        "ConstantType": "SINGULAR"|"RANGE"|"COLLECTIVE",
                        "Value": "string"
                      }
                      ...
                    ]
                  },
                  "SortDirection": "ASCENDING"|"DESCENDING",
                  "Anchor": {
                    "AnchorType": "TODAY",
                    "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
                    "Offset": integer
                  }
                }
              },
              "Direction": "INCREASE"|"DECREASE"|"NEUTRAL",
              "SortType": "ABSOLUTE_DIFFERENCE"|"CONTRIBUTION_PERCENTAGE"|"DEVIATION_FROM_EXPECTED"|"PERCENTAGE_DIFFERENCE"
            },
            "Visual": {
              "type": "string"
            }
          },
          "SupportingVisuals": [
            { ... recursive ... }
            ...
          ]
        }
        ...
      ]
    },
    "Template": {
      "TemplateType": "string",
      "Slots": [
        {
          "SlotId": "string",
          "VisualId": "string"
        }
        ...
      ]
    }
  }
  ...
]
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

TopicId -> (string)

The ID for the topic reviewed answer that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the topic.

SucceededAnswers -> (list)

The definition of Answers that are successfully created.

(structure)

The definition for a `SucceededTopicReviewedAnswer` .

AnswerId -> (string)

The answer ID for the `SucceededTopicReviewedAnswer` .

InvalidAnswers -> (list)

The definition of Answers that are invalid and not created.

(structure)

The definition for a `InvalidTopicReviewedAnswer` .

AnswerId -> (string)

The answer ID for the `InvalidTopicReviewedAnswer` .

Error -> (string)

The error that is returned for the `InvalidTopicReviewedAnswer` .

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.