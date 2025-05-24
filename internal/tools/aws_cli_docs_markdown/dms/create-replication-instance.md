# create-replication-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# create-replication-instance

## Description

Creates the replication instance using the specified parameters.

DMS requires that your account have certain roles with appropriate permissions before you can create a replication instance. For information on the required roles, see [Creating the IAM Roles to Use With the CLI and DMS API](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.APIRole) . For information on the required permissions, see [IAM Permissions Needed to Use DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions) .

### Note

If you donât specify a version when creating a replication instance, DMS will create the instance using the default engine version. For information about the default engine version, see [Release Notes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationInstance)

## Synopsis

```
create-replication-instance
--replication-instance-identifier <value>
[--allocated-storage <value>]
--replication-instance-class <value>
[--vpc-security-group-ids <value>]
[--availability-zone <value>]
[--replication-subnet-group-identifier <value>]
[--preferred-maintenance-window <value>]
[--multi-az | --no-multi-az]
[--engine-version <value>]
[--auto-minor-version-upgrade | --no-auto-minor-version-upgrade]
[--tags <value>]
[--kms-key-id <value>]
[--publicly-accessible | --no-publicly-accessible]
[--dns-name-servers <value>]
[--resource-identifier <value>]
[--network-type <value>]
[--kerberos-authentication-settings <value>]
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

`--replication-instance-identifier` (string)

The replication instance identifier. This parameter is stored as a lowercase string.

Constraints:

- Must contain 1-63 alphanumeric characters or hyphens.
- First character must be a letter.
- Canât end with a hyphen or contain two consecutive hyphens.

Example: `myrepinstance`

`--allocated-storage` (integer)

The amount of storage (in gigabytes) to be initially allocated for the replication instance.

`--replication-instance-class` (string)

The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to `"dms.c4.large"` .

For more information on the settings and capacities for the available replication instance classes, see [`Choosing the right DMS replication instance <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html >`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html#id1) ; and, [Selecting the best size for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html) .

`--vpc-security-group-ids` (list)

Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.

(string)

Syntax:

```
"string" "string" ...
```

`--availability-zone` (string)

The Availability Zone where the replication instance will be created. The default value is a random, system-chosen Availability Zone in the endpointâs Amazon Web Services Region, for example: `us-east-1d` .

`--replication-subnet-group-identifier` (string)

A subnet group to associate with the replication instance.

`--preferred-maintenance-window` (string)

The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).

Format: `ddd:hh24:mi-ddd:hh24:mi`

Default: A 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region, occurring on a random day of the week.

Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun

Constraints: Minimum 30-minute window.

`--multi-az` | `--no-multi-az` (boolean)

Specifies whether the replication instance is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true` .

`--engine-version` (string)

The engine version number of the replication instance.

If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.

`--auto-minor-version-upgrade` | `--no-auto-minor-version-upgrade` (boolean)

A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to `true` .

Default: `true`

`--tags` (list)

One or more tags to be assigned to the replication instance.

(structure)

A user-defined key-value pair that describes metadata added to an DMS resource and that is used by operations such as the following:

- `AddTagsToResource`
- `ListTagsForResource`
- `RemoveTagsFromResource`

Key -> (string)

A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

ResourceArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the resource for which the tag is created.

Shorthand Syntax:

```
Key=string,Value=string,ResourceArn=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "ResourceArn": "string"
  }
  ...
]
```

`--kms-key-id` (string)

An KMS key identifier that is used to encrypt the data on the replication instance.

If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies the accessibility options for the replication instance. A value of `true` represents an instance with a public IP address. A value of `false` represents an instance with a private IP address. The default value is `true` .

`--dns-name-servers` (string)

A list of custom DNS name servers supported for the replication instance to access your on-premise source or target database. This list overrides the default name servers supported by the replication instance. You can specify a comma-separated list of internet addresses for up to four on-premise DNS name servers. For example: `"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"`

`--resource-identifier` (string)

