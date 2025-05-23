# restore-from-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# restore-from-cluster-snapshot

## Description

Creates a new cluster from a snapshot. By default, Amazon Redshift creates the resulting cluster with the same configuration as the original cluster from which the snapshot was created, except that the new cluster is created with the default cluster security and parameter groups. After Amazon Redshift creates the cluster, you can use the  ModifyCluster API to associate a different security group and different parameter group with the restored cluster. If you are using a DS node type, you can also choose to change to another DS node type of the same size during restore.

If you restore a cluster into a VPC, you must provide a cluster subnet group where you want the cluster restored.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:

- Creating a public cluster
- Restoring a public cluster
- Modifying a private cluster to be public
- Adding a subnet with VPC BPA turned on to the subnet group when thereâs at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide* .

For more information about working with snapshots, go to [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html) in the *Amazon Redshift Cluster Management Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/RestoreFromClusterSnapshot)

## Synopsis

```
restore-from-cluster-snapshot
--cluster-identifier <value>
[--snapshot-identifier <value>]
[--snapshot-arn <value>]
[--snapshot-cluster-identifier <value>]
[--port <value>]
[--availability-zone <value>]
[--allow-version-upgrade | --no-allow-version-upgrade]
[--cluster-subnet-group-name <value>]
[--publicly-accessible | --no-publicly-accessible]
[--owner-account <value>]
[--hsm-client-certificate-identifier <value>]
[--hsm-configuration-identifier <value>]
[--elastic-ip <value>]
[--cluster-parameter-group-name <value>]
[--cluster-security-groups <value>]
[--vpc-security-group-ids <value>]
[--preferred-maintenance-window <value>]
[--automated-snapshot-retention-period <value>]
[--manual-snapshot-retention-period <value>]
[--kms-key-id <value>]
[--node-type <value>]
[--enhanced-vpc-routing | --no-enhanced-vpc-routing]
[--additional-info <value>]
[--iam-roles <value>]
[--maintenance-track-name <value>]
[--snapshot-schedule-identifier <value>]
[--number-of-nodes <value>]
[--availability-zone-relocation | --no-availability-zone-relocation]
[--aqua-configuration-status <value>]
[--default-iam-role-arn <value>]
[--reserved-node-id <value>]
[--target-reserved-node-offering-id <value>]
[--encrypted | --no-encrypted]
[--manage-master-password | --no-manage-master-password]
[--master-password-secret-kms-key-id <value>]
[--ip-address-type <value>]
[--multi-az | --no-multi-az]
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

`--cluster-identifier` (string)

The identifier of the cluster that will be created from restoring the snapshot.

Constraints:

- Must contain from 1 to 63 alphanumeric characters or hyphens.
- Alphabetic characters must be lowercase.
- First character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.
- Must be unique for all clusters within an Amazon Web Services account.

`--snapshot-identifier` (string)

The name of the snapshot from which to create the new cluster. This parameter isnât case sensitive. You must specify this parameter or `snapshotArn` , but not both.

Example: `my-snapshot-id`

`--snapshot-arn` (string)

The Amazon Resource Name (ARN) of the snapshot associated with the message to restore from a cluster. You must specify this parameter or `snapshotIdentifier` , but not both.

`--snapshot-cluster-identifier` (string)

The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.

`--port` (integer)

The port number on which the cluster accepts connections.

Default: The same port as the original cluster.

Valid values: For clusters with DC2 nodes, must be within the range `1150` -`65535` . For clusters with ra3 nodes, must be within the ranges `5431` -`5455` or `8191` -`8215` .

`--availability-zone` (string)

The Amazon EC2 Availability Zone in which to restore the cluster.

Default: A random, system-chosen Availability Zone.

Example: `us-east-2a`

`--allow-version-upgrade` | `--no-allow-version-upgrade` (boolean)

If `true` , major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.

Default: `true`

`--cluster-subnet-group-name` (string)

The name of the subnet group where you want to cluster restored.

A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

If `true` , the cluster can be accessed from a public network.

Default: false

`--owner-account` (string)

The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.

`--hsm-client-certificate-identifier` (string)

Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

`--hsm-configuration-identifier` (string)

Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

`--elastic-ip` (string)

The Elastic IP (EIP) address for the cluster. Donât specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on.

`--cluster-parameter-group-name` (string)

The name of the parameter group to be associated with this cluster.

Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to [Working with Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) .

Constraints:

- Must be 1 to 255 alphanumeric characters or hyphens.
- First character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

`--cluster-security-groups` (list)

A list of security groups to be associated with this cluster.

Default: The default cluster security group for Amazon Redshift.

Cluster security groups only apply to clusters outside of VPCs.

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.

Default: The default VPC security group is associated with the cluster.

VPC security groups only apply to clusters in VPCs.

(string)

Syntax:

```
"string" "string" ...
```

`--preferred-maintenance-window` (string)

The weekly time range (in UTC) during which automated cluster maintenance can occur.

Format: `ddd:hh24:mi-ddd:hh24:mi`

Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see [Maintenance Windows](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows) in Amazon Redshift Cluster Management Guide.

Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

Constraints: Minimum 30-minute window.

`--automated-snapshot-retention-period` (integer)

The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with  CreateClusterSnapshot .

You canât disable automated snapshots for RA3 node types. Set the automated retention period from 1-35 days.

Default: The value selected for the cluster from which the snapshot was taken.

Constraints: Must be a value from 0 to 35.

`--manual-snapshot-retention-period` (integer)

The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesnât change the retention period of existing snapshots.

The value must be either -1 or an integer between 1 and 3,653.

`--kms-key-id` (string)

The Key Management Service (KMS) key ID of the encryption key that encrypts data in the cluster restored from a shared snapshot. You can also provide the key ID when you restore from an unencrypted snapshot to an encrypted cluster in the same account. Additionally, you can specify a new KMS key ID when you restore from an encrypted snapshot in the same account in order to change it. In that case, the restored cluster is encrypted with the new KMS key ID.

`--node-type` (string)

The node type that the restored cluster will be provisioned with.

If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc2.large node type into another dc2 type. For more information about node types, see [About Clusters and Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes) in the *Amazon Redshift Cluster Management Guide* .

`--enhanced-vpc-routing` | `--no-enhanced-vpc-routing` (boolean)

An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.

If this option is `true` , enhanced VPC routing is enabled.

Default: false

`--additional-info` (string)

Reserved.

`--iam-roles` (list)

A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format.

The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to [Quotas and limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--maintenance-track-name` (string)

