# create-mount-targetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# create-mount-target

## Description

Creates a mount target for a file system. You can then mount the file system on EC2 instances by using the mount target.

You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system.

You can create only one mount target for a One Zone file system. You must create that mount target in the same Availability Zone in which the file system is located. Use the `AvailabilityZoneName` and `AvailabiltyZoneId` properties in the  DescribeFileSystems response object to get this information. Use the `subnetId` associated with the file systemâs Availability Zone when creating the mount target.

For more information, see [Amazon EFS: How it Works](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html) .

To create a mount target for a file system, the file systemâs lifecycle state must be `available` . For more information, see  DescribeFileSystems .

In the request, provide the following:

- The file system ID for which you are creating the mount target.
- A subnet ID, which determines the following:
- The VPC in which Amazon EFS creates the mount target
- The Availability Zone in which Amazon EFS creates the mount target
- The IP address range from which Amazon EFS selects the IP address of the mount target (if you donât specify an IP address in the request)

After creating the mount target, Amazon EFS returns a response that includes, a `MountTargetId` and an `IpAddress` . You use this IP address when mounting the file system in an EC2 instance. You can also use the mount targetâs DNS name when mounting the file system. The EC2 instance on which you mount the file system by using the mount target can resolve the mount targetâs DNS name to its IP address. For more information, see [How it Works: Implementation Overview](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-implementation) .

Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:

- Must belong to the same VPC as the subnets of the existing mount targets
- Must not be in the same Availability Zone as any of the subnets of the existing mount targets

If the request satisfies the requirements, Amazon EFS does the following:

- Creates a new mount target in the specified subnet.
- Also creates a new network interface in the subnet as follows:
- If the request provides an `IpAddress` , Amazon EFS assigns that IP address to the network interface. Otherwise, Amazon EFS assigns a free address in the subnet (in the same way that the Amazon EC2 `CreateNetworkInterface` call does when a request does not specify a primary private IP address).
- If the request provides `SecurityGroups` , this network interface is associated with those security groups. Otherwise, it belongs to the default security group for the subnetâs VPC.
- Assigns the description `Mount target *fsmt-id* for file system *fs-id* `` where `` *fsmt-id* `` is the mount target ID, and `` *fs-id* `` is the ``FileSystemId` .
- Sets the `requesterManaged` property of the network interface to `true` , and the `requesterId` value to `EFS` .

Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the `NetworkInterfaceId` field in the mount targetâs description to the network interface ID, and the `IpAddress` field to its address. If network interface creation fails, the entire `CreateMountTarget` operation fails.

### Note

The `CreateMountTarget` call returns only after creating the network interface, but while the mount target state is still `creating` , you can check the mount target creation status by calling the  DescribeMountTargets operation, which among other things returns the mount target state.

We recommend that you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see [Amazon EFS](http://aws.amazon.com/efs/) . In addition, by always using a mount target local to the instanceâs Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you canât access your file system through that mount target.

This operation requires permissions for the following action on the file system:

- `elasticfilesystem:CreateMountTarget`

This operation also requires permissions for the following Amazon EC2 actions:

- `ec2:DescribeSubnets`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateMountTarget)

## Synopsis

```
create-mount-target
--file-system-id <value>
--subnet-id <value>
[--ip-address <value>]
[--security-groups <value>]
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

`--file-system-id` (string)

The ID of the file system for which to create the mount target.

`--subnet-id` (string)

The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file systemâs Availability Zone.

`--ip-address` (string)

Valid IPv4 address within the address range of the specified subnet.

`--security-groups` (list)

Up to five VPC security group IDs, of the form `sg-xxxxxxxx` . These must be for the same VPC as subnet specified.

(string)

Syntax:

```
"string" "string" ...
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

**To create a mount target**

The following `create-mount-target` example creates a mount target for the specified file system.

```
aws efs create-mount-target \
    --file-system-id fs-c7a0456e \
    --subnet-id subnet-02bf4c428bexample \
    --security-groups sg-068f739363example
```

Output:

```
{
    "OwnerId": "123456789012",
    "MountTargetId": "fsmt-f9a14450",
    "FileSystemId": "fs-c7a0456e",
    "SubnetId": "subnet-02bf4c428bexample",
    "LifeCycleState": "creating",
    "IpAddress": "10.0.1.24",
    "NetworkInterfaceId": "eni-02d542216aexample",
    "AvailabilityZoneId": "use2-az2",
    "AvailabilityZoneName": "us-east-2b",
    "VpcId": "vpc-0123456789abcdef0"
}
```

For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) in the *Amazon Elastic File System User Guide*.

## Output

OwnerId -> (string)

Amazon Web Services account ID that owns the resource.

MountTargetId -> (string)

System-assigned mount target ID.

FileSystemId -> (string)

The ID of the file system for which the mount target is intended.

SubnetId -> (string)

The ID of the mount targetâs subnet.

LifeCycleState -> (string)

Lifecycle state of the mount target.

IpAddress -> (string)

Address at which the file system can be mounted by using the mount target.

NetworkInterfaceId -> (string)

The ID of the network interface that Amazon EFS created when it created the mount target.

AvailabilityZoneId -> (string)

The unique and consistent identifier of the Availability Zone that the mount target resides in. For example, `use1-az1` is an AZ ID for the us-east-1 Region and it has the same location in every Amazon Web Services account.

AvailabilityZoneName -> (string)

The name of the Availability Zone in which the mount target is located. Availability Zones are independently mapped to names for each Amazon Web Services account. For example, the Availability Zone `us-east-1a` for your Amazon Web Services account might not be the same location as `us-east-1a` for another Amazon Web Services account.

VpcId -> (string)

The virtual private cloud (VPC) ID that the mount target is configured in.