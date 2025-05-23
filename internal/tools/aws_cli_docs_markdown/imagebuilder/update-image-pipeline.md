# update-image-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# update-image-pipeline

## Description

Updates an image pipeline. Image pipelines enable you to automate the creation and distribution of images. You must specify exactly one recipe for your image, using either a `containerRecipeArn` or an `imageRecipeArn` .

### Note

UpdateImagePipeline does not support selective updates for the pipeline. You must specify all of the required properties in the update request, not just the properties that have changed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/UpdateImagePipeline)

## Synopsis

```
update-image-pipeline
--image-pipeline-arn <value>
[--description <value>]
[--image-recipe-arn <value>]
[--container-recipe-arn <value>]
--infrastructure-configuration-arn <value>
[--distribution-configuration-arn <value>]
[--image-tests-configuration <value>]
[--enhanced-image-metadata-enabled | --no-enhanced-image-metadata-enabled]
[--schedule <value>]
[--status <value>]
[--client-token <value>]
[--image-scanning-configuration <value>]
[--workflows <value>]
[--execution-role <value>]
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

`--image-pipeline-arn` (string)

The Amazon Resource Name (ARN) of the image pipeline that you want to update.

`--description` (string)

The description of the image pipeline.

`--image-recipe-arn` (string)

The Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.

`--container-recipe-arn` (string)

The Amazon Resource Name (ARN) of the container pipeline to update.

`--infrastructure-configuration-arn` (string)

The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images that this image pipeline has updated.

`--distribution-configuration-arn` (string)

The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images that this image pipeline has updated.

`--image-tests-configuration` (structure)

The image test configuration of the image pipeline.

imageTestsEnabled -> (boolean)

Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.

timeoutMinutes -> (integer)

The maximum time in minutes that tests are permitted to run.

### Note

The timeout property is not currently active. This value is ignored.

Shorthand Syntax:

```
imageTestsEnabled=boolean,timeoutMinutes=integer
```

JSON Syntax:

```
{
  "imageTestsEnabled": true|false,
  "timeoutMinutes": integer
}
```

`--enhanced-image-metadata-enabled` | `--no-enhanced-image-metadata-enabled` (boolean)

Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

`--schedule` (structure)

The schedule of the image pipeline.

scheduleExpression -> (string)

The cron expression determines how often EC2 Image Builder evaluates your `pipelineExecutionStartCondition` .

For information on how to format a cron expression in Image Builder, see [Use cron expressions in EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html) .

timezone -> (string)

The timezone that applies to the scheduling expression. For example, âEtc/UTCâ, âAmerica/Los_Angelesâ in the [IANA timezone format](https://www.joda.org/joda-time/timezones.html) . If not specified this defaults to UTC.

pipelineExecutionStartCondition -> (string)

The start condition configures when the pipeline should trigger a new image build, as follows. If no value is set Image Builder defaults to `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` .

- `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` (default) â When you use semantic version filters on the base image or components in your image recipe, EC2 Image Builder builds a new image only when there are new versions of the base image or components in your recipe that match the filter.

### Note

For semantic version syntax, see [CreateComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html) .

- `EXPRESSION_MATCH_ONLY` â This condition builds a new image every time the CRON expression matches the current time.

Shorthand Syntax:

```
scheduleExpression=string,timezone=string,pipelineExecutionStartCondition=string
```

JSON Syntax:

```
{
  "scheduleExpression": "string",
  "timezone": "string",
  "pipelineExecutionStartCondition": "EXPRESSION_MATCH_ONLY"|"EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
}
```

`--status` (string)

The status of the image pipeline.

Possible values:

- `DISABLED`
- `ENABLED`

`--client-token` (string)

Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference* .

`--image-scanning-configuration` (structure)

Contains settings for vulnerability scans.

imageScanningEnabled -> (boolean)

A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

ecrConfiguration -> (structure)

Contains Amazon ECR settings for vulnerability scans.

repositoryName -> (string)

The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you donât provide this information, Image Builder creates a repository in your account named `image-builder-image-scanning-repository` for vulnerability scans of your output container images.

containerTags -> (list)

Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.

(string)

Shorthand Syntax:

```
imageScanningEnabled=boolean,ecrConfiguration={repositoryName=string,containerTags=[string,string]}
```

JSON Syntax:

```
{
  "imageScanningEnabled": true|false,
  "ecrConfiguration": {
    "repositoryName": "string",
    "containerTags": ["string", ...]
  }
}
```

`--workflows` (list)

Contains the workflows to run for the pipeline.

(structure)

Contains control settings and configurable inputs for a workflow resource.

workflowArn -> (string)

The Amazon Resource Name (ARN) of the workflow resource.

parameters -> (list)

Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.

(structure)

Contains a key/value pair that sets the named workflow parameter.

name -> (string)

The name of the workflow parameter to set.

value -> (list)

Sets the value for the named workflow parameter.

(string)

parallelGroup -> (string)

Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.

onFailure -> (string)

The action to take if the workflow fails.

JSON Syntax:

```
[
  {
    "workflowArn": "string",
    "parameters": [
      {
        "name": "string",
        "value": ["string", ...]
      }
      ...
    ],
    "parallelGroup": "string",
    "onFailure": "CONTINUE"|"ABORT"
  }
  ...
]
```

`--execution-role` (string)

The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update an image pipeline**

The following `update-image-pipeline` example updates an image pipeline using a JSON file.

```
aws imagebuilder update-image-pipeline \
    --cli-input-json file://update-image-pipeline.json
```

Contents of `update-image-pipeline.json`:

```
{
    "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline",
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure",
    "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution",
    "imageTestsConfiguration": {
        "imageTestsEnabled": true,
        "timeoutMinutes": 120
    },
    "schedule": {
        "scheduleExpression": "cron(0 0 * * MON)",
        "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
    },
    "status": "DISABLED"
}
```

Output:

```
{
    "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html) in the *EC2 Image Builder Users Guide*.

## Output

requestId -> (string)

The request ID that uniquely identifies this request.

clientToken -> (string)

The client token that uniquely identifies the request.

imagePipelineArn -> (string)

The Amazon Resource Name (ARN) of the image pipeline that was updated by this request.