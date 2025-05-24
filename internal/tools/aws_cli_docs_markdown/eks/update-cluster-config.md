# update-cluster-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# update-cluster-config

## Description

Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with `DescribeUpdate` .

You can use this operation to do the following actions:

- You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs arenât exported to CloudWatch Logs. For more information, see [Amazon EKS Cluster control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* * .

### Note

CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/) .

- You can also use this API operation to enable or disable public and private access to your clusterâs Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* * .
- You can also use this API operation to choose different subnets and security groups for the cluster. You must specify at least two subnets that are in different Availability Zones. You canât change which VPC the subnets are from, the subnets must be in the same VPC as the subnets that the cluster was created with. For more information about the VPC requirements, see [https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) in the * *Amazon EKS User Guide* * .
- You can also use this API operation to enable or disable ARC zonal shift. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.
- You can also use this API operation to add, change, or remove the configuration in the cluster for EKS Hybrid Nodes. To remove the configuration, use the `remoteNetworkConfig` key with an object containing both subkeys with empty arrays for each. Here is an inline example: `"remoteNetworkConfig": { "remoteNodeNetworks": [], "remotePodNetworks": [] }` .

Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to `UPDATING` (this status transition is eventually consistent). When the update is complete (either `Failed` or `Successful` ), the cluster status moves to `Active` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterConfig)

## Synopsis

```
update-cluster-config
--name <value>
[--resources-vpc-config <value>]
[--logging <value>]
[--client-request-token <value>]
[--access-config <value>]
[--upgrade-policy <value>]
[--zonal-shift-config <value>]
[--compute-config <value>]
[--kubernetes-network-config <value>]
[--storage-config <value>]
[--remote-network-config <value>]
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

The name of the Amazon EKS cluster to update.

`--resources-vpc-config` (structure)

An object representing the VPC configuration to use for an Amazon EKS cluster.

subnetIds -> (list)

Specify subnets for your Amazon EKS nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your nodes and the Kubernetes control plane.

(string)

securityGroupIds -> (list)

Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use that allow communication between your nodes and the Kubernetes control plane. If you donât specify any security groups, then familiarize yourself with the difference between Amazon EKS defaults for clusters deployed with Kubernetes. For more information, see [Amazon EKS security group considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the * *Amazon EKS User Guide* * .

(string)

endpointPublicAccess -> (boolean)

Set this value to `false` to disable public access to your clusterâs Kubernetes API server endpoint. If you disable public access, your clusterâs Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is `true` , which enables public access for your Kubernetes API server. For more information, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* * .

endpointPrivateAccess -> (boolean)

Set this value to `true` to enable private access for your clusterâs Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your clusterâs VPC use the private VPC endpoint. The default value for this parameter is `false` , which disables private access for your Kubernetes API server. If you disable private access and you have nodes or Fargate pods in the cluster, then ensure that `publicAccessCidrs` includes the necessary CIDR blocks for communication with the nodes or Fargate pods. For more information, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* * .

publicAccessCidrs -> (list)

The CIDR blocks that are allowed access to your clusterâs public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is `0.0.0.0/0` . If youâve disabled private endpoint access, make sure that you specify the necessary CIDR blocks for every node and Fargate `Pod` in the cluster. For more information, see [Amazon EKS cluster endpoint access control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* * .

(string)

Shorthand Syntax:

```
subnetIds=string,string,securityGroupIds=string,string,endpointPublicAccess=boolean,endpointPrivateAccess=boolean,publicAccessCidrs=string,string
```

JSON Syntax:

```
{
  "subnetIds": ["string", ...],
  "securityGroupIds": ["string", ...],
  "endpointPublicAccess": true|false,
  "endpointPrivateAccess": true|false,
  "publicAccessCidrs": ["string", ...]
}
```

`--logging` (structure)

Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs arenât exported to CloudWatch Logs . For more information, see [Amazon EKS cluster control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* * .

### Note

CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/) .

clusterLogging -> (list)

The cluster control plane logging configuration for your cluster.

(structure)

An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

types -> (list)

The available cluster control plane log types.

(string)

enabled -> (boolean)

If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs . If a log type isnât enabled, that log type doesnât export its control plane logs. Each individual log type can be enabled or disabled independently.

JSON Syntax:

```
{
  "clusterLogging": [
    {
      "types": ["api"|"audit"|"authenticator"|"controllerManager"|"scheduler", ...],
      "enabled": true|false
    }
    ...
  ]
}
```

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--access-config` (structure)

The access configuration for the cluster.

authenticationMode -> (string)

The desired authentication mode for the cluster.

Shorthand Syntax:

```
authenticationMode=string
```

JSON Syntax:

```
{
  "authenticationMode": "API"|"API_AND_CONFIG_MAP"|"CONFIG_MAP"
}
```

`--upgrade-policy` (structure)

