# import-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/import-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/import-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html#cli-aws-payment-cryptography) ]

# import-key

## Description

Imports symmetric keys and public key certificates in PEM format (base64 encoded) into Amazon Web Services Payment Cryptography.

Amazon Web Services Payment Cryptography simplifies key exchange by replacing the existing paper-based approach with a modern electronic approach. With `ImportKey` you can import symmetric keys using either symmetric and asymmetric key exchange mechanisms.

For symmetric key exchange, Amazon Web Services Payment Cryptography uses the ANSI X9 TR-31 norm in accordance with PCI PIN guidelines. And for asymmetric key exchange, Amazon Web Services Payment Cryptography supports ANSI X9 TR-34 norm and RSA wrap and unwrap key exchange mechanisms. Asymmetric key exchange methods are typically used to establish bi-directional trust between the two parties exhanging keys and are used for initial key exchange such as Key Encryption Key (KEK) or Zone Master Key (ZMK). After which you can import working keys using symmetric method to perform various cryptographic operations within Amazon Web Services Payment Cryptography.

The TR-34 norm is intended for exchanging 3DES keys only and keys are imported in a WrappedKeyBlock format. Key attributes (such as KeyUsage, KeyAlgorithm, KeyModesOfUse, Exportability) are contained within the key block. With RSA wrap and unwrap, you can exchange both 3DES and AES-128 keys. The keys are imported in a WrappedKeyCryptogram format and you will need to specify the key attributes during import.

You can also import a *root public key certificate* , used to sign other public key certificates, or a *trusted public key certificate* under an already established root public key certificate.

**To import a public root key certificate**

Using this operation, you can import the public component (in PEM cerificate format) of your private root key. You can use the imported public root key certificate for digital signatures, for example signing wrapping key or signing key in TR-34, within your Amazon Web Services Payment Cryptography account.

Set the following parameters:

- `KeyMaterial` : `RootCertificatePublicKey`
- `KeyClass` : `PUBLIC_KEY`
- `KeyModesOfUse` : `Verify`
- `KeyUsage` : `TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE`
- `PublicKeyCertificate` : The public key certificate in PEM format (base64 encoded) of the private root key under import.

**To import a trusted public key certificate**

The root public key certificate must be in place and operational before you import a trusted public key certificate. Set the following parameters:

- `KeyMaterial` : `TrustedCertificatePublicKey`
- `CertificateAuthorityPublicKeyIdentifier` : `KeyArn` of the `RootCertificatePublicKey` .
- `KeyModesOfUse` and `KeyUsage` : Corresponding to the cryptographic operations such as wrap, sign, or encrypt that you will allow the trusted public key certificate to perform.
- `PublicKeyCertificate` : The trusted public key certificate in PEM format (base64 encoded) under import.

**To import initial keys (KEK or ZMK or similar) using TR-34**

Using this operation, you can import initial key using TR-34 asymmetric key exchange. In TR-34 terminology, the sending party of the key is called Key Distribution Host (KDH) and the receiving party of the key is called Key Receiving Device (KRD). During the key import process, KDH is the user who initiates the key import and KRD is Amazon Web Services Payment Cryptography who receives the key.

To initiate TR-34 key import, the KDH must obtain an import token by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) . This operation generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate (also known as KRD wrapping certificate) and the root certificate chain. The KDH must trust and install the KRD wrapping certificate on its HSM and use it to encrypt (wrap) the KDH key during TR-34 WrappedKeyBlock generation. The import token and associated KRD wrapping certificate expires after 7 days.

Next the KDH generates a key pair for the purpose of signing the encrypted KDH key and provides the public certificate of the signing key to Amazon Web Services Payment Cryptography. The KDH will also need to import the root certificate chain of the KDH signing certificate by calling `ImportKey` for `RootCertificatePublicKey` . For more information on TR-34 key import, see section [Importing symmetric keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html) in the *Amazon Web Services Payment Cryptography User Guide* .

Set the following parameters:

- `KeyMaterial` : Use `Tr34KeyBlock` parameters.
- `CertificateAuthorityPublicKeyIdentifier` : The `KeyARN` of the certificate chain that signed the KDH signing key certificate.
- `ImportToken` : Obtained from KRD by calling [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) .
- `WrappedKeyBlock` : The TR-34 wrapped key material from KDH. It contains the KDH key under import, wrapped with KRD wrapping certificate and signed by KDH signing private key. This TR-34 key block is typically generated by the KDH Hardware Security Module (HSM) outside of Amazon Web Services Payment Cryptography.
- `SigningKeyCertificate` : The public key certificate in PEM format (base64 encoded) of the KDH signing key generated under the root certificate (CertificateAuthorityPublicKeyIdentifier) imported in Amazon Web Services Payment Cryptography.

