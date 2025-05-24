# create-routeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/create-route.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/create-route.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migration-hub-refactor-spaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/index.html#cli-aws-migration-hub-refactor-spaces) ]

# create-route

## Description

Creates an Amazon Web Services Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a `DEFAULT` `RouteType` .

When created, the default route defaults to an active state so state is not a required input. However, like all other state values the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.

When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:

- **URL Endpoints**   If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CAâs domain is also publicly resolvable.  Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in `CreateService:UrlEndpoint` when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date.    **One-time health check**   A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to `FAILED` , an error code of `SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE` is provided, and no traffic is sent to the service. For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the [CreateService:UrlEndpoint](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint) parameter. All other health check settings for the load balancer use the default values described in the [Health checks for your target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) in the *Elastic Load Balancing guide* . The health check is considered successful if at least one target within the target group transitions to a healthy state.
- **Lambda function endpoints**   If the service has an Lambda function endpoint, then Refactor Spaces configures the Lambda functionâs resource policy to allow the applicationâs API Gateway to invoke the function. The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is `Failed` , then the route creation fails. For more information, see the [GetFunctionConfigurationâs State response parameter](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State) in the *Lambda Developer Guide* . A check is performed to determine that a Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails.

**Environments without a network bridge**

When you create environments without a network bridge ([CreateEnvironment:NetworkFabricType](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType) is `NONE)` and you use your own networking infrastructure, you need to configure [VPC to VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html) between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see [Create a route](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html) in the *Refactor Spaces User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migration-hub-refactor-spaces-2021-10-26/CreateRoute)

## Synopsis

```
create-route
--application-identifier <value>
[--client-token <value>]
[--default-route <value>]
--environment-identifier <value>
--route-type <value>
--service-identifier <value>
[--tags <value>]
[--uri-path-route <value>]
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

`--application-identifier` (string)

The ID of the application within which the route is being created.

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--default-route` (structure)

Configuration for the default route type.

ActivationState -> (string)

If set to `ACTIVE` , traffic is forwarded to this routeâs service after the route is created.

Shorthand Syntax:

```
ActivationState=string
```

JSON Syntax:

```
{
  "ActivationState": "ACTIVE"|"INACTIVE"
}
```

`--environment-identifier` (string)

The ID of the environment in which the route is created.

`--route-type` (string)

The route type of the route. `DEFAULT` indicates that all traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created. `URI_PATH` indicates a route that is based on a URI path.

Possible values:

- `DEFAULT`
- `URI_PATH`

`--service-identifier` (string)

The ID of the service in which the route is created. Traffic that matches this route is forwarded to this service.

`--tags` (map)

The tags to assign to the route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair..

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--uri-path-route` (structure)

The configuration for the URI path route type.

ActivationState -> (string)

If set to `ACTIVE` , traffic is forwarded to this routeâs service after the route is created.

AppendSourcePath -> (boolean)

If set to `true` , this option appends the source path to the service URL endpoint.

IncludeChildPaths -> (boolean)

Indicates whether to match all subpaths of the given source path. If this value is `false` , requests must match the source path exactly before they are forwarded to this routeâs service.

Methods -> (list)

A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this routeâs service.

(string)

SourcePath -> (string)

This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called âuserâ.

Shorthand Syntax:

```
ActivationState=string,AppendSourcePath=boolean,IncludeChildPaths=boolean,Methods=string,string,SourcePath=string
```

JSON Syntax:

```
{
  "ActivationState": "ACTIVE"|"INACTIVE",
  "AppendSourcePath": true|false,
  "IncludeChildPaths": true|false,
  "Methods": ["DELETE"|"GET"|"HEAD"|"OPTIONS"|"PATCH"|"POST"|"PUT", ...],
  "SourcePath": "string"
}
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

## Output

ApplicationId -> (string)

The ID of the application in which the route is created.

Arn -> (string)

The Amazon Resource Name (ARN) of the route. The format for this ARN is [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/create-route.html#id1)arn:aws:refactor-spaces:*region* :*account-id* :*resource-type/resource-id* `` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CreatedByAccountId -> (string)

The Amazon Web Services account ID of the route creator.

CreatedTime -> (timestamp)

A timestamp that indicates when the route is created.

LastUpdatedTime -> (timestamp)

A timestamp that indicates when the route was last updated.

OwnerAccountId -> (string)

The Amazon Web Services account ID of the route owner.

RouteId -> (string)

The unique identifier of the route.

RouteType -> (string)

The route type of the route.

ServiceId -> (string)

The ID of service in which the route is created. Traffic that matches this route is forwarded to this service.

State -> (string)

The current state of the route. Activation state only allows `ACTIVE` or `INACTIVE` as user inputs. `FAILED` is a route state that is system generated.

Tags -> (map)

The tags assigned to the created route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.

key -> (string)

value -> (string)

UriPathRoute -> (structure)

Configuration for the URI path route type.

ActivationState -> (string)

If set to `ACTIVE` , traffic is forwarded to this routeâs service after the route is created.

AppendSourcePath -> (boolean)

If set to `true` , this option appends the source path to the service URL endpoint.

IncludeChildPaths -> (boolean)

Indicates whether to match all subpaths of the given source path. If this value is `false` , requests must match the source path exactly before they are forwarded to this routeâs service.

Methods -> (list)

A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this routeâs service.

(string)

SourcePath -> (string)

This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called âuserâ.