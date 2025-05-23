# create-agreementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-agreement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/create-agreement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# create-agreement

## Description

Creates an agreement. An agreement is a bilateral trading partner agreement, or partnership, between an Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.

The partner is identified with the `PartnerProfileId` , and the AS2 process is identified with the `LocalProfileId` .

### Note

Specify *either* `BaseDirectory` or `CustomDirectories` , but not both. Specifying both causes the command to fail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/CreateAgreement)

## Synopsis

```
create-agreement
[--description <value>]
--server-id <value>
--local-profile-id <value>
--partner-profile-id <value>
[--base-directory <value>]
--access-role <value>
[--status <value>]
[--tags <value>]
[--preserve-filename <value>]
[--enforce-message-signing <value>]
[--custom-directories <value>]
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

`--description` (string)

A name or short description to identify the agreement.

`--server-id` (string)

A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.

`--local-profile-id` (string)

A unique identifier for the AS2 local profile.

`--partner-profile-id` (string)

A unique identifier for the partner profile used in the agreement.

`--base-directory` (string)

The landing directory (folder) for files transferred by using the AS2 protocol.

A `BaseDirectory` example is `/*amzn-s3-demo-bucket* /home/mydirectory` .

`--access-role` (string)

Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.

**For AS2 connectors**

With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths` . We use the fileâs parent directory (for example, for `--send-file-paths /bucket/dir/file.txt` , parent directory is `/bucket/dir/` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer` .

If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.

**For SFTP connectors**

Make sure that the access role provides read and write access to the parent directory of the file location thatâs used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to Secrets Manager.

`--status` (string)

The status of the agreement. The agreement can be either `ACTIVE` or `INACTIVE` .

Possible values:

- `ACTIVE`
- `INACTIVE`

`--tags` (list)

Key-value pairs that can be used to group and search for agreements.

(structure)

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

Contains one or more values that you assigned to the key name you create.

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

`--preserve-filename` (string)

Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it.

- `ENABLED` : the filename provided by your trading parter is preserved when the file is saved.
- `DISABLED` (default value): when Transfer Family saves the file, the filename is adjusted, as described in [File names and locations](https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2) .

Possible values:

- `ENABLED`
- `DISABLED`

`--enforce-message-signing` (string)

Determines whether or not unsigned messages from your trading partners will be accepted.

- `ENABLED` : Transfer Family rejects unsigned messages from your trading partner.
- `DISABLED` (default value): Transfer Family accepts unsigned messages from your trading partner.

Possible values:

- `ENABLED`
- `DISABLED`

`--custom-directories` (structure)

A `CustomDirectoriesType` structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.

- Failed files
- MDN files
- Payload files
- Status files
- Temporary files

FailedFilesDirectory -> (string)

Specifies a location to store failed AS2 message files.

MdnFilesDirectory -> (string)

Specifies a location to store MDN files.

PayloadFilesDirectory -> (string)

Specifies a location to store the payload for AS2 message files.

StatusFilesDirectory -> (string)

Specifies a location to store AS2 status messages.

TemporaryFilesDirectory -> (string)

Specifies a location to store temporary AS2 message files.

Shorthand Syntax:

```
FailedFilesDirectory=string,MdnFilesDirectory=string,PayloadFilesDirectory=string,StatusFilesDirectory=string,TemporaryFilesDirectory=string
```

JSON Syntax:

```
{
  "FailedFilesDirectory": "string",
  "MdnFilesDirectory": "string",
  "PayloadFilesDirectory": "string",
  "StatusFilesDirectory": "string",
  "TemporaryFilesDirectory": "string"
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

AgreementId -> (string)

The unique identifier for the agreement. Use this ID for deleting, or updating an agreement, as well as in any other API calls that require that you specify the agreement ID.