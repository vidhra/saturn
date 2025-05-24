# describe-valid-db-instance-modificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-valid-db-instance-modifications.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-valid-db-instance-modifications.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# describe-valid-db-instance-modifications

## Description

You can call  DescribeValidDBInstanceModifications to learn what modifications you can make to your DB instance. You can use this information when you call  ModifyDBInstance .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeValidDBInstanceModifications)

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

## Output

ValidDBInstanceModificationsMessage -> (structure)

Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the  DescribeValidDBInstanceModifications action. You can use this information when you call  ModifyDBInstance .

Storage -> (list)

Valid storage options for your DB instance.

(structure)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

StorageType -> (string)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

StorageSize -> (list)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

(structure)

A range of integer values.

From -> (integer)

The minimum value in the range.

To -> (integer)

The maximum value in the range.

Step -> (integer)

The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isnât a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000â¦

ProvisionedIops -> (list)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

(structure)

A range of integer values.

From -> (integer)

The minimum value in the range.

To -> (integer)

The maximum value in the range.

Step -> (integer)

The step value for the range. For example, if you have a range of 5,000 to 10,000, with a step value of 1,000, the valid values start at 5,000 and step up by 1,000. Even though 7,500 is within the range, it isnât a valid value for the range. The valid values are 5,000, 6,000, 7,000, 8,000â¦

IopsToStorageRatio -> (list)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

(structure)

A range of double values.

From -> (double)

The minimum value in the range.

To -> (double)

The maximum value in the range.