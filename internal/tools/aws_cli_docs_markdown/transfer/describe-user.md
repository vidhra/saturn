# describe-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# describe-user

## Description

Describes the user assigned to the specific file transfer protocol-enabled server, as identified by its `ServerId` property.

The response from this call returns the properties of the user associated with the `ServerId` value that was specified.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeUser)

## Synopsis

```
describe-user
--server-id <value>
--user-name <value>
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

`--server-id` (string)

A system-assigned unique identifier for a server that has this user assigned.

`--user-name` (string)

The name of the user assigned to one or more servers. User names are part of the sign-in credentials to use the Transfer Family service and perform file transfer tasks.

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

ServerId -> (string)

A system-assigned unique identifier for a server that has this user assigned.

User -> (structure)

An array containing the properties of the Transfer Family user for the `ServerID` value that you specified.

Arn -> (string)

Specifies the unique Amazon Resource Name (ARN) for the user that was requested to be described.

HomeDirectory -> (string)

The landing directory (folder) for a user when they log in to the server using the client.

A `HomeDirectory` example is `/bucket_name/home/mydirectory` .

### Note

The `HomeDirectory` parameter is only used if `HomeDirectoryType` is set to `PATH` .

HomeDirectoryMappings -> (list)

Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the `Entry` and `Target` pair, where `Entry` shows how the path is made visible and `Target` is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in `Target` . This value can be set only when `HomeDirectoryType` is set to *LOGICAL* .

In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory (â`chroot` â). To do this, you can set `Entry` to â/â and set `Target` to the HomeDirectory parameter value.

(structure)

Represents an object that contains entries and targets for `HomeDirectoryMappings` .

The following is an `Entry` and `Target` pair example for `chroot` .

`[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]`

Entry -> (string)

Represents an entry for `HomeDirectoryMappings` .

Target -> (string)

Represents the map target that is used in a `HomeDirectoryMapEntry` .

Type -> (string)

Specifies the type of mapping. Set the type to `FILE` if you want the mapping to point to a file, or `DIRECTORY` for the directory to point to a directory.

### Note

By default, home directory mappings have a `Type` of `DIRECTORY` when you create a Transfer Family server. You would need to explicitly set `Type` to `FILE` if you want a mapping to have a file target.

HomeDirectoryType -> (string)

The type of landing directory (folder) that you want your usersâ home directory to be when they log in to the server. If you set it to `PATH` , the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to `LOGICAL` , you need to provide mappings in the `HomeDirectoryMappings` for how you want to make Amazon S3 or Amazon EFS paths visible to your users.

### Note

If `HomeDirectoryType` is `LOGICAL` , you must provide mappings, using the `HomeDirectoryMappings` parameter. If, on the other hand, `HomeDirectoryType` is `PATH` , you provide an absolute path using the `HomeDirectory` parameter. You cannot have both `HomeDirectory` and `HomeDirectoryMappings` in your template.

Policy -> (string)

A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a userâs access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include `${Transfer:UserName}` , `${Transfer:HomeDirectory}` , and `${Transfer:HomeBucket}` .

PosixProfile -> (structure)

Specifies the full POSIX identity, including user ID (`Uid` ), group ID (`Gid` ), and any secondary groups IDs (`SecondaryGids` ), that controls your usersâ access to your Amazon Elastic File System (Amazon EFS) file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.

Uid -> (long)

The POSIX user ID used for all EFS operations by this user.

Gid -> (long)

The POSIX group ID used for all EFS operations by this user.

SecondaryGids -> (list)

The secondary POSIX group IDs used for all EFS operations by this user.

(long)

Role -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your usersâ access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your usersâ transfer requests.

SshPublicKeys -> (list)

Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.

### Note

To delete the public key body, set its value to zero keys, as shown here:

`SshPublicKeys: []`

(structure)

Provides information about the public Secure Shell (SSH) key that is associated with a Transfer Family user for the specific file transfer protocol-enabled server (as identified by `ServerId` ). The information returned includes the date the key was imported, the public key contents, and the public key ID. A user can store more than one SSH public key associated with their user name on a specific server.

DateImported -> (timestamp)

Specifies the date that the public key was added to the Transfer Family user.

SshPublicKeyBody -> (string)

Specifies the content of the SSH public key as specified by the `PublicKeyId` .

Transfer Family accepts RSA, ECDSA, and ED25519 keys.

SshPublicKeyId -> (string)

Specifies the `SshPublicKeyId` parameter contains the identifier of the public key.

Tags -> (list)

Specifies the key-value pairs for the user requested. Tag can be used to search for and group users for a variety of purposes.

(structure)

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

Contains one or more values that you assigned to the key name you create.

UserName -> (string)

Specifies the name of the user that was requested to be described. User names are used for authentication purposes. This is the string that will be used by your user when they log in to your server.