# batch-describe-merge-conflictsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-describe-merge-conflicts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-describe-merge-conflicts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# batch-describe-merge-conflicts

## Description

Returns information about one or more merge conflicts in the attempted merge of two commit specifiers using the squash or three-way merge strategy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/BatchDescribeMergeConflicts)

## Synopsis

```
batch-describe-merge-conflicts
--repository-name <value>
--destination-commit-specifier <value>
--source-commit-specifier <value>
--merge-option <value>
[--max-merge-hunks <value>]
[--max-conflict-files <value>]
[--file-paths <value>]
[--conflict-detail-level <value>]
[--conflict-resolution-strategy <value>]
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

`--repository-name` (string)

The name of the repository that contains the merge conflicts you want to review.

`--destination-commit-specifier` (string)

The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).

`--source-commit-specifier` (string)

The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).

`--merge-option` (string)

The merge option or strategy you want to use to merge the code.

Possible values:

- `FAST_FORWARD_MERGE`
- `SQUASH_MERGE`
- `THREE_WAY_MERGE`

`--max-merge-hunks` (integer)

The maximum number of merge hunks to include in the output.

`--max-conflict-files` (integer)

The maximum number of files to include in the output.

`--file-paths` (list)

The path of the target files used to describe the conflicts. If not specified, the default is all conflict files.

(string)

Syntax:

```
"string" "string" ...
```

`--conflict-detail-level` (string)

The level of conflict detail to use. If unspecified, the default FILE_LEVEL is used, which returns a not-mergeable result if the same file has differences in both branches. If LINE_LEVEL is specified, a conflict is considered not mergeable if the same file in both branches has differences on the same line.

Possible values:

- `FILE_LEVEL`
- `LINE_LEVEL`

`--conflict-resolution-strategy` (string)

Specifies which branch to use when resolving conflicts, or whether to attempt automatically merging two versions of a file. The default is NONE, which requires any conflicts to be resolved manually before the merge operation is successful.

Possible values:

- `NONE`
- `ACCEPT_SOURCE`
- `ACCEPT_DESTINATION`
- `AUTOMERGE`

`--next-token` (string)

An enumeration token that, when provided in a request, returns the next batch of the results.

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

**To get information about merge conflicts in all files or a subset of files in a merge between two commit specifiers**

The following `batch-describe-merge-conflicts` example determines the merge conflicts for merging a source branch named `feature-randomizationfeature` with a destination branch named `main` using the `THREE_WAY_MERGE` strategy in a repository named `MyDemoRepo`.

```
aws codecommit batch-describe-merge-conflicts \
    --source-commit-specifier feature-randomizationfeature \
    --destination-commit-specifier main \
    --merge-option THREE_WAY_MERGE \
    --repository-name MyDemoRepo