The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the `MaintenanceTrack` value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.

`--snapshot-schedule-identifier` (string)

A unique identifier for the snapshot schedule.

`--number-of-nodes` (integer)

The number of nodes specified when provisioning the restored cluster.

`--availability-zone-relocation` | `--no-availability-zone-relocation` (boolean)

The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is restored.

`--aqua-configuration-status` (string)

This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).

Possible values:

- `enabled`
- `disabled`
- `auto`

`--default-iam-role-arn` (string)

The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified while it was restored from a snapshot.

`--reserved-node-id` (string)

The identifier of the target reserved node offering.

`--target-reserved-node-offering-id` (string)

The identifier of the target reserved node offering.

`--encrypted` | `--no-encrypted` (boolean)

Enables support for restoring an unencrypted snapshot to a cluster encrypted with Key Management Service (KMS) and a customer managed key.

`--manage-master-password` | `--no-manage-master-password` (boolean)

If `true` , Amazon Redshift uses Secrets Manager to manage the restored clusterâs admin credentials. If `ManageMasterPassword` is false or not set, Amazon Redshift uses the admin credentials the cluster had at the time the snapshot was taken.

`--master-password-secret-kms-key-id` (string)

The ID of the Key Management Service (KMS) key used to encrypt and store the clusterâs admin credentials secret. You can only use this parameter if `ManageMasterPassword` is true.