**To import initial keys (KEK or ZMK or similar) using RSA Wrap and Unwrap**

Using this operation, you can import initial key using asymmetric RSA wrap and unwrap key exchange method. To initiate import, call [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html) with `KeyMaterial` set to `KEY_CRYPTOGRAM` to generate an import token. This operation also generates an encryption keypair for the purpose of key import, signs the key and returns back the wrapping key certificate in PEM format (base64 encoded) and its root certificate chain. The import token and associated KRD wrapping certificate expires after 7 days.

You must trust and install the wrapping certificate and its certificate chain on the sending HSM and use it to wrap the key under export for WrappedKeyCryptogram generation. Next call `ImportKey` with `KeyMaterial` set to `KEY_CRYPTOGRAM` and provide the `ImportToken` and `KeyAttributes` for the key under import.

**To import working keys using TR-31**

Amazon Web Services Payment Cryptography uses TR-31 symmetric key exchange norm to import working keys. A KEK must be established within Amazon Web Services Payment Cryptography by using TR-34 key import or by using [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) . To initiate a TR-31 key import, set the following parameters:

- `KeyMaterial` : Use `Tr31KeyBlock` parameters.
- `WrappedKeyBlock` : The TR-31 wrapped key material. It contains the key under import, encrypted using KEK. The TR-31 key block is typically generated by a HSM outside of Amazon Web Services Payment Cryptography.
- `WrappingKeyIdentifier` : The `KeyArn` of the KEK that Amazon Web Services Payment Cryptography uses to decrypt or unwrap the key under import.

**Cross-account use:** This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- [ExportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportKey.html)
- [GetParametersForImport](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetParametersForImport.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-2021-09-14/ImportKey)

## Synopsis

```
import-key
--key-material <value>
[--key-check-value-algorithm <value>]
[--enabled | --no-enabled]
[--tags <value>]
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

The key or public key certificate type to use during key material import, for example TR-34 or RootCertificatePublicKey.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RootCertificatePublicKey`, `TrustedCertificatePublicKey`, `Tr31KeyBlock`, `Tr34KeyBlock`, `KeyCryptogram`, `DiffieHellmanTr31KeyBlock`.

RootCertificatePublicKey -> (structure)

Parameter information for root public key certificate import.

KeyAttributes -> (structure)

The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the root public key is imported.

KeyUsage -> (string)

The cryptographic usage of an Amazon Web Services Payment Cryptography key as deï¬ned in section A.5.2 of the TR-31 spec.

KeyClass -> (string)

The type of Amazon Web Services Payment Cryptography key to create, which determines the classiï¬cation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.

KeyAlgorithm -> (string)

The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.

For symmetric keys, Amazon Web Services Payment Cryptography supports `AES` and `TDES` algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports `RSA` and `ECC_NIST` algorithms.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key.

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

PublicKeyCertificate -> (string)

Parameter information for root public key certificate import.

TrustedCertificatePublicKey -> (structure)

Parameter information for trusted public key certificate import.

KeyAttributes -> (structure)

The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after a trusted public key is imported.

KeyUsage -> (string)

The cryptographic usage of an Amazon Web Services Payment Cryptography key as deï¬ned in section A.5.2 of the TR-31 spec.

KeyClass -> (string)

The type of Amazon Web Services Payment Cryptography key to create, which determines the classiï¬cation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.

KeyAlgorithm -> (string)

The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.

For symmetric keys, Amazon Web Services Payment Cryptography supports `AES` and `TDES` algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports `RSA` and `ECC_NIST` algorithms.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key.

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

PublicKeyCertificate -> (string)

Parameter information for trusted public key certificate import.

CertificateAuthorityPublicKeyIdentifier -> (string)

The `KeyARN` of the root public key certificate or certificate chain that signs the trusted public key certificate import.

Tr31KeyBlock -> (structure)

Parameter information for key material import using symmetric TR-31 key exchange method.

WrappingKeyIdentifier -> (string)

The `KeyARN` of the key that will decrypt or unwrap a TR-31 key block during import.

