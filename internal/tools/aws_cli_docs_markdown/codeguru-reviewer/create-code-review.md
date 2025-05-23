# create-code-reviewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/create-code-review.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/create-code-review.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguru-reviewer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html#cli-aws-codeguru-reviewer) ]

# create-code-review

## Description

Use to create a code review with a [CodeReviewType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html) of `RepositoryAnalysis` . This type of code review analyzes all code under a specified branch in an associated repository. `PullRequest` code reviews are automatically triggered by a pull request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguru-reviewer-2019-09-19/CreateCodeReview)

## Synopsis

```
create-code-review
--name <value>
--repository-association-arn <value>
--type <value>
[--client-request-token <value>]
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

The name of the code review. The name of each code review in your Amazon Web Services account must be unique.

`--repository-association-arn` (string)

The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object. You can retrieve this ARN by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html) .

A code review can only be created on an associated repository. This is the ARN of the associated repository.

`--type` (structure)

The type of code review to create. This is specified using a [CodeReviewType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReviewType.html) object. You can create a code review only of type `RepositoryAnalysis` .

RepositoryAnalysis -> (structure)

A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in [CreateCodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview) .

RepositoryHead -> (structure)

A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the tip of a branch in an associated repository.

BranchName -> (string)

The name of the branch in an associated repository. The `RepositoryHeadSourceCodeType` specifies the tip of this branch.

SourceCodeType -> (structure)

Specifies the source code that is analyzed in a code review.

CommitDiff -> (structure)

A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a commit diff created by a pull request on an associated repository.

SourceCommit -> (string)

The SHA of the source commit used to generate a commit diff. This field is required for a pull request code review.

DestinationCommit -> (string)

The SHA of the destination commit used to generate a commit diff. This field is required for a pull request code review.

MergeBaseCommit -> (string)

The SHA of the merge base of a commit.

RepositoryHead -> (structure)

A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the tip of a branch in an associated repository.

BranchName -> (string)

The name of the branch in an associated repository. The `RepositoryHeadSourceCodeType` specifies the tip of this branch.

BranchDiff -> (structure)

A type of [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a source branch name and a destination branch name in an associated repository.

SourceBranchName -> (string)

The source branch for a diff in an associated repository.

DestinationBranchName -> (string)

The destination branch for a diff in an associated repository.

S3BucketRepository -> (structure)

Information about an associated repository in an S3 bucket that includes its name and an `S3RepositoryDetails` object. The `S3RepositoryDetails` object includes the name of an S3 bucket, an S3 key for a source code .zip file, and an S3 key for a build artifacts .zip file. `S3BucketRepository` is required in [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) for `S3BucketRepository` based code reviews.

Name -> (string)

The name of the repository when the `ProviderType` is `S3Bucket` .

Details -> (structure)

An `S3RepositoryDetails` object that specifies the name of an S3 bucket and a `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object keys for a source code .zip file and for a build artifacts .zip file.

BucketName -> (string)

The name of the S3 bucket used for associating a new S3 repository. It must begin with `codeguru-reviewer-` .

CodeArtifacts -> (structure)

