# describe-direct-connect-gateway-association-proposalsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [directconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html#cli-aws-directconnect) ]

# describe-direct-connect-gateway-association-proposals

## Description

Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)

## Synopsis

```
describe-direct-connect-gateway-association-proposals
[--direct-connect-gateway-id <value>]
[--proposal-id <value>]
[--associated-gateway-id <value>]
[--max-results <value>]
[--next-token <value>]
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

`--direct-connect-gateway-id` (string)

The ID of the Direct Connect gateway.

`--proposal-id` (string)

The ID of the proposal.

`--associated-gateway-id` (string)

The ID of the associated gateway.

`--max-results` (integer)

The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.

If `MaxResults` is given a value larger than 100, only 100 results are returned.

`--next-token` (string)

The token for the next page of results.

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

**To describe your Direct Connect gateway association proposals**

The following `describe-direct-connect-gateway-association-proposals` example displays details about your Direct Connect gateway association proposals.

```
aws directconnect describe-direct-connect-gateway-association-proposals
```

Output:

```
{
    "directConnectGatewayAssociationProposals": [
        {
            "proposalId": "c2ede9b4-bbc6-4d33-923c-bc4feEXAMPLE",
            "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE",
            "directConnectGatewayOwnerAccount": "111122223333",
            "proposalState": "requested",
            "associatedGateway": {
                "id": "tgw-02f776b1a7EXAMPLE",
                "type": "transitGateway",
                "ownerAccount": "111122223333",
                "region": "us-east-1"
            },
            "existingAllowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "192.168.2.0/30"
                },
                {
                    "cidr": "192.168.1.0/30"
                }
            ],
            "requestedAllowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "192.168.1.0/30"
                }
            ]
        },
        {
            "proposalId": "cb7f41cb-8128-43a5-93b1-dcaedEXAMPLE",
            "directConnectGatewayId": "11560968-4ac1-4fd3-bcb2-00599EXAMPLE",
            "directConnectGatewayOwnerAccount": "111122223333",
            "proposalState": "accepted",
            "associatedGateway": {
                "id": "tgw-045776b1a7EXAMPLE",
                "type": "transitGateway",
                "ownerAccount": "111122223333",
                "region": "us-east-1"
            },
            "existingAllowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "192.168.4.0/30"
                },
                {
                    "cidr": "192.168.5.0/30"
                }
            ],
            "requestedAllowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "192.168.5.0/30"
                }
            ]
        }
    ]
}
```

For more information, see [Associating and Disassociating Transit Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html#associate-tgw-with-direct-connect-gateway) in the *AWS Direct Connect User Guide*.

## Output

directConnectGatewayAssociationProposals -> (list)

Describes the Direct Connect gateway association proposals.

(structure)

Information about the proposal request to attach a virtual private gateway to a Direct Connect gateway.

proposalId -> (string)

The ID of the association proposal.

directConnectGatewayId -> (string)

The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount -> (string)

The ID of the Amazon Web Services account that owns the Direct Connect gateway.

proposalState -> (string)

The state of the proposal. The following are possible values:

- `accepted` : The proposal has been accepted. The Direct Connect gateway association is available to use in this state.
- `deleted` : The proposal has been deleted by the owner that made the proposal. The Direct Connect gateway association cannot be used in this state.
- `requested` : The proposal has been requested. The Direct Connect gateway association cannot be used in this state.

associatedGateway -> (structure)

Information about the associated gateway.

id -> (string)

The ID of the associated gateway.

type -> (string)

The type of associated gateway.

ownerAccount -> (string)

The ID of the Amazon Web Services account that owns the associated virtual private gateway or transit gateway.

region -> (string)

The Region where the associated gateway is located.

existingAllowedPrefixesToDirectConnectGateway -> (list)

The existing Amazon VPC prefixes advertised to the Direct Connect gateway.

(structure)

Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr -> (string)

The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.

requestedAllowedPrefixesToDirectConnectGateway -> (list)

The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(structure)

Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr -> (string)

The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.

nextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.