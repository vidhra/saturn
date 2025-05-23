# create-lagÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [directconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html#cli-aws-directconnect) ]

# create-lag

## Description

Creates a link aggregation group (LAG) with the specified number of bundled physical dedicated connections between the customer network and a specific Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.

All connections in a LAG must use the same bandwidth (either 1Gbps, 10Gbps, 100Gbps, or 400Gbps) and must terminate at the same Direct Connect endpoint.

You can have up to 10 dedicated connections per location. Regardless of this limit, if you request more connections for the LAG than Direct Connect can allocate on a single endpoint, no LAG is created..

You can specify an existing physical dedicated connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical dedicated connection, and re-establishes them as a member of the LAG. The LAG will be created on the same Direct Connect endpoint to which the dedicated connection terminates. Any virtual interfaces associated with the dedicated connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.

If the Amazon Web Services account used to create a LAG is a registered Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateLag)

## Synopsis

```
create-lag
--number-of-connections <value>
--location <value>
--connections-bandwidth <value>
--lag-name <value>
[--connection-id <value>]
[--tags <value>]
[--child-connection-tags <value>]
[--provider-name <value>]
[--request-mac-sec | --no-request-mac-sec]
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

`--number-of-connections` (integer)

The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.

`--location` (string)

The location for the LAG.

`--connections-bandwidth` (string)

The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps.

`--lag-name` (string)

The name of the LAG.

`--connection-id` (string)

The ID of an existing dedicated connection to migrate to the LAG.

`--tags` (list)

The tags to associate with the LAG.

(structure)

Information about a tag.

key -> (string)

The key.

value -> (string)

The value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--child-connection-tags` (list)

The tags to associate with the automtically created LAGs.

(structure)

Information about a tag.

key -> (string)

The key.

value -> (string)

