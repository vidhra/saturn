# put-supplemental-tax-registrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/put-supplemental-tax-registration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/put-supplemental-tax-registration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [taxsettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/taxsettings/index.html#cli-aws-taxsettings) ]

# put-supplemental-tax-registration

## Description

Stores supplemental tax registration for a single account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/taxsettings-2018-05-10/PutSupplementalTaxRegistration)

## Synopsis

```
put-supplemental-tax-registration
--tax-registration-entry <value>
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

`--tax-registration-entry` (structure)

The supplemental TRN information that will be stored for the caller account ID.

address -> (structure)

The details of the address associated with the TRN information.

addressLine1 -> (string)

The first line of the address.

addressLine2 -> (string)

The second line of the address, if applicable.

addressLine3 -> (string)

The third line of the address, if applicable. Currently, the Tax Settings API accepts the `addressLine3` parameter only for Saudi Arabia. When you specify a TRN in Saudi Arabia, you must enter the `addressLine3` and specify the building number for the address. For example, you might enter `1234` .

city -> (string)

The city that the address is in.

countryCode -> (string)

The country code for the country that the address is in.

districtOrCounty -> (string)

The district or county the address is located.

### Note

For addresses in Brazil, this parameter uses the name of the neighborhood. When you set a TRN in Brazil, use `districtOrCounty` for the neighborhood name.

postalCode -> (string)

The postal code associated with the address.

stateOrRegion -> (string)

The state, region, or province that the address is located. This field is only required for Canada, India, United Arab Emirates, Romania, and Brazil (CPF). It is optional for all other countries.

If this is required for tax settings, use the same name as shown on the **Tax Settings** page.

legalName -> (string)

The legal name associated with your TRN registration.

registrationId -> (string)

The supplemental TRN unique identifier.

registrationType -> (string)

Type of supplemental TRN. Currently, this can only be VAT.

Shorthand Syntax:

```
address={addressLine1=string,addressLine2=string,addressLine3=string,city=string,countryCode=string,districtOrCounty=string,postalCode=string,stateOrRegion=string},legalName=string,registrationId=string,registrationType=string
```

JSON Syntax:

```
{
  "address": {
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "city": "string",
    "countryCode": "string",
    "districtOrCounty": "string",
    "postalCode": "string",
    "stateOrRegion": "string"
  },
  "legalName": "string",
  "registrationId": "string",
  "registrationType": "VAT"
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

authorityId -> (string)

Unique authority ID for the supplemental TRN information that was stored.

status -> (string)

The status of the supplemental TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be `Verified` , `Pending` , `Rejected` , or `Deleted` .