# get-data-integration-flowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/get-data-integration-flow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/get-data-integration-flow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [supplychain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/supplychain/index.html#cli-aws-supplychain) ]

# get-data-integration-flow

## Description

Enables you to programmatically view a specific data pipeline for the provided Amazon Web Services Supply Chain instance and DataIntegrationFlow name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/supplychain-2024-01-01/GetDataIntegrationFlow)

## Synopsis

```
get-data-integration-flow
--instance-id <value>
--name <value>
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

`--name` (string)

The name of the DataIntegrationFlow created.

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

flow -> (structure)

The details of the DataIntegrationFlow returned.

instanceId -> (string)

The DataIntegrationFlow instance ID.

name -> (string)

The DataIntegrationFlow name.

sources -> (list)

The DataIntegrationFlow source configurations.

(structure)

The DataIntegrationFlow source parameters.

sourceType -> (string)

The DataIntegrationFlow source type.

sourceName -> (string)

The DataIntegrationFlow source name that can be used as table alias in SQL transformation query.

s3Source -> (structure)

The S3 DataIntegrationFlow source.

bucketName -> (string)

The bucketName of the S3 source objects.

prefix -> (string)

The prefix of the S3 source objects. To trigger data ingestion, S3 files need to be put under `s3://*bucketName* /*prefix* /` .

options -> (structure)

The other options of the S3 DataIntegrationFlow source.

fileType -> (string)

The Amazon S3 file type in S3 options.

datasetSource -> (structure)

The dataset DataIntegrationFlow source.

datasetIdentifier -> (string)

The ARN of the dataset.

options -> (structure)

The dataset DataIntegrationFlow source options.

loadType -> (string)

The target datasetâs data load type. This only affects how source S3 files are selected in the S3-to-dataset flow.

- **REPLACE** - Target dataset will get replaced with the new file added under the source s3 prefix.
- **INCREMENTAL** - Target dataset will get updated with the up-to-date content under S3 prefix incorporating any file additions or removals there.

dedupeRecords -> (boolean)

The option to perform deduplication on data records sharing same primary key values. If disabled, transformed data with duplicate primary key values will ingest into dataset, for datasets within **asc** namespace, such duplicates will cause ingestion fail. If enabled without dedupeStrategy, deduplication is done by retaining a random data record among those sharing the same primary key values. If enabled with dedupeStragtegy, the deduplication is done following the strategy.

Note that target dataset may have partition configured, when dedupe is enabled, it only dedupe against primary keys and retain only one record out of those duplicates regardless of its partition status.

dedupeStrategy -> (structure)

The deduplication strategy to dedupe the data records sharing same primary key values of the target dataset. This strategy only applies to target dataset with primary keys and with dedupeRecords option enabled. If transformed data still got duplicates after the dedupeStrategy evaluation, a random data record is chosen to be retained.

type -> (string)

The type of the deduplication strategy.

- **FIELD_PRIORITY** - Field priority configuration for the deduplication strategy specifies an ordered list of fields used to tie-break the data records sharing the same primary key values. Fields earlier in the list have higher priority for evaluation. For each field, the sort order determines whether to retain data record with larger or smaller field value.

fieldPriority -> (structure)

The field priority deduplication strategy.

fields -> (list)

The list of field names and their sort order for deduplication, arranged in descending priority from highest to lowest.

(structure)

The field used in the field priority deduplication strategy.

name -> (string)

The name of the deduplication field. Must exist in the dataset and not be a primary key.

sortOrder -> (string)

The sort order for the deduplication field.

transformation -> (structure)

The DataIntegrationFlow transformation configurations.

transformationType -> (string)

The DataIntegrationFlow transformation type.

sqlTransformation -> (structure)

The SQL DataIntegrationFlow transformation configuration.

query -> (string)

The transformation SQL query body based on SparkSQL.

target -> (structure)

The DataIntegrationFlow target configuration.

targetType -> (string)

The DataIntegrationFlow target type.

s3Target -> (structure)

The S3 DataIntegrationFlow target.

bucketName -> (string)

The bucketName of the S3 target objects.

prefix -> (string)

The prefix of the S3 target objects.

options -> (structure)

The S3 DataIntegrationFlow target options.

fileType -> (string)

The Amazon S3 file type in S3 options.

datasetTarget -> (structure)

The dataset DataIntegrationFlow target. Note that for AWS Supply Chain dataset under **asc** namespace, it has a connection_id internal field that is not allowed to be provided by client directly, they will be auto populated.

datasetIdentifier -> (string)

The dataset ARN.

options -> (structure)

The dataset DataIntegrationFlow target options.

loadType -> (string)

The target datasetâs data load type. This only affects how source S3 files are selected in the S3-to-dataset flow.

- **REPLACE** - Target dataset will get replaced with the new file added under the source s3 prefix.
- **INCREMENTAL** - Target dataset will get updated with the up-to-date content under S3 prefix incorporating any file additions or removals there.

dedupeRecords -> (boolean)

The option to perform deduplication on data records sharing same primary key values. If disabled, transformed data with duplicate primary key values will ingest into dataset, for datasets within **asc** namespace, such duplicates will cause ingestion fail. If enabled without dedupeStrategy, deduplication is done by retaining a random data record among those sharing the same primary key values. If enabled with dedupeStragtegy, the deduplication is done following the strategy.

Note that target dataset may have partition configured, when dedupe is enabled, it only dedupe against primary keys and retain only one record out of those duplicates regardless of its partition status.

dedupeStrategy -> (structure)

The deduplication strategy to dedupe the data records sharing same primary key values of the target dataset. This strategy only applies to target dataset with primary keys and with dedupeRecords option enabled. If transformed data still got duplicates after the dedupeStrategy evaluation, a random data record is chosen to be retained.

type -> (string)

The type of the deduplication strategy.

- **FIELD_PRIORITY** - Field priority configuration for the deduplication strategy specifies an ordered list of fields used to tie-break the data records sharing the same primary key values. Fields earlier in the list have higher priority for evaluation. For each field, the sort order determines whether to retain data record with larger or smaller field value.

fieldPriority -> (structure)

The field priority deduplication strategy.

fields -> (list)

The list of field names and their sort order for deduplication, arranged in descending priority from highest to lowest.

(structure)

The field used in the field priority deduplication strategy.

name -> (string)

The name of the deduplication field. Must exist in the dataset and not be a primary key.

sortOrder -> (string)

The sort order for the deduplication field.

createdTime -> (timestamp)

The DataIntegrationFlow creation timestamp.

lastModifiedTime -> (timestamp)

The DataIntegrationFlow last modified timestamp.