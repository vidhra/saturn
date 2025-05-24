# put-data-catalog-encryption-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-data-catalog-encryption-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/put-data-catalog-encryption-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# put-data-catalog-encryption-settings

## Description

Sets the security configuration for a specified catalog. After the configuration has been set, the specified encryption is applied to every catalog write thereafter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/PutDataCatalogEncryptionSettings)

## Synopsis

```
put-data-catalog-encryption-settings
[--catalog-id <value>]
--data-catalog-encryption-settings <value>
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

`--catalog-id` (string)

The ID of the Data Catalog to set the security configuration for. If none is provided, the Amazon Web Services account ID is used by default.

`--data-catalog-encryption-settings` (structure)

The security configuration to set.

EncryptionAtRest -> (structure)

Specifies the encryption-at-rest configuration for the Data Catalog.

CatalogEncryptionMode -> (string)

The encryption-at-rest mode for encrypting Data Catalog data.

SseAwsKmsKeyId -> (string)

The ID of the KMS key to use for encryption at rest.

CatalogEncryptionServiceRole -> (string)

The role that Glue assumes to encrypt and decrypt the Data Catalog objects on the callerâs behalf.

ConnectionPasswordEncryption -> (structure)

When connection password protection is enabled, the Data Catalog uses a customer-provided key to encrypt the password as part of `CreateConnection` or `UpdateConnection` and store it in the `ENCRYPTED_PASSWORD` field in the connection properties. You can enable catalog encryption or only password encryption.

ReturnConnectionPasswordEncrypted -> (boolean)

When the `ReturnConnectionPasswordEncrypted` flag is set to âtrueâ, passwords remain encrypted in the responses of `GetConnection` and `GetConnections` . This encryption takes effect independently from catalog encryption.

AwsKmsKeyId -> (string)

An KMS key that is used to encrypt the connection password.

If connection password protection is enabled, the caller of `CreateConnection` and `UpdateConnection` needs at least `kms:Encrypt` permission on the specified KMS key, to encrypt passwords before storing them in the Data Catalog.

You can set the decrypt permission to enable or restrict access on the password key according to your security requirements.

Shorthand Syntax:

```
EncryptionAtRest={CatalogEncryptionMode=string,SseAwsKmsKeyId=string,CatalogEncryptionServiceRole=string},ConnectionPasswordEncryption={ReturnConnectionPasswordEncrypted=boolean,AwsKmsKeyId=string}
```

JSON Syntax:

```
{
  "EncryptionAtRest": {
    "CatalogEncryptionMode": "DISABLED"|"SSE-KMS"|"SSE-KMS-WITH-SERVICE-ROLE",
    "SseAwsKmsKeyId": "string",
    "CatalogEncryptionServiceRole": "string"
  },
  "ConnectionPasswordEncryption": {
    "ReturnConnectionPasswordEncrypted": true|false,
    "AwsKmsKeyId": "string"
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

None