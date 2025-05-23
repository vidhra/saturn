# modify-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# modify-cluster

## Description

Modifies the settings for a cluster.

You can also change node type and the number of nodes to scale up or down the cluster. When resizing a cluster, you must specify both the number of nodes and the node type even if one of the parameters does not change.

You can add another security or parameter group, or change the admin user password. Resetting a cluster password or modifying the security groups associated with a cluster do not need a reboot. However, modifying a parameter group requires a reboot for parameters to take effect. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide* .

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:

- Creating a public cluster
- Restoring a public cluster
- Modifying a private cluster to be public
- Adding a subnet with VPC BPA turned on to the subnet group when thereâs at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/ModifyCluster)

## Synopsis

```
modify-cluster
--cluster-identifier <value>
[--cluster-type <value>]
[--node-type <value>]
[--number-of-nodes <value>]
[--cluster-security-groups <value>]
[--vpc-security-group-ids <value>]
[--master-user-password <value>]
[--cluster-parameter-group-name <value>]
[--automated-snapshot-retention-period <value>]
[--manual-snapshot-retention-period <value>]
[--preferred-maintenance-window <value>]
[--cluster-version <value>]
[--allow-version-upgrade | --no-allow-version-upgrade]
[--hsm-client-certificate-identifier <value>]
[--hsm-configuration-identifier <value>]
[--new-cluster-identifier <value>]
[--publicly-accessible | --no-publicly-accessible]
[--elastic-ip <value>]
[--enhanced-vpc-routing | --no-enhanced-vpc-routing]
[--maintenance-track-name <value>]
[--encrypted | --no-encrypted]
[--kms-key-id <value>]
[--availability-zone-relocation | --no-availability-zone-relocation]
[--availability-zone <value>]
[--port <value>]
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

The unique identifier of the cluster to be modified.

Example: `examplecluster`

`--cluster-type` (string)

The new cluster type.

When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use  DescribeResize to track the progress of the resize request.

Valid Values: `multi-node | single-node`

`--node-type` (string)

The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.

For more information about resizing clusters, go to [Resizing Clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html) in the *Amazon Redshift Cluster Management Guide* .

Valid Values: `dc2.large` | `dc2.8xlarge` | `ra3.large` | `ra3.xlplus` | `ra3.4xlarge` | `ra3.16xlarge`

`--number-of-nodes` (integer)

The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.

For more information about resizing clusters, go to [Resizing Clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html) in the *Amazon Redshift Cluster Management Guide* .

Valid Values: Integer greater than `0` .

`--cluster-security-groups` (list)

A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.

Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.

Constraints:

- Must be 1 to 255 alphanumeric characters or hyphens
- First character must be a letter
- Cannot end with a hyphen or contain two consecutive hyphens

(string)

Syntax:

```
"string" "string" ...
```

`--vpc-security-group-ids` (list)

A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.

(string)

Syntax:

```
"string" "string" ...
```

`--master-user-password` (string)

The new password for the cluster admin user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the `MasterUserPassword` element exists in the `PendingModifiedValues` element of the operation response.

You canât use `MasterUserPassword` if `ManageMasterPassword` is `true` .

### Note

Operations never return the password, so this operation provides a way to regain access to the admin user account for a cluster if the password is lost.

Default: Uses existing setting.

Constraints:

- Must be between 8 and 64 characters in length.
- Must contain at least one uppercase letter.
- Must contain at least one lowercase letter.
- Must contain one number.
- Can be any printable ASCII character (ASCII code 33-126) except `'` (single quote), `"` (double quote), `\` , `/` , or `@` .

`--cluster-parameter-group-name` (string)

The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use  RebootCluster .

Default: Uses existing setting.

Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.

`--automated-snapshot-retention-period` (integer)

The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with  CreateClusterSnapshot .

If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.

You canât disable automated snapshots for RA3 node types. Set the automated retention period from 1-35 days.

Default: Uses existing setting.

Constraints: Must be a value from 0 to 35.

`--manual-snapshot-retention-period` (integer)

The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesnât retroactively change the retention periods of existing manual snapshots.

