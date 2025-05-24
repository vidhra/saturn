# describe-flow-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-flow-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-flow-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-flow-definition

## Description

Returns information about the specified flow definition.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeFlowDefinition)

## Synopsis

```
describe-flow-definition
--flow-definition-name <value>
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

`--flow-definition-name` (string)

The name of the flow definition.

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

FlowDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the flow defintion.

FlowDefinitionName -> (string)

The Amazon Resource Name (ARN) of the flow definition.

FlowDefinitionStatus -> (string)

The status of the flow definition. Valid values are listed below.

CreationTime -> (timestamp)

The timestamp when the flow definition was created.

HumanLoopRequestSource -> (structure)

Container for configuring the source of human task requests. Used to specify if Amazon Rekognition or Amazon Textract is used as an integration source.

AwsManagedHumanLoopRequestSource -> (string)

Specifies whether Amazon Rekognition or Amazon Textract are used as the integration source. The default field settings and JSON parsing rules are different based on the integration source. Valid values:

HumanLoopActivationConfig -> (structure)

An object containing information about what triggers a human review workflow.

HumanLoopActivationConditionsConfig -> (structure)

Container structure for defining under what conditions SageMaker creates a human loop.

HumanLoopActivationConditions -> (string)

JSON expressing use-case specific conditions declaratively. If any condition is matched, atomic tasks are created against the configured work team. The set of conditions is different for Rekognition and Textract. For more information about how to structure the JSON, see [JSON Schema for Human Loop Activation Conditions in Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-human-fallback-conditions-json-schema.html) in the *Amazon SageMaker Developer Guide* .

HumanLoopConfig -> (structure)

An object containing information about who works on the task, the workforce task price, and other task details.

WorkteamArn -> (string)

Amazon Resource Name (ARN) of a team of workers. To learn more about the types of workforces and work teams you can create and use with Amazon A2I, see [Create and Manage Workforces](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html) .

HumanTaskUiArn -> (string)

The Amazon Resource Name (ARN) of the human task user interface.

You can use standard HTML and Crowd HTML Elements to create a custom worker task template. You use this template to create a human task UI.

To learn how to create a custom HTML template, see [Create Custom Worker Task Template](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-custom-templates.html) .

To learn how to create a human task UI, which is a worker task template that can be used in a flow definition, see [Create and Delete a Worker Task Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-worker-template-console.html) .

TaskTitle -> (string)

A title for the human worker task.

TaskDescription -> (string)

A description for the human worker task.

TaskCount -> (integer)

The number of distinct workers who will perform the same task on each object. For example, if `TaskCount` is set to `3` for an image classification labeling job, three workers will classify each input image. Increasing `TaskCount` can improve label accuracy.

TaskAvailabilityLifetimeInSeconds -> (integer)

The length of time that a task remains available for review by human workers.

TaskTimeLimitInSeconds -> (integer)

The amount of time that a worker has to complete a task. The default value is 3,600 seconds (1 hour).

TaskKeywords -> (list)

Keywords used to describe the task so that workers can discover the task.

(string)

PublicWorkforceTaskPrice -> (structure)

Defines the amount of money paid to an Amazon Mechanical Turk worker for each task performed.

Use one of the following prices for bounding box tasks. Prices are in US dollars and should be based on the complexity of the task; the longer it takes in your initial testing, the more you should offer.

- 0.036
- 0.048
- 0.060
- 0.072
- 0.120
- 0.240
- 0.360
- 0.480
- 0.600
- 0.720
- 0.840
- 0.960
- 1.080
- 1.200

Use one of the following prices for image classification, text classification, and custom tasks. Prices are in US dollars.

- 0.012
- 0.024
- 0.036
- 0.048
- 0.060
- 0.072
- 0.120
- 0.240
- 0.360
- 0.480
- 0.600
- 0.720
- 0.840
- 0.960
- 1.080
- 1.200

Use one of the following prices for semantic segmentation tasks. Prices are in US dollars.

- 0.840
- 0.960
- 1.080
- 1.200

Use one of the following prices for Textract AnalyzeDocument Important Form Key Amazon Augmented AI review tasks. Prices are in US dollars.

- 2.400
- 2.280
- 2.160
- 2.040
- 1.920
- 1.800
- 1.680
- 1.560
- 1.440
- 1.320
- 1.200
- 1.080
- 0.960
- 0.840
- 0.720
- 0.600
- 0.480
- 0.360
- 0.240
- 0.120
- 0.072
- 0.060
- 0.048
- 0.036
- 0.024
- 0.012

Use one of the following prices for Rekognition DetectModerationLabels Amazon Augmented AI review tasks. Prices are in US dollars.

- 1.200
- 1.080
- 0.960
- 0.840
- 0.720
- 0.600
- 0.480
- 0.360
- 0.240
- 0.120
- 0.072
- 0.060
- 0.048
- 0.036
- 0.024
- 0.012

Use one of the following prices for Amazon Augmented AI custom human review tasks. Prices are in US dollars.

- 1.200
- 1.080
- 0.960
- 0.840
- 0.720
- 0.600
- 0.480
- 0.360
- 0.240
- 0.120
- 0.072
- 0.060
- 0.048
- 0.036
- 0.024
- 0.012

AmountInUsd -> (structure)

Defines the amount of money paid to an Amazon Mechanical Turk worker in United States dollars.

Dollars -> (integer)

The whole number of dollars in the amount.

Cents -> (integer)

The fractional portion, in cents, of the amount.

TenthFractionsOfACent -> (integer)

Fractions of a cent, in tenths.

OutputConfig -> (structure)

An object containing information about the output file.

S3OutputPath -> (string)

The Amazon S3 path where the object containing human output will be made available.

To learn more about the format of Amazon A2I output data, see [Amazon A2I Output Data](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-output-data.html) .

KmsKeyId -> (string)

The Amazon Key Management Service (KMS) key ID for server-side encryption.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) execution role for the flow definition.

FailureReason -> (string)

The reason your flow definition failed.