# update-data-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-data-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# update-data-set

## Description

Updates a dataset. This operation doesnât support datasets that include uploaded files as a source. Partial updates are not supported by this operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/UpdateDataSet)

## Synopsis

```
update-data-set
--aws-account-id <value>
--data-set-id <value>
--name <value>
--physical-table-map <value>
[--logical-table-map <value>]
--import-mode <value>
[--column-groups <value>]
[--field-folders <value>]
[--row-level-permission-data-set <value>]
[--row-level-permission-tag-configuration <value>]
[--column-level-permission-rules <value>]
[--data-set-usage-configuration <value>]
[--dataset-parameters <value>]
[--performance-configuration <value>]
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

`--data-set-id` (string)

The ID for the dataset that you want to update. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

`--name` (string)

The display name for the dataset.

`--physical-table-map` (map)

Declares the physical tables that are available in the underlying data sources.

key -> (string)

value -> (structure)

A view of a data source that contains information about the shape of the data in the underlying source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

RelationalTable -> (structure)

A physical table type for relational data sources.

DataSourceArn -> (string)

The Amazon Resource Name (ARN) for the data source.

Catalog -> (string)

The catalog associated with a table.

Schema -> (string)

The schema name. This name applies to certain relational database engines.

Name -> (string)

The name of the relational table.

InputColumns -> (list)

The column schema of the table.

(structure)

Metadata for a column that is used as the input of a transform operation.

Name -> (string)

The name of this column in the underlying data source.

Type -> (string)

The data type of the column.

SubType -> (string)

The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.

CustomSql -> (structure)

A physical table type built from the results of the custom SQL query.

DataSourceArn -> (string)

The Amazon Resource Name (ARN) of the data source.

Name -> (string)

A display name for the SQL query result.

SqlQuery -> (string)

The SQL query.

Columns -> (list)

The column schema from the SQL query result set.

(structure)

Metadata for a column that is used as the input of a transform operation.

Name -> (string)

The name of this column in the underlying data source.

Type -> (string)

The data type of the column.

SubType -> (string)

The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.

S3Source -> (structure)

A physical table type for as S3 data source.

DataSourceArn -> (string)

The Amazon Resource Name (ARN) for the data source.

UploadSettings -> (structure)

Information about the format for the S3 source file or files.

Format -> (string)

File format.

StartFromRow -> (integer)

A row number to start reading data from.

ContainsHeader -> (boolean)

Whether the file has a header row, or the files each have a header row.

TextQualifier -> (string)

Text qualifier.

Delimiter -> (string)

The delimiter between values in the file.

InputColumns -> (list)

A physical table type for an S3 data source.

### Note

For files that arenât JSON, only `STRING` data types are supported in input columns.

(structure)

Metadata for a column that is used as the input of a transform operation.

Name -> (string)

The name of this column in the underlying data source.

Type -> (string)

The data type of the column.

SubType -> (string)

The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.

JSON Syntax:

```
{"string": {
      "RelationalTable": {
        "DataSourceArn": "string",
        "Catalog": "string",
        "Schema": "string",
        "Name": "string",
        "InputColumns": [
          {
            "Name": "string",
            "Type": "STRING"|"INTEGER"|"DECIMAL"|"DATETIME"|"BIT"|"BOOLEAN"|"JSON",
            "SubType": "FLOAT"|"FIXED"
          }
          ...
        ]
      },
      "CustomSql": {
        "DataSourceArn": "string",
        "Name": "string",
        "SqlQuery": "string",
        "Columns": [
          {
            "Name": "string",
            "Type": "STRING"|"INTEGER"|"DECIMAL"|"DATETIME"|"BIT"|"BOOLEAN"|"JSON",
            "SubType": "FLOAT"|"FIXED"
          }
          ...
        ]
      },
      "S3Source": {
        "DataSourceArn": "string",
        "UploadSettings": {
          "Format": "CSV"|"TSV"|"CLF"|"ELF"|"XLSX"|"JSON",
          "StartFromRow": integer,
          "ContainsHeader": true|false,
          "TextQualifier": "DOUBLE_QUOTE"|"SINGLE_QUOTE",
          "Delimiter": "string"
        },
        "InputColumns": [
          {
            "Name": "string",
            "Type": "STRING"|"INTEGER"|"DECIMAL"|"DATETIME"|"BIT"|"BOOLEAN"|"JSON",
            "SubType": "FLOAT"|"FIXED"
          }
          ...
        ]
      }
    }
  ...}
