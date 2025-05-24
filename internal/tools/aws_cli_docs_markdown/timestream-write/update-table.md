# update-tableÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-table.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/update-table.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-write](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-write/index.html#cli-aws-timestream-write) ]

# update-table

## Description

Modifies the retention duration of the memory store and magnetic store for your Timestream table. Note that the change in retention duration takes effect immediately. For example, if the retention period of the memory store was initially set to 2 hours and then changed to 24 hours, the memory store will be capable of holding 24 hours of data, but will be populated with 24 hours of data 22 hours after this change was made. Timestream does not retrieve data from the magnetic store to populate the memory store.

See [code sample](https://docs.aws.amazon.com/timestream/latest/developerguide/code-samples.update-table.html) for details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-write-2018-11-01/UpdateTable)

## Synopsis

```
update-table
--database-name <value>
--table-name <value>
[--retention-properties <value>]
[--magnetic-store-write-properties <value>]
[--schema <value>]
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

`--database-name` (string)

The name of the Timestream database.

`--table-name` (string)

The name of the Timestream table.

`--retention-properties` (structure)

The retention duration of the memory store and the magnetic store.

MemoryStoreRetentionPeriodInHours -> (long)

The duration for which data must be stored in the memory store.

MagneticStoreRetentionPeriodInDays -> (long)

The duration for which data must be stored in the magnetic store.

Shorthand Syntax:

```
MemoryStoreRetentionPeriodInHours=long,MagneticStoreRetentionPeriodInDays=long
```

JSON Syntax:

```
{
  "MemoryStoreRetentionPeriodInHours": long,
  "MagneticStoreRetentionPeriodInDays": long
}
```

`--magnetic-store-write-properties` (structure)

Contains properties to set on the table when enabling magnetic store writes.

EnableMagneticStoreWrites -> (boolean)

A flag to enable magnetic store writes.

MagneticStoreRejectedDataLocation -> (structure)

The location to write error reports for records rejected asynchronously during magnetic store writes.

S3Configuration -> (structure)

Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.

BucketName -> (string)

The bucket name of the customer S3 bucket.

ObjectKeyPrefix -> (string)

The object key preview for the customer S3 location.

EncryptionOption -> (string)

The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key or Amazon Web Services managed key.

KmsKeyId -> (string)

The KMS key ID for the customer S3 location when encrypting with an Amazon Web Services managed key.

Shorthand Syntax:

```
EnableMagneticStoreWrites=boolean,MagneticStoreRejectedDataLocation={S3Configuration={BucketName=string,ObjectKeyPrefix=string,EncryptionOption=string,KmsKeyId=string}}
```

JSON Syntax:

```
{
  "EnableMagneticStoreWrites": true|false,
  "MagneticStoreRejectedDataLocation": {
    "S3Configuration": {
      "BucketName": "string",
      "ObjectKeyPrefix": "string",
      "EncryptionOption": "SSE_S3"|"SSE_KMS",
      "KmsKeyId": "string"
    }
  }
}
```

`--schema` (structure)

The schema of the table.

CompositePartitionKey -> (list)

A non-empty list of partition keys defining the attributes used to partition the table data. The order of the list determines the partition hierarchy. The name and type of each partition key as well as the partition key order cannot be changed after the table is created. However, the enforcement level of each partition key can be changed.

(structure)

An attribute used in partitioning data in a table. A dimension key partitions data using the values of the dimension specified by the dimension-name as partition key, while a measure key partitions data using measure names (values of the âmeasure_nameâ column).

Type -> (string)

The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key).

Name -> (string)

The name of the attribute used for a dimension key.

EnforcementInRecord -> (string)

The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED (dimension key must be specified) and OPTIONAL (dimension key does not have to be specified).

Shorthand Syntax:

```
CompositePartitionKey=[{Type=string,Name=string,EnforcementInRecord=string},{Type=string,Name=string,EnforcementInRecord=string}]
```

JSON Syntax:

```
{
  "CompositePartitionKey": [
    {
      "Type": "DIMENSION"|"MEASURE",
      "Name": "string",
      "EnforcementInRecord": "REQUIRED"|"OPTIONAL"
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

Table -> (structure)

The updated Timestream table.

Arn -> (string)

The Amazon Resource Name that uniquely identifies this table.

TableName -> (string)

The name of the Timestream table.

DatabaseName -> (string)

The name of the Timestream database that contains this table.

TableStatus -> (string)

The current state of the table:

- `DELETING` - The table is being deleted.
- `ACTIVE` - The table is ready for use.

RetentionProperties -> (structure)

The retention duration for the memory store and magnetic store.

MemoryStoreRetentionPeriodInHours -> (long)

The duration for which data must be stored in the memory store.

MagneticStoreRetentionPeriodInDays -> (long)

The duration for which data must be stored in the magnetic store.

CreationTime -> (timestamp)

The time when the Timestream table was created.

LastUpdatedTime -> (timestamp)

The time when the Timestream table was last updated.

MagneticStoreWriteProperties -> (structure)

Contains properties to set on the table when enabling magnetic store writes.

EnableMagneticStoreWrites -> (boolean)

A flag to enable magnetic store writes.

MagneticStoreRejectedDataLocation -> (structure)

The location to write error reports for records rejected asynchronously during magnetic store writes.

S3Configuration -> (structure)

Configuration of an S3 location to write error reports for records rejected, asynchronously, during magnetic store writes.

BucketName -> (string)

The bucket name of the customer S3 bucket.

ObjectKeyPrefix -> (string)

The object key preview for the customer S3 location.

EncryptionOption -> (string)

The encryption option for the customer S3 location. Options are S3 server-side encryption with an S3 managed key or Amazon Web Services managed key.

KmsKeyId -> (string)

The KMS key ID for the customer S3 location when encrypting with an Amazon Web Services managed key.

Schema -> (structure)

The schema of the table.

CompositePartitionKey -> (list)

A non-empty list of partition keys defining the attributes used to partition the table data. The order of the list determines the partition hierarchy. The name and type of each partition key as well as the partition key order cannot be changed after the table is created. However, the enforcement level of each partition key can be changed.

(structure)

An attribute used in partitioning data in a table. A dimension key partitions data using the values of the dimension specified by the dimension-name as partition key, while a measure key partitions data using measure names (values of the âmeasure_nameâ column).

Type -> (string)

The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key).

Name -> (string)

The name of the attribute used for a dimension key.

EnforcementInRecord -> (string)

The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED (dimension key must be specified) and OPTIONAL (dimension key does not have to be specified).