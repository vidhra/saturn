# encrypt-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/encrypt-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/encrypt-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# encrypt-data

## Description

Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme. For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html) in the *Amazon Web Services Payment Cryptography User Guide* .

You can generate an encryption key within Amazon Web Services Payment Cryptography by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) . You can import your own encryption key by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) .

For this operation, the key must have `KeyModesOfUse` set to `Encrypt` . In asymmetric encryption, plaintext is encrypted using public component. You can import the public component of an asymmetric key pair created outside Amazon Web Services Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) .

This operation also supports dynamic keys, allowing you to pass a dynamic encryption key as a TR-31 WrappedKeyBlock. This can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To encrypt using dynamic keys, the `keyARN` is the Key Encryption Key (KEK) of the TR-31 wrapped encryption key material. The incoming wrapped key shall have a key purpose of D0 with a mode of use of B or D. For more information, see [Using Dynamic Keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html) in the *Amazon Web Services Payment Cryptography User Guide* .

For symmetric and DUKPT encryption, Amazon Web Services Payment Cryptography supports `TDES` and `AES` algorithms. For EMV encryption, Amazon Web Services Payment Cryptography supports `TDES` algorithms.For asymmetric encryption, Amazon Web Services Payment Cryptography supports `RSA` .

When you use TDES or TDES DUKPT, the plaintext data length must be a multiple of 8 bytes. For AES or AES DUKPT, the plaintext data length must be a multiple of 16 bytes. For RSA, it sould be equal to the key size unless padding is enabled.

To encrypt using DUKPT, you must already have a BDK (Base Derivation Key) key in your account with `KeyModesOfUse` set to `DeriveKey` , or you can generate a new DUKPT key by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) . To encrypt using EMV, you must already have an IMK (Issuer Master Key) key in your account with `KeyModesOfUse` set to `DeriveKey` .

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- DecryptData
- [GetPublicCertificate](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetPublicKeyCertificate.html)
- [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)
- ReEncryptData

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/EncryptData)

## Synopsis

```
encrypt-data
--key-identifier <value>
--plain-text <value>
--encryption-attributes <value>
[--wrapped-key <value>]
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

`--key-identifier` (string)

The `keyARN` of the encryption key that Amazon Web Services Payment Cryptography uses for plaintext encryption.

When a WrappedKeyBlock is provided, this value will be the identifier to the key wrapping key. Otherwise, it is the key identifier used to perform the operation.

`--plain-text` (string)

The plaintext to be encrypted.

### Note

For encryption using asymmetric keys, plaintext data length is constrained by encryption key strength that you define in `KeyAlgorithm` and padding type that you define in `AsymmetricEncryptionAttributes` . For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html) in the *Amazon Web Services Payment Cryptography User Guide* .

`--encryption-attributes` (tagged union structure)

The encryption key type and attributes for plaintext encryption.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Symmetric`, `Asymmetric`, `Dukpt`, `Emv`.

Symmetric -> (structure)

Parameters that are required to perform encryption and decryption using symmetric keys.

Mode -> (string)

The block cipher method to use for encryption.

InitializationVector -> (string)

An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.

PaddingType -> (string)

The padding to be included with the data.

Asymmetric -> (structure)

Parameters for plaintext encryption using asymmetric keys.

PaddingType -> (string)

The padding to be included with the data.

Dukpt -> (structure)

Parameters that are required to encrypt plaintext data using DUKPT.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

Mode -> (string)

The block cipher method to use for encryption.

The default is CBC.

DukptKeyDerivationType -> (string)