```

`--logical-table-map` (map)

Configures the combination and transformation of the data from the physical tables.

key -> (string)

An identifier for the logical table that is defined in the dataset

value -> (structure)

A *logical table* is a unit that joins and that data transformations operate on. A logical table has a source, which can be either a physical table or result of a join. When a logical table points to a physical table, the logical table acts as a mutable copy of that physical table through transform operations.

Alias -> (string)

A display name for the logical table.

DataTransforms -> (list)

Transform operations that act on this logical table. For this structure to be valid, only one of the attributes can be non-null.

(structure)

A data transformation on a logical table. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

ProjectOperation -> (structure)

An operation that projects columns. Operations that come after a projection can only refer to projected columns.

ProjectedColumns -> (list)

Projected columns.

(string)

FilterOperation -> (structure)

An operation that filters rows based on some condition.

ConditionExpression -> (string)

An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.

CreateColumnsOperation -> (structure)

An operation that creates calculated columns. Columns created in one such operation form a lexical closure.

Columns -> (list)

Calculated columns to create.

(structure)

A calculated column for a dataset.

ColumnName -> (string)

Column name.

ColumnId -> (string)

A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Amazon QuickSight preserves the existing calculated column.

Expression -> (string)

An expression that defines the calculated column.

RenameColumnOperation -> (structure)

An operation that renames a column.

ColumnName -> (string)

The name of the column to be renamed.

NewColumnName -> (string)

The new name for the column.

CastColumnTypeOperation -> (structure)

A transform operation that casts a column to a different type.

ColumnName -> (string)

Column name.

NewColumnType -> (string)

New column data type.

SubType -> (string)

The sub data type of the new column. Sub types are only available for decimal columns that are part of a SPICE dataset.

Format -> (string)

When casting a column from string to datetime type, you can supply a string in a format supported by Amazon QuickSight to denote the source data format.

TagColumnOperation -> (structure)

An operation that tags a column with additional information.

ColumnName -> (string)

The column that this operation acts on.

Tags -> (list)

The dataset column tag, currently only used for geospatial type tagging.

### Note

This is not tags for the Amazon Web Services tagging feature.

(structure)

A tag for a column in a `` [TagColumnOperation](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagColumnOperation.html) `` structure. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

ColumnGeographicRole -> (string)

A geospatial role for a column.

ColumnDescription -> (structure)

A description for a column.

Text -> (string)

The text of a description for a column.

UntagColumnOperation -> (structure)

A transform operation that removes tags associated with a column.

ColumnName -> (string)

The column that this operation acts on.

TagNames -> (list)

The column tags to remove from this column.

(string)

OverrideDatasetParameterOperation -> (structure)

A transform operation that overrides the dataset parameter values that are defined in another dataset.

ParameterName -> (string)

The name of the parameter to be overridden with different values.

NewParameterName -> (string)

The new name for the parameter.

NewDefaultValues -> (structure)

The new default values for the parameter.

StringStaticValues -> (list)

A list of static default values for a given string parameter.

(string)

The default value for the string parameter.

DecimalStaticValues -> (list)

A list of static default values for a given decimal parameter.

(double)

The default value for the decimal parameter.

DateTimeStaticValues -> (list)

A list of static default values for a given date time parameter.

(timestamp)

The default value for the date time parameter.

IntegerStaticValues -> (list)

A list of static default values for a given integer parameter.

(long)

The default value for the integer parameter.

Source -> (structure)

Source of this logical table.

JoinInstruction -> (structure)

Specifies the result of a join of two logical tables.

LeftOperand -> (string)

The operand on the left side of a join.

RightOperand -> (string)

The operand on the right side of a join.

LeftJoinKeyProperties -> (structure)

Join key properties of the left operand.

UniqueKey -> (boolean)

A value that indicates that a row in a table is uniquely identified by the columns in a join key. This is used by Amazon QuickSight to optimize query performance.

RightJoinKeyProperties -> (structure)

Join key properties of the right operand.

UniqueKey -> (boolean)

A value that indicates that a row in a table is uniquely identified by the columns in a join key. This is used by Amazon QuickSight to optimize query performance.

Type -> (string)

The type of join that it is.

OnClause -> (string)

The join instructions provided in the `ON` clause of a join.

PhysicalTableId -> (string)

Physical table ID.

DataSetArn -> (string)

The Amazon Resource Number (ARN) of the parent dataset.

JSON Syntax:

```
{"string": {
      "Alias": "string",
      "DataTransforms": [
        {
          "ProjectOperation": {
            "ProjectedColumns": ["string", ...]
          },
          "FilterOperation": {
            "ConditionExpression": "string"
          },
          "CreateColumnsOperation": {
            "Columns": [
              {
                "ColumnName": "string",
                "ColumnId": "string",
                "Expression": "string"
              }
              ...
            ]
          },
          "RenameColumnOperation": {
            "ColumnName": "string",
            "NewColumnName": "string"
          },
          "CastColumnTypeOperation": {
            "ColumnName": "string",
            "NewColumnType": "STRING"|"INTEGER"|"DECIMAL"|"DATETIME",
            "SubType": "FLOAT"|"FIXED",
            "Format": "string"
          },
          "TagColumnOperation": {
            "ColumnName": "string",
            "Tags": [
              {
                "ColumnGeographicRole": "COUNTRY"|"STATE"|"COUNTY"|"CITY"|"POSTCODE"|"LONGITUDE"|"LATITUDE",
                "ColumnDescription": {
                  "Text": "string"
                }
              }
              ...
            ]
          },
          "UntagColumnOperation": {
            "ColumnName": "string",
            "TagNames": ["COLUMN_GEOGRAPHIC_ROLE"|"COLUMN_DESCRIPTION", ...]
          },
          "OverrideDatasetParameterOperation": {
            "ParameterName": "string",
            "NewParameterName": "string",
            "NewDefaultValues": {
              "StringStaticValues": ["string", ...],
              "DecimalStaticValues": [double, ...],
              "DateTimeStaticValues": [timestamp, ...],
              "IntegerStaticValues": [long, ...]
            }
          }
        }
        ...
      ],
      "Source": {
        "JoinInstruction": {
          "LeftOperand": "string",
          "RightOperand": "string",
          "LeftJoinKeyProperties": {
            "UniqueKey": true|false
          },
          "RightJoinKeyProperties": {
            "UniqueKey": true|false
          },
          "Type": "INNER"|"OUTER"|"LEFT"|"RIGHT",
          "OnClause": "string"
        },
        "PhysicalTableId": "string",
        "DataSetArn": "string"
      }
    }
  ...}
