# list-document-metadata-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-metadata-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-metadata-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# list-document-metadata-history

## Description

Information about approval reviews for a version of a change template in Change Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListDocumentMetadataHistory)

## Synopsis

```
list-document-metadata-history
--name <value>
[--document-version <value>]
--metadata <value>
[--next-token <value>]
[--max-results <value>]
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

The name of the change template.

`--document-version` (string)

The version of the change template.

`--metadata` (string)

The type of data for which details are being requested. Currently, the only supported value is `DocumentReviews` .

Possible values:

- `DocumentReviews`

`--next-token` (string)

The token for the next set of items to return. (You received this token from a previous call.)

`--max-results` (integer)

The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.

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

**Example: To view approval history and status for a change template**

The following `list-document-metadata-history` example returns the approval history for the specified Change Manager change template.

```
aws ssm list-document-metadata-history \
    --name MyChangeManageTemplate \
    --metadata DocumentReviews
```

Output:

```
{
    "Name": "MyChangeManagerTemplate",
    "DocumentVersion": "1",
    "Author": "arn:aws:iam::111222333444;:user/JohnDoe",
    "Metadata": {
        "ReviewerResponse": [
            {
                "CreateTime": "2021-07-30T11:58:28.025000-07:00",
                "UpdatedTime": "2021-07-30T12:01:19.274000-07:00",
                "ReviewStatus": "APPROVED",
                "Comment": [
                    {
                        "Type": "COMMENT",
                        "Content": "I approve this template version"
                    }
                ],
                "Reviewer": "arn:aws:iam::111222333444;:user/ShirleyRodriguez"
            },
            {
                "CreateTime": "2021-07-30T11:58:28.025000-07:00",
                "UpdatedTime": "2021-07-30T11:58:28.025000-07:00",
                "ReviewStatus": "PENDING"
            }
        ]
    }
}
```

For more information, see [Reviewing and approving or rejecting change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-review.html) in the *AWS Systems Manager User Guide*.

## Output

Name -> (string)

The name of the change template.

DocumentVersion -> (string)

The version of the change template.

Author -> (string)

The user ID of the person in the organization who requested the review of the change template.

Metadata -> (structure)

Information about the response to the change template approval request.

ReviewerResponse -> (list)

Details about a reviewerâs response to a document review request.

(structure)

Information about a reviewerâs response to a document review request.

CreateTime -> (timestamp)

The date and time that a reviewer entered a response to a document review request.

UpdatedTime -> (timestamp)

The date and time that a reviewer last updated a response to a document review request.

ReviewStatus -> (string)

The current review status of a new custom SSM document created by a member of your organization, or of the latest version of an existing SSM document.

Only one version of a document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.

Only one version of a document can be in review, or PENDING, at a time.

Comment -> (list)

The comment entered by a reviewer as part of their document review response.

(structure)

Information about comments added to a document review request.

Type -> (string)

The type of information added to a review request. Currently, only the value `Comment` is supported.

Content -> (string)

The content of a comment entered by a user who requests a review of a new document version, or who reviews the new version.

Reviewer -> (string)

The user in your organization assigned to review a document request.

NextToken -> (string)

The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.