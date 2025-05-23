# list-fhir-import-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-import-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-import-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [healthlake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html#cli-aws-healthlake) ]

# list-fhir-import-jobs

## Description

Lists all FHIR import jobs associated with an account and their statuses.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/healthlake-2017-07-01/ListFHIRImportJobs)

## Synopsis

```
list-fhir-import-jobs
--datastore-id <value>
[--next-token <value>]
[--max-results <value>]
[--job-name <value>]
[--job-status <value>]
[--submitted-before <value>]
[--submitted-after <value>]
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

`--datastore-id` (string)

This parameter limits the response to the import job with the specified data store ID.

`--next-token` (string)

A pagination token used to identify the next page of results to return for a ListFHIRImportJobs query.

`--max-results` (integer)

This parameter limits the number of results returned for a ListFHIRImportJobs to a maximum quantity specified by the user.

`--job-name` (string)

This parameter limits the response to the import job with the specified job name.

`--job-status` (string)

This parameter limits the response to the import job with the specified job status.

Possible values:

- `SUBMITTED`
- `QUEUED`
- `IN_PROGRESS`
- `COMPLETED_WITH_ERRORS`
- `COMPLETED`
- `FAILED`
- `CANCEL_SUBMITTED`
- `CANCEL_IN_PROGRESS`
- `CANCEL_COMPLETED`
- `CANCEL_FAILED`

`--submitted-before` (timestamp)

This parameter limits the response to FHIR import jobs submitted before a user specified date.

`--submitted-after` (timestamp)

This parameter limits the response to FHIR import jobs submitted after a user specified date.

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

**To list all FHIR import jobs**

The following `list-fhir-import-jobs` example shows how to use the command to view a list of all import jobs associated with an account.

```
aws healthlake list-fhir-import-jobs \
    --datastore-id (Data store ID) \
    --submitted-before (DATE like 2024-10-13T19:00:00Z) \
    --submitted-after (DATE like 2020-10-13T19:00:00Z ) \
    --job-name "FHIR-IMPORT" \
    --job-status SUBMITTED  \
    -max-results (Integer between 1 and 500)
```

Output:

```
{
    "ImportJobPropertiesList": [
        {
            "JobId": "c0fddbf76f238297632d4aebdbfc9ddf",
            "JobStatus": "COMPLETED",
            "SubmitTime": "2024-11-20T10:08:46.813000-05:00",
            "EndTime": "2024-11-20T10:10:09.093000-05:00",
            "DatastoreId": "(Data store ID)",
            "InputDataConfig": {
                "S3Uri": "s3://(Bucket Name)/(Prefix Name)/"
            },
            "JobOutputDataConfig": {
                "S3Configuration": {
                    "S3Uri": "s3://(Bucket Name)/import/6407b9ae4c2def3cb6f1a46a0c599ec0-FHIR_IMPORT-c0fddbf76f238297632d4aebdbfc9ddf/",
                    "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/b7f645cb-e564-4981-8672-9e012d1ff1a0"
                }
            },
            "JobProgressReport": {
                "TotalNumberOfScannedFiles": 1,
                "TotalSizeOfScannedFilesInMB": 0.001798,
                "TotalNumberOfImportedFiles": 1,
                "TotalNumberOfResourcesScanned": 1,
                "TotalNumberOfResourcesImported": 1,
                "TotalNumberOfResourcesWithCustomerError": 0,
                "TotalNumberOfFilesReadWithCustomerError": 0,
                "Throughput": 0.0
            },
            "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)"
        }
    ]
}
```

For more information, see [Importing files to FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/import-examples.html) in the AWS HealthLake Developer Guide.

## Output

ImportJobPropertiesList -> (list)

The properties of a listed FHIR import jobs, including the ID, ARN, name, the status of the job, and the progress report of the job.

(structure)

Displays the properties of the import job, including the ID, Arn, Name, the status of the job, and the progress report of the job.

JobId -> (string)

The AWS-generated id number for the Import job.

JobName -> (string)

The user-generated name for an Import job.

JobStatus -> (string)

The job status for an Import job. Possible statuses are SUBMITTED, IN_PROGRESS, COMPLETED_WITH_ERRORS, COMPLETED, FAILED.

SubmitTime -> (timestamp)

The time that the Import job was submitted for processing.

EndTime -> (timestamp)

The time that the Import job was completed.

DatastoreId -> (string)

The datastore id used when the Import job was created.

InputDataConfig -> (tagged union structure)

The input data configuration that was supplied when the Import job was created.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `S3Uri`.

S3Uri -> (string)

The S3Uri is the user specified S3 location of the FHIR data to be imported into AWS HealthLake.

JobOutputDataConfig -> (tagged union structure)

The output data configuration that was supplied when the export job was created.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `S3Configuration`.

S3Configuration -> (structure)

The output data configuration that was supplied when the export job was created.

S3Uri -> (string)

The S3Uri is the user specified S3 location of the FHIR data to be imported into AWS HealthLake.

KmsKeyId -> (string)

The KMS key ID used to access the S3 bucket.

JobProgressReport -> (structure)

Displays the progress of the import job, including total resources scanned, total resources ingested, and total size of data ingested.

TotalNumberOfScannedFiles -> (long)

The number of files scanned from input S3 bucket.

TotalSizeOfScannedFilesInMB -> (double)

The size (in MB) of the files scanned from the input S3 bucket.

TotalNumberOfImportedFiles -> (long)

The number of files imported so far.

TotalNumberOfResourcesScanned -> (long)

The number of resources scanned from the input S3 bucket.

TotalNumberOfResourcesImported -> (long)

The number of resources imported so far.

TotalNumberOfResourcesWithCustomerError -> (long)

The number of resources that failed due to customer error.

TotalNumberOfFilesReadWithCustomerError -> (long)

The number of files that failed to be read from the input S3 bucket due to customer error.

Throughput -> (double)

The throughput (in MB/sec) of the import job.

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) that gives AWS HealthLake access to your input data.

Message -> (string)

An explanation of any errors that may have occurred during the FHIR import job.

NextToken -> (string)

A pagination token used to identify the next page of results to return for a ListFHIRImportJobs query.