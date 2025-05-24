# get-vector-enrichment-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/get-vector-enrichment-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/get-vector-enrichment-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-geospatial](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-geospatial/index.html#cli-aws-sagemaker-geospatial) ]

# get-vector-enrichment-job

## Description

Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-geospatial-2020-05-27/GetVectorEnrichmentJob)

## Synopsis

```
get-vector-enrichment-job
--arn <value>
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

`--arn` (string)

The Amazon Resource Name (ARN) of the Vector Enrichment job.

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

Arn -> (string)

The Amazon Resource Name (ARN) of the Vector Enrichment job.

CreationTime -> (timestamp)

The creation time.

DurationInSeconds -> (integer)

The duration of the Vector Enrichment job, in seconds.

ErrorDetails -> (structure)

Details about the errors generated during the Vector Enrichment job.

ErrorMessage -> (string)

A message that you define and then is processed and rendered by the Vector Enrichment job when the error occurs.

ErrorType -> (string)

The type of error generated during the Vector Enrichment job.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that you specified for the job.

ExportErrorDetails -> (structure)

Details about the errors generated during the ExportVectorEnrichmentJob.

Message -> (string)

The message providing details about the errors generated during the Vector Enrichment job.

Type -> (string)

The output error details for an Export operation on a Vector Enrichment job.

ExportStatus -> (string)

The export status of the Vector Enrichment job being initiated.

InputConfig -> (structure)

Input configuration information for the Vector Enrichment job.

DataSourceConfig -> (tagged union structure)

The input structure for the data source that represents the storage type of the input data objects.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `S3Data`.

S3Data -> (structure)

The input structure for the Amazon S3 data that represents the Amazon S3 location of the input data objects.

KmsKeyId -> (string)

The Key Management Service key ID for server-side encryption.

S3Uri -> (string)

The URL to the Amazon S3 data for the Vector Enrichment job.

DocumentType -> (string)

The input structure that defines the data source file type.

JobConfig -> (tagged union structure)

An object containing information about the job configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `MapMatchingConfig`, `ReverseGeocodingConfig`.

MapMatchingConfig -> (structure)

The input structure for Map Matching operation type.

IdAttributeName -> (string)

The field name for the data that describes the identifier representing a collection of GPS points belonging to an individual trace.

TimestampAttributeName -> (string)

The name of the timestamp attribute.

XAttributeName -> (string)

The name of the X-attribute

YAttributeName -> (string)

The name of the Y-attribute

ReverseGeocodingConfig -> (structure)

The input structure for Reverse Geocoding operation type.

XAttributeName -> (string)

The field name for the data that describes x-axis coordinate, eg. longitude of a point.

YAttributeName -> (string)

The field name for the data that describes y-axis coordinate, eg. latitude of a point.

KmsKeyId -> (string)

The Key Management Service key ID for server-side encryption.

Name -> (string)

The name of the Vector Enrichment job.

Status -> (string)

The status of the initiated Vector Enrichment job.

Tags -> (map)

Each tag consists of a key and a value.

key -> (string)

value -> (string)

Type -> (string)

The type of the Vector Enrichment job being initiated.