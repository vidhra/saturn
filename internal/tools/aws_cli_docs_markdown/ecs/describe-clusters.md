# describe-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/describe-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# describe-clusters

## Description

Describes one or more of your clusters.

For CLI examples, see [describe-clusters.rst](https://github.com/aws/aws-cli/blob/develop/awscli/examples/ecs/describe-clusters.rst) on GitHub.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ecs-2014-11-13/DescribeClusters)

## Synopsis

```
describe-clusters
[--clusters <value>]
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

`--clusters` (list)

A list of up to 100 cluster names or full cluster Amazon Resource Name (ARN) entries. If you do not specify a cluster, the default cluster is assumed.

(string)

Syntax:

```
"string" "string" ...
```

`--include` (list)

Determines whether to include additional information about the clusters in the response. If this field is omitted, this information isnât included.

If `ATTACHMENTS` is specified, the attachments for the container instances or tasks within the cluster are included, for example the capacity providers.

If `SETTINGS` is specified, the settings for the cluster are included.

If `CONFIGURATIONS` is specified, the configuration for the cluster is included.

If `STATISTICS` is specified, the task and service count is included, separated by launch type.

If `TAGS` is specified, the metadata tags associated with the cluster are included.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ATTACHMENTS
  CONFIGURATIONS
  SETTINGS
  STATISTICS
  TAGS
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

**Example 1: To describe a cluster**

The following `describe-clusters` example retrieves details about the specified cluster.

```
aws ecs describe-clusters \
    --cluster default
```

Output:

```
{
    "clusters": [
        {
            "status": "ACTIVE",
            "clusterName": "default",
            "registeredContainerInstancesCount": 0,
            "pendingTasksCount": 0,
            "runningTasksCount": 0,
            "activeServicesCount": 1,
            "clusterArn": "arn:aws:ecs:us-west-2:123456789012:cluster/default"
        }
    ],
    "failures": []
}
```

For more information, see [Amazon ECS Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_clusters.html) in the *Amazon ECS Developer Guide*.

**Example 2: To describe a cluster with the attachment option**

The following `describe-clusters` example specifies the ATTACHMENTS option. It retrieves details about the specified cluster and a list of resources attached to the cluster in the form of attachments. When using a capacity provider with a cluster, the resources, either AutoScaling plans or scaling policies, will be represented as asp or as_policy ATTACHMENTS.

```
aws ecs describe-clusters \
    --include ATTACHMENTS \
    --clusters sampleCluster
```

Output:

```
{
    "clusters": [
        {
            "clusterArn": "arn:aws:ecs:af-south-1:123456789222:cluster/sampleCluster",
            "clusterName": "sampleCluster",
            "status": "ACTIVE",
            "registeredContainerInstancesCount": 0,
            "runningTasksCount": 0,
            "pendingTasksCount": 0,
            "activeServicesCount": 0,
            "statistics": [],
            "tags": [],
            "settings": [],
            "capacityProviders": [
                "sampleCapacityProvider"
            ],
            "defaultCapacityProviderStrategy": [],
            "attachments": [
                {
                    "id": "a1b2c3d4-5678-901b-cdef-EXAMPLE22222",
                    "type": "as_policy",
                    "status": "CREATED",
                    "details": [
                        {
                            "name": "capacityProviderName",
                            "value": "sampleCapacityProvider"
                        },
                        {
                            "name": "scalingPolicyName",
                            "value": "ECSManagedAutoScalingPolicy-3048e262-fe39-4eaf-826d-6f975d303188"
                        }
                    ]
                }
            ],
            "attachmentsStatus": "UPDATE_COMPLETE"
        }
    ],
    "failures": []
}
```

For more information, see [Amazon ECS Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_clusters.html) in the *Amazon ECS Developer Guide*.

## Output

clusters -> (list)

The list of clusters.

(structure)

A regional grouping of one or more container instances where you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.

clusterArn -> (string)

The Amazon Resource Name (ARN) that identifies the cluster. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide* .

clusterName -> (string)

A user-generated string that you use to identify your cluster.

configuration -> (structure)

The execute command and managed storage configuration for the cluster.

executeCommandConfiguration -> (structure)

The details of the execute command configuration.

kmsKeyId -> (string)

Specify an Key Management Service key ID to encrypt the data between the local client and the container.

logging -> (string)

The log setting to use for redirecting logs for your execute command results. The following log settings are available.

- `NONE` : The execute command session is not logged.
- `DEFAULT` : The `awslogs` configuration in the task definition is used. If no logging parameter is specified, it defaults to this value. If no `awslogs` log driver is configured in the task definition, the output wonât be logged.
- `OVERRIDE` : Specify the logging details as a part of `logConfiguration` . If the `OVERRIDE` logging option is specified, the `logConfiguration` is required.

logConfiguration -> (structure)

The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket. When `logging=OVERRIDE` is specified, a `logConfiguration` must be provided.

cloudWatchLogGroupName -> (string)

The name of the CloudWatch log group to send logs to.

### Note

The CloudWatch log group must already be created.

cloudWatchEncryptionEnabled -> (boolean)

Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off.

s3BucketName -> (string)

The name of the S3 bucket to send logs to.

### Note

The S3 bucket must already be created.

s3EncryptionEnabled -> (boolean)

Determines whether to use encryption on the S3 logs. If not specified, encryption is not used.

s3KeyPrefix -> (string)

An optional folder in the S3 bucket to place logs in.

managedStorageConfiguration -> (structure)

The details of the managed storage configuration.

kmsKeyId -> (string)

Specify a Key Management Service key ID to encrypt Amazon ECS managed storage.

When you specify a `kmsKeyId` , Amazon ECS uses the key to encrypt data volumes managed by Amazon ECS that are attached to tasks in the cluster. The following data volumes are managed by Amazon ECS: Amazon EBS. For more information about encryption of Amazon EBS volumes attached to Amazon ECS tasks, see [Encrypt data stored in Amazon EBS volumes for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html) in the *Amazon Elastic Container Service Developer Guide* .

The key must be a single Region key.

fargateEphemeralStorageKmsKeyId -> (string)

Specify the Key Management Service key ID for Fargate ephemeral storage.

When you specify a `fargateEphemeralStorageKmsKeyId` , Amazon Web Services Fargate uses the key to encrypt data at rest in ephemeral storage. For more information about Fargate ephemeral storage encryption, see [Customer managed keys for Amazon Web Services Fargate ephemeral storage for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html) in the *Amazon Elastic Container Service Developer Guide* .

The key must be a single Region key.

status -> (string)

The status of the cluster. The following are the possible states that are returned.

ACTIVE

The cluster is ready to accept tasks and if applicable you can register container instances with the cluster.

PROVISIONING

The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being created.

DEPROVISIONING

The cluster has capacity providers that are associated with it and the resources needed for the capacity provider are being deleted.

FAILED

The cluster has capacity providers that are associated with it and the resources needed for the capacity provider have failed to create.

INACTIVE

The cluster has been deleted. Clusters with an `INACTIVE` status may remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We donât recommend that you rely on `INACTIVE` clusters persisting.

registeredContainerInstancesCount -> (integer)

The number of container instances registered into the cluster. This includes container instances in both `ACTIVE` and `DRAINING` status.

runningTasksCount -> (integer)

The number of tasks in the cluster that are in the `RUNNING` state.

pendingTasksCount -> (integer)

The number of tasks in the cluster that are in the `PENDING` state.

activeServicesCount -> (integer)

The number of services that are running on the cluster in an `ACTIVE` state. You can view these services with [PListServices](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListServices.html) .

statistics -> (list)

Additional information about your clusters that are separated by launch type. They include the following:

- runningEC2TasksCount
- RunningFargateTasksCount
- pendingEC2TasksCount
- pendingFargateTasksCount
- activeEC2ServiceCount
- activeFargateServiceCount
- drainingEC2ServiceCount
- drainingFargateServiceCount

(structure)

A key-value pair object.

name -> (string)

The name of the key-value pair. For environment variables, this is the name of the environment variable.

value -> (string)

The value of the key-value pair. For environment variables, this is the value of the environment variable.

tags -> (list)

The metadata that you apply to the cluster to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.

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

settings -> (list)

The settings for the cluster. This parameter indicates whether CloudWatch Container Insights is on or off for a cluster.

(structure)

The settings to use when creating a cluster. This parameter is used to turn on CloudWatch Container Insights with enhanced observability or CloudWatch Container Insights for a cluster.

Container Insights with enhanced observability provides all the Container Insights metrics, plus additional task and container metrics. This version supports enhanced observability for Amazon ECS clusters using the Amazon EC2 and Fargate launch types. After you configure Container Insights with enhanced observability on Amazon ECS, Container Insights auto-collects detailed infrastructure telemetry from the cluster level down to the container level in your environment and displays these critical performance data in curated dashboards removing the heavy lifting in observability set-up.

For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html) in the *Amazon Elastic Container Service Developer Guide* .

name -> (string)

The name of the cluster setting. The value is `containerInsights` .

value -> (string)

The value to set for the cluster setting. The supported values are `enhanced` , `enabled` , and `disabled` .

To use Container Insights with enhanced observability, set the `containerInsights` account setting to `enhanced` .

To use Container Insights, set the `containerInsights` account setting to `enabled` .

If a cluster value is specified, it will override the `containerInsights` value set with [PutAccountSetting](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSetting.html) or [PutAccountSettingDefault](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutAccountSettingDefault.html) .

capacityProviders -> (list)

The capacity providers associated with the cluster.

(string)

defaultCapacityProviderStrategy -> (list)

The default capacity provider strategy for the cluster. When services or tasks are run in the cluster with no launch type or capacity provider strategy specified, the default capacity provider strategy is used.

(structure)

The details of a capacity provider strategy. A capacity provider strategy can be set when using the [RunTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html) or [CreateCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) APIs or as the default capacity provider strategy for a cluster with the `CreateCluster` API.

Only capacity providers that are already associated with a cluster and have an `ACTIVE` or `UPDATING` status can be used in a capacity provider strategy. The [PutClusterCapacityProviders](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PutClusterCapacityProviders.html) API is used to associate a capacity provider with a cluster.

If specifying a capacity provider that uses an Auto Scaling group, the capacity provider must already be created. New Auto Scaling group capacity providers can be created with the [CreateClusterCapacityProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateClusterCapacityProvider.html) API operation.

To use a Fargate capacity provider, specify either the `FARGATE` or `FARGATE_SPOT` capacity providers. The Fargate capacity providers are available to all accounts and only need to be associated with a cluster to be used in a capacity provider strategy.

With `FARGATE_SPOT` , you can run interruption tolerant tasks at a rate thatâs discounted compared to the `FARGATE` price. `FARGATE_SPOT` runs tasks on spare compute capacity. When Amazon Web Services needs the capacity back, your tasks are interrupted with a two-minute warning. `FARGATE_SPOT` supports Linux tasks with the X86_64 architecture on platform version 1.3.0 or later. `FARGATE_SPOT` supports Linux tasks with the ARM64 architecture on platform version 1.4.0 or later.

A capacity provider strategy can contain a maximum of 20 capacity providers.

capacityProvider -> (string)

The short name of the capacity provider.

weight -> (integer)

The *weight* value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The `weight` value is taken into consideration after the `base` value, if defined, is satisfied.

If no `weight` value is specified, the default value of `0` is used. When multiple capacity providers are specified within a capacity provider strategy, at least one of the capacity providers must have a weight value greater than zero and any capacity providers with a weight of `0` canât be used to place tasks. If you specify multiple capacity providers in a strategy that all have a weight of `0` , any `RunTask` or `CreateService` actions using the capacity provider strategy will fail.

An example scenario for using weights is defining a strategy that contains two capacity providers and both have a weight of `1` , then when the `base` is satisfied, the tasks will be split evenly across the two capacity providers. Using that same logic, if you specify a weight of `1` for *capacityProviderA* and a weight of `4` for *capacityProviderB* , then for every one task thatâs run using *capacityProviderA* , four tasks would use *capacityProviderB* .

base -> (integer)

The *base* value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a *base* defined. If no value is specified, the default value of `0` is used.

attachments -> (list)

The resources attached to a cluster. When using a capacity provider with a cluster, the capacity provider and associated resources are returned as cluster attachments.

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

attachmentsStatus -> (string)

The status of the capacity providers associated with the cluster. The following are the states that are returned.

UPDATE_IN_PROGRESS

The available capacity providers for the cluster are updating.

UPDATE_COMPLETE

The capacity providers have successfully updated.

UPDATE_FAILED

The capacity provider updates failed.

serviceConnectDefaults -> (structure)

Use this parameter to set a default Service Connect namespace. After you set a default Service Connect namespace, any new services with Service Connect turned on that are created in the cluster are added as client services in the namespace. This setting only applies to new services that set the `enabled` parameter to `true` in the `ServiceConnectConfiguration` . You can set the namespace of each service individually in the `ServiceConnectConfiguration` to override this default parameter.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide* .

namespace -> (string)

The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace. When you create a service and donât specify a Service Connect configuration, this namespace is used.

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