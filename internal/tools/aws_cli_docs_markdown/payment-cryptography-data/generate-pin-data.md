# generate-pin-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-pin-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-pin-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# generate-pin-data

## Description

Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN Block, and PIN Offset during new card issuance or reissuance. For more information, see [Generate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html) in the *Amazon Web Services Payment Cryptography User Guide* .

PIN data is never transmitted in clear to or from Amazon Web Services Payment Cryptography. This operation generates PIN, PVV, or PIN Offset and then encrypts it using Pin Encryption Key (PEK) to create an `EncryptedPinBlock` for transmission from Amazon Web Services Payment Cryptography. This operation uses a separate Pin Verification Key (PVK) for VISA PVV generation.

Using ECDH key exchange, you can receive cardholder selectable PINs into Amazon Web Services Payment Cryptography. The ECDH derived key protects the incoming PIN block. You can also use it for reveal PIN, wherein the generated PIN block is protected by the ECDH derived key before transmission from Amazon Web Services Payment Cryptography. For more information on establishing ECDH derived keys, see the [Generating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html) in the *Amazon Web Services Payment Cryptography User Guide* .

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- GenerateCardValidationData
- TranslatePinData
- VerifyPinData

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/GeneratePinData)

## Synopsis

```
generate-pin-data
--generation-key-identifier <value>
--encryption-key-identifier <value>
--generation-attributes <value>
[--pin-data-length <value>]
--primary-account-number <value>
--pin-block-format <value>
[--encryption-wrapped-key <value>]
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

`--generation-key-identifier` (string)

The `keyARN` of the PEK that Amazon Web Services Payment Cryptography uses for pin data generation.

`--encryption-key-identifier` (string)

The `keyARN` of the PEK that Amazon Web Services Payment Cryptography uses to encrypt the PIN Block. For ECDH, it is the `keyARN` of the asymmetric ECC key.

`--generation-attributes` (tagged union structure)

The attributes and values to use for PIN, PVV, or PIN Offset generation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `VisaPin`, `VisaPinVerificationValue`, `Ibm3624PinOffset`, `Ibm3624NaturalPin`, `Ibm3624RandomPin`, `Ibm3624PinFromOffset`.

VisaPin -> (structure)

Parameters that are required to generate or verify Visa PIN.

PinVerificationKeyIndex -> (integer)

The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).

VisaPinVerificationValue -> (structure)

Parameters that are required to generate or verify Visa PIN Verification Value (PVV).

EncryptedPinBlock -> (string)

The encrypted PIN block data to verify.

PinVerificationKeyIndex -> (integer)

The value for PIN verification index. It is used in the Visa PIN algorithm to calculate the PVV (PIN Verification Value).

Ibm3624PinOffset -> (structure)

Parameters that are required to generate or verify Ibm3624 PIN offset PIN.

EncryptedPinBlock -> (string)

The encrypted PIN block data. According to ISO 9564 standard, a PIN Block is an encoded representation of a payment card Personal Account Number (PAN) and the cardholder Personal Identification Number (PIN).

DecimalizationTable -> (string)

The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.

PinValidationDataPadCharacter -> (string)

The padding character for validation data.

PinValidationData -> (string)

The unique data for cardholder identification.

Ibm3624NaturalPin -> (structure)

Parameters that are required to generate or verify Ibm3624 natural PIN.

DecimalizationTable -> (string)

The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.

PinValidationDataPadCharacter -> (string)

The padding character for validation data.

PinValidationData -> (string)

The unique data for cardholder identification.

Ibm3624RandomPin -> (structure)

Parameters that are required to generate or verify Ibm3624 random PIN.

DecimalizationTable -> (string)

The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.

PinValidationDataPadCharacter -> (string)

The padding character for validation data.

PinValidationData -> (string)

The unique data for cardholder identification.

Ibm3624PinFromOffset -> (structure)

Parameters that are required to generate or verify Ibm3624 PIN from offset PIN.

DecimalizationTable -> (string)

The decimalization table to use for IBM 3624 PIN algorithm. The table is used to convert the algorithm intermediate result from hexadecimal characters to decimal.

PinValidationDataPadCharacter -> (string)

The padding character for validation data.

PinValidationData -> (string)

The unique data for cardholder identification.

PinOffset -> (string)

The PIN offset value.

Shorthand Syntax:

```
VisaPin={PinVerificationKeyIndex=integer},VisaPinVerificationValue={EncryptedPinBlock=string,PinVerificationKeyIndex=integer},Ibm3624PinOffset={EncryptedPinBlock=string,DecimalizationTable=string,PinValidationDataPadCharacter=string,PinValidationData=string},Ibm3624NaturalPin={DecimalizationTable=string,PinValidationDataPadCharacter=string,PinValidationData=string},Ibm3624RandomPin={DecimalizationTable=string,PinValidationDataPadCharacter=string,PinValidationData=string},Ibm3624PinFromOffset={DecimalizationTable=string,PinValidationDataPadCharacter=string,PinValidationData=string,PinOffset=string}
```

JSON Syntax:

```
{
  "VisaPin": {
    "PinVerificationKeyIndex": integer
  },
  "VisaPinVerificationValue": {
    "EncryptedPinBlock": "string",
    "PinVerificationKeyIndex": integer
  },
  "Ibm3624PinOffset": {
    "EncryptedPinBlock": "string",
    "DecimalizationTable": "string",
    "PinValidationDataPadCharacter": "string",
    "PinValidationData": "string"
  },
  "Ibm3624NaturalPin": {
    "DecimalizationTable": "string",
    "PinValidationDataPadCharacter": "string",
    "PinValidationData": "string"
  },
  "Ibm3624RandomPin": {
    "DecimalizationTable": "string",
    "PinValidationDataPadCharacter": "string",
    "PinValidationData": "string"
  },
  "Ibm3624PinFromOffset": {
    "DecimalizationTable": "string",
    "PinValidationDataPadCharacter": "string",
    "PinValidationData": "string",
    "PinOffset": "string"
  }
}
```

`--pin-data-length` (integer)

The length of PIN under generation.

`--primary-account-number` (string)

The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.

`--pin-block-format` (string)

The PIN encoding format for pin data generation as specified in ISO 9564. Amazon Web Services Payment Cryptography supports `ISO_Format_0` and `ISO_Format_3` .

The `ISO_Format_0` PIN block format is equivalent to the ANSI X9.8, VISA-1, and ECI-1 PIN block formats. It is similar to a VISA-4 PIN block format. It supports a PIN from 4 to 12 digits in length.

The `ISO_Format_3` PIN block format is the same as `ISO_Format_0` except that the fill digits are random values from 10 to 15.

Possible values:

- `ISO_FORMAT_0`
- `ISO_FORMAT_3`
- `ISO_FORMAT_4`

`--encryption-wrapped-key` (structure)

Parameter information of a WrappedKeyBlock for encryption key exchange.

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

**To generate a PIN**

The following `generate-card-validation-data` example generate a new random PIN using the Visa PIN scheme.

```
aws payment-cryptography-data generate-pin-data \
    --generation-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2 \
    --encryption-key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt \
    --primary-account-number 171234567890123 \
    --pin-block-format ISO_FORMAT_0 \
    --generation-attributes VisaPin={PinVerificationKeyIndex=1}
