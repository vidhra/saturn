# derive-shared-secretÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/derive-shared-secret.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/derive-shared-secret.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# derive-shared-secret

## Description

Derives a shared secret using a key agreement algorithm.

### Note

You must use an asymmetric NIST-recommended elliptic curve (ECC) or SM2 (China Regions only) KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT` to call DeriveSharedSecret.

DeriveSharedSecret uses the [Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60) (ECDH) to establish a key agreement between two peers by deriving a shared secret from their elliptic curve public-private key pairs. You can use the raw shared secret that DeriveSharedSecret returns to derive a symmetric key that can encrypt and decrypt data that is sent between the two peers, or that can generate and verify HMACs. KMS recommends that you follow [NIST recommendations for key derivation](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Cr2.pdf) when using the raw shared secret to derive a symmetric key.

The following workflow demonstrates how to establish key agreement over an insecure communication channel using DeriveSharedSecret.

- **Alice** calls  CreateKey to create an asymmetric KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT` . The asymmetric KMS key must use a NIST-recommended elliptic curve (ECC) or SM2 (China Regions only) key spec.
- **Bob** creates an elliptic curve key pair. Bob can call  CreateKey to create an asymmetric KMS key pair or generate a key pair outside of KMS. Bobâs key pair must use the same NIST-recommended elliptic curve (ECC) or SM2 (China Regions ony) curve as Alice.
- Alice and Bob **exchange their public keys** through an insecure communication channel (like the internet). Use  GetPublicKey to download the public key of your asymmetric KMS key pair.

### Note

KMS strongly recommends verifying that the public key you receive came from the expected party before using it to derive a shared secret.

- **Alice** calls DeriveSharedSecret. KMS uses the private key from the KMS key pair generated in **Step 1** , Bobâs public key, and the Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive to derive the shared secret. The private key in your KMS key pair never leaves KMS unencrypted. DeriveSharedSecret returns the raw shared secret.
- **Bob** uses the Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive to calculate the same raw secret using his private key and Aliceâs public key.

To derive a shared secret you must provide a key agreement algorithm, the private key of the callerâs asymmetric NIST-recommended elliptic curve or SM2 (China Regions only) KMS key pair, and the public key from your peerâs NIST-recommended elliptic curve or SM2 (China Regions only) key pair. The public key can be from another asymmetric KMS key pair or from a key pair generated outside of KMS, but both key pairs must be on the same elliptic curve.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : Yes. To perform this operation with a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

**Required permissions** : [kms:DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- CreateKey
- GetPublicKey
- DescribeKey

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeriveSharedSecret)

## Synopsis

```
derive-shared-secret
--key-id <value>
--key-agreement-algorithm <value>
--public-key <value>
[--grant-tokens <value>]
[--dry-run | --no-dry-run]
[--recipient <value>]
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

Identifies an asymmetric NIST-recommended ECC or SM2 (China Regions only) KMS key. KMS uses the private key in the specified key pair to derive the shared secret. The key usage of the KMS key must be `KEY_AGREEMENT` . To find the `KeyUsage` of a KMS key, use the  DescribeKey operation.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--key-agreement-algorithm` (string)

Specifies the key agreement algorithm used to derive the shared secret. The only valid value is `ECDH` .

Possible values:

- `ECDH`

`--public-key` (blob)

Specifies the public key in your peerâs NIST-recommended elliptic curve (ECC) or SM2 (China Regions only) key pair.