The value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--provider-name` (string)

The name of the service provider associated with the LAG.

`--request-mac-sec` | `--no-request-mac-sec` (boolean)

Indicates whether the connection will support MAC Security (MACsec).

### Note

All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see [MACsec prerequisties](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites) in the *Direct Connect User Guide* .

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

**To create a LAG with new connections**

The following example creates a LAG and requests two new AWS Direct Connect connections for the LAG with a bandwidth of 1 Gbps.

Command:

```
aws directconnect create-lag --location CSVA1 --number-of-connections 2 --connections-bandwidth 1Gbps --lag-name 1GBLag
```

Output:

```
{
  "awsDevice": "CSVA1-23u8tlpaz8iks",
  "numberOfConnections": 2,
  "lagState": "pending",
  "ownerAccount": "123456789012",
  "lagName": "1GBLag",
  "connections": [
      {
          "ownerAccount": "123456789012",
          "connectionId": "dxcon-ffqr6x5q",
          "lagId": "dxlag-ffjhj9lx",
          "connectionState": "requested",
          "bandwidth": "1Gbps",
          "location": "CSVA1",
          "connectionName": "Requested Connection 1 for Lag dxlag-ffjhj9lx",
          "region": "us-east-1"
      },
      {
          "ownerAccount": "123456789012",
          "connectionId": "dxcon-fflqyj95",
          "lagId": "dxlag-ffjhj9lx",
          "connectionState": "requested",
          "bandwidth": "1Gbps",
          "location": "CSVA1",
          "connectionName": "Requested Connection 2 for Lag dxlag-ffjhj9lx",
          "region": "us-east-1"
      }
  ],
  "lagId": "dxlag-ffjhj9lx",
  "minimumLinks": 0,
  "connectionsBandwidth": "1Gbps",
  "region": "us-east-1",
  "location": "CSVA1"
}
```

**To create a LAG using an existing connection**

The following example creates a LAG from an existing connection in your account, and requests a second new connection for the LAG with the same bandwidth and location as the existing connection.

Command:

```
aws directconnect create-lag --location EqDC2 --number-of-connections 2 --connections-bandwidth 1Gbps --lag-name 2ConnLAG --connection-id dxcon-fgk145dr
```

Output:

```
{
  "awsDevice": "EqDC2-4h6ce2r1bes6",
  "numberOfConnections": 2,
  "lagState": "pending",
  "ownerAccount": "123456789012",
  "lagName": "2ConnLAG",
  "connections": [
      {
          "ownerAccount": "123456789012",
          "connectionId": "dxcon-fh6ljcvo",
          "lagId": "dxlag-fhccu14t",
          "connectionState": "requested",
          "bandwidth": "1Gbps",
          "location": "EqDC2",
          "connectionName": "Requested Connection 1 for Lag dxlag-fhccu14t",
          "region": "us-east-1"
      },
      {
          "ownerAccount": "123456789012",
          "connectionId": "dxcon-fgk145dr",
          "lagId": "dxlag-fhccu14t",
          "connectionState": "down",
          "bandwidth": "1Gbps",
          "location": "EqDC2",
          "connectionName": "VAConn1",
          "region": "us-east-1"
      }
  ],
  "lagId": "dxlag-fhccu14t",
  "minimumLinks": 0,
  "connectionsBandwidth": "1Gbps",
  "region": "us-east-1",
  "location": "EqDC2"
}
```

## Output

connectionsBandwidth -> (string)

The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps..

numberOfConnections -> (integer)

The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1 Gbps or 10 Gbps, or two when the port speed is 100 Gbps or 400 Gbps.

lagId -> (string)

The ID of the LAG.

ownerAccount -> (string)

The ID of the Amazon Web Services account that owns the LAG.

lagName -> (string)

The name of the LAG.

lagState -> (string)

The state of the LAG. The following are the possible values:

- `requested` : The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
- `pending` : The LAG has been approved and is being initialized.
- `available` : The network link is established and the LAG is ready for use.
- `down` : The network link is down.
- `deleting` : The LAG is being deleted.
- `deleted` : The LAG is deleted.
- `unknown` : The state of the LAG is not available.

location -> (string)

The location of the LAG.

region -> (string)

The Amazon Web Services Region where the connection is located.

minimumLinks -> (integer)

The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.

awsDevice -> (string)

The Direct Connect endpoint that hosts the LAG.

awsDeviceV2 -> (string)

The Direct Connect endpoint that hosts the LAG.

awsLogicalDeviceId -> (string)

The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.

connections -> (list)

The connections bundled by the LAG.

(structure)

Information about an Direct Connect connection.

ownerAccount -> (string)

The ID of the Amazon Web Services account that owns the connection.

connectionId -> (string)

The ID of the connection.

connectionName -> (string)

The name of the connection.

connectionState -> (string)

The state of the connection. The following are the possible values:

- `ordering` : The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
- `requested` : The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
- `pending` : The connection has been approved and is being initialized.
- `available` : The network link is up and the connection is ready for use.
- `down` : The network link is down.
- `deleting` : The connection is being deleted.
- `deleted` : The connection has been deleted.
- `rejected` : A hosted connection in the `ordering` state enters the `rejected` state if it is deleted by the customer.
- `unknown` : The state of the connection is not available.

region -> (string)

The Amazon Web Services Region where the connection is located.

location -> (string)

The location of the connection.

bandwidth -> (string)

The bandwidth of the connection.

vlan -> (integer)

The ID of the VLAN.

partnerName -> (string)

The name of the Direct Connect service provider associated with the connection.

loaIssueTime -> (timestamp)

The time of the most recent call to  DescribeLoa for this connection.

lagId -> (string)

The ID of the LAG.

awsDevice -> (string)

The Direct Connect endpoint on which the physical connection terminates.

jumboFrameCapable -> (boolean)

Indicates whether jumbo frames are supported.

awsDeviceV2 -> (string)

The Direct Connect endpoint that terminates the physical connection.

awsLogicalDeviceId -> (string)

The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.

hasLogicalRedundancy -> (string)

Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags -> (list)

The tags associated with the connection.

(structure)

Information about a tag.

key -> (string)

The key.

value -> (string)

The value.

providerName -> (string)

The name of the service provider associated with the connection.

macSecCapable -> (boolean)

Indicates whether the connection supports MAC Security (MACsec).

portEncryptionStatus -> (string)

The MAC Security (MACsec) port link status of the connection.

The valid values are `Encryption Up` , which means that there is an active Connection Key Name, or `Encryption Down` .

encryptionMode -> (string)

The MAC Security (MACsec) connection encryption mode.

The valid values are `no_encrypt` , `should_encrypt` , and `must_encrypt` .

macSecKeys -> (list)

The MAC Security (MACsec) security keys associated with the connection.

(structure)

Information about the MAC Security (MACsec) secret key.

secretARN -> (string)

The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.

ckn -> (string)

The Connection Key Name (CKN) for the MAC Security secret key.

state -> (string)

The state of the MAC Security (MACsec) secret key.

The possible values are:

- `associating` : The MAC Security (MACsec) secret key is being validated and not yet associated with the connection or LAG.
- `associated` : The MAC Security (MACsec) secret key is validated and associated with the connection or LAG.
- `disassociating` : The MAC Security (MACsec) secret key is being disassociated from the connection or LAG
- `disassociated` : The MAC Security (MACsec) secret key is no longer associated with the connection or LAG.

startOn -> (string)

The date that the MAC Security (MACsec) secret key takes effect. The value is displayed in UTC format.

allowsHostedConnections -> (boolean)

Indicates whether the LAG can host other connections.

jumboFrameCapable -> (boolean)

Indicates whether jumbo frames are supported.

hasLogicalRedundancy -> (string)

Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).

tags -> (list)

The tags associated with the LAG.

(structure)

Information about a tag.

key -> (string)

The key.

value -> (string)

The value.

providerName -> (string)

The name of the service provider associated with the LAG.

macSecCapable -> (boolean)

Indicates whether the LAG supports MAC Security (MACsec).

encryptionMode -> (string)

The LAG MAC Security (MACsec) encryption mode.

The valid values are `no_encrypt` , `should_encrypt` , and `must_encrypt` .

macSecKeys -> (list)

The MAC Security (MACsec) security keys associated with the LAG.

(structure)

Information about the MAC Security (MACsec) secret key.

secretARN -> (string)

The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.

ckn -> (string)

The Connection Key Name (CKN) for the MAC Security secret key.

state -> (string)

The state of the MAC Security (MACsec) secret key.

The possible values are:

- `associating` : The MAC Security (MACsec) secret key is being validated and not yet associated with the connection or LAG.
- `associated` : The MAC Security (MACsec) secret key is validated and associated with the connection or LAG.
- `disassociating` : The MAC Security (MACsec) secret key is being disassociated from the connection or LAG
- `disassociated` : The MAC Security (MACsec) secret key is no longer associated with the connection or LAG.

startOn -> (string)

The date that the MAC Security (MACsec) secret key takes effect. The value is displayed in UTC format.