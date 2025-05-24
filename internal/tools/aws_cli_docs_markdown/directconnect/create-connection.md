# create-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [directconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/index.html#cli-aws-directconnect) ]

# create-connection

## Description

Creates a connection between a customer network and a specific Direct Connect location.

A connection links your internal network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end of the cable is connected to your router, the other to an Direct Connect router.

To find the locations for your Region, use  DescribeLocations .

You can automatically add the new connection to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new connection is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no connection is created.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directconnect-2012-10-25/CreateConnection)

## Synopsis

```
create-connection
--location <value>
--bandwidth <value>
--connection-name <value>
[--lag-id <value>]
[--tags <value>]
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

`--location` (string)

The location of the connection.

`--bandwidth` (string)

The bandwidth of the connection.

`--connection-name` (string)

The name of the connection.

`--lag-id` (string)

The ID of the LAG.

`--tags` (list)

The tags to associate with the lag.

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

The name of the service provider associated with the requested connection.

`--request-mac-sec` | `--no-request-mac-sec` (boolean)

Indicates whether you want the connection to support MAC Security (MACsec).

MAC Security (MACsec) is only available on dedicated connections. For information about MAC Security (MACsec) prerequisties, see [MACsec prerequisties](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites) in the *Direct Connect User Guide* .

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

**To create a connection from your network to an AWS Direct Connect location**

The following `create-connection` command creates a connection from your network to an AWS Direct Connect location:

```
aws directconnect create-connection --location TIVIT --bandwidth 1Gbps --connection-name "Connection to AWS"
```

Output:

```
{
    "ownerAccount": "123456789012",
    "connectionId": "dxcon-fg31dyv6",
    "connectionState": "requested",
    "bandwidth": "1Gbps",
    "location": "TIVIT",
    "connectionName": "Connection to AWS",
    "region": "sa-east-1"
}
```

## Output

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