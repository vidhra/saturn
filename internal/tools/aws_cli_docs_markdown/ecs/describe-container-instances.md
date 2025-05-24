# describe-container-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-container-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-container-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# describe-container-instances

## Description

Describes one or more container instances. Returns metadata about each container instance requested.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeContainerInstances)

## Synopsis

```
describe-container-instances
[--cluster <value>]
--container-instances <value>
[--include <value>]
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

`--cluster` (string)

The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to describe. If you do not specify a cluster, the default cluster is assumed. This parameter is required if the container instance or container instances you are describing were launched in any cluster other than the default cluster.

`--container-instances` (list)

A list of up to 100 container instance IDs or full Amazon Resource Name (ARN) entries.

(string)

Syntax:

```
"string" "string" ...
```

`--include` (list)

Specifies whether you want to see the resource tags for the container instance. If `TAGS` is specified, the tags are included in the response. If `CONTAINER_INSTANCE_HEALTH` is specified, the container instance health is included in the response. If this field is omitted, tags and container instance health status arenât included in the response.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  TAGS
  CONTAINER_INSTANCE_HEALTH
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe container instance**

The following `describe-container-instances` example retrieves details for a container instance in the `update` cluster, using the container instance UUID as an identifier.

```
aws ecs describe-container-instances \
    --cluster update \
    --container-instances a1b2c3d4-5678-90ab-cdef-11111EXAMPLE
