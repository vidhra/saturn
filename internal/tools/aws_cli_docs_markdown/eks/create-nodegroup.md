# create-nodegroupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-nodegroup.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# create-nodegroup

## Description

Creates a managed node group for an Amazon EKS cluster.

You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster, unless you deploy a custom AMI using a launch template.

For later updates, you will only be able to update a node group using a launch template only if it was originally deployed with a launch template. Additionally, the launch template ID or name must match what was used when the node group was created. You can update the launch template version with necessary changes. For more information about using launch templates, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) .

An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by Amazon Web Services for an Amazon EKS cluster. For more information, see [Managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) in the *Amazon EKS User Guide* .

### Note

Windows AMI types are only supported for commercial Amazon Web Services Regions that support Windows on Amazon EKS.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateNodegroup)

## Synopsis

```
create-nodegroup
--cluster-name <value>
--nodegroup-name <value>
[--scaling-config <value>]
[--disk-size <value>]
--subnets <value>
[--instance-types <value>]
[--ami-type <value>]
[--remote-access <value>]
--node-role <value>
[--labels <value>]
[--taints <value>]
[--tags <value>]
[--client-request-token <value>]
[--launch-template <value>]
[--update-config <value>]
[--node-repair-config <value>]
[--capacity-type <value>]
[--release-version <value>]
[--kubernetes-version <value>]
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

`--cluster-name` (string)

The name of your cluster.

`--nodegroup-name` (string)

The unique name to give your node group.

`--scaling-config` (structure)

The scaling configuration details for the Auto Scaling group that is created for your node group.

minSize -> (integer)

The minimum number of nodes that the managed node group can scale in to.

maxSize -> (integer)

The maximum number of nodes that the managed node group can scale out to. For information about the maximum number that you can specify, see [Amazon EKS service quotas](https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html) in the *Amazon EKS User Guide* .

desiredSize -> (integer)

The current number of nodes that the managed node group should maintain.

### Warning

If you use the Kubernetes [Cluster Autoscaler](https://github.com/kubernetes/autoscaler#kubernetes-autoscaler) , you shouldnât change the `desiredSize` value directly, as this can cause the Cluster Autoscaler to suddenly scale up or scale down.

Whenever this parameter changes, the number of worker nodes in the node group is updated to the specified size. If this parameter is given a value that is smaller than the current number of running worker nodes, the necessary number of worker nodes are terminated to match the given value. When using CloudFormation, no action occurs if you remove this parameter from your CFN template.

This parameter can be different from `minSize` in some cases, such as when starting with extra hosts for testing. This parameter can also be different when you want to start with an estimated number of needed hosts, but let the Cluster Autoscaler reduce the number if there are too many. When the Cluster Autoscaler is used, the `desiredSize` parameter is altered by the Cluster Autoscaler (but can be out-of-date for short periods of time). the Cluster Autoscaler doesnât scale a managed node group lower than `minSize` or higher than `maxSize` .

Shorthand Syntax:

```
minSize=integer,maxSize=integer,desiredSize=integer
```

JSON Syntax:

```
{
  "minSize": integer,
  "maxSize": integer,
  "desiredSize": integer
}
```

`--disk-size` (integer)

The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB for Linux and Bottlerocket. The default disk size is 50 GiB for Windows. If you specify `launchTemplate` , then donât specify `diskSize` , or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

`--subnets` (list)

The subnets to use for the Auto Scaling group that is created for your node group. If you specify `launchTemplate` , then donât specify `` [SubnetId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html) `` in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--instance-types` (list)

