# describe-dataset-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/describe-dataset-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# describe-dataset-import-job

## Description

Describes a dataset import job created using the [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html) operation.

In addition to listing the parameters provided in the `CreateDatasetImportJob` request, this operation includes the following properties:

- `CreationTime`
- `LastModificationTime`
- `DataSize`
- `FieldStatistics`
- `Status`
- `Message` - If an error occurred, information about the error.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/DescribeDatasetImportJob)

## Synopsis

```
describe-dataset-import-job
--dataset-import-job-arn <value>
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

`--dataset-import-job-arn` (string)

The Amazon Resource Name (ARN) of the dataset import job.

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

DatasetImportJobName -> (string)

The name of the dataset import job.

DatasetImportJobArn -> (string)

The ARN of the dataset import job.

DatasetArn -> (string)

The Amazon Resource Name (ARN) of the dataset that the training data was imported to.

TimestampFormat -> (string)

The format of timestamps in the dataset. The format that you specify depends on the `DataFrequency` specified when the dataset was created. The following formats are supported

- âyyyy-MM-ddâ For the following data frequencies: Y, M, W, and D
- âyyyy-MM-dd HH:mm:ssâ For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D

TimeZone -> (string)

The single time zone applied to every item in the dataset

UseGeolocationForTimeZone -> (boolean)

Whether `TimeZone` is automatically derived from the geolocation attribute.

GeolocationFormat -> (string)

The format of the geolocation attribute. Valid Values:`"LAT_LONG"` and `"CC_POSTALCODE"` .

DataSource -> (structure)

The location of the training data to import and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data.

If encryption is used, `DataSource` includes an Key Management Service (KMS) key.

S3Config -> (structure)

The path to the data stored in an Amazon Simple Storage Service (Amazon S3) bucket along with the credentials to access the data.

Path -> (string)

The path to an Amazon Simple Storage Service (Amazon S3) bucket or file(s) in an Amazon S3 bucket.

RoleArn -> (string)

The ARN of the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the Amazon S3 bucket or files. If you provide a value for the `KMSKeyArn` key, the role must allow access to the key.

Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isnât in your account, you get an `InvalidInputException` error.

KMSKeyArn -> (string)

The Amazon Resource Name (ARN) of an Key Management Service (KMS) key.

EstimatedTimeRemainingInMinutes -> (long)

The estimated time remaining in minutes for the dataset import job to complete.

FieldStatistics -> (map)

Statistical information about each field in the input data.

key -> (string)

value -> (structure)

Provides statistics for each data field imported into to an Amazon Forecast dataset with the [CreateDatasetImportJob](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html) operation.

Count -> (integer)

The number of values in the field. If the response value is -1, refer to `CountLong` .

CountDistinct -> (integer)

The number of distinct values in the field. If the response value is -1, refer to `CountDistinctLong` .

CountNull -> (integer)

The number of null values in the field. If the response value is -1, refer to `CountNullLong` .

CountNan -> (integer)

The number of NAN (not a number) values in the field. If the response value is -1, refer to `CountNanLong` .

Min -> (string)

For a numeric field, the minimum value in the field.

Max -> (string)

For a numeric field, the maximum value in the field.

Avg -> (double)

For a numeric field, the average value in the field.

Stddev -> (double)

For a numeric field, the standard deviation.

CountLong -> (long)

The number of values in the field. `CountLong` is used instead of `Count` if the value is greater than 2,147,483,647.

CountDistinctLong -> (long)

The number of distinct values in the field. `CountDistinctLong` is used instead of `CountDistinct` if the value is greater than 2,147,483,647.

CountNullLong -> (long)

The number of null values in the field. `CountNullLong` is used instead of `CountNull` if the value is greater than 2,147,483,647.

CountNanLong -> (long)

The number of NAN (not a number) values in the field. `CountNanLong` is used instead of `CountNan` if the value is greater than 2,147,483,647.

DataSize -> (double)

The size of the dataset in gigabytes (GB) after the import job has finished.

Status -> (string)

The status of the dataset import job. States include:

- `ACTIVE`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`
- `CREATE_STOPPING` , `CREATE_STOPPED`

Message -> (string)

If an error occurred, an informational message about the error.

CreationTime -> (timestamp)

When the dataset import job was created.

LastModificationTime -> (timestamp)

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime` .
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.

Format -> (string)

The format of the imported data, CSV or PARQUET.

ImportMode -> (string)

The import mode of the dataset import job, FULL or INCREMENTAL.