# describe-datasetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-dataset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/describe-dataset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# describe-dataset

## Description

Provides a JSON description of the data in each time series dataset, including names, column names, and data types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/DescribeDataset)

## Synopsis

```
describe-dataset
--dataset-name <value>
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

`--dataset-name` (string)

The name of the dataset to be described.

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

DatasetName -> (string)

The name of the dataset being described.

DatasetArn -> (string)

The Amazon Resource Name (ARN) of the dataset being described.

CreatedAt -> (timestamp)

Specifies the time the dataset was created in Lookout for Equipment.

LastUpdatedAt -> (timestamp)

Specifies the time the dataset was last updated, if it was.

Status -> (string)

Indicates the status of the dataset.

Schema -> (string)

A JSON description of the data that is in each time series dataset, including names, column names, and data types.

ServerSideKmsKeyId -> (string)

Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment.

IngestionInputConfiguration -> (structure)

Specifies the S3 location configuration for the data input for the data ingestion job.

S3InputConfiguration -> (structure)

The location information for the S3 bucket used for input data for the data ingestion.

Bucket -> (string)

The name of the S3 bucket used for the input data for the data ingestion.

Prefix -> (string)

The prefix for the S3 location being used for the input data for the data ingestion.

KeyPattern -> (string)

The pattern for matching the Amazon S3 files that will be used for ingestion. If the schema was created previously without any KeyPattern, then the default KeyPattern {prefix}/{component_name}/* is used to download files from Amazon S3 according to the schema. This field is required when ingestion is being done for the first time.

Valid Values: {prefix}/{component_name}_* | {prefix}/{component_name}/* | {prefix}/{component_name}[DELIMITER]* (Allowed delimiters : space, dot, underscore, hyphen)

DataQualitySummary -> (structure)

Gives statistics associated with the given dataset for the latest successful associated ingestion job id. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps.

InsufficientSensorData -> (structure)

Parameter that gives information about insufficient data for sensors in the dataset. This includes information about those sensors that have complete data missing and those with a short date range.

MissingCompleteSensorData -> (structure)

Parameter that describes the total number of sensors that have data completely missing for it.

AffectedSensorCount -> (integer)

Indicates the number of sensors that have data missing completely.

SensorsWithShortDateRange -> (structure)

Parameter that describes the total number of sensors that have a short date range of less than 14 days of data overall.

AffectedSensorCount -> (integer)

Indicates the number of sensors that have less than 14 days of data.

MissingSensorData -> (structure)

Parameter that gives information about data that is missing over all the sensors in the input data.

AffectedSensorCount -> (integer)

Indicates the number of sensors that have atleast some data missing.

TotalNumberOfMissingValues -> (integer)

Indicates the total number of missing values across all the sensors.

InvalidSensorData -> (structure)

Parameter that gives information about data that is invalid over all the sensors in the input data.

AffectedSensorCount -> (integer)

Indicates the number of sensors that have at least some invalid values.

TotalNumberOfInvalidValues -> (integer)

Indicates the total number of invalid values across all the sensors.

UnsupportedTimestamps -> (structure)

Parameter that gives information about unsupported timestamps in the input data.

TotalNumberOfUnsupportedTimestamps -> (integer)

Indicates the total number of unsupported timestamps across the ingested data.

DuplicateTimestamps -> (structure)

Parameter that gives information about duplicate timestamps in the input data.

TotalNumberOfDuplicateTimestamps -> (integer)

Indicates the total number of duplicate timestamps.

IngestedFilesSummary -> (structure)

IngestedFilesSummary associated with the given dataset for the latest successful associated ingestion job id.

TotalNumberOfFiles -> (integer)

Indicates the total number of files that were submitted for ingestion.

IngestedNumberOfFiles -> (integer)

Indicates the number of files that were successfully ingested.

DiscardedFiles -> (list)

Indicates the number of files that were discarded. A file could be discarded because its format is invalid (for example, a jpg or pdf) or not readable.

(structure)

Contains information about an S3 bucket.

Bucket -> (string)

The name of the specific S3 bucket.

Key -> (string)

The Amazon Web Services Key Management Service (KMS key) key being used to encrypt the S3 object. Without this key, data in the bucket is not accessible.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that you are using for this the data ingestion job.

DataStartTime -> (timestamp)

Indicates the earliest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.

DataEndTime -> (timestamp)

Indicates the latest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset.

SourceDatasetArn -> (string)

The Amazon Resource Name (ARN) of the source dataset from which the current data being described was imported from.