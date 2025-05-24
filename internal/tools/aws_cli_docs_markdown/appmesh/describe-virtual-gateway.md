# describe-virtual-gatewayÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-gateway.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appmesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/index.html#cli-aws-appmesh) ]

# describe-virtual-gateway

## Description

Describes an existing virtual gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeVirtualGateway)

## Synopsis

```
describe-virtual-gateway
--mesh-name <value>
[--mesh-owner <value>]
--virtual-gateway-name <value>
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

`--mesh-name` (string)

The name of the service mesh that the gateway route resides in.

`--mesh-owner` (string)

The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then itâs the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

`--virtual-gateway-name` (string)

The name of the virtual gateway to describe.

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

virtualGateway -> (structure)

The full description of your virtual gateway.

meshName -> (string)

The name of the service mesh that the virtual gateway resides in.

metadata -> (structure)

An object that represents metadata for a resource.

arn -> (string)

The full Amazon Resource Name (ARN) for the resource.

createdAt -> (timestamp)

The Unix epoch timestamp in seconds for when the resource was created.

lastUpdatedAt -> (timestamp)

The Unix epoch timestamp in seconds for when the resource was last updated.

meshOwner -> (string)

The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then itâs the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

resourceOwner -> (string)

The Amazon Web Services IAM account ID of the resource owner. If the account ID is not your own, then itâs the ID of the mesh owner or of another account that the mesh is shared with. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

uid -> (string)

The unique identifier for the resource.

version -> (long)

The version of the resource. Resources are created at version 1, and this version is incremented each time that theyâre updated.

spec -> (structure)

The specifications of the virtual gateway.

backendDefaults -> (structure)

A reference to an object that represents the defaults for backends.

clientPolicy -> (structure)

A reference to an object that represents a client policy.

tls -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) client policy.

certificate -> (tagged union structure)

A reference to an object that represents a virtual gatewayâs clientâs Transport Layer Security (TLS) certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`, `sds`.

file -> (structure)

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) .

certificateChain -> (string)

The certificate chain for the certificate.

privateKey -> (string)

The private key for a certificate stored on the file system of the mesh endpoint that the proxy is running on.

sds -> (structure)

A reference to an object that represents a virtual gatewayâs clientâs Secret Discovery Service certificate.

secretName -> (string)

A reference to an object that represents the name of the secret secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.

enforce -> (boolean)

Whether the policy is enforced. The default is `True` , if a value isnât specified.

ports -> (list)

One or more ports that the policy is enforced for.

(integer)

validation -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) validation context.

subjectAlternativeNames -> (structure)

A reference to an object that represents the SANs for a virtual gatewayâs listenerâs Transport Layer Security (TLS) validation context.

match -> (structure)

An object that represents the criteria for determining a SANs match.

exact -> (list)

The values sent must match the specified values exactly.

(string)

trust -> (tagged union structure)

A reference to where to retrieve the trust chain when validating a peerâs Transport Layer Security (TLS) certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `acm`, `file`, `sds`.

acm -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) validation context trust for an Certificate Manager certificate.

certificateAuthorityArns -> (list)

One or more ACM Amazon Resource Name (ARN)s.

(string)

file -> (structure)

An object that represents a Transport Layer Security (TLS) validation context trust for a local file.

certificateChain -> (string)

The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.

sds -> (structure)

A reference to an object that represents a virtual gatewayâs Transport Layer Security (TLS) Secret Discovery Service validation context trust.

secretName -> (string)

A reference to an object that represents the name of the secret for a virtual gatewayâs Transport Layer Security (TLS) Secret Discovery Service validation context trust.

listeners -> (list)

The listeners that the mesh endpoint is expected to receive inbound traffic from. You can specify one listener.

(structure)

An object that represents a listener for a virtual gateway.

connectionPool -> (tagged union structure)

The connection pool information for the virtual gateway listener.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `grpc`, `http`, `http2`.

grpc -> (structure)

An object that represents a type of connection pool.

maxRequests -> (integer)

Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster.

http -> (structure)

An object that represents a type of connection pool.

maxConnections -> (integer)

Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.

