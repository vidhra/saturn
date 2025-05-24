# describe-smb-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-smb-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# describe-smb-settings

## Description

Gets a description of a Server Message Block (SMB) file share settings from a file gateway. This operation is only supported for file gateways.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeSMBSettings)

## Synopsis

```
describe-smb-settings
--gateway-arn <value>
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

`--gateway-arn` (string)

The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.

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

GatewayARN -> (string)

The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.

DomainName -> (string)

The name of the domain that the gateway is joined to.

ActiveDirectoryStatus -> (string)

Indicates the status of a gateway that is a member of the Active Directory domain.

### Note

This field is only used as part of a `JoinDomain` request. It is not affected by Active Directory connectivity changes that occur after the `JoinDomain` request succeeds.

- `ACCESS_DENIED` : Indicates that the `JoinDomain` operation failed due to an authentication error.
- `DETACHED` : Indicates that gateway is not joined to a domain.
- `JOINED` : Indicates that the gateway has successfully joined a domain.
- `JOINING` : Indicates that a `JoinDomain` operation is in progress.
- `NETWORK_ERROR` : Indicates that `JoinDomain` operation failed due to a network or connectivity error.
- `TIMEOUT` : Indicates that the `JoinDomain` operation failed because the operation didnât complete within the allotted time.
- `UNKNOWN_ERROR` : Indicates that the `JoinDomain` operation failed due to another type of error.

SMBGuestPasswordSet -> (boolean)

This value is `true` if a password for the guest user `smbguest` is set, otherwise `false` . Only supported for S3 File Gateways.

Valid Values: `true` | `false`

SMBSecurityStrategy -> (string)

The type of security strategy that was specified for file gateway.

- `ClientSpecified` : If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.
- `MandatorySigning` : If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing turned on. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008, or later.
- `MandatoryEncryption` : If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption turned on. Both 256-bit and 128-bit algorithms are allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.
- `MandatoryEncryptionNoAes128` : If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.

FileSharesVisible -> (boolean)

The shares on this gateway appear when listing shares. Only supported for S3 File Gateways.

SMBLocalGroups -> (structure)

A list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.

GatewayAdmins -> (list)

A list of Active Directory users and groups that have local Gateway Admin permissions. Acceptable formats include: `DOMAIN\User1` , `user1` , `DOMAIN\group1` , and `group1` .

Gateway Admins can use the Shared Folders Microsoft Management Console snap-in to force-close files that are open and locked.

(string)