```

Output:

```
{
    "conflicts": [
        {
            "conflictMetadata": {
                "filePath": "readme.md",
                "fileSizes": {
                    "source": 139,
                    "destination": 230,
                    "base": 85
                },
                "fileModes": {
                    "source": "NORMAL",
                    "destination": "NORMAL",
                    "base": "NORMAL"
                },
                "objectTypes": {
                    "source": "FILE",
                    "destination": "FILE",
                    "base": "FILE"
                },
                "numberOfConflicts": 1,
                "isBinaryFile": {
                    "source": false,
                    "destination": false,
                    "base": false
                },
                "contentConflict": true,
                "fileModeConflict": false,
                "objectTypeConflict": false,
                "mergeOperations": {
                    "source": "M",
                    "destination": "M"
                }
            },
            "mergeHunks": [
                {
                    "isConflict": true,
                    "source": {
                        "startLine": 0,
                        "endLine": 3,
                        "hunkContent": "VGhpcyBpEXAMPLE=="
                    },
                    "destination": {
                        "startLine": 0,
                        "endLine": 1,
                        "hunkContent": "VXNlIHRoEXAMPLE="
                    }
                }
            ]
        }
    ],
    "errors": [],
    "destinationCommitId": "86958e0aEXAMPLE",
    "sourceCommitId": "6ccd57fdEXAMPLE",
    "baseCommitId": "767b6958EXAMPLE"
}
```

For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#batch-describe-merge-conflicts) in the *AWS CodeCommit User Guide*.

## Output

conflicts -> (list)

A list of conflicts for each file, including the conflict metadata and the hunks of the differences between the files.

(structure)

Information about conflicts in a merge operation.

conflictMetadata -> (structure)

Metadata about a conflict in a merge operation.

filePath -> (string)

The path of the file that contains conflicts.

fileSizes -> (structure)

The file sizes of the file in the source, destination, and base of the merge.

source -> (long)

The size of a file in the source of a merge or pull request.

destination -> (long)

The size of a file in the destination of a merge or pull request.

base -> (long)

The size of a file in the base of a merge or pull request.

fileModes -> (structure)

The file modes of the file in the source, destination, and base of the merge.

source -> (string)

The file mode of a file in the source of a merge or pull request.

destination -> (string)

The file mode of a file in the destination of a merge or pull request.

base -> (string)

The file mode of a file in the base of a merge or pull request.

objectTypes -> (structure)

Information about any object type conflicts in a merge operation.

source -> (string)

The type of the object in the source branch.

destination -> (string)

The type of the object in the destination branch.

base -> (string)

The type of the object in the base commit of the merge.

numberOfConflicts -> (integer)

The number of conflicts, including both hunk conflicts and metadata conflicts.

isBinaryFile -> (structure)

A boolean value (true or false) indicating whether the file is binary or textual in the source, destination, and base of the merge.

source -> (boolean)

The binary or non-binary status of file in the source of a merge or pull request.

destination -> (boolean)

The binary or non-binary status of a file in the destination of a merge or pull request.

base -> (boolean)

The binary or non-binary status of a file in the base of a merge or pull request.

contentConflict -> (boolean)

A boolean value indicating whether there are conflicts in the content of a file.

fileModeConflict -> (boolean)

A boolean value indicating whether there are conflicts in the file mode of a file.

objectTypeConflict -> (boolean)

A boolean value (true or false) indicating whether there are conflicts between the branches in the object type of a file, folder, or submodule.

mergeOperations -> (structure)

Whether an add, modify, or delete operation caused the conflict between the source and destination of the merge.

source -> (string)

The operation (add, modify, or delete) on a file in the source of a merge or pull request.

destination -> (string)

The operation on a file in the destination of a merge or pull request.

mergeHunks -> (list)

A list of hunks that contain the differences between files or lines causing the conflict.

(structure)

Information about merge hunks in a merge or pull request operation.

isConflict -> (boolean)

A Boolean value indicating whether a combination of hunks contains a conflict. Conflicts occur when the same file or the same lines in a file were modified in both the source and destination of a merge or pull request. Valid values include true, false, and null. True when the hunk represents a conflict and one or more files contains a line conflict. File mode conflicts in a merge do not set this to true.

source -> (structure)

Information about the merge hunk in the source of a merge or pull request.

startLine -> (integer)

The start position of the hunk in the merge result.

endLine -> (integer)

The end position of the hunk in the merge result.

hunkContent -> (string)

The base-64 encoded content of the hunk merged region that might contain a conflict.

destination -> (structure)

Information about the merge hunk in the destination of a merge or pull request.

startLine -> (integer)

The start position of the hunk in the merge result.

endLine -> (integer)

The end position of the hunk in the merge result.

hunkContent -> (string)

The base-64 encoded content of the hunk merged region that might contain a conflict.

base -> (structure)

Information about the merge hunk in the base of a merge or pull request.

startLine -> (integer)

The start position of the hunk in the merge result.

endLine -> (integer)

The end position of the hunk in the merge result.

hunkContent -> (string)

The base-64 encoded content of the hunk merged region that might contain a conflict.

nextToken -> (string)

An enumeration token that can be used in a request to return the next batch of the results.

errors -> (list)

A list of any errors returned while describing the merge conflicts for each file.

(structure)

Returns information about errors in a BatchDescribeMergeConflicts operation.

filePath -> (string)

The path to the file.

exceptionName -> (string)

The name of the exception.

message -> (string)

The message provided by the exception.

destinationCommitId -> (string)

The commit ID of the destination commit specifier that was used in the merge evaluation.

sourceCommitId -> (string)

The commit ID of the source commit specifier that was used in the merge evaluation.

baseCommitId -> (string)

The commit ID of the merge base.