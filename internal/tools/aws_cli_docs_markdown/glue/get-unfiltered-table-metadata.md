# get-unfiltered-table-metadataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-unfiltered-table-metadata.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-unfiltered-table-metadata.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-unfiltered-table-metadata

## Description

Allows a third-party analytical engine to retrieve unfiltered table metadata from the Data Catalog.

For IAM authorization, the public IAM action associated with this API is `glue:GetTable` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUnfilteredTableMetadata)

## Synopsis

```
get-unfiltered-table-metadata
--catalog-id <value>
--database-name <value>
--name <value>
[--audit-context <value>]
--supported-permission-types <value>
[--parent-resource-arn <value>]
[--root-resource-arn <value>]
[--supported-dialect <value>]
[--permissions <value>]
[--query-session-context <value>]
[--resource-region <value>]
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

`--catalog-id` (string)

The catalog ID where the table resides.

`--database-name` (string)

(Required) Specifies the name of a database that contains the table.

`--name` (string)

(Required) Specifies the name of a table for which you are requesting metadata.

`--audit-context` (structure)

A structure containing Lake Formation audit context information.

AdditionalAuditContext -> (string)

A string containing the additional audit context information.

RequestedColumns -> (list)

The requested columns for audit.

(string)

AllColumnsRequested -> (boolean)

All columns request for audit.

Shorthand Syntax:

```
AdditionalAuditContext=string,RequestedColumns=string,string,AllColumnsRequested=boolean
```

JSON Syntax:

```
{
  "AdditionalAuditContext": "string",
  "RequestedColumns": ["string", ...],
  "AllColumnsRequested": true|false
}
```

`--supported-permission-types` (list)

Indicates the level of filtering a third-party analytical engine is capable of enforcing when calling the `GetUnfilteredTableMetadata` API operation. Accepted values are:

- `COLUMN_PERMISSION` - Column permissions ensure that users can access only specific columns in the table. If there are particular columns contain sensitive data, data lake administrators can define column filters that exclude access to specific columns.
- `CELL_FILTER_PERMISSION` - Cell-level filtering combines column filtering (include or exclude columns) and row filter expressions to restrict access to individual elements in the table.
- `NESTED_PERMISSION` - Nested permissions combines cell-level filtering and nested column filtering to restrict access to columns and/or nested columns in specific rows based on row filter expressions.
- `NESTED_CELL_PERMISSION` - Nested cell permissions combines nested permission with nested cell-level filtering. This allows different subsets of nested columns to be restricted based on an array of row filter expressions.

Note: Each of these permission types follows a hierarchical order where each subsequent permission type includes all permission of the previous type.

Important: If you provide a supported permission type that doesnât match the userâs level of permissions on the table, then Lake Formation raises an exception. For example, if the third-party engine calling the `GetUnfilteredTableMetadata` operation can enforce only column-level filtering, and the user has nested cell filtering applied on the table, Lake Formation throws an exception, and will not return unfiltered table metadata and data access credentials.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  COLUMN_PERMISSION
  CELL_FILTER_PERMISSION
  NESTED_PERMISSION
  NESTED_CELL_PERMISSION
```

`--parent-resource-arn` (string)

The resource ARN of the view.

`--root-resource-arn` (string)

The resource ARN of the root view in a chain of nested views.

`--supported-dialect` (structure)

A structure specifying the dialect and dialect version used by the query engine.

Dialect -> (string)

The dialect of the query engine.

DialectVersion -> (string)

The version of the dialect of the query engine. For example, 3.0.0.

Shorthand Syntax:

```
Dialect=string,DialectVersion=string
```

JSON Syntax:

```
{
  "Dialect": "REDSHIFT"|"ATHENA"|"SPARK",
  "DialectVersion": "string"
}
```

`--permissions` (list)

The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ALL
  SELECT
  ALTER
  DROP
  DELETE
  INSERT
  CREATE_DATABASE
  CREATE_TABLE
  DATA_LOCATION_ACCESS
