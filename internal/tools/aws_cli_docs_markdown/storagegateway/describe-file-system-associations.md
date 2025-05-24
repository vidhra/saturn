# describe-file-system-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-file-system-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-file-system-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# describe-file-system-associations

## Description

Gets the file system association information. This operation is only supported for FSx File Gateways.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeFileSystemAssociations)

## Synopsis

```
describe-file-system-associations
--file-system-association-arn-list <value>
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

`--file-system-association-arn-list` (list)

An array containing the Amazon Resource Name (ARN) of each file system association to be described.

(string)

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

FileSystemAssociationInfoList -> (list)

An array containing the `FileSystemAssociationInfo` data type of each file system association to be described.

(structure)

Describes the object returned by `DescribeFileSystemAssociations` that describes a created file system association.

FileSystemAssociationARN -> (string)

The Amazon Resource Name (ARN) of the file system association.

LocationARN -> (string)

The ARN of the backend Amazon FSx file system used for storing file data. For information, see [FileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_FileSystem.html) in the *Amazon FSx API Reference* .

FileSystemAssociationStatus -> (string)

The status of the file system association. Valid Values: `AVAILABLE` | `CREATING` | `DELETING` | `FORCE_DELETING` | `UPDATING` | `ERROR`

AuditDestinationARN -> (string)

The Amazon Resource Name (ARN) of the storage used for the audit logs.

GatewayARN -> (string)

The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.

Tags -> (list)

A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key name. Each tag is a key-value pair.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.

Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.

CacheAttributes -> (structure)

The refresh cache information for the file share or FSx file systems.

CacheStaleTimeoutInSeconds -> (integer)

Refreshes a file shareâs cache by using Time To Live (TTL). TTL is the length of time since the last refresh after which access to the directory would cause the file gateway to first refresh that directoryâs contents from the Amazon S3 bucket or Amazon FSx file system. The TTL duration is in seconds.

Valid Values:0, 300 to 2,592,000 seconds (5 minutes to 30 days)

EndpointNetworkConfiguration -> (structure)

Specifies network configuration information for the gateway associated with the Amazon FSx file system.

### Note

If multiple file systems are associated with this gateway, this parameterâs `IpAddresses` field is required.

IpAddresses -> (list)

A list of gateway IP addresses on which the associated Amazon FSx file system is available.

### Note

If multiple file systems are associated with this gateway, this field is required.

(string)

FileSystemAssociationStatusDetails -> (list)

An array containing the FileSystemAssociationStatusDetail data type, which provides detailed information on file system association status.

(structure)

Detailed information on file system association status.

ErrorCode -> (string)

The error code for a given file system association status.