```

Output:

```
{
    "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2",
    "GenerationKeyCheckValue": "7F2363",
    "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt",
    "EncryptionKeyCheckValue": "7CC9E2",
    "EncryptedPinBlock": "AC17DC148BDA645E",
    "PinData": {
        "VerificationValue": "5507"
    }
}
```

For more information, see [Generate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html) in the *AWS Payment Cryptography User Guide*.

## Output

GenerationKeyArn -> (string)

The `keyARN` of the pin data generation key that Amazon Web Services Payment Cryptography uses for PIN, PVV or PIN Offset generation.

GenerationKeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.

EncryptionKeyArn -> (string)

The `keyARN` of the PEK that Amazon Web Services Payment Cryptography uses for encrypted pin block generation. For ECDH, it is the `keyARN` of the asymmetric ECC key.

EncryptionKeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.

EncryptedPinBlock -> (string)

The PIN block encrypted under PEK from Amazon Web Services Payment Cryptography. The encrypted PIN block is a composite of PAN (Primary Account Number) and PIN (Personal Identification Number), generated in accordance with ISO 9564 standard.

PinData -> (tagged union structure)

The attributes and values Amazon Web Services Payment Cryptography uses for pin data generation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PinOffset`, `VerificationValue`.

PinOffset -> (string)

The PIN offset value.

VerificationValue -> (string)

The unique data to identify a cardholder. In most cases, this is the same as cardholderâs Primary Account Number (PAN). If a value is not provided, it defaults to PAN.