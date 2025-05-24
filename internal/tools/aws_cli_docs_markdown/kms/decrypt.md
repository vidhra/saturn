# decryptÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/decrypt.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/decrypt.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# decrypt

## Description

Decrypts ciphertext that was encrypted by a KMS key using any of the following operations:

- Encrypt
- GenerateDataKey
- GenerateDataKeyPair
- GenerateDataKeyWithoutPlaintext
- GenerateDataKeyPairWithoutPlaintext

You can use this operation to decrypt ciphertext that was encrypted under a symmetric encryption KMS key or an asymmetric encryption KMS key. When the KMS key is asymmetric, you must specify the KMS key and the encryption algorithm that was used to encrypt the ciphertext. For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

The `Decrypt` operation also decrypts ciphertext that was encrypted outside of KMS by the public key in an KMS asymmetric KMS key. However, it cannot decrypt symmetric ciphertext produced by other libraries, such as the [Amazon Web Services Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/) or [Amazon S3 client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html) . These libraries return a ciphertext format that is incompatible with KMS.

If the ciphertext was encrypted under a symmetric encryption KMS key, the `KeyId` parameter is optional. KMS can get this information from metadata that it adds to the symmetric ciphertext blob. This feature adds durability to your implementation by ensuring that authorized users can decrypt ciphertext decades after it was encrypted, even if theyâve lost track of the key ID. However, specifying the KMS key is always recommended as a best practice. When you use the `KeyId` parameter to specify a KMS key, KMS only uses the KMS key you specify. If the ciphertext was encrypted under a different KMS key, the `Decrypt` operation fails. This practice ensures that you use the KMS key that you intend.

