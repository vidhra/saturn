# accept-direct-connect-gateway-association-proposalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [directconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html#cli-aws-directconnect) ]

# accept-direct-connect-gateway-association-proposal

## Description

Accepts a proposal request to attach a virtual private gateway or transit gateway to a Direct Connect gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AcceptDirectConnectGatewayAssociationProposal)

## Synopsis

```
accept-direct-connect-gateway-association-proposal
--direct-connect-gateway-id <value>
--proposal-id <value>
--associated-gateway-owner-account <value>
[--override-allowed-prefixes-to-direct-connect-gateway <value>]
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

The ID of the request proposal.

`--associated-gateway-owner-account` (string)

The ID of the Amazon Web Services account that owns the virtual private gateway or transit gateway.

`--override-allowed-prefixes-to-direct-connect-gateway` (list)

Overrides the Amazon VPC prefixes advertised to the Direct Connect gateway.

For information about how to set the prefixes, see [Allowed Prefixes](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes) in the *Direct Connect User Guide* .

(structure)

Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr -> (string)

The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.

Shorthand Syntax:

```
cidr=string ...
```

JSON Syntax:

```
[
  {
    "cidr": "string"
  }
  ...
]
```

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

**To accept a gateway association proposal**

The following `accept-direct-connect-gateway-association-proposal` accepts the specified proposal.

```
aws directconnect  accept-direct-connect-gateway-association-proposal \
    --direct-connect-gateway-id 11460968-4ac1-4fd3-bdb2-00599EXAMPLE \
    --proposal-id cb7f41cb-8128-43a5-93b1-dcaedEXAMPLE \
    --associated-gateway-owner-account 111122223333

{
    "directConnectGatewayAssociation": {
        "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE",
        "directConnectGatewayOwnerAccount": "111122223333",
        "associationState": "associating",
        "associatedGateway": {
            "id": "tgw-02f776b1a7EXAMPLE",
            "type": "transitGateway",
            "ownerAccount": "111122223333",
            "region": "us-east-1"
        },
        "associationId": "6441f8bf-5917-4279-ade1-9708bEXAMPLE",
        "allowedPrefixesToDirectConnectGateway": [
            {
                "cidr": "192.168.1.0/30"
            }
        ]
    }
}
```

For more information, see [Accepting or Rejecting a Transit Gateway Association Proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-tgw.html#multi-account-tgw-accept-reject-proposal) in the *AWS Direct Connect User Guide*.

## Output

directConnectGatewayAssociation -> (structure)

Information about an association between a Direct Connect gateway and a virtual gateway or transit gateway.

directConnectGatewayId -> (string)

The ID of the Direct Connect gateway.

directConnectGatewayOwnerAccount -> (string)

The ID of the Amazon Web Services account that owns the associated gateway.

associationState -> (string)

The state of the association. The following are the possible values:

- `associating` : The initial state after calling  CreateDirectConnectGatewayAssociation .
- `associated` : The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.
- `disassociating` : The initial state after calling  DeleteDirectConnectGatewayAssociation .
- `disassociated` : The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.
- `updating` : The CIDR blocks for the virtual private gateway or transit gateway are currently being updated. This could be new CIDR blocks added or current CIDR blocks removed.

stateChangeError -> (string)

The error message if the state of an object failed to advance.

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

associationId -> (string)

The ID of the Direct Connect gateway association.

allowedPrefixesToDirectConnectGateway -> (list)

The Amazon VPC prefixes to advertise to the Direct Connect gateway.

(structure)

Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr -> (string)

The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.

associatedCoreNetwork -> (structure)

The ID of the Cloud WAN core network associated with the Direct Connect gateway attachment.

id -> (string)

The ID of the Cloud WAN core network that the Direct Connect gateway is associated to.

ownerAccount -> (string)

The account owner of the Cloud WAN core network.

attachmentId -> (string)

the ID of the Direct Connect gateway attachment.

virtualGatewayId -> (string)

The ID of the virtual private gateway. Applies only to private virtual interfaces.

virtualGatewayRegion -> (string)

The Amazon Web Services Region where the virtual private gateway is located.

virtualGatewayOwnerAccount -> (string)

The ID of the Amazon Web Services account that owns the virtual private gateway.