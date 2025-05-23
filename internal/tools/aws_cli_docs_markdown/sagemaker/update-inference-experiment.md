# update-inference-experimentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-inference-experiment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-inference-experiment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-inference-experiment

## Description

Updates an inference experiment that you created. The status of the inference experiment has to be either `Created` , `Running` . For more information on the status of an inference experiment, see [DescribeInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateInferenceExperiment)

## Synopsis

```
update-inference-experiment
--name <value>
[--schedule <value>]
[--description <value>]
[--model-variants <value>]
[--data-storage-config <value>]
[--shadow-mode-config <value>]
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

`--name` (string)

The name of the inference experiment to be updated.

`--schedule` (structure)

The duration for which the inference experiment will run. If the status of the inference experiment is `Created` , then you can update both the start and end dates. If the status of the inference experiment is `Running` , then you can update only the end date.

StartTime -> (timestamp)

The timestamp at which the inference experiment started or will start.

EndTime -> (timestamp)

The timestamp at which the inference experiment ended or will end.

Shorthand Syntax:

```
StartTime=timestamp,EndTime=timestamp
```

JSON Syntax:

```
{
  "StartTime": timestamp,
  "EndTime": timestamp
}
```

`--description` (string)

The description of the inference experiment.

`--model-variants` (list)

An array of `ModelVariantConfig` objects. There is one for each variant, whose infrastructure configuration you want to update.

(structure)

Contains information about the deployment options of a model.

ModelName -> (string)

The name of the Amazon SageMaker Model entity.

VariantName -> (string)

The name of the variant.

InfrastructureConfig -> (structure)

The configuration for the infrastructure that the model will be deployed to.

InfrastructureType -> (string)

The inference option to which to deploy your model. Possible values are the following:

- `RealTime` : Deploy to real-time inference.

RealTimeInferenceConfig -> (structure)

The infrastructure configuration for deploying the model to real-time inference.

InstanceType -> (string)

The instance type the model is deployed to.

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` .

Shorthand Syntax:

```
ModelName=string,VariantName=string,InfrastructureConfig={InfrastructureType=string,RealTimeInferenceConfig={InstanceType=string,InstanceCount=integer}} ...
```

JSON Syntax:

```
[
  {
    "ModelName": "string",
    "VariantName": "string",
    "InfrastructureConfig": {
      "InfrastructureType": "RealTimeInference",
      "RealTimeInferenceConfig": {
        "InstanceType": "ml.t2.medium"|"ml.t2.large"|"ml.t2.xlarge"|"ml.t2.2xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m4.xlarge"|"ml.m4.2xlarge"|"ml.m4.4xlarge"|"ml.m4.10xlarge"|"ml.m4.16xlarge"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.12xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c4.xlarge"|"ml.c4.2xlarge"|"ml.c4.4xlarge"|"ml.c4.8xlarge"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.18xlarge"|"ml.c5d.xlarge"|"ml.c5d.2xlarge"|"ml.c5d.4xlarge"|"ml.c5d.9xlarge"|"ml.c5d.18xlarge"|"ml.p2.xlarge"|"ml.p2.8xlarge"|"ml.p2.16xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.inf1.xlarge"|"ml.inf1.2xlarge"|"ml.inf1.6xlarge"|"ml.inf1.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.inf2.xlarge"|"ml.inf2.8xlarge"|"ml.inf2.24xlarge"|"ml.inf2.48xlarge"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge",
        "InstanceCount": integer
      }
    }
  }
  ...
]
```

`--data-storage-config` (structure)

The Amazon S3 location and configuration for storing inference request and response data.

Destination -> (string)

The Amazon S3 bucket where the inference request and response data is stored.

KmsKey -> (string)

The Amazon Web Services Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.

ContentType -> (structure)

Configuration specifying how to treat different headers. If no headers are specified Amazon SageMaker AI will by default base64 encode when capturing the data.

CsvContentTypes -> (list)

The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.

(string)

JsonContentTypes -> (list)

The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.

(string)

Shorthand Syntax:

```
Destination=string,KmsKey=string,ContentType={CsvContentTypes=[string,string],JsonContentTypes=[string,string]}
```

JSON Syntax:

```
{
  "Destination": "string",
  "KmsKey": "string",
  "ContentType": {
    "CsvContentTypes": ["string", ...],
    "JsonContentTypes": ["string", ...]
  }
}
```

`--shadow-mode-config` (structure)

The configuration of `ShadowMode` inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates.

SourceModelVariantName -> (string)

The name of the production variant, which takes all the inference requests.

ShadowModelVariants -> (list)

List of shadow variant configurations.

(structure)

The name and sampling percentage of a shadow variant.

ShadowModelVariantName -> (string)

The name of the shadow variant.

SamplingPercentage -> (integer)

The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant.

Shorthand Syntax:

```
SourceModelVariantName=string,ShadowModelVariants=[{ShadowModelVariantName=string,SamplingPercentage=integer},{ShadowModelVariantName=string,SamplingPercentage=integer}]
```

JSON Syntax:

```
{
  "SourceModelVariantName": "string",
  "ShadowModelVariants": [
    {
      "ShadowModelVariantName": "string",
      "SamplingPercentage": integer
    }
    ...
  ]
}
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

InferenceExperimentArn -> (string)

The ARN of the updated inference experiment.