WrappedKeyBlock -> (string)

The TR-31 wrapped key block to import.

Tr34KeyBlock -> (structure)

Parameter information for key material import using the asymmetric TR-34 key exchange method.

CertificateAuthorityPublicKeyIdentifier -> (string)

The `KeyARN` of the certificate chain that signs the signing key certificate during TR-34 key import.

SigningKeyCertificate -> (string)

The public key component in PEM certificate format of the private key that signs the KDH TR-34 WrappedKeyBlock.

ImportToken -> (string)

The import token that initiates key import using the asymmetric TR-34 key exchange method into Amazon Web Services Payment Cryptography. It expires after 7 days. You can use the same import token to import multiple keys to the same service account.

WrappedKeyBlock -> (string)

The TR-34 wrapped key block to import.

KeyBlockFormat -> (string)

The key block format to use during key import. The only value allowed is `X9_TR34_2012` .

RandomNonce -> (string)

A random number value that is unique to the TR-34 key block generated using 2 pass. The operation will fail, if a random nonce value is not provided for a TR-34 key block generated using 2 pass.

KeyCryptogram -> (structure)

Parameter information for key material import using asymmetric RSA wrap and unwrap key exchange method.

KeyAttributes -> (structure)

The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.

KeyUsage -> (string)

The cryptographic usage of an Amazon Web Services Payment Cryptography key as deï¬ned in section A.5.2 of the TR-31 spec.

KeyClass -> (string)

The type of Amazon Web Services Payment Cryptography key to create, which determines the classiï¬cation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.

KeyAlgorithm -> (string)

The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.

For symmetric keys, Amazon Web Services Payment Cryptography supports `AES` and `TDES` algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports `RSA` and `ECC_NIST` algorithms.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key.

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

Exportable -> (boolean)

Specifies whether the key is exportable from the service.

WrappedKeyCryptogram -> (string)

The RSA wrapped key cryptogram under import.

ImportToken -> (string)

The import token that initiates key import using the asymmetric RSA wrap and unwrap key exchange method into AWS Payment Cryptography. It expires after 7 days. You can use the same import token to import multiple keys to the same service account.

WrappingSpec -> (string)

The wrapping spec for the wrapped key cryptogram.

DiffieHellmanTr31KeyBlock -> (structure)

Parameter information for key material import using the asymmetric ECDH key exchange method.

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

WrappedKeyBlock -> (string)

The ECDH wrapped key block to import.

JSON Syntax:

