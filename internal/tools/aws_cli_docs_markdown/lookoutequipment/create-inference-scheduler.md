# create-inference-schedulerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/create-inference-scheduler.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/create-inference-scheduler.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutequipment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutequipment/index.html#cli-aws-lookoutequipment) ]

# create-inference-scheduler

## Description

Creates a scheduled inference. Scheduling an inference is setting up a continuous real-time inference plan to analyze new measurement data. When setting up the schedule, you provide an S3 bucket location for the input data, assign it a delimiter between separate entries in the data, set an offset delay if desired, and set the frequency of inferencing. You must also provide an S3 bucket location for the output data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-15/CreateInferenceScheduler)

## Synopsis

```
create-inference-scheduler
--model-name <value>
--inference-scheduler-name <value>
[--data-delay-offset-in-minutes <value>]
--data-upload-frequency <value>
--data-input-configuration <value>
--data-output-configuration <value>
--role-arn <value>
[--server-side-kms-key-id <value>]
[--client-token <value>]
[--tags <value>]
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

`--model-name` (string)

The name of the previously trained machine learning model being used to create the inference scheduler.

`--inference-scheduler-name` (string)

The name of the inference scheduler being created.

`--data-delay-offset-in-minutes` (long)

The interval (in minutes) of planned delay at the start of each inference segment. For example, if inference is set to run every ten minutes, the delay is set to five minutes and the time is 09:08. The inference scheduler will wake up at the configured interval (which, without a delay configured, would be 09:10) plus the additional five minute delay time (so 09:15) to check your Amazon S3 bucket. The delay provides a buffer for you to upload data at the same frequency, so that you donât have to stop and restart the scheduler when uploading new data.

For more information, see [Understanding the inference process](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html) .

`--data-upload-frequency` (string)

How often data is uploaded to the source Amazon S3 bucket for the input data. The value chosen is the length of time between data uploads. For instance, if you select 5 minutes, Amazon Lookout for Equipment will upload the real-time data to the source bucket once every 5 minutes. This frequency also determines how often Amazon Lookout for Equipment runs inference on your data.

For more information, see [Understanding the inference process](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-inference-process.html) .

Possible values:

- `PT5M`
- `PT10M`
- `PT15M`
- `PT30M`
- `PT1H`

`--data-input-configuration` (structure)

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

Shorthand Syntax:

```
S3InputConfiguration={Bucket=string,Prefix=string},InputTimeZoneOffset=string,InferenceInputNameConfiguration={TimestampFormat=string,ComponentTimestampDelimiter=string}
```

JSON Syntax:

```
{
  "S3InputConfiguration": {
    "Bucket": "string",
    "Prefix": "string"
  },
  "InputTimeZoneOffset": "string",
  "InferenceInputNameConfiguration": {
    "TimestampFormat": "string",
    "ComponentTimestampDelimiter": "string"
  }
}
```

`--data-output-configuration` (structure)

Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.

S3OutputConfiguration -> (structure)

Specifies configuration information for the output results from for the inference, output S3 location.

Bucket -> (string)

The bucket containing the output results from the inference

Prefix -> (string)

The prefix for the S3 bucket used for the output results from the inference.

KmsKeyId -> (string)

The ID number for the KMS key key used to encrypt the inference output.

Shorthand Syntax:

```
S3OutputConfiguration={Bucket=string,Prefix=string},KmsKeyId=string
```

JSON Syntax:

```
{
  "S3OutputConfiguration": {
    "Bucket": "string",
    "Prefix": "string"
  },
  "KmsKeyId": "string"
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference.

`--server-side-kms-key-id` (string)

Provides the identifier of the KMS key used to encrypt inference scheduler data by Amazon Lookout for Equipment.

`--client-token` (string)

A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one.

`--tags` (list)

Any tags associated with the inference scheduler.

(structure)

A tag is a key-value pair that can be added to a resource as metadata.

Key -> (string)

The key for the specified tag.

Value -> (string)

The value for the specified tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

InferenceSchedulerArn -> (string)

The Amazon Resource Name (ARN) of the inference scheduler being created.

InferenceSchedulerName -> (string)

The name of inference scheduler being created.

Status -> (string)

Indicates the status of the `CreateInferenceScheduler` operation.

ModelQuality -> (string)

Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is `POOR_QUALITY_DETECTED` . Otherwise, the value is `QUALITY_THRESHOLD_MET` .

If the model is unlabeled, the model quality canât be assessed and the value of `ModelQuality` is `CANNOT_DETERMINE_QUALITY` . In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.

For information about using labels with your models, see [Understanding labeling](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/understanding-labeling.html) .

For information about improving the quality of a model, see [Best practices with Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html) .