# describe-scheduled-actionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# describe-scheduled-actions

## Description

Describes properties of scheduled actions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/DescribeScheduledActions)

`describe-scheduled-actions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ScheduledActions`

## Synopsis

```
describe-scheduled-actions
[--scheduled-action-name <value>]
[--target-action-type <value>]
[--start-time <value>]
[--end-time <value>]
[--active | --no-active]
[--filters <value>]
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

`--scheduled-action-name` (string)

The name of the scheduled action to retrieve.

`--target-action-type` (string)

The type of the scheduled actions to retrieve.

Possible values:

- `ResizeCluster`
- `PauseCluster`
- `ResumeCluster`

`--start-time` (timestamp)

The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.

`--end-time` (timestamp)

The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.

`--active` | `--no-active` (boolean)

If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions.

`--filters` (list)

List of scheduled action filters.

(structure)

A set of elements to filter the returned scheduled actions.

Name -> (string)

The type of element to filter.

Values -> (list)

List of values. Compare if the value (of type defined by `Name` ) equals an item in the list of scheduled actions.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "cluster-identifier"|"iam-role",
    "Values": ["string", ...]
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe scheduled actions**

The following `describe-scheduled-actions` example displays details for any currently scheduled actions.

```
aws redshift describe-scheduled-actions
```

Output:

```
{
    "ScheduledActions": [
        {
            "ScheduledActionName": "resizecluster",
            "TargetAction": {
                "ResizeCluster": {
                    "ClusterIdentifier": "mycluster",
                    "NumberOfNodes": 4,
                    "Classic": false
                }
            },
            "Schedule": "at(2019-12-10T00:07:00)",
            "IamRole": "arn:aws:iam::123456789012:role/myRedshiftRole",
            "State": "ACTIVE",
            "NextInvocations": [
                "2019-12-10T00:07:00Z"
            ]
        }
    ]
}
```

## Output

Marker -> (string)

An optional parameter that specifies the starting point to return a set of response records. When the results of a  DescribeScheduledActions request exceed the value specified in `MaxRecords` , Amazon Web Services returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.

ScheduledActions -> (list)

List of retrieved scheduled actions.

(structure)

Describes a scheduled action. You can use a scheduled action to trigger some Amazon Redshift API operations on a schedule. For information about which API operations can be scheduled, see  ScheduledActionType .

ScheduledActionName -> (string)

The name of the scheduled action.

TargetAction -> (structure)

A JSON format string of the Amazon Redshift API operation with input parameters.

â`{\"ResizeCluster\":{\"NodeType\":\"ra3.4xlarge\",\"ClusterIdentifier\":\"my-test-cluster\",\"NumberOfNodes\":3}}` â.

ResizeCluster -> (structure)

An action that runs a `ResizeCluster` API operation.

ClusterIdentifier -> (string)

The unique identifier for the cluster to resize.

ClusterType -> (string)

The new cluster type for the specified cluster.

NodeType -> (string)

The new node type for the nodes you are adding. If not specified, the clusterâs current node type is used.

NumberOfNodes -> (integer)

The new number of nodes for the cluster. If not specified, the clusterâs current number of nodes is used.

Classic -> (boolean)

A boolean value indicating whether the resize operation is using the classic resize process. If you donât provide this parameter or set the value to `false` , the resize type is elastic.

ReservedNodeId -> (string)

The identifier of the reserved node.

TargetReservedNodeOfferingId -> (string)

The identifier of the target reserved node offering.

PauseCluster -> (structure)

An action that runs a `PauseCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be paused.

ResumeCluster -> (structure)

An action that runs a `ResumeCluster` API operation.

ClusterIdentifier -> (string)

The identifier of the cluster to be resumed.

Schedule -> (string)

The schedule for a one-time (at format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour.

Format of at expressions is â`at(yyyy-mm-ddThh:mm:ss)` â. For example, â`at(2016-03-04T17:27:00)` â.

Format of cron expressions is â`cron(Minutes Hours Day-of-month Month Day-of-week Year)` â. For example, â`cron(0 10 ? * MON *)` â. For more information, see [Cron Expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) in the *Amazon CloudWatch Events User Guide* .

IamRole -> (string)

The IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see [Using Identity-Based Policies for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the *Amazon Redshift Cluster Management Guide* .

ScheduledActionDescription -> (string)

The description of the scheduled action.

State -> (string)

The state of the scheduled action. For example, `DISABLED` .

NextInvocations -> (list)

List of times when the scheduled action will run.

(timestamp)

StartTime -> (timestamp)

The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.

EndTime -> (timestamp)

The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.