maxPendingRequests -> (integer)

Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster.

http2 -> (structure)

An object that represents a type of connection pool.

maxRequests -> (integer)

Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster.

healthCheck -> (structure)

The health check information for the listener.

healthyThreshold -> (integer)

The number of consecutive successful health checks that must occur before declaring the listener healthy.

intervalMillis -> (long)

The time period in milliseconds between each health check execution.

path -> (string)

The destination path for the health check request. This value is only used if the specified protocol is HTTP or HTTP/2. For any other protocol, this value is ignored.

port -> (integer)

The destination port for the health check request. This port must match the port defined in the  PortMapping for the listener.

protocol -> (string)

The protocol for the health check request. If you specify `grpc` , then your service must conform to the [GRPC Health Checking Protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) .

timeoutMillis -> (long)

The amount of time to wait when receiving a response from the health check, in milliseconds.

unhealthyThreshold -> (integer)

The number of consecutive failed health checks that must occur before declaring a virtual gateway unhealthy.

portMapping -> (structure)

The port mapping information for the listener.

port -> (integer)

The port used for the port mapping. Specify one protocol.

protocol -> (string)

The protocol used for the port mapping.

tls -> (structure)

A reference to an object that represents the Transport Layer Security (TLS) properties for the listener.

certificate -> (tagged union structure)

An object that represents a Transport Layer Security (TLS) certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `acm`, `file`, `sds`.

acm -> (structure)

A reference to an object that represents an Certificate Manager certificate.

certificateArn -> (string)

The Amazon Resource Name (ARN) for the certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites) .

file -> (structure)

A reference to an object that represents a local file certificate.

certificateChain -> (string)

The certificate chain for the certificate.

privateKey -> (string)

The private key for a certificate stored on the file system of the mesh endpoint that the proxy is running on.

sds -> (structure)

A reference to an object that represents a virtual gatewayâs listenerâs Secret Discovery Service certificate.

secretName -> (string)

A reference to an object that represents the name of the secret secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.

mode -> (string)

Specify one of the following modes.

- STRICT â Listener only accepts connections with TLS enabled.
- PERMISSIVE â Listener accepts connections with or without TLS enabled.
- DISABLED â Listener only accepts connections without TLS.

validation -> (structure)

A reference to an object that represents a virtual gatewayâs listenerâs Transport Layer Security (TLS) validation context.

subjectAlternativeNames -> (structure)

A reference to an object that represents the SANs for a virtual gateway listenerâs Transport Layer Security (TLS) validation context.

match -> (structure)

An object that represents the criteria for determining a SANs match.

exact -> (list)

The values sent must match the specified values exactly.

(string)

trust -> (tagged union structure)

A reference to where to retrieve the trust chain when validating a peerâs Transport Layer Security (TLS) certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`, `sds`.

file -> (structure)

An object that represents a Transport Layer Security (TLS) validation context trust for a local file.

certificateChain -> (string)

The certificate trust chain for a certificate stored on the file system of the virtual node that the proxy is running on.

sds -> (structure)

A reference to an object that represents a virtual gatewayâs listenerâs Transport Layer Security (TLS) Secret Discovery Service validation context trust.

secretName -> (string)

A reference to an object that represents the name of the secret for a virtual gatewayâs Transport Layer Security (TLS) Secret Discovery Service validation context trust.

logging -> (structure)

An object that represents logging information.

accessLog -> (tagged union structure)

The access log configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`.

file -> (structure)

The file object to send virtual gateway access logs to.

format -> (tagged union structure)

The specified format for the virtual gateway access logs. It can be either `json_format` or `text_format` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `json`, `text`.

json -> (list)

(structure)

An object that represents the key value pairs for the JSON.

key -> (string)

The specified key for the JSON.

value -> (string)

The specified value for the JSON.

text -> (string)

path -> (string)

The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out and configure your Envoy container to use a log driver, such as `awslogs` , to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy containerâs file system to write the files to disk.

status -> (structure)

The current status of the virtual gateway.

status -> (string)

The current status.

virtualGatewayName -> (string)

The name of the virtual gateway.