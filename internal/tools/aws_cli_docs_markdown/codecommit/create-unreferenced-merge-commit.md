# create-unreferenced-merge-commitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-unreferenced-merge-commit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-unreferenced-merge-commit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# create-unreferenced-merge-commit

## Description

Creates an unreferenced commit that represents the result of merging two branches using a specified merge strategy. This can help you determine the outcome of a potential merge. This API cannot be used with the fast-forward merge strategy because that strategy does not create a merge commit.

### Note

This unreferenced merge commit can only be accessed using the GetCommit API or through git commands such as git fetch. To retrieve this commit, you must specify its commit ID or otherwise reference it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateUnreferencedMergeCommit)

## Synopsis

```
create-unreferenced-merge-commit
--repository-name <value>
--source-commit-specifier <value>
--destination-commit-specifier <value>
--merge-option <value>
[--conflict-detail-level <value>]
[--conflict-resolution-strategy <value>]
[--author-name <value>]
[--email <value>]
[--commit-message <value>]
[--keep-empty-folders | --no-keep-empty-folders]
[--conflict-resolution <value>]
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

The name of the repository where you want to create the unreferenced merge commit.

`--source-commit-specifier` (string)

The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).

`--destination-commit-specifier` (string)

The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, a branch name or a full commit ID).

`--merge-option` (string)

The merge option or strategy you want to use to merge the code.

Possible values:

- `FAST_FORWARD_MERGE`
- `SQUASH_MERGE`
- `THREE_WAY_MERGE`

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

`--author-name` (string)

The name of the author who created the unreferenced commit. This information is used as both the author and committer for the commit.

`--email` (string)

The email address for the person who created the unreferenced commit.

`--commit-message` (string)

The commit message for the unreferenced commit.

`--keep-empty-folders` | `--no-keep-empty-folders` (boolean)

If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If this is specified as true, a .gitkeep file is created for empty folders. The default is false.

`--conflict-resolution` (structure)

If AUTOMERGE is the conflict resolution strategy, a list of inputs to use when resolving conflicts during a merge.

replaceContents -> (list)

Files to have content replaced as part of the merge conflict resolution.

(structure)

Information about a replacement content entry in the conflict of a merge or pull request operation.

filePath -> (string)

The path of the conflicting file.

replacementType -> (string)

The replacement type to use when determining how to resolve the conflict.

content -> (blob)

The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.

fileMode -> (string)

The file mode to apply during conflict resoltion.

deleteFiles -> (list)

Files to be deleted as part of the merge conflict resolution.

(structure)

A file that is deleted as part of a commit.

filePath -> (string)

The full path of the file to be deleted, including the name of the file.

setFileModes -> (list)

File modes that are set as part of the merge conflict resolution.

(structure)

Information about the file mode changes.

filePath -> (string)

The full path to the file, including the name of the file.

fileMode -> (string)

The file mode for the file.

Shorthand Syntax:

```
replaceContents=[{filePath=string,replacementType=string,content=blob,fileMode=string},{filePath=string,replacementType=string,content=blob,fileMode=string}],deleteFiles=[{filePath=string},{filePath=string}],setFileModes=[{filePath=string,fileMode=string},{filePath=string,fileMode=string}]
```

JSON Syntax:

```
{
  "replaceContents": [
    {
      "filePath": "string",
      "replacementType": "KEEP_BASE"|"KEEP_SOURCE"|"KEEP_DESTINATION"|"USE_NEW_CONTENT",
      "content": blob,
      "fileMode": "EXECUTABLE"|"NORMAL"|"SYMLINK"
    }
    ...
  ],
  "deleteFiles": [
    {
      "filePath": "string"
    }
    ...
  ],
  "setFileModes": [
    {
      "filePath": "string",
      "fileMode": "EXECUTABLE"|"NORMAL"|"SYMLINK"
    }
    ...
  ]
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create an unreferenced commit that represents the result of merging two commit specifiers**

The following `create-unreferenced-merge-commit` example creates a commit that represents the results of a merge between a source branch named `bugfix-1234` with a destination branch named `main` using the THREE_WAY_MERGE strategy in a repository named `MyDemoRepo`.

```
aws codecommit create-unreferenced-merge-commit \
    --source-commit-specifier bugfix-1234 \
    --destination-commit-specifier main \
    --merge-option THREE_WAY_MERGE \
    --repository-name MyDemoRepo \
    --name "Maria Garcia" \
    --email "maria_garcia@example.com" \
    --commit-message "Testing the results of this merge."
```

Output:

```
{
    "commitId": "4f178133EXAMPLE",
    "treeId": "389765daEXAMPLE"
}
```

For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#batch-describe-merge-conflicts) in the *AWS CodeCommit User Guide*.

## Output

commitId -> (string)

The full commit ID of the commit that contains your merge results.

treeId -> (string)

The full SHA-1 pointer of the tree information for the commit that contains the merge results.