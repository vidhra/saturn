# create-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html#cli-aws-payment-cryptography) ]

# create-key

## Description

Creates an Amazon Web Services Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and Amazon Web Services Region. You use keys for cryptographic functions such as encryption and decryption.

In addition to the key material used in cryptographic operations, an Amazon Web Services Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.

When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: `SYMMETRIC_KEY` ), key algorithm (example: `TDES_2KEY` ), key usage (example: `TR31_P0_PIN_ENCRYPTION_KEY` ) and key modes of use (example: `Encrypt` ). For information about valid combinations of key attributes, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) in the *Amazon Web Services Payment Cryptography User Guide* . The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.

Amazon Web Services Payment Cryptography binds key attributes to keys using key blocks when you store or export them. Amazon Web Services Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html)
- [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html)
- [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-2021-09-14/CreateKey)

## Synopsis

```
create-key
--key-attributes <value>
[--key-check-value-algorithm <value>]
--exportable | --no-exportable
[--enabled | --no-enabled]
[--tags <value>]
[--derive-key-usage <value>]
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

`--key-attributes` (structure)

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

Shorthand Syntax:

```
KeyUsage=string,KeyClass=string,KeyAlgorithm=string,KeyModesOfUse={Encrypt=boolean,Decrypt=boolean,Wrap=boolean,Unwrap=boolean,Generate=boolean,Sign=boolean,Verify=boolean,DeriveKey=boolean,NoRestrictions=boolean}
```

JSON Syntax:

```
{
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
}
```

`--key-check-value-algorithm` (string)

The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.

For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

Possible values:

- `CMAC`
- `ANSI_X9_24`

`--exportable` | `--no-exportable` (boolean)

Specifies whether the key is exportable from the service.

`--enabled` | `--no-enabled` (boolean)

Specifies whether to enable the key. If the key is enabled, it is activated for use within the service. If the key is not enabled, then it is created but not activated. The default value is enabled.

`--tags` (list)

Assigns one or more tags to the Amazon Web Services Payment Cryptography key. Use this parameter to tag a key when it is created. To tag an existing Amazon Web Services Payment Cryptography key, use the [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) operation.

Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You canât have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key.

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

`--derive-key-usage` (string)

The cryptographic usage of an ECDH derived key as deï¬ned in section A.5.2 of the TR-31 spec.

Possible values:

- `TR31_B0_BASE_DERIVATION_KEY`
- `TR31_C0_CARD_VERIFICATION_KEY`
- `TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`
- `TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS`
- `TR31_E1_EMV_MKEY_CONFIDENTIALITY`
- `TR31_E2_EMV_MKEY_INTEGRITY`
- `TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS`
- `TR31_E5_EMV_MKEY_CARD_PERSONALIZATION`
- `TR31_E6_EMV_MKEY_OTHER`
- `TR31_K0_KEY_ENCRYPTION_KEY`
- `TR31_K1_KEY_BLOCK_PROTECTION_KEY`
- `TR31_M3_ISO_9797_3_MAC_KEY`
- `TR31_M1_ISO_9797_1_MAC_KEY`
- `TR31_M6_ISO_9797_5_CMAC_KEY`
- `TR31_M7_HMAC_KEY`
- `TR31_P0_PIN_ENCRYPTION_KEY`
- `TR31_P1_PIN_GENERATION_KEY`
- `TR31_V1_IBM3624_PIN_VERIFICATION_KEY`
- `TR31_V2_VISA_PIN_VERIFICATION_KEY`

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

**To create a key**

The following `create-key` example generates a 2KEY TDES key you can use to generate and verify CVV/CVV2 values.

```
aws payment-cryptography create-key \
    --exportable \
    --key-attributes KeyAlgorithm=TDES_2KEY, KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY, KeyModesOfUse={Generate=true,Verify=true}
```

Output:

```
{
    "Key": {
        "CreateTimestamp": "1686800690",
        "Enabled": true,
        "Exportable": true,
        "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h",
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
        "KeyCheckValue": "F2E50F",
        "KeyCheckValueAlgorithm": "ANSI_X9_24",
        "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
        "KeyState": "CREATE_COMPLETE",
        "UsageStartTimestamp": "1686800690"
    }
}
```

For more information, see [Generating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html) in the *AWS Payment Cryptography User Guide*.

## Output

Key -> (structure)

The key material that contains all the key attributes.

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