```

`--import-mode` (string)

Indicates whether you want to import the data into SPICE.

Possible values:

- `SPICE`
- `DIRECT_QUERY`

`--column-groups` (list)

Groupings of columns that work together in certain Amazon QuickSight features. Currently, only geospatial hierarchy is supported.

(structure)

Groupings of columns that work together in certain Amazon QuickSight features. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

GeoSpatialColumnGroup -> (structure)

Geospatial column group that denotes a hierarchy.

Name -> (string)

A display name for the hierarchy.

CountryCode -> (string)

Country code.

Columns -> (list)

Columns in this hierarchy.

(string)

Shorthand Syntax:

```
GeoSpatialColumnGroup={Name=string,CountryCode=string,Columns=[string,string]} ...
```

JSON Syntax:

```
[
  {
    "GeoSpatialColumnGroup": {
      "Name": "string",
      "CountryCode": "US",
      "Columns": ["string", ...]
    }
  }
  ...
]
```

`--field-folders` (map)

The folder that contains fields and nested subfolders for your dataset.

key -> (string)

value -> (structure)

A FieldFolder element is a folder that contains fields and nested subfolders.

description -> (string)

The description for a field folder.

columns -> (list)

A folder has a list of columns. A column can only be in one folder.

(string)

Shorthand Syntax:

```
KeyName1=description=string,columns=string,string,KeyName2=description=string,columns=string,string
```

JSON Syntax:

```
{"string": {
      "description": "string",
      "columns": ["string", ...]
    }
  ...}
