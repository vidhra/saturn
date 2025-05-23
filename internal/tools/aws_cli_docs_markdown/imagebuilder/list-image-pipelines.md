# list-image-pipelinesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipelines.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# list-image-pipelines

## Description

Returns a list of image pipelines.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/ListImagePipelines)

## Synopsis

```
list-image-pipelines
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--filters` (list)

Use the following filters to streamline results:

- `description`
- `distributionConfigurationArn`
- `imageRecipeArn`
- `infrastructureConfigurationArn`
- `name`
- `status`

(structure)

A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

name -> (string)

The name of the filter. Filter names are case-sensitive.

values -> (list)

The filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum items to return in a request.

`--next-token` (string)

A token to specify where to start paginating. This is the nextToken from a previously truncated response.

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

requestId -> (string)

The request ID that uniquely identifies this request.

imagePipelineList -> (list)

The list of image pipelines.

(structure)

Details of an image pipeline.

arn -> (string)

The Amazon Resource Name (ARN) of the image pipeline.

name -> (string)

The name of the image pipeline.

description -> (string)

The description of the image pipeline.

platform -> (string)

The platform of the image pipeline.

enhancedImageMetadataEnabled -> (boolean)

Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

imageRecipeArn -> (string)

The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

containerRecipeArn -> (string)

The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

infrastructureConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

distributionConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

imageTestsConfiguration -> (structure)

The image tests configuration of the image pipeline.

imageTestsEnabled -> (boolean)

Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.

timeoutMinutes -> (integer)

The maximum time in minutes that tests are permitted to run.

### Note

The timeout property is not currently active. This value is ignored.

schedule -> (structure)

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

status -> (string)

The status of the image pipeline.

dateCreated -> (string)

The date on which this image pipeline was created.

dateUpdated -> (string)

The date on which this image pipeline was last updated.

dateLastRun -> (string)

This is no longer supported, and does not return a value.

dateNextRun -> (string)

The next date when the pipeline is scheduled to run.

tags -> (map)

The tags of this image pipeline.

key -> (string)

value -> (string)

imageScanningConfiguration -> (structure)

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

executionRole -> (string)

The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.

workflows -> (list)

Contains the workflows that run for the image pipeline.

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

nextToken -> (string)

The next token used for paginated responses. When this field isnât empty, there are additional elements that the service hasnât included in this request. Use this token with the next request to retrieve additional objects.