```

`--query-session-context` (structure)

A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the requestâs authorization context.

QueryId -> (string)

A unique identifier generated by the query engine for the query.

QueryStartTime -> (timestamp)

A timestamp provided by the query engine for when the query started.

ClusterId -> (string)

An identifier string for the consumer cluster.

QueryAuthorizationId -> (string)

A cryptographically generated query identifier generated by Glue or Lake Formation.

AdditionalContext -> (map)

An opaque string-string map passed by the query engine.

key -> (string)

value -> (string)

Shorthand Syntax:

```
QueryId=string,QueryStartTime=timestamp,ClusterId=string,QueryAuthorizationId=string,AdditionalContext={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "QueryId": "string",
  "QueryStartTime": timestamp,
  "ClusterId": "string",
  "QueryAuthorizationId": "string",
  "AdditionalContext": {"string": "string"
    ...}
}
```

`--resource-region` (string)

Specified only if the base tables belong to a different Amazon Web Services Region.

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

Table -> (structure)

A Table object containing the table metadata.

Name -> (string)

The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName -> (string)

The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description -> (string)

A description of the table.

Owner -> (string)

The owner of the table.

CreateTime -> (timestamp)

The time when the table definition was created in the Data Catalog.

UpdateTime -> (timestamp)

The last time that the table was updated.

LastAccessTime -> (timestamp)

The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime -> (timestamp)

The last time that column statistics were computed for this table.

Retention -> (integer)

The retention time for this table.

StorageDescriptor -> (structure)

A storage descriptor containing information about the physical storage of this table.

Columns -> (list)

A list of the `Columns` in the table.

(structure)

A column in a `Table` .

Name -> (string)

The name of the `Column` .

Type -> (string)

The data type of the `Column` .

Comment -> (string)

A free-form text comment.

Parameters -> (map)

These key-value pairs define properties associated with the column.

key -> (string)

value -> (string)

Location -> (string)

The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

AdditionalLocations -> (list)

A list of locations that point to the path where a Delta table is located.

(string)

InputFormat -> (string)

The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat` , or a custom format.

OutputFormat -> (string)

The output format: `SequenceFileOutputFormat` (binary), or `IgnoreKeyTextOutputFormat` , or a custom format.

Compressed -> (boolean)

`True` if the data in the table is compressed, or `False` if not.

NumberOfBuckets -> (integer)

Must be specified if the table contains any dimension columns.

SerdeInfo -> (structure)

The serialization/deserialization (SerDe) information.

Name -> (string)

Name of the SerDe.