`--ip-address-type` (string)

The IP address type for the cluster. Possible values are `ipv4` and `dualstack` .

`--multi-az` | `--no-multi-az` (boolean)

If true, the snapshot will be restored to a cluster deployed in two Availability Zones.

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

### Restore a Cluster From a Snapshot

This example restores a cluster from a snapshot.

Command:

```
aws redshift restore-from-cluster-snapshot --cluster-identifier mycluster-clone --snapshot-identifier my-snapshot-id
```

Result:

```
{
   "Cluster": {
      "NodeType": "dw.hs1.xlarge",
      "ClusterVersion": "1.0",
      "PubliclyAccessible": "true",
      "MasterUsername": "adminuser",
      "ClusterParameterGroups": [
         {
         "ParameterApplyStatus": "in-sync",
         "ParameterGroupName": "default.redshift-1.0"
         }
      ],
      "ClusterSecurityGroups": [
         {
         "Status": "active",
         "ClusterSecurityGroupName": "default"
         }
      ],
      "AllowVersionUpgrade": true,
      "VpcSecurityGroups": \[],
      "PreferredMaintenanceWindow": "sun:23:15-mon:03:15",
      "AutomatedSnapshotRetentionPeriod": 1,
      "ClusterStatus": "creating",
      "ClusterIdentifier": "mycluster-clone",
      "DBName": "dev",
      "NumberOfNodes": 2,
      "PendingModifiedValues": {}
   },
   "ResponseMetadata": {
      "RequestId": "77fd512b-64e3-11e2-8f5b-e90bd6c77476"
   }
}
```

## Output

Cluster -> (structure)

Describes a cluster.

ClusterIdentifier -> (string)

The unique identifier of the cluster.

NodeType -> (string)

The node type for the nodes in the cluster.

ClusterStatus -> (string)

The current state of the cluster. Possible values are the following:

- `available`
- `available, prep-for-resize`
- `available, resize-cleanup`
- `cancelling-resize`
- `creating`
- `deleting`
- `final-snapshot`
- `hardware-failure`
- `incompatible-hsm`
- `incompatible-network`
- `incompatible-parameters`
- `incompatible-restore`
- `modifying`
- `paused`
- `rebooting`
- `renaming`
- `resizing`
- `rotating-keys`
- `storage-full`
- `updating-hsm`

ClusterAvailabilityStatus -> (string)

The availability status of the cluster for queries. Possible values are the following:

- Available - The cluster is available for queries.
- Unavailable - The cluster is not available for queries.
- Maintenance - The cluster is intermittently available for queries due to maintenance activities.
- Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.
- Failed - The cluster failed and is not available for queries.

ModifyStatus -> (string)

The status of a modify operation, if any, initiated for the cluster.

MasterUsername -> (string)

The admin user name for the cluster. This name is used to connect to the database that is specified in the **DBName** parameter.

DBName -> (string)

The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named `dev` dev was created by default.

Endpoint -> (structure)

The connection endpoint.

Address -> (string)

The DNS address of the Cluster.

Port -> (integer)

The port that the database engine is listening on.

VpcEndpoints -> (list)

Describes a connection endpoint.

(structure)

The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.

VpcEndpointId -> (string)

The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.

VpcId -> (string)

The VPC identifier that the endpoint is associated.

NetworkInterfaces -> (list)

One or more network interfaces of the endpoint. Also known as an interface endpoint.

(structure)

Describes a network interface.

NetworkInterfaceId -> (string)

The network interface identifier.

SubnetId -> (string)

The subnet identifier.

PrivateIpAddress -> (string)

The IPv4 address of the network interface within the subnet.

AvailabilityZone -> (string)

The Availability Zone.

Ipv6Address -> (string)

The IPv6 address of the network interface within the subnet.

