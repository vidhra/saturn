# create-trial-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-trial-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-trial-component

## Description

Creates a *trial component* , which is a stage of a machine learning *trial* . A trial is composed of one or more trial components. A trial component can be used in multiple trials.

Trial components include pre-processing jobs, training jobs, and batch transform jobs.

When you use SageMaker Studio or the SageMaker Python SDK, all experiments, trials, and trial components are automatically tracked, logged, and indexed. When you use the Amazon Web Services SDK for Python (Boto), you must use the logging APIs provided by the SDK.

You can add tags to a trial component and then use the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search for the tags.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTrialComponent)

## Synopsis

```
create-trial-component
--trial-component-name <value>
[--display-name <value>]
[--status <value>]
[--start-time <value>]
[--end-time <value>]
[--parameters <value>]
[--input-artifacts <value>]
[--output-artifacts <value>]
[--metadata-properties <value>]
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

`--trial-component-name` (string)

The name of the component. The name must be unique in your Amazon Web Services account and is not case-sensitive.

`--display-name` (string)

The name of the component as displayed. The name doesnât need to be unique. If `DisplayName` isnât specified, `TrialComponentName` is displayed.

`--status` (structure)

The status of the component. States include:

- InProgress
- Completed
- Failed

PrimaryStatus -> (string)

The status of the trial component.

Message -> (string)

If the component failed, a message describing why.

Shorthand Syntax:

```
PrimaryStatus=string,Message=string
```

JSON Syntax:

```
{
  "PrimaryStatus": "InProgress"|"Completed"|"Failed"|"Stopping"|"Stopped",
  "Message": "string"
}
```

`--start-time` (timestamp)

When the component started.

`--end-time` (timestamp)

When the component ended.

`--parameters` (map)

The hyperparameters for the component.

key -> (string)

value -> (structure)

The value of a hyperparameter. Only one of `NumberValue` or `StringValue` can be specified.

This object is specified in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

StringValue -> (string)

The string value of a categorical hyperparameter. If you specify a value for this parameter, you canât specify the `NumberValue` parameter.

NumberValue -> (double)

The numeric value of a numeric hyperparameter. If you specify a value for this parameter, you canât specify the `StringValue` parameter.

Shorthand Syntax:

```
KeyName1=StringValue=string,NumberValue=double,KeyName2=StringValue=string,NumberValue=double
```

JSON Syntax:

```
{"string": {
      "StringValue": "string",
      "NumberValue": double
    }
  ...}
```

`--input-artifacts` (map)

The input artifacts for the component. Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

Shorthand Syntax:

```
KeyName1=MediaType=string,Value=string,KeyName2=MediaType=string,Value=string
```

JSON Syntax:

```
{"string": {
      "MediaType": "string",
      "Value": "string"
    }
  ...}
```

`--output-artifacts` (map)

The output artifacts for the component. Examples of output artifacts are metrics, snapshots, logs, and images.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

Shorthand Syntax:

```
KeyName1=MediaType=string,Value=string,KeyName2=MediaType=string,Value=string
```

JSON Syntax:

```
{"string": {
      "MediaType": "string",
      "Value": "string"
    }
  ...}
```

`--metadata-properties` (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

Shorthand Syntax:

```
CommitId=string,Repository=string,GeneratedBy=string,ProjectId=string
```

JSON Syntax:

```
{
  "CommitId": "string",
  "Repository": "string",
  "GeneratedBy": "string",
  "ProjectId": "string"
}
```

`--tags` (list)

A list of tags to associate with the component. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.

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

TrialComponentArn -> (string)

The Amazon Resource Name (ARN) of the trial component.