You can enable or disable extended support for clusters currently on standard support. You cannot disable extended support once it starts. You must enable extended support before your cluster exits standard support.

supportType -> (string)

If the cluster is set to `EXTENDED` , it will enter extended support at the end of standard support. If the cluster is set to `STANDARD` , it will be automatically upgraded at the end of standard support.

[Learn more about EKS Extended Support in the *Amazon EKS User Guide* .](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)

Shorthand Syntax:

```
supportType=string
```

JSON Syntax:

```
{
  "supportType": "STANDARD"|"EXTENDED"
}
```

`--zonal-shift-config` (structure)

Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.

Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.

You can start a zonal shift for an EKS cluster, or you can allow Amazon Web Services to do it for you by enabling *zonal autoshift* . This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see [Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the * *Amazon EKS User Guide* * .

enabled -> (boolean)

If zonal shift is enabled, Amazon Web Services configures zonal autoshift for the cluster.

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

`--compute-config` (structure)

Update the configuration of the compute capability of your EKS Auto Mode cluster. For example, enable the capability.

enabled -> (boolean)

Request to enable or disable the compute capability on your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your Amazon Web Services account.

nodePools -> (list)

Configuration for node pools that defines the compute resources for your EKS Auto Mode cluster. For more information, see EKS Auto Mode Node Pools in the *Amazon EKS User Guide* .

(string)

nodeRoleArn -> (string)

The ARN of the IAM Role EKS will assign to EC2 Managed Instances in your EKS Auto Mode cluster. This value cannot be changed after the compute capability of EKS Auto Mode is enabled. For more information, see the IAM Reference in the *Amazon EKS User Guide* .

Shorthand Syntax:

```
enabled=boolean,nodePools=string,string,nodeRoleArn=string
```

JSON Syntax:

```
{
  "enabled": true|false,
  "nodePools": ["string", ...],
  "nodeRoleArn": "string"
}
```

`--kubernetes-network-config` (structure)

The Kubernetes network configuration for the cluster.

serviceIpv4Cidr -> (string)

Donât specify a value if you select `ipv6` for **ipFamily** . The CIDR block to assign Kubernetes service IP addresses from. If you donât specify a block, Kubernetes assigns addresses from either the `10.100.0.0/16` or `172.20.0.0/16` CIDR blocks. We recommend that you specify a block that does not overlap with resources in other networks that are peered or connected to your VPC. The block must meet the following requirements:

- Within one of the following private IP address blocks: `10.0.0.0/8` , `172.16.0.0/12` , or `192.168.0.0/16` .
- Doesnât overlap with any CIDR block assigned to the VPC that you selected for VPC.
- Between `/24` and `/12` .

### Warning

You can only specify a custom CIDR block when you create a cluster. You canât change this value after the cluster is created.

ipFamily -> (string)

Specify which IP family is used to assign Kubernetes pod and service IP addresses. If you donât specify a value, `ipv4` is used by default. You can only specify an IP family when you create a cluster and canât change this value once the cluster is created. If you specify `ipv6` , the VPC and subnets that you specify for cluster creation must have both `IPv4` and `IPv6` CIDR blocks assigned to them. You canât specify `ipv6` for clusters in China Regions.

You can only specify `ipv6` for `1.21` and later clusters that use version `1.10.1` or later of the Amazon VPC CNI add-on. If you specify `ipv6` , then ensure that your VPC meets the requirements listed in the considerations listed in [Assigning IPv6 addresses to pods and services](https://docs.aws.amazon.com/eks/latest/userguide/cni-ipv6.html) in the *Amazon EKS User Guide* . Kubernetes assigns services `IPv6` addresses from the unique local address range `(fc00::/7)` . You canât specify a custom `IPv6` CIDR block. Pod addresses are assigned from the subnetâs `IPv6` CIDR.

elasticLoadBalancing -> (structure)

Request to enable or disable the load balancing capability on your EKS Auto Mode cluster. For more information, see EKS Auto Mode load balancing capability in the *Amazon EKS User Guide* .

enabled -> (boolean)

Indicates if the load balancing capability is enabled on your EKS Auto Mode cluster. If the load balancing capability is enabled, EKS Auto Mode will create and delete load balancers in your Amazon Web Services account.

Shorthand Syntax:

```
serviceIpv4Cidr=string,ipFamily=string,elasticLoadBalancing={enabled=boolean}
```

JSON Syntax:

```
{
  "serviceIpv4Cidr": "string",
  "ipFamily": "ipv4"|"ipv6",
  "elasticLoadBalancing": {
    "enabled": true|false
  }
}
```

`--storage-config` (structure)

Update the configuration of the block storage capability of your EKS Auto Mode cluster. For example, enable the capability.

blockStorage -> (structure)

Request to configure EBS Block Storage settings for your EKS Auto Mode cluster.

enabled -> (boolean)

Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account.

Shorthand Syntax:

```
blockStorage={enabled=boolean}
```

JSON Syntax:

```
{
  "blockStorage": {
    "enabled": true|false
  }
}
```

`--remote-network-config` (structure)

The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.

remoteNodeNetworks -> (list)

The list of network CIDRs that can contain hybrid nodes.

These CIDR blocks define the expected IP address range of the hybrid nodes that join the cluster. These blocks are typically determined by your network administrator.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.
- Each block must have a route to the VPC that uses the VPC CIDR blocks, not public IPs or Elastic IPs. There are many options including Transit Gateway, Site-to-Site VPN, or Direct Connect.
- Each host must allow outbound connection to the EKS cluster control plane on TCP ports `443` and `10250` .
- Each host must allow inbound connection from the EKS cluster control plane on TCP port 10250 for logs, exec and port-forward operations.
- Each host must allow TCP and UDP network connectivity to and from other hosts that are running `CoreDNS` on UDP port `53` for service and pod DNS names.

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

These CIDR blocks are determined by configuring your Container Network Interface (CNI) plugin. We recommend the Calico CNI or Cilium CNI. Note that the Amazon VPC CNI plugin for Kubernetes isnât available for on-premises and edge locations.

Enter one or more IPv4 CIDR blocks in decimal dotted-quad notation (for example, `10.2.0.0/16` ).

It must satisfy the following requirements:

- Each block must be within an `IPv4` RFC-1918 network range. Minimum allowed size is /24, maximum allowed size is /8. Publicly-routable addresses arenât supported.
- Each block cannot overlap with the range of the VPC CIDR blocks for your EKS resources, or the block of the Kubernetes service IP range.

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

JSON Syntax:

```
{
  "remoteNodeNetworks": [
    {
      "cidrs": ["string", ...]
    }
    ...
  ],
  "remotePodNetworks": [
    {
      "cidrs": ["string", ...]
    }
    ...
  ]
}
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

**To update cluster endpoint access**

This example command updates a cluster to disable endpoint public access and enable private endpoint access.

Command:

```
aws eks update-cluster-config --name example \
--resources-vpc-config endpointPublicAccess=false,endpointPrivateAccess=true
```

Output:

```
{
    "update": {
        "id": "ec883c93-2e9e-407c-a22f-8f6fa6e67d4f",
        "status": "InProgress",
        "type": "EndpointAccessUpdate",
        "params": [
            {
                "type": "EndpointPublicAccess",
                "value": "false"
            },
            {
                "type": "EndpointPrivateAccess",
                "value": "true"
            }
        ],
        "createdAt": 1565806986.506,
        "errors": []
    }
}
```

**To enable logging for a cluster**

This example command enables all cluster control plane logging types for a cluster named `example`.

Command:

```
aws eks update-cluster-config --name example \
--logging '{"clusterLogging":[{"types":["api","audit","authenticator","controllerManager","scheduler"],"enabled":true}]}'
```

Output:

```
{
    "update": {
        "id": "7551c64b-1d27-4b1e-9f8e-c45f056eb6fd",
        "status": "InProgress",
        "type": "LoggingUpdate",
        "params": [
            {
                "type": "ClusterLogging",
                "value": "{\"clusterLogging\":[{\"types\":[\"api\",\"audit\",\"authenticator\",\"controllerManager\",\"scheduler\"],\"enabled\":true}]}"
            }
        ],
        "createdAt": 1565807210.37,
        "errors": []
    }
}
```

## Output

update -> (structure)

An object representing an asynchronous update.

id -> (string)

A UUID that is used to track the update.

status -> (string)

The current status of the update.

type -> (string)

The type of the update.

params -> (list)

A key-value map that contains the parameters associated with the update.

(structure)

An object representing the details of an update request.

type -> (string)

The keys associated with an update request.

value -> (string)

The value of the keys submitted as part of an update request.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

errors -> (list)

Any errors associated with a `Failed` update.

(structure)

An object representing an error when an asynchronous operation fails.

errorCode -> (string)

A brief description of the error.

- **SubnetNotFound** : We couldnât find one of the subnets associated with the cluster.
- **SecurityGroupNotFound** : We couldnât find one of the security groups associated with the cluster.
- **EniLimitReached** : You have reached the elastic network interface limit for your account.
- **IpNotAvailable** : A subnet associated with the cluster doesnât have any available IP addresses.
- **AccessDenied** : You donât have permissions to perform the specified operation.
- **OperationNotPermitted** : The service role associated with the cluster doesnât have the required access permissions for Amazon EKS.
- **VpcIdNotFound** : We couldnât find the VPC associated with the cluster.

errorMessage -> (string)

A more complete description of the error.

resourceIds -> (list)

An optional field that contains the resource IDs associated with the error.

(string)