A `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object key for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.

SourceCodeArtifactsObjectKey -> (string)

The S3 object key for a source code .zip file. This is required for all code reviews.

BuildArtifactsObjectKey -> (string)

The S3 object key for a build artifacts .zip file that contains .jar or .class files. This is required for a code review with security analysis. For more information, see [Create code reviews with GitHub Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html) in the *Amazon CodeGuru Reviewer User Guide* .

RequestMetadata -> (structure)

Metadata that is associated with a code review. This applies to any type of code review supported by CodeGuru Reviewer. The `RequestMetadaa` field captures any event metadata. For example, it might capture metadata associated with an event trigger, such as a push or a pull request.

RequestId -> (string)

The ID of the request. This is required for a pull request code review.

Requester -> (string)

An identifier, such as a name or account ID, that is associated with the requester. The `Requester` is used to capture the `author/actor` name of the event request.

EventInfo -> (structure)

Information about the event associated with a code review.

Name -> (string)

The name of the event. The possible names are `pull_request` , `workflow_dispatch` , `schedule` , and `push`

State -> (string)

The state of an event. The state might be open, closed, or another state.

VendorName -> (string)

The name of the repository vendor used to upload code to an S3 bucket for a CI/CD code review. For example, if code and artifacts are uploaded to an S3 bucket for a CI/CD code review by GitHub scripts from a GitHub repository, then the repository associationâs `ProviderType` is `S3Bucket` and the CI/CD repository vendor name is GitHub. For more information, see the definition for `ProviderType` in [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) .

AnalysisTypes -> (list)

They types of analysis performed during a repository analysis or a pull request review. You can specify either `Security` , `CodeQuality` , or both.

(string)

JSON Syntax:

```
{
  "RepositoryAnalysis": {
    "RepositoryHead": {
      "BranchName": "string"
    },
    "SourceCodeType": {
      "CommitDiff": {
        "SourceCommit": "string",
        "DestinationCommit": "string",
        "MergeBaseCommit": "string"
      },
      "RepositoryHead": {
        "BranchName": "string"
      },
      "BranchDiff": {
        "SourceBranchName": "string",
        "DestinationBranchName": "string"
      },
      "S3BucketRepository": {
        "Name": "string",
        "Details": {
          "BucketName": "string",
          "CodeArtifacts": {
            "SourceCodeArtifactsObjectKey": "string",
            "BuildArtifactsObjectKey": "string"
          }
        }
      },
      "RequestMetadata": {
        "RequestId": "string",
        "Requester": "string",
        "EventInfo": {
          "Name": "string",
          "State": "string"
        },
        "VendorName": "GitHub"|"GitLab"|"NativeS3"
      }
    }
  },
  "AnalysisTypes": ["Security"|"CodeQuality", ...]
}
```

`--client-request-token` (string)

Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate code reviews if there are failures and retries.

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

**To create a code review.**

The following `create-code-review` creates a review of code in the `mainline` branch of an AWS CodeCommit repository that is named `my-repository-name`.

```
aws codeguru-reviewer create-code-review \
    --name my-code-review \
    --repository-association-arn arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --type '{"RepositoryAnalysis": {"RepositoryHead": {"BranchName": "mainline"}}}'
