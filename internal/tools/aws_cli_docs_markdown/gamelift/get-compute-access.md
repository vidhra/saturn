# get-compute-accessÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-access.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/get-compute-access.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# get-compute-access

## Description

Requests authorization to remotely connect to a hosting resource in a Amazon GameLift managed fleet. This operation is not used with Amazon GameLift Anywhere fleets.

**Request options**

Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.

- For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.
- For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name.

**Results**

If successful, this operation returns a set of temporary Amazon Web Services credentials, including a two-part access key and a session token.

- With a managed EC2 fleet (where compute type is `EC2` ), use these credentials with Amazon EC2 Systems Manager (SSM) to start a session with the compute. For more details, see [Starting a session (CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#sessions-start-cli) in the *Amazon EC2 Systems Manager User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/GetComputeAccess)

## Synopsis

```
get-compute-access
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

A unique identifier for the fleet that holds the compute resource that you want to connect to. You can use either the fleet ID or ARN value.

`--compute-name` (string)

A unique identifier for the compute resource that you want to connect to. For an EC2 fleet, use an instance ID. For a managed container fleet, use a compute name. You can retrieve a fleetâs compute names by calling [ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html) .

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

FleetId -> (string)

The ID of the fleet that holds the compute resource to be accessed.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` .

ComputeName -> (string)

The identifier of the compute resource to be accessed. This value might be either a compute name or an instance ID.

ComputeArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to an Amazon GameLift compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` .

Credentials -> (structure)

A set of temporary Amazon Web Services credentials for use when connecting to the compute resource with Amazon EC2 Systems Manager (SSM).

AccessKeyId -> (string)

The access key ID that identifies the temporary security credentials.

SecretAccessKey -> (string)

The secret access key that can be used to sign requests.

SessionToken -> (string)

The token that users must pass to the service API to use the temporary credentials.

Target -> (string)

The instance ID where the compute resource is running.

ContainerIdentifiers -> (list)

For a managed container fleet, a list of containers on the compute. Use the container runtime ID with Docker commands to connect to a specific container.

(structure)

A unique identifier for a container in a compute on a managed container fleet instance. This information makes it possible to remotely connect to a specific container on a fleet instance.

**Related to:** [ContainerAttribute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerAttribute.html)

**Use with:** [GetComputeAccess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess.html)

ContainerName -> (string)

The identifier for a container thatâs running in a compute.

ContainerRuntimeId -> (string)

The runtime ID for the container thatâs running in a compute. This value is unique within the compute. It is returned as a `ContainerAttribute` value in a `Compute` object.