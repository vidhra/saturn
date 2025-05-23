# list-snomedct-inference-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-snomedct-inference-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/list-snomedct-inference-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehendmedical](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehendmedical/index.html#cli-aws-comprehendmedical) ]

# list-snomedct-inference-jobs

## Description

Gets a list of InferSNOMEDCT jobs a user has submitted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehendmedical-2018-10-30/ListSNOMEDCTInferenceJobs)

## Synopsis

```
list-snomedct-inference-jobs
[--filter <value>]
[--next-token <value>]
[--max-results <value>]
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

`--filter` (structure)

Provides information for filtering a list of detection jobs.

JobName -> (string)

Filters on the name of the job.

JobStatus -> (string)

Filters the list of jobs based on job status. Returns only jobs with the specified status.

SubmitTimeBefore -> (timestamp)

Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.

SubmitTimeAfter -> (timestamp)

Filters the list of jobs based on the time that the job was submitted for processing. Returns only jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.

Shorthand Syntax:

```
JobName=string,JobStatus=string,SubmitTimeBefore=timestamp,SubmitTimeAfter=timestamp
```

JSON Syntax:

```
{
  "JobName": "string",
  "JobStatus": "SUBMITTED"|"IN_PROGRESS"|"COMPLETED"|"PARTIAL_SUCCESS"|"FAILED"|"STOP_REQUESTED"|"STOPPED",
  "SubmitTimeBefore": timestamp,
  "SubmitTimeAfter": timestamp
}
```

`--next-token` (string)

Identifies the next page of InferSNOMEDCT results to return.

`--max-results` (integer)

The maximum number of results to return in each page. The default is 100.

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

**To list all SNOMED CT inference jobs**

The following example shows how the `list-snomedct-inference-jobs` operation returns a list of current asynchronous SNOMED CT batch inference jobs.

```
aws comprehendmedical list-snomedct-inference-jobs
```

Output:

```
{
    "ComprehendMedicalAsyncJobPropertiesList": [
        {
            "JobId": "5780034166536cdb52ffa3295a1b00a7",
            "JobStatus": "COMPLETED",
            "SubmitTime": "2020-05-19T20:38:37.594000+00:00",
            "EndTime": "2020-05-19T20:45:07.894000+00:00",
            "ExpirationTime": "2020-09-17T20:38:37+00:00",
            "InputDataConfig": {
                "S3Bucket": "comp-med-input",
                "S3Key": "AKIAIOSFODNN7EXAMPLE"
            },
            "OutputDataConfig": {
                "S3Bucket": "comp-med-output",
                "S3Key": "AKIAIOSFODNN7EXAMPLE"
            },
            "LanguageCode": "en",
            "DataAccessRoleArn": "arn:aws:iam::867139942017:role/ComprehendMedicalBatchProcessingRole",
            "ModelVersion":  "0.1.0"
        }
    ]
}
```

For more information, see [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html) in the *Amazon Comprehend Medical Developer Guide*.

## Output

ComprehendMedicalAsyncJobPropertiesList -> (list)

A list containing the properties of each job that is returned.

(structure)

Provides information about a detection job.

JobId -> (string)

The identifier assigned to the detection job.

JobName -> (string)

The name that you assigned to the detection job.

JobStatus -> (string)

The current status of the detection job. If the status is `FAILED` , the `Message` field shows the reason for the failure.

Message -> (string)

A description of the status of a job.

SubmitTime -> (timestamp)

The time that the detection job was submitted for processing.

EndTime -> (timestamp)

The time that the detection job completed.

ExpirationTime -> (timestamp)

The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the `ListEntitiesDetectionV2Job` or the `ListPHIDetectionJobs` operation.

InputDataConfig -> (structure)

The input data configuration that you supplied when you created the detection job.

S3Bucket -> (string)

The URI of the S3 bucket that contains the input data. The bucket must be in the same region as the API endpoint that you are calling.

S3Key -> (string)

The path to the input data files in the S3 bucket.

OutputDataConfig -> (structure)

The output data configuration that you supplied when you created the detection job.

S3Bucket -> (string)

When you use the `OutputDataConfig` object with asynchronous operations, you specify the Amazon S3 location where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. The location is used as the prefix for the actual location of the output.

S3Key -> (string)

The path to the output data files in the S3 bucket. Amazon Comprehend Medical creates an output directory using the job ID so that the output from one job does not overwrite the output of another.

LanguageCode -> (string)

The language code of the input documents.

DataAccessRoleArn -> (string)

The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.

ManifestFilePath -> (string)

The path to the file that describes the results of a batch job.

KMSKey -> (string)

The AWS Key Management Service key, if any, used to encrypt the output files.

ModelVersion -> (string)

The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.

NextToken -> (string)

Identifies the next page of results to return.