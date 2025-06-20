# register-container-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-container-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-container-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# register-container-instance

## Description

### Note

This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/RegisterContainerInstance)

## Synopsis

```
register-container-instance
[--cluster <value>]
[--instance-identity-document <value>]
[--instance-identity-document-signature <value>]
[--total-resources <value>]
[--version-info <value>]
[--container-instance-arn <value>]
[--attributes <value>]
[--platform-devices <value>]
[--tags <value>]
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

The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.

`--instance-identity-document` (string)

The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: `curl http://169.254.169.254/latest/dynamic/instance-identity/document/`

`--instance-identity-document-signature` (string)

The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: `curl http://169.254.169.254/latest/dynamic/instance-identity/signature/`

`--total-resources` (list)

The resources available on the instance.

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

Shorthand Syntax:

```
name=string,type=string,doubleValue=double,longValue=long,integerValue=integer,stringSetValue=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "type": "string",
    "doubleValue": double,
    "longValue": long,
    "integerValue": integer,
    "stringSetValue": ["string", ...]
  }
  ...
]
```

`--version-info` (structure)

The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.

agentVersion -> (string)

The version number of the Amazon ECS container agent.

agentHash -> (string)

The Git commit hash for the Amazon ECS container agent build on the [amazon-ecs-agent](https://github.com/aws/amazon-ecs-agent/commits/master) GitHub repository.

dockerVersion -> (string)

The Docker version thatâs running on the container instance.

Shorthand Syntax:

```
agentVersion=string,agentHash=string,dockerVersion=string
```

JSON Syntax:

```
{
  "agentVersion": "string",
  "agentHash": "string",
  "dockerVersion": "string"
}
```

`--container-instance-arn` (string)

The ARN of the container instance (if it was previously registered).

`--attributes` (list)

The container instance attributes that this container instance supports.

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

Shorthand Syntax:

```
name=string,value=string,targetType=string,targetId=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "value": "string",
    "targetType": "container-instance",
    "targetId": "string"
  }
  ...
]
```

`--platform-devices` (list)

The devices that are available on the container instance. The only supported device type is a GPU.

(structure)

The devices that are available on the container instance. The only supported device type is a GPU.

id -> (string)

The ID for the GPUs on the container instance. The available GPU IDs can also be obtained on the container instance in the `/var/lib/ecs/gpu/nvidia_gpu_info.json` file.

type -> (string)

The type of device thatâs available on the container instance. The only supported value is `GPU` .

Shorthand Syntax:

```
id=string,type=string ...
```

JSON Syntax:

```
[
  {
    "id": "string",
    "type": "GPU"
  }
  ...
]
```

`--tags` (list)

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

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

containerInstance -> (structure)

The container instance that was registered.

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