ClusterCreateTime -> (timestamp)

The date and time that the cluster was created.

AutomatedSnapshotRetentionPeriod -> (integer)

The number of days that automatic cluster snapshots are retained.

ManualSnapshotRetentionPeriod -> (integer)

The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesnât change the retention period of existing snapshots.

The value must be either -1 or an integer between 1 and 3,653.

ClusterSecurityGroups -> (list)

A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains `ClusterSecurityGroup.Name` and `ClusterSecurityGroup.Status` subelements.

Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the **VpcSecurityGroups** parameter.

(structure)

Describes a cluster security group.

ClusterSecurityGroupName -> (string)

The name of the cluster security group.

Status -> (string)

The status of the cluster security group.

VpcSecurityGroups -> (list)

A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.

(structure)

Describes the members of a VPC security group.

VpcSecurityGroupId -> (string)

The identifier of the VPC security group.

Status -> (string)

The status of the VPC security group.

ClusterParameterGroups -> (list)

The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.

(structure)

Describes the status of a parameter group.

ParameterGroupName -> (string)

The name of the cluster parameter group.

ParameterApplyStatus -> (string)

The status of parameter updates.

ClusterParameterStatusList -> (list)

The list of parameter statuses.

For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide* .

(structure)

Describes the status of a parameter group.

ParameterName -> (string)

The name of the parameter.

ParameterApplyStatus -> (string)

The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.

The following are possible statuses and descriptions.

- `in-sync` : The parameter value is in sync with the database.
- `pending-reboot` : The parameter value will be applied after the cluster reboots.
- `applying` : The parameter value is being applied to the database.
- `invalid-parameter` : Cannot apply the parameter value because it has an invalid value or syntax.
- `apply-deferred` : The parameter contains static property changes. The changes are deferred until the cluster reboots.
- `apply-error` : Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
- `unknown-error` : Cannot apply the parameter change right now. The change will be applied after the cluster reboots.

ParameterApplyErrorDescription -> (string)

The error that prevented the parameter from being applied to the database.

ClusterSubnetGroupName -> (string)

The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.

VpcId -> (string)

The identifier of the VPC the cluster is in, if the cluster is in a VPC.

AvailabilityZone -> (string)

The name of the Availability Zone in which the cluster is located.

PreferredMaintenanceWindow -> (string)

The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.

PendingModifiedValues -> (structure)

A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.

MasterUserPassword -> (string)

The pending or in-progress change of the admin user password for the cluster.

NodeType -> (string)

The pending or in-progress change of the clusterâs node type.

NumberOfNodes -> (integer)

The pending or in-progress change of the number of nodes in the cluster.

ClusterType -> (string)

The pending or in-progress change of the cluster type.

ClusterVersion -> (string)

The pending or in-progress change of the service version.

AutomatedSnapshotRetentionPeriod -> (integer)

The pending or in-progress change of the automated snapshot retention period.

ClusterIdentifier -> (string)

The pending or in-progress change of the new identifier for the cluster.

PubliclyAccessible -> (boolean)

The pending or in-progress change of the ability to connect to the cluster from the public network.

EnhancedVpcRouting -> (boolean)

An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.

If this option is `true` , enhanced VPC routing is enabled.

Default: false

MaintenanceTrackName -> (string)

The name of the maintenance track that the cluster will change to during the next maintenance window.

EncryptionType -> (string)

The encryption type for a cluster. Possible values are: KMS and None.

ClusterVersion -> (string)

The version ID of the Amazon Redshift engine that is running on the cluster.

AllowVersionUpgrade -> (boolean)

A boolean value that, if `true` , indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.

NumberOfNodes -> (integer)

The number of compute nodes in the cluster.

PubliclyAccessible -> (boolean)

A boolean value that, if `true` , indicates that the cluster can be accessed from a public network.

Default: false

Encrypted -> (boolean)

