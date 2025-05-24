# create-db-shard-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-shard-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-shard-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# create-db-shard-group

## Description

Creates a new DB shard group for Aurora Limitless Database. You must enable Aurora Limitless Database to create a DB shard group.

Valid for: Aurora DB clusters only

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/CreateDBShardGroup)

## Synopsis

```
create-db-shard-group
--db-shard-group-identifier <value>
--db-cluster-identifier <value>
[--compute-redundancy <value>]
--max-acu <value>
[--min-acu <value>]
[--publicly-accessible | --no-publicly-accessible]
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

`--db-shard-group-identifier` (string)

The name of the DB shard group.

`--db-cluster-identifier` (string)

The name of the primary DB cluster for the DB shard group.

`--compute-redundancy` (integer)

Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:

- 0 - Creates a DB shard group without a standby DB shard group. This is the default value.
- 1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).
- 2 - Creates a DB shard group with two standby DB shard groups in two different AZs.

`--max-acu` (double)

The maximum capacity of the DB shard group in Aurora capacity units (ACUs).

`--min-acu` (double)

The minimum capacity of the DB shard group in Aurora capacity units (ACUs).

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies whether the DB shard group is publicly accessible.

When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard groupâs virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard groupâs VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access is not permitted if the security group assigned to the DB shard group doesnât permit it.

When the DB shard group isnât publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.

Default: The default behavior varies depending on whether `DBSubnetGroupName` is specified.

If `DBSubnetGroupName` isnât specified, and `PubliclyAccessible` isnât specified, the following applies:

- If the default VPC in the target Region doesnât have an internet gateway attached to it, the DB shard group is private.
- If the default VPC in the target Region has an internet gateway attached to it, the DB shard group is public.

If `DBSubnetGroupName` is specified, and `PubliclyAccessible` isnât specified, the following applies:

- If the subnets are part of a VPC that doesnât have an internet gateway attached to it, the DB shard group is private.
- If the subnets are part of a VPC that has an internet gateway attached to it, the DB shard group is public.

`--tags` (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create an Aurora PostgreSQL primary DB cluster**

The following `create-db-cluster` example creates an Aurora PostgreSQL SQL primary DB cluster thatâs compatible with Aurora Serverless v2 and Aurora Limitless Database.

```
aws rds create-db-cluster \
    --db-cluster-identifier my-sv2-cluster \
    --engine aurora-postgresql \
    --engine-version 15.2-limitless \
    --storage-type aurora-iopt1 \
    --serverless-v2-scaling-configuration MinCapacity=2,MaxCapacity=16 \
    --enable-limitless-database \
    --master-username myuser \
    --master-user-password mypassword \
    --enable-cloudwatch-logs-exports postgresql
```

Output:

```
{
    "DBCluster": {
        "AllocatedStorage": 1,
        "AvailabilityZones": [
            "us-east-2b",
            "us-east-2c",
            "us-east-2a"
        ],
        "BackupRetentionPeriod": 1,
        "DBClusterIdentifier": "my-sv2-cluster",
        "DBClusterParameterGroup": "default.aurora-postgresql15",
        "DBSubnetGroup": "default",
        "Status": "creating",
        "Endpoint": "my-sv2-cluster.cluster-cekycexample.us-east-2.rds.amazonaws.com",
        "ReaderEndpoint": "my-sv2-cluster.cluster-ro-cekycexample.us-east-2.rds.amazonaws.com",
        "MultiAZ": false,
        "Engine": "aurora-postgresql",
        "EngineVersion": "15.2-limitless",
        "Port": 5432,
        "MasterUsername": "myuser",
        "PreferredBackupWindow": "06:05-06:35",
        "PreferredMaintenanceWindow": "mon:08:25-mon:08:55",
        "ReadReplicaIdentifiers": [],
        "DBClusterMembers": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-########",
                "Status": "active"
            }
        ],
        "HostedZoneId": "Z2XHWR1EXAMPLE",
        "StorageEncrypted": false,
        "DbClusterResourceId": "cluster-XYEDT6ML6FHIXH4Q2J1EXAMPLE",
        "DBClusterArn": "arn:aws:rds:us-east-2:123456789012:cluster:my-sv2-cluster",
        "AssociatedRoles": [],
        "IAMDatabaseAuthenticationEnabled": false,
        "ClusterCreateTime": "2024-02-19T16:24:07.771000+00:00",
        "EnabledCloudwatchLogsExports": [
            "postgresql"
        ],
        "EngineMode": "provisioned",
        "DeletionProtection": false,
        "HttpEndpointEnabled": false,
        "CopyTagsToSnapshot": false,
        "CrossAccountClone": false,
        "DomainMemberships": [],
        "TagList": [],
        "StorageType": "aurora-iopt1",
        "AutoMinorVersionUpgrade": true,
        "ServerlessV2ScalingConfiguration": {
            "MinCapacity": 2.0,
            "MaxCapacity": 16.0
        },
        "NetworkType": "IPV4",
        "IOOptimizedNextAllowedModificationTime": "2024-03-21T16:24:07.781000+00:00",
        "LimitlessDatabase": {
            "Status": "not-in-use",
            "MinRequiredACU": 96.0
        }
    }
}
```

**Example 2: To create the primary (writer) DB instance**

The following `create-db-instance` example creates an Aurora Serverless v2 primary (writer) DB instance. When you use the console to create a DB cluster, Amazon RDS automatically creates the writer DB instance for your DB cluster. However, when you use the AWS CLI to create a DB cluster, you must explicitly create the writer DB instance for your DB cluster using the `create-db-instance` AWS CLI command.

```
aws rds create-db-instance \
    --db-instance-identifier my-sv2-instance \
    --db-cluster-identifier my-sv2-cluster \
    --engine aurora-postgresql \
    --db-instance-class db.serverless
