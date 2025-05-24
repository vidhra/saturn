# associate-virtual-interfaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-virtual-interface.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-virtual-interface.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [directconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html#cli-aws-directconnect) ]

# associate-virtual-interface

## Description

Associates a virtual interface with a specified link aggregation group (LAG) or connection. Connectivity to Amazon Web Services is temporarily interrupted as the virtual interface is being migrated. If the target connection or LAG has an associated virtual interface with a conflicting VLAN number or a conflicting IP address, the operation fails.

Virtual interfaces associated with a hosted connection cannot be associated with a LAG; hosted connections must be migrated along with their virtual interfaces using  AssociateHostedConnection .

To reassociate a virtual interface to a new connection or LAG, the requester must own either the virtual interface itself or the connection to which the virtual interface is currently associated. Additionally, the requester must own the connection or LAG for the association.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/AssociateVirtualInterface)

## Synopsis

```
associate-virtual-interface
--virtual-interface-id <value>
--connection-id <value>
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

`--virtual-interface-id` (string)

The ID of the virtual interface.

`--connection-id` (string)

The ID of the LAG or connection.

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

**To associate a virtual interface with a connection**

The following example associates the specified virtual interface with the specified LAG. Alternatively, to associate the virtual interface with a connection, specify the ID of an AWS Direct Connect connection for `--connection-id`; for example, `dxcon-ffnikghc`.

Command:

```
aws directconnect associate-virtual-interface --connection-id dxlag-ffjhj9lx --virtual-interface-id dxvif-fgputw0j
```

Output:

```
{
  "virtualInterfaceState": "pending",
  "asn": 65000,
  "vlan": 123,
  "customerAddress": "169.254.255.2/30",
  "ownerAccount": "123456789012",
  "connectionId": "dxlag-ffjhj9lx",
  "addressFamily": "ipv4",
  "virtualGatewayId": "vgw-38e90b51",
  "virtualInterfaceId": "dxvif-fgputw0j",
  "authKey": "0x123pK5_VBqv.UQ3kJ4123_",
  "routeFilterPrefixes": [],
  "location": "CSVA1",
  "bgpPeers": [
      {
          "bgpStatus": "down",
          "customerAddress": "169.254.255.2/30",
          "addressFamily": "ipv4",
          "authKey": "0x123pK5_VBqv.UQ3kJ4123_",
          "bgpPeerState": "deleting",
          "amazonAddress": "169.254.255.1/30",
          "asn": 65000
      },
      {
          "bgpStatus": "down",
          "customerAddress": "169.254.255.2/30",
          "addressFamily": "ipv4",
          "authKey": "0x123pK5_VBqv.UQ3kJ4123_",
          "bgpPeerState": "pending",
          "amazonAddress": "169.254.255.1/30",
          "asn": 65000
      }
  ],
  "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fgputw0j\">\n  <vlan>123</vlan>\n  <customer_address>169.254.255.2/30</customer_address>\n  <amazon_address>169.254.255.1/30</amazon_address>\n  <bgp_asn>65000</bgp_asn>\n  <bgp_auth_key>0x123pK5_VBqv.UQ3kJ4123_</bgp_auth_key>\n  <amazon_bgp_asn>7224</amazon_bgp_asn>\n  <connection_type>private</connection_type>\n</logical_connection>\n",
  "amazonAddress": "169.254.255.1/30",
  "virtualInterfaceType": "private",
  "virtualInterfaceName": "VIF1A"
}
```

## Output

ownerAccount -> (string)

The ID of the Amazon Web Services account that owns the virtual interface.

virtualInterfaceId -> (string)

The ID of the virtual interface.

location -> (string)

The location of the connection.

connectionId -> (string)

The ID of the connection.

virtualInterfaceType -> (string)

The type of virtual interface. The possible values are `private` , `public` and `transit` .

virtualInterfaceName -> (string)

The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).

vlan -> (integer)

The ID of the VLAN.

asn -> (integer)

The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

The valid values are 1-2147483647.

amazonSideAsn -> (long)

The autonomous system number (ASN) for the Amazon side of the connection.

authKey -> (string)

The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

amazonAddress -> (string)

The IP address assigned to the Amazon interface.

customerAddress -> (string)

The IP address assigned to the customer interface.

addressFamily -> (string)

The address family for the BGP peer.

virtualInterfaceState -> (string)

The state of the virtual interface. The following are the possible values:

- `confirming` : The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
- `verifying` : This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
- `pending` : A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
- `available` : A virtual interface that is able to forward traffic.
- `down` : A virtual interface that is BGP down.
- `testing` : A virtual interface is in this state immediately after calling  StartBgpFailoverTest and remains in this state during the duration of the test.
- `deleting` : A virtual interface is in this state immediately after calling  DeleteVirtualInterface until it can no longer forward traffic.
- `deleted` : A virtual interface that cannot forward traffic.
- `rejected` : The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the `Confirming` state is deleted by the virtual interface owner, the virtual interface enters the `Rejected` state.
- `unknown` : The state of the virtual interface is not available.

customerRouterConfig -> (string)

The customer router configuration.

mtu -> (integer)

The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500

jumboFrameCapable -> (boolean)

Indicates whether jumbo frames are supported.

virtualGatewayId -> (string)

The ID of the virtual private gateway. Applies only to private virtual interfaces.

directConnectGatewayId -> (string)

The ID of the Direct Connect gateway.

routeFilterPrefixes -> (list)

The routes to be advertised to the Amazon Web Services network in this Region. Applies to public virtual interfaces.

(structure)

Information about a route filter prefix that a customer can advertise through Border Gateway Protocol (BGP) over a public virtual interface.

cidr -> (string)

The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.

bgpPeers -> (list)

The BGP peers configured on this virtual interface.

(structure)

Information about a BGP peer.

bgpPeerId -> (string)

The ID of the BGP peer.

asn -> (integer)

The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

authKey -> (string)

The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.

addressFamily -> (string)

The address family for the BGP peer.

amazonAddress -> (string)

The IP address assigned to the Amazon interface.

customerAddress -> (string)

The IP address assigned to the customer interface.

bgpPeerState -> (string)

The state of the BGP peer. The following are the possible values:

- `verifying` : The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
- `pending` : The BGP peer is created, and remains in this state until it is ready to be established.
- `available` : The BGP peer is ready to be established.
- `deleting` : The BGP peer is being deleted.
- `deleted` : The BGP peer is deleted and cannot be established.

bgpStatus -> (string)

The status of the BGP peer. The following are the possible values:

- `up` : The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
- `down` : The BGP peer is down.
- `unknown` : The BGP peer status is not available.

awsDeviceV2 -> (string)

The Direct Connect endpoint that terminates the BGP peer.

awsLogicalDeviceId -> (string)

The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.

region -> (string)

The Amazon Web Services Region where the virtual interface is located.

awsDeviceV2 -> (string)

The Direct Connect endpoint that terminates the physical connection.

awsLogicalDeviceId -> (string)

The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.

tags -> (list)

The tags associated with the virtual interface.

(structure)

Information about a tag.

key -> (string)

The key.

value -> (string)

The value.

siteLinkEnabled -> (boolean)

Indicates whether SiteLink is enabled.