Specify the instance types for a node group. If you specify a GPU instance type, make sure to also specify an applicable GPU AMI type with the `amiType` parameter. If you specify `launchTemplate` , then you can specify zero or one instance type in your launch template *or* you can specify 0-20 instance types for `instanceTypes` . If however, you specify an instance type in your launch template *and* specify any `instanceTypes` , the node group deployment will fail. If you donât specify an instance type in a launch template or for `instanceTypes` , then `t3.medium` is used, by default. If you specify `Spot` for `capacityType` , then we recommend specifying multiple values for `instanceTypes` . For more information, see [Managed node group capacity types](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types) and [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--ami-type` (string)

The AMI type for your node group. If you specify `launchTemplate` , and your launch template uses a custom AMI, then donât specify `amiType` , or the node group deployment will fail. If your launch template uses a Windows custom AMI, then add `eks:kube-proxy-windows` to your Windows nodes `rolearn` in the `aws-auth` `ConfigMap` . For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

Possible values:

- `AL2_x86_64`
- `AL2_x86_64_GPU`
- `AL2_ARM_64`
- `CUSTOM`
- `BOTTLEROCKET_ARM_64`
- `BOTTLEROCKET_x86_64`
- `BOTTLEROCKET_ARM_64_FIPS`
- `BOTTLEROCKET_x86_64_FIPS`
- `BOTTLEROCKET_ARM_64_NVIDIA`
- `BOTTLEROCKET_x86_64_NVIDIA`
- `WINDOWS_CORE_2019_x86_64`
- `WINDOWS_FULL_2019_x86_64`
- `WINDOWS_CORE_2022_x86_64`
- `WINDOWS_FULL_2022_x86_64`
- `AL2023_x86_64_STANDARD`
- `AL2023_ARM_64_STANDARD`
- `AL2023_x86_64_NEURON`
- `AL2023_x86_64_NVIDIA`
- `AL2023_ARM_64_NVIDIA`

`--remote-access` (structure)

The remote access configuration to use with your node group. For Linux, the protocol is SSH. For Windows, the protocol is RDP. If you specify `launchTemplate` , then donât specify `remoteAccess` , or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

ec2SshKey -> (string)

The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group. For more information, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances* . For Windows, an Amazon EC2 SSH key is used to obtain the RDP password. For more information, see [Amazon EC2 key pairs and Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances* .

sourceSecurityGroups -> (list)

The security group IDs that are allowed SSH access (port 22) to the nodes. For Windows, the port is 3389. If you specify an Amazon EC2 SSH key but donât specify a source security group when you create a managed node group, then the port on the nodes is opened to the internet (`0.0.0.0/0` ). For more information, see [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon Virtual Private Cloud User Guide* .

(string)

Shorthand Syntax:

```
ec2SshKey=string,sourceSecurityGroups=string,string
```

JSON Syntax:

```
{
  "ec2SshKey": "string",
  "sourceSecurityGroups": ["string", ...]
}
```

`--node-role` (string)

The Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node `kubelet` daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the * *Amazon EKS User Guide* * . If you specify `launchTemplate` , then donât specify `` [IamInstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html) `` in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

`--labels` (map)

The Kubernetes `labels` to apply to the nodes in the node group when they are created.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--taints` (list)

The Kubernetes taints to be applied to the nodes in the node group. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) .

(structure)

A property that allows a node to repel a `Pod` . For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) in the *Amazon EKS User Guide* .

key -> (string)

The key of the taint.

value -> (string)

The value of the taint.

effect -> (string)

The effect of the taint.

Shorthand Syntax:

```
key=string,value=string,effect=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string",
    "effect": "NO_SCHEDULE"|"NO_EXECUTE"|"PREFER_NO_SCHEDULE"
  }
  ...
]
```

