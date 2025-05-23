# create-replication-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-replication-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-replication-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# create-replication-configuration

## Description

Creates a replication conï¬guration to either a new or existing EFS file system. For more information, see [Amazon EFS replication](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html) in the *Amazon EFS User Guide* . The replication configuration specifies the following:

- **Source file system** â The EFS file system that you want to replicate.
- **Destination file system** â The destination file system to which the source file system is replicated. There can only be one destination file system in a replication configuration.

### Note

A file system can be part of only one replication configuration.

The destination parameters for the replication configuration depend on whether you are replicating to a new file system or to an existing file system, and if you are replicating across Amazon Web Services accounts. See  DestinationToCreate for more information.

This operation requires permissions for the `elasticfilesystem:CreateReplicationConfiguration` action. Additionally, other permissions are required depending on how you are replicating file systems. For more information, see [Required permissions for replication](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html#efs-replication-permissions) in the *Amazon EFS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateReplicationConfiguration)

## Synopsis

```
create-replication-configuration
--source-file-system-id <value>
--destinations <value>
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

`--source-file-system-id` (string)

Specifies the Amazon EFS file system that you want to replicate. This file system cannot already be a source or destination file system in another replication configuration.

`--destinations` (list)

An array of destination configuration objects. Only one destination configuration object is supported.

(structure)

Describes the new or existing destination file system for the replication configuration.

- If you want to replicate to a new file system, do not specify the File System ID for the destination file system. Amazon EFS creates a new, empty file system. For One Zone storage, specify the Availability Zone to create the file system in. To use an Key Management Service key other than the default KMS key, then specify it. For more information, see [Configuring replication to new Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/create-replication.html) in the *Amazon EFS User Guide* .

### Note

After the file system is created, you cannot change the KMS key or the performance mode.

- If you want to replicate to an existing file system thatâs in the same account as the source file system, then you need to provide the ID or Amazon Resource Name (ARN) of the file system to which to replicate. The file systemâs replication overwrite protection must be disabled. For more information, see [Replicating to an existing file system](https://docs.aws.amazon.com/efs/latest/ug/efs-replication#replicate-existing-destination) in the *Amazon EFS User Guide* .
- If you are replicating the file system to a file system thatâs in a different account than the source file system (cross-account replication), you need to provide the ARN for the file system and the IAM role that allows Amazon EFS to perform replication on the destination account. The file systemâs replication overwrite protection must be disabled. For more information, see [Replicating across Amazon Web Services accounts](https://docs.aws.amazon.com/efs/latest/ug/cross-account-replication.html) in the *Amazon EFS User Guide* .

Region -> (string)

To create a file system that uses Regional storage, specify the Amazon Web Services Region in which to create the destination file system. The Region must be enabled for the Amazon Web Services account that owns the source file system. For more information, see [Managing Amazon Web Services Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) in the *Amazon Web Services General Reference Reference Guide* .

AvailabilityZoneName -> (string)

To create a file system that uses One Zone storage, specify the name of the Availability Zone in which to create the destination file system.

KmsKeyId -> (string)

Specify the Key Management Service (KMS) key that you want to use to encrypt the destination file system. If you do not specify a KMS key, Amazon EFS uses your default KMS key for Amazon EFS, `/aws/elasticfilesystem` . This ID can be in one of the following formats:

- Key ID - The unique identifier of the key, for example `1234abcd-12ab-34cd-56ef-1234567890ab` .
- ARN - The ARN for the key, for example `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab` .
- Key alias - A previously created display name for a key, for example `alias/projectKey1` .
- Key alias ARN - The ARN for a key alias, for example `arn:aws:kms:us-west-2:444455556666:alias/projectKey1` .

FileSystemId -> (string)

The ID or ARN of the file system to use for the destination. For cross-account replication, this must be an ARN. The file systemâs replication overwrite replication must be disabled. If no ID or ARN is specified, then a new file system is created.

RoleArn -> (string)

Amazon Resource Name (ARN) of the IAM role in the source account that allows Amazon EFS to perform replication on its behalf. This is optional for same-account replication and required for cross-account replication.

Shorthand Syntax:

```
Region=string,AvailabilityZoneName=string,KmsKeyId=string,FileSystemId=string,RoleArn=string ...
```

JSON Syntax:

```
[
  {
    "Region": "string",
    "AvailabilityZoneName": "string",
    "KmsKeyId": "string",
    "FileSystemId": "string",
    "RoleArn": "string"
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

## Output

SourceFileSystemId -> (string)

The ID of the source Amazon EFS file system that is being replicated.

SourceFileSystemRegion -> (string)

The Amazon Web Services Region in which the source EFS file system is located.

SourceFileSystemArn -> (string)

The Amazon Resource Name (ARN) of the current source file system in the replication configuration.

OriginalSourceFileSystemArn -> (string)

The Amazon Resource Name (ARN) of the original source EFS file system in the replication configuration.

CreationTime -> (timestamp)

Describes when the replication configuration was created.

Destinations -> (list)

An array of destination objects. Only one destination object is supported.

(structure)

Describes the destination file system in the replication configuration.

Status -> (string)

Describes the status of the replication configuration. For more information about replication status, see [Viewing replication details](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html) in the *Amazon EFS User Guide* .

FileSystemId -> (string)

The ID of the destination Amazon EFS file system.

Region -> (string)

The Amazon Web Services Region in which the destination file system is located.

LastReplicatedTimestamp -> (timestamp)

The time when the most recent sync was successfully completed on the destination file system. Any changes to data on the source file system that occurred before this time have been successfully replicated to the destination file system. Any changes that occurred after this time might not be fully replicated.

OwnerId -> (string)

ID of the Amazon Web Services account in which the destination file system resides.

StatusMessage -> (string)

Message that provides details about the `PAUSED` or `ERRROR` state of the replication destination configuration. For more information about replication status messages, see [Viewing replication details](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html) in the *Amazon EFS User Guide* .

RoleArn -> (string)

Amazon Resource Name (ARN) of the IAM role in the source account that allows Amazon EFS to perform replication on its behalf. This is optional for same-account replication and required for cross-account replication.

SourceFileSystemOwnerId -> (string)

ID of the Amazon Web Services account in which the source file system resides.