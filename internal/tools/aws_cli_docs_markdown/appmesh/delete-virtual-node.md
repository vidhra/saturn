# delete-virtual-nodeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appmesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/index.html#cli-aws-appmesh) ]

# delete-virtual-node

## Description

Deletes an existing virtual node.

You must delete any virtual services that list a virtual node as a service provider before you can delete the virtual node itself.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteVirtualNode)

## Synopsis

```
delete-virtual-node
--mesh-name <value>
[--mesh-owner <value>]
--virtual-node-name <value>
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

The name of the service mesh to delete the virtual node in.

`--mesh-owner` (string)

The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then itâs the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

`--virtual-node-name` (string)

The name of the virtual node to delete.

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

**To delete a virtual node**

The following `delete-virtual-node` example deletes the specified virtual node.

```
aws appmesh delete-virtual-node \
    --mesh-name app1 \
    --virtual-node-name vnServiceBv2
```

Output:

```
{
    "virtualNode": {
        "meshName": "app1",
        "metadata": {
            "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv2",
            "createdAt": 1563810117.297,
            "lastUpdatedAt": 1563824700.678,
            "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "version": 2
        },
        "spec": {
            "backends": [],
            "listeners": [
                {
                    "portMapping": {
                        "port": 80,
                        "protocol": "http"
                    }
                }
            ],
            "serviceDiscovery": {
                "dns": {
                    "hostname": "serviceBv2.svc.cluster.local"
                }
            }
        },
        "status": {
            "status": "DELETED"
        },
        "virtualNodeName": "vnServiceBv2"
    }
}
```

For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html) in the *AWS App Mesh User Guide*.

## Output

virtualNode -> (structure)

The virtual node that was deleted.

meshName -> (string)

The name of the service mesh that the virtual node resides in.

metadata -> (structure)

The associated metadata for the virtual node.

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

The specifications of the virtual node.

backendDefaults -> (structure)

A reference to an object that represents the defaults for backends.

clientPolicy -> (structure)

A reference to an object that represents a client policy.

tls -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) client policy.

certificate -> (tagged union structure)

A reference to an object that represents a clientâs TLS certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`, `sds`.

file -> (structure)

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) .

certificateChain -> (string)

The certificate chain for the certificate.

privateKey -> (string)

The private key for a certificate stored on the file system of the virtual node that the proxy is running on.

sds -> (structure)

A reference to an object that represents a clientâs TLS Secret Discovery Service certificate.

secretName -> (string)

A reference to an object that represents the name of the secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.

enforce -> (boolean)

Whether the policy is enforced. The default is `True` , if a value isnât specified.

ports -> (list)

One or more ports that the policy is enforced for.

(integer)

validation -> (structure)

A reference to an object that represents a TLS validation context.

subjectAlternativeNames -> (structure)

A reference to an object that represents the SANs for a Transport Layer Security (TLS) validation context. If you donât specify SANs on the *terminating* mesh endpoint, the Envoy proxy for that node doesnât verify the SAN on a peer client certificate. If you donât specify SANs on the *originating* mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration. Since SPIRE vended certificates have a SPIFFE ID as a name, you must set the SAN since the name doesnât match the service discovery name.

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

A reference to an object that represents a Transport Layer Security (TLS) Secret Discovery Service validation context trust.

secretName -> (string)

A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.

backends -> (list)

The backends that the virtual node is expected to send outbound traffic to.

(tagged union structure)

An object that represents the backends that a virtual node is expected to send outbound traffic to.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `virtualService`.

virtualService -> (structure)

Specifies a virtual service to use as a backend.

clientPolicy -> (structure)

A reference to an object that represents the client policy for a backend.

tls -> (structure)

A reference to an object that represents a Transport Layer Security (TLS) client policy.

certificate -> (tagged union structure)

