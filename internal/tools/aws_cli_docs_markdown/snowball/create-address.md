# create-addressÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-address.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/create-address.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [snowball](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/index.html#cli-aws-snowball) ]

# create-address

## Description

Creates an address for a Snow device to be shipped to. In most regions, addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown. If providing an address as a JSON file through the `cli-input-json` option, include the full file path. For example, `--cli-input-json file://create-address.json` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/snowball-2016-06-30/CreateAddress)

## Synopsis

```
create-address
--address <value>
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

`--address` (structure)

The address that you want the Snow device shipped to.

AddressId -> (string)

The unique ID for an address.

Name -> (string)

The name of a person to receive a Snow device at an address.

Company -> (string)

The name of the company to receive a Snow device at an address.

Street1 -> (string)

The first line in a street address that a Snow device is to be delivered to.

Street2 -> (string)

The second line in a street address that a Snow device is to be delivered to.

Street3 -> (string)

The third line in a street address that a Snow device is to be delivered to.

City -> (string)

The city in an address that a Snow device is to be delivered to.

StateOrProvince -> (string)

The state or province in an address that a Snow device is to be delivered to.

PrefectureOrDistrict -> (string)

This field is no longer used and the value is ignored.

Landmark -> (string)

This field is no longer used and the value is ignored.

Country -> (string)

The country in an address that a Snow device is to be delivered to.

PostalCode -> (string)

The postal code in an address that a Snow device is to be delivered to.

PhoneNumber -> (string)

The phone number associated with an address that a Snow device is to be delivered to.

IsRestricted -> (boolean)

If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.

Type -> (string)

Differentiates between delivery address and pickup address in the customer account. Provided at job creation.

Shorthand Syntax:

```
AddressId=string,Name=string,Company=string,Street1=string,Street2=string,Street3=string,City=string,StateOrProvince=string,PrefectureOrDistrict=string,Landmark=string,Country=string,PostalCode=string,PhoneNumber=string,IsRestricted=boolean,Type=string
```

JSON Syntax:

```
{
  "AddressId": "string",
  "Name": "string",
  "Company": "string",
  "Street1": "string",
  "Street2": "string",
  "Street3": "string",
  "City": "string",
  "StateOrProvince": "string",
  "PrefectureOrDistrict": "string",
  "Landmark": "string",
  "Country": "string",
  "PostalCode": "string",
  "PhoneNumber": "string",
  "IsRestricted": true|false,
  "Type": "CUST_PICKUP"|"AWS_SHIP"
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

AddressId -> (string)

The automatically generated ID for a specific address. Youâll use this ID when you create a job to specify which address you want the Snow device for that job shipped to.