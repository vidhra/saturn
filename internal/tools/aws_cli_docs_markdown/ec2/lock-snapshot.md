# lock-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/lock-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/lock-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# lock-snapshot

## Description

Locks an Amazon EBS snapshot in either *governance* or *compliance* mode to protect it against accidental or malicious deletions for a specific duration. A locked snapshot canât be deleted.

You can also use this action to modify the lock settings for a snapshot that is already locked. The allowed modifications depend on the lock mode and lock state:

- If the snapshot is locked in governance mode, you can modify the lock mode and the lock duration or lock expiration date.
- If the snapshot is locked in compliance mode and it is in the cooling-off period, you can modify the lock mode and the lock duration or lock expiration date.
- If the snapshot is locked in compliance mode and the cooling-off period has lapsed, you can only increase the lock duration or extend the lock expiration date.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/LockSnapshot)

## Synopsis

```
lock-snapshot
--snapshot-id <value>
[--dry-run | --no-dry-run]
--lock-mode <value>
[--cool-off-period <value>]
[--lock-duration <value>]
[--expiration-date <value>]
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

`--snapshot-id` (string)

The ID of the snapshot to lock.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--lock-mode` (string)

The mode in which to lock the snapshot. Specify one of the following:

- `governance` - Locks the snapshot in governance mode. Snapshots locked in governance mode canât be deleted until one of the following conditions are met:
- The lock duration expires.
- The snapshot is unlocked by a user with the appropriate permissions.

Users with the appropriate IAM permissions can unlock the snapshot, increase or decrease the lock duration, and change the lock mode to `compliance` at any time.

If you lock a snapshot in `governance` mode, omit **CoolOffPeriod** .

- `compliance` - Locks the snapshot in compliance mode. Snapshots locked in compliance mode canât be unlocked by any user. They can be deleted only after the lock duration expires. Users canât decrease the lock duration or change the lock mode to `governance` . However, users with appropriate IAM permissions can increase the lock duration at any time. If you lock a snapshot in `compliance` mode, you can optionally specify **CoolOffPeriod** .

Possible values:

- `compliance`
- `governance`

`--cool-off-period` (integer)

The cooling-off period during which you can unlock the snapshot or modify the lock settings after locking the snapshot in compliance mode, in hours. After the cooling-off period expires, you canât unlock or delete the snapshot, decrease the lock duration, or change the lock mode. You can increase the lock duration after the cooling-off period expires.

The cooling-off period is optional when locking a snapshot in compliance mode. If you are locking the snapshot in governance mode, omit this parameter.

To lock the snapshot in compliance mode immediately without a cooling-off period, omit this parameter.

If you are extending the lock duration for a snapshot that is locked in compliance mode after the cooling-off period has expired, omit this parameter. If you specify a cooling-period in a such a request, the request fails.

Allowed values: Min 1, max 72.

`--lock-duration` (integer)

The period of time for which to lock the snapshot, in days. The snapshot lock will automatically expire after this period lapses.

You must specify either this parameter or **ExpirationDate** , but not both.

Allowed values: Min: 1, max 36500

`--expiration-date` (timestamp)

The date and time at which the snapshot lock is to automatically expire, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ).

You must specify either this parameter or **LockDuration** , but not both.

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

**Example 1: To lock a snapshot in governance mode**

The following `lock-snapshot` example locks the specified snapshot in governance mode.

```
aws ec2 lock-snapshot \
    --snapshot-id snap-0b5e733b4a8df6e0d \
    --lock-mode governance \
    --lock-duration 365
```

Output:

```
{
    "SnapshotId": "snap-0b5e733b4a8df6e0d",
    "LockState": "governance",
    "LockDuration": 365,
    "LockCreatedOn": "2024-05-05T00:56:06.208000+00:00",
    "LockExpiresOn": "2025-05-05T00:56:06.208000+00:00",
    "LockDurationStartTime": "2024-05-05T00:56:06.208000+00:00"
}
```

For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html) in the *Amazon EBS User Guide*.

**Example 2: To lock a snapshot in compliance mode**

The following `lock-snapshot` example lock the specified snapshot in compliance mode.

```
aws ec2 lock-snapshot \
    --snapshot-id snap-0163a8524c5b9901f \
    --lock-mode compliance \
    --cool-off-period 24 \
    --lock-duration 365
```

Output:

```
{
    "SnapshotId": "snap-0b5e733b4a8df6e0d",
    "LockState": "compliance-cooloff",
    "LockDuration": 365,
    "CoolOffPeriod": 24,
    "CoolOffPeriodExpiresOn": "2024-05-06T01:02:20.527000+00:00",
    "LockCreatedOn": "2024-05-05T01:02:20.527000+00:00",
    "LockExpiresOn": "2025-05-05T01:02:20.527000+00:00",
    "LockDurationStartTime": "2024-05-05T01:02:20.527000+00:00"
}
```

For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html) in the *Amazon EBS User Guide*.

## Output

SnapshotId -> (string)

The ID of the snapshot

LockState -> (string)

The state of the snapshot lock. Valid states include:

- `compliance-cooloff` - The snapshot has been locked in compliance mode but it is still within the cooling-off period. The snapshot canât be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
- `governance` - The snapshot is locked in governance mode. The snapshot canât be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.
- `compliance` - The snapshot is locked in compliance mode and the cooling-off period has expired. The snapshot canât be unlocked or deleted. The lock duration can only be increased by users with appropriate permissions.
- `expired` - The snapshot was locked in compliance or governance mode but the lock duration has expired. The snapshot is not locked and can be deleted.

LockDuration -> (integer)

The period of time for which the snapshot is locked, in days.

CoolOffPeriod -> (integer)

The compliance mode cooling-off period, in hours.

CoolOffPeriodExpiresOn -> (timestamp)

The date and time at which the compliance mode cooling-off period expires, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ).

LockCreatedOn -> (timestamp)

The date and time at which the snapshot was locked, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ).

LockExpiresOn -> (timestamp)

The date and time at which the lock will expire, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ).

LockDurationStartTime -> (timestamp)

The date and time at which the lock duration started, in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ).