# get-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# get-job

## Description

Gets a Deadline Cloud job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/GetJob)

## Synopsis

```
get-job
--farm-id <value>
--queue-id <value>
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

`--farm-id` (string)

The farm ID of the farm in the job.

`--queue-id` (string)

The queue ID associated with the job.

`--job-id` (string)

The job ID.

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

The job ID.

name -> (string)

The name of the job.

lifecycleStatus -> (string)

The life cycle status for the job.

lifecycleStatusMessage -> (string)

A message that communicates the status of the life cycle for the job.

priority -> (integer)

The job priority.

createdAt -> (timestamp)

The date and time the resource was created.

createdBy -> (string)

The user or system that created this resource.

updatedAt -> (timestamp)

The date and time the resource was updated.

updatedBy -> (string)

The user or system that updated this resource.

startedAt -> (timestamp)

The date and time the resource started running.

endedAt -> (timestamp)

The date and time the resource ended running.

taskRunStatus -> (string)

The task run status for the job.

targetTaskRunStatus -> (string)

The task status with which the job started.

taskRunStatusCounts -> (map)

The number of tasks running on the job.

key -> (string)

value -> (integer)

storageProfileId -> (string)

The storage profile ID associated with the job.

maxFailedTasksCount -> (integer)

The number of task failures before the job stops running and is marked as `FAILED` .

maxRetriesPerTask -> (integer)

The maximum number of retries per failed tasks.

parameters -> (map)

The parameters for the job.

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

attachments -> (structure)

The attachments for the job.

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

description -> (string)

The description of the job.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

maxWorkerCount -> (integer)

The maximum number of worker hosts that can concurrently process a job. When the `maxWorkerCount` is reached, no more workers will be assigned to process the job, even if the fleets assigned to the jobâs queue has available workers.

If you donât set the `maxWorkerCount` when you create a job, this value is not returned in the response.

sourceJobId -> (string)

The job ID for the source job.