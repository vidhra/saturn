# update-pull-request-approval-rule-contentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-rule-content.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-rule-content.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# update-pull-request-approval-rule-content

## Description

Updates the structure of an approval rule created specifically for a pull request. For example, you can change the number of required approvers and the approval pool for approvers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/UpdatePullRequestApprovalRuleContent)

## Synopsis

```
update-pull-request-approval-rule-content
--pull-request-id <value>
--approval-rule-name <value>
[--existing-rule-content-sha256 <value>]
--new-rule-content <value>
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

The system-generated ID of the pull request.

`--approval-rule-name` (string)

The name of the approval rule you want to update.

`--existing-rule-content-sha256` (string)

The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using  GetPullRequest .

`--new-rule-content` (string)

The updated content for the approval rule.

### Note

When you update the content of the approval rule, you can specify approvers in an approval pool in one of two ways:

- **CodeCommitApprovers** : This option only requires an Amazon Web Services account and a resource. It can be used for both IAM users and federated access users whose name matches the provided resource name. This is a very powerful option that offers a great deal of flexibility. For example, if you specify the Amazon Web Services account *123456789012* and *Mary_Major* , all of the following are counted as approvals coming from that user:
- An IAM user in the account (arn:aws:iam::*123456789012* :user/*Mary_Major* )
- A federated user identified in IAM as Mary_Major (arn:aws:sts::*123456789012* :federated-user/*Mary_Major* )

This option does not recognize an active session of someone assuming the role of CodeCommitReview with a role session name of *Mary_Major* (arn:aws:sts::*123456789012* :assumed-role/CodeCommitReview/*Mary_Major* ) unless you include a wildcard ([*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-rule-content.html#id1)Mary_Major).

- **Fully qualified ARN** : This option allows you to specify the fully qualified Amazon Resource Name (ARN) of the IAM user or role.

For more information about IAM ARNs, wildcards, and formats, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide* .

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

**To edit an approval rule for a pull request**

The following `update-pull-request-approval-rule-content` example updates she specified approval rule to require one user approval from an approval pool that includes any IAM user in the `123456789012` AWS account.

```
aws codecommit update-pull-request-approval-rule-content \
    --pull-request-id 27  \
    --approval-rule-name "Require two approved approvers" \
    --approval-rule-content "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 1, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/*\"]}]}}"
```

Output:

```
{
    "approvalRule": {
        "approvalRuleContent": "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 1, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/*\"]}]}}",
        "approvalRuleId": "aac33506-EXAMPLE",
        "originApprovalRuleTemplate": {},
        "creationDate": 1570752871.932,
        "lastModifiedDate": 1570754058.333,
        "approvalRuleName": Require two approved approvers",
        "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major",
        "ruleContentSha256": "cd93921cEXAMPLE",
    }
}
```

For more information, see [Edit or Delete an Approval Rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-delete-pull-request-approval-rule.html#update-pull-request-approval-rule-content) in the *AWS CodeCommit User Guide*.

## Output

approvalRule -> (structure)

Information about the updated approval rule.

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