A boolean value that, if `true` , indicates that data in the cluster is encrypted at rest.

RestoreStatus -> (structure)

A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.

Status -> (string)

The status of the restore action. Returns starting, restoring, completed, or failed.

CurrentRestoreRateInMegaBytesPerSecond -> (double)

The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 node types.

SnapshotSizeInMegaBytes -> (long)

The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 node types.

ProgressInMegaBytes -> (long)

The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 node types.

ElapsedTimeInSeconds -> (long)

The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 node types.

EstimatedTimeToCompletionInSeconds -> (long)

The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 node types.

DataTransferProgress -> (structure)

Status -> (string)

Describes the status of the cluster. While the transfer is in progress the status is `transferringdata` .

CurrentRateInMegaBytesPerSecond -> (double)

Describes the data transfer rate in MBâs per second.

TotalDataInMegaBytes -> (long)

Describes the total amount of data to be transfered in megabytes.

DataTransferredInMegaBytes -> (long)

Describes the total amount of data that has been transfered in MBâs.

EstimatedTimeToCompletionInSeconds -> (long)

Describes the estimated number of seconds remaining to complete the transfer.

ElapsedTimeInSeconds -> (long)

Describes the number of seconds that have elapsed during the data transfer.

HsmStatus -> (structure)

A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.

Values: active, applying

HsmClientCertificateIdentifier -> (string)

Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

HsmConfigurationIdentifier -> (string)

Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

Status -> (string)

Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.

Values: active, applying

ClusterSnapshotCopyStatus -> (structure)

A value that returns the destination region and retention period that are configured for cross-region snapshot copy.

DestinationRegion -> (string)

The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.

RetentionPeriod -> (long)

The number of days that automated snapshots are retained in the destination region after they are copied from a source region.

ManualSnapshotRetentionPeriod -> (integer)

The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.

The value must be either -1 or an integer between 1 and 3,653.

SnapshotCopyGrantName -> (string)

The name of the snapshot copy grant.

ClusterPublicKey -> (string)

The public key for the cluster.

ClusterNodes -> (list)

The nodes in the cluster.

(structure)

The identifier of a node in a cluster.

NodeRole -> (string)

Whether the node is a leader node or a compute node.

PrivateIPAddress -> (string)

The private IP address of a node within a cluster.

PublicIPAddress -> (string)

The public IP address of a node within a cluster.

ElasticIpStatus -> (structure)

The status of the elastic IP (EIP) address.

ElasticIp -> (string)

The elastic IP (EIP) address for the cluster.

Status -> (string)

The status of the elastic IP (EIP) address.

ClusterRevisionNumber -> (string)

The specific revision number of the database in the cluster.

Tags -> (list)

The list of tags for the cluster.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.

KmsKeyId -> (string)

The Key Management Service (KMS) key ID of the encryption key used to encrypt data in the cluster.

EnhancedVpcRouting -> (boolean)

An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.

If this option is `true` , enhanced VPC routing is enabled.

Default: false

IamRoles -> (list)

A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services.

(structure)

An Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other Amazon Web Services services.

IamRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role, for example, `arn:aws:iam::123456789012:role/RedshiftCopyUnload` .

ApplyStatus -> (string)

A value that describes the status of the IAM roleâs association with an Amazon Redshift cluster.

The following are possible statuses and descriptions.

- `in-sync` : The role is available for use by the cluster.
- `adding` : The role is in the process of being associated with the cluster.
- `removing` : The role is in the process of being disassociated with the cluster.

PendingActions -> (list)

Cluster operations that are waiting to be started.

(string)

MaintenanceTrackName -> (string)

The name of the maintenance track for the cluster.

ElasticResizeNumberOfNodeOptions -> (string)

The number of nodes that you can resize the cluster to with the elastic resize method.

DeferredMaintenanceWindows -> (list)

Describes a group of `DeferredMaintenanceWindow` objects.

(structure)

Describes a deferred maintenance window

