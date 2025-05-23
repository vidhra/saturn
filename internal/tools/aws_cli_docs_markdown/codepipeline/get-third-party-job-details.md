# get-third-party-job-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-third-party-job-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-third-party-job-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# get-third-party-job-details

## Description

Requests the details of a job for a third party action. Used for partner actions only.

### Warning

When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/GetThirdPartyJobDetails)

## Synopsis

```
get-third-party-job-details
--job-id <value>
--client-token <value>
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

`--job-id` (string)

The unique system-generated ID used for identifying the job.

`--client-token` (string)

The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.

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

jobDetails -> (structure)

The details of the job, including any protected values defined for the job.

id -> (string)

The identifier used to identify the job details in CodePipeline.

data -> (structure)

The data to be returned by the third party job worker.

actionTypeId -> (structure)

Represents information about an action type.

category -> (string)

A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Valid categories are limited to one of the following values.

- Source
- Build
- Test
- Deploy
- Invoke
- Approval
- Compute

owner -> (string)

The creator of the action being called. There are three valid values for the `Owner` field in the action category section within your pipeline structure: `AWS` , `ThirdParty` , and `Custom` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

provider -> (string)

The provider of the service being called by the action. Valid providers are determined by the action category. For example, an action in the Deploy category type might have a provider of CodeDeploy, which would be specified as `CodeDeploy` . For more information, see [Valid Action Types and Providers in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#actions-valid-providers) .

version -> (string)

A string that describes the action version.

actionConfiguration -> (structure)

Represents information about an action configuration.

configuration -> (map)

The configuration data for the action.

key -> (string)

value -> (string)

pipelineContext -> (structure)

Represents information about a pipeline to a job worker.

### Note

Does not include `pipelineArn` and `pipelineExecutionId` for ThirdParty jobs.

pipelineName -> (string)

The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.

stage -> (structure)

The stage of the pipeline.

name -> (string)

The name of the stage.

action -> (structure)

The context of an action to a job worker in the stage of a pipeline.

name -> (string)

The name of the action in the context of a job.

actionExecutionId -> (string)

The system-generated unique ID that corresponds to an actionâs execution.

pipelineArn -> (string)

The Amazon Resource Name (ARN) of the pipeline.

pipelineExecutionId -> (string)

The execution ID of the pipeline.

inputArtifacts -> (list)

The name of the artifact that is worked on by the action, if any. This name might be system-generated, such as âMyAppâ, or it might be defined by the user when the action is created. The input artifact name must match the name of an output artifact generated by an action in an earlier action or stage of the pipeline.

(structure)

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

name -> (string)

The artifactâs name.

revision -> (string)

The artifactâs revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location -> (structure)

The location of an artifact.

type -> (string)

The type of artifact in the location.

s3Location -> (structure)

The S3 bucket that contains the artifact.

bucketName -> (string)

The name of the S3 bucket.

objectKey -> (string)

The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.

outputArtifacts -> (list)

The name of the artifact that is the result of the action, if any. This name might be system-generated, such as âMyBuiltAppâ, or it might be defined by the user when the action is created.

(structure)

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp_Windows.zip

name -> (string)

The artifactâs name.

revision -> (string)

The artifactâs revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).

location -> (structure)

The location of an artifact.

type -> (string)

The type of artifact in the location.

s3Location -> (structure)

The S3 bucket that contains the artifact.

bucketName -> (string)

The name of the S3 bucket.

objectKey -> (string)

The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.

artifactCredentials -> (structure)

Represents an Amazon Web Services session credentials object. These credentials are temporary credentials that are issued by Amazon Web Services Secure Token Service (STS). They can be used to access input and output artifacts in the S3 bucket used to store artifact for the pipeline in CodePipeline.

accessKeyId -> (string)

The access key for the session.

secretAccessKey -> (string)

The secret access key for the session.

sessionToken -> (string)

The token for the session.

continuationToken -> (string)

A system-generated token, such as a CodeDeploy deployment ID, that a job requires to continue the job asynchronously.

encryptionKey -> (structure)

The encryption key used to encrypt and decrypt data in the artifact store for the pipeline, such as an Amazon Web Services Key Management Service (Amazon Web Services KMS) key. This is optional and might not be present.

id -> (string)

The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.

### Note

Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).

type -> (string)

The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to âKMSâ.

nonce -> (string)

A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Use this number in an  AcknowledgeThirdPartyJob request.