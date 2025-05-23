# execute-statementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/execute-statement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/execute-statement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/index.html#cli-aws-rds-data) ]

# execute-statement

## Description

Runs a SQL statement against a database.

### Note

If a call isnât part of a transaction because it doesnât include the `transactionID` parameter, changes that result from the call are committed automatically.

If the binary response data from the database is more than 1 MB, the call is terminated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-data-2018-08-01/ExecuteStatement)

## Synopsis

```
execute-statement
--resource-arn <value>
--secret-arn <value>
--sql <value>
[--database <value>]
[--schema <value>]
[--parameters <value>]
[--transaction-id <value>]
[--include-result-metadata | --no-include-result-metadata]
[--continue-after-timeout | --no-continue-after-timeout]
[--result-set-options <value>]
[--format-records-as <value>]
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

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.

`--secret-arn` (string)

The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.

For information about creating the secret, see [Create a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html) .

`--sql` (string)

The SQL statement to run.

`--database` (string)

The name of the database.

`--schema` (string)

The name of the database schema.

### Note

Currently, the `schema` parameter isnât supported.

`--parameters` (list)

The parameters for the SQL statement.

### Note

Array parameters are not supported.

(structure)

A parameter used in a SQL statement.

name -> (string)

The name of the parameter.

value -> (tagged union structure)

The value of the parameter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `isNull`, `booleanValue`, `longValue`, `doubleValue`, `stringValue`, `blobValue`, `arrayValue`.

isNull -> (boolean)

A NULL value.

booleanValue -> (boolean)

A value of Boolean data type.

longValue -> (long)

A value of long data type.

doubleValue -> (double)

A value of double data type.

stringValue -> (string)

A value of string data type.

blobValue -> (blob)

A value of BLOB data type.

arrayValue -> (tagged union structure)

An array of values.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

(tagged union structure)

Contains an array.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

( â¦ recursive â¦ )

typeHint -> (string)

A hint that specifies the correct object type for data type mapping. Possible values are as follows:

- `DATE` - The corresponding `String` parameter value is sent as an object of `DATE` type to the database. The accepted format is `YYYY-MM-DD` .
- `DECIMAL` - The corresponding `String` parameter value is sent as an object of `DECIMAL` type to the database.
- `JSON` - The corresponding `String` parameter value is sent as an object of `JSON` type to the database.
- `TIME` - The corresponding `String` parameter value is sent as an object of `TIME` type to the database. The accepted format is `HH:MM:SS[.FFF]` .
- `TIMESTAMP` - The corresponding `String` parameter value is sent as an object of `TIMESTAMP` type to the database. The accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]` .
- `UUID` - The corresponding `String` parameter value is sent as an object of `UUID` type to the database.

JSON Syntax:

```
[
  {
    "name": "string",
    "value": {
      "isNull": true|false,
      "booleanValue": true|false,
      "longValue": long,
      "doubleValue": double,
      "stringValue": "string",
      "blobValue": blob,
      "arrayValue": {
        "booleanValues": [true|false, ...],
        "longValues": [long, ...],
        "doubleValues": [double, ...],
        "stringValues": ["string", ...],
        "arrayValues": [
          {
            "booleanValues": [true|false, ...],
            "longValues": [long, ...],
            "doubleValues": [double, ...],
            "stringValues": ["string", ...],
            "arrayValues": [
              { ... recursive ... }
              ...
            ]
          }
          ...
        ]
      }
    },
    "typeHint": "JSON"|"UUID"|"TIMESTAMP"|"DATE"|"TIME"|"DECIMAL"
  }
  ...
]
```

`--transaction-id` (string)

The identifier of a transaction that was started by using the `BeginTransaction` operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.

If the SQL statement is not part of a transaction, donât set this parameter.

`--include-result-metadata` | `--no-include-result-metadata` (boolean)

A value that indicates whether to include metadata in the results.

`--continue-after-timeout` | `--no-continue-after-timeout` (boolean)

A value that indicates whether to continue running the statement after the call times out. By default, the statement stops running when the call times out.

### Note

For DDL statements, we recommend continuing to run the statement after the call times out. When a DDL statement terminates before it is finished running, it can result in errors and possibly corrupted data structures.

`--result-set-options` (structure)

Options that control how the result set is returned.

decimalReturnType -> (string)

A value that indicates how a field of `DECIMAL` type is represented in the response. The value of `STRING` , the default, specifies that it is converted to a String value. The value of `DOUBLE_OR_LONG` specifies that it is converted to a Long value if its scale is 0, or to a Double value otherwise.

### Note

Conversion to Double or Long can result in roundoff errors due to precision loss. We recommend converting to String, especially when working with currency values.

longReturnType -> (string)

A value that indicates how a field of `LONG` type is represented. Allowed values are `LONG` and `STRING` . The default is `LONG` . Specify `STRING` if the length or precision of numeric values might cause truncation or rounding errors.

Shorthand Syntax:

