# get-configured-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-configured-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/get-configured-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# get-configured-table

## Description

Retrieves a configured table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/GetConfiguredTable)

## Synopsis

```
get-configured-table
--configured-table-identifier <value>
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

The unique ID for the configured table to retrieve.

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

configuredTable -> (structure)

The retrieved configured table.

id -> (string)

The unique ID for the configured table.

arn -> (string)

The unique ARN for the configured table.

name -> (string)

A name for the configured table.

description -> (string)

A description for the configured table.

tableReference -> (tagged union structure)

The table that this configured table represents.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `glue`, `snowflake`, `athena`.

glue -> (structure)

If present, a reference to the Glue table referred to by this table reference.

tableName -> (string)

The name of the Glue table.

databaseName -> (string)

The name of the database the Glue table belongs to.

snowflake -> (structure)

If present, a reference to the Snowflake table referred to by this table reference.

secretArn -> (string)

The secret ARN of the Snowflake table reference.

accountIdentifier -> (string)

The account identifier for the Snowflake table reference.

databaseName -> (string)

The name of the database the Snowflake table belongs to.

tableName -> (string)

The name of the Snowflake table.

schemaName -> (string)

The schema name of the Snowflake table reference.

tableSchema -> (tagged union structure)

The schema of the Snowflake table.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (list)

The schema of a Snowflake table.

(structure)

The Snowflake table schema.

columnName -> (string)

The column name.

columnType -> (string)

The columnâs data type. Supported data types: `ARRAY` , `BIGINT` , `BOOLEAN` , `CHAR` , `DATE` , `DECIMAL` , `DOUBLE` , `DOUBLE PRECISION` , `FLOAT` , `FLOAT4` , `INT` , `INTEGER` , `MAP` , `NUMERIC` , `NUMBER` , `REAL` , `SMALLINT` , `STRING` , `TIMESTAMP` , `TIMESTAMP_LTZ` , `TIMESTAMP_NTZ` , `DATETIME` , `TINYINT` , `VARCHAR` , `TEXT` , `CHARACTER` .

athena -> (structure)

If present, a reference to the Athena table referred to by this table reference.

workGroup -> (string)

The workgroup of the Athena table reference.

outputLocation -> (string)

The output location for the Athena table.

databaseName -> (string)

The database name.

tableName -> (string)

The table reference.

createTime -> (timestamp)

The time the configured table was created.

updateTime -> (timestamp)

The time the configured table was last updated

analysisRuleTypes -> (list)

The types of analysis rules associated with this configured table. Currently, only one analysis rule may be associated with a configured table.

(string)

analysisMethod -> (string)

The analysis method for the configured table.

`DIRECT_QUERY` allows SQL queries to be run directly on this table.

`DIRECT_JOB` allows PySpark jobs to be run directly on this table.

`MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.

allowedColumns -> (list)

The columns within the underlying Glue table that can be utilized within collaborations.

(string)

selectedAnalysisMethods -> (list)

The selected analysis methods for the configured table.

(string)