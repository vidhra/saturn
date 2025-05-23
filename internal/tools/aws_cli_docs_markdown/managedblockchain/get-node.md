# get-nodeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/get-node.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [managedblockchain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/managedblockchain/index.html#cli-aws-managedblockchain) ]

# get-node

## Description

Returns detailed information about a node.

Applies to Hyperledger Fabric and Ethereum.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/managedblockchain-2018-09-24/GetNode)

## Synopsis

```
get-node
--network-id <value>
[--member-id <value>]
--node-id <value>
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

`--network-id` (string)

The unique identifier of the network that the node is on.

`--member-id` (string)

The unique identifier of the member that owns the node.

Applies only to Hyperledger Fabric and is required for Hyperledger Fabric.

`--node-id` (string)

The unique identifier of the node.

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

## Output

Node -> (structure)

Properties of the node configuration.

NetworkId -> (string)

The unique identifier of the network that the node is on.

MemberId -> (string)

The unique identifier of the member to which the node belongs.

Applies only to Hyperledger Fabric.

Id -> (string)

The unique identifier of the node.

InstanceType -> (string)

The instance type of the node.

AvailabilityZone -> (string)

The Availability Zone in which the node exists. Required for Ethereum nodes.

FrameworkAttributes -> (structure)

Attributes of the blockchain framework being used.

Fabric -> (structure)

Attributes of Hyperledger Fabric for a peer node on a Managed Blockchain network that uses Hyperledger Fabric.

PeerEndpoint -> (string)

The endpoint that identifies the peer node for all services except peer channel-based event services.

PeerEventEndpoint -> (string)

The endpoint that identifies the peer node for peer channel-based event services.

Ethereum -> (structure)

Attributes of Ethereum for a node on a Managed Blockchain network that uses Ethereum.

HttpEndpoint -> (string)

The endpoint on which the Ethereum node listens to run Ethereum API methods over HTTP connections from a client. Use this endpoint in client code for smart contracts when using an HTTP connection. Connections to this endpoint are authenticated using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

WebSocketEndpoint -> (string)

The endpoint on which the Ethereum node listens to run Ethereum JSON-RPC methods over WebSocket connections from a client. Use this endpoint in client code for smart contracts when using a WebSocket connection. Connections to this endpoint are authenticated using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

LogPublishingConfiguration -> (structure)

Configuration properties for logging events associated with a peer node on a Hyperledger Fabric network on Managed Blockchain.

Fabric -> (structure)

Configuration properties for logging events associated with a node that is owned by a member of a Managed Blockchain network using the Hyperledger Fabric framework.

ChaincodeLogs -> (structure)

Configuration properties for logging events associated with chaincode execution on a peer node. Chaincode logs contain the results of instantiating, invoking, and querying the chaincode. A peer can run multiple instances of chaincode. When enabled, a log stream is created for all chaincodes, with an individual log stream for each chaincode.

Cloudwatch -> (structure)

Parameters for publishing logs to Amazon CloudWatch Logs.

Enabled -> (boolean)

Indicates whether logging is enabled.

PeerLogs -> (structure)

Configuration properties for a peer node log. Peer node logs contain messages generated when your client submits transaction proposals to peer nodes, requests to join channels, enrolls an admin peer, and lists the chaincode instances on a peer node.

Cloudwatch -> (structure)

Parameters for publishing logs to Amazon CloudWatch Logs.

Enabled -> (boolean)

Indicates whether logging is enabled.

StateDB -> (string)

The state database that the node uses. Values are `LevelDB` or `CouchDB` .

Applies only to Hyperledger Fabric.

Status -> (string)

The status of the node.

- `CREATING` - The Amazon Web Services account is in the process of creating a node.
- `AVAILABLE` - The node has been created and can participate in the network.
- `UNHEALTHY` - The node is impaired and might not function as expected. Amazon Managed Blockchain automatically finds nodes in this state and tries to recover them. If a node is recoverable, it returns to `AVAILABLE` . Otherwise, it moves to `FAILED` status.
- `CREATE_FAILED` - The Amazon Web Services account attempted to create a node and creation failed.
- `UPDATING` - The node is in the process of being updated.
- `DELETING` - The node is in the process of being deleted.
- `DELETED` - The node can no longer participate on the network.
- `FAILED` - The node is no longer functional, cannot be recovered, and must be deleted.
- `INACCESSIBLE_ENCRYPTION_KEY` - The node is impaired and might not function as expected because it cannot access the specified customer managed key in KMS for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked. The effect of disabling or deleting a key or of revoking a grant isnât immediate. It might take some time for the node resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.

CreationDate -> (timestamp)

The date and time that the node was created.

Tags -> (map)

Tags assigned to the node. Each tag consists of a key and optional value.

For more information about tags, see [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html) in the *Amazon Managed Blockchain Ethereum Developer Guide* , or [Tagging Resources](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

key -> (string)

value -> (string)

Arn -> (string)

The Amazon Resource Name (ARN) of the node. For more information about ARNs and their format, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the customer managed key in Key Management Service (KMS) that the node uses for encryption at rest. If the value of this parameter is `"AWS Owned KMS Key"` , the node uses an Amazon Web Services owned KMS key for encryption. The node inherits this parameter from the member that it belongs to.

For more information, see [Encryption at Rest](https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/managed-blockchain-encryption-at-rest.html) in the *Amazon Managed Blockchain Hyperledger Fabric Developer Guide* .

Applies only to Hyperledger Fabric.