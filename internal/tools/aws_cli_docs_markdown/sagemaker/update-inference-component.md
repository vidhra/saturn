# update-inference-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-inference-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-inference-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-inference-component

## Description

Updates an inference component.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateInferenceComponent)

## Synopsis

```
update-inference-component
--inference-component-name <value>
[--specification <value>]
[--runtime-config <value>]
[--deployment-config <value>]
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

`--inference-component-name` (string)

The name of the inference component.

`--specification` (structure)

Details about the resources to deploy with this inference component, including the model, container, and compute resources.

ModelName -> (string)

The name of an existing SageMaker AI model object in your account that you want to deploy with the inference component.

Container -> (structure)

Defines a container that provides the runtime environment for a model that you deploy with an inference component.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where the Docker image for the model is stored.

ArtifactUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the Environment string-to-string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

StartupParameters -> (structure)

Settings that take effect while the model container starts up.

ModelDataDownloadTimeoutInSeconds -> (integer)

The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this inference component.

ContainerStartupHealthCheckTimeoutInSeconds -> (integer)

The timeout value, in seconds, for your inference container to pass health check by Amazon S3 Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests) .

ComputeResourceRequirements -> (structure)

The compute resources allocated to run the model, plus any adapter models, that you assign to the inference component.

Omit this parameter if your request is meant to create an adapter inference component. An adapter inference component is loaded by a base inference component, and it uses the compute resources of the base inference component.

NumberOfCpuCoresRequired -> (float)

The number of CPU cores to allocate to run a model that you assign to an inference component.

NumberOfAcceleratorDevicesRequired -> (float)

The number of accelerators to allocate to run a model that you assign to an inference component. Accelerators include GPUs and Amazon Web Services Inferentia.

MinMemoryRequiredInMb -> (integer)

The minimum MB of memory to allocate to run a model that you assign to an inference component.

MaxMemoryRequiredInMb -> (integer)

The maximum MB of memory to allocate to run a model that you assign to an inference component.

BaseInferenceComponentName -> (string)

The name of an existing inference component that is to contain the inference component that youâre creating with your request.

Specify this parameter only if your request is meant to create an adapter inference component. An adapter inference component contains the path to an adapter model. The purpose of the adapter model is to tailor the inference output of a base foundation model, which is hosted by the base inference component. The adapter inference component uses the compute resources that you assigned to the base inference component.

When you create an adapter inference component, use the `Container` parameter to specify the location of the adapter artifacts. In the parameter value, use the `ArtifactUrl` parameter of the `InferenceComponentContainerSpecification` data type.

Before you can create an adapter inference component, you must have an existing inference component that contains the foundation model that you want to adapt.

Shorthand Syntax:

```
ModelName=string,Container={Image=string,ArtifactUrl=string,Environment={KeyName1=string,KeyName2=string}},StartupParameters={ModelDataDownloadTimeoutInSeconds=integer,ContainerStartupHealthCheckTimeoutInSeconds=integer},ComputeResourceRequirements={NumberOfCpuCoresRequired=float,NumberOfAcceleratorDevicesRequired=float,MinMemoryRequiredInMb=integer,MaxMemoryRequiredInMb=integer},BaseInferenceComponentName=string
```

JSON Syntax:

```
{
  "ModelName": "string",
  "Container": {
    "Image": "string",
    "ArtifactUrl": "string",
    "Environment": {"string": "string"
      ...}
  },
  "StartupParameters": {
    "ModelDataDownloadTimeoutInSeconds": integer,
    "ContainerStartupHealthCheckTimeoutInSeconds": integer
  },
  "ComputeResourceRequirements": {
    "NumberOfCpuCoresRequired": float,
    "NumberOfAcceleratorDevicesRequired": float,
    "MinMemoryRequiredInMb": integer,
    "MaxMemoryRequiredInMb": integer
  },
  "BaseInferenceComponentName": "string"
}
```

`--runtime-config` (structure)

Runtime settings for a model that is deployed with an inference component.

CopyCount -> (integer)

The number of runtime copies of the model container to deploy with the inference component. Each copy can serve inference requests.

Shorthand Syntax:

```
CopyCount=integer
```

JSON Syntax:

```
{
  "CopyCount": integer
}
```

`--deployment-config` (structure)

The deployment configuration for the inference component. The configuration contains the desired deployment strategy and rollback settings.

RollingUpdatePolicy -> (structure)

Specifies a rolling deployment strategy for updating a SageMaker AI endpoint.

MaximumBatchSize -> (structure)

The batch size for each rolling step in the deployment process. For each step, SageMaker AI provisions capacity on the new endpoint fleet, routes traffic to that fleet, and terminates capacity on the old endpoint fleet. The value must be between 5% to 50% of the copy count of the inference component.

Type -> (string)

Specifies the endpoint capacity type.

COPY_COUNT

The endpoint activates based on the number of inference component copies.

CAPACITY_PERCENT

The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of inference component copies or a capacity percentage.

WaitIntervalInSeconds -> (integer)

The length of the baking period, during which SageMaker AI monitors alarms for each batch on the new fleet.

MaximumExecutionTimeoutInSeconds -> (integer)

The time limit for the total deployment. Exceeding this limit causes a timeout.

RollbackMaximumBatchSize -> (structure)

The batch size for a rollback to the old endpoint fleet. If this field is absent, the value is set to the default, which is 100% of the total capacity. When the default is used, SageMaker AI provisions the entire capacity of the old fleet at once during rollback.

Type -> (string)

Specifies the endpoint capacity type.

COPY_COUNT

The endpoint activates based on the number of inference component copies.

CAPACITY_PERCENT

The endpoint activates based on the specified percentage of capacity.

Value -> (integer)

Defines the capacity size, either as a number of inference component copies or a capacity percentage.

AutoRollbackConfiguration -> (structure)

Automatic rollback configuration for handling endpoint deployment failures and recovery.

Alarms -> (list)

List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.

(structure)

An Amazon CloudWatch alarm configured to monitor metrics on an endpoint.

AlarmName -> (string)

The name of a CloudWatch alarm in your account.

JSON Syntax:

```
{
  "RollingUpdatePolicy": {
    "MaximumBatchSize": {
      "Type": "COPY_COUNT"|"CAPACITY_PERCENT",
      "Value": integer
    },
    "WaitIntervalInSeconds": integer,
    "MaximumExecutionTimeoutInSeconds": integer,
    "RollbackMaximumBatchSize": {
      "Type": "COPY_COUNT"|"CAPACITY_PERCENT",
      "Value": integer
    }
  },
  "AutoRollbackConfiguration": {
    "Alarms": [
      {
        "AlarmName": "string"
      }
      ...
    ]
  }
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

InferenceComponentArn -> (string)

The Amazon Resource Name (ARN) of the inference component.