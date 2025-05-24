# create-access-pointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-access-point.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-access-point.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [efs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/index.html#cli-aws-efs) ]

# create-access-point

## Description

Creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access pointâs root directory. Applications using the access point can only access data in the applicationâs own directory and any subdirectories. To learn more, see [Mounting a file system using EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) .

### Note

If multiple requests to create access points on the same file system are sent in quick succession, and the file system is near the limit of 1,000 access points, you may experience a throttling response for these requests. This is to ensure that the file system does not exceed the stated access point limit.

This operation requires permissions for the `elasticfilesystem:CreateAccessPoint` action.

Access points can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the `elasticfilesystem:TagResource` action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the `elasticfilesystem:TagResource` action. For more information, see [Granting permissions to tag resources during creation](https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateAccessPoint)

## Synopsis

```
create-access-point
[--client-token <value>]
[--tags <value>]
--file-system-id <value>
[--posix-user <value>]
[--root-directory <value>]
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

`--client-token` (string)

A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.

`--tags` (list)

Creates tags associated with the access point. Each tag is a key-value pair, each key must be unique. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

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

`--file-system-id` (string)

The ID of the EFS file system that the access point provides access to.

`--posix-user` (structure)

The operating system user and group applied to all file system requests made using the access point.

Uid -> (long)

The POSIX user ID used for all file system operations using this access point.

Gid -> (long)

The POSIX group ID used for all file system operations using this access point.

SecondaryGids -> (list)

Secondary POSIX group IDs used for all file system operations using this access point.

(long)

Shorthand Syntax:

```
Uid=long,Gid=long,SecondaryGids=long,long
```

JSON Syntax:

```
{
  "Uid": long,
  "Gid": long,
  "SecondaryGids": [long, ...]
}
```

`--root-directory` (structure)

Specifies the directory on the EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the `RootDirectory` > `Path` specified does not exist, Amazon EFS creates it and applies the `CreationInfo` settings when a client connects to an access point. When specifying a `RootDirectory` , you must provide the `Path` , and the `CreationInfo` .

Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.

Path -> (string)

Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the `CreationInfo` .

CreationInfo -> (structure)

(Optional) Specifies the POSIX IDs and permissions to apply to the access pointâs `RootDirectory` . If the `RootDirectory` > `Path` specified does not exist, EFS creates the root directory using the `CreationInfo` settings when a client connects to an access point. When specifying the `CreationInfo` , you must provide values for all properties.

### Warning

If you do not provide `CreationInfo` and the specified `RootDirectory` > `Path` does not exist, attempts to mount the file system using the access point will fail.

OwnerUid -> (long)

Specifies the POSIX user ID to apply to the `RootDirectory` . Accepts values from 0 to 2^32 (4294967295).

OwnerGid -> (long)

Specifies the POSIX group ID to apply to the `RootDirectory` . Accepts values from 0 to 2^32 (4294967295).

Permissions -> (string)

Specifies the POSIX permissions to apply to the `RootDirectory` , in the format of an octal number representing the fileâs mode bits.

Shorthand Syntax:

```
Path=string,CreationInfo={OwnerUid=long,OwnerGid=long,Permissions=string}
```

JSON Syntax:

```
{
  "Path": "string",
  "CreationInfo": {
    "OwnerUid": long,
    "OwnerGid": long,
    "Permissions": "string"
  }
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

ClientToken -> (string)

The opaque string specified in the request to ensure idempotent creation.

Name -> (string)

The name of the access point. This is the value of the `Name` tag.

Tags -> (list)

The tags associated with the access point, presented as an array of Tag objects.

(structure)

A tag is a key-value pair. Allowed characters are letters, white space, and numbers that can be represented in UTF-8, and the following characters:`+ - = . _ : /` .

Key -> (string)

The tag key (String). The key canât start with `aws:` .

Value -> (string)

The value of the tag key.

AccessPointId -> (string)

The ID of the access point, assigned by Amazon EFS.

AccessPointArn -> (string)

The unique Amazon Resource Name (ARN) associated with the access point.

FileSystemId -> (string)

The ID of the EFS file system that the access point applies to.

PosixUser -> (structure)

The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.

Uid -> (long)

The POSIX user ID used for all file system operations using this access point.

Gid -> (long)

The POSIX group ID used for all file system operations using this access point.

SecondaryGids -> (list)

Secondary POSIX group IDs used for all file system operations using this access point.

(long)

RootDirectory -> (structure)

The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.

Path -> (string)

Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the `CreationInfo` .

CreationInfo -> (structure)

(Optional) Specifies the POSIX IDs and permissions to apply to the access pointâs `RootDirectory` . If the `RootDirectory` > `Path` specified does not exist, EFS creates the root directory using the `CreationInfo` settings when a client connects to an access point. When specifying the `CreationInfo` , you must provide values for all properties.

### Warning

If you do not provide `CreationInfo` and the specified `RootDirectory` > `Path` does not exist, attempts to mount the file system using the access point will fail.

OwnerUid -> (long)

Specifies the POSIX user ID to apply to the `RootDirectory` . Accepts values from 0 to 2^32 (4294967295).

OwnerGid -> (long)

Specifies the POSIX group ID to apply to the `RootDirectory` . Accepts values from 0 to 2^32 (4294967295).

Permissions -> (string)

Specifies the POSIX permissions to apply to the `RootDirectory` , in the format of an octal number representing the fileâs mode bits.

OwnerId -> (string)

Identifies the Amazon Web Services account that owns the access point resource.

LifeCycleState -> (string)

Identifies the lifecycle phase of the access point.