```

Output:

```
{
    "failures": [],
    "containerInstances": [
        {
            "status": "ACTIVE",
            "registeredResources": [
                {
                    "integerValue": 2048,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "CPU",
                    "doubleValue": 0.0
                },
                {
                    "integerValue": 3955,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "MEMORY",
                    "doubleValue": 0.0
                },
                {
                    "name": "PORTS",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET",
                    "integerValue": 0
                }
            ],
            "ec2InstanceId": "i-A1B2C3D4",
            "agentConnected": true,
            "containerInstanceArn": "arn:aws:ecs:us-west-2:123456789012:container-instance/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
            "pendingTasksCount": 0,
            "remainingResources": [
                {
                    "integerValue": 2048,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "CPU",
                    "doubleValue": 0.0
                },
                {
                    "integerValue": 3955,
                    "longValue": 0,
                    "type": "INTEGER",
                    "name": "MEMORY",
                    "doubleValue": 0.0
                },
                {
                    "name": "PORTS",
                    "longValue": 0,
                    "doubleValue": 0.0,
                    "stringSetValue": [
                        "22",
                        "2376",
                        "2375",
                        "51678"
                    ],
                    "type": "STRINGSET",
                    "integerValue": 0
                }
            ],
            "runningTasksCount": 0,
            "versionInfo": {
                "agentVersion": "1.0.0",
                "agentHash": "4023248",
                "dockerVersion": "DockerVersion: 1.5.0"
            }
        }
    ]
}
```

For more information, see [Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html) in the *Amazon ECS Developer Guide*.

## Output

containerInstances -> (list)

The list of container instances.

(structure)

An Amazon EC2 or External instance thatâs running the Amazon ECS agent and has been registered with a cluster.

containerInstanceArn -> (string)

The Amazon Resource Name (ARN) of the container instance. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide* .

ec2InstanceId -> (string)

The ID of the container instance. For Amazon EC2 instances, this value is the Amazon EC2 instance ID. For external instances, this value is the Amazon Web Services Systems Manager managed instance ID.

capacityProviderName -> (string)

The capacity provider thatâs associated with the container instance.

version -> (long)

The version counter for the container instance. Every time a container instance experiences a change that triggers a CloudWatch event, the version counter is incremented. If youâre replicating your Amazon ECS container instance state with CloudWatch Events, you can compare the version of a container instance reported by the Amazon ECS APIs with the version reported in CloudWatch Events for the container instance (inside the `detail` object) to verify that the version in your event stream is current.

versionInfo -> (structure)

The version information for the Amazon ECS container agent and Docker daemon running on the container instance.

agentVersion -> (string)

The version number of the Amazon ECS container agent.

agentHash -> (string)

The Git commit hash for the Amazon ECS container agent build on the [amazon-ecs-agent](https://github.com/aws/amazon-ecs-agent/commits/master) GitHub repository.

dockerVersion -> (string)

The Docker version thatâs running on the container instance.

remainingResources -> (list)

For CPU and memory resource types, this parameter describes the remaining CPU and memory that wasnât already allocated to tasks and is therefore available for new tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent (at instance registration time) and any task containers that have reserved port mappings on the host (with the `host` or `bridge` network mode). Any port thatâs not specified here is available for new tasks.

(structure)

Describes the resources available for a container instance.

name -> (string)

The name of the resource, such as `CPU` , `MEMORY` , `PORTS` , `PORTS_UDP` , or a user-defined resource.

type -> (string)

The type of the resource. Valid values: `INTEGER` , `DOUBLE` , `LONG` , or `STRINGSET` .

doubleValue -> (double)

When the `doubleValue` type is set, the value of the resource must be a double precision floating-point type.

longValue -> (long)

When the `longValue` type is set, the value of the resource must be an extended precision floating-point type.

integerValue -> (integer)

When the `integerValue` type is set, the value of the resource must be an integer.

stringSetValue -> (list)

When the `stringSetValue` type is set, the value of the resource must be a string type.

(string)

registeredResources -> (list)

For CPU and memory resource types, this parameter describes the amount of each resource that was available on the container instance when the container agent registered it with Amazon ECS. This value represents the total amount of CPU and memory that can be allocated on this container instance to tasks. For port resource types, this parameter describes the ports that were reserved by the Amazon ECS container agent when it registered the container instance with Amazon ECS.

(structure)

Describes the resources available for a container instance.

name -> (string)

The name of the resource, such as `CPU` , `MEMORY` , `PORTS` , `PORTS_UDP` , or a user-defined resource.

type -> (string)

The type of the resource. Valid values: `INTEGER` , `DOUBLE` , `LONG` , or `STRINGSET` .

doubleValue -> (double)

When the `doubleValue` type is set, the value of the resource must be a double precision floating-point type.

longValue -> (long)

When the `longValue` type is set, the value of the resource must be an extended precision floating-point type.

integerValue -> (integer)

When the `integerValue` type is set, the value of the resource must be an integer.

stringSetValue -> (list)

When the `stringSetValue` type is set, the value of the resource must be a string type.

(string)

status -> (string)

The status of the container instance. The valid values are `REGISTERING` , `REGISTRATION_FAILED` , `ACTIVE` , `INACTIVE` , `DEREGISTERING` , or `DRAINING` .

If your account has opted in to the `awsvpcTrunking` account setting, then any newly registered container instance will transition to a `REGISTERING` status while the trunk elastic network interface is provisioned for the instance. If the registration fails, the instance will transition to a `REGISTRATION_FAILED` status. You can describe the container instance and see the reason for failure in the `statusReason` parameter. Once the container instance is terminated, the instance transitions to a `DEREGISTERING` status while the trunk elastic network interface is deprovisioned. The instance then transitions to an `INACTIVE` status.

The `ACTIVE` status indicates that the container instance can accept tasks. The `DRAINING` indicates that new tasks arenât placed on the container instance and any service tasks running on the container instance are removed if possible. For more information, see [Container instance draining](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html) in the *Amazon Elastic Container Service Developer Guide* .

statusReason -> (string)

The reason that the container instance reached its current status.

agentConnected -> (boolean)

This parameter returns `true` if the agent is connected to Amazon ECS. An instance with an agent that may be unhealthy or stopped return `false` . Only instances connected to an agent can accept task placement requests.

runningTasksCount -> (integer)

The number of tasks on the container instance that have a desired status (`desiredStatus` ) of `RUNNING` .

pendingTasksCount -> (integer)

The number of tasks on the container instance that are in the `PENDING` status.

agentUpdateStatus -> (string)

The status of the most recent agent update. If an update wasnât ever requested, this value is `NULL` .

attributes -> (list)

The attributes set for the container instance, either by the Amazon ECS container agent at instance registration or manually with the [PutAttributes](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAttributes.html) operation.

(structure)

An attribute is a name-value pair thatâs associated with an Amazon ECS object. Use attributes to extend the Amazon ECS data model by adding custom metadata to your resources. For more information, see [Attributes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes) in the *Amazon Elastic Container Service Developer Guide* .

name -> (string)

The name of the attribute. The `name` must contain between 1 and 128 characters. The name may contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), forward slashes (/), back slashes (), or periods (.).

value -> (string)

The value of the attribute. The `value` must contain between 1 and 128 characters. It can contain letters (uppercase and lowercase), numbers, hyphens (-), underscores (_), periods (.), at signs (@), forward slashes (/), back slashes (), colons (:), or spaces. The value canât start or end with a space.

targetType -> (string)

The type of the target to attach the attribute with. This parameter is required if you use the short form ID for a resource instead of the full ARN.

targetId -> (string)

The ID of the target. You can specify the short form ID for a resource or the full Amazon Resource Name (ARN).

registeredAt -> (timestamp)

The Unix timestamp for the time when the container instance was registered.

attachments -> (list)

The resources attached to a container instance, such as an elastic network interface.

(structure)

An object representing a container instance or task attachment.

id -> (string)

The unique identifier for the attachment.

type -> (string)

The type of the attachment, such as `ElasticNetworkInterface` , `Service Connect` , and `AmazonElasticBlockStorage` .

status -> (string)

The status of the attachment. Valid values are `PRECREATED` , `CREATED` , `ATTACHING` , `ATTACHED` , `DETACHING` , `DETACHED` , `DELETED` , and `FAILED` .

details -> (list)

Details of the attachment.

For elastic network interfaces, this includes the network interface ID, the MAC address, the subnet ID, and the private IPv4 address.

For Service Connect services, this includes `portName` , `clientAliases` , `discoveryName` , and `ingressPortOverride` .

For Elastic Block Storage, this includes `roleArn` , `deleteOnTermination` , `volumeName` , `volumeId` , and `statusReason` (only when the attachment fails to create or attach).

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

tags -> (list)

The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

(structure)

The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length - 128 Unicode characters in UTF-8
- Maximum value length - 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.
- Tag keys and values are case-sensitive.
- Do not use `aws:` , `AWS:` , or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

healthStatus -> (structure)

An object representing the health status of the container instance.

overallStatus -> (string)

The overall health status of the container instance. This is an aggregate status of all container instance health checks.

details -> (list)

An array of objects representing the details of the container instance health status.

(structure)

An object representing the result of a container instance health status check.

type -> (string)

The type of container instance health status that was verified.

status -> (string)

The container instance health status.

lastUpdated -> (timestamp)

The Unix timestamp for when the container instance health status was last updated.

lastStatusChange -> (timestamp)

The Unix timestamp for when the container instance health status last changed.

failures -> (list)

Any failures associated with the call.

(structure)

A failed resource. For a list of common causes, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide* .

arn -> (string)

The Amazon Resource Name (ARN) of the failed resource.

reason -> (string)

The reason for the failure.

detail -> (string)

The details of the failure.