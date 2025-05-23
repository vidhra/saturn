# describe-update-actionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-update-actions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-update-actions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# describe-update-actions

## Description

Returns details of the update actions

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeUpdateActions)

`describe-update-actions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `UpdateActions`

## Synopsis

```
describe-update-actions
[--service-update-name <value>]
[--replication-group-ids <value>]
[--cache-cluster-ids <value>]
[--engine <value>]
[--service-update-status <value>]
[--service-update-time-range <value>]
[--update-action-status <value>]
[--show-node-level-update-status | --no-show-node-level-update-status]
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

`--service-update-name` (string)

The unique ID of the service update

`--replication-group-ids` (list)

The replication group IDs

(string)

Syntax:

```
"string" "string" ...
```

`--cache-cluster-ids` (list)

The cache cluster IDs

(string)

Syntax:

```
"string" "string" ...
```

`--engine` (string)

The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.

`--service-update-status` (list)

The status of the service update

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  available
  cancelled
  expired
```

`--service-update-time-range` (structure)

The range of time specified to search for service updates that are in available status

StartTime -> (timestamp)

The start time of the time range filter

EndTime -> (timestamp)

The end time of the time range filter

Shorthand Syntax:

```
StartTime=timestamp,EndTime=timestamp
```

JSON Syntax:

```
{
  "StartTime": timestamp,
  "EndTime": timestamp
}
```

`--update-action-status` (list)

The status of the update action.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  not-applied
  waiting-to-start
  in-progress
  stopping
  stopped
  complete
  scheduling
  scheduled
  not-applicable
```

`--show-node-level-update-status` | `--no-show-node-level-update-status` (boolean)

Dictates whether to include node level update status in the response

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

**To describe update actions**

The following `describe-update-actions` example returns details of update actions.

```
aws elasticache describe-update-actions
```

Output:

```
{
    "UpdateActions": [
        {
            "ReplicationGroupId": "mycluster",
            "ServiceUpdateName": "elc-20191007-001",
            "ServiceUpdateReleaseDate": "2019-10-09T16:00:00Z",
            "ServiceUpdateSeverity": "important",
            "ServiceUpdateStatus": "available",
            "ServiceUpdateRecommendedApplyByDate": "2019-11-08T15:59:59Z",
            "ServiceUpdateType": "security-update",
            "UpdateActionAvailableDate": "2019-12-05T19:15:19.995Z",
            "UpdateActionStatus": "complete",
            "NodesUpdated": "9/9",
            "UpdateActionStatusModifiedDate": "2019-12-05T19:15:20.461Z",
            "SlaMet": "n/a",
            "Engine": "redis"
        },
        {
            "CacheClusterId": "my-memcached-cluster",
            "ServiceUpdateName": "elc-20191007-001",
            "ServiceUpdateReleaseDate": "2019-10-09T16:00:00Z",
            "ServiceUpdateSeverity": "important",
            "ServiceUpdateStatus": "available",
            "ServiceUpdateRecommendedApplyByDate": "2019-11-08T15:59:59Z",
            "ServiceUpdateType": "security-update",
            "UpdateActionAvailableDate": "2019-12-04T18:26:05.349Z",
            "UpdateActionStatus": "complete",
            "NodesUpdated": "1/1",
            "UpdateActionStatusModifiedDate": "2019-12-04T18:26:05.352Z",
            "SlaMet": "n/a",
            "Engine": "redis"
        },
        {
            "ReplicationGroupId": "my-cluster",
            "ServiceUpdateName": "elc-20191007-001",
            "ServiceUpdateReleaseDate": "2019-10-09T16:00:00Z",
            "ServiceUpdateSeverity": "important",
            "ServiceUpdateStatus": "available",
            "ServiceUpdateRecommendedApplyByDate": "2019-11-08T15:59:59Z",
            "ServiceUpdateType": "security-update",
            "UpdateActionAvailableDate": "2019-11-26T03:36:26.320Z",
            "UpdateActionStatus": "complete",
            "NodesUpdated": "4/4",
            "UpdateActionStatusModifiedDate": "2019-12-04T22:11:12.664Z",
            "SlaMet": "n/a",
            "Engine": "redis"
        },
        {
            "ReplicationGroupId": "my-cluster2",
            "ServiceUpdateName": "elc-20191007-001",
            "ServiceUpdateReleaseDate": "2019-10-09T16:00:00Z",
            "ServiceUpdateSeverity": "important",
            "ServiceUpdateStatus": "available",
            "ServiceUpdateRecommendedApplyByDate": "2019-11-08T15:59:59Z",
            "ServiceUpdateType": "security-update",
            "UpdateActionAvailableDate": "2019-11-26T01:26:01.617Z",
            "UpdateActionStatus": "complete",
            "NodesUpdated": "3/3",
            "UpdateActionStatusModifiedDate": "2019-11-26T01:26:01.753Z",
            "SlaMet": "n/a",
            "Engine": "redis"
        }
    ]
}
```

