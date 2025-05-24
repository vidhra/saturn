# create-bulk-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-bulk-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-bulk-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# create-bulk-import-job

## Description

Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see [Create a bulk import job (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html) in the *Amazon Simple Storage Service User Guide* .

### Warning

Before you create a bulk import job, you must enable IoT SiteWise warm tier or IoT SiteWise cold tier. For more information about how to configure storage settings, see [PutStorageConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html) .

Bulk import is designed to store historical data to IoT SiteWise. It does not trigger computations or notifications on IoT SiteWise warm or cold tier storage.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/CreateBulkImportJob)

## Synopsis

```
create-bulk-import-job
--job-name <value>
--job-role-arn <value>
--files <value>
--error-report-location <value>
--job-configuration <value>
[--adaptive-ingestion | --no-adaptive-ingestion]
[--delete-files-after-import | --no-delete-files-after-import]
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

`--job-name` (string)

The unique name that helps identify the job request.

`--job-role-arn` (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM role that allows IoT SiteWise to read Amazon S3 data.

`--files` (list)

The files in the specified Amazon S3 bucket that contain your data.

(structure)

The file in Amazon S3 where your data is saved.

bucket -> (string)

The name of the Amazon S3 bucket from which data is imported.

key -> (string)

The key of the Amazon S3 object that contains your data. Each object has a key that is a unique identifier. Each object has exactly one key.

versionId -> (string)

The version ID to identify a specific version of the Amazon S3 object that contains your data.

Shorthand Syntax:

```
bucket=string,key=string,versionId=string ...
```

JSON Syntax:

```
[
  {
    "bucket": "string",
    "key": "string",
    "versionId": "string"
  }
  ...
]
```

`--error-report-location` (structure)

The Amazon S3 destination where errors associated with the job creation request are saved.

bucket -> (string)

The name of the Amazon S3 bucket to which errors associated with the bulk import job are sent.

prefix -> (string)

Amazon S3 uses the prefix as a folder name to organize data in the bucket. Each Amazon S3 object has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/). For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
bucket=string,prefix=string
```

JSON Syntax:

```
{
  "bucket": "string",
  "prefix": "string"
}
```

`--job-configuration` (structure)

Contains the configuration information of a job, such as the file format used to save data in Amazon S3.

fileFormat -> (structure)

The file format of the data in S3.

csv -> (structure)

The file is in .CSV format.

columnNames -> (list)

The column names specified in the .csv file.

(string)

parquet -> (structure)

The file is in parquet format.

JSON Syntax:

```
{
  "fileFormat": {
    "csv": {
      "columnNames": ["ALIAS"|"ASSET_ID"|"PROPERTY_ID"|"DATA_TYPE"|"TIMESTAMP_SECONDS"|"TIMESTAMP_NANO_OFFSET"|"QUALITY"|"VALUE", ...]
    },
    "parquet": {

    }
  }
}
```

`--adaptive-ingestion` | `--no-adaptive-ingestion` (boolean)

If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.

`--delete-files-after-import` | `--no-delete-files-after-import` (boolean)

If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.

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

jobId -> (string)

The ID of the job.

jobName -> (string)

The unique name that helps identify the job request.

jobStatus -> (string)

The status of the bulk import job can be one of following values:

- `PENDING` â IoT SiteWise is waiting for the current bulk import job to finish.
- `CANCELLED` â The bulk import job has been canceled.
- `RUNNING` â IoT SiteWise is processing your request to import your data from Amazon S3.
- `COMPLETED` â IoT SiteWise successfully completed your request to import data from Amazon S3.
- `FAILED` â IoT SiteWise couldnât process your request to import data from Amazon S3. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.
- `COMPLETED_WITH_FAILURES` â IoT SiteWise completed your request to import data from Amazon S3 with errors. You can use logs saved in the specified error report location in Amazon S3 to troubleshoot issues.