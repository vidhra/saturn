# get-shipping-labelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/get-shipping-label.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/get-shipping-label.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [importexport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/index.html#cli-aws-importexport) ]

# get-shipping-label

## Description

This operation generates a pre-paid UPS shipping label that you will use to ship your device to AWS for processing.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/GetShippingLabel)

## Synopsis

```
get-shipping-label
--job-ids <value>
[--name <value>]
[--company <value>]
[--phone-number <value>]
[--country <value>]
[--state-or-province <value>]
[--city <value>]
[--postal-code <value>]
[--street1 <value>]
[--street2 <value>]
[--street3 <value>]
[--api-version <value>]
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

`--job-ids` (list)
(string)

Syntax:

```
"string" "string" ...
```

`--name` (string)
Specifies the name of the person responsible for shipping this package.

`--company` (string)
Specifies the name of the company that will ship this package.

`--phone-number` (string)
Specifies the phone number of the person responsible for shipping this package.

`--country` (string)
Specifies the name of your country for the return address.

`--state-or-province` (string)
Specifies the name of your state or your province for the return address.

`--city` (string)
Specifies the name of your city for the return address.

`--postal-code` (string)
Specifies the postal code for the return address.

`--street1` (string)
Specifies the first part of the street address for the return address, for example 1234 Main Street.

`--street2` (string)
Specifies the optional second part of the street address for the return address, for example Suite 100.

`--street3` (string)
Specifies the optional third part of the street address for the return address, for example c/o Jane Doe.

`--api-version` (string)
Specifies the version of the client tool.

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

The following command creates a pre-paid shipping label for the specified job:

```
aws importexport get-shipping-label --job-ids EX1ID --name "Jane Roe" --company "Example Corp." --phone-number "206-555-1111" --country "USA" --state-or-province "WA" --city "Anytown" --postal-code "91011-1111" --street-1 "123 Any Street"
```

The output for the get-shipping-label command looks like the following:

```
https://s3.amazonaws.com/amzn-s3-demo-bucket/shipping-label-EX1ID.pdf
```

The link in the output contains the pre-paid shipping label generated in a PDF. It also contains shipping instructions with a unique bar code to identify and authenticate your device. For more information about using the pre-paid shipping label and shipping your device, see [Shipping Your Storage Device](http://docs.aws.amazon.com/AWSImportExport/latest/DG/CHAP_ShippingYourStorageDevice.html) in the *AWS Import/Export Developer Guide*.

## Output

ShippingLabelURL -> (string)

Warning -> (string)