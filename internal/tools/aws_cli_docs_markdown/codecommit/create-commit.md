# create-commitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# create-commit

## Description

Creates a commit for a repository on the tip of a specified branch.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/CreateCommit)

## Synopsis

```
create-commit
--repository-name <value>
--branch-name <value>
[--parent-commit-id <value>]
[--author-name <value>]
[--email <value>]
[--commit-message <value>]
[--keep-empty-folders | --no-keep-empty-folders]
[--put-files <value>]
[--delete-files <value>]
[--set-file-modes <value>]
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

The name of the repository where you create the commit.

`--branch-name` (string)

The name of the branch where you create the commit.

`--parent-commit-id` (string)

The ID of the commit that is the parent of the commit you create. Not required if this is an empty repository.

`--author-name` (string)

The name of the author who created the commit. This information is used as both the author and committer for the commit.

`--email` (string)

The email address of the person who created the commit.

`--commit-message` (string)

The commit message you want to include in the commit. Commit messages are limited to 256 KB. If no message is specified, a default message is used.

`--keep-empty-folders` | `--no-keep-empty-folders` (boolean)

If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a ..gitkeep file is created for empty folders. The default is false.

`--put-files` (list)

The files to add or update in this commit.

(structure)

Information about a file added or updated as part of a commit.

filePath -> (string)

The full path to the file in the repository, including the name of the file.

fileMode -> (string)

The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.

fileContent -> (blob)

The content of the file, if a source file is not specified.

sourceFile -> (structure)

The name and full path of the file that contains the changes you want to make as part of the commit, if you are not providing the file content directly.

filePath -> (string)

The full path to the file, including the name of the file.

isMove -> (boolean)

Whether to remove the source file from the parent commit.

Shorthand Syntax:

```
filePath=string,fileMode=string,fileContent=blob,sourceFile={filePath=string,isMove=boolean} ...
```

JSON Syntax:

```
[
  {
    "filePath": "string",
    "fileMode": "EXECUTABLE"|"NORMAL"|"SYMLINK",
    "fileContent": blob,
    "sourceFile": {
      "filePath": "string",
      "isMove": true|false
    }
  }
  ...
]
```

`--delete-files` (list)

The files to delete in this commit. These files still exist in earlier commits.

(structure)

A file that is deleted as part of a commit.

filePath -> (string)

The full path of the file to be deleted, including the name of the file.

Shorthand Syntax:

```
filePath=string ...
```

JSON Syntax:

```
[
  {
    "filePath": "string"
  }
  ...
]
```

`--set-file-modes` (list)

The file modes to update for files in this commit.

(structure)

Information about the file mode changes.

filePath -> (string)

The full path to the file, including the name of the file.

fileMode -> (string)

The file mode for the file.

Shorthand Syntax:

```
filePath=string,fileMode=string ...
```

JSON Syntax:

```
[
  {
    "filePath": "string",
    "fileMode": "EXECUTABLE"|"NORMAL"|"SYMLINK"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a commit**

The following `create-commit` example demonstrates how to create an initial commit for a repository that adds a `readme.md` file to a repository named `MyDemoRepo` in the `main` branch.

```
aws codecommit create-commit \
    --repository-name MyDemoRepo \
    --branch-name main \
    --put-files "filePath=readme.md,fileContent='Welcome to our team repository.'"
```

Output:

```
{
    "filesAdded": [
        {
            "blobId": "5e1c309d-EXAMPLE",
            "absolutePath": "readme.md",
            "fileMode": "NORMAL"
        }
    ],
    "commitId": "4df8b524-EXAMPLE",
    "treeId": "55b57003-EXAMPLE",
    "filesDeleted": [],
    "filesUpdated": []
}
```

For more information, see [Create a Commit in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html#how-to-create-commit-cli) in the *AWS CodeCommit User Guide*.

## Output

commitId -> (string)

The full commit ID of the commit that contains your committed file changes.

treeId -> (string)

The full SHA-1 pointer of the tree information for the commit that contains the commited file changes.

filesAdded -> (list)

The files added as part of the committed file changes.

(structure)

A file to be added, updated, or deleted as part of a commit.

absolutePath -> (string)

The full path to the file to be added or updated, including the name of the file.

blobId -> (string)

The blob ID that contains the file information.

fileMode -> (string)

The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.

filesUpdated -> (list)

The files updated as part of the commited file changes.

(structure)

A file to be added, updated, or deleted as part of a commit.

absolutePath -> (string)

The full path to the file to be added or updated, including the name of the file.

blobId -> (string)

The blob ID that contains the file information.

fileMode -> (string)

The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.

filesDeleted -> (list)

The files deleted as part of the committed file changes.

(structure)

A file to be added, updated, or deleted as part of a commit.

absolutePath -> (string)

The full path to the file to be added or updated, including the name of the file.

blobId -> (string)

The blob ID that contains the file information.

fileMode -> (string)

The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.