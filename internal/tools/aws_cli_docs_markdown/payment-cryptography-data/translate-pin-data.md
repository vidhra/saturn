# translate-pin-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/translate-pin-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/translate-pin-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# translate-pin-data

## Description

Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4. For more information, see [Translate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html) in the *Amazon Web Services Payment Cryptography User Guide* .

PIN block translation involves changing a PIN block from one encryption key to another and optionally change its format. PIN block translation occurs entirely within the HSM boundary and PIN data never enters or leaves Amazon Web Services Payment Cryptography in clear text. The encryption key transformation can be from PEK (Pin Encryption Key) to BDK (Base Derivation Key) for DUKPT or from BDK for DUKPT to PEK.

Amazon Web Services Payment Cryptography also supports use of dynamic keys and ECDH (Elliptic Curve Diffie-Hellman) based key exchange for this operation.

Dynamic keys allow you to pass a PEK as a TR-31 WrappedKeyBlock. They can be used when key material is frequently rotated, such as during every card transaction, and there is need to avoid importing short-lived keys into Amazon Web Services Payment Cryptography. To translate PIN block using dynamic keys, the `keyARN` is the Key Encryption Key (KEK) of the TR-31 wrapped PEK. The incoming wrapped key shall have a key purpose of P0 with a mode of use of B or D. For more information, see [Using Dynamic Keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-acquirers-dynamickeys.html) in the *Amazon Web Services Payment Cryptography User Guide* .

Using ECDH key exchange, you can receive cardholder selectable PINs into Amazon Web Services Payment Cryptography. The ECDH derived key protects the incoming PIN block, which is translated to a PEK encrypted PIN block for use within the service. You can also use ECDH for reveal PIN, wherein the service translates the PIN block from PEK to a ECDH derived encryption key. For more information on establishing ECDH derived keys, see the [Generating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html) in the *Amazon Web Services Payment Cryptography User Guide* .

The allowed combinations of PIN block format translations are guided by PCI. It is important to note that not all encrypted PIN block formats (example, format 1) require PAN (Primary Account Number) as input. And as such, PIN block format that requires PAN (example, formats 0,3,4) cannot be translated to a format (format 1) that does not require a PAN for generation.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

### Note

Amazon Web Services Payment Cryptography currently supports ISO PIN block 4 translation for PIN block built using legacy PAN length. That is, PAN is the right most 12 digits excluding the check digits.

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- GeneratePinData
- VerifyPinData

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/TranslatePinData)

## Synopsis

