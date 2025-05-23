# delete-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/index.html#cli-aws-payment-cryptography) ]

# delete-key

## Description

Deletes the key material and metadata associated with Amazon Web Services Payment Cryptography key.

Key deletion is irreversible. After a key is deleted, you canât perform cryptographic operations using the key. For example, you canât decrypt data that was encrypted by a deleted Amazon Web Services Payment Cryptography key, and the data may become unrecoverable. Because key deletion is destructive, Amazon Web Services Payment Cryptography has a safety mechanism to prevent accidental deletion of a key. When you call this operation, Amazon Web Services Payment Cryptography disables the specified key but doesnât delete it until after a waiting period set using `DeleteKeyInDays` . The default waiting period is 7 days. During the waiting period, the `KeyState` is `DELETE_PENDING` . After the key is deleted, the `KeyState` is `DELETE_COMPLETE` .

You should delete a key only when you are sure that you donât need to use it anymore and no other parties are utilizing this key. If you arenât sure, consider deactivating it instead by calling [StopKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html) .

**Cross-account use:** This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- [RestoreKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_RestoreKey.html)
- [StartKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StartKeyUsage.html)
- [StopKeyUsage](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_StopKeyUsage.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-2021-09-14/DeleteKey)

## Synopsis

```
delete-key
--key-identifier <value>
[--delete-key-in-days <value>]
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

The `KeyARN` of the key that is scheduled for deletion.

`--delete-key-in-days` (integer)

The waiting period for key deletion. The default value is seven days.

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

**To delete a key**

The following `delete-key` example schedules a key for deletion after 7 days, which is the default waiting period.

```
aws payment-cryptography delete-key \
    --key-identifier arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h
```

Output:

```
{
    "Key": {
        "CreateTimestamp": "1686801198",
        "DeletePendingTimestamp": "1687405998",
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
        "KeyState": "DELETE_PENDING",
        "UsageStartTimestamp": "1686801190"
    }
}
```

For more information, see [Deleting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-deleting.html) in the *AWS Payment Cryptography User Guide*.

## Output

Key -> (structure)

The `KeyARN` of the key that is scheduled for deletion.

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