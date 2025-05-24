# describe-computeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-compute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-compute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# describe-compute

## Description

Retrieves properties for a specific compute resource in an Amazon GameLift fleet. You can list all computes in a fleet by calling [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html) .

**Request options**

Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.

- For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.
- For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name.
- For a compute in an Anywhere fleet, provide a registered compute name. Anywhere fleet computes are created when you register a hosting resource with the fleet.

**Results**

If successful, this operation returns details for the requested compute resource. Depending on the fleetâs compute type, the result includes the following information:

- For a managed EC2 fleet, this operation returns information about the EC2 instance.
- For an Anywhere fleet, this operation returns information about the registered compute.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeCompute)

## Synopsis

```
describe-compute
--fleet-id <value>
--compute-name <value>
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

`--fleet-id` (string)

A unique identifier for the fleet that the compute belongs to. You can use either the fleet ID or ARN value.

`--compute-name` (string)

The unique identifier of the compute resource to retrieve properties for. For a managed container fleet or Anywhere fleet, use a compute name. For an EC2 fleet, use an instance ID. To retrieve a fleetâs compute identifiers, call [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html) .

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

Compute -> (structure)

The set of properties for the requested compute resource.

FleetId -> (string)

A unique identifier for the fleet that the compute belongs to.

FleetArn -> (string)

The Amazon Resource Name (ARN) of the fleet that the compute belongs to.

ComputeName -> (string)

A descriptive label for the compute resource. For instances in a managed EC2 fleet, the compute name is the same value as the `InstanceId` ID.

ComputeArn -> (string)

The ARN that is assigned to a compute resource and uniquely identifies it. ARNs are unique across locations. Instances in managed EC2 fleets are not assigned a Compute ARN.

IpAddress -> (string)

The IP address of a compute resource. Amazon GameLift requires a DNS name or IP address for a compute.

DnsName -> (string)

The DNS name of a compute resource. Amazon GameLift requires a DNS name or IP address for a compute.

ComputeStatus -> (string)

Current status of the compute. A compute must have an `ACTIVE` status to host game sessions.

Location -> (string)

The name of the custom location you added to the fleet that this compute resource resides in.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

OperatingSystem -> (string)

The type of operating system on the compute resource.

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

Type -> (string)

The Amazon EC2 instance type that the fleet uses. For registered computes in an Amazon GameLift Anywhere fleet, this property is empty.

GameLiftServiceSdkEndpoint -> (string)

The Amazon GameLift SDK endpoint connection for a registered compute resource in an Anywhere fleet. The game servers on the compute use this endpoint to connect to the Amazon GameLift service.

GameLiftAgentEndpoint -> (string)

The endpoint of the Amazon GameLift Agent.

InstanceId -> (string)

The `InstanceID` of the EC2 instance that is hosting the compute.

ContainerAttributes -> (list)

A set of attributes for each container in the compute.

(structure)

A unique identifier for a container in a container fleet compute.

**Returned by:** [DescribeCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute.html)

ContainerName -> (string)

The identifier for a container thatâs running in a compute.

ContainerRuntimeId -> (string)

The runtime ID for the container thatâs running in a compute. This value is unique within the compute.

GameServerContainerGroupDefinitionArn -> (string)

The game server container group definition for the compute.