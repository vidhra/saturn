# create-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# create-import-job

## Description

Creates an import job for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/CreateImportJob)

## Synopsis

```
create-import-job
--application-id <value>
--import-job-request <value>
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--import-job-request` (structure)

Specifies the settings for a job that imports endpoint definitions from an Amazon Simple Storage Service (Amazon S3) bucket.

DefineSegment -> (boolean)

Specifies whether to create a segment that contains the endpoints, when the endpoint definitions are imported.

ExternalId -> (string)

(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We donât recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.

Format -> (string)

The format of the files that contain the endpoint definitions to import. Valid values are: CSV, for comma-separated values format; and, JSON, for newline-delimited JSON format. If the Amazon S3 location stores multiple files that use different formats, Amazon Pinpoint imports data only from the files that use the specified format.

RegisterEndpoints -> (boolean)

Specifies whether to register the endpoints with Amazon Pinpoint, when the endpoint definitions are imported.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from.

S3Url -> (string)

The URL of the Amazon Simple Storage Service (Amazon S3) bucket that contains the endpoint definitions to import. This location can be a folder or a single file. If the location is a folder, Amazon Pinpoint imports endpoint definitions from the files in this location, including any subfolders that the folder contains.

The URL should be in the following format: s3://bucket-name/folder-name/file-name. The location can end with the key for an individual object or a prefix that qualifies multiple objects.

SegmentId -> (string)

The identifier for the segment to update or add the imported endpoint definitions to, if the import job is meant to update an existing segment.

SegmentName -> (string)

A custom name for the segment thatâs created by the import job, if the value of the DefineSegment property is true.

Shorthand Syntax:

```
DefineSegment=boolean,ExternalId=string,Format=string,RegisterEndpoints=boolean,RoleArn=string,S3Url=string,SegmentId=string,SegmentName=string
```

JSON Syntax:

```
{
  "DefineSegment": true|false,
  "ExternalId": "string",
  "Format": "CSV"|"JSON",
  "RegisterEndpoints": true|false,
  "RoleArn": "string",
  "S3Url": "string",
  "SegmentId": "string",
  "SegmentName": "string"
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

ImportJobResponse -> (structure)

Provides information about the status and settings of a job that imports endpoint definitions from one or more files. The files can be stored in an Amazon Simple Storage Service (Amazon S3) bucket or uploaded directly from a computer by using the Amazon Pinpoint console.

ApplicationId -> (string)

The unique identifier for the application thatâs associated with the import job.

CompletedPieces -> (integer)

The number of pieces that were processed successfully (completed) by the import job, as of the time of the request.

CompletionDate -> (string)

The date, in ISO 8601 format, when the import job was completed.

CreationDate -> (string)

The date, in ISO 8601 format, when the import job was created.

Definition -> (structure)

The resource settings that apply to the import job.

DefineSegment -> (boolean)

Specifies whether the import job creates a segment that contains the endpoints, when the endpoint definitions are imported.

ExternalId -> (string)

(Deprecated) Your AWS account ID, which you assigned to an external ID key in an IAM trust policy. Amazon Pinpoint previously used this value to assume an IAM role when importing endpoint definitions, but we removed this requirement. We donât recommend use of external IDs for IAM roles that are assumed by Amazon Pinpoint.

Format -> (string)

The format of the files that contain the endpoint definitions to import. Valid values are: CSV, for comma-separated values format; and, JSON, for newline-delimited JSON format.

If the files are stored in an Amazon S3 location and that location contains multiple files that use different formats, Amazon Pinpoint imports data only from the files that use the specified format.

RegisterEndpoints -> (boolean)

Specifies whether the import job registers the endpoints with Amazon Pinpoint, when the endpoint definitions are imported.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to access the Amazon S3 location to import endpoint definitions from.

S3Url -> (string)

The URL of the Amazon Simple Storage Service (Amazon S3) bucket that contains the endpoint definitions to import. This location can be a folder or a single file. If the location is a folder, Amazon Pinpoint imports endpoint definitions from the files in this location, including any subfolders that the folder contains.

The URL should be in the following format: s3://bucket-name/folder-name/file-name. The location can end with the key for an individual object or a prefix that qualifies multiple objects.

SegmentId -> (string)

The identifier for the segment that the import job updates or adds endpoint definitions to, if the import job updates an existing segment.

SegmentName -> (string)

The custom name for the segment thatâs created by the import job, if the value of the DefineSegment property is true.

FailedPieces -> (integer)

The number of pieces that werenât processed successfully (failed) by the import job, as of the time of the request.

Failures -> (list)

An array of entries, one for each of the first 100 entries that werenât processed successfully (failed) by the import job, if any.

(string)

Id -> (string)

The unique identifier for the import job.

JobStatus -> (string)

The status of the import job. The job status is FAILED if Amazon Pinpoint wasnât able to process one or more pieces in the job.

TotalFailures -> (integer)

The total number of endpoint definitions that werenât processed successfully (failed) by the import job, typically because an error, such as a syntax error, occurred.

TotalPieces -> (integer)

The total number of pieces that must be processed to complete the import job. Each piece consists of an approximately equal portion of the endpoint definitions that are part of the import job.

TotalProcessed -> (integer)

The total number of endpoint definitions that were processed by the import job.

Type -> (string)

The job type. This value is IMPORT for import jobs.