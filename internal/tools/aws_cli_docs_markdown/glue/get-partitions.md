# get-partitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-partitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-partitions

## Description

Retrieves information about the partitions in a table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartitions)

`get-partitions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Partitions`

## Synopsis

```
get-partitions
[--catalog-id <value>]
--database-name <value>
--table-name <value>
[--expression <value>]
[--segment <value>]
[--exclude-column-schema | --no-exclude-column-schema]
[--transaction-id <value>]
[--query-as-of-time <value>]
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

`--catalog-id` (string)

The ID of the Data Catalog where the partitions in question reside. If none is provided, the Amazon Web Services account ID is used by default.

`--database-name` (string)

The name of the catalog database where the partitions reside.

`--table-name` (string)

The name of the partitionsâ table.

`--expression` (string)

An expression that filters the partitions to be returned.

The expression uses SQL syntax similar to the SQL `WHERE` filter clause. The SQL statement parser [JSQLParser](http://jsqlparser.sourceforge.net/home.php) parses the expression.

*Operators* : The following are the operators that you can use in the `Expression` API call:

=

Checks whether the values of the two operands are equal; if yes, then the condition becomes true.

Example: Assume âvariable aâ holds 10 and âvariable bâ holds 20.

(a = b) is not true.

< >

Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.

Example: (a < > b) is true.

>

Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.

Example: (a > b) is not true.

<

Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.

Example: (a < b) is true.

>=

Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.

Example: (a >= b) is not true.

<=

Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.

Example: (a <= b) is true.

AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL

Logical operators.

*Supported Partition Key Types* : The following are the supported partition keys.

- `string`
- `date`
- `timestamp`
- `int`
- `bigint`
- `long`
- `tinyint`
- `smallint`
- `decimal`

If an type is encountered that is not valid, an exception is thrown.

The following list shows the valid operators on each type. When you define a crawler, the `partitionKey` type is created as a `STRING` , to be compatible with the catalog partitions.

*Sample API Call* :

`--segment` (structure)

The segment of the tableâs partitions to scan in this request.

SegmentNumber -> (integer)

The zero-based index number of the segment. For example, if the total number of segments is 4, `SegmentNumber` values range from 0 through 3.

TotalSegments -> (integer)

The total number of segments.

Shorthand Syntax:

```
SegmentNumber=integer,TotalSegments=integer
```

JSON Syntax:

```
{
  "SegmentNumber": integer,
  "TotalSegments": integer
}
```

`--exclude-column-schema` | `--no-exclude-column-schema` (boolean)

When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the problem of a large response by not returning duplicate data.

`--transaction-id` (string)

The transaction ID at which to read the partition contents.

`--query-as-of-time` (timestamp)

The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId` .

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

## Output

Partitions -> (list)

A list of requested partitions.

(structure)

Represents a slice of table data.

Values -> (list)

The values of the partition.

(string)

DatabaseName -> (string)

The name of the catalog database in which to create the partition.

TableName -> (string)

The name of the database table in which to create the partition.

CreationTime -> (timestamp)

The time at which the partition was created.

LastAccessTime -> (timestamp)

The last time at which the partition was accessed.

StorageDescriptor -> (structure)

Provides information about the physical location where the partition is stored.

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

Parameters -> (map)

These key-value pairs define partition parameters.

key -> (string)

value -> (string)

LastAnalyzedTime -> (timestamp)

The last time at which column statistics were computed for this partition.

CatalogId -> (string)

The ID of the Data Catalog in which the partition resides.

NextToken -> (string)

A continuation token, if the returned list of partitions does not include the last one.