A friendly name for the resource identifier at the end of the `EndpointArn` response parameter that is returned in the created `Endpoint` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen (â-â). Also, it canât end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as `Example-App-ARN1` . For example, this value might result in the `EndpointArn` value `arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1` . If you donât specify a `ResourceIdentifier` value, DMS generates a default identifier value for the end of `EndpointArn` .

`--network-type` (string)

The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.

`--kerberos-authentication-settings` (structure)

Specifies the settings required for kerberos authentication when creating the replication instance.

KeyCacheSecretId -> (string)

Specifies the ID of the secret that stores the key cache file required for kerberos authentication.

KeyCacheSecretIamArn -> (string)

Specifies the Amazon Resource Name (ARN) of the IAM role that grants Amazon Web Services DMS access to the secret containing key cache file for the kerberos authentication.

Krb5FileContents -> (string)

Specifies the contents of krb5 configuration file required for kerberos authentication.

Shorthand Syntax:

```
KeyCacheSecretId=string,KeyCacheSecretIamArn=string,Krb5FileContents=string
```

JSON Syntax:

```
{
  "KeyCacheSecretId": "string",
  "KeyCacheSecretIamArn": "string",
  "Krb5FileContents": "string"
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

**To create a replication instance**

The following `create-replication-instance` example creates a replication instance.

```
aws dms create-replication-instance \
    --replication-instance-identifier my-repl-instance \
    --replication-instance-class dms.t2.micro \
    --allocated-storage 5
```

Output:

```
{
    "ReplicationInstance": {
        "ReplicationInstanceIdentifier": "my-repl-instance",
        "ReplicationInstanceClass": "dms.t2.micro",
        "ReplicationInstanceStatus": "creating",
        "AllocatedStorage": 5,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-f839b688",
                "Status": "active"
            }
        ],
        "ReplicationSubnetGroup": {
            "ReplicationSubnetGroupIdentifier": "default",
            "ReplicationSubnetGroupDescription": "default",
            "VpcId": "vpc-136a4c6a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-da327bf6",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-42599426",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1d"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-bac383e0",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1c"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-6746046b",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1f"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-d7c825e8",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1e"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-cbfff283",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sat:12:35-sat:13:05",
        "PendingModifiedValues": {},
        "MultiAZ": false,
        "EngineVersion": "3.3.2",
        "AutoMinorVersionUpgrade": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a",
        "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:ZK2VQBUWFDBAWHIXHAYG5G2PKY",
        "PubliclyAccessible": true
    }
}
```

For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) in the *AWS Database Migration Service User Guide*.

## Output

ReplicationInstance -> (structure)

The replication instance that was created.

ReplicationInstanceIdentifier -> (string)

The replication instance identifier is a required parameter. This parameter is stored as a lowercase string.

Constraints:

- Must contain 1-63 alphanumeric characters or hyphens.
- First character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `myrepinstance`

ReplicationInstanceClass -> (string)

The compute and memory capacity of the replication instance as defined for the specified replication instance class. It is a required parameter, although a default value is pre-selected in the DMS console.

For more information on the settings and capacities for the available replication instance classes, see [Selecting the right DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth) .

ReplicationInstanceStatus -> (string)

The status of the replication instance. The possible return values include:

- `"available"`
- `"creating"`
- `"deleted"`
- `"deleting"`
- `"failed"`
- `"modifying"`
- `"upgrading"`
- `"rebooting"`
- `"resetting-master-credentials"`
- `"storage-full"`
- `"incompatible-credentials"`
- `"incompatible-network"`
- `"maintenance"`

AllocatedStorage -> (integer)

The amount of storage (in gigabytes) that is allocated for the replication instance.

InstanceCreateTime -> (timestamp)

The time the replication instance was created.

VpcSecurityGroups -> (list)

The VPC security group for the instance.

(structure)

Describes the status of a security group associated with the virtual private cloud (VPC) hosting your replication and DB instances.

VpcSecurityGroupId -> (string)

The VPC security group ID.

Status -> (string)

The status of the VPC security group.

AvailabilityZone -> (string)

The Availability Zone for the instance.

ReplicationSubnetGroup -> (structure)

The subnet group for the replication instance.

ReplicationSubnetGroupIdentifier -> (string)

The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription -> (string)

A description for the replication subnet group.

VpcId -> (string)

The ID of the VPC.

SubnetGroupStatus -> (string)

The status of the subnet group.

Subnets -> (list)

The subnets that are in the subnet group.

(structure)

In response to a request by the `DescribeReplicationSubnetGroups` operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier -> (string)

The subnet identifier.

SubnetAvailabilityZone -> (structure)

The Availability Zone of the subnet.

Name -> (string)

The name of the Availability Zone.

SubnetStatus -> (string)

The status of the subnet.

SupportedNetworkTypes -> (list)

The IP addressing protocol supported by the subnet group. This is used by a replication instance with values such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.

(string)

PreferredMaintenanceWindow -> (string)

The maintenance window times for the replication instance. Any pending upgrades to the replication instance are performed during this time.

PendingModifiedValues -> (structure)

The pending modification values.

ReplicationInstanceClass -> (string)

The compute and memory capacity of the replication instance as defined for the specified replication instance class.

For more information on the settings and capacities for the available replication instance classes, see [Selecting the right DMS replication instance for your migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth) .

AllocatedStorage -> (integer)

The amount of storage (in gigabytes) that is allocated for the replication instance.

MultiAZ -> (boolean)

Specifies whether the replication instance is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true` .