`--tags` (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--launch-template` (structure)

An object representing a node groupâs launch template specification. When using this object, donât directly specify `instanceTypes` , `diskSize` , or `remoteAccess` . You cannot later specify a different launch template ID or name than what was used to create the node group.

Make sure that the launch template meets the requirements in `launchTemplateSpecification` . Also refer to [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

name -> (string)

The name of the launch template.

You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.

version -> (string)

The version number of the launch template to use. If no version is specified, then the templateâs default version is used. You can use a different version for node group updates.

id -> (string)

The ID of the launch template.

You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.

Shorthand Syntax:

```
name=string,version=string,id=string
```

JSON Syntax:

```
{
  "name": "string",
  "version": "string",
  "id": "string"
}
```

`--update-config` (structure)

The node group update configuration.

maxUnavailable -> (integer)

The maximum number of nodes unavailable at once during a version update. Nodes are updated in parallel. This value or `maxUnavailablePercentage` is required to have a value.The maximum number is 100.

maxUnavailablePercentage -> (integer)

The maximum percentage of nodes unavailable during a version update. This percentage of nodes are updated in parallel, up to 100 nodes at once. This value or `maxUnavailable` is required to have a value.

updateStrategy -> (string)

The configuration for the behavior to follow during a node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an ` `UpdateNodegroupVersion` [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion).html`__ action.

An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. The *update strategy* changes the managed node update behavior of the managed node group for each quantity. The *default* strategy has guardrails to protect you from misconfiguration and launches the new instances first, before terminating the old instances. The *minimal* strategy removes the guardrails and terminates the old instances before launching the new instances. This minimal strategy is useful in scenarios where you are constrained to resources or costs (for example, with hardware accelerators such as GPUs).

Shorthand Syntax:

```
maxUnavailable=integer,maxUnavailablePercentage=integer,updateStrategy=string
```

JSON Syntax:

```
{
  "maxUnavailable": integer,
  "maxUnavailablePercentage": integer,
  "updateStrategy": "DEFAULT"|"MINIMAL"
}
```

`--node-repair-config` (structure)

The node auto repair configuration for the node group.

enabled -> (boolean)

Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default.

Shorthand Syntax:

```
enabled=boolean
```

JSON Syntax:

```
{
  "enabled": true|false
}
```

`--capacity-type` (string)

The capacity type for your node group.

Possible values:

- `ON_DEMAND`
- `SPOT`
- `CAPACITY_BLOCK`

`--release-version` (string)

The AMI version of the Amazon EKS optimized AMI to use with your node group. By default, the latest available AMI version for the node groupâs current Kubernetes version is used. For information about Linux versions, see [Amazon EKS optimized Amazon Linux AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html) in the *Amazon EKS User Guide* . Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see [Amazon EKS optimized Windows AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html) in the *Amazon EKS User Guide* .

If you specify `launchTemplate` , and your launch template uses a custom AMI, then donât specify `releaseVersion` , or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

`--kubernetes-version` (string)

The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value. If you specify `launchTemplate` , and your launch template uses a custom AMI, then donât specify `version` , or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide* .

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

**Example 1: Creates a managed node group for an Amazon EKS cluster**

The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster.

```
aws eks create-nodegroup \
    --cluster-name my-eks-cluster \
    --nodegroup-name my-eks-nodegroup \
    --node-role arn:aws:iam::111122223333:role/role-name \
    --subnets "subnet-0e2907431c9988b72" "subnet-04ad87f71c6e5ab4d" "subnet-09d912bb63ef21b9a" \
    --scaling-config minSize=1,maxSize=3,desiredSize=1 \
    --region us-east-2
```

Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/bac7550f-b8b8-5fbb-4f3e-7502a931119e",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T13:19:32.260000-04:00",
        "modifiedAt": "2024-04-04T13:19:32.260000-04:00",
        "status": "CREATING",
        "capacityType": "ON_DEMAND",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 3,
            "desiredSize": 1
        },
        "instanceTypes": [
            "t3.medium"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72, subnet-04ad87f71c6e5ab4d, subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "diskSize": 20,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 1
        },
        "tags": {}
    }
}
```

For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.

**Example 2: Creates a managed node group for an Amazon EKS cluster with custom instance-types and disk-size**

The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster with custom instance-types and disk-size.

```
aws eks create-nodegroup \
    --cluster-name my-eks-cluster \
    --nodegroup-name my-eks-nodegroup \
    --node-role arn:aws:iam::111122223333:role/role-name \
    --subnets "subnet-0e2907431c9988b72" "subnet-04ad87f71c6e5ab4d" "subnet-09d912bb63ef21b9a" \
    --scaling-config minSize=1,maxSize=3,desiredSize=1 \
    --capacity-type ON_DEMAND \
    --instance-types 'm5.large' \
    --disk-size 50 \
    --region us-east-2
```

Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/c0c7551b-e4f9-73d9-992c-a450fdb82322",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T13:46:07.595000-04:00",
        "modifiedAt": "2024-04-04T13:46:07.595000-04:00",
        "status": "CREATING",
        "capacityType": "ON_DEMAND",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 3,
            "desiredSize": 1
        },
        "instanceTypes": [
            "m5.large"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "diskSize": 50,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 1
        },
        "tags": {}
    }
}
```

For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.

**Example 3: Creates a managed node group for an Amazon EKS cluster with custom instance-types, disk-size, ami-type, capacity-type, update-config, labels, taints and tags.**

The following `create-nodegroup` example creates a managed node group for an Amazon EKS cluster with custom instance-types, disk-size, ami-type, capacity-type, update-config, labels, taints and tags.

```
aws eks create-nodegroup  \
    --cluster-name my-eks-cluster \
    --nodegroup-name my-eks-nodegroup \
    --node-role arn:aws:iam::111122223333:role/role-name \
    --subnets "subnet-0e2907431c9988b72" "subnet-04ad87f71c6e5ab4d" "subnet-09d912bb63ef21b9a" \
    --scaling-config minSize=1,maxSize=5,desiredSize=4 \
    --instance-types 't3.large' \
    --disk-size 50 \
    --ami-type AL2_x86_64 \
    --capacity-type SPOT \
    --update-config maxUnavailable=2 \
    --labels '{"my-eks-nodegroup-label-1": "value-1" , "my-eks-nodegroup-label-2": "value-2"}' \
    --taints '{"key": "taint-key-1" , "value": "taint-value-1", "effect": "NO_EXECUTE"}' \
    --tags '{"my-eks-nodegroup-key-1": "value-1" , "my-eks-nodegroup-key-2": "value-2"}'