A reference to an object that represents a clientâs TLS certificate.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`, `sds`.

file -> (structure)

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) .

certificateChain -> (string)

The certificate chain for the certificate.

privateKey -> (string)

The private key for a certificate stored on the file system of the virtual node that the proxy is running on.

sds -> (structure)

A reference to an object that represents a clientâs TLS Secret Discovery Service certificate.

secretName -> (string)

A reference to an object that represents the name of the secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.

enforce -> (boolean)

Whether the policy is enforced. The default is `True` , if a value isnât specified.

ports -> (list)

One or more ports that the policy is enforced for.

(integer)

validation -> (structure)

A reference to an object that represents a TLS validation context.

subjectAlternativeNames -> (structure)

A reference to an object that represents the SANs for a Transport Layer Security (TLS) validation context. If you donât specify SANs on the *terminating* mesh endpoint, the Envoy proxy for that node doesnât verify the SAN on a peer client certificate. If you donât specify SANs on the *originating* mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration. Since SPIRE vended certificates have a SPIFFE ID as a name, you must set the SAN since the name doesnât match the service discovery name.

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

A reference to an object that represents a Transport Layer Security (TLS) Secret Discovery Service validation context trust.

secretName -> (string)

A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.

virtualServiceName -> (string)

The name of the virtual service that is acting as a virtual node backend.

listeners -> (list)

The listener that the virtual node is expected to receive inbound traffic from. You can specify one listener.

(structure)

An object that represents a listener for a virtual node.

connectionPool -> (tagged union structure)

The connection pool information for the listener.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `grpc`, `http`, `http2`, `tcp`.

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

tcp -> (structure)

An object that represents a type of connection pool.

maxConnections -> (integer)

Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.

healthCheck -> (structure)

The health check information for the listener.

healthyThreshold -> (integer)

The number of consecutive successful health checks that must occur before declaring listener healthy.

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

The number of consecutive failed health checks that must occur before declaring a virtual node unhealthy.

outlierDetection -> (structure)

The outlier detection information for the listener.

baseEjectionDuration -> (structure)

The base amount of time for which a host is ejected.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

interval -> (structure)

The time interval between ejection sweep analysis.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

maxEjectionPercent -> (integer)

Maximum percentage of hosts in load balancing pool for upstream service that can be ejected. Will eject at least one host regardless of the value.

maxServerErrors -> (long)

Number of consecutive `5xx` errors required for ejection.

portMapping -> (structure)

The port mapping information for the listener.

port -> (integer)

The port used for the port mapping.

protocol -> (string)

The protocol used for the port mapping. Specify one protocol.

timeout -> (tagged union structure)

An object that represents timeouts for different protocols.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `grpc`, `http`, `http2`, `tcp`.

grpc -> (structure)

An object that represents types of timeouts.

idle -> (structure)

An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

perRequest -> (structure)

An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

http -> (structure)

An object that represents types of timeouts.

idle -> (structure)

An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

perRequest -> (structure)

An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

http2 -> (structure)

An object that represents types of timeouts.

idle -> (structure)

An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

perRequest -> (structure)

An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

tcp -> (structure)

An object that represents types of timeouts.

idle -> (structure)

An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

tls -> (structure)

A reference to an object that represents the Transport Layer Security (TLS) properties for a listener.

certificate -> (tagged union structure)

A reference to an object that represents a listenerâs Transport Layer Security (TLS) certificate.

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

The private key for a certificate stored on the file system of the virtual node that the proxy is running on.

sds -> (structure)

A reference to an object that represents a listenerâs Secret Discovery Service certificate.

secretName -> (string)

A reference to an object that represents the name of the secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.

mode -> (string)

Specify one of the following modes.

- STRICT â Listener only accepts connections with TLS enabled.
- PERMISSIVE â Listener accepts connections with or without TLS enabled.
- DISABLED â Listener only accepts connections without TLS.

validation -> (structure)

A reference to an object that represents a listenerâs Transport Layer Security (TLS) validation context.

subjectAlternativeNames -> (structure)

A reference to an object that represents the SANs for a listenerâs Transport Layer Security (TLS) validation context.

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

A reference to an object that represents a listenerâs Transport Layer Security (TLS) Secret Discovery Service validation context trust.

secretName -> (string)

A reference to an object that represents the name of the secret for a Transport Layer Security (TLS) Secret Discovery Service validation context trust.

logging -> (structure)

The inbound and outbound access logging information for the virtual node.

accessLog -> (tagged union structure)

The access log configuration for a virtual node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`.

file -> (structure)

The file object to send virtual node access logs to.

format -> (tagged union structure)

The specified format for the logs. The format is either `json_format` or `text_format` .

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

### Note

The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.

serviceDiscovery -> (tagged union structure)

The service discovery information for the virtual node. If your virtual node does not expect ingress traffic, you can omit this parameter. If you specify a `listener` , then you must specify service discovery information.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `awsCloudMap`, `dns`.

awsCloudMap -> (structure)

Specifies any Cloud Map information for the virtual node.

attributes -> (list)

A string map that contains attributes with values that you can use to filter instances by any custom attribute that you specified when you registered the instance. Only instances that match all of the specified key/value pairs will be returned.

(structure)

An object that represents the Cloud Map attribute information for your virtual node.

### Note

Cloud Map is not available in the eu-south-1 Region.

key -> (string)

The name of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.

value -> (string)

The value of an Cloud Map service instance attribute key. Any Cloud Map service instance that contains the specified key and value is returned.

ipPreference -> (string)

The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.

namespaceName -> (string)

The name of the Cloud Map namespace to use.

serviceName -> (string)

The name of the Cloud Map service to use.

dns -> (structure)

Specifies the DNS information for the virtual node.

hostname -> (string)

Specifies the DNS service discovery hostname for the virtual node.

ipPreference -> (string)

The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.

responseType -> (string)

Specifies the DNS response type for the virtual node.

status -> (structure)

The current status for the virtual node.

status -> (string)

The current status of the virtual node.

virtualNodeName -> (string)

The name of the virtual node.