```
{
  "RootCertificatePublicKey": {
    "KeyAttributes": {
      "KeyUsage": "TR31_B0_BASE_DERIVATION_KEY"|"TR31_C0_CARD_VERIFICATION_KEY"|"TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY"|"TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION"|"TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS"|"TR31_E1_EMV_MKEY_CONFIDENTIALITY"|"TR31_E2_EMV_MKEY_INTEGRITY"|"TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS"|"TR31_E5_EMV_MKEY_CARD_PERSONALIZATION"|"TR31_E6_EMV_MKEY_OTHER"|"TR31_K0_KEY_ENCRYPTION_KEY"|"TR31_K1_KEY_BLOCK_PROTECTION_KEY"|"TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT"|"TR31_M3_ISO_9797_3_MAC_KEY"|"TR31_M1_ISO_9797_1_MAC_KEY"|"TR31_M6_ISO_9797_5_CMAC_KEY"|"TR31_M7_HMAC_KEY"|"TR31_P0_PIN_ENCRYPTION_KEY"|"TR31_P1_PIN_GENERATION_KEY"|"TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"|"TR31_V1_IBM3624_PIN_VERIFICATION_KEY"|"TR31_V2_VISA_PIN_VERIFICATION_KEY"|"TR31_K2_TR34_ASYMMETRIC_KEY",
      "KeyClass": "SYMMETRIC_KEY"|"ASYMMETRIC_KEY_PAIR"|"PRIVATE_KEY"|"PUBLIC_KEY",
      "KeyAlgorithm": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"|"RSA_2048"|"RSA_3072"|"RSA_4096"|"ECC_NIST_P256"|"ECC_NIST_P384"|"ECC_NIST_P521",
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
      }
    },
    "PublicKeyCertificate": "string"
  },
  "TrustedCertificatePublicKey": {
    "KeyAttributes": {
      "KeyUsage": "TR31_B0_BASE_DERIVATION_KEY"|"TR31_C0_CARD_VERIFICATION_KEY"|"TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY"|"TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION"|"TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS"|"TR31_E1_EMV_MKEY_CONFIDENTIALITY"|"TR31_E2_EMV_MKEY_INTEGRITY"|"TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS"|"TR31_E5_EMV_MKEY_CARD_PERSONALIZATION"|"TR31_E6_EMV_MKEY_OTHER"|"TR31_K0_KEY_ENCRYPTION_KEY"|"TR31_K1_KEY_BLOCK_PROTECTION_KEY"|"TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT"|"TR31_M3_ISO_9797_3_MAC_KEY"|"TR31_M1_ISO_9797_1_MAC_KEY"|"TR31_M6_ISO_9797_5_CMAC_KEY"|"TR31_M7_HMAC_KEY"|"TR31_P0_PIN_ENCRYPTION_KEY"|"TR31_P1_PIN_GENERATION_KEY"|"TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"|"TR31_V1_IBM3624_PIN_VERIFICATION_KEY"|"TR31_V2_VISA_PIN_VERIFICATION_KEY"|"TR31_K2_TR34_ASYMMETRIC_KEY",
      "KeyClass": "SYMMETRIC_KEY"|"ASYMMETRIC_KEY_PAIR"|"PRIVATE_KEY"|"PUBLIC_KEY",
      "KeyAlgorithm": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"|"RSA_2048"|"RSA_3072"|"RSA_4096"|"ECC_NIST_P256"|"ECC_NIST_P384"|"ECC_NIST_P521",
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
      }
    },
    "PublicKeyCertificate": "string",
    "CertificateAuthorityPublicKeyIdentifier": "string"
  },
  "Tr31KeyBlock": {
    "WrappingKeyIdentifier": "string",
    "WrappedKeyBlock": "string"
  },
  "Tr34KeyBlock": {
    "CertificateAuthorityPublicKeyIdentifier": "string",
    "SigningKeyCertificate": "string",
    "ImportToken": "string",
    "WrappedKeyBlock": "string",
    "KeyBlockFormat": "X9_TR34_2012",
    "RandomNonce": "string"
  },
  "KeyCryptogram": {
    "KeyAttributes": {
      "KeyUsage": "TR31_B0_BASE_DERIVATION_KEY"|"TR31_C0_CARD_VERIFICATION_KEY"|"TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY"|"TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION"|"TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS"|"TR31_E1_EMV_MKEY_CONFIDENTIALITY"|"TR31_E2_EMV_MKEY_INTEGRITY"|"TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS"|"TR31_E5_EMV_MKEY_CARD_PERSONALIZATION"|"TR31_E6_EMV_MKEY_OTHER"|"TR31_K0_KEY_ENCRYPTION_KEY"|"TR31_K1_KEY_BLOCK_PROTECTION_KEY"|"TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT"|"TR31_M3_ISO_9797_3_MAC_KEY"|"TR31_M1_ISO_9797_1_MAC_KEY"|"TR31_M6_ISO_9797_5_CMAC_KEY"|"TR31_M7_HMAC_KEY"|"TR31_P0_PIN_ENCRYPTION_KEY"|"TR31_P1_PIN_GENERATION_KEY"|"TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"|"TR31_V1_IBM3624_PIN_VERIFICATION_KEY"|"TR31_V2_VISA_PIN_VERIFICATION_KEY"|"TR31_K2_TR34_ASYMMETRIC_KEY",
      "KeyClass": "SYMMETRIC_KEY"|"ASYMMETRIC_KEY_PAIR"|"PRIVATE_KEY"|"PUBLIC_KEY",
      "KeyAlgorithm": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"|"RSA_2048"|"RSA_3072"|"RSA_4096"|"ECC_NIST_P256"|"ECC_NIST_P384"|"ECC_NIST_P521",
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
      }
    },
    "Exportable": true|false,
    "WrappedKeyCryptogram": "string",
    "ImportToken": "string",
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
    "WrappedKeyBlock": "string"
  }
}
```

