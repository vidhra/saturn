# generate-mac-emv-pin-changeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-mac-emv-pin-change.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-mac-emv-pin-change.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# generate-mac-emv-pin-change

## Description

Generates an issuer script mac for EMV payment cards that use offline PINs as the cardholder verification method (CVM).

This operation generates an authenticated issuer script response by appending the incoming message data (APDU command) with the target encrypted PIN block in ISO2 format. The command structure and method to send the issuer script update to the card is not defined by this operation and is typically determined by the applicable payment card scheme.

The primary inputs to this operation include the incoming new encrypted pinblock, PIN encryption key (PEK), issuer master key (IMK), primary account number (PAN), and the payment card derivation method.

The operation uses two issuer master keys - secure messaging for confidentiality (IMK-SMC) and secure messaging for integrity (IMK-SMI). The SMC key is used to internally derive a key to secure the pin, while SMI key is used to internally derive a key to authenticate the script reponse as per the [EMV 4.4 - Book 2 - Security and Key Management](https://www.emvco.com/specifications/) specification.

This operation supports Amex, EMV2000, EMVCommon, Mastercard and Visa derivation methods, each requiring specific input parameters. Users must follow the specific derivation method and input parameters defined by the respective payment card scheme.

### Note

Use  GenerateMac operation when sending a script update to an EMV card that does not involve PIN change. When assigning IAM permissions, it is important to understand that  EncryptData using EMV keys and  GenerateMac perform similar functions to this command.

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- EncryptData
- GenerateMac

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/GenerateMacEmvPinChange)

## Synopsis

```
generate-mac-emv-pin-change
--new-pin-pek-identifier <value>
--new-encrypted-pin-block <value>
--pin-block-format <value>
--secure-messaging-integrity-key-identifier <value>
--secure-messaging-confidentiality-key-identifier <value>
--message-data <value>
--derivation-method-attributes <value>
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

`--new-pin-pek-identifier` (string)

The `keyARN` of the PEK protecting the incoming new encrypted PIN block.

`--new-encrypted-pin-block` (string)

The incoming new encrypted PIN block data for offline pin change on an EMV card.

`--pin-block-format` (string)

The PIN encoding format of the incoming new encrypted PIN block as specified in ISO 9564.

Possible values:

- `ISO_FORMAT_0`
- `ISO_FORMAT_1`
- `ISO_FORMAT_3`

`--secure-messaging-integrity-key-identifier` (string)

The `keyARN` of the issuer master key (IMK-SMI) used to authenticate the issuer script response.

`--secure-messaging-confidentiality-key-identifier` (string)

The `keyARN` of the issuer master key (IMK-SMC) used to protect the PIN block data in the issuer script response.

`--message-data` (string)

The message data is the APDU command from the card reader or terminal. The target encrypted PIN block, after translation to ISO2 format, is appended to this message data to generate an issuer script response.

`--derivation-method-attributes` (tagged union structure)

The attributes and data values to derive payment card specific confidentiality and integrity keys.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EmvCommon`, `Amex`, `Visa`, `Emv2000`, `Mastercard`.

EmvCommon -> (structure)

Parameters to derive the confidentiality and integrity keys for a payment card using Emv common derivation method.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for the payment card.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

ApplicationCryptogram -> (string)

The application cryptogram for the current transaction that is provided by the terminal during transaction processing.

Mode -> (string)

The block cipher method to use for encryption.

PinBlockPaddingType -> (string)

The padding to be added to the PIN block prior to encryption.

Padding type should be `ISO_IEC_7816_4` , if `PinBlockLengthPosition` is set to `FRONT_OF_PIN_BLOCK` . No padding is required, if `PinBlockLengthPosition` is set to `NONE` .

PinBlockLengthPosition -> (string)

Specifies if PIN block length should be added to front of the pin block.

If value is set to `FRONT_OF_PIN_BLOCK` , then PIN block padding type should be `ISO_IEC_7816_4` .

Amex -> (structure)

Parameters to derive the confidentiality and integrity keys for a payment card using Amex derivation method.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for a payment card using Amex derivation.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

ApplicationTransactionCounter -> (string)

The transaction counter of the current transaction that is provided by the terminal during transaction processing.

AuthorizationRequestKeyIdentifier -> (string)

The `keyArn` of the issuer master key for cryptogram (IMK-AC) for the payment card.

CurrentPinAttributes -> (structure)

The encrypted pinblock of the old pin stored on the chip card.

CurrentPinPekIdentifier -> (string)

