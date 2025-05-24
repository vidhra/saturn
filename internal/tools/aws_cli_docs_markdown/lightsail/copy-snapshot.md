# copy-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/copy-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/copy-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# copy-snapshot

## Description

Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manual or automatic snapshot of an instance or a disk from one Amazon Web Services Region to another in Amazon Lightsail.

When copying a *manual snapshot* , be sure to define the `source region` , `source snapshot name` , and `target snapshot name` parameters.

When copying an *automatic snapshot* , be sure to define the `source region` , `source resource name` , `target snapshot name` , and either the `restore date` or the `use latest restorable auto snapshot` parameters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CopySnapshot)

## Synopsis

```
copy-snapshot
[--source-snapshot-name <value>]
[--source-resource-name <value>]
[--restore-date <value>]
[--use-latest-restorable-auto-snapshot | --no-use-latest-restorable-auto-snapshot]
--target-snapshot-name <value>
--source-region <value>
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

`--source-snapshot-name` (string)

The name of the source manual snapshot to copy.

Constraint:

- Define this parameter only when copying a manual snapshot as another manual snapshot.

`--source-resource-name` (string)

The name of the source instance or disk from which the source automatic snapshot was created.

Constraint:

- Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots) .

`--restore-date` (string)

The date of the source automatic snapshot to copy. Use the `get auto snapshots` operation to identify the dates of the available automatic snapshots.

Constraints:

- Must be specified in `YYYY-MM-DD` format.
- This parameter cannot be defined together with the `use latest restorable auto snapshot` parameter. The `restore date` and `use latest restorable auto snapshot` parameters are mutually exclusive.
- Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots) .

`--use-latest-restorable-auto-snapshot` | `--no-use-latest-restorable-auto-snapshot` (boolean)

A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or disk.

Constraints:

- This parameter cannot be defined together with the `restore date` parameter. The `use latest restorable auto snapshot` and `restore date` parameters are mutually exclusive.
- Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots) .

`--target-snapshot-name` (string)

The name of the new manual snapshot to be created as a copy.

`--source-region` (string)

The Amazon Web Services Region where the source manual or automatic snapshot is located.

Possible values:

- `us-east-1`
- `us-east-2`
- `us-west-1`
- `us-west-2`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `eu-central-1`
- `ca-central-1`
- `ap-south-1`
- `ap-southeast-1`
- `ap-southeast-2`
- `ap-northeast-1`
- `ap-northeast-2`
- `eu-north-1`

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

**Example 1: To copy a snapshot within the same AWS Region**

The following `copy-snapshot` example copies instance snapshot `MEAN-1-1571075291` as instance snapshot `MEAN-1-Copy` within the same AWS Region `us-west-2`.

```
aws lightsail copy-snapshot \
    --source-snapshot-name MEAN-1-1571075291 \
    --target-snapshot-name MEAN-1-Copy \
    --source-region us-west-2
```

Output:

```
{
    "operations": [
        {
            "id": "ced16fc1-f401-4556-8d82-1EXAMPLEb982",
            "resourceName": "MEAN-1-Copy",
            "resourceType": "InstanceSnapshot",
            "createdAt": 1571075581.498,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationDetails": "us-west-2:MEAN-1-1571075291",
            "operationType": "CopySnapshot",
            "status": "Started",
            "statusChangedAt": 1571075581.498
        }
    ]
}
```

For more information, see [Copying snapshots from one AWS Region to another in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-copying-snapshots-from-one-region-to-another) in the *Lightsail Dev Guide*.

**Example 2: To copy a snapshot from one AWS Region to another**

The following `copy-snapshot` example copies instance snapshot `MEAN-1-1571075291` as instance snapshot `MEAN-1-1571075291-Copy` from AWS Region `us-west-2` to `us-east-1`.

```
aws lightsail copy-snapshot \
    --source-snapshot-name MEAN-1-1571075291 \
    --target-snapshot-name MEAN-1-1571075291-Copy \
    --source-region us-west-2 \
    --region us-east-1
```

Output:

```
{
    "operations": [
        {
            "id": "91116b79-119c-4451-b44a-dEXAMPLEd97b",
            "resourceName": "MEAN-1-1571075291-Copy",
            "resourceType": "InstanceSnapshot",
            "createdAt": 1571075695.069,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-east-1"
            },
            "isTerminal": false,
            "operationDetails": "us-west-2:MEAN-1-1571075291",
            "operationType": "CopySnapshot",
            "status": "Started",
            "statusChangedAt": 1571075695.069
        }
    ]
}
```

For more information, see [Copying snapshots from one AWS Region to another in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-copying-snapshots-from-one-region-to-another) in the *Lightsail Dev Guide*.

**Example 3: To copy an automatic snapshot within the same AWS Region**

The following `copy-snapshot` example copies automatic snapshot `2019-10-14` of instance `WordPress-1` as a manual snapshot `WordPress-1-10142019` in the AWS Region `us-west-2`.

```
aws lightsail copy-snapshot \
    --source-resource-name WordPress-1 \
    --restore-date 2019-10-14 \
    --target-snapshot-name WordPress-1-10142019 \
    --source-region us-west-2
```

Output:

```
{
    "operations": [
        {
            "id": "be3e6754-cd1d-48e6-ad9f-2EXAMPLE1805",
            "resourceName": "WordPress-1-10142019",
            "resourceType": "InstanceSnapshot",
            "createdAt": 1571082412.311,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationDetails": "us-west-2:WordPress-1",
            "operationType": "CopySnapshot",
            "status": "Started",
            "statusChangedAt": 1571082412.311
        }
    ]
}
```

For more information, see [Keeping automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-keeping-automatic-snapshots) in the *Lightsail Dev Guide*.

**Example 4: To copy an automatic snapshot from one AWS Region to another**

The following `copy-snapshot` example copies automatic snapshot `2019-10-14` of instance `WordPress-1` as a manual snapshot `WordPress-1-10142019` from the AWS Region `us-west-2` to `us-east-1`.

```
aws lightsail copy-snapshot \
    --source-resource-name WordPress-1 \
    --restore-date 2019-10-14 \
    --target-snapshot-name WordPress-1-10142019 \
    --source-region us-west-2 \
    --region us-east-1
```

Output:

```
{
    "operations": [
        {
            "id": "dffa128b-0b07-476e-b390-bEXAMPLE3775",
            "resourceName": "WordPress-1-10142019",
            "resourceType": "InstanceSnapshot",
            "createdAt": 1571082493.422,
            "location": {
                "availabilityZone": "all",
                "regionName": "us-east-1"
            },
            "isTerminal": false,
            "operationDetails": "us-west-2:WordPress-1",
            "operationType": "CopySnapshot",
            "status": "Started",
            "statusChangedAt": 1571082493.422
        }
    ]
}
```

For more information, see [Keeping automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-keeping-automatic-snapshots) in the *Lightsail Dev Guide*.

## Output

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.