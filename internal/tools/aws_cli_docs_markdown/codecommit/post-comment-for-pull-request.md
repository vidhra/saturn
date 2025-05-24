# post-comment-for-pull-requestÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-pull-request.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-pull-request.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# post-comment-for-pull-request

## Description

Posts a comment on a pull request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/PostCommentForPullRequest)

## Synopsis

```
post-comment-for-pull-request
--pull-request-id <value>
--repository-name <value>
--before-commit-id <value>
--after-commit-id <value>
[--location <value>]
--content <value>
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

`--pull-request-id` (string)

The system-generated ID of the pull request. To get this ID, use  ListPullRequests .

`--repository-name` (string)

The name of the repository where you want to post a comment on a pull request.

`--before-commit-id` (string)

The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.

`--after-commit-id` (string)

The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.

`--location` (structure)

The location of the change where you want to post your comment. If no location is provided, the comment is posted as a general comment on the pull request difference between the before commit ID and the after commit ID.

filePath -> (string)

The name of the file being compared, including its extension and subdirectory, if any.

filePosition -> (long)

The position of a change in a compared file, in line number format.

relativeFileVersion -> (string)

In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.

Shorthand Syntax:

```
filePath=string,filePosition=long,relativeFileVersion=string
```

JSON Syntax:

```
{
  "filePath": "string",
  "filePosition": long,
  "relativeFileVersion": "BEFORE"|"AFTER"
}
```

`--content` (string)

The content of your comment on the change.

`--client-request-token` (string)

A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

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

**To add a comment to a pull request**

The following `post-comment-for-pull-request` example adds the comment âThese donât appear to be used anywhere. Can we remove them?â on the change to the `ahs_count.py` file in a pull request with the ID of `47` in a repository named `MyDemoRepo`.

```
aws codecommit post-comment-for-pull-request \
    --pull-request-id "47" \
    --repository-name MyDemoRepo \
    --before-commit-id 317f8570EXAMPLE \
    --after-commit-id 5d036259EXAMPLE \
    --client-request-token 123Example \
    --content "These don't appear to be used anywhere. Can we remove them?" \
    --location filePath=ahs_count.py,filePosition=367,relativeFileVersion=AFTER
```

Output:

```
{
     "afterBlobId": "1f330709EXAMPLE",
     "afterCommitId": "5d036259EXAMPLE",
     "beforeBlobId": "80906a4cEXAMPLE",
     "beforeCommitId": "317f8570EXAMPLE",
     "comment": {
            "authorArn": "arn:aws:iam::111111111111:user/Saanvi_Sarkar",
            "clientRequestToken": "123Example",
            "commentId": "abcd1234EXAMPLEb5678efgh",
            "content": "These don't appear to be used anywhere. Can we remove them?",
            "creationDate": 1508369622.123,
            "deleted": false,
            "CommentId": "",
            "lastModifiedDate": 1508369622.123,
            "callerReactions": [],
            "reactionCounts": []
        },
        "location": {
            "filePath": "ahs_count.py",
            "filePosition": 367,
            "relativeFileVersion": "AFTER"
         },
     "repositoryName": "MyDemoRepo",
     "pullRequestId": "47"
}
```

## Output

repositoryName -> (string)

The name of the repository where you posted a comment on a pull request.

pullRequestId -> (string)

The system-generated ID of the pull request.

beforeCommitId -> (string)

The full commit ID of the commit in the source branch used to create the pull request, or in the case of an updated pull request, the full commit ID of the commit used to update the pull request.

afterCommitId -> (string)

The full commit ID of the commit in the destination branch where the pull request is merged.

beforeBlobId -> (string)

In the directionality of the pull request, the blob ID of the before blob.

afterBlobId -> (string)

In the directionality of the pull request, the blob ID of the after blob.

location -> (structure)

The location of the change where you posted your comment.

filePath -> (string)

The name of the file being compared, including its extension and subdirectory, if any.

filePosition -> (long)

The position of a change in a compared file, in line number format.

relativeFileVersion -> (string)

In a comparison of commits or a pull request, whether the change is in the before or after of that comparison.

comment -> (structure)

The content of the comment you posted.

commentId -> (string)

The system-generated comment ID.

content -> (string)

The content of the comment.

inReplyTo -> (string)

The ID of the comment for which this comment is a reply, if any.

creationDate -> (timestamp)

The date and time the comment was created, in timestamp format.

lastModifiedDate -> (timestamp)

The date and time the comment was most recently modified, in timestamp format.

authorArn -> (string)

The Amazon Resource Name (ARN) of the person who posted the comment.

deleted -> (boolean)

A Boolean value indicating whether the comment has been deleted.

clientRequestToken -> (string)

A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

callerReactions -> (list)

The emoji reactions to a comment, if any, submitted by the user whose credentials are associated with the call to the API.

(string)

reactionCounts -> (map)

A string to integer map that represents the number of individual users who have responded to a comment with the specified reactions.

key -> (string)

value -> (integer)