`--key-check-value-algorithm` (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

Possible values:

- `CMAC`
- `ANSI_X9_24`

`--enabled` | `--no-enabled` (boolean)

Specifies whether import key is enabled.

`--tags` (list)

Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is imported. To tag an existing Amazon Web Services Payment Cryptography key, use the [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) operation.

Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You canât have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, Amazon Web Services Payment Cryptography replaces the current tag value with the specified one.

### Warning

Donât include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

### Note

Tagging or untagging an Amazon Web Services Payment Cryptography key can allow or deny permission to the key.

(structure)

A structure that contains information about a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

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

**To import a TR-34 key**

The following `import-key` example imports a TR-34 key.

```
aws payment-cryptography import-key \
        --key-material='{ "Tr34KeyBlock": {" \
            CertificateAuthorityPublicKeyIdentifier": "arn:aws:payment-cryptography:us-west-2:123456789012:key/rmm5wn2q564njnjm", \
            "ImportToken": "import-token-5ott6ho5nts7bbcg", \
            "KeyBlockFormat": "X9_TR34_2012", \
            "SigningKeyCertificate": file://signing-key-certificate.pem, \
            "WrappedKeyBlock": file://wrapped-key-block.pem }}'
```

Contents of `signing-key-certificate.pem`:

```
LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUV2RENDQXFTZ0F3SUJBZ0lRYWVCK25IbE1WZU1PR1ZiNjU1Q2JzREFOQmdrcWhraUc5dzBCQVEwRkFEQ0IKaVRFTE1Ba0dBMVVFQmhNQ1ZWTXhHVEFYQmdOVkJBb01FRUZYVXlCRGNubHdkRzluY21Gd2FIa3hJVEFmQmdOVgpCQXNNR0VGWFV5QlFZWGx0Wlc1MElFTnllWEIwYjJkeVlYQm9lVEVSTUE4R0ExVUVDQXdJVm1seVoybHVhV0V4CkZUQVRCZ05WQkFNTUREVXlPVEF5TnpRMU5UUTVOVEVTTUJBR0ExVUVCd3dKUVhKc2FXNW5kRzl1TUI0WERUSXoKTURZd09USXlNVEkxTUZvWERUSXpNRFl4TmpJek1USTFNRm93TERFVk1CTUdBMVVFQXd3TU5USTVNREkzTkRVMQpORGsxTVJNd0VRWURWUVFGRXdvek1EVTRNVGszTkRjNE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBCk1JSUJDZ0tDQVFFQXdMc0dGb0pqOTVJY0UxL1p1OGZxak40SDVHTFJHVGZQSkFyWWJLbjA4WXVrQTE0SjRBSHEKWGR6ZlY5MjcvVTJZTWN2S3FsNlk5SVQwejZhTVBGbDVYemZWNU1YVW5YMlJxYTladU1ndDhGSDJJYWxsMEQ3bgo0V0RjUkg3TERQdEhXZTRaVmh3aExRVEFQa1I2dUxTWC84UDhSN2lrSWpkVkI4SytjVitnbHh0clB1Vkh5TzNxCjhXRUl3a1lYVTFDVjJybHptNklzWjcycjhPcXJWcHNiZEhERENBelJ2YUtPN3hMNU1RUGVFMFcvdkxmRGdrYmoKb2h4VHl6Z3dRSlJFK21tUXdCRmlIeXdaY2F5Y1FZdXdzTktoK0xPWXJpN0ZGM2lRRTJlYlY5Mm4zZER5NDRtcQpUSjFHUWJENndFM3ZHS0xnYXNqMVl0WVNSTk9xNld1UTV3SURBUUFCbzN3d2VqQUpCZ05WSFJNRUFqQUFNQjhHCkExVWRJd1FZTUJhQUZHMVBsWElaUGdETVU0WjVwRTc3dE8xYmV2eDVNQjBHQTFVZERnUVdCQlFwanByQXFoZGMKVmF2dElTRnBBNkswVzJMcmJUQU9CZ05WSFE4QkFmOEVCQU1DQmFBd0hRWURWUjBsQkJZd0ZBWUlLd1lCQlFVSApBd0VHQ0NzR0FRVUZCd01DTUEwR0NTcUdTSWIzRFFFQkRRVUFBNElDQVFCOXVxcFVadU1oK1kzQXhXSklNUkx5Cmlob2gvR0xIanh1aVhxK1IvdFRxbTBNYTA3R2dvbGxhRkdIZzZMei9ELy9ZRDB2UHdYc1dVOE5qY0Vib095aGcKc0hmay9hVGxjRnovZm51MVlkRUpvYUpFdW15bDkwSTBMNyswUmJNYXJScWU0bC9yQlQ4YTM3R0JyQ0x0ZUlyRgorcnp1cmovU1BDM1FiUWkvOVBzWmlieTFKMlFxTzVVRUJncEYreklaVk84dzgwMzVEK1YrUXhsY2RaUGVLS2JnCmI5WHNSeHF3cUZIVUVRM2tybXdVZUZveERlbm91QmxKMVFzOTVXUHBpVk9zYUFvbkJkYUtEbFBaRTlqdG1zZkwKMER3b1lRRy92bHdWN0pIVnNNd0dleml2VGJXaWFNdmZTTkxIMmVZMG9rblhFcHlHcmlWMjczSVFqVU1QTXBMNgpjODh3OUYzcTJnY0x6Nk0ycEFHUTZ0SVBrZ2c3aUZjbk9haGp4Ty9ORFZrS0xxbXZ0eFFlcUk2VDRveWRuWkVWCkdOMjBISStZcFVud09Eem1GL1k5TXZQQXFtdGJka2dZZGRJWExtbU9ORlF1dm4wenp0Tm01NzNTN0NSYWxCNTgKeFhyNm1iak1MQU1tcmZGQmNrU0NYaUZ6Y3gvNHJTRGJtbU9INWM0dGxiNEM3SzF5QU96NWo3OHhWOWNQOTM3SQpwczcrZUFZRkFpYTdzZGpuS3hNUDN4ZVVTM0tNS2FGMzg2TGRYbkRwdTFyczhVRWhPeDhqakt6RWplWU9qV3hLClo5Mjd1Yzd0b2kwZlcvT2tzT3NnWVlybmttSEhyd3p0NXRBc2llcjFyWXFGK2lYa1Y4TzRxSzI0bHc4cXFPanUKS3htVHMzY0NlTmdGNUZhVmhCV1Zjdz09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0=
```

Contents of `wrapped-key-block.pem`:

```
3082059806092A864886F70D010702A082058930820585020101310D300B06096086480165030402013082031606092A864886F70D010703A082030704820303020100318201F3308201EF02010030819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3532393032373435353439353112301006035504070C0941726C696E67746F6E021026C5E52507841B72C59D9F0065548DC1304506092A864886F70D0101073038300D06096086480165030402010500301806092A864886F70D010108300B0609608648016503040201300D06092A864886F70D01010904000482010013D3C2E9405CA45A947BA6EA098DD5A83A7E6CFF4E140B141634EBFF9E0F78057B5C22013574BA8C8D8D64B43C391E1D9CDF081B33D15CDE3AB2DB21CAE7380E64B0A09A8C45B8A0F87659638E6E30D4351E9B941EDD384183DA169ADDF71FC64E06487F8750B74B2CD3AB4F8534C024AE04BD7C070CB685A250EB2A8C1EEDEBFA387935466D152E063D3EBEDD6231216EEE5145983C74D755C050D191E6E41DC2BDB09E78CDA203C2767270E3E56C6E24EB1090904462743B054098DE278A18C71577CAE1EC13CF776055224F299DBF1BC96C11F339DEE1A2CD130A275959820FBE5C34C0CB21DB6404F868B348D5A6F8ED8E5DC5BC681F6115BA278879FF8F3082010506092A864886F70D0107013081F706082A864886F70D0307040857F8BFE99B4493AD8081E05DEE59D9E60520DB8A15869BB840F1CC908DAE6CC6F6BE79DDF72DD8EA84F881D7DFB4A186CDC622B29E3F97AEB7C00872D1BB47FE235D9204F80A4D3EF502309ECD967F8F70A2F741738ACE7B7CA0AA2EBB0DACD3126F7831F79AF6DC3C74CEBF7D0947301245F42C59508FBC0318C03F02E37EDF014C4D0170ACC4E992EC7E9B85D95BF87F75FD2E0B938E2D8E807872DE4017F8530D59A48C9F68AF5BEC1B2115D7555C248F980DF28C69619E508317F0C20461AE26CD0D55896FEE71E1EA89F7F9B5DC047F9BD063210E1F09D9566EF2AF6472AD44A8ACC0180AC1995CDE318202553082025102010130819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3532393032373435353439353112301006035504070C0941726C696E67746F6E021069E07E9C794C55E30E1956FAE7909BB0300B0609608648016503040201A0818A301806092A864886F70D010903310B06092A864886F70D010703301C06092A864886F70D010905310F170D3233303630393233333934365A301F06092A864886F70D0107013112041044303131324330544330304530303030302F06092A864886F70D01090431220420D6413C502DC4552B495B9A8449F9A3BF9E6DCB31AD56A1D158DB482BDF06EEAD300D06092A864886F70D010101050004820100313BA7BCDFE6C55F3544A8E7D9973A346DDAD17CC5C506DE72B8B7E490891702E753C445FED78D5477C5E5A2BF63378B2F12CE6C22C1A543BCC41FA978568F65C0171DBF3E438E70FD68DAB52BA1DEB294C4ED92CD6EAA684B4352AF6C53924048931595FC7F1FF642E82B12DBD8B8578DA200DC0CCE2FA075897CDA6D5257C78DC2B515015CC414E78B49075AFF333C7CEAFF81F5EEC44C5C9F6BD32898E6983A7CEA40DD5C0CF9CD51DB3E712ED1C755E0A9DA38286872B46D7119088A76728DC08AECB0F624B34E15349E5B2334900E57885A6461AC6E74B35A3FFF5C010ACE5F15DE9D867A5160D30217997E7DE6319A74F5D55D44A934908A3BC1602D22
```

Output:

```
{
    "Key": {
        "CreateTimestamp": "2023-06-09T16:56:27.621000-07:00",
        "Enabled": true,
        "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/bzmvgyxdg3sktwxd",
        "KeyAttributes": {
            "KeyAlgorithm": "TDES_2KEY",
            "KeyClass": "SYMMETRIC_KEY",
            "KeyModesOfUse": {
                "Decrypt": false,
                "DeriveKey": false,
                "Encrypt": false,
                "Generate": true,
                "NoRestrictions": false,
                "Sign": false,
                "Unwrap": false,
                "Verify": true,
                "Wrap": false
            },
            "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY"
        },
        "KeyCheckValue": "D9B20E",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "EXTERNAL",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "2023-06-09T16:56:27.621000-07:00"
    }
}
```

For more information, see [Import keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html) in the *AWS Payment Cryptography User Guide*.

## Output

Key -> (structure)

The `KeyARN` of the key material imported within Amazon Web Services Payment Cryptography.

KeyArn -> (string)

The Amazon Resource Name (ARN) of the key.

KeyAttributes -> (structure)

The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.

KeyUsage -> (string)

The cryptographic usage of an Amazon Web Services Payment Cryptography key as deï¬ned in section A.5.2 of the TR-31 spec.

KeyClass -> (string)

The type of Amazon Web Services Payment Cryptography key to create, which determines the classiï¬cation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.

KeyAlgorithm -> (string)

The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.

For symmetric keys, Amazon Web Services Payment Cryptography supports `AES` and `TDES` algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports `RSA` and `ECC_NIST` algorithms.

KeyModesOfUse -> (structure)

The list of cryptographic operations that you can perform using the key.

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

KeyCheckValue -> (string)

The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.

KeyCheckValueAlgorithm -> (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

Enabled -> (boolean)

Specifies whether the key is enabled.

Exportable -> (boolean)

Specifies whether the key is exportable. This data is immutable after the key is created.

KeyState -> (string)

The state of key that is being created or deleted.

KeyOrigin -> (string)

The source of the key material. For keys created within Amazon Web Services Payment Cryptography, the value is `AWS_PAYMENT_CRYPTOGRAPHY` . For keys imported into Amazon Web Services Payment Cryptography, the value is `EXTERNAL` .

CreateTimestamp -> (timestamp)

The date and time when the key was created.

UsageStartTimestamp -> (timestamp)

The date and time after which Amazon Web Services Payment Cryptography will start using the key material for cryptographic operations.

UsageStopTimestamp -> (timestamp)

The date and time after which Amazon Web Services Payment Cryptography will stop using the key material for cryptographic operations.

DeletePendingTimestamp -> (timestamp)

The date and time after which Amazon Web Services Payment Cryptography will delete the key. This value is present only when `KeyState` is `DELETE_PENDING` and the key is scheduled for deletion.

DeleteTimestamp -> (timestamp)

The date and time after which Amazon Web Services Payment Cryptography will delete the key. This value is present only when when the `KeyState` is `DELETE_COMPLETE` and the Amazon Web Services Payment Cryptography key is deleted.

DeriveKeyUsage -> (string)

The cryptographic usage of an ECDH derived key as deï¬ned in section A.5.2 of the TR-31 spec.