# list-file-commit-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-file-commit-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-file-commit-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# list-file-commit-history

## Description

Retrieves a list of commits and changes to a specified file.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/ListFileCommitHistory)

## Synopsis

```
list-file-commit-history
--repository-name <value>
[--commit-specifier <value>]
--file-path <value>
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

`--repository-name` (string)

The name of the repository that contains the file.

`--commit-specifier` (string)

The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as `refs/heads/main` . If none is provided, the head commit is used.

`--file-path` (string)

The full path of the file whose history you want to retrieve, including the name of the file.

`--max-results` (integer)

A non-zero, non-negative integer used to limit the number of returned results.

`--next-token` (string)

An enumeration token that allows the operation to batch the results.

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

revisionDag -> (list)

An array of FileVersion objects that form a directed acyclic graph (DAG) of the changes to the file made by the commits that changed the file.

(structure)

Information about a version of a file.

commit -> (structure)

Returns information about a specific commit.

commitId -> (string)

The full SHA ID of the specified commit.

treeId -> (string)

Tree information for the specified commit.

parents -> (list)

A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.

(string)

message -> (string)

The commit message associated with the specified commit.

author -> (structure)

Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.

name -> (string)

The name of the user who made the specified commit.

email -> (string)

The email address associated with the user who made the commit, if any.

date -> (string)

The date when the specified commit was commited, in timestamp format with GMT offset.

committer -> (structure)

Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.

For more information about the difference between an author and a committer in Git, see [Viewing the Commit History](http://git-scm.com/book/ch2-3.html) in Pro Git by Scott Chacon and Ben Straub.

name -> (string)

The name of the user who made the specified commit.

email -> (string)

The email address associated with the user who made the commit, if any.

date -> (string)

The date when the specified commit was commited, in timestamp format with GMT offset.

additionalData -> (string)

Any other data associated with the specified commit.

blobId -> (string)

The blob ID of the object that represents the content of the file in this version.

path -> (string)

The name and path of the file at which this blob is indexed which contains the data for this version of the file. This value will vary between file versions if a file is renamed or if its path changes.

revisionChildren -> (list)

An array of commit IDs that contain more recent versions of this file. If there are no additional versions of the file, this array will be empty.

(string)

nextToken -> (string)

An enumeration token that can be used to return the next batch of results.