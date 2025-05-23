# update-smb-file-shareÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-smb-file-share.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# update-smb-file-share

## Description

Updates a Server Message Block (SMB) file share. This operation is only supported for S3 File Gateways.

### Note

To leave a file share field unchanged, set the corresponding input field to null.

### Warning

File gateways require Security Token Service (Amazon Web Services STS) to be activated to enable you to create a file share. Make sure that Amazon Web Services STS is activated in the Amazon Web Services Region you are creating your file gateway in. If Amazon Web Services STS is not activated in this Amazon Web Services Region, activate it. For information about how to activate Amazon Web Services STS, see [Activating and deactivating Amazon Web Services STS in an Amazon Web Services Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *Identity and Access Management User Guide* .

File gateways donât support creating hard or symbolic links on a file share.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/UpdateSMBFileShare)

## Synopsis

```
update-smb-file-share
--file-share-arn <value>
[--encryption-type <value>]
[--kms-encrypted | --no-kms-encrypted]
[--kms-key <value>]
[--default-storage-class <value>]
[--object-acl <value>]
[--read-only | --no-read-only]
[--guess-mime-type-enabled | --no-guess-mime-type-enabled]
[--requester-pays | --no-requester-pays]
[--smbacl-enabled | --no-smbacl-enabled]
[--access-based-enumeration | --no-access-based-enumeration]
[--admin-user-list <value>]
[--valid-user-list <value>]
[--invalid-user-list <value>]
[--audit-destination-arn <value>]
[--case-sensitivity <value>]
[--file-share-name <value>]
[--cache-attributes <value>]
[--notification-policy <value>]
[--oplocks-enabled | --no-oplocks-enabled]
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

`--file-share-arn` (string)

The Amazon Resource Name (ARN) of the SMB file share that you want to update.

`--encryption-type` (string)

A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.

### Note

We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.

If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3` , then `KMSEncrypted` must be `false` . If `EncryptionType` is `SseKms` or `DsseKms` , then `KMSEncrypted` must be `true` .

Possible values:

- `SseS3`
- `SseKms`
- `DsseKms`

`--kms-encrypted` | `--no-kms-encrypted` (boolean)

Optional. Set to `true` to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.

### Note

We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.

If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3` , then `KMSEncrypted` must be `false` . If `EncryptionType` is `SseKms` or `DsseKms` , then `KMSEncrypted` must be `true` .

Valid Values: `true` | `false`

`--kms-key` (string)

Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if `KMSEncrypted` is `true` , or if `EncryptionType` is `SseKms` or `DsseKms` .

`--default-storage-class` (string)

The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD` . Optional.

Valid Values: `S3_STANDARD` | `S3_INTELLIGENT_TIERING` | `S3_STANDARD_IA` | `S3_ONEZONE_IA`

`--object-acl` (string)

A value that sets the access control list (ACL) permission for objects in the S3 bucket that a S3 File Gateway puts objects into. The default value is `private` .

Possible values:

- `private`
- `public-read`
- `public-read-write`
- `authenticated-read`
- `bucket-owner-read`
- `bucket-owner-full-control`
- `aws-exec-read`

`--read-only` | `--no-read-only` (boolean)

A value that sets the write status of a file share. Set this value to `true` to set write status to read-only, otherwise set to `false` .

Valid Values: `true` | `false`

`--guess-mime-type-enabled` | `--no-guess-mime-type-enabled` (boolean)

A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false` . The default value is `true` .

Valid Values: `true` | `false`

`--requester-pays` | `--no-requester-pays` (boolean)

A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true` , the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.

### Note

`RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.

Valid Values: `true` | `false`

`--smbacl-enabled` | `--no-smbacl-enabled` (boolean)

Set this value to `true` to enable access control list (ACL) on the SMB file share. Set it to `false` to map file and directory permissions to the POSIX permissions.

For more information, see [Using Windows ACLs to limit SMB file share access](https://docs.aws.amazon.com/filegateway/latest/files3/smb-acl.html) in the *Amazon S3 File Gateway User Guide* .

Valid Values: `true` | `false`

`--access-based-enumeration` | `--no-access-based-enumeration` (boolean)

The files and folders on this share will only be visible to users with read access.

`--admin-user-list` (list)

A list of users or groups in the Active Directory that have administrator rights to the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1` , `user1` , `@group1` , and `@DOMAIN\group1` . Can only be set if Authentication is set to `ActiveDirectory` .

(string)

Syntax:

```
"string" "string" ...
```

`--valid-user-list` (list)

A list of users or groups in the Active Directory that are allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1` , `user1` , `@group1` , and `@DOMAIN\group1` . Can only be set if Authentication is set to `ActiveDirectory` .

(string)

Syntax:

```
"string" "string" ...
```

`--invalid-user-list` (list)

A list of users or groups in the Active Directory that are not allowed to access the file share. A group must be prefixed with the @ character. Acceptable formats include: `DOMAIN\User1` , `user1` , `@group1` , and `@DOMAIN\group1` . Can only be set if Authentication is set to `ActiveDirectory` .

(string)

Syntax:

```
"string" "string" ...
```

`--audit-destination-arn` (string)

The Amazon Resource Name (ARN) of the storage used for audit logs.

`--case-sensitivity` (string)

The case of an object name in an Amazon S3 bucket. For `ClientSpecified` , the client determines the case sensitivity. For `CaseSensitive` , the gateway determines the case sensitivity. The default value is `ClientSpecified` .

Possible values:

- `ClientSpecified`
- `CaseSensitive`

`--file-share-name` (string)

The name of the file share. Optional.

### Note

`FileShareName` must be set if an S3 prefix name is set in `LocationARN` , or if an access point or access point alias is used.

A valid SMB file share name cannot contain the following characters: `[` ,``]`` ,``#`` ,``;`` ,``<`` ,``>`` ,``:`` ,``â`` ,```` ,``/`` ,``|`` ,``?`` ,``*`` ,``+`` , or ASCII control characters `1-31` .

`--cache-attributes` (structure)

Specifies refresh cache information for the file share.

CacheStaleTimeoutInSeconds -> (integer)

Refreshes a file shareâs cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directoryâs contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.

Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)

Shorthand Syntax:

```
CacheStaleTimeoutInSeconds=integer
```

JSON Syntax:

```
{
  "CacheStaleTimeoutInSeconds": integer
}
```

`--notification-policy` (string)

The notification policy of the file share. `SettlingTimeInSeconds` controls the number of seconds to wait after the last point in time a client wrote to a file before generating an `ObjectUploaded` notification. Because clients can make many small writes to files, itâs best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.

### Note

`SettlingTimeInSeconds` has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.

This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.

The following example sets `NotificationPolicy` on with `SettlingTimeInSeconds` set to 60.

`{\"Upload\": {\"SettlingTimeInSeconds\": 60}}`

The following example sets `NotificationPolicy` off.

`{}`

`--oplocks-enabled` | `--no-oplocks-enabled` (boolean)

Specifies whether opportunistic locking is enabled for the SMB file share.

### Note

Enabling opportunistic locking on case-sensitive shares is not recommended for workloads that involve access to files with the same name in different case.

Valid Values: `true` | `false`

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

FileShareARN -> (string)

The Amazon Resource Name (ARN) of the updated SMB file share.