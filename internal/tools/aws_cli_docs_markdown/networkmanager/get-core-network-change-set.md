# get-core-network-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-core-network-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-core-network-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# get-core-network-change-set

## Description

Returns a change set between the LIVE core network policy and a submitted policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/GetCoreNetworkChangeSet)

`get-core-network-change-set` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CoreNetworkChanges`

## Synopsis

```
get-core-network-change-set
--core-network-id <value>
--policy-version-id <value>
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

`--core-network-id` (string)

The ID of a core network.

`--policy-version-id` (integer)

The ID of the policy version.

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

CoreNetworkChanges -> (list)

Describes a core network changes.

(structure)

Details describing a core network change.

Type -> (string)

The type of change.

Action -> (string)

The action to take for a core network.

Identifier -> (string)

The resource identifier.

PreviousValues -> (structure)

The previous values for a core network.

SegmentName -> (string)

The names of the segments in a core network.

NetworkFunctionGroupName -> (string)

The network function group name if the change event is associated with a network function group.

EdgeLocations -> (list)

The Regions where edges are located in a core network.

(string)

Asn -> (long)

The ASN of a core network.

Cidr -> (string)

The IP addresses used for a core network.

DestinationIdentifier -> (string)

The ID of the destination.

InsideCidrBlocks -> (list)

The inside IP addresses used for core network change values.

(string)

SharedSegments -> (list)

The shared segments for a core network change value.

(string)

ServiceInsertionActions -> (list)

Describes the service insertion action.

(structure)

Describes the action that the service insertion will take for any segments associated with it.

Action -> (string)

The action the service insertion takes for traffic. `send-via` sends east-west traffic between attachments. `send-to` sends north-south traffic to the security appliance, and then from that to either the Internet or to an on-premesis location.

Mode -> (string)

Describes the mode packets take for the `send-via` action. This is not used when the action is `send-to` . `dual-hop` packets traverse attachments in both the source to the destination core network edges. This mode requires that an inspection attachment must be present in all Regions of the service insertion-enabled segments. For `single-hop` , packets traverse a single intermediate inserted attachment. You can use `EdgeOverride` to specify a specific edge to use.

WhenSentTo -> (structure)

The list of destination segments if the service insertion action is `send-via` .

WhenSentToSegmentsList -> (list)

The list of destination segments when the service insertion action is `send-to` .

(string)

Via -> (structure)

The list of network function groups and any edge overrides for the chosen service insertion action. Used for both `send-to` or `send-via` .

NetworkFunctionGroups -> (list)

The list of network function groups associated with the service insertion action.

(structure)

Describes a network function group for service insertion.

Name -> (string)

The name of the network function group.

WithEdgeOverrides -> (list)

Describes any edge overrides. An edge override is a specific edge to be used for traffic.

(structure)

Describes the edge thatâs used for the override.

EdgeSets -> (list)

The list of edge locations.

(list)

(string)

UseEdge -> (string)

The edge that should be used when overriding the current edge order.

NewValues -> (structure)

The new value for a core network

SegmentName -> (string)

The names of the segments in a core network.

NetworkFunctionGroupName -> (string)

The network function group name if the change event is associated with a network function group.

EdgeLocations -> (list)

The Regions where edges are located in a core network.

(string)

Asn -> (long)

The ASN of a core network.

Cidr -> (string)

The IP addresses used for a core network.

DestinationIdentifier -> (string)

The ID of the destination.

InsideCidrBlocks -> (list)

The inside IP addresses used for core network change values.

(string)

SharedSegments -> (list)

The shared segments for a core network change value.

(string)

ServiceInsertionActions -> (list)

Describes the service insertion action.

(structure)

Describes the action that the service insertion will take for any segments associated with it.

Action -> (string)

The action the service insertion takes for traffic. `send-via` sends east-west traffic between attachments. `send-to` sends north-south traffic to the security appliance, and then from that to either the Internet or to an on-premesis location.

Mode -> (string)

Describes the mode packets take for the `send-via` action. This is not used when the action is `send-to` . `dual-hop` packets traverse attachments in both the source to the destination core network edges. This mode requires that an inspection attachment must be present in all Regions of the service insertion-enabled segments. For `single-hop` , packets traverse a single intermediate inserted attachment. You can use `EdgeOverride` to specify a specific edge to use.

WhenSentTo -> (structure)

The list of destination segments if the service insertion action is `send-via` .

WhenSentToSegmentsList -> (list)

The list of destination segments when the service insertion action is `send-to` .

(string)

Via -> (structure)

The list of network function groups and any edge overrides for the chosen service insertion action. Used for both `send-to` or `send-via` .

NetworkFunctionGroups -> (list)

The list of network function groups associated with the service insertion action.

(structure)

Describes a network function group for service insertion.

Name -> (string)

The name of the network function group.

WithEdgeOverrides -> (list)

Describes any edge overrides. An edge override is a specific edge to be used for traffic.

(structure)

Describes the edge thatâs used for the override.

EdgeSets -> (list)

The list of edge locations.

(list)

(string)

UseEdge -> (string)

The edge that should be used when overriding the current edge order.

IdentifierPath -> (string)

Uniquely identifies the path for a change within the changeset. For example, the `IdentifierPath` for a core network segment change might be `"CORE_NETWORK_SEGMENT/us-east-1/devsegment"` .

NextToken -> (string)

The token for the next page of results.