```
decimalReturnType=string,longReturnType=string
```

JSON Syntax:

```
{
  "decimalReturnType": "STRING"|"DOUBLE_OR_LONG",
  "longReturnType": "STRING"|"LONG"
}
```

`--format-records-as` (string)

A value that indicates whether to format the result set as a single JSON string. This parameter only applies to `SELECT` statements and is ignored for other types of statements. Allowed values are `NONE` and `JSON` . The default value is `NONE` . The result is returned in the `formattedRecords` field.

For usage information about the JSON format for result sets, see [Using the Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide* .

Possible values:

- `NONE`
- `JSON`

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

**Example 1: To execute a SQL statement that is part of a transaction**

The following `execute-statement` example runs a SQL statement that is part of a transaction.

```
aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster" \
    --database "mydb" \
    --secret-arn "arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret" \
    --sql "update mytable set quantity=5 where id=201" \
    --transaction-id "ABC1234567890xyz"
```

Output:

```
{
    "numberOfRecordsUpdated": 1
}
```

**Example 2: To execute a SQL statement with parameters**

The following `execute-statement` example runs a SQL statement with parameters.

```
aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster" \
    --database "mydb" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret" \
    --sql "insert into mytable values (:id, :val)" \
    --parameters "[{\"name\": \"id\", \"value\": {\"longValue\": 1}},{\"name\": \"val\", \"value\": {\"stringValue\": \"value1\"}}]"
```

Output:

```
{
    "numberOfRecordsUpdated": 1
}
```

For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon RDS User Guide*.

## Output

records -> (list)

The records returned by the SQL statement. This field is blank if the `formatRecordsAs` parameter is set to `JSON` .

(list)

(tagged union structure)

Contains a value.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `isNull`, `booleanValue`, `longValue`, `doubleValue`, `stringValue`, `blobValue`, `arrayValue`.

isNull -> (boolean)

A NULL value.

booleanValue -> (boolean)

A value of Boolean data type.

longValue -> (long)

A value of long data type.

doubleValue -> (double)

A value of double data type.

stringValue -> (string)

A value of string data type.

blobValue -> (blob)

A value of BLOB data type.

arrayValue -> (tagged union structure)

An array of values.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

(tagged union structure)

Contains an array.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

( â¦ recursive â¦ )

columnMetadata -> (list)

Metadata for the columns included in the results. This field is blank if the `formatRecordsAs` parameter is set to `JSON` .

(structure)

Contains the metadata for a column.

name -> (string)

The name of the column.

type -> (integer)

The type of the column.

typeName -> (string)

The database-specific data type of the column.

label -> (string)

The label for the column.

schemaName -> (string)

The name of the schema that owns the table that includes the column.

tableName -> (string)

The name of the table that includes the column.

isAutoIncrement -> (boolean)

A value that indicates whether the column increments automatically.

isSigned -> (boolean)

A value that indicates whether an integer column is signed.

isCurrency -> (boolean)

A value that indicates whether the column contains currency values.

isCaseSensitive -> (boolean)

A value that indicates whether the column is case-sensitive.

nullable -> (integer)

A value that indicates whether the column is nullable.

precision -> (integer)

The precision value of a decimal number column.

scale -> (integer)

The scale value of a decimal number column.

arrayBaseColumnType -> (integer)

The type of the column.

numberOfRecordsUpdated -> (long)

The number of records updated by the request.

generatedFields -> (list)

Values for fields generated during a DML request.

### Note

The `generatedFields` data isnât supported by Aurora PostgreSQL. To get the values of generated fields, use the `RETURNING` clause. For more information, see [Returning Data From Modified Rows](https://www.postgresql.org/docs/10/dml-returning.html) in the PostgreSQL documentation.

(tagged union structure)

Contains a value.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `isNull`, `booleanValue`, `longValue`, `doubleValue`, `stringValue`, `blobValue`, `arrayValue`.

isNull -> (boolean)

A NULL value.

booleanValue -> (boolean)

A value of Boolean data type.

longValue -> (long)

A value of long data type.

doubleValue -> (double)

A value of double data type.

stringValue -> (string)

A value of string data type.

blobValue -> (blob)

A value of BLOB data type.

arrayValue -> (tagged union structure)

An array of values.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

(tagged union structure)

Contains an array.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValues`, `longValues`, `doubleValues`, `stringValues`, `arrayValues`.

booleanValues -> (list)

An array of Boolean values.

(boolean)

longValues -> (list)

An array of integers.

(long)

doubleValues -> (list)

An array of floating-point numbers.

(double)

stringValues -> (list)

An array of strings.

(string)

arrayValues -> (list)

An array of arrays.

( â¦ recursive â¦ )

formattedRecords -> (string)

A string value that represents the result set of a `SELECT` statement in JSON format. This value is only present when the `formatRecordsAs` parameter is set to `JSON` .

The size limit for this field is currently 10 MB. If the JSON-formatted string representing the result set requires more than 10 MB, the call returns an error.