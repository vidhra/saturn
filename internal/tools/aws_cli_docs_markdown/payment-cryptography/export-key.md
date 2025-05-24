# export-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/export-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/export-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html#cli-aws-payment-cryptography) ]

# export-key

## Description

Exports a key from Amazon Web Services Payment Cryptography.

Amazon Web Services Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With `ExportKey` you can export symmetric keys using either symmetric and asymmetric key exchange mechanisms. Using this operation, you can share your Amazon Web Services Payment Cryptography generated keys with other service partners to perform cryptographic operations outside of Amazon Web Services Payment Cryptography

For symmetric key exchange, Amazon Web Services Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, Amazon Web Services Payment Cryptography supports ANSI X9 TR-34 norm and RSA wrap and unwrap key exchange mechanism. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK). After which you can export working keys using symmetric method to perform various cryptographic operations within Amazon Web Services Payment Cryptography.

The TR-34 norm is intended for exchanging 3DES keys only and keys are imported in a WrappedKeyBlock format. Key attributes (such as KeyUsage, KeyAlgorithm, KeyModesOfUse, Exportability) are contained within the key block. With RSA wrap and unwrap, you can exchange both 3DES and AES-128 keys. The keys are imported in a WrappedKeyCryptogram format and you will need to specify the key attributes during import.

You can also use `ExportKey` functionality to generate and export an IPEK (Initial Pin Encryption Key) from Amazon Web Services Payment Cryptography using either TR-31 or TR-34 export key exchange. IPEK is generated from BDK (Base Derivation Key) and `ExportDukptInitialKey` attribute KSN (`KeySerialNumber` ). The generated IPEK does not persist within Amazon Web Services Payment Cryptography and has to be re-generated each time during export.

For key exchange using TR-31 or TR-34 key blocks, you can also export optional blocks within the key block header which contain additional attribute information about the key. The `KeyVersion` within `KeyBlockHeaders` indicates the version of the key within the key block. Furthermore, `KeyExportability` within `KeyBlockHeaders` can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.

The `OptionalBlocks` contain the additional data related to the key. For information on data type that can be included within optional blocks, refer to [ASC X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) .

### Note

Data included in key block headers is signed but transmitted in clear text. Sensitive or confidential information should not be included in optional blocks. Refer to ASC X9.143-2022 standard for information on allowed data type.

**To export initial keys (KEK) or IPEK using TR-34**

Using this operation, you can export initial key using TR-34 asymmetric key exchange. You can only export KEK generated within Amazon Web Services Payment Cryptography. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During key export process, KDH is Amazon Web Services Payment Cryptography which initiates key export and KRD is the user receiving the key.

To initiate TR-34 key export, the KRD must obtain an export token by calling [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html) . This operation also generates a key pair for the purpose of key export, signs the key and returns back the signing public key certificate (also known as KDH signing certificate) and root certificate chain. The KDH uses the private key to sign the the export payload and the signing public key certificate is provided to KRD to verify the signature. The KRD can import the root certificate into its Hardware Security Module (HSM), as required. The export token and the associated KDH signing certificate expires after 7 days.

Next the KRD generates a key pair for the the purpose of encrypting the KDH key and provides the public key cerificate (also known as KRD wrapping certificate) back to KDH. The KRD will also import the root cerificate chain into Amazon Web Services Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) for `RootCertificatePublicKey` . The KDH, Amazon Web Services Payment Cryptography, will use the KRD wrapping cerificate to encrypt (wrap) the key under export and signs it with signing private key to generate a TR-34 WrappedKeyBlock. For more information on TR-34 key export, see section [Exporting symmetric keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html) in the *Amazon Web Services Payment Cryptography User Guide* .

Set the following parameters:

- `ExportAttributes` : Specify export attributes in case of IPEK export. This parameter is optional for KEK export.
- `ExportKeyIdentifier` : The `KeyARN` of the KEK or BDK (in case of IPEK) under export.
- `KeyMaterial` : Use `Tr34KeyBlock` parameters.
- `CertificateAuthorityPublicKeyIdentifier` : The `KeyARN` of the certificate chain that signed the KRD wrapping key certificate.
- `ExportToken` : Obtained from KDH by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) .
- `WrappingKeyCertificate` : The public key certificate in PEM format (base64 encoded) of the KRD wrapping key Amazon Web Services Payment Cryptography uses for encryption of the TR-34 export payload. This certificate must be signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into Amazon Web Services Payment Cryptography.

