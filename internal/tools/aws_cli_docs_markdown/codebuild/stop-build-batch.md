# stop-build-batchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# stop-build-batch

## Description

Stops a running batch build.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/StopBuildBatch)

## Synopsis

```
stop-build-batch
--id <value>
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

`--id` (string)

The identifier of the batch build to stop.

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

**To stop an in-progress batch build in AWS CodeBuild.**

The following `stop-build-batch` example stops the specified batch build.

```
aws codebuild stop-build-batch \
    --id <project-name>:<batch-ID>
```

Output:

```
{
    "buildBatch": {
        "id": "<project-name>:<batch-ID>",
        "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build-batch/<project-name>:<batch-ID>",
        "startTime": "2020-10-21T16:54:24.740000+00:00",
        "endTime": "2020-10-21T16:56:05.152000+00:00",
        "currentPhase": "STOPPED",
        "buildBatchStatus": "STOPPED",
        "resolvedSourceVersion": "aef7744ed069c51098e15c360f4102cd2cd1ad64",
        "projectName": "<project-name>",
        "phases": [
            {
                "phaseType": "SUBMITTED",
                "phaseStatus": "SUCCEEDED",
                "startTime": "2020-10-21T16:54:24.740000+00:00",
                "endTime": "2020-10-21T16:54:25.039000+00:00",
                "durationInSeconds": 0
            },
            {
                "phaseType": "DOWNLOAD_BATCHSPEC",
                "phaseStatus": "SUCCEEDED",
                "startTime": "2020-10-21T16:54:25.039000+00:00",
                "endTime": "2020-10-21T16:54:56.583000+00:00",
                "durationInSeconds": 31
            },
            {
                "phaseType": "IN_PROGRESS",
                "phaseStatus": "STOPPED",
                "startTime": "2020-10-21T16:54:56.583000+00:00",
                "endTime": "2020-10-21T16:56:05.152000+00:00",
                "durationInSeconds": 68
            },
            {
                "phaseType": "STOPPED",
                "startTime": "2020-10-21T16:56:05.152000+00:00"
            }
        ],
        "source": {
            "type": "GITHUB",
            "location": "<GitHub-repo-URL>",
            "gitCloneDepth": 1,
            "gitSubmodulesConfig": {
                "fetchSubmodules": false
            },
            "reportBuildStatus": false,
            "insecureSsl": false
        },
        "secondarySources": [],
        "secondarySourceVersions": [],
        "artifacts": {
            "location": ""
        },
        "secondaryArtifacts": [],
        "cache": {
            "type": "NO_CACHE"
        },
        "environment": {
            "type": "LINUX_CONTAINER",
            "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0",
            "computeType": "BUILD_GENERAL1_SMALL",
            "environmentVariables": [],
            "privilegedMode": false,
            "imagePullCredentialsType": "CODEBUILD"
        },
        "logConfig": {
            "cloudWatchLogs": {
                "status": "ENABLED"
            },
            "s3Logs": {
                "status": "DISABLED",
                "encryptionDisabled": false
            }
        },
        "buildTimeoutInMinutes": 60,
        "queuedTimeoutInMinutes": 480,
        "complete": true,
        "initiator": "Strohm",
        "encryptionKey": "arn:aws:kms:<region-ID>:<account-ID>:alias/aws/s3",
        "buildBatchNumber": 3,
        "buildBatchConfig": {
            "serviceRole": "arn:aws:iam::<account-ID>:role/service-role/<project-name>",
            "restrictions": {
                "maximumBuildsAllowed": 100
            },
            "timeoutInMins": 480
        },
        "buildGroups": [
            {
                "identifier": "DOWNLOAD_SOURCE",
                "ignoreFailure": false,
                "currentBuildSummary": {
                    "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>",
                    "requestedOn": "2020-10-21T16:54:25.468000+00:00",
                    "buildStatus": "SUCCEEDED",
                    "primaryArtifact": {
                        "type": "no_artifacts",
                        "identifier": "DOWNLOAD_SOURCE"
                    },
                    "secondaryArtifacts": []
                }
            },
            {
                "identifier": "linux_small",
                "dependsOn": [],
                "ignoreFailure": false,
                "currentBuildSummary": {
                    "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>",
                    "requestedOn": "2020-10-21T16:54:56.833000+00:00",
                    "buildStatus": "IN_PROGRESS"
                }
            },
            {
                "identifier": "linux_medium",
                "dependsOn": [
                    "linux_small"
                ],
                "ignoreFailure": false,
                "currentBuildSummary": {
                    "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>",
                    "requestedOn": "2020-10-21T16:54:56.211000+00:00",
                    "buildStatus": "PENDING"
                }
            },
            {
                "identifier": "linux_large",
                "dependsOn": [
                    "linux_medium"
                ],
                "ignoreFailure": false,
                "currentBuildSummary": {
                    "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>",
                    "requestedOn": "2020-10-21T16:54:56.330000+00:00",
                    "buildStatus": "PENDING"
                }
            }
        ]
    }
}
```

For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html) in the *AWS CodeBuild User Guide*.

## Output

buildBatch -> (structure)

Contains information about a batch build.

id -> (string)

The identifier of the batch build.

arn -> (string)

The ARN of the batch build.

startTime -> (timestamp)

The date and time that the batch build started.

endTime -> (timestamp)

The date and time that the batch build ended.

currentPhase -> (string)

The current phase of the batch build.

buildBatchStatus -> (string)

The status of the batch build.

sourceVersion -> (string)

The identifier of the version of the source code to be built.

resolvedSourceVersion -> (string)

The identifier of the resolved version of this batch buildâs source code.

- For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.
- For CodePipeline, the source revision provided by CodePipeline.
- For Amazon S3, this does not apply.

projectName -> (string)

The name of the batch build project.

phases -> (list)

An array of `BuildBatchPhase` objects the specify the phases of the batch build.

(structure)

Contains information about a stage for a batch build.

phaseType -> (string)

The name of the batch build phase. Valid values include:

COMBINE_ARTIFACTS

Build output artifacts are being combined and uploaded to the output location.

DOWNLOAD_BATCHSPEC

The batch build specification is being downloaded.

FAILED

One or more of the builds failed.

IN_PROGRESS

The batch build is in progress.

STOPPED

The batch build was stopped.

SUBMITTED

The btach build has been submitted.

SUCCEEDED

The batch build succeeded.

phaseStatus -> (string)

The current status of the batch build phase. Valid values include:

FAILED

The build phase failed.

FAULT

The build phase faulted.

IN_PROGRESS

The build phase is still in progress.

STOPPED

The build phase stopped.

SUCCEEDED

The build phase succeeded.

TIMED_OUT

The build phase timed out.

startTime -> (timestamp)

When the batch build phase started, expressed in Unix time format.

endTime -> (timestamp)

When the batch build phase ended, expressed in Unix time format.

durationInSeconds -> (long)

How long, in seconds, between the starting and ending times of the batch buildâs phase.

contexts -> (list)

Additional information about the batch build phase. Especially to help troubleshoot a failed batch build.

(structure)

Additional information about a build phase that has an error. You can use this information for troubleshooting.

statusCode -> (string)

The status code for the context of the build phase.

message -> (string)

An explanation of the build phaseâs context. This might include a command ID and an exit code.

source -> (structure)

Information about the build input source code for the build project.

type -> (string)

The type of repository that contains the source code to be built. Valid values include:

- `BITBUCKET` : The source code is in a Bitbucket repository.
- `CODECOMMIT` : The source code is in an CodeCommit repository.
- `CODEPIPELINE` : The source code settings are specified in the source action of a pipeline in CodePipeline.
- `GITHUB` : The source code is in a GitHub repository.
- `GITHUB_ENTERPRISE` : The source code is in a GitHub Enterprise Server repository.
- `GITLAB` : The source code is in a GitLab repository.
- `GITLAB_SELF_MANAGED` : The source code is in a self-managed GitLab repository.
- `NO_SOURCE` : The project does not have input source code.
- `S3` : The source code is in an Amazon S3 bucket.

location -> (string)

Information about the location of the source code to be built. Valid values include:

- For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipelineâs source action instead of this value.
- For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>` ).
- For source code in an Amazon S3 input bucket, one of the following.
- The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip` ).
- The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/` ).
- For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access** , choose **Request access** next to each repository you want to allow CodeBuild to have access to, and then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .
- For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize** . Then on the CodeConnections **Create GitLab connection** page, choose **Connect to GitLab** . (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the `auth` objectâs `type` value to `CODECONNECTIONS` in the `source` object.
- For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .

If you specify `CODEPIPELINE` for the `Type` property, donât specify this property. For all of the other types, you must specify `Location` .

gitCloneDepth -> (integer)

Information about the Git clone depth for the build project.

gitSubmodulesConfig -> (structure)

Information about the Git submodules configuration for the build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

buildspec -> (string)

The buildspec file declaration to use for the builds in this build project.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

auth -> (structure)

Information about the authorization settings for CodeBuild to access the source code to be built.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

reportBuildStatus -> (boolean)

Set to true to report the status of a buildâs start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

The status of a build triggered by a webhook is always reported to your source provider.

If your projectâs builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.

buildStatusConfig -> (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

insecureSsl -> (boolean)

Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier -> (string)

An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

secondarySources -> (list)

An array of `ProjectSource` objects that define the sources for the batch build.

(structure)

Information about the build input source code for the build project.

type -> (string)

The type of repository that contains the source code to be built. Valid values include:

- `BITBUCKET` : The source code is in a Bitbucket repository.
- `CODECOMMIT` : The source code is in an CodeCommit repository.
- `CODEPIPELINE` : The source code settings are specified in the source action of a pipeline in CodePipeline.
- `GITHUB` : The source code is in a GitHub repository.
- `GITHUB_ENTERPRISE` : The source code is in a GitHub Enterprise Server repository.
- `GITLAB` : The source code is in a GitLab repository.
- `GITLAB_SELF_MANAGED` : The source code is in a self-managed GitLab repository.
- `NO_SOURCE` : The project does not have input source code.
- `S3` : The source code is in an Amazon S3 bucket.

location -> (string)

Information about the location of the source code to be built. Valid values include:

- For source code settings that are specified in the source action of a pipeline in CodePipeline, `location` should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipelineâs source action instead of this value.
- For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, `https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name>` ).
- For source code in an Amazon S3 input bucket, one of the following.
- The path to the ZIP file that contains the source code (for example, `<bucket-name>/<path>/<object-name>.zip` ).
- The path to the folder that contains the source code (for example, `<bucket-name>/<path-to-source-code>/<folder>/` ).
- For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub **Authorize application** page, for **Organization access** , choose **Request access** next to each repository you want to allow CodeBuild to have access to, and then choose **Authorize application** . (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .
- For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections **Authorize application** page, choose **Authorize** . Then on the CodeConnections **Create GitLab connection** page, choose **Connect to GitLab** . (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the `auth` objectâs `type` value to `CODECONNECTIONS` in the `source` object.
- For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket **Confirm access to your account** page, choose **Grant access** . (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the `source` object, set the `auth` objectâs `type` value to `OAUTH` .

If you specify `CODEPIPELINE` for the `Type` property, donât specify this property. For all of the other types, you must specify `Location` .

gitCloneDepth -> (integer)

Information about the Git clone depth for the build project.

gitSubmodulesConfig -> (structure)

Information about the Git submodules configuration for the build project.

fetchSubmodules -> (boolean)

Set to true to fetch Git submodules for your CodeBuild build project.

buildspec -> (string)

The buildspec file declaration to use for the builds in this build project.

If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in `CODEBUILD_SRC_DIR` environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, `arn:aws:s3:::my-codebuild-sample2/buildspec.yml` ). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see [Buildspec File Name and Storage Location](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage) .

auth -> (structure)

Information about the authorization settings for CodeBuild to access the source code to be built.

type -> (string)

The authorization type to use. Valid options are OAUTH, CODECONNECTIONS, or SECRETS_MANAGER.

resource -> (string)

The resource value that applies to the specified authorization type.

reportBuildStatus -> (boolean)

Set to true to report the status of a buildâs start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an `invalidInputException` is thrown.

To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see [Source provider access](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) in the *CodeBuild User Guide* .

The status of a build triggered by a webhook is always reported to your source provider.

If your projectâs builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.

buildStatusConfig -> (structure)

Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is `GITHUB` , `GITHUB_ENTERPRISE` , or `BITBUCKET` .

context -> (string)

Specifies the context of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `name` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `context` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

targetUrl -> (string)

Specifies the target url of the build status CodeBuild sends to the source provider. The usage of this parameter depends on the source provider.

Bitbucket

This parameter is used for the `url` parameter in the Bitbucket commit status. For more information, see [build](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bnode%7D/statuses/build) in the Bitbucket API documentation.

GitHub/GitHub Enterprise Server

This parameter is used for the `target_url` parameter in the GitHub commit status. For more information, see [Create a commit status](https://developer.github.com/v3/repos/statuses/#create-a-commit-status) in the GitHub developer guide.

insecureSsl -> (boolean)

Enable this flag to ignore SSL warnings while connecting to the project source code.

sourceIdentifier -> (string)

An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

secondarySourceVersions -> (list)

An array of `ProjectSourceVersion` objects. Each `ProjectSourceVersion` must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

(structure)

A source identifier and its corresponding version.

sourceIdentifier -> (string)

An identifier for a source in the build project. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length.

sourceVersion -> (string)

The source version for the corresponding source identifier. If specified, must be one of:

- For CodeCommit: the commit ID, branch, or Git tag to use.
- For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format `pr/pull-request-ID` (for example, `pr/25` ). If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For GitLab: the commit ID, branch, or Git tag to use.
- For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branchâs HEAD commit ID is used. If not specified, the default branchâs HEAD commit ID is used.
- For Amazon S3: the version ID of the object that represents the build input ZIP file to use.

For more information, see [Source Version Sample with CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html) in the *CodeBuild User Guide* .

artifacts -> (structure)

A `BuildArtifacts` object the defines the build artifacts for this batch build.

location -> (string)

Information about the location of the build artifacts.

sha256sum -> (string)

The SHA-256 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

md5sum -> (string)

The MD5 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

secondaryArtifacts -> (list)

An array of `BuildArtifacts` objects the define the build artifacts for this batch build.

(structure)

Information about build output artifacts.

location -> (string)

Information about the location of the build artifacts.

sha256sum -> (string)

The SHA-256 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

md5sum -> (string)

The MD5 hash of the build artifact.

You can use this hash along with a checksum tool to confirm file integrity and authenticity.

### Note

This value is available only if the build projectâs `packaging` value is set to `ZIP` .

overrideArtifactName -> (boolean)

If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique.

encryptionDisabled -> (boolean)

Information that tells you if encryption for build artifacts is disabled.

artifactIdentifier -> (string)

An identifier for this artifact definition.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

cache -> (structure)

Information about the cache for the build project.

type -> (string)

The type of cache used by the build project. Valid values include:

- `NO_CACHE` : The build project does not use any cache.
- `S3` : The build project reads and writes from and to S3.
- `LOCAL` : The build project stores a cache locally on a build host that is only available to that build host.

location -> (string)

Information about the cache location:

- `NO_CACHE` or `LOCAL` : This value is ignored.
- `S3` : This is the S3 bucket name/prefix.

modes -> (list)

An array of strings that specify the local cache modes. You can use one or more local cache modes at the same time. This is only used for `LOCAL` cache types.

Possible values are:

LOCAL_SOURCE_CACHE

Caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored.

LOCAL_DOCKER_LAYER_CACHE

Caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network.

### Note

- You can use a Docker layer cache in the Linux environment only.
- The `privileged` flag must be set so that your project has the required Docker permissions.
- You should consider the security implications before you use a Docker layer cache.

LOCAL_CUSTOM_CACHE

Caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache:

- Only directories can be specified for caching. You cannot specify individual files.
- Symlinks are used to reference cached directories.
- Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file.

(string)

cacheNamespace -> (string)

Defines the scope of the cache. You can use this namespace to share a cache across multiple projects. For more information, see [Cache sharing between projects](https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html#caching-s3-sharing) in the *CodeBuild User Guide* .

environment -> (structure)

Information about the build environment of the build project.

type -> (string)

The type of build environment to use for related builds.

### Note

If youâre using compute fleets during project creation, `type` will be ignored.

For more information, see [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *CodeBuild user guide* .

image -> (string)

The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:

- For an image tag: `<registry>/<repository>:<tag>` . For example, in the Docker repository that CodeBuild uses to manage its Docker images, this would be `aws/codebuild/standard:4.0` .
- For an image digest: `<registry>/<repository>@<digest>` . For example, to specify an image with the digest âsha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf,â use `<registry>/<repository>@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf` .

For more information, see [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) in the *CodeBuild user guide* .

computeType -> (string)

Information about the compute resources the build project uses. Available values include:

- `ATTRIBUTE_BASED_COMPUTE` : Specify the amount of vCPUs, memory, disk space, and the type of machine.

### Note

If you use `ATTRIBUTE_BASED_COMPUTE` , you must define your attributes by using `computeConfiguration` . CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see [Reserved capacity environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types) in the *CodeBuild User Guide* .

- `BUILD_GENERAL1_SMALL` : Use up to 4 GiB memory and 2 vCPUs for builds.
- `BUILD_GENERAL1_MEDIUM` : Use up to 8 GiB memory and 4 vCPUs for builds.
- `BUILD_GENERAL1_LARGE` : Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.
- `BUILD_GENERAL1_XLARGE` : Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.
- `BUILD_GENERAL1_2XLARGE` : Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.
- `BUILD_LAMBDA_1GB` : Use up to 1 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_2GB` : Use up to 2 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_4GB` : Use up to 4 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_8GB` : Use up to 8 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .
- `BUILD_LAMBDA_10GB` : Use up to 10 GiB memory for builds. Only available for environment type `LINUX_LAMBDA_CONTAINER` and `ARM_LAMBDA_CONTAINER` .

If you use `BUILD_GENERAL1_SMALL` :

- For environment type `LINUX_CONTAINER` , you can use up to 4 GiB memory and 2 vCPUs for builds.
- For environment type `LINUX_GPU_CONTAINER` , you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.
- For environment type `ARM_CONTAINER` , you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.

If you use `BUILD_GENERAL1_LARGE` :

- For environment type `LINUX_CONTAINER` , you can use up to 16 GiB memory and 8 vCPUs for builds.
- For environment type `LINUX_GPU_CONTAINER` , you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.
- For environment type `ARM_CONTAINER` , you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.

For more information, see [On-demand environment types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types) in the *CodeBuild User Guide.*

computeConfiguration -> (structure)

The compute configuration of the build project. This is only required if `computeType` is set to `ATTRIBUTE_BASED_COMPUTE` .

vCpu -> (long)

The number of vCPUs of the instance type included in your fleet.

memory -> (long)

The amount of memory of the instance type included in your fleet.

disk -> (long)

The amount of disk space of the instance type included in your fleet.

machineType -> (string)

The machine type of the instance type included in your fleet.

instanceType -> (string)

The EC2 instance type to be launched in your fleet.

fleet -> (structure)

A ProjectFleet object to use for this build project.

fleetArn -> (string)

Specifies the compute fleet ARN for the build project.

environmentVariables -> (list)

A set of environment variables to make available to builds for this build project.

(structure)

Information about an environment variable for a build project or a build.

name -> (string)

The name or key of the environment variable.

value -> (string)

The value of the environment variable.

### Warning

We strongly discourage the use of `PLAINTEXT` environment variables to store sensitive values, especially Amazon Web Services secret key IDs. `PLAINTEXT` environment variables can be displayed in plain text using the CodeBuild console and the CLI. For sensitive values, we recommend you use an environment variable of type `PARAMETER_STORE` or `SECRETS_MANAGER` .

type -> (string)

The type of environment variable. Valid values include:

- `PARAMETER_STORE` : An environment variable stored in Systems Manager Parameter Store. For environment variables of this type, specify the name of the parameter as the `value` of the EnvironmentVariable. The parameter value will be substituted for the name at runtime. You can also define Parameter Store environment variables in the buildspec. To learn how to do so, see [env/parameter-store](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store) in the *CodeBuild User Guide* .
- `PLAINTEXT` : An environment variable in plain text format. This is the default value.
- `SECRETS_MANAGER` : An environment variable stored in Secrets Manager. For environment variables of this type, specify the name of the secret as the `value` of the EnvironmentVariable. The secret value will be substituted for the name at runtime. You can also define Secrets Manager environment variables in the buildspec. To learn how to do so, see [env/secrets-manager](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.secrets-manager) in the *CodeBuild User Guide* .

privilegedMode -> (boolean)

Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is `false` .

You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:

If the operating systemâs base image is Ubuntu Linux:

`- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&`

`- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"`

If the operating systemâs base image is Alpine Linux and the previous command does not work, add the `-t` argument to `timeout` :

`- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&`

`- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"`

certificate -> (string)

The ARN of the Amazon S3 bucket, path prefix, and object key that contains the PEM-encoded certificate for the build project. For more information, see [certificate](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-cli.html#cli.environment.certificate) in the *CodeBuild User Guide* .

registryCredential -> (structure)

The credentials for access to a private registry.

credential -> (string)

The Amazon Resource Name (ARN) or name of credentials created using Secrets Manager.

### Note

The `credential` can use the name of the credentials only if they exist in your current Amazon Web Services Region.

credentialProvider -> (string)

The service that created the credentials to access a private Docker registry. The valid value, SECRETS_MANAGER, is for Secrets Manager.

imagePullCredentialsType -> (string)

The type of credentials CodeBuild uses to pull images in your build. There are two valid values:

- `CODEBUILD` specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild service principal.
- `SERVICE_ROLE` specifies that CodeBuild uses your build projectâs service role.

When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an CodeBuild curated image, you must use CODEBUILD credentials.

dockerServer -> (structure)

A DockerServer object to use for this build project.

computeType -> (string)

Information about the compute resources the docker server uses. Available values include:

- `BUILD_GENERAL1_SMALL` : Use up to 4 GiB memory and 2 vCPUs for your docker server.
- `BUILD_GENERAL1_MEDIUM` : Use up to 8 GiB memory and 4 vCPUs for your docker server.
- `BUILD_GENERAL1_LARGE` : Use up to 16 GiB memory and 8 vCPUs for your docker server.
- `BUILD_GENERAL1_XLARGE` : Use up to 64 GiB memory and 32 vCPUs for your docker server.
- `BUILD_GENERAL1_2XLARGE` : Use up to 128 GiB memory and 64 vCPUs for your docker server.

securityGroupIds -> (list)

A list of one or more security groups IDs.

### Note

Security groups configured for Docker servers should allow ingress network traffic from the VPC configured in the project. They should allow ingress on port 9876.

(string)

status -> (structure)

A DockerServerStatus object to use for this docker server.

status -> (string)

The status of the docker server.

message -> (string)

A message associated with the status of a docker server.

serviceRole -> (string)

The name of a service role used for builds in the batch.

logConfig -> (structure)

Information about logs for a build project. These can be logs in CloudWatch Logs, built in a specified S3 bucket, or both.

cloudWatchLogs -> (structure)

Information about CloudWatch Logs for a build project. CloudWatch Logs are enabled by default.

status -> (string)

The current status of the logs in CloudWatch Logs for a build project. Valid values are:

- `ENABLED` : CloudWatch Logs are enabled for this build project.
- `DISABLED` : CloudWatch Logs are not enabled for this build project.

groupName -> (string)

The group name of the logs in CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

streamName -> (string)

The prefix of the stream name of the CloudWatch Logs. For more information, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) .

s3Logs -> (structure)

Information about logs built to an S3 bucket for a build project. S3 logs are not enabled by default.

status -> (string)

The current status of the S3 build logs. Valid values are:

- `ENABLED` : S3 build logs are enabled for this build project.
- `DISABLED` : S3 build logs are not enabled for this build project.

location -> (string)

The ARN of an S3 bucket and the path prefix for S3 logs. If your Amazon S3 bucket name is `my-bucket` , and your path prefix is `build-log` , then acceptable formats are `my-bucket/build-log` or `arn:aws:s3:::my-bucket/build-log` .

encryptionDisabled -> (boolean)

Set to true if you do not want your S3 build log output encrypted. By default S3 build logs are encrypted.

bucketOwnerAccess -> (string)

Specifies the bucket ownerâs access for objects that another account uploads to their Amazon S3 bucket. By default, only the account that uploads the objects to the bucket has access to these objects. This property allows you to give the bucket owner access to these objects.

### Note

To use this property, your CodeBuild service role must have the `s3:PutBucketAcl` permission. This permission allows CodeBuild to modify the access control list for the bucket.

This property can be one of the following values:

NONE

The bucket owner does not have access to the objects. This is the default.

READ_ONLY

The bucket owner has read-only access to the objects. The uploading account retains ownership of the objects.

FULL

The bucket owner has full access to the objects. Object ownership is determined by the following criteria:

- If the bucket is configured with the **Bucket owner preferred** setting, the bucket owner owns the objects. The uploading account will have object access as specified by the bucketâs policy.
- Otherwise, the uploading account retains ownership of the objects.

For more information about Amazon S3 object ownership, see [Controlling ownership of uploaded objects using S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon Simple Storage Service User Guide* .

buildTimeoutInMinutes -> (integer)

Specifies the maximum amount of time, in minutes, that the build in a batch must be completed in.

queuedTimeoutInMinutes -> (integer)

Specifies the amount of time, in minutes, that the batch build is allowed to be queued before it times out.

complete -> (boolean)

Indicates if the batch build is complete.

initiator -> (string)

The entity that started the batch build. Valid values include:

- If CodePipeline started the build, the pipelineâs name (for example, `codepipeline/my-demo-pipeline` ).
- If a user started the build, the userâs name.
- If the Jenkins plugin for CodeBuild started the build, the string `CodeBuild-Jenkins-Plugin` .

vpcConfig -> (structure)

Information about the VPC configuration that CodeBuild accesses.

vpcId -> (string)

The ID of the Amazon VPC.

subnets -> (list)

A list of one or more subnet IDs in your Amazon VPC.

(string)

securityGroupIds -> (list)

A list of one or more security groups IDs in your Amazon VPC.

(string)

encryptionKey -> (string)

The Key Management Service customer master key (CMK) to be used for encrypting the batch build output artifacts.

### Note

You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key.

You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMKâs alias (using the format `alias/<alias-name>` ).

buildBatchNumber -> (long)

The number of the batch build. For each project, the `buildBatchNumber` of its first batch build is `1` . The `buildBatchNumber` of each subsequent batch build is incremented by `1` . If a batch build is deleted, the `buildBatchNumber` of other batch builds does not change.

fileSystemLocations -> (list)

An array of `ProjectFileSystemLocation` objects for the batch build project. A `ProjectFileSystemLocation` object specifies the `identifier` , `location` , `mountOptions` , `mountPoint` , and `type` of a file system created using Amazon Elastic File System.

(structure)

Information about a file system created by Amazon Elastic File System (EFS). For more information, see [What Is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

type -> (string)

The type of the file system. The one supported type is `EFS` .

location -> (string)

A string that specifies the location of the file system created by Amazon EFS. Its format is `efs-dns-name:/directory-path` . You can find the DNS name of file system when you view it in the Amazon EFS console. The directory path is a path to a directory in the file system that CodeBuild mounts. For example, if the DNS name of a file system is `fs-abcd1234.efs.us-west-2.amazonaws.com` , and its mount directory is `my-efs-mount-directory` , then the `location` is `fs-abcd1234.efs.us-west-2.amazonaws.com:/my-efs-mount-directory` .

The directory path in the format `efs-dns-name:/directory-path` is optional. If you do not specify a directory path, the location is only the DNS name and CodeBuild mounts the entire file system.

mountPoint -> (string)

The location in the container where you mount the file system.

identifier -> (string)

The name used to access a file system created by Amazon EFS. CodeBuild creates an environment variable by appending the `identifier` in all capital letters to `CODEBUILD_` . For example, if you specify `my_efs` for `identifier` , a new environment variable is create named `CODEBUILD_MY_EFS` .

The `identifier` is used to mount your file system.

mountOptions -> (string)

The mount options for a file system created by Amazon EFS. The default mount options used by CodeBuild are `nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2` . For more information, see [Recommended NFS Mount Options](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-nfs-mount-settings.html) .

buildBatchConfig -> (structure)

Contains configuration information about a batch build project.

serviceRole -> (string)

Specifies the service role ARN for the batch build project.

combineArtifacts -> (boolean)

Specifies if the build artifacts for the batch build should be combined into a single artifact location.

restrictions -> (structure)

A `BatchRestrictions` object that specifies the restrictions for the batch build.

maximumBuildsAllowed -> (integer)

Specifies the maximum number of builds allowed.

computeTypesAllowed -> (list)

An array of strings that specify the compute types that are allowed for the batch build. See [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the *CodeBuild User Guide* for these values.

(string)

fleetsAllowed -> (list)

An array of strings that specify the fleets that are allowed for the batch build. See [Run builds on reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html) in the *CodeBuild User Guide* for more information.

(string)

timeoutInMins -> (integer)

Specifies the maximum amount of time, in minutes, that the batch build must be completed in.

batchReportMode -> (string)

Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.

REPORT_AGGREGATED_BATCH

(Default) Aggregate all of the build statuses into a single status report.

REPORT_INDIVIDUAL_BUILDS

Send a separate status report for each individual build.

buildGroups -> (list)

An array of `BuildGroup` objects that define the build groups for the batch build.

(structure)

Contains information about a batch build build group. Build groups are used to combine builds that can run in parallel, while still being able to set dependencies on other build groups.

identifier -> (string)

Contains the identifier of the build group.

dependsOn -> (list)

An array of strings that contain the identifiers of the build groups that this build group depends on.

(string)

ignoreFailure -> (boolean)

Specifies if failures in this build group can be ignored.

currentBuildSummary -> (structure)

A `BuildSummary` object that contains a summary of the current build group.

arn -> (string)

The batch build ARN.

requestedOn -> (timestamp)

When the build was started, expressed in Unix time format.

buildStatus -> (string)

The status of the build group.

FAILED

The build group failed.

FAULT

The build group faulted.

IN_PROGRESS

The build group is still in progress.

STOPPED

The build group stopped.

SUCCEEDED

The build group succeeded.

TIMED_OUT

The build group timed out.

primaryArtifact -> (structure)

A `ResolvedArtifact` object that represents the primary build artifacts for the build group.

type -> (string)

Specifies the type of artifact.

location -> (string)

The location of the artifact.

identifier -> (string)

The identifier of the artifact.

secondaryArtifacts -> (list)

An array of `ResolvedArtifact` objects that represents the secondary build artifacts for the build group.

(structure)

Represents a resolved build artifact. A resolved artifact is an artifact that is built and deployed to the destination, such as Amazon S3.

type -> (string)

Specifies the type of artifact.

location -> (string)

The location of the artifact.

identifier -> (string)

The identifier of the artifact.

priorBuildSummaryList -> (list)

An array of `BuildSummary` objects that contain summaries of previous build groups.

(structure)

Contains summary information about a batch build group.

arn -> (string)

The batch build ARN.

requestedOn -> (timestamp)

When the build was started, expressed in Unix time format.

buildStatus -> (string)

The status of the build group.

FAILED

The build group failed.

FAULT

The build group faulted.

IN_PROGRESS

The build group is still in progress.

STOPPED

The build group stopped.

SUCCEEDED

The build group succeeded.

TIMED_OUT

The build group timed out.

primaryArtifact -> (structure)

A `ResolvedArtifact` object that represents the primary build artifacts for the build group.

type -> (string)

Specifies the type of artifact.

location -> (string)

The location of the artifact.

identifier -> (string)

The identifier of the artifact.

secondaryArtifacts -> (list)

An array of `ResolvedArtifact` objects that represents the secondary build artifacts for the build group.

(structure)

Represents a resolved build artifact. A resolved artifact is an artifact that is built and deployed to the destination, such as Amazon S3.

type -> (string)

Specifies the type of artifact.

location -> (string)

The location of the artifact.

identifier -> (string)

The identifier of the artifact.

debugSessionEnabled -> (boolean)

Specifies if session debugging is enabled for this batch build. For more information, see [Viewing a running build in Session Manager](https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html) . Batch session debugging is not supported for matrix batch builds.

reportArns -> (list)

An array that contains the ARNs of reports created by merging reports from builds associated with this batch build.

(string)