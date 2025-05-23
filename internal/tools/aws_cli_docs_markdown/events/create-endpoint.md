# create-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/create-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# create-endpoint

## Description

Creates a global endpoint. Global endpoints improve your applicationâs availability by making it regional-fault tolerant. To do this, you define a primary and secondary Region with event buses in each Region. You also create a Amazon Route 53 health check that will tell EventBridge to route events to the secondary Region when an âunhealthyâ state is encountered and events will be routed back to the primary Region when the health check reports a âhealthyâ state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/CreateEndpoint)

## Synopsis

```
create-endpoint
--name <value>
[--description <value>]
--routing-config <value>
[--replication-config <value>]
--event-buses <value>
[--role-arn <value>]
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

`--name` (string)

The name of the global endpoint. For example, `"Name":"us-east-2-custom_bus_A-endpoint"` .

`--description` (string)

A description of the global endpoint.

`--routing-config` (structure)

Configure the routing policy, including the health check and secondary Region..

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

Shorthand Syntax:

```
FailoverConfig={Primary={HealthCheck=string},Secondary={Route=string}}
```

JSON Syntax:

```
{
  "FailoverConfig": {
    "Primary": {
      "HealthCheck": "string"
    },
    "Secondary": {
      "Route": "string"
    }
  }
}
```

`--replication-config` (structure)

Enable or disable event replication. The default state is `ENABLED` which means you must supply a `RoleArn` . If you donât have a `RoleArn` or you donât want event replication enabled, set the state to `DISABLED` .

State -> (string)

The state of event replication.

Shorthand Syntax:

```
State=string
```

JSON Syntax:

```
{
  "State": "ENABLED"|"DISABLED"
}
```

`--event-buses` (list)

Define the event buses used.

### Warning

The names of the event buses must be identical in each Region.

(structure)

The event buses the endpoint is associated with.

EventBusArn -> (string)

The ARN of the event bus the endpoint is associated with.

Shorthand Syntax:

```
EventBusArn=string ...
```

JSON Syntax:

```
[
  {
    "EventBusArn": "string"
  }
  ...
]
```

`--role-arn` (string)

The ARN of the role used for replication.

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

Name -> (string)

The name of the endpoint that was created by this request.

Arn -> (string)

The ARN of the endpoint that was created by this request.

RoutingConfig -> (structure)

The routing configuration defined by this request.

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

Whether event replication was enabled or disabled by this request.

State -> (string)

The state of event replication.

EventBuses -> (list)

The event buses used by this request.

(structure)

The event buses the endpoint is associated with.

EventBusArn -> (string)

The ARN of the event bus the endpoint is associated with.

RoleArn -> (string)

The ARN of the role used by event replication for this request.

State -> (string)

The state of the endpoint that was created by this request.