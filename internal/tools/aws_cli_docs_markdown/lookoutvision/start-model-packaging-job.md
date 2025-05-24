# start-model-packaging-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model-packaging-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/start-model-packaging-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# start-model-packaging-job

## Description

Starts an Amazon Lookout for Vision model packaging job. A model packaging job creates an AWS IoT Greengrass component for a Lookout for Vision model. You can use the component to deploy your model to an edge device managed by Greengrass.

Use the  DescribeModelPackagingJob API to determine the current status of the job. The model packaging job is complete if the value of `Status` is `SUCCEEDED` .

To deploy the component to the target device, use the component name and component version with the AWS IoT Greengrass [CreateDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_CreateDeployment.html) API.

This operation requires the following permissions:

- `lookoutvision:StartModelPackagingJob`
- `s3:PutObject`
- `s3:GetBucketLocation`
- `kms:GenerateDataKey`
- `greengrass:CreateComponentVersion`
- `greengrass:DescribeComponent`
- (Optional) `greengrass:TagResource` . Only required if you want to tag the component.

For more information, see *Using your Amazon Lookout for Vision model on an edge device* in the Amazon Lookout for Vision Developer Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/StartModelPackagingJob)

## Synopsis

```
start-model-packaging-job
--project-name <value>
--model-version <value>
[--job-name <value>]
--configuration <value>
[--description <value>]
[--client-token <value>]
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

`--project-name` (string)

The name of the project which contains the version of the model that you want to package.

`--model-version` (string)

The version of the model within the project that you want to package.

`--job-name` (string)

A name for the model packaging job. If you donât supply a value, the service creates a job name for you.

`--configuration` (structure)

The configuration for the model packaging job.

Greengrass -> (structure)

Configuration information for the AWS IoT Greengrass component in a model packaging job.

CompilerOptions -> (string)

Additional compiler options for the Greengrass component. Currently, only NVIDIA Graphics Processing Units (GPU) and CPU accelerators are supported. If you specify `TargetDevice` , donât specify `CompilerOptions` .

For more information, see *Compiler options* in the Amazon Lookout for Vision Developer Guide.

TargetDevice -> (string)

The target device for the model. Currently the only supported value is `jetson_xavier` . If you specify `TargetDevice` , you canât specify `TargetPlatform` .

TargetPlatform -> (structure)

The target platform for the model. If you specify `TargetPlatform` , you canât specify `TargetDevice` .

Os -> (string)

The target operating system for the model. Linux is the only operating system that is currently supported.

Arch -> (string)

The target architecture for the model. The currently supported architectures are X86_64 (64-bit version of the x86 instruction set) and ARM_64 (ARMv8 64-bit CPU).

Accelerator -> (string)

The target accelerator for the model. Currently, Amazon Lookout for Vision only supports NVIDIA (Nvidia graphics processing unit) and CPU accelerators. If you specify NVIDIA as an accelerator, you must also specify the `gpu-code` , `trt-ver` , and `cuda-ver` compiler options. If you donât specify an accelerator, Lookout for Vision uses the CPU for compilation and we highly recommend that you use the  GreengrassConfiguration$CompilerOptions field. For example, you can use the following compiler options for CPU:

- `mcpu` : CPU micro-architecture. For example, `{'mcpu': 'skylake-avx512'}`
- `mattr` : CPU flags. For example, `{'mattr': ['+neon', '+vfpv4']}`

S3OutputLocation -> (structure)

An S3 location in which Lookout for Vision stores the component artifacts.

Bucket -> (string)

The S3 bucket that contains the training or model packaging job output. If you are training a model, the bucket must in your AWS account. If you use an S3 bucket for a model packaging job, the S3 bucket must be in the same AWS Region and AWS account in which you use AWS IoT Greengrass.

Prefix -> (string)

The path of the folder, within the S3 bucket, that contains the output.

ComponentName -> (string)

A name for the AWS IoT Greengrass component.

ComponentVersion -> (string)

A Version for the AWS IoT Greengrass component. If you donât provide a value, a default value of `` *Model Version* .0.0`` is used.

ComponentDescription -> (string)

A description for the AWS IoT Greengrass component.

Tags -> (list)

A set of tags (key-value pairs) that you want to attach to the AWS IoT Greengrass component.

(structure)

A key and value pair that is attached to the specified Amazon Lookout for Vision model.

Key -> (string)

The key of the tag that is attached to the specified model.

Value -> (string)

The value of the tag that is attached to the specified model.

JSON Syntax:

```
{
  "Greengrass": {
    "CompilerOptions": "string",
    "TargetDevice": "jetson_xavier",
    "TargetPlatform": {
      "Os": "LINUX",
      "Arch": "ARM64"|"X86_64",
      "Accelerator": "NVIDIA"
    },
    "S3OutputLocation": {
      "Bucket": "string",
      "Prefix": "string"
    },
    "ComponentName": "string",
    "ComponentVersion": "string",
    "ComponentDescription": "string",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
  }
}
```

`--description` (string)

A description for the model packaging job.

`--client-token` (string)

ClientToken is an idempotency token that ensures a call to `StartModelPackagingJob` completes only once. You choose the value to pass. For example, An issue might prevent you from getting a response from `StartModelPackagingJob` . In this case, safely retry your call to `StartModelPackagingJob` by using the same `ClientToken` parameter value.

If you donât supply a value for `ClientToken` , the AWS SDK you are using inserts a value for you. This prevents retries after a network error from making multiple dataset creation requests. Youâll need to provide your own value for other use cases.

An error occurs if the other input parameters are not the same as in the first request. Using a different value for `ClientToken` is considered a new call to `StartModelPackagingJob` . An idempotency token is active for 8 hours.

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

JobName -> (string)

The job name for the model packaging job. If you donât supply a job name in the `JobName` input parameter, the service creates a job name for you.