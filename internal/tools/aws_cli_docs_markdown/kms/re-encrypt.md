# re-encryptÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# re-encrypt

## Description

Decrypts ciphertext and then reencrypts it entirely within KMS. You can use this operation to change the KMS key under which data is encrypted, such as when you [manually rotate](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-manually) a KMS key or change the KMS key that protects a ciphertext. You can also use it to reencrypt ciphertext under the same KMS key, such as to change the [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) of a ciphertext.

The `ReEncrypt` operation can decrypt ciphertext that was encrypted by using a KMS key in an KMS operation, such as  Encrypt or  GenerateDataKey . It can also decrypt ciphertext that was encrypted by using the public key of an [asymmetric KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html#asymmetric-cmks) outside of KMS. However, it cannot decrypt ciphertext produced by other libraries, such as the [Amazon Web Services Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/) or [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html) . These libraries return a ciphertext format that is incompatible with KMS.

When you use the `ReEncrypt` operation, you need to provide information for the decrypt operation and the subsequent encrypt operation.

- If your ciphertext was encrypted under an asymmetric KMS key, you must use the `SourceKeyId` parameter to identify the KMS key that encrypted the ciphertext. You must also supply the encryption algorithm that was used. This information is required to decrypt the data.
- If your ciphertext was encrypted under a symmetric encryption KMS key, the `SourceKeyId` parameter is optional. KMS can get this information from metadata that it adds to the symmetric ciphertext blob. This feature adds durability to your implementation by ensuring that authorized users can decrypt ciphertext decades after it was encrypted, even if theyâve lost track of the key ID. However, specifying the source KMS key is always recommended as a best practice. When you use the `SourceKeyId` parameter to specify a KMS key, KMS uses only the KMS key you specify. If the ciphertext was encrypted under a different KMS key, the `ReEncrypt` operation fails. This practice ensures that you use the KMS key that you intend.
- To reencrypt the data, you must use the `DestinationKeyId` parameter to specify the KMS key that re-encrypts the data after it is decrypted. If the destination KMS key is an asymmetric KMS key, you must also provide the encryption algorithm. The algorithm that you choose must be compatible with the KMS key.

### Warning

When you use an asymmetric KMS key to encrypt or reencrypt data, be sure to record the KMS key and encryption algorithm that you choose. You will be required to provide the same KMS key and encryption algorithm when you decrypt the data. If the KMS key and algorithm do not match the values used to encrypt the data, the decrypt operation fails. You are not required to supply the key ID and encryption algorithm when you decrypt with symmetric encryption KMS keys because KMS stores this information in the ciphertext blob. KMS cannot store metadata in ciphertext generated with asymmetric keys. The standard format for asymmetric key ciphertext does not include configurable fields.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : Yes. The source KMS key and destination KMS key can be in different Amazon Web Services accounts. Either or both KMS keys can be in a different account than the caller. To specify a KMS key in a different account, you must use its key ARN or alias ARN.

**Required permissions** :

- [kms:ReEncryptFrom](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission on the source KMS key (key policy)
- [kms:ReEncryptTo](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission on the destination KMS key (key policy)

To permit reencryption from or to a KMS key, include the `"kms:ReEncrypt*"` permission in your [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) . This permission is automatically included in the key policy when you use the console to create a KMS key. But you must include it manually when you create a KMS key programmatically or when you use the  PutKeyPolicy operation to set a key policy.

**Related operations:**

- Decrypt
- Encrypt
- GenerateDataKey
- GenerateDataKeyPair

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReEncrypt)

## Synopsis

```
re-encrypt
--ciphertext-blob <value>
[--source-encryption-context <value>]
[--source-key-id <value>]
--destination-key-id <value>
[--destination-encryption-context <value>]
[--source-encryption-algorithm <value>]
[--destination-encryption-algorithm <value>]
[--grant-tokens <value>]
[--dry-run | --no-dry-run]
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

`--ciphertext-blob` (blob)

Ciphertext of the data to reencrypt.

`--source-encryption-context` (map)

Specifies the encryption context to use to decrypt the ciphertext. Enter the same encryption context that was used to encrypt the ciphertext.

An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.

For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *Key Management Service Developer Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--source-key-id` (string)

Specifies the KMS key that KMS will use to decrypt the ciphertext before it is re-encrypted.

Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the `ReEncrypt` operation throws an `IncorrectKeyException` .

This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key. If you used a symmetric encryption KMS key, KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--destination-key-id` (string)

A unique identifier for the KMS key that is used to reencrypt the data. Specify a symmetric encryption KMS key or an asymmetric KMS key with a `KeyUsage` value of `ENCRYPT_DECRYPT` . To find the `KeyUsage` value of a KMS key, use the  DescribeKey operation.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--destination-encryption-context` (map)

Specifies that encryption context to use when the reencrypting the data.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

A destination encryption context is valid only when the destination KMS key is a symmetric encryption KMS key. The standard ciphertext format for asymmetric KMS keys does not include fields for metadata.

An *encryption context* is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.

For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *Key Management Service Developer Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--source-encryption-algorithm` (string)

Specifies the encryption algorithm that KMS will use to decrypt the ciphertext before it is reencrypted. The default value, `SYMMETRIC_DEFAULT` , represents the algorithm used for symmetric encryption KMS keys.

Specify the same algorithm that was used to encrypt the ciphertext. If you specify a different algorithm, the decrypt attempt fails.

This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key.

Possible values:

- `SYMMETRIC_DEFAULT`
- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `SM2PKE`

`--destination-encryption-algorithm` (string)

Specifies the encryption algorithm that KMS will use to reecrypt the data after it has decrypted it. The default value, `SYMMETRIC_DEFAULT` , represents the encryption algorithm used for symmetric encryption KMS keys.

This parameter is required only when the destination KMS key is an asymmetric KMS key.

Possible values:

- `SYMMETRIC_DEFAULT`
- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `SM2PKE`

`--grant-tokens` (list)

A list of grant tokens.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks if your request will succeed. `DryRun` is an optional parameter.

To learn more about how to use this parameter, see [Testing your KMS API calls](https://docs.aws.amazon.com/kms/latest/developerguide/programming-dryrun.html) in the *Key Management Service Developer Guide* .

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

**Example 1: To re-encrypt an encrypted message under a different symmetric KMS key (Linux and macOS).**

The following `re-encrypt` command example demonstrates the recommended way to re-encrypt data with the AWS CLI.

- Provide the ciphertext in a file.

In the value of the `--ciphertext-blob` parameter, use the `fileb://` prefix, which tells the CLI to read the data from a binary file. If the file is not in the current directory, type the full path to file. For more information about reading AWS CLI parameter values from a file, see Loading AWS CLI parameters from a file <https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html> in the *AWS Command Line Interface User Guide* and Best Practices for Local File Parameters<https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/> in the *AWS Command Line Tool Blog*.
- Specify the source KMS key, which decrypts the ciphertext.

The `--source-key-id` parameter is not required when decrypting with symmetric encryption KMS keys. AWS KMS can get the KMS key that was used to encrypt the data from the metadata in the ciphertext blob. But itâs always a best practice to specify the KMS key you are using. This practice ensures that you use the KMS key that you intend, and prevents you from inadvertently decrypting a ciphertext using a KMS key you do not trust.
- Specify the destination KMS key, which re-encrypts the data.

The `--destination-key-id` parameter is always required. This example uses a key ARN, but you can use any valid key identifier.
- Request the plaintext output as a text value.

The `--query` parameter tells the CLI to get only the value of the `Plaintext` field from the output. The `--output` parameter returns the output as text.
- Base64-decode the plaintext and save it in a file.

The following example pipes (|) the value of the `Plaintext` parameter to the Base64 utility, which decodes it. Then, it redirects (>) the decoded output to the `ExamplePlaintext` file.

Before running this command, replace the example key IDs with valid key identifiers from your AWS account.

```
aws kms re-encrypt \
    --ciphertext-blob fileb://ExampleEncryptedFile \
    --source-key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --destination-key-id 0987dcba-09fe-87dc-65ba-ab0987654321 \
    --query CiphertextBlob \
    --output text | base64 --decode > ExampleReEncryptedFile
```

This command produces no output. The output from the `re-encrypt` command is base64-decoded and saved in a file.

For more information, see [`ReEncrypt <https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html#id1) in the *AWS Key Management Service API Reference*.

**Example 2: To re-encrypt an encrypted message under a different symmetric KMS key (Windows command prompt).**

The following `re-encrypt` command example is the same as the previous one except that it uses the `certutil` utility to Base64-decode the plaintext data. This procedure requires two commands, as shown in the following examples.

Before running this command, replace the example key ID with a valid key ID from your AWS account.

```
aws kms re-encrypt ^
    --ciphertext-blob fileb://ExampleEncryptedFile ^
    --source-key-id 1234abcd-12ab-34cd-56ef-1234567890ab ^
    --destination-key-id 0987dcba-09fe-87dc-65ba-ab0987654321 ^
    --query CiphertextBlob ^
    --output text > ExampleReEncryptedFile.base64
```

Then use the `certutil` utility

```
certutil -decode ExamplePlaintextFile.base64 ExamplePlaintextFile
```

Output:

```
Input Length = 18
Output Length = 12
CertUtil: -decode command completed successfully.
```

For more information, see [`ReEncrypt <https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/re-encrypt.html#id1) in the *AWS Key Management Service API Reference*.

## Output

CiphertextBlob -> (blob)

The reencrypted data. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

SourceKeyId -> (string)

Unique identifier of the KMS key used to originally encrypt the data.

KeyId -> (string)

The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) ) of the KMS key that was used to reencrypt the data.

SourceEncryptionAlgorithm -> (string)

The encryption algorithm that was used to decrypt the ciphertext before it was reencrypted.

DestinationEncryptionAlgorithm -> (string)

The encryption algorithm that was used to reencrypt the data.