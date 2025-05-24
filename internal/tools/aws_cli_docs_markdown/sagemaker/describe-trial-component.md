# describe-trial-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-trial-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# describe-trial-component

## Description

Provides a list of a trials componentâs properties.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrialComponent)

## Synopsis

```
describe-trial-component
--trial-component-name <value>
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

The name of the trial component to describe.

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

TrialComponentName -> (string)

The name of the trial component.

TrialComponentArn -> (string)

The Amazon Resource Name (ARN) of the trial component.

DisplayName -> (string)

The name of the component as displayed. If `DisplayName` isnât specified, `TrialComponentName` is displayed.

Source -> (structure)

The Amazon Resource Name (ARN) of the source and, optionally, the job type.

SourceArn -> (string)

The source Amazon Resource Name (ARN).

SourceType -> (string)

The source job type.

Status -> (structure)

The status of the component. States include:

- InProgress
- Completed
- Failed

PrimaryStatus -> (string)

The status of the trial component.

Message -> (string)

If the component failed, a message describing why.

StartTime -> (timestamp)

When the component started.

EndTime -> (timestamp)

When the component ended.

CreationTime -> (timestamp)

When the component was created.

CreatedBy -> (structure)

Who created the trial component.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

When the component was last modified.

LastModifiedBy -> (structure)

Who last modified the component.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

Parameters -> (map)

The hyperparameters of the component.

key -> (string)

value -> (structure)

The value of a hyperparameter. Only one of `NumberValue` or `StringValue` can be specified.

This object is specified in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

StringValue -> (string)

The string value of a categorical hyperparameter. If you specify a value for this parameter, you canât specify the `NumberValue` parameter.

NumberValue -> (double)

The numeric value of a numeric hyperparameter. If you specify a value for this parameter, you canât specify the `StringValue` parameter.

InputArtifacts -> (map)

The input artifacts of the component.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

OutputArtifacts -> (map)

The output artifacts of the component.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

MetadataProperties -> (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

Metrics -> (list)

The metrics for the component.

(structure)

A summary of the metrics of a trial component.

MetricName -> (string)

The name of the metric.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source.

TimeStamp -> (timestamp)

When the metric was last updated.

Max -> (double)

The maximum value of the metric.

Min -> (double)

The minimum value of the metric.

Last -> (double)

The most recent value of the metric.

Count -> (integer)

The number of samples used to generate the metric.

Avg -> (double)

The average value of the metric.

StdDev -> (double)

The standard deviation of the metric.

LineageGroupArn -> (string)

The Amazon Resource Name (ARN) of the lineage group.

Sources -> (list)

A list of ARNs and, if applicable, job types for multiple sources of an experiment run.

(structure)

The Amazon Resource Name (ARN) and job type of the source of a trial component.

SourceArn -> (string)

The source Amazon Resource Name (ARN).

SourceType -> (string)

The source job type.