# convert-recovery-point-to-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/convert-recovery-point-to-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/convert-recovery-point-to-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# convert-recovery-point-to-snapshot

## Description

Converts a recovery point to a snapshot. For more information about recovery points and snapshots, see [Working with snapshots and recovery points](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/ConvertRecoveryPointToSnapshot)

## Synopsis

```
convert-recovery-point-to-snapshot
--recovery-point-id <value>
[--retention-period <value>]
--snapshot-name <value>
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

`--recovery-point-id` (string)

The unique identifier of the recovery point.

`--retention-period` (integer)

How long to retain the snapshot.

`--snapshot-name` (string)

The name of the snapshot.

`--tags` (list)

An array of [Tag objects](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html) to associate with the created snapshot.

(structure)

A map of key-value pairs.

key -> (string)

The key to use in the tag.

value -> (string)

The value of the tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

snapshot -> (structure)

The snapshot converted from the recovery point.

accountsWithProvisionedRestoreAccess -> (list)

All of the Amazon Web Services accounts that have access to restore a snapshot to a provisioned cluster.

(string)

accountsWithRestoreAccess -> (list)

All of the Amazon Web Services accounts that have access to restore a snapshot to a namespace.

(string)

actualIncrementalBackupSizeInMegaBytes -> (double)

The size of the incremental backup in megabytes.

adminPasswordSecretArn -> (string)

The Amazon Resource Name (ARN) for the namespaceâs admin user credentials secret.

adminPasswordSecretKmsKeyId -> (string)

The ID of the Key Management Service (KMS) key used to encrypt and store the namespaceâs admin credentials secret.

adminUsername -> (string)

The username of the database within a snapshot.

backupProgressInMegaBytes -> (double)

The size in megabytes of the data that has been backed up to a snapshot.

currentBackupRateInMegaBytesPerSecond -> (double)

The rate at which data is backed up into a snapshot in megabytes per second.

elapsedTimeInSeconds -> (long)

The amount of time it took to back up data into a snapshot.

estimatedSecondsToCompletion -> (long)

The estimated amount of seconds until the snapshot completes backup.

kmsKeyId -> (string)

The unique identifier of the KMS key used to encrypt the snapshot.

namespaceArn -> (string)

The Amazon Resource Name (ARN) of the namespace the snapshot was created from.

namespaceName -> (string)

The name of the namepsace.

ownerAccount -> (string)

The owner Amazon Web Services; account of the snapshot.

snapshotArn -> (string)

The Amazon Resource Name (ARN) of the snapshot.

snapshotCreateTime -> (timestamp)

The timestamp of when the snapshot was created.

snapshotName -> (string)

The name of the snapshot.

snapshotRemainingDays -> (integer)

The amount of days until the snapshot is deleted.

snapshotRetentionPeriod -> (integer)

The period of time, in days, of how long the snapshot is retained.

snapshotRetentionStartTime -> (timestamp)

The timestamp of when data within the snapshot started getting retained.

status -> (string)

The status of the snapshot.

totalBackupSizeInMegaBytes -> (double)

The total size, in megabytes, of how big the snapshot is.