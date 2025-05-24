# delete-volumeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-volume.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/delete-volume.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# delete-volume

## Description

Deletes an Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS volume.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DeleteVolume)

## Synopsis

```
delete-volume
[--client-request-token <value>]
--volume-id <value>
[--ontap-configuration <value>]
[--open-zfs-configuration <value>]
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

`--client-request-token` (string)

(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.

`--volume-id` (string)

The ID of the volume that you are deleting.

`--ontap-configuration` (structure)

For Amazon FSx for ONTAP volumes, specify whether to take a final backup of the volume and apply tags to the backup. To apply tags to the backup, you must have the `fsx:TagResource` permission.

SkipFinalBackup -> (boolean)

Set to true if you want to skip taking a final backup of the volume you are deleting.

FinalBackupTags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

BypassSnaplockEnterpriseRetention -> (boolean)

Setting this to `true` allows a SnapLock administrator to delete an FSx for ONTAP SnapLock Enterprise volume with unexpired write once, read many (WORM) files. The IAM permission `fsx:BypassSnaplockEnterpriseRetention` is also required to delete SnapLock Enterprise volumes with unexpired WORM files. The default value is `false` .

For more information, see [Deleting a SnapLock volume](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-delete-volume.html) .

Shorthand Syntax:

```
SkipFinalBackup=boolean,FinalBackupTags=[{Key=string,Value=string},{Key=string,Value=string}],BypassSnaplockEnterpriseRetention=boolean
```

JSON Syntax:

```
{
  "SkipFinalBackup": true|false,
  "FinalBackupTags": [
    {
      "Key": "string",
      "Value": "string"
    }
    ...
  ],
  "BypassSnaplockEnterpriseRetention": true|false
}
```

`--open-zfs-configuration` (structure)

For Amazon FSx for OpenZFS volumes, specify whether to delete all child volumes and snapshots.

Options -> (list)

To delete the volumeâs child volumes, snapshots, and clones, use the string `DELETE_CHILD_VOLUMES_AND_SNAPSHOTS` .

(string)

Shorthand Syntax:

```
Options=string,string
```

JSON Syntax:

```
{
  "Options": ["DELETE_CHILD_VOLUMES_AND_SNAPSHOTS", ...]
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

## Output

VolumeId -> (string)

The ID of the volume thatâs being deleted.

Lifecycle -> (string)

The lifecycle state of the volume being deleted. If the `DeleteVolume` operation is successful, this value is `DELETING` .

OntapResponse -> (structure)

Returned after a `DeleteVolume` request, showing the status of the delete request.

FinalBackupId -> (string)

The ID of the source backup. Specifies the backup that you are copying.

FinalBackupTags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .