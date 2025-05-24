# update-integration-table-propertiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-integration-table-properties.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-integration-table-properties.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-integration-table-properties

## Description

This API is used to provide optional override properties for the tables that need to be replicated. These properties can include properties for filtering and partitioning for the source and target tables. To set both source and target properties the same API need to be invoked with the Glue connection ARN as `ResourceArn` with `SourceTableConfig` , and the Glue database ARN as `ResourceArn` with `TargetTableConfig` respectively.

The override will be reflected across all the integrations using same `ResourceArn` and source table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateIntegrationTableProperties)

## Synopsis

```
update-integration-table-properties
--resource-arn <value>
--table-name <value>
[--source-table-config <value>]
[--target-table-config <value>]
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

The connection ARN of the source, or the database ARN of the target.

`--table-name` (string)

The name of the table to be replicated.

`--source-table-config` (structure)

A structure for the source table configuration.

Fields -> (list)

A list of fields used for column-level filtering. Currently unsupported.

(string)

FilterPredicate -> (string)

A condition clause used for row-level filtering. Currently unsupported.

PrimaryKey -> (list)

Provide the primary key set for this table. Currently supported specifically for SAP `EntityOf` entities upon request. Contact Amazon Web Services Support to make this feature available.

(string)

RecordUpdateField -> (string)

Incremental pull timestamp-based field. Currently unsupported.

Shorthand Syntax:

```
Fields=string,string,FilterPredicate=string,PrimaryKey=string,string,RecordUpdateField=string
```

JSON Syntax:

```
{
  "Fields": ["string", ...],
  "FilterPredicate": "string",
  "PrimaryKey": ["string", ...],
  "RecordUpdateField": "string"
}
```

`--target-table-config` (structure)

A structure for the target table configuration.

UnnestSpec -> (string)

Specifies how nested objects are flattened to top-level elements. Valid values are: âTOPLEVELâ, âFULLâ, or âNOUNNESTâ.

PartitionSpec -> (list)

Determines the file layout on the target.

(structure)

A structure that describes how data is partitioned on the target.

FieldName -> (string)

The field name used to partition data on the target. Avoid using columns that have unique values for each row (for example, LastModifiedTimestamp, SystemModTimeStamp) as the partition column. These columns are not suitable for partitioning because they create a large number of small partitions, which can lead to performance issues.

FunctionSpec -> (string)

Specifies the function used to partition data on the target. The only accepted value for this parameter is âidentityâ (string). The âidentityâ function ensures that the data partitioning on the target follows the same scheme as the source. In other words, the partitioning structure of the source data is preserved in the target destination.

TargetTableName -> (string)

The optional name of a target table.

Shorthand Syntax:

```
UnnestSpec=string,PartitionSpec=[{FieldName=string,FunctionSpec=string},{FieldName=string,FunctionSpec=string}],TargetTableName=string
```

JSON Syntax:

```
{
  "UnnestSpec": "TOPLEVEL"|"FULL"|"NOUNNEST",
  "PartitionSpec": [
    {
      "FieldName": "string",
      "FunctionSpec": "string"
    }
    ...
  ],
  "TargetTableName": "string"
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

None