# describe-nfs-file-sharesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-nfs-file-shares.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-nfs-file-shares.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# describe-nfs-file-shares

## Description

Gets a description for one or more Network File System (NFS) file shares from an S3 File Gateway. This operation is only supported for S3 File Gateways.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeNFSFileShares)

## Synopsis

```
describe-nfs-file-shares
--file-share-arn-list <value>
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

`--file-share-arn-list` (list)

An array containing the Amazon Resource Name (ARN) of each file share to be described.

(string)

The Amazon Resource Name (ARN) of the file share.

Syntax:

```
"string" "string" ...
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

NFSFileShareInfoList -> (list)

An array containing a description for each requested file share.

(structure)

The Unix file permissions and ownership information assigned, by default, to native S3 objects when an S3 File Gateway discovers them in S3 buckets. This operation is only supported in S3 File Gateways.

NFSFileShareDefaults -> (structure)

Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets donât, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for S3 File Gateways.

FileMode -> (string)

The Unix file mode in the form ânnnnâ. For example, `0666` represents the default file mode inside the file share. The default value is `0666` .

DirectoryMode -> (string)

The Unix directory mode in the form ânnnnâ. For example, `0666` represents the default access mode for all directories inside the file share. The default value is `0777` .

GroupId -> (long)

The default group ID for the file share (unless the files have another group ID specified). The default value is `nfsnobody` .

OwnerId -> (long)

The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is `nfsnobody` .

FileShareARN -> (string)

The Amazon Resource Name (ARN) of the file share.

FileShareId -> (string)

The ID of the file share.

FileShareStatus -> (string)

The status of the file share.

Valid Values: `CREATING` | `UPDATING` | `AVAILABLE` | `DELETING`

GatewayARN -> (string)

The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.

EncryptionType -> (string)

A value that specifies the type of server-side encryption that the file share will use for the data that it stores in Amazon S3.

### Note

We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.

If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3` , then `KMSEncrypted` must be `false` . If `EncryptionType` is `SseKms` or `DsseKms` , then `KMSEncrypted` must be `true` .

KMSEncrypted -> (boolean)

Optional. Set to `true` to use Amazon S3 server-side encryption with your own KMS key (SSE-KMS), or `false` to use a key managed by Amazon S3 (SSE-S3). To use dual-layer encryption (DSSE-KMS), set the `EncryptionType` parameter instead.

### Note

We recommend using `EncryptionType` instead of `KMSEncrypted` to set the file share encryption method. You do not need to provide values for both parameters.

If values for both parameters exist in the same request, then the specified encryption methods must not conflict. For example, if `EncryptionType` is `SseS3` , then `KMSEncrypted` must be `false` . If `EncryptionType` is `SseKms` or `DsseKms` , then `KMSEncrypted` must be `true` .

Valid Values: `true` | `false`

KMSKey -> (string)

Optional. The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value must be set if `KMSEncrypted` is `true` , or if `EncryptionType` is `SseKms` or `DsseKms` .

Path -> (string)

The file share path used by the NFS client to identify the mount point.

Role -> (string)

The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.

LocationARN -> (string)

A custom ARN for the backend storage used for storing data for file shares. It includes a resource ARN with an optional prefix concatenation. The prefix must end with a forward slash (/).

### Note

You can specify LocationARN as a bucket ARN, access point ARN or access point alias, as shown in the following examples.

Bucket ARN:

`arn:aws:s3:::amzn-s3-demo-bucket/prefix/`

Access point ARN:

`arn:aws:s3:region:account-id:accesspoint/access-point-name/prefix/`

If you specify an access point, the bucket policy must be configured to delegate access control to the access point. For information, see [Delegating access control to access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html#access-points-delegating-control) in the *Amazon S3 User Guide* .

Access point alias:

`test-ap-ab123cdef4gehijklmn5opqrstuvuse1a-s3alias`

DefaultStorageClass -> (string)

The default storage class for objects put into an Amazon S3 bucket by the S3 File Gateway. The default value is `S3_STANDARD` . Optional.

Valid Values: `S3_STANDARD` | `S3_INTELLIGENT_TIERING` | `S3_STANDARD_IA` | `S3_ONEZONE_IA`

ObjectACL -> (string)

A value that sets the access control list (ACL) permission for objects in the S3 bucket that an S3 File Gateway puts objects into. The default value is `private` .

ClientList -> (list)

The list of clients that are allowed to access the S3 File Gateway. The list must contain either valid IP addresses or valid CIDR blocks.

(string)

Squash -> (string)

The user mapped to anonymous user. Valid options are the following:

- `RootSquash` : Only root is mapped to anonymous user.
- `NoSquash` : No one is mapped to anonymous user.
- `AllSquash` : Everyone is mapped to anonymous user.

ReadOnly -> (boolean)

A value that sets the write status of a file share. Set this value to `true` to set the write status to read-only, otherwise set to `false` .

Valid Values: `true` | `false`

GuessMIMETypeEnabled -> (boolean)

A value that enables guessing of the MIME type for uploaded objects based on file extensions. Set this value to `true` to enable MIME type guessing, otherwise set to `false` . The default value is `true` .

Valid Values: `true` | `false`

RequesterPays -> (boolean)

A value that sets who pays the cost of the request and the cost associated with data download from the S3 bucket. If this value is set to `true` , the requester pays the costs; otherwise, the S3 bucket owner pays. However, the S3 bucket owner always pays the cost of storing data.

### Note

`RequesterPays` is a configuration for the S3 bucket that backs the file share, so make sure that the configuration on the file share is the same as the S3 bucket configuration.

Valid Values: `true` | `false`

Tags -> (list)

A list of up to 50 tags assigned to the NFS file share, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the `ListTagsForResource` API operation.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.

Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.

FileShareName -> (string)

The name of the file share. Optional.

### Note

`FileShareName` must be set if an S3 prefix name is set in `LocationARN` , or if an access point or access point alias is used.

CacheAttributes -> (structure)

Refresh cache information for the file share.

CacheStaleTimeoutInSeconds -> (integer)

Refreshes a file shareâs cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directoryâs contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.

Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)

NotificationPolicy -> (string)

The notification policy of the file share. `SettlingTimeInSeconds` controls the number of seconds to wait after the last point in time a client wrote to a file before generating an `ObjectUploaded` notification. Because clients can make many small writes to files, itâs best to set this parameter for as long as possible to avoid generating multiple notifications for the same file in a small time period.

### Note

`SettlingTimeInSeconds` has no effect on the timing of the object uploading to Amazon S3, only the timing of the notification.

This setting is not meant to specify an exact time at which the notification will be sent. In some cases, the gateway might require more than the specified delay time to generate and send notifications.

The following example sets `NotificationPolicy` on with `SettlingTimeInSeconds` set to 60.

`{\"Upload\": {\"SettlingTimeInSeconds\": 60}}`

The following example sets `NotificationPolicy` off.

`{}`

VPCEndpointDNSName -> (string)

Specifies the DNS name for the VPC endpoint that the NFS file share uses to connect to Amazon S3.

### Note

This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.

BucketRegion -> (string)

Specifies the Region of the S3 bucket where the NFS file share stores files.

### Note

This parameter is required for NFS file shares that connect to Amazon S3 through a VPC endpoint, a VPC access point, or an access point alias that points to a VPC access point.

AuditDestinationARN -> (string)

The Amazon Resource Name (ARN) of the storage used for audit logs.