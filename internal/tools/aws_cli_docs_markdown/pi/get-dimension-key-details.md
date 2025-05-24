# get-dimension-key-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-dimension-key-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-dimension-key-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html#cli-aws-pi) ]

# get-dimension-key-details

## Description

Get the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, `GetDimensionKeyDetails` retrieves the full text of the dimension `db.sql.statement` associated with this ID. This operation is useful because `GetResourceMetrics` and `DescribeDimensionKeys` donât support retrieval of large SQL statement text, lock snapshots, and execution plans.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/GetDimensionKeyDetails)

## Synopsis

```
get-dimension-key-details
--service-type <value>
--identifier <value>
--group <value>
--group-identifier <value>
[--requested-dimensions <value>]
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

`--service-type` (string)

The Amazon Web Services service for which Performance Insights returns data. The only valid value is `RDS` .

Possible values:

- `RDS`
- `DOCDB`

`--identifier` (string)

The ID for a data source from which to gather dimension data. This ID must be immutable and unique within an Amazon Web Services Region. When a DB instance is the data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X` .

`--group` (string)

The name of the dimension group. Performance Insights searches the specified group for the dimension group ID. The following group name values are valid:

- `db.execution_plan` (Amazon RDS and Aurora only)
- `db.lock_snapshot` (Aurora only)
- `db.query` (Amazon DocumentDB only)
- `db.sql` (Amazon RDS and Aurora only)

`--group-identifier` (string)

The ID of the dimension group from which to retrieve dimension details. For dimension group `db.sql` , the group ID is `db.sql.id` . The following group ID values are valid:

- `db.execution_plan.id` for dimension group `db.execution_plan` (Aurora and RDS only)
- `db.sql.id` for dimension group `db.sql` (Aurora and RDS only)
- `db.query.id` for dimension group `db.query` (DocumentDB only)
- For the dimension group `db.lock_snapshot` , the `GroupIdentifier` is the epoch timestamp when Performance Insights captured the snapshot, in seconds. You can retrieve this value with the `GetResourceMetrics` operation for a 1 second period.

`--requested-dimensions` (list)

A list of dimensions to retrieve the detail data for within the given dimension group. If you donât specify this parameter, Performance Insights returns all dimension data within the specified dimension group. Specify dimension names for the following dimension groups:

- `db.execution_plan` - Specify the dimension name `db.execution_plan.raw_plan` or the short dimension name `raw_plan` (Amazon RDS and Aurora only)
- `db.lock_snapshot` - Specify the dimension name `db.lock_snapshot.lock_trees` or the short dimension name `lock_trees` . (Aurora only)
- `db.sql` - Specify either the full dimension name `db.sql.statement` or the short dimension name `statement` (Aurora and RDS only).
- `db.query` - Specify either the full dimension name `db.query.statement` or the short dimension name `statement` (DocumentDB only).

(string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

Syntax:

```
"string" "string" ...
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

Dimensions -> (list)

The details for the requested dimensions.

(structure)

An object that describes the details for a specified dimension.

Value -> (string)

The value of the dimension detail data. Depending on the return status, this value is either the full or truncated SQL query for the following dimensions:

- `db.query.statement` (Amazon DocumentDB)
- `db.sql.statement` (Amazon RDS and Aurora)

Dimension -> (string)

The full name of the dimension. The full name includes the group name and key name. The following values are valid:

- `db.query.statement` (Amazon DocumentDB)
- `db.sql.statement` (Amazon RDS and Aurora)

Status -> (string)

The status of the dimension detail data. Possible values include the following:

- `AVAILABLE` - The dimension detail data is ready to be retrieved.
- `PROCESSING` - The dimension detail data isnât ready to be retrieved because more processing time is required. If the requested detail data has the status `PROCESSING` , Performance Insights returns the truncated query.
- `UNAVAILABLE` - The dimension detail data could not be collected successfully.