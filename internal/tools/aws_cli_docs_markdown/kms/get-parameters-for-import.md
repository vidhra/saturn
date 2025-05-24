# get-parameters-for-importÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-parameters-for-import.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-parameters-for-import.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# get-parameters-for-import

## Description

Returns the public key and an import token you need to import or reimport key material for a KMS key.

By default, KMS keys are created with key material that KMS generates. This operation supports [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) , an advanced feature that lets you generate and import the cryptographic key material for a KMS key. For more information about importing key material into KMS, see [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *Key Management Service Developer Guide* .

Before calling `GetParametersForImport` , use the  CreateKey operation with an `Origin` value of `EXTERNAL` to create a KMS key with no key material. You can import key material for a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, or asymmetric signing KMS key. You can also import key material into a [multi-Region key](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. However, you canât import key material into a KMS key in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) . You can also use `GetParametersForImport` to get a public key and import token to [reimport the original key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html#reimport-key-material) into a KMS key whose key material expired or was deleted.

`GetParametersForImport` returns the items that you need to import your key material.

- The public key (or âwrapping keyâ) of an RSA key pair that KMS generates. You will use this public key to encrypt (âwrapâ) your key material while itâs in transit to KMS.
- A import token that ensures that KMS can decrypt your key material and associate it with the correct KMS key.

The public key and its import token are permanently linked and must be used together. Each public key and import token set is valid for 24 hours. The expiration date and time appear in the `ParametersValidTo` field in the `GetParametersForImport` response. You cannot use an expired public key or import token in an  ImportKeyMaterial request. If your key and token expire, send another `GetParametersForImport` request.

`GetParametersForImport` requires the following information:

- The key ID of the KMS key for which you are importing the key material.
- The key spec of the public key (âwrapping keyâ) that you will use to encrypt your key material during import.
- The wrapping algorithm that you will use with the public key to encrypt your key material.

You can use the same or a different public key spec and wrapping algorithm each time you import or reimport the same key material.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : No. You cannot perform this operation on a KMS key in a different Amazon Web Services account.

**Required permissions** : [kms:GetParametersForImport](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- ImportKeyMaterial
- DeleteImportedKeyMaterial

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetParametersForImport)

## Synopsis

```
get-parameters-for-import
--key-id <value>
--wrapping-algorithm <value>
--wrapping-key-spec <value>
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

`--key-id` (string)

The identifier of the KMS key that will be associated with the imported key material. The `Origin` of the KMS key must be `EXTERNAL` .

All KMS key types are supported, including multi-Region keys. However, you cannot import key material into a KMS key in a custom key store.

Specify the key ID or key ARN of the KMS key.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey .

`--wrapping-algorithm` (string)

The algorithm you will use with the RSA public key (`PublicKey` ) in the response to protect your key material during import. For more information, see [Select a wrapping algorithm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/importing-keys-get-public-key-and-token.html#select-wrapping-algorithm) in the *Key Management Service Developer Guide* .

For RSA_AES wrapping algorithms, you encrypt your key material with an AES key that you generate, then encrypt your AES key with the RSA public key from KMS. For RSAES wrapping algorithms, you encrypt your key material directly with the RSA public key from KMS.

The wrapping algorithms that you can use depend on the type of key material that you are importing. To import an RSA private key, you must use an RSA_AES wrapping algorithm.

- **RSA_AES_KEY_WRAP_SHA_256** â Supported for wrapping RSA and ECC key material.
- **RSA_AES_KEY_WRAP_SHA_1** â Supported for wrapping RSA and ECC key material.
- **RSAES_OAEP_SHA_256** â Supported for all types of key material, except RSA key material (private key). You cannot use the RSAES_OAEP_SHA_256 wrapping algorithm with the RSA_2048 wrapping key spec to wrap ECC_NIST_P521 key material.
- **RSAES_OAEP_SHA_1** â Supported for all types of key material, except RSA key material (private key). You cannot use the RSAES_OAEP_SHA_1 wrapping algorithm with the RSA_2048 wrapping key spec to wrap ECC_NIST_P521 key material.
- **RSAES_PKCS1_V1_5** (Deprecated) â As of October 10, 2023, KMS does not support the RSAES_PKCS1_V1_5 wrapping algorithm.

Possible values:

- `RSAES_PKCS1_V1_5`
- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `RSA_AES_KEY_WRAP_SHA_1`
- `RSA_AES_KEY_WRAP_SHA_256`
- `SM2PKE`

`--wrapping-key-spec` (string)

The type of RSA public key to return in the response. You will use this wrapping key with the specified wrapping algorithm to protect your key material during import.

Use the longest RSA wrapping key that is practical.

You cannot use an RSA_2048 public key to directly wrap an ECC_NIST_P521 private key. Instead, use an RSA_AES wrapping algorithm or choose a longer RSA public key.

Possible values:

- `RSA_2048`
- `RSA_3072`
- `RSA_4096`
- `SM2`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get the items required to import key material into a KMS key**

The following `get-parameters-for-import` example gets the public key and import token that you need to import key material into a KMS key. When you use the `import-key-material` command, be sure to use the import token and key material encrypted by the public key that were returned in the same `get-parameters-for-import` command. Also, the wrapping algorithm that you specify in this command must be one that you use to encrypt the key material with the public key.

To specify the KMS key, use the `key-id` parameter. This example uses an key ID, but you can use a key ID or key ARN in this command.

```
aws kms get-parameters-for-import \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --wrapping-algorithm RSAES_OAEP_SHA_256 \
    --wrapping-key-spec RSA_2048
```

Output:

```
{
    "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "PublicKey": "<public key base64 encoded data>",
    "ImportToken": "<import token base64 encoded data>",
    "ParametersValidTo": 1593893322.32
}
```

For more information, see [Download the public key and import token](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-get-public-key-and-token.html) in the *AWS Key Management Service Developer Guide*.

## Output

KeyId -> (string)

The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) ) of the KMS key to use in a subsequent  ImportKeyMaterial request. This is the same KMS key specified in the `GetParametersForImport` request.

ImportToken -> (blob)

The import token to send in a subsequent  ImportKeyMaterial request.

PublicKey -> (blob)

The public key to use to encrypt the key material before importing it with  ImportKeyMaterial .

ParametersValidTo -> (timestamp)

The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an  ImportKeyMaterial request and you must send another `GetParametersForImport` request to get new ones.