EngineVersion -> (string)

The engine version number of the replication instance.

NetworkType -> (string)

The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.

MultiAZ -> (boolean)

Specifies whether the replication instance is a Multi-AZ deployment. You canât set the `AvailabilityZone` parameter if the Multi-AZ parameter is set to `true` .

EngineVersion -> (string)

The engine version number of the replication instance.

If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.

When modifying a major engine version of an instance, also set `AllowMajorVersionUpgrade` to `true` .

AutoMinorVersionUpgrade -> (boolean)

Boolean value indicating if minor version upgrades will be automatically applied to the instance.

KmsKeyId -> (string)

An KMS key identifier that is used to encrypt the data on the replication instance.

If you donât specify a value for the `KmsKeyId` parameter, then DMS uses your default encryption key.

KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.

ReplicationInstanceArn -> (string)

The Amazon Resource Name (ARN) of the replication instance.

ReplicationInstancePublicIpAddress -> (string)

The public IP address of the replication instance.

ReplicationInstancePrivateIpAddress -> (string)

The private IP address of the replication instance.

ReplicationInstancePublicIpAddresses -> (list)

One or more public IP addresses for the replication instance.

(string)

ReplicationInstancePrivateIpAddresses -> (list)

One or more private IP addresses for the replication instance.

(string)

ReplicationInstanceIpv6Addresses -> (list)

One or more IPv6 addresses for the replication instance.

(string)

PubliclyAccessible -> (boolean)

Specifies the accessibility options for the replication instance. A value of `true` represents an instance with a public IP address. A value of `false` represents an instance with a private IP address. The default value is `true` .

SecondaryAvailabilityZone -> (string)

The Availability Zone of the standby replication instance in a Multi-AZ deployment.

FreeUntil -> (timestamp)

The expiration date of the free replication instance that is part of the Free DMS program.

DnsNameServers -> (string)

The DNS name servers supported for the replication instance to access your on-premise source or target database.

NetworkType -> (string)

The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.

KerberosAuthenticationSettings -> (structure)

Specifies the settings required for kerberos authentication when replicating an instance.

KeyCacheSecretId -> (string)

Specifies the ID of the secret that stores the key cache file required for kerberos authentication.

KeyCacheSecretIamArn -> (string)

Specifies the Amazon Resource Name (ARN) of the IAM role that grants Amazon Web Services DMS access to the secret containing key cache file for the kerberos authentication.

Krb5FileContents -> (string)

Specifies the contents of krb5 configuration file required for kerberos authentication.