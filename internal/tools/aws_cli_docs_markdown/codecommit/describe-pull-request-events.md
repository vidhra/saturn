# describe-pull-request-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-pull-request-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-pull-request-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/index.html#cli-aws-codecommit) ]

# describe-pull-request-events

## Description

Returns information about one or more pull request events.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecommit-2015-04-13/DescribePullRequestEvents)

`describe-pull-request-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `pullRequestEvents`

## Synopsis

```
describe-pull-request-events
--pull-request-id <value>
[--pull-request-event-type <value>]
[--actor-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--pull-request-event-type` (string)

Optional. The pull request event type about which you want to return information.

Possible values:

- `PULL_REQUEST_CREATED`
- `PULL_REQUEST_STATUS_CHANGED`
- `PULL_REQUEST_SOURCE_REFERENCE_UPDATED`
- `PULL_REQUEST_MERGE_STATE_CHANGED`
- `PULL_REQUEST_APPROVAL_RULE_CREATED`
- `PULL_REQUEST_APPROVAL_RULE_UPDATED`
- `PULL_REQUEST_APPROVAL_RULE_DELETED`
- `PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN`
- `PULL_REQUEST_APPROVAL_STATE_CHANGED`

`--actor-arn` (string)

The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To view events in a pull request**

The following `describe-pull-request-events` example retrieves the events for a pull request with the ID of â8â.

```
aws codecommit describe-pull-request-events --pull-request-id 8
```

Output:

```
{
    "pullRequestEvents": [
        {
            "pullRequestId": "8",
            "pullRequestEventType": "PULL_REQUEST_CREATED",
            "eventDate": 1510341779.53,
            "actor": "arn:aws:iam::111111111111:user/Zhang_Wei"
        },
        {
            "pullRequestStatusChangedEventMetadata": {
                "pullRequestStatus": "CLOSED"
            },
            "pullRequestId": "8",
            "pullRequestEventType": "PULL_REQUEST_STATUS_CHANGED",
            "eventDate": 1510341930.72,
            "actor": "arn:aws:iam::111111111111:user/Jane_Doe"
        }
    ]
}
```

## Output

pullRequestEvents -> (list)

Information about the pull request events.

(structure)

Returns information about a pull request event.

pullRequestId -> (string)

The system-generated ID of the pull request.

eventDate -> (timestamp)

The day and time of the pull request event, in timestamp format.

pullRequestEventType -> (string)

The type of the pull request event (for example, a status change event (PULL_REQUEST_STATUS_CHANGED) or update event (PULL_REQUEST_SOURCE_REFERENCE_UPDATED)).

actorArn -> (string)

The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.

pullRequestCreatedEventMetadata -> (structure)

Information about the source and destination branches for the pull request.

repositoryName -> (string)

The name of the repository where the pull request was created.

sourceCommitId -> (string)

The commit ID on the source branch used when the pull request was created.

destinationCommitId -> (string)

The commit ID of the tip of the branch specified as the destination branch when the pull request was created.

mergeBase -> (string)

The commit ID of the most recent commit that the source branch and the destination branch have in common.

pullRequestStatusChangedEventMetadata -> (structure)

Information about the change in status for the pull request event.

pullRequestStatus -> (string)

The changed status of the pull request.

pullRequestSourceReferenceUpdatedEventMetadata -> (structure)

Information about the updated source branch for the pull request event.

repositoryName -> (string)

The name of the repository where the pull request was updated.

beforeCommitId -> (string)

The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was updated.

afterCommitId -> (string)

The full commit ID of the commit in the source branch that was the tip of the branch at the time the pull request was updated.

mergeBase -> (string)

The commit ID of the most recent commit that the source branch and the destination branch have in common.

pullRequestMergedStateChangedEventMetadata -> (structure)

Information about the change in mergability state for the pull request event.

repositoryName -> (string)

The name of the repository where the pull request was created.

destinationReference -> (string)

The name of the branch that the pull request is merged into.

mergeMetadata -> (structure)

Information about the merge state change event.

isMerged -> (boolean)

A Boolean value indicating whether the merge has been made.

mergedBy -> (string)

The Amazon Resource Name (ARN) of the user who merged the branches.

mergeCommitId -> (string)

The commit ID for the merge commit, if any.

mergeOption -> (string)

The merge strategy used in the merge.

approvalRuleEventMetadata -> (structure)

Information about a pull request event.

approvalRuleName -> (string)

The name of the approval rule.

approvalRuleId -> (string)

The system-generated ID of the approval rule.

approvalRuleContent -> (string)

The content of the approval rule.

approvalStateChangedEventMetadata -> (structure)

Information about an approval state change for a pull request.

revisionId -> (string)

The revision ID of the pull request when the approval state changed.

approvalStatus -> (string)

The approval status for the pull request.

approvalRuleOverriddenEventMetadata -> (structure)

Information about an approval rule override event for a pull request.

revisionId -> (string)

The revision ID of the pull request when the override event occurred.

overrideStatus -> (string)

The status of the override event.

nextToken -> (string)

An enumeration token that can be used in a request to return the next batch of the results.