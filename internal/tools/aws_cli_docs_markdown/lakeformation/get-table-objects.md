# get-table-objectsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-table-objects.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-table-objects.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lakeformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/index.html#cli-aws-lakeformation) ]

# get-table-objects

## Description

Returns the set of Amazon S3 objects that make up the specified governed table. A transaction ID or timestamp can be specified for time-travel queries.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GetTableObjects)

## Synopsis

```
get-table-objects
[--catalog-id <value>]
--database-name <value>
--table-name <value>
[--transaction-id <value>]
[--query-as-of-time <value>]
[--partition-predicate <value>]
[--max-results <value>]
[--next-token <value>]
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

The catalog containing the governed table. Defaults to the callerâs account.

`--database-name` (string)

The database containing the governed table.

`--table-name` (string)

The governed table for which to retrieve objects.

`--transaction-id` (string)

The transaction ID at which to read the governed table contents. If this transaction has aborted, an error is returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with `QueryAsOfTime` .

`--query-as-of-time` (timestamp)

The time as of when to read the governed table contents. If not set, the most recent transaction commit time is used. Cannot be specified along with `TransactionId` .

`--partition-predicate` (string)

A predicate to filter the objects returned based on the partition keys defined in the governed table.

- The comparison operators supported are: =, >, <, >=, <=
- The logical operators supported are: AND
- The data types supported are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ssâ), string and decimal.

`--max-results` (integer)

Specifies how many values to return in a page.

`--next-token` (string)

A continuation token if this is not the first call to retrieve these objects.

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

**To list objects of governed table**

The following `get-table-objects` example returns the set of Amazon S3 objects that make up the specified governed table.

```
aws lakeformation get-table-objects \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "012345678901",
    "DatabaseName": "tpc",
    "TableName": "dl_tpc_household_demographics_gov",
    "QueryAsOfTime": "2022-08-10T15:00:00"
}
```

Output:

```
{
    "Objects": [{
        "PartitionValues": [],
        "Objects": [{
            "Uri": "s3://lf-data-lake-012345678901/target/dl_tpc_household_demographics_gov/run-unnamed-1-part-block-0-r-00000-snappy-ff26b17504414fe88b302cd795eabd00.parquet",
            "ETag": "12345b1fc50a316b149b4e1f21a73800",
            "Size": 43235
        }]
    }]
}
```

For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html) in the *AWS Lake Formation Developer Guide*.

## Output

Objects -> (list)

A list of objects organized by partition keys.

(structure)

A structure containing a list of partition values and table objects.

PartitionValues -> (list)

A list of partition values.

(string)

Objects -> (list)

A list of table objects

(structure)

Specifies the details of a governed table.

Uri -> (string)

The Amazon S3 location of the object.

ETag -> (string)

The Amazon S3 ETag of the object. Returned by `GetTableObjects` for validation and used to identify changes to the underlying data.

Size -> (long)

The size of the Amazon S3 object in bytes.

NextToken -> (string)

A continuation token indicating whether additional data is available.