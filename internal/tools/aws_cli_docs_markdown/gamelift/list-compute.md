# list-computeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-compute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/list-compute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# list-compute

## Description

Retrieves information on the compute resources in an Amazon GameLift fleet. Use the pagination parameters to retrieve results in a set of sequential pages.

**Request options**

- Retrieve a list of all computes in a fleet. Specify a fleet ID.
- Retrieve a list of all computes in a specific fleet location. Specify a fleet ID and location.

**Results**

If successful, this operation returns information on a set of computes. Depending on the type of fleet, the result includes the following information:

- For a managed EC2 fleet (compute type `EC2` ), this operation returns information about the EC2 instance. Compute names are EC2 instance IDs.
- For an Anywhere fleet (compute type `ANYWHERE` ), this operation returns compute names and details from when the compute was registered with `RegisterCompute` . This includes `GameLiftServiceSdkEndpoint` or `GameLiftAgentEndpoint` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/ListCompute)

`list-compute` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ComputeList`

## Synopsis

```
list-compute
--fleet-id <value>
[--location <value>]
[--container-group-definition-name <value>]
[--compute-status <value>]
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

`--fleet-id` (string)

A unique identifier for the fleet to retrieve compute resources for.

`--location` (string)

The name of a location to retrieve compute resources for. For an Amazon GameLift Anywhere fleet, use a custom location. For a managed fleet, provide a Amazon Web Services Region or Local Zone code (for example: `us-west-2` or `us-west-2-lax-1` ).

`--container-group-definition-name` (string)

For computes in a managed container fleet, the name of the deployed container group definition.

`--compute-status` (string)

The status of computes in a managed container fleet, based on the success of the latest update deployment.

- `ACTIVE` â The compute is deployed with the correct container definitions. It is ready to process game servers and host game sessions.
- `IMPAIRED` â An update deployment to the compute failed, and the compute is deployed with incorrect container definitions.

Possible values:

- `ACTIVE`
- `IMPAIRED`

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

ComputeList -> (list)

A list of compute resources in the specified fleet.

(structure)

An Amazon GameLift compute resource for hosting your game servers. Computes in an Amazon GameLift fleet differs depending on the fleetâs compute type property as follows:

- For managed EC2 fleets, a compute is an EC2 instance.
- For Anywhere fleets, a compute is a computing resource that you provide and is registered to the fleet.

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

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.