```
translate-pin-data
--incoming-key-identifier <value>
--outgoing-key-identifier <value>
--incoming-translation-attributes <value>
--outgoing-translation-attributes <value>
--encrypted-pin-block <value>
[--incoming-dukpt-attributes <value>]
[--outgoing-dukpt-attributes <value>]
[--incoming-wrapped-key <value>]
[--outgoing-wrapped-key <value>]
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

`--incoming-key-identifier` (string)

The `keyARN` of the encryption key under which incoming PIN block data is encrypted. This key type can be PEK or BDK.

For dynamic keys, it is the `keyARN` of KEK of the TR-31 wrapped PEK. For ECDH, it is the `keyARN` of the asymmetric ECC key.

`--outgoing-key-identifier` (string)

The `keyARN` of the encryption key for encrypting outgoing PIN block data. This key type can be PEK or BDK.

For ECDH, it is the `keyARN` of the asymmetric ECC key.

`--incoming-translation-attributes` (tagged union structure)

The format of the incoming PIN block data for translation within Amazon Web Services Payment Cryptography.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `IsoFormat0`, `IsoFormat1`, `IsoFormat3`, `IsoFormat4`.

IsoFormat0 -> (structure)

Parameters that are required for ISO9564 PIN format 0 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

IsoFormat1 -> (structure)

Parameters that are required for ISO9564 PIN format 1 tranlation.

IsoFormat3 -> (structure)

Parameters that are required for ISO9564 PIN format 3 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

IsoFormat4 -> (structure)

Parameters that are required for ISO9564 PIN format 4 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

Shorthand Syntax:

```
IsoFormat0={PrimaryAccountNumber=string},IsoFormat1={},IsoFormat3={PrimaryAccountNumber=string},IsoFormat4={PrimaryAccountNumber=string}
```

JSON Syntax:

```
{
  "IsoFormat0": {
    "PrimaryAccountNumber": "string"
  },
  "IsoFormat1": {

  },
  "IsoFormat3": {
    "PrimaryAccountNumber": "string"
  },
  "IsoFormat4": {
    "PrimaryAccountNumber": "string"
  }
}
```

`--outgoing-translation-attributes` (tagged union structure)

The format of the outgoing PIN block data after translation by Amazon Web Services Payment Cryptography.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `IsoFormat0`, `IsoFormat1`, `IsoFormat3`, `IsoFormat4`.

IsoFormat0 -> (structure)

Parameters that are required for ISO9564 PIN format 0 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

IsoFormat1 -> (structure)

Parameters that are required for ISO9564 PIN format 1 tranlation.

IsoFormat3 -> (structure)

Parameters that are required for ISO9564 PIN format 3 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

IsoFormat4 -> (structure)

Parameters that are required for ISO9564 PIN format 4 tranlation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

Shorthand Syntax:

```
IsoFormat0={PrimaryAccountNumber=string},IsoFormat1={},IsoFormat3={PrimaryAccountNumber=string},IsoFormat4={PrimaryAccountNumber=string}
```

JSON Syntax:

```
{
  "IsoFormat0": {
    "PrimaryAccountNumber": "string"
  },
  "IsoFormat1": {

  },
  "IsoFormat3": {
    "PrimaryAccountNumber": "string"
  },
  "IsoFormat4": {
    "PrimaryAccountNumber": "string"
  }
}
```

`--encrypted-pin-block` (string)

The encrypted PIN block data that Amazon Web Services Payment Cryptography translates.

`--incoming-dukpt-attributes` (structure)

The attributes and values to use for incoming DUKPT encryption key for PIN block translation.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

DukptKeyDerivationType -> (string)

The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY`

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be for incoming data decryption, outgoing data encryption, or both.

Shorthand Syntax:

```
KeySerialNumber=string,DukptKeyDerivationType=string,DukptKeyVariant=string
```

JSON Syntax:

```
{
  "KeySerialNumber": "string",
  "DukptKeyDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256",
  "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE"
}
```

`--outgoing-dukpt-attributes` (structure)

The attributes and values to use for outgoing DUKPT encryption key after PIN block translation.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

DukptKeyDerivationType -> (string)

The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY`

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be for incoming data decryption, outgoing data encryption, or both.

Shorthand Syntax:

```
KeySerialNumber=string,DukptKeyDerivationType=string,DukptKeyVariant=string
```

JSON Syntax:

```
{
  "KeySerialNumber": "string",
  "DukptKeyDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256",
  "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE"
}
```

`--incoming-wrapped-key` (structure)

The WrappedKeyBlock containing the encryption key under which incoming PIN block data is encrypted.

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

`--outgoing-wrapped-key` (structure)

The WrappedKeyBlock containing the encryption key for encrypting outgoing PIN block data.

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

**To translate PIN data**

The following `translate-pin-data` example translates a PIN from PEK TDES encryption using ISO 0 PIN block to an AES ISO 4 PIN Block using the DUKPT algorithm.

```
aws payment-cryptography-data translate-pin-data \
    --encrypted-pin-block "AC17DC148BDA645E" \
    --incoming-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' \
    --incoming-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --outgoing-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/4pmyquwjs3yj4vwe \
    --outgoing-translation-attributes IsoFormat4="{PrimaryAccountNumber=171234567890123}" \
    --outgoing-dukpt-attributes KeySerialNumber="FFFF9876543210E00008"
```

Output:

```
{
    "PinBlock": "1F4209C670E49F83E75CC72E81B787D9",
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt
    "KeyCheckValue": "7CC9E2"
}
```

For more information, see [Translate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html) in the *AWS Payment Cryptography User Guide*.

## Output

PinBlock -> (string)

The outgoing encrypted PIN block data after translation.

KeyArn -> (string)

The `keyARN` of the encryption key that Amazon Web Services Payment Cryptography uses to encrypt outgoing PIN block data after translation.

KeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.