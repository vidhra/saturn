# list-inference-schedulersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-inference-schedulers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/list-inference-schedulers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# list-inference-schedulers

## Description

Retrieves a list of all inference schedulers currently available for your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/ListInferenceSchedulers)

## Synopsis

```
list-inference-schedulers
[--next-token <value>]
[--max-results <value>]
[--inference-scheduler-name-begins-with <value>]
[--model-name <value>]
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

An opaque pagination token indicating where to continue the listing of inference schedulers.

`--max-results` (integer)

Specifies the maximum number of inference schedulers to list.

`--inference-scheduler-name-begins-with` (string)

The beginning of the name of the inference schedulers to be listed.

`--model-name` (string)

The name of the machine learning model used by the inference scheduler to be listed.

`--status` (string)

Specifies the current status of the inference schedulers.

Possible values:

- `PENDING`
- `RUNNING`
- `STOPPING`
- `STOPPED`

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

An opaque pagination token indicating where to continue the listing of inference schedulers.

InferenceSchedulerSummaries -> (list)

Provides information about the specified inference scheduler, including data upload frequency, model name and ARN, and status.

(structure)

Contains information about the specific inference scheduler, including data delay offset, model name and ARN, status, and so on.

ModelName -> (string)

The name of the machine learning model used for the inference scheduler.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the machine learning model used by the inference scheduler.

InferenceSchedulerName -> (string)

The name of the inference scheduler.

InferenceSchedulerArn -> (string)

The Amazon Resource Name (ARN) of the inference scheduler.

Status -> (string)

Indicates the status of the inference scheduler.

DataDelayOffsetInMinutes -> (long)

A period of time (in minutes) by which inference on the data is delayed after the data starts. For instance, if an offset delay time of five minutes was selected, inference will not begin on the data until the first data measurement after the five minute mark. For example, if five minutes is selected, the inference scheduler will wake up at the configured frequency with the additional five minute delay time to check the customer S3 bucket. The customer can upload data at the same frequency and they donât need to stop and restart the scheduler when uploading new data.

DataUploadFrequency -> (string)

How often data is uploaded to the source S3 bucket for the input data. This value is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment starts a scheduled inference on your data. In this example, it starts once every 5 minutes.

LatestInferenceResult -> (string)

Indicates whether the latest execution for the inference scheduler was Anomalous (anomalous events found) or Normal (no anomalous events found).