```

Output:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "my-sv2-instance",
        "DBInstanceClass": "db.serverless",
        "Engine": "aurora-postgresql",
        "DBInstanceStatus": "creating",
        "MasterUsername": "myuser",
        "AllocatedStorage": 1,
        "PreferredBackupWindow": "06:05-06:35",
        "BackupRetentionPeriod": 1,
        "DBSecurityGroups": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-########",
                "Status": "active"
            }
        ],
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.aurora-postgresql15",
                "ParameterApplyStatus": "in-sync"
            }
        ],
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-########",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-2c"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-2a"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-########",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-2b"
                    },
                    "SubnetOutpost": {},
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "fri:09:01-fri:09:31",
        "PendingModifiedValues": {
            "PendingCloudwatchLogsExports": {
                "LogTypesToEnable": [
                    "postgresql"
                ]
            }
        },
        "MultiAZ": false,
        "EngineVersion": "15.2-limitless",
        "AutoMinorVersionUpgrade": true,
        "ReadReplicaDBInstanceIdentifiers": [],
        "LicenseModel": "postgresql-license",
        "OptionGroupMemberships": [
            {
                "OptionGroupName": "default:aurora-postgresql-15",
                "Status": "in-sync"
            }
        ],
        "PubliclyAccessible": false,
        "StorageType": "aurora-iopt1",
        "DbInstancePort": 0,
        "DBClusterIdentifier": "my-sv2-cluster",
        "StorageEncrypted": false,
        "DbiResourceId": "db-BIQTE3B3K3RM7M74SK5EXAMPLE",
        "CACertificateIdentifier": "rds-ca-rsa2048-g1",
        "DomainMemberships": [],
        "CopyTagsToSnapshot": false,
        "MonitoringInterval": 0,
        "PromotionTier": 1,
        "DBInstanceArn": "arn:aws:rds:us-east-2:123456789012:db:my-sv2-instance",
        "IAMDatabaseAuthenticationEnabled": false,
        "PerformanceInsightsEnabled": false,
        "DeletionProtection": false,
        "AssociatedRoles": [],
        "TagList": [],
        "CustomerOwnedIpEnabled": false,
        "BackupTarget": "region",
        "NetworkType": "IPV4",
        "StorageThroughput": 0,
        "CertificateDetails": {
            "CAIdentifier": "rds-ca-rsa2048-g1"
        },
        "DedicatedLogVolume": false
    }
}
```

**Example 3: To create the DB shard group**

The following `create-db-shard-group` example creates a DB shard group in your Aurora PostgreSQL primary DB cluster.

```
aws rds create-db-shard-group \
    --db-shard-group-identifier my-db-shard-group \
    --db-cluster-identifier my-sv2-cluster \
    --max-acu 768
```

Output:

```
{
    "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890",
    "DBShardGroupIdentifier": "my-db-shard-group",
    "DBClusterIdentifier": "my-sv2-cluster",
    "MaxACU": 768.0,
    "ComputeRedundancy": 0,
    "Status": "creating",
    "PubliclyAccessible": false,
    "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com"
}
```

For more information, see [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.

## Output

DBShardGroupResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the DB shard group.

DBShardGroupIdentifier -> (string)

The name of the DB shard group.

DBClusterIdentifier -> (string)

The name of the primary DB cluster for the DB shard group.

MaxACU -> (double)

The maximum capacity of the DB shard group in Aurora capacity units (ACUs).

MinACU -> (double)

The minimum capacity of the DB shard group in Aurora capacity units (ACUs).

ComputeRedundancy -> (integer)

Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:

- 0 - Creates a DB shard group without a standby DB shard group. This is the default value.
- 1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).
- 2 - Creates a DB shard group with two standby DB shard groups in two different AZs.

Status -> (string)

The status of the DB shard group.

PubliclyAccessible -> (boolean)

Indicates whether the DB shard group is publicly accessible.

When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard groupâs virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard groupâs VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access isnât permitted if the security group assigned to the DB shard group doesnât permit it.

When the DB shard group isnât publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.

For more information, see  CreateDBShardGroup .

This setting is only for Aurora Limitless Database.

Endpoint -> (string)

The connection endpoint for the DB shard group.

DBShardGroupArn -> (string)

The Amazon Resource Name (ARN) for the DB shard group.

TagList -> (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).