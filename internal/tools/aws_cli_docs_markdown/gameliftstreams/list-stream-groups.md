# list-stream-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/list-stream-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/list-stream-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gameliftstreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gameliftstreams/index.html#cli-aws-gameliftstreams) ]

# list-stream-groups

## Description

Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. This operation returns stream groups in all statuses, in no particular order. You can paginate the results as needed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gameliftstreams-2018-05-10/ListStreamGroups)

`list-stream-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-stream-groups
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Items -> (list)

A collection of Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. Each item includes stream group metadata and status, but doesnât include capacity information.

(structure)

Describes a Amazon GameLift Streams stream group resource for hosting content streams. To retrieve additional stream group details, call [GetStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html) .

Arn -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4` or ID-`sg-1AB2C3De4` .

CreatedAt -> (timestamp)

A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

DefaultApplication -> (structure)

Object that identifies the Amazon GameLift Streams application to stream with this stream group.

Arn -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Format example: `arn:aws:gameliftstreams:us-west-2:123456789012:application/a-9ZY8X7Wv6` .

Id -> (string)

An ID that uniquely identifies the application resource. For example: `a-9ZY8X7Wv6` .

Description -> (string)

A descriptive label for the stream group.

Id -> (string)

An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Format example: ARN-`arn:aws:gameliftstreams:us-west-2:123456789012:streamgroup/sg-1AB2C3De4` or ID-`sg-1AB2C3De4` .

LastUpdatedAt -> (timestamp)

A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).

Status -> (string)

The current status of the stream group resource. Possible statuses include the following:

- `ACTIVATING` : The stream group is deploying and isnât ready to host streams.
- `ACTIVE` : The stream group is ready to host streams.
- `ACTIVE_WITH_ERRORS` : One or more locations in the stream group are in an error state. Verify the details of individual locations and remove any locations which are in error.
- `ERROR` : An error occurred when the stream group deployed. See `StatusReason` for more information.
- `DELETING` : Amazon GameLift Streams is in the process of deleting the stream group.
- `UPDATING_LOCATIONS` : One or more locations in the stream group are in the process of updating (either activating or deleting).

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

NextToken -> (string)

A token that marks the start of the next sequential page of results. If an operation doesnât return a token, youâve reached the end of the list.