When this operation is successful, Amazon Web Services Payment Cryptography returns the KEK or IPEK as a TR-34 WrappedKeyBlock.

**To export initial keys (KEK) or IPEK using RSA Wrap and Unwrap**

Using this operation, you can export initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate export, generate an asymmetric key pair on the receiving HSM and obtain the public key certificate in PEM format (base64 encoded) for the purpose of wrapping and the root certifiate chain. Import the root certificate into Amazon Web Services Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) for `RootCertificatePublicKey` .

Next call `ExportKey` and set the following parameters:

- `CertificateAuthorityPublicKeyIdentifier` : The `KeyARN` of the certificate chain that signed wrapping key certificate.
- `KeyMaterial` : Set to `KeyCryptogram` .
- `WrappingKeyCertificate` : The public key certificate in PEM format (base64 encoded) obtained by the receiving HSM and signed by the root certificate (CertificateAuthorityPublicKeyIdentifier) imported into Amazon Web Services Payment Cryptography. The receiving HSM uses its private key component to unwrap the WrappedKeyCryptogram.

When this operation is successful, Amazon Web Services Payment Cryptography returns the WrappedKeyCryptogram.

**To export working keys or IPEK using TR-31**

Using this operation, you can export working keys or IPEK using TR-31 symmetric key exchange. In TR-31, you must use an initial key such as KEK to encrypt or wrap the key under export. To establish a KEK, you can use [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) or [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) .

Set the following parameters:

- `ExportAttributes` : Specify export attributes in case of IPEK export. This parameter is optional for KEK export.
- `ExportKeyIdentifier` : The `KeyARN` of the KEK or BDK (in case of IPEK) under export.
- `KeyMaterial` : Use `Tr31KeyBlock` parameters.

When this operation is successful, Amazon Web Services Payment Cryptography returns the working key or IPEK as a TR-31 WrappedKeyBlock.

**Cross-account use:** This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html)
- [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-2021-09-14/ExportKey)

## Synopsis

```
export-key
--key-material <value>
--export-key-identifier <value>
[--export-attributes <value>]
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

`--key-material` (tagged union structure)

The key block format type, for example, TR-34 or TR-31, to use during key material export.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Tr31KeyBlock`, `Tr34KeyBlock`, `KeyCryptogram`, `DiffieHellmanTr31KeyBlock`.

Tr31KeyBlock -> (structure)

Parameter information for key material export using symmetric TR-31 key exchange method.

WrappingKeyIdentifier -> (string)

The `KeyARN` of the the wrapping key. This key encrypts or wraps the key under export for TR-31 key block generation.

KeyBlockHeaders -> (structure)

Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key. The modes of use are deï¬ned in section A.5.3 of the TR-31 spec.

Encrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to encrypt data.

Decrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to decrypt data.

Wrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to wrap other keys.

Unwrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to unwrap other keys.

Generate -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to generate and verify other card and PIN verification keys.

Sign -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used for signing.

Verify -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to verify signatures.

DeriveKey -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to derive new keys.

NoRestrictions -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key has no special restrictions other than the restrictions implied by `KeyUsage` .

KeyExportability -> (string)

Specifies subsequent exportability of the key within the key block after it is received by the receiving party. It can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.

When set to `EXPORTABLE` , the key can be subsequently exported by the receiver under a KEK using TR-31 or TR-34 key block export only. When set to `NON_EXPORTABLE` , the key cannot be subsequently exported by the receiver. When set to `SENSITIVE` , the key can be exported by the receiver under a KEK using TR-31, TR-34, RSA wrap and unwrap cryptogram or using a symmetric cryptogram key export method. For further information refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) .

KeyVersion -> (string)

Parameter used to indicate the version of the key carried in the key block or indicate the value carried in the key block is a component of a key.

