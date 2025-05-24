# verify-auth-request-cryptogramÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-auth-request-cryptogram.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-auth-request-cryptogram.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# verify-auth-request-cryptogram

## Description

Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card authorization. For more information, see [Verify auth request cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html) in the *Amazon Web Services Payment Cryptography User Guide* .

ARQC generation is done outside of Amazon Web Services Payment Cryptography and is typically generated on a point of sale terminal for an EMV chip card to obtain payment authorization during transaction time. For ARQC verification, you must first import the ARQC generated outside of Amazon Web Services Payment Cryptography by calling [ImportKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ImportKey.html) . This operation uses the imported ARQC and an major encryption key (DUKPT) created by calling [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html) to either provide a boolean ARQC verification result or provide an APRC (Authorization Response Cryptogram) response using Method 1 or Method 2. The `ARPC_METHOD_1` uses `AuthResponseCode` to generate ARPC and `ARPC_METHOD_2` uses `CardStatusUpdate` to generate ARPC.

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- VerifyCardValidationData
- VerifyPinData

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/VerifyAuthRequestCryptogram)

## Synopsis

```
verify-auth-request-cryptogram
--key-identifier <value>
--transaction-data <value>
--auth-request-cryptogram <value>
--major-key-derivation-mode <value>
--session-key-derivation-attributes <value>
[--auth-response-attributes <value>]
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

The `keyARN` of the major encryption key that Amazon Web Services Payment Cryptography uses for ARQC verification.

`--transaction-data` (string)

The transaction data that Amazon Web Services Payment Cryptography uses for ARQC verification. The same transaction is used for ARQC generation outside of Amazon Web Services Payment Cryptography.

`--auth-request-cryptogram` (string)

The auth request cryptogram imported into Amazon Web Services Payment Cryptography for ARQC verification using a major encryption key and transaction data.

`--major-key-derivation-mode` (string)

The method to use when deriving the major encryption key for ARQC verification within Amazon Web Services Payment Cryptography. The same key derivation mode was used for ARQC generation outside of Amazon Web Services Payment Cryptography.

Possible values:

- `EMV_OPTION_A`
- `EMV_OPTION_B`

`--session-key-derivation-attributes` (tagged union structure)

The attributes and values to use for deriving a session key for ARQC verification within Amazon Web Services Payment Cryptography. The same attributes were used for ARQC generation outside of Amazon Web Services Payment Cryptography.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `EmvCommon`, `Mastercard`, `Emv2000`, `Amex`, `Visa`.

EmvCommon -> (structure)

Parameters to derive session key for an Emv common payment card for ARQC verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

ApplicationTransactionCounter -> (string)

The transaction counter that is provided by the terminal during transaction processing.

Mastercard -> (structure)

Parameters to derive session key for a Mastercard payment card for ARQC verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

ApplicationTransactionCounter -> (string)

The transaction counter that is provided by the terminal during transaction processing.

UnpredictableNumber -> (string)

A random number generated by the issuer.

Emv2000 -> (structure)

Parameters to derive session key for an Emv2000 payment card for ARQC verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

ApplicationTransactionCounter -> (string)

The transaction counter that is provided by the terminal during transaction processing.

Amex -> (structure)

Parameters to derive session key for an Amex payment card for ARQC verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

Visa -> (structure)

Parameters to derive session key for a Visa payment cardfor ARQC verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN) of the cardholder. A PAN is a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

Shorthand Syntax:

```
EmvCommon={PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string},Mastercard={PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string,UnpredictableNumber=string},Emv2000={PrimaryAccountNumber=string,PanSequenceNumber=string,ApplicationTransactionCounter=string},Amex={PrimaryAccountNumber=string,PanSequenceNumber=string},Visa={PrimaryAccountNumber=string,PanSequenceNumber=string}
```

JSON Syntax:

```
{
  "EmvCommon": {
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string"
  },
  "Mastercard": {
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string",
    "UnpredictableNumber": "string"
  },
  "Emv2000": {
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "ApplicationTransactionCounter": "string"
  },
  "Amex": {
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string"
  },
  "Visa": {
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string"
  }
}
```

`--auth-response-attributes` (tagged union structure)

The attributes and values for auth request cryptogram verification. These parameters are required in case using ARPC Method 1 or Method 2 for ARQC verification.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ArpcMethod1`, `ArpcMethod2`.

ArpcMethod1 -> (structure)

Parameters that are required for ARPC response generation using method1 after ARQC verification is successful.

AuthResponseCode -> (string)

The auth code used to calculate APRC after ARQC verification is successful. This is the same auth code used for ARQC generation outside of Amazon Web Services Payment Cryptography.

ArpcMethod2 -> (structure)

Parameters that are required for ARPC response generation using method2 after ARQC verification is successful.

CardStatusUpdate -> (string)

The data indicating whether the issuer approves or declines an online transaction using an EMV chip card.

ProprietaryAuthenticationData -> (string)

The proprietary authentication data used by issuer for communication during online transaction using an EMV chip card.

Shorthand Syntax:

```
ArpcMethod1={AuthResponseCode=string},ArpcMethod2={CardStatusUpdate=string,ProprietaryAuthenticationData=string}
```

JSON Syntax:

```
{
  "ArpcMethod1": {
    "AuthResponseCode": "string"
  },
  "ArpcMethod2": {
    "CardStatusUpdate": "string",
    "ProprietaryAuthenticationData": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To verify an auth request**

The following `verify-auth-request-cryptogram` example verifies an Authorization Request Cryptogram (ARQC).

```
aws payment-cryptography-data verify-auth-request-cryptogram \
    --auth-request-cryptogram F6E1BD1E6037FB3E \
    --auth-response-attributes '{"ArpcMethod1": {"AuthResponseCode": "1111"}}' \
    --key-identifier arn:aws:payment-cryptography:us-west-2:111122223333:key/pboipdfzd4mdklya \
    --major-key-derivation-mode "EMV_OPTION_A" \
    --session-key-derivation-attributes '{"EmvCommon": {"ApplicationTransactionCounter": "1234","PanSequenceNumber": "01","PrimaryAccountNumber": "471234567890123"}}' \
    --transaction-data "123456789ABCDEF"
```

Output:

```
{
    "AuthResponseValue": "D899B8C6FBF971AA",
    "KeyArn": "arn:aws:payment-cryptography:us-west-2:111122223333:key/pboipdfzd4mdklya",
    "KeyCheckValue": "985792"
}
```

For more information, see [Verify auth request (ARQC) cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html) in the *AWS Payment Cryptography User Guide*.

## Output

KeyArn -> (string)

The `keyARN` of the major encryption key that Amazon Web Services Payment Cryptography uses for ARQC verification.

KeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.

AuthResponseValue -> (string)

The result for ARQC verification or ARPC generation within Amazon Web Services Payment Cryptography.