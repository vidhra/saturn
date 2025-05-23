# describe-datastoreÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-datastore.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-datastore.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotanalytics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/index.html#cli-aws-iotanalytics) ]

# describe-datastore

## Description

Retrieves information about a data store.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotanalytics-2017-11-27/DescribeDatastore)

## Synopsis

```
describe-datastore
--datastore-name <value>
[--include-statistics | --no-include-statistics]
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

`--datastore-name` (string)

The name of the data store

`--include-statistics` | `--no-include-statistics` (boolean)

If true, additional statistical information about the data store is included in the response. This feature canât be used with a data store whose S3 storage is customer-managed.

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

**To retrieve information about a data store**

The following `describe-datastore` example displays details, including statistics, for the specified data store.

```
aws iotanalytics describe-datastore \
    --datastore-name mydatastore \
    --include-statistics
```

Output:

```
{
    "datastore": {
        "status": "ACTIVE",
        "name": "mydatastore",
        "lastUpdateTime": 1557858971.02,
        "creationTime": 1557858971.02,
        "retentionPeriod": {
            "unlimited": true
        },
        "arn": "arn:aws:iotanalytics:us-west-2:123456789012:datastore/mydatastore"
    },
    "statistics": {
        "size": {
            "estimatedSizeInBytes": 397.0,
            "estimatedOn": 1561592040.0
        }
    }
}
```

For more information, see [DescribeDatastore](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DescribeDatastore.html) in the *AWS IoT Analytics API Reference*.

## Output

datastore -> (structure)

Information about the data store.

name -> (string)

The name of the data store.

storage -> (structure)

Where data in a data store is stored.. You can choose `serviceManagedS3` storage, `customerManagedS3` storage, or `iotSiteWiseMultiLayerStorage` storage. The default is `serviceManagedS3` . You canât change the choice of Amazon S3 storage after your data store is created.

serviceManagedS3 -> (structure)

Used to store data in an Amazon S3 bucket managed by IoT Analytics. You canât change the choice of Amazon S3 storage after your data store is created.

customerManagedS3 -> (structure)

S3-customer-managed; When you choose customer-managed storage, the `retentionPeriod` parameter is ignored. You canât change the choice of Amazon S3 storage after your data store is created.

bucket -> (string)

The name of the Amazon S3 bucket where your data is stored.

keyPrefix -> (string)

(Optional) The prefix used to create the keys of the data store data objects. Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

roleArn -> (string)

The ARN of the role that grants IoT Analytics permission to interact with your Amazon S3 resources.

iotSiteWiseMultiLayerStorage -> (structure)

Used to store data used by IoT SiteWise in an Amazon S3 bucket that you manage. You canât change the choice of Amazon S3 storage after your data store is created.

customerManagedS3Storage -> (structure)

Used to store data used by IoT SiteWise in an Amazon S3 bucket that you manage.

bucket -> (string)

The name of the Amazon S3 bucket where your data is stored.

keyPrefix -> (string)

(Optional) The prefix used to create the keys of the data store data objects. Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

arn -> (string)

The ARN of the data store.

status -> (string)

The status of a data store:

CREATING

The data store is being created.

ACTIVE

The data store has been created and can be used.

DELETING

The data store is being deleted.

retentionPeriod -> (structure)

How long, in days, message data is kept for the data store. When `customerManagedS3` storage is selected, this parameter is ignored.

unlimited -> (boolean)

If true, message data is kept indefinitely.

numberOfDays -> (integer)

The number of days that message data is kept. The `unlimited` parameter must be false.

creationTime -> (timestamp)

When the data store was created.

lastUpdateTime -> (timestamp)

The last time the data store was updated.

lastMessageArrivalTime -> (timestamp)

The last time when a new message arrived in the data store.

IoT Analytics updates this value at most once per minute for Amazon Simple Storage Service one data store. Hence, the `lastMessageArrivalTime` value is an approximation.

This feature only applies to messages that arrived in the data store after October 23, 2020.

fileFormatConfiguration -> (structure)

Contains the configuration information of file formats. IoT Analytics data stores support JSON and [Parquet](https://parquet.apache.org/) .

The default file format is JSON. You can specify only one format.

You canât change the file format after you create the data store.

jsonConfiguration -> (structure)

Contains the configuration information of the JSON format.

parquetConfiguration -> (structure)

Contains the configuration information of the Parquet format.

schemaDefinition -> (structure)

Information needed to define a schema.

columns -> (list)

Specifies one or more columns that store your data.

Each schema can have up to 100 columns. Each column can have up to 100 nested types.

(structure)

Contains information about a column that stores your data.

name -> (string)

The name of the column.

type -> (string)

The type of data. For more information about the supported data types, see [Common data types](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html) in the *Glue Developer Guide* .

datastorePartitions -> (structure)

Contains information about the partition dimensions in a data store.

partitions -> (list)

A list of partition dimensions in a data store.

(structure)

A single dimension to partition a data store. The dimension must be an `AttributePartition` or a `TimestampPartition` .

attributePartition -> (structure)

A partition dimension defined by an `attributeName` .

attributeName -> (string)

The name of the attribute that defines a partition dimension.

timestampPartition -> (structure)

A partition dimension defined by a timestamp attribute.

attributeName -> (string)

The attribute name of the partition defined by a timestamp.

timestampFormat -> (string)

The timestamp format of a partition defined by a timestamp. The default format is seconds since epoch (January 1, 1970 at midnight UTC time).

statistics -> (structure)

Additional statistical information about the data store. Included if the `includeStatistics` parameter is set to `true` in the request.

size -> (structure)

The estimated size of the data store.

estimatedSizeInBytes -> (double)

The estimated size of the resource, in bytes.

estimatedOn -> (timestamp)

The time when the estimate of the size of the resource was made.