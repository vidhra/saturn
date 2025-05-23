# list-engagement-by-accepting-invitation-tasksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-by-accepting-invitation-tasks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/list-engagement-by-accepting-invitation-tasks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# list-engagement-by-accepting-invitation-tasks

## Description

Lists all in-progress, completed, or failed StartEngagementByAcceptingInvitationTask tasks that were initiated by the callerâs account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/ListEngagementByAcceptingInvitationTasks)

`list-engagement-by-accepting-invitation-tasks` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TaskSummaries`

## Synopsis

```
list-engagement-by-accepting-invitation-tasks
--catalog <value>
[--engagement-invitation-identifier <value>]
[--opportunity-identifier <value>]
[--sort <value>]
[--task-identifier <value>]
[--task-status <value>]
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

`--catalog` (string)

Specifies the catalog related to the request. Valid values are:

- AWS: Retrieves the request from the production AWS environment.
- Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes.

`--engagement-invitation-identifier` (list)

Filters tasks by the identifiers of the engagement invitations they are processing.

(string)

Syntax:

```
"string" "string" ...
```

`--opportunity-identifier` (list)

Filters tasks by the identifiers of the opportunities they created or are associated with.

(string)

Syntax:

```
"string" "string" ...
```

`--sort` (structure)

Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes.

SortBy -> (string)

Specifies the field by which the task list should be sorted.

SortOrder -> (string)

Determines the order in which the sorted results are presented.

Shorthand Syntax:

```
SortBy=string,SortOrder=string
```

JSON Syntax:

```
{
  "SortBy": "StartTime",
  "SortOrder": "ASCENDING"|"DESCENDING"
}
```

`--task-identifier` (list)

Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks.

(string)

Syntax:

```
"string" "string" ...
```

`--task-status` (list)

Filters the tasks based on their current status. This allows you to focus on tasks in specific states.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  IN_PROGRESS
  COMPLETE
  FAILED
```

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

## Output

NextToken -> (string)

A token used for pagination to retrieve the next page of results.If there are more results available, this field will contain a token that can be used in a subsequent API call to retrieve the next page. If there are no more results, this field will be null or an empty string.

TaskSummaries -> (list)

An array of `EngagementByAcceptingInvitationTaskSummary` objects, each representing a task that matches the specified filters. The array may be empty if no tasks match the criteria.

(structure)

Specifies a subset of fields associated with tasks related to accepting an engagement invitation.

EngagementInvitationId -> (string)

The unique identifier of the engagement invitation that was accepted.

Message -> (string)

Detailed message describing the failure and possible recovery steps.

OpportunityId -> (string)

Unique identifier of opportunity that was created.

ReasonCode -> (string)

A code pointing to the specific reason for the failure.

ResourceSnapshotJobId -> (string)

Unique identifier of the resource snapshot job that was created.

StartTime -> (timestamp)

Task start timestamp.

TaskArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the task.

TaskId -> (string)

Unique identifier of the task.

TaskStatus -> (string)

Status of the task.