The value must be either -1 or an integer between 1 and 3,653.

The default value is -1.

`--preferred-maintenance-window` (string)

The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.

This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.

Default: Uses existing setting.

Format: ddd:hh24:mi-ddd:hh24:mi, for example `wed:07:30-wed:08:00` .

Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun

Constraints: Must be at least 30 minutes.

`--cluster-version` (string)

The new version number of the Amazon Redshift engine to upgrade to.

For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide* .

Example: `1.0`

`--allow-version-upgrade` | `--no-allow-version-upgrade` (boolean)

If `true` , major version upgrades will be applied automatically to the cluster during the maintenance window.

Default: `false`

`--hsm-client-certificate-identifier` (string)

Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.

`--hsm-configuration-identifier` (string)

Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.

`--new-cluster-identifier` (string)

The new identifier for the cluster.

Constraints:

- Must contain from 1 to 63 alphanumeric characters or hyphens.
- Alphabetic characters must be lowercase.
- First character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.
- Must be unique for all clusters within an Amazon Web Services account.

Example: `examplecluster`

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

If `true` , the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.

Default: false

`--elastic-ip` (string)

The Elastic IP (EIP) address for the cluster.

Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to [Supported Platforms to Launch Your Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms) in the Amazon Redshift Cluster Management Guide.

`--enhanced-vpc-routing` | `--no-enhanced-vpc-routing` (boolean)

An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.

If this option is `true` , enhanced VPC routing is enabled.

Default: false

`--maintenance-track-name` (string)

The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the `PendingModifiedValues` for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.

`--encrypted` | `--no-encrypted` (boolean)

Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the `KmsKeyId` parameter, we encrypt the cluster with the provided `KmsKeyId` . If you donât provide a `KmsKeyId` , we encrypt with the default key.

If the value is not encrypted (false), then the cluster is decrypted.

`--kms-key-id` (string)

The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.

`--availability-zone-relocation` | `--no-availability-zone-relocation` (boolean)

The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.

`--availability-zone` (string)

The option to initiate relocation for an Amazon Redshift cluster to the target Availability Zone.

`--port` (integer)

The option to change the port of an Amazon Redshift cluster.

Valid Values:

- For clusters with ra3 nodes - Select a port within the ranges `5431-5455` or `8191-8215` . (If you have an existing cluster with ra3 nodes, it isnât required that you change the port to these ranges.)
- For clusters with dc2 nodes - Select a port within the range `1150-65535` .

`--manage-master-password` | `--no-manage-master-password` (boolean)

If `true` , Amazon Redshift uses Secrets Manager to manage this clusterâs admin credentials. You canât use `MasterUserPassword` if `ManageMasterPassword` is true. If `ManageMasterPassword` is false or not set, Amazon Redshift uses `MasterUserPassword` for the admin user accountâs password.

`--master-password-secret-kms-key-id` (string)

The ID of the Key Management Service (KMS) key used to encrypt and store the clusterâs admin credentials secret. You can only use this parameter if `ManageMasterPassword` is true.

`--ip-address-type` (string)

The IP address types that the cluster supports. Possible values are `ipv4` and `dualstack` .

`--multi-az` | `--no-multi-az` (boolean)

If true and the cluster is currently only deployed in a single Availability Zone, the cluster will be modified to be deployed in two Availability Zones.

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

### Associate a Security Group with a Cluster

This example shows how to associate a cluster security group with the specified cluster.

Command:

```
aws redshift modify-cluster --cluster-identifier mycluster --cluster-security-groups mysecuritygroup
```

### Modify the Maintenance Window for a Cluster

This shows how to change the weekly preferred maintenance window for a cluster to be the minimum four hour window
starting Sundays at 11:15 PM, and ending Mondays at 3:15 AM.

Command:

```
aws redshift modify-cluster --cluster-identifier mycluster --preferred-maintenance-window Sun:23:15-Mon:03:15
```

### Change the Master Password for the Cluster

This example shows how to change the master password for a cluster.

Command:

```
aws redshift modify-cluster --cluster-identifier mycluster --master-user-password A1b2c3d4
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