SerializationLibrary -> (string)

Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe` .

Parameters -> (map)

These key-value pairs define initialization parameters for the SerDe.

key -> (string)

value -> (string)

BucketColumns -> (list)

A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string)

SortColumns -> (list)

A list specifying the sort order of each bucket in the table.

(structure)

Specifies the sort order of a sorted column.

Column -> (string)

The name of the column.

SortOrder -> (integer)

Indicates that the column is sorted in ascending order (`== 1` ), or in descending order (`==0` ).

Parameters -> (map)

The user-supplied properties in key-value form.

key -> (string)

value -> (string)

SkewedInfo -> (structure)

The information about values that appear frequently in a column (skewed values).

SkewedColumnNames -> (list)

A list of names of columns that contain skewed values.

(string)

SkewedColumnValues -> (list)

A list of values that appear so frequently as to be considered skewed.

(string)

SkewedColumnValueLocationMaps -> (map)

A mapping of skewed values to the columns that contain them.

key -> (string)

value -> (string)

StoredAsSubDirectories -> (boolean)

`True` if the table data is stored in subdirectories, or `False` if not.

SchemaReference -> (structure)

An object that references a schema stored in the Glue Schema Registry.

When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.

SchemaId -> (structure)

A structure that contains schema identity fields. Either this or the `SchemaVersionId` has to be provided.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema. One of `SchemaArn` or `SchemaName` has to be provided.

SchemaName -> (string)

The name of the schema. One of `SchemaArn` or `SchemaName` has to be provided.

RegistryName -> (string)

The name of the schema registry that contains the schema.

SchemaVersionId -> (string)

The unique ID assigned to a version of the schema. Either this or the `SchemaId` has to be provided.

SchemaVersionNumber -> (long)

The version number of the schema.

PartitionKeys -> (list)

A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

When you create a table used by Amazon Athena, and you do not specify any `partitionKeys` , you must at least set the value of `partitionKeys` to an empty list. For example:

`"PartitionKeys": []`

(structure)

A column in a `Table` .

Name -> (string)

The name of the `Column` .

Type -> (string)

The data type of the `Column` .

Comment -> (string)

A free-form text comment.

Parameters -> (map)

These key-value pairs define properties associated with the column.

key -> (string)

value -> (string)

ViewOriginalText -> (string)

Included for Apache Hive compatibility. Not used in the normal course of Glue operations. If the table is a `VIRTUAL_VIEW` , certain Athena configuration encoded in base64.

ViewExpandedText -> (string)

Included for Apache Hive compatibility. Not used in the normal course of Glue operations.

TableType -> (string)

The type of this table. Glue will create tables with the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.

Glue related table types:

EXTERNAL_TABLE

Hive compatible attribute - indicates a non-Hive managed table.

GOVERNED

Used by Lake Formation. The Glue Data Catalog understands `GOVERNED` .

Parameters -> (map)

These key-value pairs define properties associated with the table.

key -> (string)

value -> (string)

CreatedBy -> (string)

The person or entity who created the table.

IsRegisteredWithLakeFormation -> (boolean)

Indicates whether the table has been registered with Lake Formation.

TargetTable -> (structure)

A `TableIdentifier` structure that describes a target table for resource linking.

CatalogId -> (string)

The ID of the Data Catalog in which the table resides.

DatabaseName -> (string)

The name of the catalog database that contains the target table.

Name -> (string)

The name of the target table.

Region -> (string)

Region of the target table.

CatalogId -> (string)

The ID of the Data Catalog in which the table resides.

VersionId -> (string)

The ID of the table version.

FederatedTable -> (structure)

A `FederatedTable` structure that references an entity outside the Glue Data Catalog.

Identifier -> (string)

A unique identifier for the federated table.

DatabaseIdentifier -> (string)

A unique identifier for the federated database.

ConnectionName -> (string)

The name of the connection to the external metastore.

ViewDefinition -> (structure)

A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.

IsProtected -> (boolean)

You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engineâs documentation to understand the guarantees provided, if any.

Definer -> (string)

The definer of a view in SQL.

SubObjects -> (list)

A list of table Amazon Resource Names (ARNs).

(string)

Representations -> (list)

A list of representations.

(structure)

A structure that contains the dialect of the view, and the query that defines the view.

Dialect -> (string)

The dialect of the query engine.

DialectVersion -> (string)

The version of the dialect of the query engine. For example, 3.0.0.

ViewOriginalText -> (string)

The `SELECT` query provided by the customer during `CREATE VIEW DDL` . This SQL is not used during a query on a view (`ViewExpandedText` is used instead). `ViewOriginalText` is used for cases like `SHOW CREATE VIEW` where users want to see the original DDL command that created the view.

ViewExpandedText -> (string)

The expanded SQL for the view. This SQL is used by engines while processing a query on a view. Engines may perform operations during view creation to transform `ViewOriginalText` to `ViewExpandedText` . For example:

- Fully qualified identifiers: `SELECT * from table1 -> SELECT * from db1.table1`

ValidationConnection -> (string)

The name of the connection to be used to validate the specific representation of the view.

IsStale -> (boolean)

Dialects marked as stale are no longer valid and must be updated before they can be queried in their respective query engines.

IsMultiDialectView -> (boolean)

Specifies whether the view supports the SQL dialects of one or more different query engines and can therefore be read by those engines.

Status -> (structure)

A structure containing information about the state of an asynchronous change to a table.

RequestedBy -> (string)

The ARN of the user who requested the asynchronous change.

UpdatedBy -> (string)

The ARN of the user to last manually alter the asynchronous change (requesting cancellation, etc).

RequestTime -> (timestamp)

An ISO 8601 formatted date string indicating the time that the change was initiated.

UpdateTime -> (timestamp)

An ISO 8601 formatted date string indicating the time that the state was last updated.

Action -> (string)

Indicates which action was called on the table, currently only `CREATE` or `UPDATE` .

State -> (string)

A generic status for the change in progress, such as QUEUED, IN_PROGRESS, SUCCESS, or FAILED.

Error -> (structure)

An error that will only appear when the state is âFAILEDâ. This is a parent level exception message, there may be different `Error` s for each dialect.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

Details -> (structure)

A `StatusDetails` object with information about the requested change.

RequestedChange -> (structure)

A `Table` object representing the requested changes.

Name -> (string)

The table name. For Hive compatibility, this must be entirely lowercase.

DatabaseName -> (string)

The name of the database where the table metadata resides. For Hive compatibility, this must be all lowercase.

Description -> (string)

A description of the table.

Owner -> (string)

The owner of the table.

CreateTime -> (timestamp)

The time when the table definition was created in the Data Catalog.

UpdateTime -> (timestamp)

The last time that the table was updated.

LastAccessTime -> (timestamp)

The last time that the table was accessed. This is usually taken from HDFS, and might not be reliable.

LastAnalyzedTime -> (timestamp)

The last time that column statistics were computed for this table.

Retention -> (integer)

The retention time for this table.

StorageDescriptor -> (structure)

A storage descriptor containing information about the physical storage of this table.

Columns -> (list)

A list of the `Columns` in the table.

(structure)

A column in a `Table` .

Name -> (string)

The name of the `Column` .

Type -> (string)

The data type of the `Column` .

Comment -> (string)

A free-form text comment.

Parameters -> (map)

These key-value pairs define properties associated with the column.

key -> (string)

value -> (string)

Location -> (string)

The physical location of the table. By default, this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.

AdditionalLocations -> (list)

A list of locations that point to the path where a Delta table is located.

(string)

InputFormat -> (string)

The input format: `SequenceFileInputFormat` (binary), or `TextInputFormat` , or a custom format.

OutputFormat -> (string)

The output format: `SequenceFileOutputFormat` (binary), or `IgnoreKeyTextOutputFormat` , or a custom format.

Compressed -> (boolean)

`True` if the data in the table is compressed, or `False` if not.

NumberOfBuckets -> (integer)

Must be specified if the table contains any dimension columns.

SerdeInfo -> (structure)

The serialization/deserialization (SerDe) information.

Name -> (string)

Name of the SerDe.

SerializationLibrary -> (string)

Usually the class that implements the SerDe. An example is `org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe` .

Parameters -> (map)

These key-value pairs define initialization parameters for the SerDe.

key -> (string)

value -> (string)

BucketColumns -> (list)

A list of reducer grouping columns, clustering columns, and bucketing columns in the table.

(string)

SortColumns -> (list)

A list specifying the sort order of each bucket in the table.

(structure)

Specifies the sort order of a sorted column.

Column -> (string)

The name of the column.

SortOrder -> (integer)

Indicates that the column is sorted in ascending order (`== 1` ), or in descending order (`==0` ).

Parameters -> (map)

The user-supplied properties in key-value form.

key -> (string)

value -> (string)

SkewedInfo -> (structure)

The information about values that appear frequently in a column (skewed values).

SkewedColumnNames -> (list)

A list of names of columns that contain skewed values.

(string)

SkewedColumnValues -> (list)

A list of values that appear so frequently as to be considered skewed.

(string)

SkewedColumnValueLocationMaps -> (map)

A mapping of skewed values to the columns that contain them.

key -> (string)

value -> (string)

StoredAsSubDirectories -> (boolean)

`True` if the table data is stored in subdirectories, or `False` if not.

SchemaReference -> (structure)

An object that references a schema stored in the Glue Schema Registry.

When creating a table, you can pass an empty list of columns for the schema, and instead use a schema reference.

SchemaId -> (structure)

A structure that contains schema identity fields. Either this or the `SchemaVersionId` has to be provided.

SchemaArn -> (string)

The Amazon Resource Name (ARN) of the schema. One of `SchemaArn` or `SchemaName` has to be provided.

SchemaName -> (string)

The name of the schema. One of `SchemaArn` or `SchemaName` has to be provided.

RegistryName -> (string)

The name of the schema registry that contains the schema.

SchemaVersionId -> (string)

The unique ID assigned to a version of the schema. Either this or the `SchemaId` has to be provided.

SchemaVersionNumber -> (long)

The version number of the schema.

PartitionKeys -> (list)

A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

When you create a table used by Amazon Athena, and you do not specify any `partitionKeys` , you must at least set the value of `partitionKeys` to an empty list. For example:

`"PartitionKeys": []`

(structure)

A column in a `Table` .

Name -> (string)

The name of the `Column` .

Type -> (string)

The data type of the `Column` .

Comment -> (string)

A free-form text comment.

Parameters -> (map)

These key-value pairs define properties associated with the column.

key -> (string)

value -> (string)

ViewOriginalText -> (string)

Included for Apache Hive compatibility. Not used in the normal course of Glue operations. If the table is a `VIRTUAL_VIEW` , certain Athena configuration encoded in base64.

ViewExpandedText -> (string)

Included for Apache Hive compatibility. Not used in the normal course of Glue operations.

TableType -> (string)

The type of this table. Glue will create tables with the `EXTERNAL_TABLE` type. Other services, such as Athena, may create tables with additional table types.

Glue related table types:

EXTERNAL_TABLE

Hive compatible attribute - indicates a non-Hive managed table.

GOVERNED

Used by Lake Formation. The Glue Data Catalog understands `GOVERNED` .

Parameters -> (map)

These key-value pairs define properties associated with the table.

key -> (string)

value -> (string)

CreatedBy -> (string)

The person or entity who created the table.

IsRegisteredWithLakeFormation -> (boolean)

Indicates whether the table has been registered with Lake Formation.

TargetTable -> (structure)

A `TableIdentifier` structure that describes a target table for resource linking.

CatalogId -> (string)

The ID of the Data Catalog in which the table resides.

DatabaseName -> (string)

The name of the catalog database that contains the target table.

Name -> (string)

The name of the target table.

Region -> (string)

Region of the target table.

CatalogId -> (string)

The ID of the Data Catalog in which the table resides.

VersionId -> (string)

The ID of the table version.

FederatedTable -> (structure)

A `FederatedTable` structure that references an entity outside the Glue Data Catalog.

Identifier -> (string)

A unique identifier for the federated table.

DatabaseIdentifier -> (string)

A unique identifier for the federated database.

ConnectionName -> (string)

The name of the connection to the external metastore.

ViewDefinition -> (structure)

A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.

IsProtected -> (boolean)

You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engineâs documentation to understand the guarantees provided, if any.

Definer -> (string)

The definer of a view in SQL.

SubObjects -> (list)

A list of table Amazon Resource Names (ARNs).

(string)

Representations -> (list)

A list of representations.

(structure)

A structure that contains the dialect of the view, and the query that defines the view.

Dialect -> (string)

The dialect of the query engine.

DialectVersion -> (string)

The version of the dialect of the query engine. For example, 3.0.0.

ViewOriginalText -> (string)

The `SELECT` query provided by the customer during `CREATE VIEW DDL` . This SQL is not used during a query on a view (`ViewExpandedText` is used instead). `ViewOriginalText` is used for cases like `SHOW CREATE VIEW` where users want to see the original DDL command that created the view.

ViewExpandedText -> (string)

The expanded SQL for the view. This SQL is used by engines while processing a query on a view. Engines may perform operations during view creation to transform `ViewOriginalText` to `ViewExpandedText` . For example:

- Fully qualified identifiers: `SELECT * from table1 -> SELECT * from db1.table1`

ValidationConnection -> (string)

The name of the connection to be used to validate the specific representation of the view.

IsStale -> (boolean)

Dialects marked as stale are no longer valid and must be updated before they can be queried in their respective query engines.

IsMultiDialectView -> (boolean)

Specifies whether the view supports the SQL dialects of one or more different query engines and can therefore be read by those engines.

Status -> (structure)

A structure containing information about the state of an asynchronous change to a table.

RequestedBy -> (string)

The ARN of the user who requested the asynchronous change.

UpdatedBy -> (string)

The ARN of the user to last manually alter the asynchronous change (requesting cancellation, etc).

RequestTime -> (timestamp)

An ISO 8601 formatted date string indicating the time that the change was initiated.

UpdateTime -> (timestamp)

An ISO 8601 formatted date string indicating the time that the state was last updated.

Action -> (string)

Indicates which action was called on the table, currently only `CREATE` or `UPDATE` .

State -> (string)

A generic status for the change in progress, such as QUEUED, IN_PROGRESS, SUCCESS, or FAILED.

Error -> (structure)

An error that will only appear when the state is âFAILEDâ. This is a parent level exception message, there may be different `Error` s for each dialect.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

Details -> (structure)

A `StatusDetails` object with information about the requested change.

( â¦ recursive â¦ )ViewValidations -> (list)

A list of `ViewValidation` objects that contain information for an analytical engine to validate a view.

(structure)

A structure that contains information for an analytical engine to validate a view, prior to persisting the view metadata. Used in the case of direct `UpdateTable` or `CreateTable` API calls.

Dialect -> (string)

The dialect of the query engine.

DialectVersion -> (string)

The version of the dialect of the query engine. For example, 3.0.0.

ViewValidationText -> (string)

The `SELECT` query that defines the view, as provided by the customer.

UpdateTime -> (timestamp)

The time of the last update.

State -> (string)

The state of the validation.

Error -> (structure)

An error associated with the validation.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

ViewValidations -> (list)

A list of `ViewValidation` objects that contain information for an analytical engine to validate a view.

(structure)

A structure that contains information for an analytical engine to validate a view, prior to persisting the view metadata. Used in the case of direct `UpdateTable` or `CreateTable` API calls.

Dialect -> (string)

The dialect of the query engine.

DialectVersion -> (string)

The version of the dialect of the query engine. For example, 3.0.0.

ViewValidationText -> (string)

The `SELECT` query that defines the view, as provided by the customer.

UpdateTime -> (timestamp)

The time of the last update.

State -> (string)

The state of the validation.

Error -> (structure)

An error associated with the validation.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

AuthorizedColumns -> (list)

A list of column names that the user has been granted access to.

(string)

IsRegisteredWithLakeFormation -> (boolean)

A Boolean value that indicates whether the partition location is registered with Lake Formation.

CellFilters -> (list)

A list of column row filters.

(structure)

A filter that uses both column-level and row-level filtering.

ColumnName -> (string)

A string containing the name of the column.

RowFilterExpression -> (string)

A string containing the row-level filter expression.

QueryAuthorizationId -> (string)

A cryptographically generated query identifier generated by Glue or Lake Formation.

IsMultiDialectView -> (boolean)

Specifies whether the view supports the SQL dialects of one or more different query engines and can therefore be read by those engines.

ResourceArn -> (string)

The resource ARN of the parent resource extracted from the request.

IsProtected -> (boolean)

A flag that instructs the engine not to push user-provided operations into the logical plan of the view during query planning. However, if set this flag does not guarantee that the engine will comply. Refer to the engineâs documentation to understand the guarantees provided, if any.

Permissions -> (list)

The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.

(string)

RowFilter -> (string)

The filter that applies to the table. For example when applying the filter in SQL, it would go in the `WHERE` clause and can be evaluated by using an `AND` operator with any other predicates applied by the user querying the table.