OptionalBlocks -> (map)

Parameter used to indicate the type of optional data in key block headers. Refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) for information on allowed data type for optional blocks.

Optional block character limit is 112 characters. For each optional block, 2 characters are reserved for optional block ID and 2 characters reserved for optional block length. More than one optional blocks can be included as long as the combined length does not increase 112 characters.

key -> (string)

value -> (string)

Tr34KeyBlock -> (structure)

Parameter information for key material export using the asymmetric TR-34 key exchange method.

CertificateAuthorityPublicKeyIdentifier -> (string)

The `KeyARN` of the certificate chain that signs the wrapping key certificate during TR-34 key export.

WrappingKeyCertificate -> (string)

The `KeyARN` of the wrapping key certificate. Amazon Web Services Payment Cryptography uses this certificate to wrap the key under export.

ExportToken -> (string)

The export token to initiate key export from Amazon Web Services Payment Cryptography. It also contains the signing key certificate that will sign the wrapped key during TR-34 key block generation. Call [GetParametersForExport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForExport.html) to receive an export token. It expires after 7 days. You can use the same export token to export multiple keys from the same service account.

KeyBlockFormat -> (string)

The format of key block that Amazon Web Services Payment Cryptography will use during key export.

RandomNonce -> (string)

A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.

KeyBlockHeaders -> (structure)

Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key. The modes of use are deï¬ned in section A.5.3 of the TR-31 spec.

Encrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to encrypt data.

Decrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to decrypt data.

Wrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to wrap other keys.

Unwrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to unwrap other keys.

Generate -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to generate and verify other card and PIN verification keys.

Sign -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used for signing.

Verify -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to verify signatures.

DeriveKey -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to derive new keys.

NoRestrictions -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key has no special restrictions other than the restrictions implied by `KeyUsage` .

KeyExportability -> (string)

Specifies subsequent exportability of the key within the key block after it is received by the receiving party. It can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.

When set to `EXPORTABLE` , the key can be subsequently exported by the receiver under a KEK using TR-31 or TR-34 key block export only. When set to `NON_EXPORTABLE` , the key cannot be subsequently exported by the receiver. When set to `SENSITIVE` , the key can be exported by the receiver under a KEK using TR-31, TR-34, RSA wrap and unwrap cryptogram or using a symmetric cryptogram key export method. For further information refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) .

KeyVersion -> (string)

Parameter used to indicate the version of the key carried in the key block or indicate the value carried in the key block is a component of a key.

OptionalBlocks -> (map)

Parameter used to indicate the type of optional data in key block headers. Refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) for information on allowed data type for optional blocks.

Optional block character limit is 112 characters. For each optional block, 2 characters are reserved for optional block ID and 2 characters reserved for optional block length. More than one optional blocks can be included as long as the combined length does not increase 112 characters.

key -> (string)

value -> (string)

KeyCryptogram -> (structure)

Parameter information for key material export using asymmetric RSA wrap and unwrap key exchange method

CertificateAuthorityPublicKeyIdentifier -> (string)

The `KeyARN` of the certificate chain that signs the wrapping key certificate during RSA wrap and unwrap key export.

WrappingKeyCertificate -> (string)

The wrapping key certificate in PEM format (base64 encoded). Amazon Web Services Payment Cryptography uses this certificate to wrap the key under export.

WrappingSpec -> (string)

The wrapping spec for the key under export.

DiffieHellmanTr31KeyBlock -> (structure)

Parameter information for key material export using the asymmetric ECDH key exchange method.

PrivateKeyIdentifier -> (string)

The `keyARN` of the asymmetric ECC key.

CertificateAuthorityPublicKeyIdentifier -> (string)

The `keyARN` of the certificate that signed the clientâs `PublicKeyCertificate` .

PublicKeyCertificate -> (string)

The clientâs public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.

DeriveKeyAlgorithm -> (string)

The key algorithm of the derived ECDH key.

KeyDerivationFunction -> (string)

The key derivation function to use for deriving a key using ECDH.

KeyDerivationHashAlgorithm -> (string)

The hash type to use for deriving a key using ECDH.

