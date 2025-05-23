# update-connectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-connector.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/update-connector.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# update-connector

## Description

Updates some of the parameters for an existing connector. Provide the `ConnectorId` for the connector that you want to update, along with the new values for the parameters to update.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/UpdateConnector)

## Synopsis

```
update-connector
--connector-id <value>
[--url <value>]
[--as2-config <value>]
[--access-role <value>]
[--logging-role <value>]
[--sftp-config <value>]
[--security-policy-name <value>]
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

`--connector-id` (string)

The unique identifier for the connector.

`--url` (string)

The URL of the partnerâs AS2 or SFTP endpoint.

`--as2-config` (structure)

A structure that contains the parameters for an AS2 connector object.

LocalProfileId -> (string)

A unique identifier for the AS2 local profile.

PartnerProfileId -> (string)

A unique identifier for the partner profile for the connector.

MessageSubject -> (string)

Used as the `Subject` HTTP header attribute in AS2 messages that are being sent with the connector.

Compression -> (string)

Specifies whether the AS2 file is compressed.

EncryptionAlgorithm -> (string)

The algorithm that is used to encrypt the file.

Note the following:

- Do not use the `DES_EDE3_CBC` algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm.
- You can only specify `NONE` if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.

SigningAlgorithm -> (string)

The algorithm that is used to sign the AS2 messages sent with the connector.

MdnSigningAlgorithm -> (string)

The signing algorithm for the MDN response.

### Note

If set to DEFAULT (or not set at all), the value for `SigningAlgorithm` is used.

MdnResponse -> (string)

Used for outbound requests (from an Transfer Family connector to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous. Specify either of the following values:

- `SYNC` : The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not).
- `NONE` : Specifies that no MDN response is required.

BasicAuthSecretId -> (string)

Provides Basic authentication support to the AS2 Connectors API. To use Basic authentication, you must provide the name or Amazon Resource Name (ARN) of a secret in Secrets Manager.

The default value for this parameter is `null` , which indicates that Basic authentication is not enabled for the connector.

If the connector should use Basic authentication, the secret needs to be in the following format:

`{ "Username": "user-name", "Password": "user-password" }`

Replace `user-name` and `user-password` with the credentials for the actual user that is being authenticated.

Note the following:

- You are storing these credentials in Secrets Manager, *not passing them directly* into this API.
- If you are using the API, SDKs, or CloudFormation to configure your connector, then you must create the secret before you can enable Basic authentication. However, if you are using the Amazon Web Services management console, you can have the system create the secret for you.

If you have previously enabled Basic authentication for a connector, you can disable it by using the `UpdateConnector` API call. For example, if you are using the CLI, you can run the following command to remove Basic authentication:

`update-connector --connector-id my-connector-id --as2-config 'BasicAuthSecretId=""'`

PreserveContentType -> (string)

Allows you to use the Amazon S3 `Content-Type` that is associated with objects in S3 instead of having the content type mapped based on the file extension. This parameter is enabled by default when you create an AS2 connector from the console, but disabled by default when you create an AS2 connector by calling the API directly.

Shorthand Syntax:

```
LocalProfileId=string,PartnerProfileId=string,MessageSubject=string,Compression=string,EncryptionAlgorithm=string,SigningAlgorithm=string,MdnSigningAlgorithm=string,MdnResponse=string,BasicAuthSecretId=string,PreserveContentType=string
```

JSON Syntax:

```
{
  "LocalProfileId": "string",
  "PartnerProfileId": "string",
  "MessageSubject": "string",
  "Compression": "ZLIB"|"DISABLED",
  "EncryptionAlgorithm": "AES128_CBC"|"AES192_CBC"|"AES256_CBC"|"DES_EDE3_CBC"|"NONE",
  "SigningAlgorithm": "SHA256"|"SHA384"|"SHA512"|"SHA1"|"NONE",
  "MdnSigningAlgorithm": "SHA256"|"SHA384"|"SHA512"|"SHA1"|"NONE"|"DEFAULT",
  "MdnResponse": "SYNC"|"NONE",
  "BasicAuthSecretId": "string",
  "PreserveContentType": "ENABLED"|"DISABLED"
}
```

`--access-role` (string)

Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.

**For AS2 connectors**

With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths` . We use the fileâs parent directory (for example, for `--send-file-paths /bucket/dir/file.txt` , parent directory is `/bucket/dir/` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer` .

If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.

**For SFTP connectors**

Make sure that the access role provides read and write access to the parent directory of the file location thatâs used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to Secrets Manager.

`--logging-role` (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.

`--sftp-config` (structure)

A structure that contains the parameters for an SFTP connector object.

UserSecretId -> (string)

The identifier for the secret (in Amazon Web Services Secrets Manager) that contains the SFTP userâs private key, password, or both. The identifier must be the Amazon Resource Name (ARN) of the secret.

### Note

- Required when creating an SFTP connector
- Optional when updating an existing SFTP connector

TrustedHostKeys -> (list)

The public portion of the host key, or keys, that are used to identify the external server to which you are connecting. You can use the `ssh-keyscan` command against the SFTP server to retrieve the necessary key.

### Note

`TrustedHostKeys` is optional for `CreateConnector` . If not provided, you can use `TestConnection` to retrieve the server host key during the initial connection attempt, and subsequently update the connector with the observed host key.

The three standard SSH public key format elements are `<key type>` , `<body base64>` , and an optional `<comment>` , with spaces between each element. Specify only the `<key type>` and `<body base64>` : do not enter the `<comment>` portion of the key.

For the trusted host key, Transfer Family accepts RSA and ECDSA keys.

- For RSA keys, the `<key type>` string is `ssh-rsa` .
- For ECDSA keys, the `<key type>` string is either `ecdsa-sha2-nistp256` , `ecdsa-sha2-nistp384` , or `ecdsa-sha2-nistp521` , depending on the size of the key you generated.

Run this command to retrieve the SFTP server host key, where your SFTP server name is `ftp.host.com` .

`ssh-keyscan ftp.host.com`

This prints the public host key to standard output.

`ftp.host.com ssh-rsa AAAAB3Nza...<long-string-for-public-key`

Copy and paste this string into the `TrustedHostKeys` field for the `create-connector` command or into the **Trusted host keys** field in the console.

(string)

MaxConcurrentConnections -> (integer)

Specify the number of concurrent connections that your connector creates to the remote server. The default value is `5` (this is also the maximum value allowed).

This parameter specifies the number of active connections that your connector can establish with the remote server at the same time. Increasing this value can enhance connector performance when transferring large file batches by enabling parallel operations.

Shorthand Syntax:

```
UserSecretId=string,TrustedHostKeys=string,string,MaxConcurrentConnections=integer
```

JSON Syntax:

```
{
  "UserSecretId": "string",
  "TrustedHostKeys": ["string", ...],
  "MaxConcurrentConnections": integer
}
```

`--security-policy-name` (string)

Specifies the name of the security policy for the connector.

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

ConnectorId -> (string)

Returns the identifier of the connector object that you are updating.