```

Output:

```
{
    "CodeReview": {
        "Name": "my-code-review",
        "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222:code-review:RepositoryAnalysis-my-code-review",
        "RepositoryName": "my-repository-name",
        "Owner": "123456789012",
        "ProviderType": "CodeCommit",
        "State": "Pending",
        "StateReason": "CodeGuru Reviewer has received the request, and a code review is scheduled.",
        "CreatedTimeStamp": 1618873489.195,
        "LastUpdatedTimeStamp": 1618873489.195,
        "Type": "RepositoryAnalysis",
        "SourceCodeType": {
            "RepositoryHead": {
                "BranchName": "mainline"
            }
        },
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
}
```

For more information, see [Create code reviews in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-code-reviews.html) in the *Amazon CodeGuru Reviewer User Guide*.

## Output

CodeReview -> (structure)

Information about a code review. A code review belongs to the associated repository that contains the reviewed code.

Name -> (string)

The name of the code review.

CodeReviewArn -> (string)

The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.

RepositoryName -> (string)

The name of the repository.

Owner -> (string)

The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.

ProviderType -> (string)

The type of repository that contains the reviewed code (for example, GitHub or Bitbucket).

State -> (string)

The valid code review states are:

- `Completed` : The code review is complete.
- `Pending` : The code review started and has not completed or failed.
- `Failed` : The code review failed.
- `Deleting` : The code review is being deleted.

StateReason -> (string)

The reason for the state of the code review.

CreatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the code review was created.

LastUpdatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the code review was last updated.

Type -> (string)

The type of code review.

PullRequestId -> (string)

The pull request ID for the code review.

SourceCodeType -> (structure)

The type of the source code for the code review.

CommitDiff -> (structure)

A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a commit diff created by a pull request on an associated repository.

SourceCommit -> (string)

The SHA of the source commit used to generate a commit diff. This field is required for a pull request code review.

DestinationCommit -> (string)

The SHA of the destination commit used to generate a commit diff. This field is required for a pull request code review.

MergeBaseCommit -> (string)

The SHA of the merge base of a commit.

RepositoryHead -> (structure)

A [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies the tip of a branch in an associated repository.

BranchName -> (string)

The name of the branch in an associated repository. The `RepositoryHeadSourceCodeType` specifies the tip of this branch.

BranchDiff -> (structure)

A type of [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) that specifies a source branch name and a destination branch name in an associated repository.

SourceBranchName -> (string)

The source branch for a diff in an associated repository.

DestinationBranchName -> (string)

The destination branch for a diff in an associated repository.

S3BucketRepository -> (structure)

Information about an associated repository in an S3 bucket that includes its name and an `S3RepositoryDetails` object. The `S3RepositoryDetails` object includes the name of an S3 bucket, an S3 key for a source code .zip file, and an S3 key for a build artifacts .zip file. `S3BucketRepository` is required in [SourceCodeType](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType) for `S3BucketRepository` based code reviews.

Name -> (string)

The name of the repository when the `ProviderType` is `S3Bucket` .

Details -> (structure)

An `S3RepositoryDetails` object that specifies the name of an S3 bucket and a `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object keys for a source code .zip file and for a build artifacts .zip file.

BucketName -> (string)

The name of the S3 bucket used for associating a new S3 repository. It must begin with `codeguru-reviewer-` .

CodeArtifacts -> (structure)

A `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object key for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.

SourceCodeArtifactsObjectKey -> (string)

The S3 object key for a source code .zip file. This is required for all code reviews.

BuildArtifactsObjectKey -> (string)

The S3 object key for a build artifacts .zip file that contains .jar or .class files. This is required for a code review with security analysis. For more information, see [Create code reviews with GitHub Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html) in the *Amazon CodeGuru Reviewer User Guide* .

RequestMetadata -> (structure)

Metadata that is associated with a code review. This applies to any type of code review supported by CodeGuru Reviewer. The `RequestMetadaa` field captures any event metadata. For example, it might capture metadata associated with an event trigger, such as a push or a pull request.

RequestId -> (string)

The ID of the request. This is required for a pull request code review.

Requester -> (string)

An identifier, such as a name or account ID, that is associated with the requester. The `Requester` is used to capture the `author/actor` name of the event request.

EventInfo -> (structure)

Information about the event associated with a code review.

Name -> (string)

The name of the event. The possible names are `pull_request` , `workflow_dispatch` , `schedule` , and `push`

State -> (string)

The state of an event. The state might be open, closed, or another state.

VendorName -> (string)

The name of the repository vendor used to upload code to an S3 bucket for a CI/CD code review. For example, if code and artifacts are uploaded to an S3 bucket for a CI/CD code review by GitHub scripts from a GitHub repository, then the repository associationâs `ProviderType` is `S3Bucket` and the CI/CD repository vendor name is GitHub. For more information, see the definition for `ProviderType` in [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) .

AssociationArn -> (string)

The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) that contains the reviewed source code. You can retrieve associated repository ARNs by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html) .

Metrics -> (structure)

The statistics from the code review.

MeteredLinesOfCodeCount -> (long)

`MeteredLinesOfCodeCount` is the number of lines of code in the repository where the code review happened. This does not include non-code lines such as comments and blank lines.

SuppressedLinesOfCodeCount -> (long)

`SuppressedLinesOfCodeCount` is the number of lines of code in the repository where the code review happened that CodeGuru Reviewer did not analyze. The lines suppressed in the analysis is based on the `excludeFiles` variable in the `aws-codeguru-reviewer.yml` file. This number does not include non-code lines such as comments and blank lines.

FindingsCount -> (long)

Total number of recommendations found in the code review.

AnalysisTypes -> (list)

The types of analysis performed during a repository analysis or a pull request review. You can specify either `Security` , `CodeQuality` , or both.

(string)

ConfigFileState -> (string)

The state of the `aws-codeguru-reviewer.yml` configuration file that allows the configuration of the CodeGuru Reviewer analysis. The file either exists, doesnât exist, or exists with errors at the root directory of your repository.