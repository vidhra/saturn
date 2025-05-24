# delete-gateway-routeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-gateway-route.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-gateway-route.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appmesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/index.html#cli-aws-appmesh) ]

# delete-gateway-route

## Description

Deletes an existing gateway route.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appmesh-2019-01-25/DeleteGatewayRoute)

## Synopsis

```
delete-gateway-route
--gateway-route-name <value>
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

`--gateway-route-name` (string)

The name of the gateway route to delete.

`--mesh-name` (string)

The name of the service mesh to delete the gateway route from.

`--mesh-owner` (string)

The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then itâs the ID of the account that shared the mesh with your account. For more information about mesh sharing, see [Working with shared meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html) .

`--virtual-gateway-name` (string)

The name of the virtual gateway to delete the route from.

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

gatewayRoute -> (structure)

The gateway route that was deleted.

gatewayRouteName -> (string)

The name of the gateway route.

meshName -> (string)

The name of the service mesh that the resource resides in.

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

The specifications of the gateway route.

grpcRoute -> (structure)

An object that represents the specification of a gRPC gateway route.

action -> (structure)

An object that represents the action to take if a match is determined.

rewrite -> (structure)

The gateway route action to rewrite.

hostname -> (structure)

The host name of the gateway route to rewrite.

defaultTargetHostname -> (string)

The default target host name to write to.

target -> (structure)

An object that represents the target that traffic is routed to when a request matches the gateway route.

port -> (integer)

The port number of the gateway route target.

virtualService -> (structure)

An object that represents a virtual service gateway route target.

virtualServiceName -> (string)

The name of the virtual service that traffic is routed to.

match -> (structure)

An object that represents the criteria for determining a request match.

hostname -> (structure)

The gateway route host name to be matched on.

exact -> (string)

The exact host name to match on.

suffix -> (string)

The specified ending characters of the host name to match on.

metadata -> (list)

The gateway route metadata to be matched on.

(structure)

An object representing the metadata of the gateway route.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

The criteria for determining a metadata match.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `exact`, `prefix`, `range`, `regex`, `suffix`.

exact -> (string)

The exact method header to be matched on.

prefix -> (string)

The specified beginning characters of the method header to be matched on.

range -> (structure)

An object that represents the range of values to match on. The first character of the range is included in the range, though the last character is not. For example, if the range specified were 1-100, only values 1-99 would be matched.

end -> (long)

The end of the range.

start -> (long)

The start of the range.

regex -> (string)

The regex used to match the method header.

suffix -> (string)

The specified ending characters of the method header to match on.

name -> (string)

A name for the gateway route metadata.

port -> (integer)

The gateway route port to be matched on.

serviceName -> (string)

The fully qualified domain name for the service to match from the request.

http2Route -> (structure)

An object that represents the specification of an HTTP/2 gateway route.

action -> (structure)

An object that represents the action to take if a match is determined.

rewrite -> (structure)

The gateway route action to rewrite.

hostname -> (structure)

The host name to rewrite.

defaultTargetHostname -> (string)

The default target host name to write to.

path -> (structure)

The path to rewrite.

exact -> (string)

The exact path to rewrite.

prefix -> (structure)

The specified beginning characters to rewrite.

defaultPrefix -> (string)

The default prefix used to replace the incoming route prefix when rewritten.

value -> (string)

The value used to replace the incoming route prefix when rewritten.

target -> (structure)

An object that represents the target that traffic is routed to when a request matches the gateway route.

port -> (integer)

The port number of the gateway route target.

virtualService -> (structure)

An object that represents a virtual service gateway route target.

virtualServiceName -> (string)

The name of the virtual service that traffic is routed to.

match -> (structure)

An object that represents the criteria for determining a request match.

headers -> (list)

The client request headers to match on.

(structure)

An object that represents the HTTP header in the gateway route.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

An object that represents the method and value to match with the header value sent in a request. Specify one match method.

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

A name for the HTTP header in the gateway route that will be matched on.

hostname -> (structure)

The host name to match on.

exact -> (string)

The exact host name to match on.

suffix -> (string)

The specified ending characters of the host name to match on.

method -> (string)

The method to match on.

path -> (structure)

The path to match on.

exact -> (string)

The exact path to match on.

regex -> (string)

The regex used to match the path.

port -> (integer)

The port number to match on.

prefix -> (string)

Specifies the path to match requests with. This parameter must always start with `/` , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics` , your prefix should be `/metrics` .

queryParameters -> (list)

The query parameter to match on.

(structure)

An object that represents the query parameter in the request.

match -> (structure)

The query parameter to match on.

exact -> (string)

The exact query parameter to match on.

name -> (string)

A name for the query parameter that will be matched on.

httpRoute -> (structure)

An object that represents the specification of an HTTP gateway route.

action -> (structure)

An object that represents the action to take if a match is determined.

rewrite -> (structure)

The gateway route action to rewrite.

hostname -> (structure)

The host name to rewrite.

defaultTargetHostname -> (string)

The default target host name to write to.

path -> (structure)

The path to rewrite.

exact -> (string)

The exact path to rewrite.

prefix -> (structure)

The specified beginning characters to rewrite.

defaultPrefix -> (string)

The default prefix used to replace the incoming route prefix when rewritten.

value -> (string)

The value used to replace the incoming route prefix when rewritten.

target -> (structure)

An object that represents the target that traffic is routed to when a request matches the gateway route.

port -> (integer)

The port number of the gateway route target.

virtualService -> (structure)

An object that represents a virtual service gateway route target.

virtualServiceName -> (string)

The name of the virtual service that traffic is routed to.

match -> (structure)

An object that represents the criteria for determining a request match.

headers -> (list)

The client request headers to match on.

(structure)

An object that represents the HTTP header in the gateway route.

invert -> (boolean)

Specify `True` to match anything except the match criteria. The default value is `False` .

match -> (tagged union structure)

An object that represents the method and value to match with the header value sent in a request. Specify one match method.

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

A name for the HTTP header in the gateway route that will be matched on.

hostname -> (structure)

The host name to match on.

exact -> (string)

The exact host name to match on.

suffix -> (string)

The specified ending characters of the host name to match on.

method -> (string)

The method to match on.

path -> (structure)

The path to match on.

exact -> (string)

The exact path to match on.

regex -> (string)

The regex used to match the path.

port -> (integer)

The port number to match on.

prefix -> (string)

Specifies the path to match requests with. This parameter must always start with `/` , which by itself matches all requests to the virtual service name. You can also match for path-based routing of requests. For example, if your virtual service name is `my-service.local` and you want the route to match requests to `my-service.local/metrics` , your prefix should be `/metrics` .

queryParameters -> (list)

The query parameter to match on.

(structure)

An object that represents the query parameter in the request.

match -> (structure)

The query parameter to match on.

exact -> (string)

The exact query parameter to match on.

name -> (string)

A name for the query parameter that will be matched on.

priority -> (integer)

The ordering of the gateway routes spec.

status -> (structure)

The status of the gateway route.

status -> (string)

The current status for the gateway route.

virtualGatewayName -> (string)

The virtual gateway that the gateway route is associated with.