```

Output:

```
{
    "nodegroup": {
        "nodegroupName": "my-eks-nodegroup",
        "nodegroupArn": "arn:aws:eks:us-east-2:111122223333:nodegroup/my-eks-cluster/my-eks-nodegroup/88c75524-97af-0cb9-a9c5-7c0423ab5314",
        "clusterName": "my-eks-cluster",
        "version": "1.26",
        "releaseVersion": "1.26.12-20240329",
        "createdAt": "2024-04-04T14:05:07.940000-04:00",
        "modifiedAt": "2024-04-04T14:05:07.940000-04:00",
        "status": "CREATING",
        "capacityType": "SPOT",
        "scalingConfig": {
            "minSize": 1,
            "maxSize": 5,
            "desiredSize": 4
        },
        "instanceTypes": [
            "t3.large"
        ],
        "subnets": [
            "subnet-0e2907431c9988b72",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-09d912bb63ef21b9a"
        ],
        "amiType": "AL2_x86_64",
        "nodeRole": "arn:aws:iam::111122223333:role/role-name",
        "labels": {
            "my-eks-nodegroup-label-2": "value-2",
            "my-eks-nodegroup-label-1": "value-1"
        },
        "taints": [
            {
                "key": "taint-key-1",
                "value": "taint-value-1",
                "effect": "NO_EXECUTE"
            }
        ],
        "diskSize": 50,
        "health": {
            "issues": []
        },
        "updateConfig": {
            "maxUnavailable": 2
        },
        "tags": {
            "my-eks-nodegroup-key-1": "value-1",
            "my-eks-nodegroup-key-2": "value-2"
        }
    }
}
```

For more information, see [Creating a managed node group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html) in the *Amazon EKS User Guide*.

## Output

nodegroup -> (structure)

The full description of your new node group.

nodegroupName -> (string)

The name associated with an Amazon EKS managed node group.

nodegroupArn -> (string)

The Amazon Resource Name (ARN) associated with the managed node group.

clusterName -> (string)

The name of your cluster.

version -> (string)

The Kubernetes version of the managed node group.

releaseVersion -> (string)

If the node group was deployed using a launch template with a custom AMI, then this is the AMI ID that was specified in the launch template. For node groups that werenât deployed using a launch template, this is the version of the Amazon EKS optimized AMI that the node group was deployed with.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

modifiedAt -> (timestamp)

The Unix epoch timestamp for the last modification to the object.

status -> (string)

The current status of the managed node group.

capacityType -> (string)

The capacity type of your managed node group.

scalingConfig -> (structure)

The scaling configuration details for the Auto Scaling group that is associated with your node group.

minSize -> (integer)

The minimum number of nodes that the managed node group can scale in to.

maxSize -> (integer)

The maximum number of nodes that the managed node group can scale out to. For information about the maximum number that you can specify, see [Amazon EKS service quotas](https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html) in the *Amazon EKS User Guide* .

desiredSize -> (integer)

The current number of nodes that the managed node group should maintain.

### Warning

If you use the Kubernetes [Cluster Autoscaler](https://github.com/kubernetes/autoscaler#kubernetes-autoscaler) , you shouldnât change the `desiredSize` value directly, as this can cause the Cluster Autoscaler to suddenly scale up or scale down.

Whenever this parameter changes, the number of worker nodes in the node group is updated to the specified size. If this parameter is given a value that is smaller than the current number of running worker nodes, the necessary number of worker nodes are terminated to match the given value. When using CloudFormation, no action occurs if you remove this parameter from your CFN template.

This parameter can be different from `minSize` in some cases, such as when starting with extra hosts for testing. This parameter can also be different when you want to start with an estimated number of needed hosts, but let the Cluster Autoscaler reduce the number if there are too many. When the Cluster Autoscaler is used, the `desiredSize` parameter is altered by the Cluster Autoscaler (but can be out-of-date for short periods of time). the Cluster Autoscaler doesnât scale a managed node group lower than `minSize` or higher than `maxSize` .

instanceTypes -> (list)

If the node group wasnât deployed with a launch template, then this is the instance type that is associated with the node group. If the node group was deployed with a launch template, then this is `null` .

(string)

subnets -> (list)

The subnets that were specified for the Auto Scaling group that is associated with your node group.

(string)

remoteAccess -> (structure)

If the node group wasnât deployed with a launch template, then this is the remote access configuration that is associated with the node group. If the node group was deployed with a launch template, then this is `null` .

ec2SshKey -> (string)

The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group. For more information, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances* . For Windows, an Amazon EC2 SSH key is used to obtain the RDP password. For more information, see [Amazon EC2 key pairs and Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html) in the *Amazon Elastic Compute Cloud User Guide for Windows Instances* .

sourceSecurityGroups -> (list)

The security group IDs that are allowed SSH access (port 22) to the nodes. For Windows, the port is 3389. If you specify an Amazon EC2 SSH key but donât specify a source security group when you create a managed node group, then the port on the nodes is opened to the internet (`0.0.0.0/0` ). For more information, see [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon Virtual Private Cloud User Guide* .

(string)

amiType -> (string)

If the node group was deployed using a launch template with a custom AMI, then this is `CUSTOM` . For node groups that werenât deployed using a launch template, this is the AMI type that was specified in the node group configuration.

nodeRole -> (string)

The IAM role associated with your node group. The Amazon EKS node `kubelet` daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies.

labels -> (map)

The Kubernetes `labels` applied to the nodes in the node group.

### Note

Only `labels` that are applied with the Amazon EKS API are shown here. There may be other Kubernetes `labels` applied to the nodes in this group.

key -> (string)

value -> (string)

taints -> (list)

The Kubernetes taints to be applied to the nodes in the node group when they are created. Effect is one of `No_Schedule` , `Prefer_No_Schedule` , or `No_Execute` . Kubernetes taints can be used together with tolerations to control how workloads are scheduled to your nodes. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) .

(structure)

A property that allows a node to repel a `Pod` . For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html) in the *Amazon EKS User Guide* .

key -> (string)

The key of the taint.

value -> (string)

The value of the taint.

effect -> (string)

The effect of the taint.

resources -> (structure)

The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.

autoScalingGroups -> (list)

The Auto Scaling groups associated with the node group.

(structure)

An Auto Scaling group that is associated with an Amazon EKS managed node group.

name -> (string)

The name of the Auto Scaling group associated with an Amazon EKS managed node group.

remoteAccessSecurityGroup -> (string)

The remote access security group associated with the node group. This security group controls SSH access to the nodes.

diskSize -> (integer)

If the node group wasnât deployed with a launch template, then this is the disk size in the node group configuration. If the node group was deployed with a launch template, then this is `null` .

health -> (structure)

The health status of the node group. If there are issues with your node groupâs health, they are listed here.

issues -> (list)

Any issues that are associated with the node group.

(structure)

An object representing an issue with an Amazon EKS resource.

code -> (string)

A brief description of the error.

- **AccessDenied** : Amazon EKS or one or more of your managed nodes is failing to authenticate or authorize with your Kubernetes cluster API server.
- **AsgInstanceLaunchFailures** : Your Auto Scaling group is experiencing failures while attempting to launch instances.
- **AutoScalingGroupNotFound** : We couldnât find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.
- **ClusterUnreachable** : Amazon EKS or one or more of your managed nodes is unable to to communicate with your Kubernetes cluster API server. This can happen if there are network disruptions or if API servers are timing out processing requests.
- **Ec2InstanceTypeDoesNotExist** : One or more of the supplied Amazon EC2 instance types do not exist. Amazon EKS checked for the instance types that you provided in this Amazon Web Services Region, and one or more arenât available.
- **Ec2LaunchTemplateNotFound** : We couldnât find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.
- **Ec2LaunchTemplateVersionMismatch** : The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.
- **Ec2SecurityGroupDeletionFailure** : We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.
- **Ec2SecurityGroupNotFound** : We couldnât find the cluster security group for the cluster. You must recreate your cluster.
- **Ec2SubnetInvalidConfiguration** : One or more Amazon EC2 subnets specified for a node group do not automatically assign public IP addresses to instances launched into it. If you want your instances to be assigned a public IP address, then you need to enable the `auto-assign public IP address` setting for the subnet. See Modifying the public ``IPv4` addressing attribute for your subnet <[https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip)>`__ in the *Amazon VPC User Guide* .
- **IamInstanceProfileNotFound** : We couldnât find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.
- **IamNodeRoleNotFound** : We couldnât find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.
- **InstanceLimitExceeded** : Your Amazon Web Services account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.
- **InsufficientFreeAddresses** : One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.
- **InternalFailure** : These errors are usually caused by an Amazon EKS server-side issue.
- **NodeCreationFailure** : Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient [node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) permissions or lack of outbound internet access for the nodes.

message -> (string)

The error message associated with the issue.

resourceIds -> (list)

The Amazon Web Services resources that are afflicted by this issue.

(string)

updateConfig -> (structure)

The node group update configuration.

maxUnavailable -> (integer)

The maximum number of nodes unavailable at once during a version update. Nodes are updated in parallel. This value or `maxUnavailablePercentage` is required to have a value.The maximum number is 100.

maxUnavailablePercentage -> (integer)

The maximum percentage of nodes unavailable during a version update. This percentage of nodes are updated in parallel, up to 100 nodes at once. This value or `maxUnavailable` is required to have a value.

updateStrategy -> (string)

The configuration for the behavior to follow during a node group version update of this managed node group. You choose between two possible strategies for replacing nodes during an ` `UpdateNodegroupVersion` [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateNodegroupVersion).html`__ action.

An Amazon EKS managed node group updates by replacing nodes with new nodes of newer AMI versions in parallel. The *update strategy* changes the managed node update behavior of the managed node group for each quantity. The *default* strategy has guardrails to protect you from misconfiguration and launches the new instances first, before terminating the old instances. The *minimal* strategy removes the guardrails and terminates the old instances before launching the new instances. This minimal strategy is useful in scenarios where you are constrained to resources or costs (for example, with hardware accelerators such as GPUs).

nodeRepairConfig -> (structure)

The node auto repair configuration for the node group.

enabled -> (boolean)

Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default.

launchTemplate -> (structure)

If a launch template was used to create the node group, then this is the launch template that was used.

name -> (string)

The name of the launch template.

You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.

version -> (string)

The version number of the launch template to use. If no version is specified, then the templateâs default version is used. You can use a different version for node group updates.

id -> (string)

The ID of the launch template.

You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.

tags -> (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).