The public key must be a DER-encoded X.509 public key, also known as `SubjectPublicKeyInfo` (SPKI), as defined in [RFC 5280](https://tools.ietf.org/html/rfc5280) .

GetPublicKey returns the public key of an asymmetric KMS key pair in the required DER-encoded format.

### Note

If you use [Amazon Web Services CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html) , you must provide the DER-encoded X.509 public key in a file. Otherwise, the Amazon Web Services CLI Base64-encodes the public key a second time, resulting in a `ValidationException` .

You can specify the public key as binary data in a file using fileb (`fileb://<path-to-file>` ) or in-line using a Base64 encoded string.

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

`--recipient` (structure)

A signed [attestation document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc) from an Amazon Web Services Nitro enclave and the encryption algorithm to use with the enclaveâs public key. The only valid encryption algorithm is `RSAES_OAEP_SHA_256` .

This parameter only supports attestation documents for Amazon Web Services Nitro Enclaves. To call DeriveSharedSecret for an Amazon Web Services Nitro Enclaves, use the [Amazon Web Services Nitro Enclaves SDK](https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk) to generate the attestation document and then use the Recipient parameter from any Amazon Web Services SDK to provide the attestation document for the enclave.

When you use this parameter, instead of returning a plaintext copy of the shared secret, KMS encrypts the plaintext shared secret under the public key in the attestation document, and returns the resulting ciphertext in the `CiphertextForRecipient` field in the response. This ciphertext can be decrypted only with the private key in the enclave. The `CiphertextBlob` field in the response contains the encrypted shared secret derived from the KMS key specified by the `KeyId` parameter and public key specified by the `PublicKey` parameter. The `SharedSecret` field in the response is null or empty.

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

**To derive a shared secret**

The following `derive-shared-secret` example derives a shared secret using a key agreement algorithm.

You must use an asymmetric NIST-recommended elliptic curve (ECC) or SM2 (China Regions only) KMS key pair with a `KeyUsage` value of `KEY_AGREEMENT` to call DeriveSharedSecret.

```
aws kms derive-shared-secret \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --key-agreement-algorithm ECDH \
    --public-key "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvH3Yj0wbkLEpUl95Cv1cJVjsVNSjwGq3tCLnzXfhVwVvmzGN8pYj3U8nKwgouaHbBWNJYjP5VutbbkKS4Kv4GojwZBJyHN17kmxo8yTjRmjR15SKIQ8cqRA2uaERMLnpztIXdZp232PQPbWGxDyXYJ0aJ5EFSag"
```

Output:

```
{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "SharedSecret": "MEYCIQCKZLWyTk5runarx6XiAkU9gv3lbwPO/pHa+DXFehzdDwIhANwpsIV2g/9SPWLLsF6p/hiSskuIXMTRwqrMdVKWTMHG",
    "KeyAgreementAlgorithm": "ECDH",
    "KeyOrigin": "AWS_KMS"
}
```

For more information, see [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret.html) in the *AWS Key Management Service API Reference*.

## Output

KeyId -> (string)

Identifies the KMS key used to derive the shared secret.

SharedSecret -> (blob)

The raw secret derived from the specified key agreement algorithm, private key in the asymmetric KMS key, and your peerâs public key.

If the response includes the `CiphertextForRecipient` field, the `SharedSecret` field is null or empty.

CiphertextForRecipient -> (blob)

The plaintext shared secret encrypted with the public key in the attestation document.

This field is included in the response only when the `Recipient` parameter in the request includes a valid attestation document from an Amazon Web Services Nitro enclave. For information about the interaction between KMS and Amazon Web Services Nitro Enclaves, see [How Amazon Web Services Nitro Enclaves uses KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-nitro-enclaves.html) in the *Key Management Service Developer Guide* .

KeyAgreementAlgorithm -> (string)

Identifies the key agreement algorithm used to derive the shared secret.

KeyOrigin -> (string)

The source of the key material for the specified KMS key.

When this value is `AWS_KMS` , KMS created the key material. When this value is `EXTERNAL` , the key material was imported or the KMS key doesnât have any key material.

The only valid values for DeriveSharedSecret are `AWS_KMS` and `EXTERNAL` . DeriveSharedSecret does not support KMS keys with a `KeyOrigin` value of `AWS_CLOUDHSM` or `EXTERNAL_KEY_STORE` .