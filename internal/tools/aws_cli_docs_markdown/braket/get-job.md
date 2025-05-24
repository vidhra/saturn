# get-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/get-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [braket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/braket/index.html#cli-aws-braket) ]

# get-job

## Description

Retrieves the specified Amazon Braket job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/braket-2019-09-01/GetJob)

## Synopsis

```
get-job
[--additional-attribute-names <value>]
--job-arn <value>
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

`--additional-attribute-names` (list)

A list of attributes to return information for.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  QueueInfo
```

`--job-arn` (string)

The ARN of the job to retrieve.

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

algorithmSpecification -> (structure)

Definition of the Amazon Braket job created. Specifies the container image the job uses, information about the Python scripts used for entry and training, and the user-defined metrics used to evaluation the job.

containerImage -> (structure)

The container image used to create an Amazon Braket job.

uri -> (string)

The URI locating the container image.

scriptModeConfig -> (structure)

Configures the paths to the Python scripts used for entry and training.

compressionType -> (string)

The type of compression used by the Python scripts for an Amazon Braket job.

entryPoint -> (string)

The path to the Python script that serves as the entry point for an Amazon Braket job.

s3Uri -> (string)

The URI that specifies the S3 path to the Python script module that contains the training script used by an Amazon Braket job.

associations -> (list)

The list of Amazon Braket resources associated with the hybrid job.

(structure)

The Amazon Braket resource and the association type.

arn -> (string)

The Amazon Braket resource arn.

type -> (string)

The association type for the specified Amazon Braket resource arn.

billableDuration -> (integer)

The billable time the Amazon Braket job used to complete.

checkpointConfig -> (structure)

Information about the output locations for job checkpoint data.

localPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/braket/checkpoints/` .

s3Uri -> (string)

Identifies the S3 path where you want Amazon Braket to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

createdAt -> (timestamp)

The date and time that the Amazon Braket job was created.

deviceConfig -> (structure)

The quantum processing unit (QPU) or simulator used to run the Amazon Braket job.

device -> (string)

The primary quantum processing unit (QPU) or simulator used to create and run an Amazon Braket job.

endedAt -> (timestamp)

The date and time that the Amazon Braket job ended.

events -> (list)

Details about the type and time events occurred related to the Amazon Braket job.

(structure)

Details about the type and time events occurred related to the Amazon Braket job.

eventType -> (string)

The type of event that occurred related to the Amazon Braket job.

message -> (string)

A message describing the event that occurred related to the Amazon Braket job.

timeOfEvent -> (timestamp)

The type of event that occurred related to the Amazon Braket job.

failureReason -> (string)

A description of the reason why an Amazon Braket job failed, if it failed.

hyperParameters -> (map)

Algorithm-specific parameters used by an Amazon Braket job that influence the quality of the traiing job. The values are set with a string of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of th hyperparameter.

key -> (string)

value -> (string)

inputDataConfig -> (list)

A list of parameters that specify the name and type of input data and where it is located.

(structure)

A list of parameters that specify the input channels, type of input data, and where it is located.

channelName -> (string)

A named input source that an Amazon Braket job can consume.

contentType -> (string)

The MIME type of the data.

dataSource -> (structure)

The location of the channel data.

s3DataSource -> (structure)

Information about the data stored in Amazon S3 used by the Amazon Braket job.

s3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest that locates the S3 data source.

instanceConfig -> (structure)

The resource instances to use while running the hybrid job on Amazon Braket.

instanceCount -> (integer)

Configures the number of resource instances to use while running an Amazon Braket job on Amazon Braket. The default value is 1.

instanceType -> (string)

Configures the type resource instances to use while running an Amazon Braket hybrid job.

volumeSizeInGb -> (integer)

The size of the storage volume, in GB, that user wants to provision.

jobArn -> (string)

The ARN of the Amazon Braket job.

jobName -> (string)

The name of the Amazon Braket job.

outputDataConfig -> (structure)

The path to the S3 location where job artifacts are stored and the encryption key used to store them there.

kmsKeyId -> (string)

The AWS Key Management Service (AWS KMS) key that Amazon Braket uses to encrypt the job training artifacts at rest using Amazon S3 server-side encryption.

s3Path -> (string)

Identifies the S3 path where you want Amazon Braket to store the job training artifacts. For example, `s3://bucket-name/key-name-prefix` .

queueInfo -> (structure)

Queue information for the requested job. Only returned if `QueueInfo` is specified in the `additionalAttributeNames"` field in the `GetJob` API request.

message -> (string)

Optional. Provides more information about the queue position. For example, if the job is complete and no longer in the queue, the message field contains that information.

position -> (string)

Current position of the job in the jobs queue.

queue -> (string)

The name of the queue.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output resources to the s3 buckets of a user.

startedAt -> (timestamp)

The date and time that the Amazon Braket job was started.

status -> (string)

The status of the Amazon Braket job.

stoppingCondition -> (structure)

The user-defined criteria that specifies when to stop a job running.

maxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that an Amazon Braket job can run.

tags -> (map)

A tag object that consists of a key and an optional value, used to manage metadata for Amazon Braket resources.

key -> (string)

value -> (string)