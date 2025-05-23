# get-stream-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/get-stream-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/get-stream-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# get-stream-group

## Description

Retrieves properties for a Amazon GameLift Streams stream group resource. Specify the ID of the stream group that you want to retrieve. If the operation is successful, it returns properties for the requested stream group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/GetStreamGroup)

## Synopsis

```
get-stream-group
--identifier <value>
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

The unique ID value of the stream group resource to retrieve. Format example: `sg-1AB2C3De4` .

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

Arn -> (string)

An Amazon Resource Name (ARN) that is assigned to the stream group resource and that uniquely identifies the group across all Amazon Web Services Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:streamgroup/[resource ID]` .

AssociatedApplications -> (list)

A set of applications that this stream group is associated to. You can stream any of these applications by using this stream group.

This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify application resources. Format example: `arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` .

(string)

CreatedAt -> (timestamp)

A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

DefaultApplication -> (structure)

The default Amazon GameLift Streams application that is associated with this stream group.

Arn -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Format example: `arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` .

Id -> (string)

An ID that uniquely identifies the application resource. For example: `a-9ZY8X7Wv6` .

Description -> (string)

A descriptive label for the stream group.

Id -> (string)

A unique ID value that is assigned to the resource when itâs created. Format example: `sg-1AB2C3De4` .

LastUpdatedAt -> (timestamp)

A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

LocationStates -> (list)

This value is the set of locations, including their name, current status, and capacities.

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

Status -> (string)

The current status of the stream group resource. Possible statuses include the following:

- `ACTIVATING` : The stream group is deploying and isnât ready to host streams.
- `ACTIVE` : The stream group is ready to host streams.
- `ACTIVE_WITH_ERRORS` : One or more locations in the stream group are in an error state. Verify the details of individual locations and remove any locations which are in error.
- `ERROR` : An error occurred when the stream group deployed. See `StatusReason` for more information.
- `DELETING` : Amazon GameLift Streams is in the process of deleting the stream group.
- `UPDATING_LOCATIONS` : One or more locations in the stream group are in the process of updating (either activating or deleting).

StatusReason -> (string)

A short description of the reason that the stream group is in `ERROR` status. The possible reasons can be one of the following:

- `internalError` : The request canât process right now bcause of an issue with the server. Try again later. Reach out to the Amazon GameLift Streams team for more help.
- `noAvailableInstances` : Amazon GameLift Streams does not currently have enough available On-Demand capacity to fulfill your request. Wait a few minutes and retry the request as capacity can shift frequently. You can also try to make the request using a different stream class or in another region.

StreamClass -> (string)

The target stream quality for the stream group.

A stream class can be one of the following:

- **``gen5n_win2022`` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA A10G Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
- Tenancy: Supports 1 concurrent stream session
- **``gen5n_high`` (NVIDIA, high)** Supports applications with moderate to high 3D scene complexity. Uses NVIDIA A10G Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM
- Tenancy: Supports up to 2 concurrent stream sessions
- **``gen5n_ultra`` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Uses dedicated NVIDIA A10G Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM
- Tenancy: Supports 1 concurrent stream session
- **``gen4n_win2022`` (NVIDIA, ultra)** Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.4, 32 and 64-bit applications, and anti-cheat technology. Uses NVIDIA T4 Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
- Tenancy: Supports 1 concurrent stream session
- **``gen4n_high`` (NVIDIA, high)** Supports applications with moderate to high 3D scene complexity. Uses NVIDIA T4 Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM
- Tenancy: Supports up to 2 concurrent stream sessions
- **``gen4n_ultra`` (NVIDIA, ultra)** Supports applications with high 3D scene complexity. Uses dedicated NVIDIA T4 Tensor GPU.
- Reference resolution: 1080p
- Reference frame rate: 60 fps
- Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM
- Tenancy: Supports 1 concurrent stream session