The `keyArn` of the current PIN PEK.

CurrentEncryptedPinBlock -> (string)

The encrypted pinblock of the current pin stored on the chip card.

Visa -> (structure)

Parameters to derive the confidentiality and integrity keys for a a payment card using Visa derivation method.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for the payment card.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

ApplicationTransactionCounter -> (string)

The transaction counter of the current transaction that is provided by the terminal during transaction processing.

AuthorizationRequestKeyIdentifier -> (string)

The `keyArn` of the issuer master key for cryptogram (IMK-AC) for the payment card.

CurrentPinAttributes -> (structure)

The encrypted pinblock of the old pin stored on the chip card.

CurrentPinPekIdentifier -> (string)

The `keyArn` of the current PIN PEK.

CurrentEncryptedPinBlock -> (string)

The encrypted pinblock of the current pin stored on the chip card.

Emv2000 -> (structure)

Parameters to derive the confidentiality and integrity keys for a payment card using Emv2000 derivation method.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for the payment card.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

ApplicationTransactionCounter -> (string)

The transaction counter of the current transaction that is provided by the terminal during transaction processing.

Mastercard -> (structure)

Parameters to derive the confidentiality and integrity keys for a payment card using Mastercard derivation method.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for the payment card.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.

ApplicationCryptogram -> (string)

The application cryptogram for the current transaction that is provided by the terminal during transaction processing.

Shorthand Syntax:

```
EmvCommon={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationCryptogram=string,Mode=string,PinBlockPaddingType=string,PinBlockLengthPosition=string},Amex={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string,AuthorizationRequestKeyIdentifier=string,CurrentPinAttributes={CurrentPinPekIdentifier=string,CurrentEncryptedPinBlock=string}},Visa={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string,AuthorizationRequestKeyIdentifier=string,CurrentPinAttributes={CurrentPinPekIdentifier=string,CurrentEncryptedPinBlock=string}},Emv2000={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string},Mastercard={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationCryptogram=string}
```

JSON Syntax:

```
{
  "EmvCommon": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationCryptogram": "string",
    "Mode": "ECB"|"CBC",
    "PinBlockPaddingType": "NO_PADDING"|"ISO_IEC_7816_4",
    "PinBlockLengthPosition": "NONE"|"FRONT_OF_PIN_BLOCK"
  },
  "Amex": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string",
    "AuthorizationRequestKeyIdentifier": "string",
    "CurrentPinAttributes": {
      "CurrentPinPekIdentifier": "string",
      "CurrentEncryptedPinBlock": "string"
    }
  },
  "Visa": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string",
    "AuthorizationRequestKeyIdentifier": "string",
    "CurrentPinAttributes": {
      "CurrentPinPekIdentifier": "string",
      "CurrentEncryptedPinBlock": "string"
    }
  },
  "Emv2000": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string"
  },
  "Mastercard": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationCryptogram": "string"
  }
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

## Output

NewPinPekArn -> (string)

Returns the `keyArn` of the PEK protecting the incoming new encrypted PIN block.

SecureMessagingIntegrityKeyArn -> (string)

Returns the `keyArn` of the IMK-SMI used by the operation.

SecureMessagingConfidentialityKeyArn -> (string)

Returns the `keyArn` of the IMK-SMC used by the operation.

Mac -> (string)

Returns the mac of the issuer script containing message data and appended target encrypted pin block in ISO2 format.

EncryptedPinBlock -> (string)

Returns the incoming new encrpted PIN block.

NewPinPekKeyCheckValue -> (string)

The key check value (KCV) of the PEK uprotecting the incoming new encrypted PIN block.

SecureMessagingIntegrityKeyCheckValue -> (string)

The key check value (KCV) of the SMI issuer master key used by the operation.

SecureMessagingConfidentialityKeyCheckValue -> (string)

The key check value (KCV) of the SMC issuer master key used by the operation.

VisaAmexDerivationOutputs -> (structure)

The attribute values used for Amex and Visa derivation methods.

AuthorizationRequestKeyArn -> (string)

The `keyArn` of the issuer master key for cryptogram (IMK-AC) used by the operation.

AuthorizationRequestKeyCheckValue -> (string)

The key check value (KCV) of the issuer master key for cryptogram (IMK-AC) used by the operation.

CurrentPinPekArn -> (string)

The `keyArn` of the current PIN PEK.

CurrentPinPekKeyCheckValue -> (string)

The key check value (KCV) of the current PIN PEK.