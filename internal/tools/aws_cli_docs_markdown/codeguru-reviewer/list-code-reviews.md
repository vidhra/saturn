# list-code-reviewsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-code-reviews.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-code-reviews.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguru-reviewer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html#cli-aws-codeguru-reviewer) ]

# list-code-reviews

## Description

Lists all the code reviews that the customer has created in the past 90 days.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguru-reviewer-2019-09-19/ListCodeReviews)

## Synopsis

```
list-code-reviews
[--provider-types <value>]
[--states <value>]
[--repository-names <value>]
--type <value>
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

`--provider-types` (list)

List of provider types for filtering that needs to be applied before displaying the result. For example, `providerTypes=[GitHub]` lists code reviews from GitHub.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  CodeCommit
  GitHub
  Bitbucket
  GitHubEnterpriseServer
  S3Bucket
```

`--states` (list)

List of states for filtering that needs to be applied before displaying the result. For example, `states=[Pending]` lists code reviews in the Pending state.

The valid code review states are:

- `Completed` : The code review is complete.
- `Pending` : The code review started and has not completed or failed.
- `Failed` : The code review failed.
- `Deleting` : The code review is being deleted.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Completed
  Pending
  Failed
  Deleting
```

`--repository-names` (list)

List of repository names for filtering that needs to be applied before displaying the result.

(string)

Syntax:

```
"string" "string" ...
```

`--type` (string)

The type of code reviews to list in the response.

Possible values:

- `PullRequest`
- `RepositoryAnalysis`

`--max-results` (integer)

The maximum number of results that are returned per call. The default is 100.

`--next-token` (string)

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.

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

**To list code reviews created in your AWS account in the last 90 days.**

The following `list-code-reviews` example lists the code reviews created in the last 90 days using pull requests.

```
aws codeguru-reviewer list-code-reviews \
    --type PullRequest
```

Output:

```
{
    "CodeReviewSummaries": [
        {
            "LastUpdatedTimeStamp": 1588897288.054,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "ProviderType": "GitHub",
            "PullRequestId": "5",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 24,
                "FindingsCount": 1
            },
            "CreatedTimeStamp": 1588897068.512,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        },
        {
            "LastUpdatedTimeStamp": 1588869793.263,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "ProviderType": "GitHub",
            "PullRequestId": "4",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 29,
                "FindingsCount": 0
            },
            "CreatedTimeStamp": 1588869575.949,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        },
        {
            "LastUpdatedTimeStamp": 1588870511.211,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "ProviderType": "GitHub",
            "PullRequestId": "4",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 2,
                "FindingsCount": 0
            },
            "CreatedTimeStamp": 1588870292.425,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        },
        {
            "LastUpdatedTimeStamp": 1588118522.452,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
            "ProviderType": "GitHub",
            "PullRequestId": "3",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 29,
                "FindingsCount": 0
            },
            "CreatedTimeStamp": 1588118301.131,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        },
        {
            "LastUpdatedTimeStamp": 1588112205.207,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
            "ProviderType": "GitHub",
            "PullRequestId": "2",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 25,
                "FindingsCount": 0
            },
            "CreatedTimeStamp": 1588111987.443,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        },
        {
            "LastUpdatedTimeStamp": 1588104489.981,
            "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
            "ProviderType": "GitHub",
            "PullRequestId": "1",
            "MetricsSummary": {
                "MeteredLinesOfCodeCount": 25,
                "FindingsCount": 0
            },
            "CreatedTimeStamp": 1588104270.223,
            "State": "Completed",
            "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
            "Owner": "sample-owner",
            "RepositoryName": "sample-repository-name",
            "Type": "PullRequest"
        }
    ]
}
```

For more information, see [View all code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/view-all-code-reviews.html) in the *Amazon CodeGuru Reviewer User Guide*.

## Output

CodeReviewSummaries -> (list)

A list of code reviews that meet the criteria of the request.

(structure)

Information about the summary of the code review.

Name -> (string)

The name of the code review.

CodeReviewArn -> (string)

The Amazon Resource Name (ARN) of the [CodeReview](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html) object.

RepositoryName -> (string)

The name of the repository.

Owner -> (string)

The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.

ProviderType -> (string)

The provider type of the repository association.

State -> (string)

The state of the code review.

The valid code review states are:

- `Completed` : The code review is complete.
- `Pending` : The code review started and has not completed or failed.
- `Failed` : The code review failed.
- `Deleting` : The code review is being deleted.

CreatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the code review was created.

LastUpdatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the code review was last updated.

Type -> (string)

The type of the code review.

PullRequestId -> (string)

The pull request ID for the code review.

MetricsSummary -> (structure)

The statistics from the code review.

MeteredLinesOfCodeCount -> (long)

Lines of code metered in the code review. For the initial code review pull request and all subsequent revisions, this includes all lines of code in the files added to the pull request. In subsequent revisions, for files that already existed in the pull request, this includes only the changed lines of code. In both cases, this does not include non-code lines such as comments and import statements. For example, if you submit a pull request containing 5 files, each with 500 lines of code, and in a subsequent revision you added a new file with 200 lines of code, and also modified a total of 25 lines across the initial 5 files, `MeteredLinesOfCodeCount` includes the first 5 files (5 * 500 = 2,500 lines), the new file (200 lines) and the 25 changed lines of code for a total of 2,725 lines of code.

SuppressedLinesOfCodeCount -> (long)

Lines of code suppressed in the code review based on the `excludeFiles` element in the `aws-codeguru-reviewer.yml` file. For full repository analyses, this number includes all lines of code in the files that are suppressed. For pull requests, this number only includes the *changed* lines of code that are suppressed. In both cases, this number does not include non-code lines such as comments and import statements. For example, if you initiate a full repository analysis on a repository containing 5 files, each file with 100 lines of code, and 2 files are listed as excluded in the `aws-codeguru-reviewer.yml` file, then `SuppressedLinesOfCodeCount` returns 200 (2 * 100) as the total number of lines of code suppressed. However, if you submit a pull request for the same repository, then `SuppressedLinesOfCodeCount` only includes the lines in the 2 files that changed. If only 1 of the 2 files changed in the pull request, then `SuppressedLinesOfCodeCount` returns 100 (1 * 100) as the total number of lines of code suppressed.

FindingsCount -> (long)

Total number of recommendations found in the code review.

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

NextToken -> (string)

Pagination token.