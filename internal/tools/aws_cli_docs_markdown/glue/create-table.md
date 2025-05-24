# create-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# create-table

## Description

Creates a new table definition in the Data Catalog.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/CreateTable)

## Synopsis

```
create-table
[--catalog-id <value>]
--database-name <value>
--table-input <value>
[--partition-indexes <value>]
[--transaction-id <value>]
[--open-table-format-input <value>]
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

The ID of the Data Catalog in which to create the `Table` . If none is supplied, the Amazon Web Services account ID is used by default.

`--database-name` (string)

The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.

`--table-input` (structure)

The `TableInput` object that defines the metadata table to create in the catalog.

Name -> (string)

The table name. For Hive compatibility, this is folded to lowercase when it is stored.

Description -> (string)

A description of the table.

Owner -> (string)

The table owner. Included for Apache Hive compatibility. Not used in the normal course of Glue operations.

LastAccessTime -> (timestamp)

The last time that the table was accessed.

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

ViewDefinition -> (structure)

A structure that contains all the information that defines the view, including the dialect or dialects for the view, and the query.

IsProtected -> (boolean)

You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engineâs documentation to understand the guarantees provided, if any.

Definer -> (string)

The definer of a view in SQL.

Representations -> (list)

A list of structures that contains the dialect of the view, and the query that defines the view.

(structure)

A structure containing details of a representation to update or create a Lake Formation view.

Dialect -> (string)

A parameter that specifies the engine type of a specific representation.

DialectVersion -> (string)

A parameter that specifies the version of the engine of a specific representation.

ViewOriginalText -> (string)

A string that represents the original SQL query that describes the view.

ValidationConnection -> (string)

The name of the connection to be used to validate the specific representation of the view.

ViewExpandedText -> (string)

A string that represents the SQL query that describes the view with expanded resource ARNs

SubObjects -> (list)

A list of base table ARNs that make up the view.

(string)

JSON Syntax:

```
{
  "Name": "string",
  "Description": "string",
  "Owner": "string",
  "LastAccessTime": timestamp,
  "LastAnalyzedTime": timestamp,
  "Retention": integer,
  "StorageDescriptor": {
    "Columns": [
      {
        "Name": "string",
        "Type": "string",
        "Comment": "string",
        "Parameters": {"string": "string"
          ...}
      }
      ...
    ],
    "Location": "string",
    "AdditionalLocations": ["string", ...],
    "InputFormat": "string",
    "OutputFormat": "string",
    "Compressed": true|false,
    "NumberOfBuckets": integer,
    "SerdeInfo": {
      "Name": "string",
      "SerializationLibrary": "string",
      "Parameters": {"string": "string"
        ...}
    },
    "BucketColumns": ["string", ...],
    "SortColumns": [
      {
        "Column": "string",
        "SortOrder": integer
      }
      ...
    ],
    "Parameters": {"string": "string"
      ...},
    "SkewedInfo": {
      "SkewedColumnNames": ["string", ...],
      "SkewedColumnValues": ["string", ...],
      "SkewedColumnValueLocationMaps": {"string": "string"
        ...}
    },
    "StoredAsSubDirectories": true|false,
    "SchemaReference": {
      "SchemaId": {
        "SchemaArn": "string",
        "SchemaName": "string",
        "RegistryName": "string"
      },
      "SchemaVersionId": "string",
      "SchemaVersionNumber": long
    }
  },
  "PartitionKeys": [
    {
      "Name": "string",
      "Type": "string",
      "Comment": "string",
      "Parameters": {"string": "string"
        ...}
    }
    ...
  ],
  "ViewOriginalText": "string",
  "ViewExpandedText": "string",
  "TableType": "string",
  "Parameters": {"string": "string"
    ...},
  "TargetTable": {
    "CatalogId": "string",
    "DatabaseName": "string",
    "Name": "string",
    "Region": "string"
  },
  "ViewDefinition": {
    "IsProtected": true|false,
    "Definer": "string",
    "Representations": [
      {
        "Dialect": "REDSHIFT"|"ATHENA"|"SPARK",
        "DialectVersion": "string",
        "ViewOriginalText": "string",
        "ValidationConnection": "string",
        "ViewExpandedText": "string"
      }
      ...
    ],
    "SubObjects": ["string", ...]
  }
}
```

`--partition-indexes` (list)

A list of partition indexes, `PartitionIndex` structures, to create in the table.

(structure)

A structure for a partition index.

Keys -> (list)

The keys for the partition index.

(string)

IndexName -> (string)

The name of the partition index.

Shorthand Syntax:

```
Keys=string,string,IndexName=string ...
```

JSON Syntax:

```
[
  {
    "Keys": ["string", ...],
    "IndexName": "string"
  }
  ...
]
```

`--transaction-id` (string)

The ID of the transaction.

`--open-table-format-input` (structure)

Specifies an `OpenTableFormatInput` structure when creating an open format table.

IcebergInput -> (structure)

Specifies an `IcebergInput` structure that defines an Apache Iceberg metadata table.

MetadataOperation -> (string)

A required metadata operation. Can only be set to `CREATE` .

Version -> (string)

The table version for the Iceberg table. Defaults to 2.

Shorthand Syntax:

```
IcebergInput={MetadataOperation=string,Version=string}
```

JSON Syntax:

```
{
  "IcebergInput": {
    "MetadataOperation": "CREATE",
    "Version": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a table for a Kinesis data stream**

The following `create-table` example creates a table in the AWS Glue Data Catalog that describes a Kinesis data stream.

```
aws glue create-table \
    --database-name tempdb \
    --table-input  '{"Name":"test-kinesis-input", "StorageDescriptor":{ \
            "Columns":[ \
                {"Name":"sensorid", "Type":"int"}, \
                {"Name":"currenttemperature", "Type":"int"}, \
                {"Name":"status", "Type":"string"}
            ], \
            "Location":"my-testing-stream", \
            "Parameters":{ \
                "typeOfData":"kinesis","streamName":"my-testing-stream", \
                "kinesisUrl":"https://kinesis.us-east-1.amazonaws.com" \
            }, \
            "SerdeInfo":{ \
                "SerializationLibrary":"org.openx.data.jsonserde.JsonSerDe"} \
        }, \
        "Parameters":{ \
            "classification":"json"} \
        }' \
    --profile my-profile \
    --endpoint https://glue.us-east-1.amazonaws.com
```

This command produces no output.

For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html) in the *AWS Glue Developer Guide*.

**Example 2: To create a table for a Kafka data store**

The following `create-table` example creates a table in the AWS Glue Data Catalog that describes a Kafka data store.

```
aws glue create-table \
    --database-name tempdb \
    --table-input  '{"Name":"test-kafka-input", "StorageDescriptor":{ \
            "Columns":[ \
                {"Name":"sensorid", "Type":"int"}, \
                {"Name":"currenttemperature", "Type":"int"}, \
                {"Name":"status", "Type":"string"}
            ], \
            "Location":"glue-topic", \
            "Parameters":{ \
                "typeOfData":"kafka","topicName":"glue-topic", \
                "connectionName":"my-kafka-connection"
            }, \
            "SerdeInfo":{ \
                "SerializationLibrary":"org.apache.hadoop.hive.serde2.OpenCSVSerde"} \
        }, \
        "Parameters":{ \
            "separatorChar":","} \
        }' \
    --profile my-profile \
    --endpoint https://glue.us-east-1.amazonaws.com
```

This command produces no output.

For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html) in the *AWS Glue Developer Guide*.

**Example 3: To create a table for a AWS S3 data store**

The following `create-table` example creates a table in the AWS Glue Data Catalog that
describes a AWS Simple Storage Service (AWS S3) data store.

```
aws glue create-table \
    --database-name tempdb \
    --table-input  '{"Name":"s3-output", "StorageDescriptor":{ \
            "Columns":[ \
                {"Name":"s1", "Type":"string"}, \
                {"Name":"s2", "Type":"int"}, \
                {"Name":"s3", "Type":"string"}
            ], \
            "Location":"s3://bucket-path/", \
            "SerdeInfo":{ \
                "SerializationLibrary":"org.openx.data.jsonserde.JsonSerDe"} \
        }, \
        "Parameters":{ \
            "classification":"json"} \
        }' \
    --profile my-profile \
    --endpoint https://glue.us-east-1.amazonaws.com
```

This command produces no output.

For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html) in the *AWS Glue Developer Guide*.

## Output

None