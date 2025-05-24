# list-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# list-clusters

## Description

Provides the status of all clusters visible to this Amazon Web Services account. Allows you to filter the list of clusters based on certain criteria; for example, filtering by cluster creation date and time or by status. This call returns a maximum of 50 clusters in unsorted order per call, but returns a marker to track the paging of the cluster list across multiple ListClusters calls.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListClusters)

`list-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Clusters`

## Synopsis

```
list-clusters
[--created-after <value>]
[--created-before <value>]
[--cluster-states <value>]
[--active | --terminated | --failed]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--created-after` (timestamp)

List only those clusters created after the date and time specified in the format yyyy-mm-ddThh:mm:ss. For example, `--created-after 2017-07-04T00:01:30.`

`--created-before` (timestamp)

List only those clusters created before the date and time specified in the format yyyy-mm-ddThh:mm:ss. For example, `--created-before 2017-07-04T00:01:30.`

`--cluster-states` (string)

Specifies that only clusters in the states specified are listed. Alternatively, you can use the shorthand form for single states or a group of states.

Takes the following state values:

- `STARTING`
- `BOOTSTRAPPING`
- `RUNNING`
- `WAITING`
- `TERMINATING`
- `TERMINATED`
- `TERMINATED_WITH_ERRORS`

`--active` | `--terminated` | `--failed` (boolean)

Shortcut options for âcluster-states. The following shortcut options can be specified:

- `--active` - list only clusters that are `STARTING` ,``BOOTSTRAPPING`` , `RUNNING` , `WAITING` , or `TERMINATING` .
- `--terminated` - list only clusters that are `TERMINATED` .
- `--failed` - list only clusters that are `TERMINATED_WITH_ERRORS` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

The following command lists all active EMR clusters in the current region:

```
aws emr list-clusters --active
```

Output:

```
{
    "Clusters": [
        {
            "Status": {
                "Timeline": {
                    "ReadyDateTime": 1433200405.353,
                    "CreationDateTime": 1433199926.596
                },
                "State": "WAITING",
                "StateChangeReason": {
                    "Message": "Waiting after step completed"
                }
            },
            "NormalizedInstanceHours": 6,
            "Id": "j-3SD91U2E1L2QX",
            "Name": "my-cluster"
        }
    ]
}
```

## Output

Clusters -> (list)

The list of clusters for the account based on the given filters.

(structure)

The summary description of the cluster.

Id -> (string)

The unique identifier for the cluster.

Name -> (string)

The name of the cluster.

Status -> (structure)

The details about the current status of the cluster.

State -> (string)

The current state of the cluster.

StateChangeReason -> (structure)

The reason for the cluster status change.

Code -> (string)

The programmatic code for the state change reason.

Message -> (string)

The descriptive message for the state change reason.

Timeline -> (structure)

A timeline that represents the status of a cluster over the lifetime of the cluster.

CreationDateTime -> (timestamp)

The creation date and time of the cluster.

ReadyDateTime -> (timestamp)

The date and time when the cluster was ready to run steps.

EndDateTime -> (timestamp)

The date and time when the cluster was terminated.

ErrorDetails -> (list)

A list of tuples that provides information about the errors that caused a cluster to terminate. This structure can contain up to 10 different `ErrorDetail` tuples.

(structure)

A tuple that provides information about an error that caused a cluster to terminate.

ErrorCode -> (string)

The name or code associated with the error.

ErrorData -> (list)

A list of key value pairs that provides contextual information about why an error occured.

(map)

key -> (string)

value -> (string)

ErrorMessage -> (string)

A message that describes the error.

NormalizedInstanceHours -> (integer)

An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.

ClusterArn -> (string)

The Amazon Resource Name of the cluster.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost where the cluster is launched.

Marker -> (string)

The pagination token that indicates the next set of results to retrieve.