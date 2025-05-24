# update-pull-request-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# update-pull-request-status

## Description

Updates the status of a pull request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestStatus)

## Synopsis

```
update-pull-request-status
--pull-request-id <value>
--pull-request-status <value>
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

`--pull-request-status` (string)

The status of the pull request. The only valid operations are to update the status from `OPEN` to `OPEN` , `OPEN` to `CLOSED` or from `CLOSED` to `CLOSED` .

Possible values:

- `OPEN`
- `CLOSED`

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

**To change the status of a pull request**

This example demonstrates how to to change the status of a pull request with the ID of `42` to a status of `CLOSED` in an AWS CodeCommit repository named `MyDemoRepo`.

```
aws codecommit update-pull-request-status \
    --pull-request-id 42 \
    --pull-request-status CLOSED
```

Output:

```
{
    "pullRequest": {
        "approvalRules": [
            {
                "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}",
                "approvalRuleId": "dd8b17fe-EXAMPLE",
                "approvalRuleName": "2-approvers-needed-for-this-change",
                "creationDate": 1571356106.936,
                "lastModifiedDate": 571356106.936,
                "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
                "ruleContentSha256": "4711b576EXAMPLE"
            }
        ],
        "authorArn": "arn:aws:iam::123456789012:user/Li_Juan",
        "clientRequestToken": "",
        "creationDate": 1508530823.165,
        "description": "Updated the pull request to remove unused global variable.",
        "lastActivityDate": 1508372423.12,
        "pullRequestId": "47",
        "pullRequestStatus": "CLOSED",
        "pullRequestTargets": [
            {
                "destinationCommit": "9f31c968EXAMPLE",
                "destinationReference": "refs/heads/main",
                "mergeMetadata": {
                    "isMerged": false,
                },
                "repositoryName": "MyDemoRepo",
                "sourceCommit": "99132ab0EXAMPLE",
                "sourceReference": "refs/heads/variables-branch"
            }
        ],
        "title": "Consolidation of global variables"
    }
}
```

## Output

pullRequest -> (structure)

Information about the pull request.

pullRequestId -> (string)

The system-generated ID of the pull request.

title -> (string)

The user-defined title of the pull request. This title is displayed in the list of pull requests to other repository users.

description -> (string)

The user-defined description of the pull request. This description can be used to clarify what should be reviewed and other details of the request.

lastActivityDate -> (timestamp)

The day and time of the last user or system activity on the pull request, in timestamp format.

creationDate -> (timestamp)

The date and time the pull request was originally created, in timestamp format.

pullRequestStatus -> (string)

The status of the pull request. Pull request status can only change from `OPEN` to `CLOSED` .

authorArn -> (string)

The Amazon Resource Name (ARN) of the user who created the pull request.

pullRequestTargets -> (list)

The targets of the pull request, including the source branch and destination branch for the pull request.

(structure)

Returns information about a pull request target.

repositoryName -> (string)

The name of the repository that contains the pull request source and destination branches.

sourceReference -> (string)

The branch of the repository that contains the changes for the pull request. Also known as the source branch.

destinationReference -> (string)

The branch of the repository where the pull request changes are merged. Also known as the destination branch.

destinationCommit -> (string)

The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.

sourceCommit -> (string)

The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.

mergeBase -> (string)

The commit ID of the most recent commit that the source branch and the destination branch have in common.

mergeMetadata -> (structure)

Returns metadata about the state of the merge, including whether the merge has been made.

isMerged -> (boolean)

A Boolean value indicating whether the merge has been made.

mergedBy -> (string)

The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId -> (string)

The commit ID for the merge commit, if any.

mergeOption -> (string)

The merge strategy used in the merge.

clientRequestToken -> (string)

A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.

revisionId -> (string)

The system-generated revision ID for the pull request.

approvalRules -> (list)

The approval rules applied to the pull request.

(structure)

Returns information about an approval rule.

approvalRuleId -> (string)

The system-generated ID of the approval rule.

approvalRuleName -> (string)

The name of the approval rule.

approvalRuleContent -> (string)

The content of the approval rule.

ruleContentSha256 -> (string)

The SHA-256 hash signature for the content of the approval rule.

lastModifiedDate -> (timestamp)

The date the approval rule was most recently changed, in timestamp format.

creationDate -> (timestamp)

The date the approval rule was created, in timestamp format.

lastModifiedUser -> (string)

The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.

originApprovalRuleTemplate -> (structure)

The approval rule template used to create the rule.

approvalRuleTemplateId -> (string)

The ID of the template that created the approval rule.

approvalRuleTemplateName -> (string)

The name of the template that created the approval rule.