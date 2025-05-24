# verify-card-validation-dataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-card-validation-data.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-card-validation-data.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# verify-card-validation-data

## Description

Verifies card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card Security Codes (CSC). For more information, see [Verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html) in the *Amazon Web Services Payment Cryptography User Guide* .

This operation validates the CVV or CSC codes that is printed on a payment credit or debit card during card payment transaction. The input values are typically provided as part of an inbound transaction to an issuer or supporting platform partner. Amazon Web Services Payment Cryptography uses CVV or CSC, PAN (Primary Account Number) and expiration date of the card to check its validity during transaction processing. In this operation, the CVK (Card Verification Key) encryption key for use with card data verification is same as the one in used for  GenerateCardValidationData .

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- GenerateCardValidationData
- VerifyAuthRequestCryptogram
- VerifyPinData

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/VerifyCardValidationData)

## Synopsis

```
verify-card-validation-data
--key-identifier <value>
--primary-account-number <value>
--verification-attributes <value>
--validation-data <value>
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

The `keyARN` of the CVK encryption key that Amazon Web Services Payment Cryptography uses to verify card data.

`--primary-account-number` (string)

The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.

`--verification-attributes` (tagged union structure)

The algorithm to use for verification of card data within Amazon Web Services Payment Cryptography.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AmexCardSecurityCodeVersion1`, `AmexCardSecurityCodeVersion2`, `CardVerificationValue1`, `CardVerificationValue2`, `CardHolderVerificationValue`, `DynamicCardVerificationCode`, `DynamicCardVerificationValue`, `DiscoverDynamicCardVerificationCode`.

AmexCardSecurityCodeVersion1 -> (structure)

Card data parameters that are required to generate a Card Security Code (CSC2) for an AMEX payment card.

CardExpiryDate -> (string)

The expiry date of a payment card.

AmexCardSecurityCodeVersion2 -> (structure)

Card data parameters that are required to verify a Card Security Code (CSC2) for an AMEX payment card.

CardExpiryDate -> (string)

The expiry date of a payment card.

ServiceCode -> (string)

The service code of the AMEX payment card. This is different from the Card Security Code (CSC).

CardVerificationValue1 -> (structure)

Card data parameters that are required to verify Card Verification Value (CVV) for the payment card.

CardExpiryDate -> (string)

The expiry date of a payment card.

ServiceCode -> (string)

The service code of the payment card. This is different from Card Security Code (CSC).

CardVerificationValue2 -> (structure)

Card data parameters that are required to verify Card Verification Value (CVV2) for the payment card.

CardExpiryDate -> (string)

The expiry date of a payment card.

CardHolderVerificationValue -> (structure)

Card data parameters that are required to verify a cardholder verification value for the payment card.

UnpredictableNumber -> (string)

A random number generated by the issuer.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

ApplicationTransactionCounter -> (string)

The transaction counter value that comes from a point of sale terminal.

DynamicCardVerificationCode -> (structure)

Card data parameters that are required to verify CDynamic Card Verification Code (dCVC) for the payment card.

UnpredictableNumber -> (string)

A random number generated by the issuer.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

ApplicationTransactionCounter -> (string)

The transaction counter value that comes from the terminal.

TrackData -> (string)

The data on the two tracks of magnetic cards used for financial transactions. This includes the cardholder name, PAN, expiration date, bank ID (BIN) and several other numbers the issuing bank uses to validate the data received.

DynamicCardVerificationValue -> (structure)

Card data parameters that are required to verify CDynamic Card Verification Value (dCVV) for the payment card.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

CardExpiryDate -> (string)

The expiry date of a payment card.

ServiceCode -> (string)

The service code of the payment card. This is different from Card Security Code (CSC).

ApplicationTransactionCounter -> (string)

The transaction counter value that comes from the terminal.

DiscoverDynamicCardVerificationCode -> (structure)

Card data parameters that are required to verify CDynamic Card Verification Code (dCVC) for the payment card.

CardExpiryDate -> (string)

The expiry date of a payment card.

UnpredictableNumber -> (string)

A random number that is generated by the issuer.

ApplicationTransactionCounter -> (string)

The transaction counter value that comes from the terminal.

Shorthand Syntax:

```
AmexCardSecurityCodeVersion1={CardExpiryDate=string},AmexCardSecurityCodeVersion2={CardExpiryDate=string,ServiceCode=string},CardVerificationValue1={CardExpiryDate=string,ServiceCode=string},CardVerificationValue2={CardExpiryDate=string},CardHolderVerificationValue={UnpredictableNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string},DynamicCardVerificationCode={UnpredictableNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string,TrackData=string},DynamicCardVerificationValue={PanSequenceNumber=string,CardExpiryDate=string,ServiceCode=string,ApplicationTransactionCounter=string},DiscoverDynamicCardVerificationCode={CardExpiryDate=string,UnpredictableNumber=string,ApplicationTransactionCounter=string}
```

JSON Syntax:

```
{
  "AmexCardSecurityCodeVersion1": {
    "CardExpiryDate": "string"
  },
  "AmexCardSecurityCodeVersion2": {
    "CardExpiryDate": "string",
    "ServiceCode": "string"
  },
  "CardVerificationValue1": {
    "CardExpiryDate": "string",
    "ServiceCode": "string"
  },
  "CardVerificationValue2": {
    "CardExpiryDate": "string"
  },
  "CardHolderVerificationValue": {
    "UnpredictableNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string"
  },
  "DynamicCardVerificationCode": {
    "UnpredictableNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string",
    "TrackData": "string"
  },
  "DynamicCardVerificationValue": {
    "PanSequenceNumber": "string",
    "CardExpiryDate": "string",
    "ServiceCode": "string",
    "ApplicationTransactionCounter": "string"
  },
  "DiscoverDynamicCardVerificationCode": {
    "CardExpiryDate": "string",
    "UnpredictableNumber": "string",
    "ApplicationTransactionCounter": "string"
  }
}
```

`--validation-data` (string)

The CVV or CSC value for use for card data verification within Amazon Web Services Payment Cryptography.

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

**To validate a CVV**

The following `verify-card-validation-data` example validates a CVV/CVV2 for a PAN.

```
aws payment-cryptography-data verify-card-validation-data \
    --key-identifier arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi \
    --primary-account-number=171234567890123 \
    --verification-attributes CardVerificationValue2={CardExpiryDate=0123} \
    --validation-data 801
```

Output:

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi",
    "KeyCheckValue": "CADDA1"
}
```

For more information, see [Verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html) in the *AWS Payment Cryptography User Guide*.

## Output

KeyArn -> (string)

The `keyARN` of the CVK encryption key that Amazon Web Services Payment Cryptography uses to verify CVV or CSC.

KeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.