DerivationData -> (tagged union structure)

Derivation data used to derive an ECDH key.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SharedInformation`.

SharedInformation -> (string)

A byte string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.

It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes, and re-using shared information for multiple ECDH key derivations is not recommended.

KeyBlockHeaders -> (structure)

Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key. The modes of use are deï¬ned in section A.5.3 of the TR-31 spec.

Encrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to encrypt data.

Decrypt -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to decrypt data.

Wrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to wrap other keys.

Unwrap -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to unwrap other keys.

Generate -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to generate and verify other card and PIN verification keys.

Sign -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used for signing.

Verify -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to verify signatures.

DeriveKey -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key can be used to derive new keys.

NoRestrictions -> (boolean)

Speciï¬es whether an Amazon Web Services Payment Cryptography key has no special restrictions other than the restrictions implied by `KeyUsage` .

KeyExportability -> (string)

Specifies subsequent exportability of the key within the key block after it is received by the receiving party. It can be used to further restrict exportability of the key after export from Amazon Web Services Payment Cryptography.

When set to `EXPORTABLE` , the key can be subsequently exported by the receiver under a KEK using TR-31 or TR-34 key block export only. When set to `NON_EXPORTABLE` , the key cannot be subsequently exported by the receiver. When set to `SENSITIVE` , the key can be exported by the receiver under a KEK using TR-31, TR-34, RSA wrap and unwrap cryptogram or using a symmetric cryptogram key export method. For further information refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) .

KeyVersion -> (string)

Parameter used to indicate the version of the key carried in the key block or indicate the value carried in the key block is a component of a key.

OptionalBlocks -> (map)

Parameter used to indicate the type of optional data in key block headers. Refer to [ANSI X9.143-2022](https://webstore.ansi.org/standards/ascx9/ansix91432022) for information on allowed data type for optional blocks.

Optional block character limit is 112 characters. For each optional block, 2 characters are reserved for optional block ID and 2 characters reserved for optional block length. More than one optional blocks can be included as long as the combined length does not increase 112 characters.

key -> (string)

value -> (string)

JSON Syntax:

```
{
  "Tr31KeyBlock": {
    "WrappingKeyIdentifier": "string",
    "KeyBlockHeaders": {
      "KeyModesOfUse": {
        "Encrypt": true|false,
        "Decrypt": true|false,
        "Wrap": true|false,
        "Unwrap": true|false,
        "Generate": true|false,
        "Sign": true|false,
        "Verify": true|false,
        "DeriveKey": true|false,
        "NoRestrictions": true|false
      },
      "KeyExportability": "EXPORTABLE"|"NON_EXPORTABLE"|"SENSITIVE",
      "KeyVersion": "string",
      "OptionalBlocks": {"string": "string"
        ...}
    }
  },
  "Tr34KeyBlock": {
    "CertificateAuthorityPublicKeyIdentifier": "string",
    "WrappingKeyCertificate": "string",
    "ExportToken": "string",
    "KeyBlockFormat": "X9_TR34_2012",
    "RandomNonce": "string",
    "KeyBlockHeaders": {
      "KeyModesOfUse": {
        "Encrypt": true|false,
        "Decrypt": true|false,
        "Wrap": true|false,
        "Unwrap": true|false,
        "Generate": true|false,
        "Sign": true|false,
        "Verify": true|false,
        "DeriveKey": true|false,
        "NoRestrictions": true|false
      },
      "KeyExportability": "EXPORTABLE"|"NON_EXPORTABLE"|"SENSITIVE",
      "KeyVersion": "string",
      "OptionalBlocks": {"string": "string"
        ...}
    }
  },
  "KeyCryptogram": {
    "CertificateAuthorityPublicKeyIdentifier": "string",
    "WrappingKeyCertificate": "string",
    "WrappingSpec": "RSA_OAEP_SHA_256"|"RSA_OAEP_SHA_512"
  },
  "DiffieHellmanTr31KeyBlock": {
    "PrivateKeyIdentifier": "string",
    "CertificateAuthorityPublicKeyIdentifier": "string",
    "PublicKeyCertificate": "string",
    "DeriveKeyAlgorithm": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256",
    "KeyDerivationFunction": "NIST_SP800"|"ANSI_X963",
    "KeyDerivationHashAlgorithm": "SHA_256"|"SHA_384"|"SHA_512",
    "DerivationData": {
      "SharedInformation": "string"
    },
    "KeyBlockHeaders": {
      "KeyModesOfUse": {
        "Encrypt": true|false,
        "Decrypt": true|false,
        "Wrap": true|false,
        "Unwrap": true|false,
        "Generate": true|false,
        "Sign": true|false,
        "Verify": true|false,
        "DeriveKey": true|false,
        "NoRestrictions": true|false
      },
      "KeyExportability": "EXPORTABLE"|"NON_EXPORTABLE"|"SENSITIVE",
      "KeyVersion": "string",
      "OptionalBlocks": {"string": "string"
        ...}
    }
  }
}
```

`--export-key-identifier` (string)

The `KeyARN` of the key under export from Amazon Web Services Payment Cryptography.

`--export-attributes` (structure)

The attributes for IPEK generation during export.

ExportDukptInitialKey -> (structure)

Parameter information for IPEK export.

KeySerialNumber -> (string)

The KSN for IPEK generation using DUKPT.

KSN must be padded before sending to Amazon Web Services Payment Cryptography. KSN hex length should be 20 for a TDES_2KEY key or 24 for an AES key.

KeyCheckValueAlgorithm -> (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity. Specify KCV for IPEK export only.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

Shorthand Syntax:

```
ExportDukptInitialKey={KeySerialNumber=string},KeyCheckValueAlgorithm=string
```

JSON Syntax:

```
{
  "ExportDukptInitialKey": {
    "KeySerialNumber": "string"
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

**To export a key**

The following `export-key` example exports a key.

```
aws payment-cryptography export-key \
    --export-key-identifier arn:aws:payment-cryptography:us-west-2:123456789012:key/lco3w6agsk7zgu2l \
    --key-material '{"Tr34KeyBlock": { \
        "CertificateAuthorityPublicKeyIdentifier": "arn:aws:payment-cryptography:us-west-2:123456789012:key/ftobshq7pvioc5fx", \
        "ExportToken": "export-token-cu4lg26ofcziixny", \
        "KeyBlockFormat": "X9_TR34_2012", \
        "WrappingKeyCertificate": file://wrapping-key-certificate.pem }}'
```

Contents of `wrapping-key-certificate.pem`:

```
LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUV2VENDQXFXZ0F3SUJBZ0lSQU1ZZS8xMXFUK2svVzlRUDJQOElVdWd3RFFZSktvWklodmNOQVFFTkJRQXcKZ1lreEN6QUpCZ05WQkFZVEFsVlRNUmt3RndZRFZRUUtEQkJCVjFNZ1EzSjVjSFJ2WjNKaGNHaDVNU0V3SHdZRApWUVFMREJoQlYxTWdVR0Y1YldWdWRDQkRjbmx3ZEc5bmNtRndhSGt4RVRBUEJnTlZCQWdNQ0ZacGNtZHBibWxoCk1SVXdFd1lEVlFRRERBd3dOelUxTlRZNU5UTTNOVEF4RWpBUUJnTlZCQWNNQ1VGeWJHbHVaM1J2YmpBZUZ3MHkKTXpBMk1UTXhOelV6TVROYUZ3MHlNekEyTWpBeE9EVXpNVEphTUN3eEZUQVRCZ05WQkFNTUREQTNOVFUxTmprMQpNemMxTURFVE1CRUdBMVVFQlJNS09URTFNRGMzTnpRMk9EQ0NBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQCkFEQ0NBUW9DZ2dFQkFNUjZsVTZ0SFJwcWtCQmI1Z2FFa0FrbVRxNEgwNUQ2UXR2MS9WemhSaThtNVBFMjVtMFIKVnRtZmsxcUEySi94TEROTEl3dHFDR3BIVldOM0JMdFhuSmh2Y1dNNkI0QlRRVXNicENMbG9PYW1jMGF0UXRmeQo0ZUhoWHJoT2lDMFVpR05zeTc5ZlltTkZ3Q3RrSDhvZzJXTEdYNldXNSszRzlTaFZKR3dhbWpNamtlOVo1a0FhCnJKZHk4Y2tsMTFBTS8wQjVZRFR2TU5KVTcyZnVUMlJ5KzVoRmdFTE14aS8vbGE1TnFCQWp5VTY0cmV3eGdVSjAKZ1pVM3lJU2F2UjFwMElNOFNvZzdXUHlkVlNNTitZeTdLMG1OL3lFa3FZTWQxZWxvS1I0OVV3V0hvdzFMcHVzcwpzMDh5a0diWGxsMnBvZ3NvSmZZaFFGWTc4UmRsTU9vY2dOc0NBd0VBQWFOOE1Ib3dDUVlEVlIwVEJBSXdBREFmCkJnTlZIU01FR0RBV2dCU2tDVlVEZzJGZDdPZWpVSUlVRnBvbUpxWG9FREFkQmdOVkhRNEVGZ1FVZU1sRzJ5dkgKamxsQzM2OUV2U3hIcXBBODVkMHdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01CMEdBMVVkSlFRV01CUUdDQ3NHQVFVRgpCd01CQmdnckJnRUZCUWNEQWpBTkJna3Foa2lHOXcwQkFRMEZBQU9DQWdFQURNS2gxbnhYWWtncVkwYmMwVjA1ClNCUTBlcm5vMmsxbXdRQnhpUDBpcUpMdWNFUnF6b0RzOTBJWTN5SjhjMkMzU2kzU1JrVzBmQUhKR0VucTlzblgKbGdGWnRBZmtNbzR4Wllpb1JGZmY1TWdSOUdNaUZNQnVQS2tIeGxKc0R2NllSbnp1Zmkza1lDT1NzeWE4U2tTMQp2M2l2UEpLcTk3aDBBaThoNFQ3clBtN0NNSnYxZ0JTUEF4UVdtdndES2RrTjFsd0VudmtGdzlLZjhqeVpaNjhGCjlmUFV4Z1RvYm1MSmNialZxaFdsQ3U1VE9mSGNPR2RLRURwZE54RE12ODNZZ1ZaWUszclc4UHVxWWIyWFdMR2IKdmFISXh2RGVnOVJwNDByVVpETGVyalptb0gwUWpEZmxCV1RYK0JqU3ZLMm5yUGpzZzJIUC91S1VncVIwQWM5eAo0UjF5YjU2cHh3eU54TUU2NmFTVWNVQ3F1WTloY1Q3eWxWNjc3REVhRHpLTG1abnpMcWdWZU5PaUtzQTMvTi9hCnI2UW56VjNabEtJbCs5aWZwNTVPaTVLMXFyWFkyeVlPL1V2SXBXZjAxcFNFUERHN0hXSllnaGorbXpDRFVkM24KdldBeHBjUXlYRGlybS8wSkRZTWtuYzhjK2Z4QmxQR3ZiT2cwWldOeVUwSVpqRmx3aDVwUnIrMnRkT3lhRkZrNApWNytmMkpRWXdKZWgzWDdQL0N6WldKMlQvbnVzaVZXd0Y2K0hueDQ2ZHVGTzhXSWJZTnJUU1hTQnFEV04vdWpZCjBwYUhwS1poUTJOVnV1M0t3a2JaTDUzRjBRM09EVjcydGtiTHJyajZvOUNGd3JGUFluV0owSWtsemN0d1VtQ24KNjd5TzlSVjVzcC83YlNxTkhYNFRuNmc9Ci0tLS0tRU5EIENFUlRJRklDQVRFEXAMPLE=
```

Output:

```
{
    "WrappedKey": {
        "KeyMaterial": "308205A106092A864886F70D010702A08205923082058E020101310D300B06096086480165030402013082031F06092A864886F70D010703A08203100482030C020100318201F4308201F002010030819F308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3037353535363935333735303112301006035504070C0941726C696E67746F6E021100C61EFF5D6A4FE93F5BD40FD8FF0852E8304506092A864886F70D0101073038300D06096086480165030402010500301806092A864886F70D010108300B0609608648016503040201300D06092A864886F70D0101090400048201008B09AFE9DFF1EA4E97F8651B6B3B51A3BFF68B0365F3956AD34A64B015185BB3FFB3DC7D5812B0D21D58436EAEC131F8110389E2A9F22DA146805A4D818BDCD6AA0387284188CEF5691565A849659C117AAD0042DF5D2C290386710B58A8C63A298C99280EB75861B793302F78299DE64853433227F23DBB383A605DA23620546DCA92B2D3CD8B486339D303844D807C2D6AF17CF1ABF191F63ACFF0E0F8A91AA5B22C1A0D9EE663854D1D76CEE37FE3A0113C8577B57F173ECD69FA752A8A1AEF49AB2A62D39F091FF9AA0FD4CB695D084637DBA7EF7DA2E657BBBF0C5FCC355DB37866B7BBD5AE065DC0FD399A8E0FC19C10943D5059507DC822DED6AFA67A3082010D06092A864886F70D0107013081FF06082A864886F70D030704085050B8007C2CE5608081E8DC683EECE2BF1FC1D209D5F6642E01E58DC76FF7926B576CB6884B6723C63DDE91D8E6C75DFC4E94F1CDDA8A3E863BE8A7E1DFCD2115E251675F73388D022A28247ED66D7892AA57800750A5F84313ACC3616449A703D7DFC770F50C816F224FB038E675FB1751916699FD00585C1B2EA19FECEE696611FA65B4E8516210D884E351201A888A47D874B1ACDDF4AE7F6F59D0780A5BE3E788DD6FB4E6AC1B9D966443881E9998A625CFB10A35D943B21A3ABB902CF68AD6F7FE7B0C18FF05B94C10E254017203541AFF71E440A42C8B915A84B341F923EF657280DB7B19F769E29725FF7E5999859C318202553082025102010130819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3037353535363935333735303112301006035504070C0941726C696E67746F6E02106BD452CE836B7D2A717B69DB8FAF3679300B0609608648016503040201A0818A301806092A864886F70D010903310B06092A864886F70D010703301C06092A864886F70D010905310F170D3233303631333139303234305A301F06092A864886F70D0107013112041044303131324B30544230304530303030302F06092A864886F70D010904312204209AD3A76A89E2F58433DF669174A6F4D4B6B3D60A8A7341712CB666CA6AE4125E300D06092A864886F70D0101010500048201009BA48B242A227AD05243DBB99ACF6249D626CEF086DAFD8B064592EFF1205CFE6713D5FC373D8CD53AF9A88292E143A4B9C1887792E8E7F6310503B1FD8F0F89F735DFF11CC55114859B902841E4D163D64E19DFAE0151B93590C8D770E47E939DF08242897F9319DC6AB272C26DE2ACC539BF055CE528B139D61B45542FF35D2ABDE34EEF5BE19D1C48679187B455864EDD3D976CDC80070A6A6635DF5A00AF08CBBF309C4D59A4710A531A719562D390394A736E9F2DED502B2F766BA56727DFB0C6A92FD4D2BABC69BDDBD6B17EB376FA9ADD83C2974292447E63F26D168E66A4558ED97E417BDE97837188DB4F414A2219BAC50A8D726CD54C3C1EXAMPLE",
        "WrappedKeyMaterialFormat": "TR34_KEY_BLOCK"
    }
}
```

For more information, see [Export keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html) in the *AWS Payment Cryptography User Guide*.

## Output

WrappedKey -> (structure)

The key material under export as a TR-34 WrappedKeyBlock or a TR-31 WrappedKeyBlock. or a RSA WrappedKeyCryptogram.

WrappingKeyArn -> (string)

The `KeyARN` of the wrapped key.

WrappedKeyMaterialFormat -> (string)

The key block format of a wrapped key.

KeyMaterial -> (string)

Parameter information for generating a wrapped key using TR-31 or TR-34 skey exchange method.

KeyCheckValue -> (string)

The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.

KeyCheckValueAlgorithm -> (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.