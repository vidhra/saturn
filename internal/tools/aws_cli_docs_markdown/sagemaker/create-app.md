# create-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-app

## Description

Creates a running app for the specified UserProfile. This operation is automatically invoked by Amazon SageMaker AI upon access to the associated Domain, and when new kernel configurations are selected by the user. A user may have multiple Apps active simultaneously.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateApp)

## Synopsis

```
create-app
--domain-id <value>
[--user-profile-name <value>]
[--space-name <value>]
--app-type <value>
--app-name <value>
[--tags <value>]
[--resource-spec <value>]
[--recovery-mode | --no-recovery-mode]
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

`--domain-id` (string)

The domain ID.

`--user-profile-name` (string)

The user profile name. If this value is not set, then `SpaceName` must be set.

`--space-name` (string)

The name of the space. If this value is not set, then `UserProfileName` must be set.

`--app-type` (string)

The type of app.

Possible values:

- `JupyterServer`
- `KernelGateway`
- `DetailedProfiler`
- `TensorBoard`
- `CodeEditor`
- `JupyterLab`
- `RStudioServerPro`
- `RSessionGateway`
- `Canvas`

`--app-name` (string)

The name of the app.

`--tags` (list)

Each tag consists of a key and an optional value. Tag keys must be unique per resource.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

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

`--resource-spec` (structure)

The instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.

### Note

The value of `InstanceType` passed as part of the `ResourceSpec` in the `CreateApp` call overrides the value passed as part of the `ResourceSpec` configured for the user profile or the domain. If `InstanceType` is not specified in any of those three `ResourceSpec` values for a `KernelGateway` app, the `CreateApp` call fails with a request validation error.

SageMakerImageArn -> (string)

The ARN of the SageMaker AI image that the image version belongs to.

SageMakerImageVersionArn -> (string)

The ARN of the image version created on the instance. To clear the value set for `SageMakerImageVersionArn` , pass `None` as the value.

SageMakerImageVersionAlias -> (string)

The SageMakerImageVersionAlias of the image to launch with. This value is in SemVer 2.0.0 versioning format.

InstanceType -> (string)

The instance type that the image version runs on.

### Note

**JupyterServer apps** only support the `system` value.

For **KernelGateway apps** , the `system` value is translated to `ml.t3.medium` . KernelGateway apps also support all other values for available instance types.

LifecycleConfigArn -> (string)

The Amazon Resource Name (ARN) of the Lifecycle Configuration attached to the Resource.

Shorthand Syntax:

```
SageMakerImageArn=string,SageMakerImageVersionArn=string,SageMakerImageVersionAlias=string,InstanceType=string,LifecycleConfigArn=string
```

JSON Syntax:

```
{
  "SageMakerImageArn": "string",
  "SageMakerImageVersionArn": "string",
  "SageMakerImageVersionAlias": "string",
  "InstanceType": "system"|"ml.t3.micro"|"ml.t3.small"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.m5d.large"|"ml.m5d.xlarge"|"ml.m5d.2xlarge"|"ml.m5d.4xlarge"|"ml.m5d.8xlarge"|"ml.m5d.12xlarge"|"ml.m5d.16xlarge"|"ml.m5d.24xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.p3.2xlarge"|"ml.p3.8xlarge"|"ml.p3.16xlarge"|"ml.p3dn.24xlarge"|"ml.g4dn.xlarge"|"ml.g4dn.2xlarge"|"ml.g4dn.4xlarge"|"ml.g4dn.8xlarge"|"ml.g4dn.12xlarge"|"ml.g4dn.16xlarge"|"ml.r5.large"|"ml.r5.xlarge"|"ml.r5.2xlarge"|"ml.r5.4xlarge"|"ml.r5.8xlarge"|"ml.r5.12xlarge"|"ml.r5.16xlarge"|"ml.r5.24xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.16xlarge"|"ml.g5.12xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.12xlarge"|"ml.g6.16xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.12xlarge"|"ml.g6e.16xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.geospatial.interactive"|"ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.trn1.2xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.p5.48xlarge"|"ml.p5en.48xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.c7i.large"|"ml.c7i.xlarge"|"ml.c7i.2xlarge"|"ml.c7i.4xlarge"|"ml.c7i.8xlarge"|"ml.c7i.12xlarge"|"ml.c7i.16xlarge"|"ml.c7i.24xlarge"|"ml.c7i.48xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge"|"ml.m6id.large"|"ml.m6id.xlarge"|"ml.m6id.2xlarge"|"ml.m6id.4xlarge"|"ml.m6id.8xlarge"|"ml.m6id.12xlarge"|"ml.m6id.16xlarge"|"ml.m6id.24xlarge"|"ml.m6id.32xlarge"|"ml.c6id.large"|"ml.c6id.xlarge"|"ml.c6id.2xlarge"|"ml.c6id.4xlarge"|"ml.c6id.8xlarge"|"ml.c6id.12xlarge"|"ml.c6id.16xlarge"|"ml.c6id.24xlarge"|"ml.c6id.32xlarge"|"ml.r6id.large"|"ml.r6id.xlarge"|"ml.r6id.2xlarge"|"ml.r6id.4xlarge"|"ml.r6id.8xlarge"|"ml.r6id.12xlarge"|"ml.r6id.16xlarge"|"ml.r6id.24xlarge"|"ml.r6id.32xlarge",
  "LifecycleConfigArn": "string"
}
```

`--recovery-mode` | `--no-recovery-mode` (boolean)

Indicates whether the application is launched in recovery mode.

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

AppArn -> (string)

The Amazon Resource Name (ARN) of the app.