The key type encrypted using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY`

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be incoming data decryption, outgoing data encryption, or both.

InitializationVector -> (string)

An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.

Emv -> (structure)

Parameters for plaintext encryption using EMV keys.

MajorKeyDerivationMode -> (string)

The EMV derivation mode to use for ICC master key derivation as per EMV version 4.3 book 2.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

SessionDerivationData -> (string)

The derivation value used to derive the ICC session key. It is typically the application transaction counter value padded with zeros or previous ARQC value padded with zeros as per EMV version 4.3 book 2.

Mode -> (string)

The block cipher method to use for encryption.

InitializationVector -> (string)

An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.

Shorthand Syntax:

```
Symmetric={Mode=string,InitializationVector=string,PaddingType=string},Asymmetric={PaddingType=string},Dukpt={KeySerialNumber=string,Mode=string,DukptKeyDerivationType=string,DukptKeyVariant=string,InitializationVector=string},Emv={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,SessionDerivationData=string,Mode=string,InitializationVector=string}
```

JSON Syntax:

```
{
  "Symmetric": {
    "Mode": "ECB"|"CBC"|"CFB"|"CFB1"|"CFB8"|"CFB64"|"CFB128"|"OFB",
    "InitializationVector": "string",
    "PaddingType": "PKCS1"|"OAEP_SHA1"|"OAEP_SHA256"|"OAEP_SHA512"
  },
  "Asymmetric": {
    "PaddingType": "PKCS1"|"OAEP_SHA1"|"OAEP_SHA256"|"OAEP_SHA512"
  },
  "Dukpt": {
    "KeySerialNumber": "string",
    "Mode": "ECB"|"CBC",
    "DukptKeyDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256",
    "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE",
    "InitializationVector": "string"
  },
  "Emv": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "SessionDerivationData": "string",
    "Mode": "ECB"|"CBC",
    "InitializationVector": "string"
  }
}
```

`--wrapped-key` (structure)

The WrappedKeyBlock containing the encryption key for plaintext encryption.

WrappedKeyMaterial -> (tagged union structure)

Parameter information of a WrappedKeyBlock for encryption key exchange.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Tr31KeyBlock`, `DiffieHellmanSymmetricKey`.

Tr31KeyBlock -> (string)

The TR-31 wrapped key block.

DiffieHellmanSymmetricKey -> (structure)

The parameter information for deriving a ECDH shared key.

CertificateAuthorityPublicKeyIdentifier -> (string)

The `keyArn` of the certificate that signed the clientâs `PublicKeyCertificate` .

PublicKeyCertificate -> (string)

The clientâs public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.

KeyAlgorithm -> (string)

The key algorithm of the derived ECDH key.

KeyDerivationFunction -> (string)

The key derivation function to use for deriving a key using ECDH.

KeyDerivationHashAlgorithm -> (string)

The hash type to use for deriving a key using ECDH.

SharedInformation -> (string)

A byte string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.

It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes, and re-using shared information for multiple ECDH key derivations is not recommended.

KeyCheckValueAlgorithm -> (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

Shorthand Syntax:

```
WrappedKeyMaterial={Tr31KeyBlock=string,DiffieHellmanSymmetricKey={CertificateAuthorityPublicKeyIdentifier=string,PublicKeyCertificate=string,KeyAlgorithm=string,KeyDerivationFunction=string,KeyDerivationHashAlgorithm=string,SharedInformation=string}},KeyCheckValueAlgorithm=string
```

JSON Syntax:

```
{
  "WrappedKeyMaterial": {
    "Tr31KeyBlock": "string",
    "DiffieHellmanSymmetricKey": {
      "CertificateAuthorityPublicKeyIdentifier": "string",
      "PublicKeyCertificate": "string",
      "KeyAlgorithm": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256",
      "KeyDerivationFunction": "NIST_SP800"|"ANSI_X963",
      "KeyDerivationHashAlgorithm": "SHA_256"|"SHA_384"|"SHA_512",
      "SharedInformation": "string"
    }
  },
  "KeyCheckValueAlgorithm": "CMAC"|"ANSI_X9_24"
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

**To encrypt data**

The following `encrypt-data` example encrypts plaintext data using a symmetric key. For this operation, the key must have `KeyModesOfUse` set to `Encrypt` and `KeyUsage` set to `TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`.

```
aws payment-cryptography-data encrypt-data \
    --key-identifier arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h \
    --plain-text 31323334313233343132333431323334 \
    --encryption-attributes 'Symmetric={Mode=CBC}'
```

Output:

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h",
    "KeyCheckValue": "71D7AE",
    "CipherText": "33612AB9D6929C3A828EB6030082B2BD"
}
```

For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html) in the *AWS Payment Cryptography User Guide*.

## Output

KeyArn -> (string)

The `keyARN` of the encryption key that Amazon Web Services Payment Cryptography uses for plaintext encryption.

KeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.

CipherText -> (string)

The encrypted ciphertext.