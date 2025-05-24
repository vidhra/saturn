# describe-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dax](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/index.html#cli-aws-dax) ]

# describe-clusters

## Description

Returns information about all provisioned DAX clusters if no cluster identifier is specified, or about a specific DAX cluster if a cluster identifier is supplied.

If the cluster is in the CREATING state, only cluster level information will be displayed until all of the nodes are successfully provisioned.

If the cluster is in the DELETING state, only cluster level information will be displayed.

If nodes are currently being added to the DAX cluster, node endpoint information and creation time for the additional nodes will not be displayed until they are completely provisioned. When the DAX cluster state is *available* , the cluster is ready for use.

If nodes are currently being removed from the DAX cluster, no endpoint information for the removed nodes is displayed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dax-2017-04-19/DescribeClusters)

`describe-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Clusters`

## Synopsis

```
describe-clusters
[--cluster-names <value>]
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

`--cluster-names` (list)

The names of the DAX clusters being described.

(string)

Syntax:

```
"string" "string" ...
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

**To return information about all provisioned DAX clusters**

The following `describe-clusters` example displays details about all provisioned DAX clusters.

```
aws dax describe-clusters
```

Output:

```
{
    "Clusters": [
        {
            "ClusterName": "daxcluster",
            "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster",
            "TotalNodes": 1,
            "ActiveNodes": 1,
            "NodeType": "dax.r4.large",
            "Status": "available",
            "ClusterDiscoveryEndpoint": {
                "Address": "daxcluster.ey3o9d.clustercfg.dax.usw2.cache.amazonaws.com",
                "Port": 8111
            },
            "Nodes": [
                {
                    "NodeId": "daxcluster-a",
                    "Endpoint": {
                        "Address": "daxcluster-a.ey3o9d.0001.dax.usw2.cache.amazonaws.com",
                        "Port": 8111
                    },
                    "NodeCreateTime": 1576625059.509,
                    "AvailabilityZone": "us-west-2c",
                    "NodeStatus": "available",
                    "ParameterGroupStatus": "in-sync"
                }
            ],
            "PreferredMaintenanceWindow": "thu:13:00-thu:14:00",
            "SubnetGroup": "default",
            "SecurityGroups": [
                {
                    "SecurityGroupIdentifier": "sg-1af6e36e",
                    "Status": "active"
                }
            ],
            "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess",
            "ParameterGroup": {
                "ParameterGroupName": "default.dax1.0",
                "ParameterApplyStatus": "in-sync",
                "NodeIdsToReboot": []
            },
            "SSEDescription": {
                "Status": "ENABLED"
            }
        }
    ]
}
```

For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html) in the *Amazon DynamoDB Developer Guide*.

## Output

NextToken -> (string)

Provides an identifier to allow retrieval of paginated results.

Clusters -> (list)

The descriptions of your DAX clusters, in response to a *DescribeClusters* request.

(structure)

Contains all of the attributes of a specific DAX cluster.

ClusterName -> (string)

The name of the DAX cluster.

Description -> (string)

The description of the cluster.

ClusterArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the cluster.

TotalNodes -> (integer)

The total number of nodes in the cluster.

ActiveNodes -> (integer)

The number of nodes in the cluster that are active (i.e., capable of serving requests).

NodeType -> (string)

The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)

Status -> (string)

The current status of the cluster.

ClusterDiscoveryEndpoint -> (structure)

The endpoint for this DAX cluster, consisting of a DNS name, a port number, and a URL. Applications should use the URL to configure the DAX client to find their cluster.

Address -> (string)

The DNS hostname of the endpoint.

Port -> (integer)

The port number that applications should use to connect to the endpoint.

URL -> (string)

The URL that applications should use to connect to the endpoint. The default ports are 8111 for the âdaxâ protocol and 9111 for the âdaxsâ protocol.

NodeIdsToRemove -> (list)

A list of nodes to be removed from the cluster.

(string)

Nodes -> (list)

A list of nodes that are currently in the cluster.

(structure)

Represents an individual node within a DAX cluster.

NodeId -> (string)

A system-generated identifier for the node.

Endpoint -> (structure)

The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.

Address -> (string)

The DNS hostname of the endpoint.

Port -> (integer)

The port number that applications should use to connect to the endpoint.

URL -> (string)

The URL that applications should use to connect to the endpoint. The default ports are 8111 for the âdaxâ protocol and 9111 for the âdaxsâ protocol.

NodeCreateTime -> (timestamp)

The date and time (in UNIX epoch format) when the node was launched.

AvailabilityZone -> (string)

The Availability Zone (AZ) in which the node has been deployed.

NodeStatus -> (string)

The current status of the node. For example: `available` .

ParameterGroupStatus -> (string)

The status of the parameter group associated with this node. For example, `in-sync` .

PreferredMaintenanceWindow -> (string)

A range of time when maintenance of DAX cluster software will be performed. For example: `sun:01:00-sun:09:00` . Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.

NotificationConfiguration -> (structure)

Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

TopicArn -> (string)

The Amazon Resource Name (ARN) that identifies the topic.

TopicStatus -> (string)

The current state of the topic. A value of âactiveâ means that notifications will be sent to the topic. A value of âinactiveâ means that notifications will not be sent to the topic.

SubnetGroup -> (string)

The subnet group where the DAX cluster is running.

SecurityGroups -> (list)

A list of security groups, and the status of each, for the nodes in the cluster.

(structure)

An individual VPC security group and its status.

SecurityGroupIdentifier -> (string)

The unique ID for this security group.

Status -> (string)

The status of this security group.

IamRoleArn -> (string)

A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the roleâs permissions to access DynamoDB on your behalf.

ParameterGroup -> (structure)

The parameter group being used by nodes in the cluster.

ParameterGroupName -> (string)

The name of the parameter group.

ParameterApplyStatus -> (string)

The status of parameter updates.

NodeIdsToReboot -> (list)

The node IDs of one or more nodes to be rebooted.

(string)

SSEDescription -> (structure)

The description of the server-side encryption status on the specified DAX cluster.

Status -> (string)

The current state of server-side encryption:

- `ENABLING` - Server-side encryption is being enabled.
- `ENABLED` - Server-side encryption is enabled.
- `DISABLING` - Server-side encryption is being disabled.
- `DISABLED` - Server-side encryption is disabled.

ClusterEndpointEncryptionType -> (string)

The type of encryption supported by the clusterâs endpoint. Values are:

- `NONE` for no encryption  `TLS` for Transport Layer Security