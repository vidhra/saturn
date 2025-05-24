# list-inference-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-inference-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-inference-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# list-inference-executions

## Description

Lists all inference executions that have been performed by the specified inference scheduler.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/ListInferenceExecutions)

## Synopsis

```
list-inference-executions
[--next-token <value>]
[--max-results <value>]
--inference-scheduler-name <value>
[--data-start-time-after <value>]
[--data-end-time-before <value>]
[--status <value>]
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

`--next-token` (string)

An opaque pagination token indicating where to continue the listing of inference executions.

`--max-results` (integer)

Specifies the maximum number of inference executions to list.

`--inference-scheduler-name` (string)

The name of the inference scheduler for the inference execution listed.

`--data-start-time-after` (timestamp)

The time reference in the inferenced dataset after which Amazon Lookout for Equipment started the inference execution.

`--data-end-time-before` (timestamp)

The time reference in the inferenced dataset before which Amazon Lookout for Equipment stopped the inference execution.

`--status` (string)

The status of the inference execution.

Possible values:

- `IN_PROGRESS`
- `SUCCESS`
- `FAILED`

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

NextToken -> (string)

An opaque pagination token indicating where to continue the listing of inference executions.

InferenceExecutionSummaries -> (list)

Provides an array of information about the individual inference executions returned from the `ListInferenceExecutions` operation, including model used, inference scheduler, data configuration, and so on.

### Note

If you donât supply the `InferenceSchedulerName` request parameter, or if you supply the name of an inference scheduler that doesnât exist, `ListInferenceExecutions` returns an empty array in `InferenceExecutionSummaries` .

(structure)

Contains information about the specific inference execution, including input and output data configuration, inference scheduling information, status, and so on.

ModelName -> (string)

The name of the machine learning model being used for the inference execution.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the machine learning model used for the inference execution.

InferenceSchedulerName -> (string)

The name of the inference scheduler being used for the inference execution.

InferenceSchedulerArn -> (string)

The Amazon Resource Name (ARN) of the inference scheduler being used for the inference execution.

ScheduledStartTime -> (timestamp)

Indicates the start time at which the inference scheduler began the specific inference execution.

DataStartTime -> (timestamp)

Indicates the time reference in the dataset at which the inference execution began.

DataEndTime -> (timestamp)

Indicates the time reference in the dataset at which the inference execution stopped.

DataInputConfiguration -> (structure)

Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.

S3InputConfiguration -> (structure)

Specifies configuration information for the input data for the inference, including Amazon S3 location of input data.

Bucket -> (string)

The bucket containing the input dataset for the inference.

Prefix -> (string)

The prefix for the S3 bucket used for the input data for the inference.

InputTimeZoneOffset -> (string)

Indicates the difference between your time zone and Coordinated Universal Time (UTC).

InferenceInputNameConfiguration -> (structure)

Specifies configuration information for the input data for the inference, including timestamp format and delimiter.

TimestampFormat -> (string)

The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).

ComponentTimestampDelimiter -> (string)

Indicates the delimiter character used between items in the data.

DataOutputConfiguration -> (structure)

Specifies configuration information for the output results from for the inference execution, including the output Amazon S3 location.

S3OutputConfiguration -> (structure)

Specifies configuration information for the output results from for the inference, output S3 location.

Bucket -> (string)

The bucket containing the output results from the inference

Prefix -> (string)

The prefix for the S3 bucket used for the output results from the inference.

KmsKeyId -> (string)

The ID number for the KMS key key used to encrypt the inference output.

CustomerResultObject -> (structure)

The S3 object that the inference execution results were uploaded to.

Bucket -> (string)

The name of the specific S3 bucket.

Key -> (string)

The Amazon Web Services Key Management Service (KMS key) key being used to encrypt the S3 object. Without this key, data in the bucket is not accessible.

Status -> (string)

Indicates the status of the inference execution.

FailedReason -> (string)

Specifies the reason for failure when an inference execution has failed.

ModelVersion -> (long)

The model version used for the inference execution.

ModelVersionArn -> (string)

The Amazon Resource Number (ARN) of the model version used for the inference execution.