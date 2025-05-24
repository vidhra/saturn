# create-file-systemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# create-file-system

## Description

Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the callerâs Amazon Web Services account with the specified creation token, this operation does the following:

- Creates a new, empty file system. The file system will have an Amazon EFS assigned ID, and an initial lifecycle state `creating` .
- Returns with the description of the created file system.

Otherwise, this operation returns a `FileSystemAlreadyExists` error with the ID of the existing file system.

### Note

For basic use cases, you can use a randomly generated UUID for the creation token.

The idempotent operation allows you to retry a `CreateFileSystem` call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the `FileSystemAlreadyExists` error.

For more information, see [Creating a file system](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html#creating-using-create-fs-part1) in the *Amazon EFS User Guide* .

### Note

The `CreateFileSystem` call returns while the file systemâs lifecycle state is still `creating` . You can check the file system creation status by calling the  DescribeFileSystems operation, which among other things returns the file system state.

This operation accepts an optional `PerformanceMode` parameter that you choose for your file system. We recommend `generalPurpose` `PerformanceMode` for all file systems. The `maxIO` mode is a previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies than the `generalPurpose` mode. `MaxIO` mode is not supported for One Zone file systems or file systems that use Elastic throughput.

The `PerformanceMode` canât be changed after the file system has been created. For more information, see [Amazon EFS performance modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes.html) .

You can set the throughput mode for the file system using the `ThroughputMode` parameter.

After the file system is fully created, Amazon EFS sets its lifecycle state to `available` , at which point you can create one or more mount targets for the file system in your VPC. For more information, see  CreateMountTarget . You mount your Amazon EFS file system on an EC2 instances in your VPC by using the mount target. For more information, see [Amazon EFS: How it Works](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html) .

This operation requires permissions for the `elasticfilesystem:CreateFileSystem` action.

File systems can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the `elasticfilesystem:TagResource` action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the `elasticfilesystem:TagResource` action. For more information, see [Granting permissions to tag resources during creation](https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateFileSystem)

## Synopsis

```
create-file-system
[--creation-token <value>]
[--performance-mode <value>]
[--encrypted | --no-encrypted]
[--kms-key-id <value>]
[--throughput-mode <value>]
[--provisioned-throughput-in-mibps <value>]
[--availability-zone-name <value>]
[--backup | --no-backup]
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

`--creation-token` (string)

A string of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.

`--performance-mode` (string)

The performance mode of the file system. We recommend `generalPurpose` performance mode for all file systems. File systems using the `maxIO` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode canât be changed after the file system has been created. The `maxIO` mode is not supported on One Zone file systems.

### Warning

Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.

Default is `generalPurpose` .

Possible values:

- `generalPurpose`
- `maxIO`

`--encrypted` | `--no-encrypted` (boolean)

A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying an existing Key Management Service key (KMS key). If you donât specify a KMS key, then the default KMS key for Amazon EFS, `/aws/elasticfilesystem` , is used to protect the encrypted file system.

`--kms-key-id` (string)

The ID of the KMS key that you want to use to protect the encrypted file system. This parameter is required only if you want to use a non-default KMS key. If this parameter is not specified, the default KMS key for Amazon EFS is used. You can specify a KMS key ID using the following formats:

- Key ID - A unique identifier of the key, for example `1234abcd-12ab-34cd-56ef-1234567890ab` .
- ARN - An Amazon Resource Name (ARN) for the key, for example `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Key alias - A previously created display name for a key, for example `alias/projectKey1` .
- Key alias ARN - An ARN for a key alias, for example `arn:aws:kms:us-west-2:444455556666:alias/projectKey1` .

If you use `KmsKeyId` , you must set the  CreateFileSystemRequest$Encrypted parameter to true.

### Warning

EFS accepts only symmetric KMS keys. You cannot use asymmetric KMS keys with Amazon EFS file systems.

`--throughput-mode` (string)

Specifies the throughput mode for the file system. The mode can be `bursting` , `provisioned` , or `elastic` . If you set `ThroughputMode` to `provisioned` , you must also set a value for `ProvisionedThroughputInMibps` . After you create the file system, you can decrease your file systemâs Provisioned throughput or change between the throughput modes, with certain time restrictions. For more information, see [Specifying throughput with provisioned mode](https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput) in the *Amazon EFS User Guide* .

Default is `bursting` .

Possible values:

- `bursting`
- `provisioned`
- `elastic`

`--provisioned-throughput-in-mibps` (double)

The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that youâre creating. Required if `ThroughputMode` is set to `provisioned` . Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see [Amazon EFS quotas that you can increase](https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits) in the *Amazon EFS User Guide* .

`--availability-zone-name` (string)

For One Zone file systems, specify the Amazon Web Services Availability Zone in which to create the file system. Use the format `us-east-1a` to specify the Availability Zone. For more information about One Zone file systems, see [EFS file system types](https://docs.aws.amazon.com/efs/latest/ug/availability-durability.html#file-system-type) in the *Amazon EFS User Guide* .

### Note

One Zone file systems are not available in all Availability Zones in Amazon Web Services Regions where Amazon EFS is available.

`--backup` | `--no-backup` (boolean)

Specifies whether automatic backups are enabled on the file system that you are creating. Set the value to `true` to enable automatic backups. If you are creating a One Zone file system, automatic backups are enabled by default. For more information, see [Automatic backups](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#automatic-backups) in the *Amazon EFS User Guide* .

Default is `false` . However, if you specify an `AvailabilityZoneName` , the default is `true` .

### Note

Backup is not available in all Amazon Web Services Regions where Amazon EFS is available.

`--tags` (list)

Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a `"Key":"Name","Value":"{value}"` key-value pair. Each key must be unique. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:`+ - = . _ : /` .

Key -> (string)

The tag key (String). The key canât start with `aws:` .

Value -> (string)

The value of the tag key.

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

**To create an encrypted file system**

The following `create-file-system` example creates an encrypted file system using the default CMK. It also adds the tag `Name=my-file-system`.

```
aws efs create-file-system \
    --performance-mode generalPurpose \
    --throughput-mode bursting \
    --encrypted \
    --tags Key=Name,Value=my-file-system
```

Output:

```
{
    "OwnerId": "123456789012",
    "CreationToken": "console-d7f56c5f-e433-41ca-8307-9d9c0example",
    "FileSystemId": "fs-c7a0456e",
    "FileSystemArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-48499b4d",
    "CreationTime": 1595286880.0,
    "LifeCycleState": "creating",
    "Name": "my-file-system",
    "NumberOfMountTargets": 0,
    "SizeInBytes": {
        "Value": 0,
        "ValueInIA": 0,
        "ValueInStandard": 0
    },
    "PerformanceMode": "generalPurpose",
    "Encrypted": true,
    "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/a59b3472-e62c-42e4-adcf-30d92example",
    "ThroughputMode": "bursting",
    "Tags": [
        {
            "Key": "Name",
            "Value": "my-file-system"
        }
    ]
}
```

For more information, see [Creating Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html) in the *Amazon Elastic File System User Guide*.

## Output

OwnerId -> (string)

The Amazon Web Services account that created the file system.

CreationToken -> (string)

The opaque string specified in the request.

FileSystemId -> (string)

The ID of the file system, assigned by Amazon EFS.

FileSystemArn -> (string)

The Amazon Resource Name (ARN) for the EFS file system, in the format `arn:aws:elasticfilesystem:*region* :*account-id* :file-system/*file-system-id* `` . Example with sample data: ``arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-01234567`

CreationTime -> (timestamp)

The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

LifeCycleState -> (string)

The lifecycle phase of the file system.

Name -> (string)

You can add tags to a file system, including a `Name` tag. For more information, see  CreateFileSystem . If the file system has a `Name` tag, Amazon EFS returns the value in this field.

NumberOfMountTargets -> (integer)

The current number of mount targets that the file system has. For more information, see  CreateMountTarget .

SizeInBytes -> (structure)

The latest known metered size (in bytes) of data stored in the file system, in its `Value` field, and the time at which that size was determined in its `Timestamp` field. The `Timestamp` value is the integer number of seconds since 1970-01-01T00:00:00Z. The `SizeInBytes` value doesnât represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, `SizeInBytes` represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time.

Value -> (long)

The latest known metered size (in bytes) of data stored in the file system.

Timestamp -> (timestamp)

The time at which the size of data, returned in the `Value` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

ValueInIA -> (long)

The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.

ValueInStandard -> (long)

The latest known metered size (in bytes) of data stored in the Standard storage class.

ValueInArchive -> (long)

The latest known metered size (in bytes) of data stored in the Archive storage class.

PerformanceMode -> (string)

The performance mode of the file system.

Encrypted -> (boolean)

A Boolean value that, if true, indicates that the file system is encrypted.

KmsKeyId -> (string)

The ID of an KMS key used to protect the encrypted file system.

ThroughputMode -> (string)

Displays the file systemâs throughput mode. For more information, see [Throughput modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes) in the *Amazon EFS User Guide* .

ProvisionedThroughputInMibps -> (double)

The amount of provisioned throughput, measured in MiBps, for the file system. Valid for file systems using `ThroughputMode` set to `provisioned` .

AvailabilityZoneName -> (string)

Describes the Amazon Web Services Availability Zone in which the file system is located, and is valid only for One Zone file systems. For more information, see [Using EFS storage classes](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html) in the *Amazon EFS User Guide* .

AvailabilityZoneId -> (string)

The unique and consistent identifier of the Availability Zone in which the file system is located, and is valid only for One Zone file systems. For example, `use1-az1` is an Availability Zone ID for the us-east-1 Amazon Web Services Region, and it has the same location in every Amazon Web Services account.

Tags -> (list)

The tags associated with the file system, presented as an array of `Tag` objects.

(structure)

A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:`+ - = . _ : /` .

Key -> (string)

The tag key (String). The key canât start with `aws:` .

Value -> (string)

The value of the tag key.

FileSystemProtection -> (structure)

Describes the protection on the file system.

ReplicationOverwriteProtection -> (string)

The status of the file systemâs replication overwrite protection.

- `ENABLED` â The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is `ENABLED` by default.
- `DISABLED` â The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.
- `REPLICATING` â The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by EFS replication.

If the replication configuration is deleted, the file systemâs replication overwrite protection is re-enabled, the file system becomes writeable.