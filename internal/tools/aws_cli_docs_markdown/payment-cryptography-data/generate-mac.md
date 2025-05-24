# generate-macÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-mac.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-mac.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [payment-cryptography-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/index.html#cli-aws-payment-cryptography-data) ]

# generate-mac

## Description

Generates a Message Authentication Code (MAC) cryptogram within Amazon Web Services Payment Cryptography.

You can use this operation to authenticate card-related data by using known data values to generate MAC for data validation between the sending and receiving parties. This operation uses message data, a secret encryption key and MAC algorithm to generate a unique MAC value for transmission. The receiving party of the MAC must use the same message data, secret encryption key and MAC algorithm to reproduce another MAC value for comparision.

You can use this operation to generate a DUPKT, CMAC, HMAC or EMV MAC by setting generation attributes and algorithm to the associated values. The MAC generation encryption key must have valid values for `KeyUsage` such as `TR31_M7_HMAC_KEY` for HMAC generation, and they key must have `KeyModesOfUse` set to `Generate` and `Verify` .

For information about valid keys for this operation, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) and [Key types for specific data operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops-validkeys-ops.html) in the *Amazon Web Services Payment Cryptography User Guide* .

**Cross-account use** : This operation canât be used across different Amazon Web Services accounts.

**Related operations:**

- VerifyMac

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/payment-cryptography-data-2022-02-03/GenerateMac)

## Synopsis

```
generate-mac
--key-identifier <value>
--message-data <value>
--generation-attributes <value>
[--mac-length <value>]
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

The `keyARN` of the MAC generation encryption key.

`--message-data` (string)

The data for which a MAC is under generation. This value must be hexBinary.

`--generation-attributes` (tagged union structure)

The attributes and data values to use for MAC generation within Amazon Web Services Payment Cryptography.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Algorithm`, `EmvMac`, `DukptIso9797Algorithm1`, `DukptIso9797Algorithm3`, `DukptCmac`.

Algorithm -> (string)

The encryption algorithm for MAC generation or verification.

EmvMac -> (structure)

Parameters that are required for MAC generation or verification using EMV MAC algorithm.

MajorKeyDerivationMode -> (string)

The method to use when deriving the master key for EMV MAC generation or verification.

PrimaryAccountNumber -> (string)

The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.

PanSequenceNumber -> (string)

A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).

SessionKeyDerivationMode -> (string)

The method of deriving a session key for EMV MAC generation or verification.

SessionKeyDerivationValue -> (tagged union structure)

Parameters that are required to generate session key for EMV generation and verification.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ApplicationCryptogram`, `ApplicationTransactionCounter`.

ApplicationCryptogram -> (string)

The cryptogram provided by the terminal during transaction processing.

ApplicationTransactionCounter -> (string)

The transaction counter that is provided by the terminal during transaction processing.

DukptIso9797Algorithm1 -> (structure)

Parameters that are required for MAC generation or verification using DUKPT ISO 9797 algorithm1.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be MAC generation, MAC verification, or both.

DukptDerivationType -> (string)

The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY` .

DukptIso9797Algorithm3 -> (structure)

Parameters that are required for MAC generation or verification using DUKPT ISO 9797 algorithm3.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be MAC generation, MAC verification, or both.

DukptDerivationType -> (string)

The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY` .

DukptCmac -> (structure)

Parameters that are required for MAC generation or verification using DUKPT CMAC algorithm.

KeySerialNumber -> (string)

The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.

DukptKeyVariant -> (string)

The type of use of DUKPT, which can be MAC generation, MAC verification, or both.

DukptDerivationType -> (string)

The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you canât use `AES_128` as a derivation type for a BDK of `AES_128` or `TDES_2KEY` .

Shorthand Syntax:

```
Algorithm=string,EmvMac={MajorKeyDerivationMode=string,PrimaryAccountNumber=string,PanSequenceNumber=string,SessionKeyDerivationMode=string,SessionKeyDerivationValue={ApplicationCryptogram=string,ApplicationTransactionCounter=string}},DukptIso9797Algorithm1={KeySerialNumber=string,DukptKeyVariant=string,DukptDerivationType=string},DukptIso9797Algorithm3={KeySerialNumber=string,DukptKeyVariant=string,DukptDerivationType=string},DukptCmac={KeySerialNumber=string,DukptKeyVariant=string,DukptDerivationType=string}
```

JSON Syntax:

```
{
  "Algorithm": "ISO9797_ALGORITHM1"|"ISO9797_ALGORITHM3"|"CMAC"|"HMAC_SHA224"|"HMAC_SHA256"|"HMAC_SHA384"|"HMAC_SHA512",
  "EmvMac": {
    "MajorKeyDerivationMode": "EMV_OPTION_A"|"EMV_OPTION_B",
    "PrimaryAccountNumber": "string",
    "PanSequenceNumber": "string",
    "SessionKeyDerivationMode": "EMV_COMMON_SESSION_KEY"|"EMV2000"|"AMEX"|"MASTERCARD_SESSION_KEY"|"VISA",
    "SessionKeyDerivationValue": {
      "ApplicationCryptogram": "string",
      "ApplicationTransactionCounter": "string"
    }
  },
  "DukptIso9797Algorithm1": {
    "KeySerialNumber": "string",
    "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE",
    "DukptDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"
  },
  "DukptIso9797Algorithm3": {
    "KeySerialNumber": "string",
    "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE",
    "DukptDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"
  },
  "DukptCmac": {
    "KeySerialNumber": "string",
    "DukptKeyVariant": "BIDIRECTIONAL"|"REQUEST"|"RESPONSE",
    "DukptDerivationType": "TDES_2KEY"|"TDES_3KEY"|"AES_128"|"AES_192"|"AES_256"
  }
}
```

`--mac-length` (integer)

The length of a MAC under generation.

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

**To generate a MAC**

The following `generate-card-validation-data` example generates a Hash-Based Message Authentication Code (HMAC) for card data authentication using the algorithm HMAC_SHA256 and an HMAC encryption key. The key must have `KeyUsage` set to `TR31_M7_HMAC_KEY` and `KeyModesOfUse` to `Generate`.

```
aws payment-cryptography-data generate-mac \
    --key-identifier arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h \
    --message-data "3b313038383439303031303733393431353d32343038323236303030373030303f33" \
    --generation-attributes Algorithm=HMAC_SHA256
```

Output:

```
{
    "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h,
    "KeyCheckValue": "2976E7",
    "Mac": "ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C"
}
```

For more information, see [Generate MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-mac.html) in the *AWS Payment Cryptography User Guide*.

## Output

KeyArn -> (string)

The `keyARN` of the encryption key that Amazon Web Services Payment Cryptography uses for MAC generation.

KeyCheckValue -> (string)

The key check value (KCV) of the encryption key. The KCV is used to check if all parties holding a given key have the same key or to detect that a key has changed.

Amazon Web Services Payment Cryptography computes the KCV according to the CMAC specification.

Mac -> (string)

The MAC cryptogram generated within Amazon Web Services Payment Cryptography.