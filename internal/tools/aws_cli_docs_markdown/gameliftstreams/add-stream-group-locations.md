# add-stream-group-locationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/add-stream-group-locations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/add-stream-group-locations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# add-stream-group-locations

## Description

Add locations that can host stream sessions. You configure locations and their corresponding capacity for each stream group. Creating a stream group in a location thatâs nearest to your end users can help minimize latency and improve quality.

This operation provisions stream capacity at the specified locations. By default, all locations have 1 or 2 capacity, depending on the stream class option: 2 for âHighâ and 1 for âUltraâ and âWin2022â. This operation also copies the content files of all associated applications to an internal S3 bucket at each location. This allows Amazon GameLift Streams to host performant stream sessions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/AddStreamGroupLocations)

## Synopsis

```
add-stream-group-locations
--identifier <value>
--location-configurations <value>
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

`--identifier` (string)

A stream group to add the specified locations to.

This value is a Amazon Resource Name (ARN) that uniquely identifies the stream group resource. Format example: `sg-1AB2C3De4` .

`--location-configurations` (list)

A set of one or more locations and the streaming capacity for each location.

(structure)

Configuration settings that define a stream groupâs stream capacity for a location. When configuring a location for the first time, you must specify a numeric value for at least one of the two capacity types. To update the capacity for an existing stream group, call [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html) . To add a new location and specify its capacity, call [AddStreamGroupLocations](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AddStreamGroupLocations.html) .

AlwaysOnCapacity -> (integer)

The streaming capacity that is allocated and ready to handle stream requests without delay. You pay for this capacity whether itâs in use or not. Best for quickest time from streaming request to streaming session.

LocationName -> (string)

A locationâs name. For example, `us-east-1` . For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions and quotas](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide* .

OnDemandCapacity -> (integer)

The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes).

Shorthand Syntax:

```
AlwaysOnCapacity=integer,LocationName=string,OnDemandCapacity=integer ...
```

JSON Syntax:

```
[
  {
    "AlwaysOnCapacity": integer,
    "LocationName": "string",
    "OnDemandCapacity": integer
  }
  ...
]
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

Identifier -> (string)

This value is the Amazon Resource Name (ARN) that uniquely identifies the stream group resource. Format example: `sg-1AB2C3De4` .

Locations -> (list)

This value is set of locations, including their name, current status, and capacities.

A location can be in one of the following states:

- **ACTIVATING** : Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
- **ACTIVE** : The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
- **ERROR** : Amazon GameLift Streams failed to set up this location. The StatusReason field describes the error. You can remove this location and try to add it again.
- **REMOVING** : Amazon GameLift Streams is working to remove this location. It releases all provisioned capacity for this location in this stream group.

(structure)

Represents a location and its corresponding stream capacity and status.

AllocatedCapacity -> (integer)

This value is the number of compute resources that a stream group has provisioned and is ready to stream. It includes resources that are currently streaming and resources that are idle and ready to respond to stream requests.

AlwaysOnCapacity -> (integer)

The streaming capacity that is allocated and ready to handle stream requests without delay. You pay for this capacity whether itâs in use or not. Best for quickest time from streaming request to streaming session.

IdleCapacity -> (integer)

This value is the amount of allocated capacity that is not currently streaming. It represents the stream groupâs availability to respond to new stream requests, but not including on-demand capacity.

LocationName -> (string)

A locationâs name. For example, `us-east-1` . For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions and quotas](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide* .

OnDemandCapacity -> (integer)

The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes).

RequestedCapacity -> (integer)

This value is the total number of compute resources that you request for a stream group. This includes resources that Amazon GameLift Streams has either already provisioned or is working to provision. You request capacity for each location in a stream group.

Status -> (string)

This value is set of locations, including their name, current status, and capacities.

A location can be in one of the following states:

- **ACTIVATING** : Amazon GameLift Streams is preparing the location. You cannot stream from, scale the capacity of, or remove this location yet.
- **ACTIVE** : The location is provisioned with initial capacity. You can now stream from, scale the capacity of, or remove this location.
- **ERROR** : Amazon GameLift Streams failed to set up this location. The StatusReason field describes the error. You can remove this location and try to add it again.
- **REMOVING** : Amazon GameLift Streams is working to remove this location. It releases all provisioned capacity for this location in this stream group.