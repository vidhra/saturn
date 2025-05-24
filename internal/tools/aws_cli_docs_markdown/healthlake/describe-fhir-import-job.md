# describe-fhir-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [healthlake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html#cli-aws-healthlake) ]

# describe-fhir-import-job

## Description

Displays the properties of a FHIR import job, including the ID, ARN, name, and the status of the job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/healthlake-2017-07-01/DescribeFHIRImportJob)

## Synopsis

```
describe-fhir-import-job
--datastore-id <value>
--job-id <value>
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

The AWS-generated ID of the data store.

`--job-id` (string)

The AWS-generated job ID.

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

**To describe a FHIR import job**

The following `describe-fhir-import-job` example shows how to learn the properties of a FHIR import job using AWS HealthLake.

```
aws healthlake describe-fhir-import-job \
    --datastore-id (Data store ID) \
    --job-id c145fbb27b192af392f8ce6e7838e34f
```

Output:

```
{
    "ImportJobProperties": {
    "InputDataConfig": {
        "S3Uri": "s3://(Bucket Name)/(Prefix Name)/"
        { "arrayitem2": 2 }
    },
    "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)",
    "JobStatus": "COMPLETED",
    "JobId": "c145fbb27b192af392f8ce6e7838e34f",
    "SubmitTime": 1606272542.161,
    "EndTime": 1606272609.497,
    "DatastoreId": "(Data store ID)"
    }
}
```

For more information, see [Importing files to a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/import-datastore.html) in the *AWS HealthLake Developer Guide*.

## Output

ImportJobProperties -> (structure)

The properties of the Import job request, including the ID, ARN, name, status of the job, and the progress report of the job.

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