# describe-valid-db-instance-modificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-valid-db-instance-modifications.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-valid-db-instance-modifications.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-valid-db-instance-modifications

## Description

You can call `DescribeValidDBInstanceModifications` to learn what modifications you can make to your DB instance. You can use this information when you call `ModifyDBInstance` .

This command doesnât apply to RDS Custom.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeValidDBInstanceModifications)

## Synopsis

```
describe-valid-db-instance-modifications
--db-instance-identifier <value>
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

`--db-instance-identifier` (string)

The customer identifier or the ARN of your DB instance.

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

**To describe valid modifications for a DB instance**

The following `describe-valid-db-instance-modifications` example retrieves details about the valid modifications for the specified DB instance.

```
aws rds describe-valid-db-instance-modifications \
    --db-instance-identifier test-instance
```

Output:

```
{
    "ValidDBInstanceModificationsMessage": {
        "ValidProcessorFeatures": [],
        "Storage": [
            {
                "StorageSize": [
                    {
                        "Step": 1,
                        "To": 20,
                        "From": 20
                    },
                    {
                        "Step": 1,
                        "To": 6144,
                        "From": 22
                    }
                ],
                "ProvisionedIops": [
                    {
                        "Step": 1,
                        "To": 0,
                        "From": 0
                    }
                ],
                "IopsToStorageRatio": [
                    {
                        "To": 0.0,
                        "From": 0.0
                    }
                ],
                "StorageType": "gp2"
            },
            {
                "StorageSize": [
                    {
                        "Step": 1,
                        "To": 6144,
                        "From": 100
                    }
                ],
                "ProvisionedIops": [
                    {
                        "Step": 1,
                        "To": 40000,
                        "From": 1000
                    }
                ],
                "IopsToStorageRatio": [
                    {
                        "To": 50.0,
                        "From": 1.0
                    }
                ],
                "StorageType": "io1"
            },
            {
                "StorageSize": [
                    {
                        "Step": 1,
                        "To": 20,
                        "From": 20
                    },
                    {
                        "Step": 1,
                        "To": 3072,
                        "From": 22
                    }
                ],
                "ProvisionedIops": [
                    {
                        "Step": 1,
                        "To": 0,
                        "From": 0
                    }
                ],
                "IopsToStorageRatio": [
                    {
                        "To": 0.0,
                        "From": 0.0
                    }
                ],
                "StorageType": "magnetic"
            }
        ]
    }
}
```

## Output

ValidDBInstanceModificationsMessage -> (structure)

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the `DescribeValidDBInstanceModifications` action. You can use this information when you call `ModifyDBInstance` .

Storage -> (list)

Valid storage options for your DB instance.

(structure)

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the `DescribeValidDBInstanceModifications` action.

StorageType -> (string)

The valid storage types for your DB instance. For example: gp2, gp3, io1, io2.

StorageSize -> (list)

The valid range of storage in gibibytes (GiB). For example, 100 to 16,384.

(structure)

A range of integer values.

From -> (integer)

The minimum value in the range.

To -> (integer)

The maximum value in the range.

Step -> (integer)

The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isnât a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000â¦

ProvisionedIops -> (list)

The valid range of provisioned IOPS. For example, 1000-256,000.

(structure)

A range of integer values.

From -> (integer)

The minimum value in the range.

To -> (integer)

The maximum value in the range.

Step -> (integer)

The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isnât a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000â¦

IopsToStorageRatio -> (list)

The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example, 3-10, which means that provisioned IOPS can be between 3 and 10 times storage.

(structure)

A range of double values.

From -> (double)

The minimum value in the range.

To -> (double)

The maximum value in the range.

SupportsStorageAutoscaling -> (boolean)

Indicates whether or not Amazon RDS can automatically scale storage for DB instances that use the new instance class.

ProvisionedStorageThroughput -> (list)

The valid range of provisioned storage throughput. For example, 500-4,000 mebibytes per second (MiBps).

(structure)

A range of integer values.

From -> (integer)

The minimum value in the range.

To -> (integer)

The maximum value in the range.

Step -> (integer)

The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isnât a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000â¦

StorageThroughputToIopsRatio -> (list)

The valid range of storage throughput to provisioned IOPS ratios. For example, 0-0.25.

(structure)

A range of double values.

From -> (double)

The minimum value in the range.

To -> (double)

The maximum value in the range.

ValidProcessorFeatures -> (list)

Valid processor features for your DB instance.

(structure)

Contains the available processor feature information for the DB instance class of a DB instance.

For more information, see [Configuring the Processor of the DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor) in the *Amazon RDS User Guide.*

Name -> (string)

The name of the processor feature. Valid names are `coreCount` and `threadsPerCore` .

DefaultValue -> (string)

The default value for the processor feature of the DB instance class.

AllowedValues -> (string)

The allowed values for the processor feature of the DB instance class.

SupportsDedicatedLogVolume -> (boolean)

Indicates whether a DB instance supports using a dedicated log volume (DLV).