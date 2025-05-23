# get-query-results-monitor-top-contributorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-monitor-top-contributors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/get-query-results-monitor-top-contributors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkflowmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkflowmonitor/index.html#cli-aws-networkflowmonitor) ]

# get-query-results-monitor-top-contributors

## Description

Return the data for a query with the Network Flow Monitor query interface. You specify the query that you want to return results for by providing a query ID and a monitor name. This query returns the top contributors for a specific monitor.

Create a query ID for this call by calling the corresponding API call to start the query, `StartQueryMonitorTopContributors` . Use the scope ID that was returned for your account by `CreateScope` .

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type, related to a scope (for workload insights) or a monitor.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkflowmonitor-2023-04-19/GetQueryResultsMonitorTopContributors)

`get-query-results-monitor-top-contributors` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `topContributors`

## Synopsis

```
get-query-results-monitor-top-contributors
--monitor-name <value>
--query-id <value>
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

`--monitor-name` (string)

The name of the monitor.

`--query-id` (string)

The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.

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

unit -> (string)

The units for a metric returned by the query.

topContributors -> (list)

The top contributor network flows overall for a specific metric type, for example, the number of retransmissions.

(structure)

A set of information for a top contributor network flow in a monitor. In a monitor, Network Flow Monitor returns information about the network flows for top contributors for each metric. Top contributors are network flows with the top values for each metric type.

localIp -> (string)

The IP address of the local resource for a top contributor network flow.

snatIp -> (string)

The secure network address translation (SNAT) IP address for a top contributor network flow.

localInstanceId -> (string)

The instance identifier for the local resource for a top contributor network flow.

localVpcId -> (string)

The VPC ID for a top contributor network flow for the local resource.

localRegion -> (string)

The Amazon Web Services Region for the local resource for a top contributor network flow.

localAz -> (string)

The Availability Zone for the local resource for a top contributor network flow.

localSubnetId -> (string)

The subnet ID for the local resource for a top contributor network flow.

targetPort -> (integer)

The target port.

destinationCategory -> (string)

The destination category for a top contributors row. Destination categories can be one of the following:

- `INTRA_AZ` : Top contributor network flows within a single Availability Zone
- `INTER_AZ` : Top contributor network flows between Availability Zones
- `INTER_VPC` : Top contributor network flows between VPCs
- `AWS_SERVICES` : Top contributor network flows to or from Amazon Web Services services
- `UNCLASSIFIED` : Top contributor network flows that do not have a bucket classification

remoteVpcId -> (string)

The VPC ID for a top contributor network flow for the remote resource.

remoteRegion -> (string)

The Amazon Web Services Region for the remote resource for a top contributor network flow.

remoteAz -> (string)

The Availability Zone for the remote resource for a top contributor network flow.

remoteSubnetId -> (string)

The subnet ID for the remote resource for a top contributor network flow.

remoteInstanceId -> (string)

The instance identifier for the remote resource for a top contributor network flow.

remoteIp -> (string)

The IP address of the remote resource for a top contributor network flow.

dnatIp -> (string)

The destination network address translation (DNAT) IP address for a top contributor network flow.

value -> (long)

The value of the metric for a top contributor network flow.

traversedConstructs -> (list)

The constructs traversed by a network flow.

(structure)

A section of the network that a network flow has traveled through.

componentId -> (string)

The identifier for the traversed component.

componentType -> (string)

The type of component that was traversed.

componentArn -> (string)

The Amazon Resource Name (ARN) of a tranversed component.

serviceName -> (string)

The service name for the traversed component.

kubernetesMetadata -> (structure)

Meta data about Kubernetes resources.

localServiceName -> (string)

The service name for a local resource.

localPodName -> (string)

The name of the pod for a local resource.

localPodNamespace -> (string)

The namespace of the pod for a local resource.

remoteServiceName -> (string)

The service name for a remote resource.

remotePodName -> (string)

The name of the pod for a remote resource.

remotePodNamespace -> (string)

The namespace of the pod for a remote resource.

localInstanceArn -> (string)

The Amazon Resource Name (ARN) of a local resource.

localSubnetArn -> (string)

The Amazon Resource Name (ARN) of a local subnet.

localVpcArn -> (string)

The Amazon Resource Name (ARN) of a local VPC.

remoteInstanceArn -> (string)

The Amazon Resource Name (ARN) of a remote resource.

remoteSubnetArn -> (string)

The Amazon Resource Name (ARN) of a remote subnet.

remoteVpcArn -> (string)

The Amazon Resource Name (ARN) of a remote VPC.

nextToken -> (string)

The token for the next set of results. You receive this token from a previous call.