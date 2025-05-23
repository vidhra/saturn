# enable-fast-snapshot-restoresÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# enable-fast-snapshot-restores

## Description

Enables fast snapshot restores for the specified snapshots in the specified Availability Zones.

You get the full benefit of fast snapshot restores after they enter the `enabled` state. To get the current state of fast snapshot restores, use  DescribeFastSnapshotRestores . To disable fast snapshot restores, use  DisableFastSnapshotRestores .

For more information, see [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html) in the *Amazon EBS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/EnableFastSnapshotRestores)

## Synopsis

```
enable-fast-snapshot-restores
--availability-zones <value>
--source-snapshot-ids <value>
[--dry-run | --no-dry-run]
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

`--availability-zones` (list)

One or more Availability Zones. For example, `us-east-2a` .

(string)

Syntax:

```
"string" "string" ...
```

`--source-snapshot-ids` (list)

The IDs of one or more snapshots. For example, `snap-1234567890abcdef0` . You can specify a snapshot that was shared with you from another Amazon Web Services account.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To enable fast snapshot restore**

The following `enable-fast-snapshot-restores` example enables fast snapshot restore for the specified snapshot in the specified Availability Zones.

```
aws ec2 enable-fast-snapshot-restores \
    --availability-zones us-east-2a us-east-2b \
    --source-snapshot-ids snap-1234567890abcdef0
```

Output:

```
{
    "Successful": [
        {
            "SnapshotId": "snap-1234567890abcdef0"
            "AvailabilityZone": "us-east-2a",
            "State": "enabling",
            "StateTransitionReason": "Client.UserInitiated",
            "OwnerId": "123456789012",
            "EnablingTime": "2020-01-25T23:57:49.602Z"
        },
        {
            "SnapshotId": "snap-1234567890abcdef0"
            "AvailabilityZone": "us-east-2b",
            "State": "enabling",
            "StateTransitionReason": "Client.UserInitiated",
            "OwnerId": "123456789012",
            "EnablingTime": "2020-01-25T23:57:49.596Z"
        }
    ],
    "Unsuccessful": []
}
```

## Output

Successful -> (list)

Information about the snapshots for which fast snapshot restores were successfully enabled.

(structure)

Describes fast snapshot restores that were successfully enabled.

SnapshotId -> (string)

The ID of the snapshot.

AvailabilityZone -> (string)

The Availability Zone.

State -> (string)

The state of fast snapshot restores.

StateTransitionReason -> (string)

The reason for the state transition. The possible values are as follows:

- `Client.UserInitiated` - The state successfully transitioned to `enabling` or `disabling` .
- `Client.UserInitiated - Lifecycle state transition` - The state successfully transitioned to `optimizing` , `enabled` , or `disabled` .

OwnerId -> (string)

The ID of the Amazon Web Services account that enabled fast snapshot restores on the snapshot.

OwnerAlias -> (string)

The Amazon Web Services owner alias that enabled fast snapshot restores on the snapshot. This is intended for future use.

EnablingTime -> (timestamp)

The time at which fast snapshot restores entered the `enabling` state.

OptimizingTime -> (timestamp)

The time at which fast snapshot restores entered the `optimizing` state.

EnabledTime -> (timestamp)

The time at which fast snapshot restores entered the `enabled` state.

DisablingTime -> (timestamp)

The time at which fast snapshot restores entered the `disabling` state.

DisabledTime -> (timestamp)

The time at which fast snapshot restores entered the `disabled` state.

Unsuccessful -> (list)

Information about the snapshots for which fast snapshot restores could not be enabled.

(structure)

Contains information about the errors that occurred when enabling fast snapshot restores.

SnapshotId -> (string)

The ID of the snapshot.

FastSnapshotRestoreStateErrors -> (list)

The errors.

(structure)

Contains information about an error that occurred when enabling fast snapshot restores.

AvailabilityZone -> (string)

The Availability Zone.

Error -> (structure)

The error.

Code -> (string)

The error code.

Message -> (string)

The error message.