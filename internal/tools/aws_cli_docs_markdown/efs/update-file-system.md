# update-file-systemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/update-file-system.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/update-file-system.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# update-file-system

## Description

Updates the throughput mode or the amount of provisioned throughput of an existing file system.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/UpdateFileSystem)

## Synopsis

```
update-file-system
--file-system-id <value>
[--throughput-mode <value>]
[--provisioned-throughput-in-mibps <value>]
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

The ID of the file system that you want to update.

`--throughput-mode` (string)

(Optional) Updates the file systemâs throughput mode. If youâre not updating your throughput mode, you donât need to provide this value in your request. If you are changing the `ThroughputMode` to `provisioned` , you must also set a value for `ProvisionedThroughputInMibps` .

Possible values:

- `bursting`
- `provisioned`
- `elastic`

`--provisioned-throughput-in-mibps` (double)

(Optional) The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that youâre creating. Required if `ThroughputMode` is set to `provisioned` . Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see [Amazon EFS quotas that you can increase](https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits) in the *Amazon EFS User Guide* .

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