For more information, see [Self-Service Updates in Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Self-Service-Updates.html) in the *Elasticache User Guide*.

## Output

Marker -> (string)

An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

UpdateActions -> (list)

Returns a list of update actions

(structure)

The status of the service update for a specific replication group

ReplicationGroupId -> (string)

The ID of the replication group

CacheClusterId -> (string)

The ID of the cache cluster

ServiceUpdateName -> (string)

The unique ID of the service update

ServiceUpdateReleaseDate -> (timestamp)

The date the update is first available

ServiceUpdateSeverity -> (string)

The severity of the service update

ServiceUpdateStatus -> (string)

The status of the service update

ServiceUpdateRecommendedApplyByDate -> (timestamp)

The recommended date to apply the service update to ensure compliance. For information on compliance, see [Self-Service Security Updates for Compliance](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-compliance.html#elasticache-compliance-self-service) .

ServiceUpdateType -> (string)

Reflects the nature of the service update

UpdateActionAvailableDate -> (timestamp)

The date that the service update is available to a replication group

UpdateActionStatus -> (string)

The status of the update action

NodesUpdated -> (string)

The progress of the service update on the replication group

UpdateActionStatusModifiedDate -> (timestamp)

The date when the UpdateActionStatus was last modified

SlaMet -> (string)

If yes, all nodes in the replication group have been updated by the recommended apply-by date. If no, at least one node in the replication group have not been updated by the recommended apply-by date. If N/A, the replication group was created after the recommended apply-by date.

NodeGroupUpdateStatus -> (list)

The status of the service update on the node group

(structure)

The status of the service update on the node group

NodeGroupId -> (string)

The ID of the node group

NodeGroupMemberUpdateStatus -> (list)

The status of the service update on the node group member

(structure)

The status of the service update on the node group member

CacheClusterId -> (string)

The cache cluster ID

CacheNodeId -> (string)

The node ID of the cache cluster

NodeUpdateStatus -> (string)

The update status of the node

NodeDeletionDate -> (timestamp)

The deletion date of the node

NodeUpdateStartDate -> (timestamp)

The start date of the update for a node

NodeUpdateEndDate -> (timestamp)

The end date of the update for a node

NodeUpdateInitiatedBy -> (string)

Reflects whether the update was initiated by the customer or automatically applied

NodeUpdateInitiatedDate -> (timestamp)

The date when the update is triggered

NodeUpdateStatusModifiedDate -> (timestamp)

The date when the NodeUpdateStatus was last modified

CacheNodeUpdateStatus -> (list)

The status of the service update on the cache node

(structure)

The status of the service update on the cache node

CacheNodeId -> (string)

The node ID of the cache cluster

NodeUpdateStatus -> (string)

The update status of the node

NodeDeletionDate -> (timestamp)

The deletion date of the node

NodeUpdateStartDate -> (timestamp)

The start date of the update for a node

NodeUpdateEndDate -> (timestamp)

The end date of the update for a node

NodeUpdateInitiatedBy -> (string)

Reflects whether the update was initiated by the customer or automatically applied

NodeUpdateInitiatedDate -> (timestamp)

The date when the update is triggered

NodeUpdateStatusModifiedDate -> (timestamp)

The date when the NodeUpdateStatus was last modified>

EstimatedUpdateTime -> (string)

The estimated length of time for the update to complete

Engine -> (string)

The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.