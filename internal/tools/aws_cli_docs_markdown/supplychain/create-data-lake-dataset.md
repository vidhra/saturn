# create-data-lake-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/create-data-lake-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/create-data-lake-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [supplychain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/index.html#cli-aws-supplychain) ]

# create-data-lake-dataset

## Description

Enables you to programmatically create an Amazon Web Services Supply Chain data lake dataset. Developers can create the datasets using their pre-defined or custom schema for a given instance ID, namespace, and dataset name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/supplychain-2024-01-01/CreateDataLakeDataset)

## Synopsis

```
create-data-lake-dataset
--instance-id <value>
--namespace <value>
--name <value>
[--schema <value>]
[--description <value>]
[--partition-spec <value>]
[--tags <value>]
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

`--instance-id` (string)

The Amazon Web Services Supply Chain instance identifier.

`--namespace` (string)

The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:

- **asc** - For information on the Amazon Web Services Supply Chain supported datasets see [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html) .
- **default** - For datasets with custom user-defined schemas.

`--name` (string)

The name of the dataset. For **asc** name space, the name must be one of the supported data entities under [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html) .

`--schema` (structure)

The custom schema of the data lake dataset and required for dataset in **default** and custom namespaces.

name -> (string)

The name of the dataset schema.

fields -> (list)

The list of field details of the dataset schema.

(structure)

The dataset field details.

name -> (string)

The dataset field name.

type -> (string)

The dataset field type.

isRequired -> (boolean)

Indicate if the field is required or not.

primaryKeys -> (list)

The list of primary key fields for the dataset. Primary keys defined can help data ingestion methods to ensure data uniqueness: CreateDataIntegrationFlowâs dedupe strategy will leverage primary keys to perform records deduplication before write to dataset; SendDataIntegrationEventâs UPSERT and DELETE can only work with dataset with primary keys. For more details, refer to those data ingestion documentations.

Note that defining primary keys does not necessarily mean the dataset cannot have duplicate records, duplicate records can still be ingested if CreateDataIntegrationFlowâs dedupe disabled or through SendDataIntegrationEventâs APPEND operation.

(structure)

The detail of the primary key field.

name -> (string)

The name of the primary key field.

Shorthand Syntax:

```
name=string,fields=[{name=string,type=string,isRequired=boolean},{name=string,type=string,isRequired=boolean}],primaryKeys=[{name=string},{name=string}]
```

JSON Syntax:

```
{
  "name": "string",
  "fields": [
    {
      "name": "string",
      "type": "INT"|"DOUBLE"|"STRING"|"TIMESTAMP"|"LONG",
      "isRequired": true|false
    }
    ...
  ],
  "primaryKeys": [
    {
      "name": "string"
    }
    ...
  ]
}
```

`--description` (string)

The description of the dataset.

`--partition-spec` (structure)

The partition specification of the dataset. Partitioning can effectively improve the dataset query performance by reducing the amount of data scanned during query execution. But partitioning or not will affect how data get ingested by data ingestion methods, such as SendDataIntegrationEventâs dataset UPSERT will upsert records within partition (instead of within whole dataset). For more details, refer to those data ingestion documentations.

fields -> (list)

The fields on which to partition a dataset. The partitions will be applied hierarchically based on the order of this list.

(structure)

The detail of the partition field.

name -> (string)

The name of the partition field.

transform -> (structure)

The transformation of the partition field. A transformation specifies how to partition on a given field. For example, with timestamp you can specify that youâd like to partition fields by day, e.g. data record with value 2025-01-03T00:00:00Z in partition field is in 2025-01-03 partition. Also noted that data record without any value in optional partition field is in NULL partition.

type -> (string)

The type of partitioning transformation for this field. The available options are:

- **IDENTITY** - Partitions data on a given field by its exact values.
- **YEAR** - Partitions data on a timestamp field using year granularity.
- **MONTH** - Partitions data on a timestamp field using month granularity.
- **DAY** - Partitions data on a timestamp field using day granularity.
- **HOUR** - Partitions data on a timestamp field using hour granularity.

JSON Syntax:

```
{
  "fields": [
    {
      "name": "string",
      "transform": {
        "type": "YEAR"|"MONTH"|"DAY"|"HOUR"|"IDENTITY"
      }
    }
    ...
  ]
}
```

`--tags` (map)

The tags of the dataset.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

dataset -> (structure)

The detail of created dataset.

instanceId -> (string)

The Amazon Web Services Supply Chain instance identifier.

namespace -> (string)

The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:

- **asc** - For information on the Amazon Web Services Supply Chain supported datasets see [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html) .
- **default** - For datasets with custom user-defined schemas.

name -> (string)

The name of the dataset. For **asc** namespace, the name must be one of the supported data entities under [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html) .

arn -> (string)

The arn of the dataset.

schema -> (structure)

The schema of the dataset.

name -> (string)

The name of the dataset schema.

fields -> (list)

The list of field details of the dataset schema.

(structure)

The dataset field details.

name -> (string)

The dataset field name.

type -> (string)

The dataset field type.

isRequired -> (boolean)

Indicate if the field is required or not.

primaryKeys -> (list)

The list of primary key fields for the dataset. Primary keys defined can help data ingestion methods to ensure data uniqueness: CreateDataIntegrationFlowâs dedupe strategy will leverage primary keys to perform records deduplication before write to dataset; SendDataIntegrationEventâs UPSERT and DELETE can only work with dataset with primary keys. For more details, refer to those data ingestion documentations.

Note that defining primary keys does not necessarily mean the dataset cannot have duplicate records, duplicate records can still be ingested if CreateDataIntegrationFlowâs dedupe disabled or through SendDataIntegrationEventâs APPEND operation.

(structure)

The detail of the primary key field.

name -> (string)

The name of the primary key field.

description -> (string)

The description of the dataset.

partitionSpec -> (structure)

The partition specification for a dataset.

fields -> (list)

The fields on which to partition a dataset. The partitions will be applied hierarchically based on the order of this list.

(structure)

The detail of the partition field.

name -> (string)

The name of the partition field.

transform -> (structure)

The transformation of the partition field. A transformation specifies how to partition on a given field. For example, with timestamp you can specify that youâd like to partition fields by day, e.g. data record with value 2025-01-03T00:00:00Z in partition field is in 2025-01-03 partition. Also noted that data record without any value in optional partition field is in NULL partition.

type -> (string)

The type of partitioning transformation for this field. The available options are:

- **IDENTITY** - Partitions data on a given field by its exact values.
- **YEAR** - Partitions data on a timestamp field using year granularity.
- **MONTH** - Partitions data on a timestamp field using month granularity.
- **DAY** - Partitions data on a timestamp field using day granularity.
- **HOUR** - Partitions data on a timestamp field using hour granularity.

createdTime -> (timestamp)

The creation time of the dataset.

lastModifiedTime -> (timestamp)

The last modified time of the dataset.