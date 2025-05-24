# describe-routeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appmesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/index.html#cli-aws-appmesh) ]

# describe-route

## Description

Describes an existing route.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DescribeRoute)

## Synopsis

```
describe-route
--mesh-name <value>
[--mesh-owner <value>]
--route-name <value>
--virtual-router-name <value>
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

The name of the service mesh that the route resides in.

`--mesh-owner` (string)

The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then itâs the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

`--route-name` (string)

The name of the route to describe.

`--virtual-router-name` (string)

The name of the virtual router that the route is associated with.

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

**To describe a route**

The following `describe-route` example returns details about the specified route.

```
aws appmesh describe-route \
    --mesh-name app1 \
    --virtual-router-name vrServiceB \
    --route-name toVnServiceB-weighted
```

Output:

```
{
    "route": {
        "meshName": "app1",
        "metadata": {
            "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB/route/toVnServiceB-weighted",
            "createdAt": 1563811384.015,
            "lastUpdatedAt": 1563811384.015,
            "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "version": 1
        },
        "routeName": "toVnServiceB-weighted",
        "spec": {
            "httpRoute": {
                "action": {
                    "weightedTargets": [
                        {
                            "virtualNode": "vnServiceBv1",
                            "weight": 90
                        },
                        {
                            "virtualNode": "vnServiceBv2",
                            "weight": 10
                        }
                    ]
                },
                "match": {
                    "prefix": "/"
                }
            }
        },
        "status": {
            "status": "ACTIVE"
        },
        "virtualRouterName": "vrServiceB"
    }
}
```

For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html) in the *AWS App Mesh User Guide*.

## Output

route -> (structure)

The full description of your route.

meshName -> (string)

The name of the service mesh that the route resides in.

metadata -> (structure)

The associated metadata for the route.

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

routeName -> (string)

The name of the route.

spec -> (structure)

The specifications of the route.

grpcRoute -> (structure)

An object that represents the specification of a gRPC route.

action -> (structure)

An object that represents the action to take if a match is determined.

weightedTargets -> (list)

An object that represents the targets that traffic is routed to when a request matches the route.

(structure)

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

port -> (integer)

The targeted port of the weighted object.

virtualNode -> (string)

The virtual node to associate with the weighted target.

weight -> (integer)

The relative weight of the weighted target.

match -> (structure)

An object that represents the criteria for determining a request match.

metadata -> (list)

An object that represents the data to match from the request.

(structure)

An object that represents the match metadata for the route.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

An object that represents the data to match from the request.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `exact`, `prefix`, `range`, `regex`, `suffix`.

exact -> (string)

The value sent by the client must match the specified value exactly.

prefix -> (string)

The value sent by the client must begin with the specified characters.

range -> (structure)

An object that represents the range of values to match on.

end -> (long)

The end of the range.

start -> (long)

The start of the range.

regex -> (string)

The value sent by the client must include the specified characters.

suffix -> (string)

The value sent by the client must end with the specified characters.

name -> (string)

The name of the route.

methodName -> (string)

The method name to match from the request. If you specify a name, you must also specify a `serviceName` .

port -> (integer)

The port number to match on.

serviceName -> (string)

The fully qualified domain name for the service to match from the request.

retryPolicy -> (structure)

An object that represents a retry policy.

grpcRetryEvents -> (list)

Specify at least one of the valid values.

(string)

httpRetryEvents -> (list)

Specify at least one of the following values.

- **server-error** â HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
- **gateway-error** â HTTP status codes 502, 503, and 504
- **client-error** â HTTP status code 409
- **stream-error** â Retry on refused stream

(string)

maxRetries -> (long)

The maximum number of retry attempts.

perRetryTimeout -> (structure)

The timeout for each retry attempt.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

tcpRetryEvents -> (list)

Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.

(string)

timeout -> (structure)

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

http2Route -> (structure)

An object that represents the specification of an HTTP/2 route.

action -> (structure)

An object that represents the action to take if a match is determined.

weightedTargets -> (list)

An object that represents the targets that traffic is routed to when a request matches the route.

(structure)

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

port -> (integer)

The targeted port of the weighted object.

virtualNode -> (string)

The virtual node to associate with the weighted target.

weight -> (integer)

The relative weight of the weighted target.

match -> (structure)

An object that represents the criteria for determining a request match.

headers -> (list)

The client request headers to match on.

(structure)

An object that represents the HTTP header in the request.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

The `HeaderMatchMethod` object.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `exact`, `prefix`, `range`, `regex`, `suffix`.

exact -> (string)

The value sent by the client must match the specified value exactly.

prefix -> (string)

The value sent by the client must begin with the specified characters.

range -> (structure)

An object that represents the range of values to match on.

end -> (long)

The end of the range.

start -> (long)

The start of the range.

regex -> (string)

The value sent by the client must include the specified characters.

suffix -> (string)

The value sent by the client must end with the specified characters.

name -> (string)

A name for the HTTP header in the client request that will be matched on.

method -> (string)

The client request method to match on. Specify only one.

path -> (structure)

The client request path to match on.

exact -> (string)

The exact path to match on.

regex -> (string)

The regex used to match the path.

port -> (integer)

The port number to match on.

prefix -> (string)

Specifies the path to match requests with. This parameter must always start with `/` , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics` , your prefix should be `/metrics` .

