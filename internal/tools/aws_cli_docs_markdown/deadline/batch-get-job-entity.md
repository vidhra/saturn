# batch-get-job-entityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/batch-get-job-entity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/batch-get-job-entity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# batch-get-job-entity

## Description

Get batched job details for a worker.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/BatchGetJobEntity)

`batch-get-job-entity` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
batch-get-job-entity
--farm-id <value>
--fleet-id <value>
--worker-id <value>
--identifiers <value>
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

`--farm-id` (string)

The farm ID of the worker thatâs fetching job details. The worker must have an assignment on a job to fetch job details.

`--fleet-id` (string)

The fleet ID of the worker thatâs fetching job details. The worker must have an assignment on a job to fetch job details.

`--worker-id` (string)

The worker ID of the worker containing the job details to get.

`--identifiers` (list)

The job identifiers to include within the job entity batch details.

(tagged union structure)

The details of a job entity identifier.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `jobDetails`, `jobAttachmentDetails`, `stepDetails`, `environmentDetails`.

jobDetails -> (structure)

The job details.

jobId -> (string)

The job ID.

jobAttachmentDetails -> (structure)

The job attachment details.

jobId -> (string)

The job ID.

stepDetails -> (structure)

The step details.

jobId -> (string)

The job ID.

stepId -> (string)

The step ID.

environmentDetails -> (structure)

The environment details.

jobId -> (string)

The job ID.

environmentId -> (string)

The environment ID.

Shorthand Syntax:

```
jobDetails={jobId=string},jobAttachmentDetails={jobId=string},stepDetails={jobId=string,stepId=string},environmentDetails={jobId=string,environmentId=string} ...
```

JSON Syntax:

```
[
  {
    "jobDetails": {
      "jobId": "string"
    },
    "jobAttachmentDetails": {
      "jobId": "string"
    },
    "stepDetails": {
      "jobId": "string",
      "stepId": "string"
    },
    "environmentDetails": {
      "jobId": "string",
      "environmentId": "string"
    }
  }
  ...
]
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

entities -> (list)

A list of the job entities, or details, in the batch.

(tagged union structure)

The details of a job entity.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `jobDetails`, `jobAttachmentDetails`, `stepDetails`, `environmentDetails`.

jobDetails -> (structure)

The job details.

jobId -> (string)

The job ID.

jobAttachmentSettings -> (structure)

The job attachment settings.

s3BucketName -> (string)

The Amazon S3 bucket name.

rootPrefix -> (string)

The root prefix.

jobRunAsUser -> (structure)

The user name and group that the job uses when run.

posix -> (structure)

The user and group that the jobs in the queue run as.

user -> (string)

The name of the POSIX user.

group -> (string)

The name of the POSIX userâs group.

windows -> (structure)

Identifies a Microsoft Windows user.

user -> (string)

The user.

passwordArn -> (string)

The password ARN for the Windows user.

runAs -> (string)

Specifies whether the job should run using the queueâs system user or if the job should run using the worker agent system user.

logGroupName -> (string)

The log group name.

queueRoleArn -> (string)

The queue role ARN.

parameters -> (map)

The parameters.

key -> (string)

value -> (tagged union structure)

The details of job parameters.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `int`, `float`, `string`, `path`.

int -> (string)

A signed integer represented as a string.

float -> (string)

A double precision IEEE-754 floating point number represented as a string.

string -> (string)

A UTF-8 string.

path -> (string)

A file system path represented as a string.

schemaVersion -> (string)

The schema version.

pathMappingRules -> (list)

The path mapping rules.

(structure)

The details of a source and destination path.

sourcePathFormat -> (string)

The source path format.

sourcePath -> (string)

The source path.

destinationPath -> (string)

The destination path.

jobAttachmentDetails -> (structure)

The job attachment details.

jobId -> (string)

The job ID.

attachments -> (structure)

The job attachments.

manifests -> (list)

A list of manifests which describe job attachment configurations.

(structure)

The details of the manifest that links a jobâs source information.

fileSystemLocationName -> (string)

The file system location name.

rootPath -> (string)

The fileâs root path.

rootPathFormat -> (string)

The format of the root path.

outputRelativeDirectories -> (list)

The file path relative to the directory.

(string)

inputManifestPath -> (string)

The file path.

inputManifestHash -> (string)

The hash value of the file.

fileSystem -> (string)

The file system.

stepDetails -> (structure)

The step details.

jobId -> (string)

The job ID.

stepId -> (string)

The step ID.

schemaVersion -> (string)

The schema version for a step template.

template -> (document)

The template for a step.

dependencies -> (list)

The dependencies for a step.

(string)

environmentDetails -> (structure)

The environment details for the job entity.

jobId -> (string)

The job ID.

environmentId -> (string)

The environment ID.

schemaVersion -> (string)

The schema version in the environment.

template -> (document)

The template used for the environment.

errors -> (list)

A list of errors from the job error logs for the batch.

(tagged union structure)

The error for the job entity.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `jobDetails`, `jobAttachmentDetails`, `stepDetails`, `environmentDetails`.

jobDetails -> (structure)

The job details for the failed job entity.

jobId -> (string)

The job ID.

code -> (string)

The error code.

message -> (string)

The error message detailing the errorâs cause.

jobAttachmentDetails -> (structure)

The job attachment details for the failed job entity.

jobId -> (string)

The job ID.

code -> (string)

The error code.

message -> (string)

The error message detailing the errorâs cause.

stepDetails -> (structure)

The step details for the failed job entity.

jobId -> (string)

The job ID.

stepId -> (string)

The step ID.

code -> (string)

The error code.

message -> (string)

The error message detailing the errorâs cause.

environmentDetails -> (structure)

The environment details for the failed job entity.

jobId -> (string)

The job ID.

environmentId -> (string)

The environment ID.

code -> (string)

The error code.

message -> (string)

The error message detailing the errorâs cause.