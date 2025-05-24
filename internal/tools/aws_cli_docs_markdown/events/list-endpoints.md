# list-endpointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-endpoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-endpoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# list-endpoints

## Description

List the global endpoints associated with this account. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* * .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/ListEndpoints)

## Synopsis

```
list-endpoints
[--name-prefix <value>]
[--home-region <value>]
[--next-token <value>]
[--max-results <value>]
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

`--name-prefix` (string)

A value that will return a subset of the endpoints associated with this account. For example, `"NamePrefix": "ABC"` will return all endpoints with âABCâ in the name.

`--home-region` (string)

The primary Region of the endpoints associated with this account. For example `"HomeRegion": "us-east-1"` .

`--next-token` (string)

The token returned by a previous call, which you can use to retrieve the next set of results.

The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.

Using an expired pagination token results in an `HTTP 400 InvalidToken` error.

`--max-results` (integer)

The maximum number of results returned by the call.

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

Endpoints -> (list)

The endpoints returned by the call.

(structure)

A global endpoint used to improve your applicationâs availability by making it regional-fault tolerant. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* * .

Name -> (string)

The name of the endpoint.

Description -> (string)

A description for the endpoint.

Arn -> (string)

The ARN of the endpoint.

RoutingConfig -> (structure)

The routing configuration of the endpoint.

FailoverConfig -> (structure)

The failover configuration for an endpoint. This includes what triggers failover and what happens when itâs triggered.

Primary -> (structure)

The main Region of the endpoint.

HealthCheck -> (string)

The ARN of the health check used by the endpoint to determine whether failover is triggered.

Secondary -> (structure)

The Region that events are routed to when failover is triggered or event replication is enabled.

Route -> (string)

Defines the secondary Region.

ReplicationConfig -> (structure)

Whether event replication was enabled or disabled for this endpoint. The default state is `ENABLED` which means you must supply a `RoleArn` . If you donât have a `RoleArn` or you donât want event replication enabled, set the state to `DISABLED` .

State -> (string)

The state of event replication.

EventBuses -> (list)

The event buses being used by the endpoint.

(structure)

The event buses the endpoint is associated with.

EventBusArn -> (string)

The ARN of the event bus the endpoint is associated with.

RoleArn -> (string)

The ARN of the role used by event replication for the endpoint.

EndpointId -> (string)

The URL subdomain of the endpoint. For example, if the URL for Endpoint is [https://abcde.veo.endpoints.event.amazonaws.com](https://abcde.veo.endpoints.event.amazonaws.com), then the EndpointId is `abcde.veo` .

EndpointUrl -> (string)

The URL of the endpoint.

State -> (string)

The current state of the endpoint.

StateReason -> (string)

The reason the endpoint is in its current state.

CreationTime -> (timestamp)

The time the endpoint was created.

LastModifiedTime -> (timestamp)

The last time the endpoint was modified.

NextToken -> (string)

A token indicating there are more results available. If there are no more results, no token is included in the response.

The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.

Using an expired pagination token results in an `HTTP 400 InvalidToken` error.