queryParameters -> (list)

The client request query parameters to match on.

(structure)

An object that represents the query parameter in the request.

match -> (structure)

The query parameter to match on.

exact -> (string)

The exact query parameter to match on.

name -> (string)

A name for the query parameter that will be matched on.

scheme -> (string)

The client request scheme to match on. Specify only one. Applicable only for HTTP2 routes.

retryPolicy -> (structure)

An object that represents a retry policy.

httpRetryEvents -> (list)

Specify at least one of the following values.

- **server-error** â HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
- **gateway-error** â HTTP status codes 502, 503, and 504
- **client-error** â HTTP status code 409
- **stream-error** â Retry on refused stream

(string)

maxRetries -> (long)

The maximum number of retry attempts.

perRetryTimeout -> (structure)

The timeout for each retry attempt.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

tcpRetryEvents -> (list)

Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.

(string)

timeout -> (structure)

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

httpRoute -> (structure)

An object that represents the specification of an HTTP route.

action -> (structure)

An object that represents the action to take if a match is determined.

weightedTargets -> (list)

An object that represents the targets that traffic is routed to when a request matches the route.

(structure)

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

port -> (integer)

The targeted port of the weighted object.

virtualNode -> (string)

The virtual node to associate with the weighted target.

weight -> (integer)

The relative weight of the weighted target.

match -> (structure)

An object that represents the criteria for determining a request match.

headers -> (list)

The client request headers to match on.

(structure)

An object that represents the HTTP header in the request.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

The `HeaderMatchMethod` object.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `exact`, `prefix`, `range`, `regex`, `suffix`.

exact -> (string)

The value sent by the client must match the specified value exactly.

prefix -> (string)

The value sent by the client must begin with the specified characters.

range -> (structure)

An object that represents the range of values to match on.

end -> (long)

The end of the range.

start -> (long)

The start of the range.

regex -> (string)

The value sent by the client must include the specified characters.

suffix -> (string)

The value sent by the client must end with the specified characters.

name -> (string)

A name for the HTTP header in the client request that will be matched on.

method -> (string)

The client request method to match on. Specify only one.

path -> (structure)

The client request path to match on.

exact -> (string)

The exact path to match on.

regex -> (string)

The regex used to match the path.

port -> (integer)

The port number to match on.

prefix -> (string)

Specifies the path to match requests with. This parameter must always start with `/` , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics` , your prefix should be `/metrics` .

queryParameters -> (list)

The client request query parameters to match on.

(structure)

An object that represents the query parameter in the request.

match -> (structure)

The query parameter to match on.

exact -> (string)

The exact query parameter to match on.

name -> (string)

A name for the query parameter that will be matched on.

scheme -> (string)

The client request scheme to match on. Specify only one. Applicable only for HTTP2 routes.

retryPolicy -> (structure)

An object that represents a retry policy.

httpRetryEvents -> (list)

Specify at least one of the following values.

- **server-error** â HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
- **gateway-error** â HTTP status codes 502, 503, and 504
- **client-error** â HTTP status code 409
- **stream-error** â Retry on refused stream

(string)

maxRetries -> (long)

The maximum number of retry attempts.

perRetryTimeout -> (structure)

The timeout for each retry attempt.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

tcpRetryEvents -> (list)

Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.

(string)

timeout -> (structure)

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

priority -> (integer)

The priority for the route. Routes are matched based on the specified value, where 0 is the highest priority.

tcpRoute -> (structure)

An object that represents the specification of a TCP route.

action -> (structure)

The action to take if a match is determined.

weightedTargets -> (list)

An object that represents the targets that traffic is routed to when a request matches the route.

(structure)

An object that represents a target and its relative weight. Traffic is distributed across targets according to their relative weight. For example, a weighted target with a relative weight of 50 receives five times as much traffic as one with a relative weight of 10. The total weight for all targets combined must be less than or equal to 100.

port -> (integer)

The targeted port of the weighted object.

virtualNode -> (string)

The virtual node to associate with the weighted target.

weight -> (integer)

The relative weight of the weighted target.

match -> (structure)

An object that represents the criteria for determining a request match.

port -> (integer)

The port number to match on.

timeout -> (structure)

An object that represents types of timeouts.

idle -> (structure)

An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.

unit -> (string)

A unit of time.

value -> (long)

A number of time units.

status -> (structure)

The status of the route.

status -> (string)

The current status for the route.

virtualRouterName -> (string)

The virtual router that the route is associated with.