Whenever possible, use key policies to give users permission to call the `Decrypt` operation on a particular KMS key, instead of using &IAM; policies. Otherwise, you might create an &IAM; policy that gives the user `Decrypt` permission on all KMS keys. This user could decrypt ciphertext that was encrypted by KMS keys in other accounts if the key policy for the cross-account KMS key permits it. If you must use an IAM policy for `Decrypt` permissions, limit the user to particular KMS keys or particular trusted accounts. For details, see [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html#iam-policies-best-practices) in the *Key Management Service Developer Guide* .

`Decrypt` also supports [Amazon Web Services Nitro Enclaves](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave.html) , which provide an isolated compute environment in Amazon EC2. To call `Decrypt` for a Nitro enclave, use the [Amazon Web Services Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any Amazon Web Services SDK. Use the `Recipient` parameter to provide the attestation document for the enclave. Instead of the plaintext data, the response includes the plaintext data encrypted with the public key from the attestation document (`CiphertextForRecipient` ). For information about the interaction between KMS and Amazon Web Services Nitro Enclaves, see [How Amazon Web Services Nitro Enclaves uses KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) in the *Key Management Service Developer Guide* .

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : Yes. If you use the `KeyId` parameter to identify a KMS key in a different Amazon Web Services account, specify the key ARN or the alias ARN of the KMS key.

**Required permissions** : [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- Encrypt
- GenerateDataKey
- GenerateDataKeyPair
- ReEncrypt

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Decrypt)

## Synopsis

```
decrypt
--ciphertext-blob <value>
[--encryption-context <value>]
[--grant-tokens <value>]
[--key-id <value>]
[--encryption-algorithm <value>]
[--recipient <value>]
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

Ciphertext to be decrypted. The blob includes metadata.

`--encryption-context` (map)

Specifies the encryption context to use when decrypting the data. An encryption context is valid only for [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) with a symmetric encryption KMS key. The standard asymmetric encryption algorithms and HMAC algorithms that KMS uses do not support an encryption context.

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

`--grant-tokens` (list)

A list of grant tokens.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--key-id` (string)

Specifies the KMS key that KMS uses to decrypt the ciphertext.

Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the `Decrypt` operation throws an `IncorrectKeyException` .

This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key. If you used a symmetric encryption KMS key, KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--encryption-algorithm` (string)

Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify the same algorithm that was used to encrypt the data. If you specify a different algorithm, the `Decrypt` operation fails.

This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key. The default value, `SYMMETRIC_DEFAULT` , represents the only supported algorithm that is valid for symmetric encryption KMS keys.

Possible values:

- `SYMMETRIC_DEFAULT`
- `RSAES_OAEP_SHA_1`
- `RSAES_OAEP_SHA_256`
- `SM2PKE`

`--recipient` (structure)

A signed [attestation document](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-concepts.html#term-attestdoc) from an Amazon Web Services Nitro enclave and the encryption algorithm to use with the enclaveâs public key. The only valid encryption algorithm is `RSAES_OAEP_SHA_256` .

This parameter only supports attestation documents for Amazon Web Services Nitro Enclaves. To include this parameter, use the [Amazon Web Services Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) or any Amazon Web Services SDK.

When you use this parameter, instead of returning the plaintext data, KMS encrypts the plaintext data with the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the enclave. The `Plaintext` field in the response is null or empty.

For information about the interaction between KMS and Amazon Web Services Nitro Enclaves, see [How Amazon Web Services Nitro Enclaves uses KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) in the *Key Management Service Developer Guide* .

KeyEncryptionAlgorithm -> (string)

The encryption algorithm that KMS should use with the public key for an Amazon Web Services Nitro Enclave to encrypt plaintext values for the response. The only valid value is `RSAES_OAEP_SHA_256` .

AttestationDocument -> (blob)

The attestation document for an Amazon Web Services Nitro Enclave. This document includes the enclaveâs public key.

Shorthand Syntax:

```
KeyEncryptionAlgorithm=string,AttestationDocument=blob
```

JSON Syntax:

```
{
  "KeyEncryptionAlgorithm": "RSAES_OAEP_SHA_256",
  "AttestationDocument": blob
}
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

**Example 1: To decrypt an encrypted message with a symmetric KMS key (Linux and macOS)**

The following `decrypt` command example demonstrates the recommended way to decrypt data with the AWS CLI. This version shows how to decrypt data under a symmetric KMS key.

- Provide the ciphertext in a file.

In the value of the `--ciphertext-blob` parameter, use the `fileb://` prefix, which tells the CLI to read the data from a binary file. If the file is not in the current directory, type the full path to file. For more information about reading AWS CLI parameter values from a file, see Loading AWS CLI parameters from a file <https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html> in the *AWS Command Line Interface User Guide* and Best Practices for Local File Parameters<https://aws.amazon.com/blogs/developer/best-practices-for-local-file-parameters/> in the *AWS Command Line Tool Blog*.
- Specify the KMS key to decrypt the ciphertext.

The `--key-id` parameter is not required when decrypting with a symmetric KMS key. AWS KMS can get the key ID of the KMS key that was used to encrypt the data from the metadata in the ciphertext. But itâs always a best practice to specify the KMS key you are using. This practice ensures that you use the KMS key that you intend, and prevents you from inadvertently decrypting a ciphertext using a KMS key you do not trust.
- Request the plaintext output as a text value.

The `--query` parameter tells the CLI to get only the value of the `Plaintext` field from the output. The `--output` parameter returns the output as text.
- Base64-decode the plaintext and save it in a file.

The  following example pipes (|) the value of the `Plaintext` parameter to the Base64 utility, which decodes it. Then, it redirects (>) the decoded output to the `ExamplePlaintext` file.

Before running this command, replace the example key ID with a valid key ID from your AWS account.

```
aws kms decrypt \
    --ciphertext-blob fileb://ExampleEncryptedFile \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --output text \
    --query Plaintext | base64 \
    --decode > ExamplePlaintextFile
```

This command produces no output. The output from the `decrypt` command is base64-decoded and saved in a file.

For more information, see [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) in the *AWS Key Management Service API Reference*.

**Example 2: To decrypt an encrypted message with a symmetric KMS key (Windows command prompt)**

The following example is the same as the previous one except that it uses the `certutil` utility to Base64-decode the plaintext data. This procedure requires two commands, as shown in the following examples.

Before running this command, replace the example key ID with a valid key ID from your AWS account.

```
aws kms decrypt ^
    --ciphertext-blob fileb://ExampleEncryptedFile ^
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab ^
    --output text ^
    --query Plaintext > ExamplePlaintextFile.base64
```

Run the `certutil` command.

```
certutil -decode ExamplePlaintextFile.base64 ExamplePlaintextFile
```

Output:

```
Input Length = 18
Output Length = 12
CertUtil: -decode command completed successfully.
```

For more information, see [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) in the *AWS Key Management Service API Reference*.

**Example 3: To decrypt an encrypted message with an asymmetric KMS key (Linux and macOS)**

The following `decrypt` command example shows how to decrypt data encrypted under an RSA asymmetric KMS key.

When using an asymmetric KMS key, the `encryption-algorithm` parameter, which specifies the algorithm used to encrypt the plaintext, is required.

Before running this command, replace the example key ID with a valid key ID from your AWS account.

```
aws kms decrypt \
    --ciphertext-blob fileb://ExampleEncryptedFile \
    --key-id 0987dcba-09fe-87dc-65ba-ab0987654321 \
    --encryption-algorithm RSAES_OAEP_SHA_256 \
    --output text \
    --query Plaintext | base64 \
    --decode > ExamplePlaintextFile
```

This command produces no output. The output from the `decrypt` command is base64-decoded and saved in a file.

For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

## Output

KeyId -> (string)

The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) ) of the KMS key that was used to decrypt the ciphertext.

Plaintext -> (blob)

Decrypted plaintext data. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

If the response includes the `CiphertextForRecipient` field, the `Plaintext` field is null or empty.

EncryptionAlgorithm -> (string)

The encryption algorithm that was used to decrypt the ciphertext.

CiphertextForRecipient -> (blob)

The plaintext data encrypted with the public key in the attestation document.

This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves, see [How Amazon Web Services Nitro Enclaves uses KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) in the *Key Management Service Developer Guide* .