DeferMaintenanceIdentifier -> (string)

A unique identifier for the maintenance window.

DeferMaintenanceStartTime -> (timestamp)

A timestamp for the beginning of the time period when we defer maintenance.

DeferMaintenanceEndTime -> (timestamp)

A timestamp for the end of the time period when we defer maintenance.

SnapshotScheduleIdentifier -> (string)

A unique identifier for the cluster snapshot schedule.

SnapshotScheduleState -> (string)

The current state of the cluster snapshot schedule.

ExpectedNextSnapshotScheduleTime -> (timestamp)

The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled.

ExpectedNextSnapshotScheduleTimeStatus -> (string)

The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:

- OnTrack - The next snapshot is expected to be taken on time.
- Pending - The next snapshot is pending to be taken.

NextMaintenanceWindowStartTime -> (timestamp)

The date and time in UTC when system maintenance can begin.

ResizeInfo -> (structure)

Returns the following:

- AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.
- ResizeType: Returns ClassicResize

ResizeType -> (string)

Returns the value `ClassicResize` .

AllowCancelResize -> (boolean)

A boolean value indicating if the resize operation can be cancelled.

AvailabilityZoneRelocationStatus -> (string)

Describes the status of the Availability Zone relocation operation.

ClusterNamespaceArn -> (string)

The namespace Amazon Resource Name (ARN) of the cluster.

TotalStorageCapacityInMegaBytes -> (long)

The total storage capacity of the cluster in megabytes.

AquaConfiguration -> (structure)

This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).

AquaStatus -> (string)

This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).

AquaConfigurationStatus -> (string)

This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).

DefaultIamRoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role set as default for the cluster.

ReservedNodeExchangeStatus -> (structure)

The status of the reserved-node exchange request. Statuses include in-progress and requested.

ReservedNodeExchangeRequestId -> (string)

The identifier of the reserved-node exchange request.

Status -> (string)

The status of the reserved-node exchange request. Statuses include in-progress and requested.

RequestTime -> (timestamp)

A date and time that indicate when the reserved-node exchange was requested.

SourceReservedNodeId -> (string)

The identifier of the source reserved node.

SourceReservedNodeType -> (string)

The source reserved-node type, for example ra3.4xlarge.

SourceReservedNodeCount -> (integer)

The source reserved-node count in the cluster.

TargetReservedNodeOfferingId -> (string)

The identifier of the target reserved node offering.

TargetReservedNodeType -> (string)

The node type of the target reserved node, for example ra3.4xlarge.

TargetReservedNodeCount -> (integer)

The count of target reserved nodes in the cluster.

CustomDomainName -> (string)

The custom domain name associated with the cluster.

CustomDomainCertificateArn -> (string)

The certificate Amazon Resource Name (ARN) for the custom domain name.

CustomDomainCertificateExpiryDate -> (timestamp)

The expiration date for the certificate associated with the custom domain name.

MasterPasswordSecretArn -> (string)

The Amazon Resource Name (ARN) for the clusterâs admin user credentials secret.

MasterPasswordSecretKmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt and store the clusterâs admin credentials secret.

IpAddressType -> (string)

The IP address type for the cluster. Possible values are `ipv4` and `dualstack` .

MultiAZ -> (string)

A boolean value that, if true, indicates that the cluster is deployed in two Availability Zones.

MultiAZSecondary -> (structure)

The secondary compute unit of a cluster, if Multi-AZ deployment is turned on.

AvailabilityZone -> (string)

The name of the Availability Zone in which the secondary compute unit of the cluster is located.

ClusterNodes -> (list)

The nodes in the secondary compute unit.

(structure)

The identifier of a node in a cluster.

NodeRole -> (string)

Whether the node is a leader node or a compute node.

PrivateIPAddress -> (string)

The private IP address of a node within a cluster.

PublicIPAddress -> (string)

The public IP address of a node within a cluster.