# delete-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# delete-cluster

## Description

Deletes an Amazon EKS cluster control plane.

If you have active services in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see [Deleting a cluster](https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html) in the *Amazon EKS User Guide* .

If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see `DeleteNodgroup` and `DeleteFargateProfile` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteCluster)

## Synopsis

```
delete-cluster
--name <value>
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

`--name` (string)

The name of the cluster to delete.

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

**Delete an Amazon EKS cluster control plane**

The following `delete-cluster` example deletes an Amazon EKS cluster control plane.

```
aws eks delete-cluster \
    --name my-eks-cluster
```

Output:

```
{
    "cluster": {
        "name": "my-eks-cluster",
        "arn": "arn:aws:eks:us-east-2:111122223333:cluster/my-eks-cluster",
        "createdAt": "2024-03-14T11:31:44.348000-04:00",
        "version": "1.27",
        "endpoint": "https://DALSJ343KE23J3RN45653DSKJTT647TYD.yl4.us-east-2.eks.amazonaws.com",
        "roleArn": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-cluster-ServiceRole-zMF6CBakwwbW",
        "resourcesVpcConfig": {
            "subnetIds": [
                "subnet-0fb75d2d8401716e7",
                "subnet-02184492f67a3d0f9",
                "subnet-04098063527aab776",
                "subnet-0e2907431c9988b72",
                "subnet-04ad87f71c6e5ab4d",
                "subnet-09d912bb63ef21b9a"
            ],
            "securityGroupIds": [
                "sg-0c1327f6270afbb36"
            ],
            "clusterSecurityGroupId": "sg-01c84d09d70f39a7f",
            "vpcId": "vpc-0012b8e1cc0abb17d",
            "endpointPublicAccess": true,
            "endpointPrivateAccess": true,
            "publicAccessCidrs": [
                "0.0.0.0/0"
            ]
        },
        "kubernetesNetworkConfig": {
            "serviceIpv4Cidr": "10.100.0.0/16",
            "ipFamily": "ipv4"
        },
        "logging": {
            "clusterLogging": [
                {
                    "types": [
                        "api",
                        "audit",
                        "authenticator",
                        "controllerManager",
                        "scheduler"
                    ],
                    "enabled": true
                }
            ]
        },
        "identity": {
            "oidc": {
                "issuer": "https://oidc.eks.us-east-2.amazonaws.com/id/DALSJ343KE23J3RN45653DSKJTT647TYD"
            }
        },
        "status": "DELETING",
        "certificateAuthority": {
            "data": "XXX_CA_DATA_XXX"
        },
        "platformVersion": "eks.16",
        "tags": {
            "aws:cloudformation:stack-name": "eksctl-my-eks-cluster-cluster",
            "alpha.eksctl.io/cluster-name": "my-eks-cluster",
            "karpenter.sh/discovery": "my-eks-cluster",
            "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-east-2:111122223333:stack/eksctl-my-eks-cluster-cluster/e752ea00-e217-11ee-beae-0a9599c8c7ed",
            "auto-delete": "no",
            "eksctl.cluster.k8s.io/v1alpha1/cluster-name": "my-eks-cluster",
            "EKS-Cluster-Name": "my-eks-cluster",
            "alpha.eksctl.io/cluster-oidc-enabled": "true",
            "aws:cloudformation:logical-id": "ControlPlane",
            "alpha.eksctl.io/eksctl-version": "0.173.0-dev+a7ee89342.2024-03-01T03:40:57Z",
            "Name": "eksctl-my-eks-cluster-cluster/ControlPlane"
        },
        "accessConfig": {
            "authenticationMode": "API_AND_CONFIG_MAP"
        }
    }
}
```

For more information, see [Deleting an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html) in the *Amazon EKS User Guide*.

## Output

cluster -> (structure)

The full description of the cluster to delete.

name -> (string)

The name of your cluster.

arn -> (string)

The Amazon Resource Name (ARN) of the cluster.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

version -> (string)

The Kubernetes server version for the cluster.

endpoint -> (string)

The endpoint for your Kubernetes API server.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to Amazon Web Services API operations on your behalf.

resourcesVpcConfig -> (structure)

The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster security group considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* .

subnetIds -> (list)

The subnets associated with your cluster.

(string)

securityGroupIds -> (list)

The security groups associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Kubernetes control plane.

(string)

clusterSecurityGroupId -> (string)

The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control-plane-to-data-plane communication.

vpcId -> (string)

The VPC associated with your cluster.

endpointPublicAccess -> (boolean)

Whether the public API server endpoint is enabled.

endpointPrivateAccess -> (boolean)

This parameter indicates whether the Amazon EKS private API server endpoint is enabled. If the Amazon EKS private API server endpoint is enabled, Kubernetes API requests that originate from within your clusterâs VPC use the private VPC endpoint instead of traversing the internet. If this value is disabled and you have nodes or Fargate pods in the cluster, then ensure that `publicAccessCidrs` includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* * .

publicAccessCidrs -> (list)

The CIDR blocks that are allowed access to your clusterâs public Kubernetes API server endpoint.

(string)

kubernetesNetworkConfig -> (structure)

The Kubernetes network configuration for the cluster.

serviceIpv4Cidr -> (string)

The CIDR block that Kubernetes `Pod` and `Service` object IP addresses are assigned from. Kubernetes assigns addresses from an `IPv4` CIDR block assigned to a subnet that the node is in. If you didnât specify a CIDR block when you created the cluster, then Kubernetes assigns addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks. If this was specified, then it was specified when the cluster was created and it canât be changed.

serviceIpv6Cidr -> (string)

The CIDR block that Kubernetes pod and service IP addresses are assigned from if you created a 1.21 or later cluster with version 1.10.1 or later of the Amazon VPC CNI add-on and specified `ipv6` for **ipFamily** when you created the cluster. Kubernetes assigns service addresses from the unique local address range (`fc00::/7` ) because you canât specify a custom IPv6 CIDR block when you create the cluster.

ipFamily -> (string)

The IP family used to assign Kubernetes `Pod` and `Service` objects IP addresses. The IP family is always `ipv4` , unless you have a `1.21` or later cluster running version `1.10.1` or later of the Amazon VPC CNI plugin for Kubernetes and specified `ipv6` when you created the cluster.

elasticLoadBalancing -> (structure)

Indicates the current configuration of the load balancing capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled.

enabled -> (boolean)

Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your Amazon Web Services account.

logging -> (structure)

The logging configuration for your cluster.

clusterLogging -> (list)

The cluster control plane logging configuration for your cluster.

(structure)

An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

types -> (list)

The available cluster control plane log types.

(string)

enabled -> (boolean)

If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs . If a log type isnât enabled, that log type doesnât export its control plane logs. Each individual log type can be enabled or disabled independently.

identity -> (structure)

The identity provider information for the cluster.

oidc -> (structure)

An object representing the [OpenID Connect](https://openid.net/connect/) identity provider information.

issuer -> (string)

The issuer URL for the OIDC identity provider.

status -> (string)

The current status of the cluster.

certificateAuthority -> (structure)

The `certificate-authority-data` for your cluster.

data -> (string)

The Base64-encoded certificate data required to communicate with your cluster. Add this to the `certificate-authority-data` section of the `kubeconfig` file for your cluster.

clientRequestToken -> (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

platformVersion -> (string)

The platform version of your Amazon EKS cluster. For more information about clusters deployed on the Amazon Web Services Cloud, see [Platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html) in the * *Amazon EKS User Guide* * . For more information about local clusters deployed on an Outpost, see [Amazon EKS local cluster platform versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-platform-versions.html) in the * *Amazon EKS User Guide* * .

tags -> (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

encryptionConfig -> (list)

The encryption configuration for the cluster.

(structure)

The encryption configuration for the cluster.

resources -> (list)

Specifies the resources to be encrypted. The only supported value is `secrets` .

(string)

provider -> (structure)

Key Management Service (KMS) key. Either the ARN or the alias can be used.

keyArn -> (string)

Amazon Resource Name (ARN) or alias of the KMS key. The KMS key must be symmetric and created in the same Amazon Web Services Region as the cluster. If the KMS key was created in a different account, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) must have access to the KMS key. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *Key Management Service Developer Guide* .

connectorConfig -> (structure)

The configuration used to connect to a cluster for registration.

activationId -> (string)

A unique ID associated with the cluster for registration purposes.

activationCode -> (string)

A unique code associated with the cluster for registration purposes.

activationExpiry -> (timestamp)

The expiration time of the connected cluster. The clusterâs YAML file must be applied through the native provider.

provider -> (string)

The clusterâs cloud service provider.

roleArn -> (string)

The Amazon Resource Name (ARN) of the role to communicate with services from the connected Kubernetes cluster.

id -> (string)

The ID of your local Amazon EKS cluster on an Amazon Web Services Outpost. This property isnât available for an Amazon EKS cluster on the Amazon Web Services cloud.

health -> (structure)

An object representing the health of your Amazon EKS cluster.

issues -> (list)

An object representing the health issues of your Amazon EKS cluster.

(structure)

An issue with your Amazon EKS cluster.

code -> (string)

The error code of the issue.

message -> (string)

A description of the issue.

resourceIds -> (list)

The resource IDs that the issue relates to.

(string)

outpostConfig -> (structure)

An object representing the configuration of your local Amazon EKS cluster on an Amazon Web Services Outpost. This object isnât available for clusters on the Amazon Web Services cloud.

outpostArns -> (list)

The ARN of the Outpost that you specified for use with your local Amazon EKS cluster on Outposts.

(string)

controlPlaneInstanceType -> (string)

The Amazon EC2 instance type used for the control plane. The instance type is the same for all control plane instances.

controlPlanePlacement -> (structure)

An object representing the placement configuration for all the control plane instances of your local Amazon EKS cluster on an Amazon Web Services Outpost. For more information, see [Capacity considerations](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-capacity-considerations.html) in the *Amazon EKS User Guide* .

groupName -> (string)

The name of the placement group for the Kubernetes control plane instances.

accessConfig -> (structure)

The access configuration for the cluster.

bootstrapClusterCreatorAdminPermissions -> (boolean)

Specifies whether or not the cluster creator IAM principal was set as a cluster admin access entry during cluster creation time.

authenticationMode -> (string)

The current authentication mode of the cluster.

upgradePolicy -> (structure)

This value indicates if extended support is enabled or disabled for the cluster.

[Learn more about EKS Extended Support in the *Amazon EKS User Guide* .](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

supportType -> (string)

If the cluster is set to `EXTENDED` , it will enter extended support at the end of standard support. If the cluster is set to `STANDARD` , it will be automatically upgraded at the end of standard support.

[Learn more about EKS Extended Support in the *Amazon EKS User Guide* .](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

zonalShiftConfig -> (structure)

The configuration for zonal shift for the cluster.

enabled -> (boolean)

Whether the zonal shift is enabled.

remoteNetworkConfig -> (structure)

The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.

remoteNodeNetworks -> (list)

The list of network CIDRs that can contain hybrid nodes.

(structure)

A network CIDR that can contain hybrid nodes.

These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
- Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including Transit Gateway, Site-to-Site VPN, or Direct Connect.
- Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250` .
- Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
- Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.

cidrs -> (list)

A network CIDR that can contain hybrid nodes.

These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
- Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including Transit Gateway, Site-to-Site VPN, or Direct Connect.
- Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250` .
- Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
- Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.

(string)

remotePodNetworks -> (list)

The list of network CIDRs that can contain pods that run Kubernetes webhooks on hybrid nodes.

(structure)

A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.

These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isnât available for on-premises and edge locations.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.

cidrs -> (list)

A network CIDR that can contain pods that run Kubernetes webhooks on hybrid nodes.

These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isnât available for on-premises and edge locations.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.

(string)

computeConfig -> (structure)

Indicates the current configuration of the compute capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account. For more information, see EKS Auto Mode compute capability in the *Amazon EKS User Guide* .

enabled -> (boolean)

Indicates if the compute capability is enabled on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account.

nodePools -> (list)

Indicates the current configuration of node pools in your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the *Amazon EKS User Guide* .

(string)

nodeRoleArn -> (string)

The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster.

storageConfig -> (structure)

Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide* .

blockStorage -> (structure)

Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled.

enabled -> (boolean)

Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account.