```

`--row-level-permission-data-set` (structure)

The row-level security configuration for the data you want to create.

Namespace -> (string)

The namespace associated with the dataset that contains permissions for RLS.

Arn -> (string)

The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.

PermissionPolicy -> (string)

The type of permissions to use when interpreting the permissions for RLS. `DENY_ACCESS` is included for backward compatibility only.

FormatVersion -> (string)

The user or group rules associated with the dataset that contains permissions for RLS.

By default, `FormatVersion` is `VERSION_1` . When `FormatVersion` is `VERSION_1` , `UserName` and `GroupName` are required. When `FormatVersion` is `VERSION_2` , `UserARN` and `GroupARN` are required, and `Namespace` must not exist.

Status -> (string)

The status of the row-level security permission dataset. If enabled, the status is `ENABLED` . If disabled, the status is `DISABLED` .

Shorthand Syntax:

```
Namespace=string,Arn=string,PermissionPolicy=string,FormatVersion=string,Status=string
```

JSON Syntax:

```
{
  "Namespace": "string",
  "Arn": "string",
  "PermissionPolicy": "GRANT_ACCESS"|"DENY_ACCESS",
  "FormatVersion": "VERSION_1"|"VERSION_2",
  "Status": "ENABLED"|"DISABLED"
}
```

`--row-level-permission-tag-configuration` (structure)

The configuration of tags on a dataset to set row-level security. Row-level security tags are currently supported for anonymous embedding only.

Status -> (string)

The status of row-level security tags. If enabled, the status is `ENABLED` . If disabled, the status is `DISABLED` .

TagRules -> (list)

A set of rules associated with row-level security, such as the tag names and columns that they are assigned to.

(structure)

A set of rules associated with a tag.

TagKey -> (string)

The unique key for a tag.

ColumnName -> (string)

The column name that a tag key is assigned to.

TagMultiValueDelimiter -> (string)

A string that you want to use to delimit the values when you pass the values at run time. For example, you can delimit the values with a comma.

MatchAllValue -> (string)

A string that you want to use to filter by all the values in a column in the dataset and donât want to list the values one by one. For example, you can use an asterisk as your match all value.

TagRuleConfigurations -> (list)

A list of tag configuration rules to apply to a dataset. All tag configurations have the OR condition. Tags within each tile will be joined (AND). At least one rule in this structure must have all tag values assigned to it to apply Row-level security (RLS) to the dataset.

(list)

(string)

Shorthand Syntax:

```
Status=string,TagRules=[{TagKey=string,ColumnName=string,TagMultiValueDelimiter=string,MatchAllValue=string},{TagKey=string,ColumnName=string,TagMultiValueDelimiter=string,MatchAllValue=string}],TagRuleConfigurations=[[string,string],[string,string]]
```

JSON Syntax:

```
{
  "Status": "ENABLED"|"DISABLED",
  "TagRules": [
    {
      "TagKey": "string",
      "ColumnName": "string",
      "TagMultiValueDelimiter": "string",
      "MatchAllValue": "string"
    }
    ...
  ],
  "TagRuleConfigurations": [
    ["string", ...]
    ...
  ]
}
```

`--column-level-permission-rules` (list)

A set of one or more definitions of a `` [ColumnLevelPermissionRule](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html) `` .

(structure)

A rule defined to grant access on one or more restricted columns. Each dataset can have multiple rules. To create a restricted column, you add it to one or more rules. Each rule must contain at least one column and at least one user or group. To be able to see a restricted column, a user or group needs to be added to a rule for that column.

Principals -> (list)

An array of Amazon Resource Names (ARNs) for Amazon QuickSight users or groups.

(string)

ColumnNames -> (list)

An array of column names.

(string)

Shorthand Syntax:

```
Principals=string,string,ColumnNames=string,string ...
```

JSON Syntax:

```
[
  {
    "Principals": ["string", ...],
    "ColumnNames": ["string", ...]
  }
  ...
]
```

`--data-set-usage-configuration` (structure)

The usage configuration to apply to child datasets that reference this dataset as a source.

DisableUseAsDirectQuerySource -> (boolean)

An option that controls whether a child dataset of a direct query can use this dataset as a source.

DisableUseAsImportedSource -> (boolean)

An option that controls whether a child dataset thatâs stored in QuickSight can use this dataset as a source.

Shorthand Syntax:

```
DisableUseAsDirectQuerySource=boolean,DisableUseAsImportedSource=boolean
```

JSON Syntax:

```
{
  "DisableUseAsDirectQuerySource": true|false,
  "DisableUseAsImportedSource": true|false
}
```

`--dataset-parameters` (list)

The parameter declarations of the dataset.

(structure)

A parameter that is created in a dataset. The parameter can be a string, integer, decimal, or datetime data type.

StringDatasetParameter -> (structure)

A string parameter that is created in the dataset.

Id -> (string)

An identifier for the string parameter that is created in the dataset.

Name -> (string)

The name of the string parameter that is created in the dataset.

ValueType -> (string)

The value type of the dataset parameter. Valid values are `single value` or `multi value` .

DefaultValues -> (structure)

A list of default values for a given string dataset parameter type. This structure only accepts static values.

StaticValues -> (list)

A list of static default values for a given string parameter.

(string)

The default value for the string parameter.

DecimalDatasetParameter -> (structure)

A decimal parameter that is created in the dataset.

Id -> (string)

An identifier for the decimal parameter created in the dataset.

Name -> (string)

The name of the decimal parameter that is created in the dataset.

ValueType -> (string)

The value type of the dataset parameter. Valid values are `single value` or `multi value` .

DefaultValues -> (structure)

A list of default values for a given decimal parameter. This structure only accepts static values.

StaticValues -> (list)

A list of static default values for a given decimal parameter.

(double)

The default value for the decimal parameter.

IntegerDatasetParameter -> (structure)

An integer parameter that is created in the dataset.

Id -> (string)

An identifier for the integer parameter created in the dataset.

Name -> (string)

The name of the integer parameter that is created in the dataset.

ValueType -> (string)

The value type of the dataset parameter. Valid values are `single value` or `multi value` .

DefaultValues -> (structure)

A list of default values for a given integer parameter. This structure only accepts static values.

StaticValues -> (list)

A list of static default values for a given integer parameter.

(long)

The default value for the integer parameter.

DateTimeDatasetParameter -> (structure)

A date time parameter that is created in the dataset.

Id -> (string)

An identifier for the parameter that is created in the dataset.

Name -> (string)

The name of the date time parameter that is created in the dataset.

ValueType -> (string)

The value type of the dataset parameter. Valid values are `single value` or `multi value` .

TimeGranularity -> (string)

The time granularity of the date time parameter.

DefaultValues -> (structure)

A list of default values for a given date time parameter. This structure only accepts static values.

StaticValues -> (list)

A list of static default values for a given date time parameter.

(timestamp)

The default value for the date time parameter.

JSON Syntax:

```
[
  {
    "StringDatasetParameter": {
      "Id": "string",
      "Name": "string",
      "ValueType": "MULTI_VALUED"|"SINGLE_VALUED",
      "DefaultValues": {
        "StaticValues": ["string", ...]
      }
    },
    "DecimalDatasetParameter": {
      "Id": "string",
      "Name": "string",
      "ValueType": "MULTI_VALUED"|"SINGLE_VALUED",
      "DefaultValues": {
        "StaticValues": [double, ...]
      }
    },
    "IntegerDatasetParameter": {
      "Id": "string",
      "Name": "string",
      "ValueType": "MULTI_VALUED"|"SINGLE_VALUED",
      "DefaultValues": {
        "StaticValues": [long, ...]
      }
    },
    "DateTimeDatasetParameter": {
      "Id": "string",
      "Name": "string",
      "ValueType": "MULTI_VALUED"|"SINGLE_VALUED",
      "TimeGranularity": "YEAR"|"QUARTER"|"MONTH"|"WEEK"|"DAY"|"HOUR"|"MINUTE"|"SECOND"|"MILLISECOND",
      "DefaultValues": {
        "StaticValues": [timestamp, ...]
      }
    }
  }
  ...
]
```

`--performance-configuration` (structure)

The configuration for the performance optimization of the dataset that contains a `UniqueKey` configuration.

UniqueKeys -> (list)

A `UniqueKey` configuration.

(structure)

A `UniqueKey` configuration that references a dataset column.

ColumnNames -> (list)

The name of the column that is referenced in the `UniqueKey` configuration.

(string)

JSON Syntax:

```
{
  "UniqueKeys": [
    {
      "ColumnNames": ["string", ...]
    }
    ...
  ]
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

Arn -> (string)

The Amazon Resource Name (ARN) of the dataset.

DataSetId -> (string)

The ID for the dataset that you want to create. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

IngestionArn -> (string)

The ARN for the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

IngestionId -> (string)

The ID of the ingestion, which is triggered as a result of dataset creation if the import mode is SPICE.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.