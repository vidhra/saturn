# update-deviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/update-device.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [networkmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/index.html#cli-aws-networkmanager) ]

# update-device

## Description

Updates the details for an existing device. To remove information for any of the parameters, specify an empty string.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/networkmanager-2019-07-05/UpdateDevice)

## Synopsis

```
update-device
--global-network-id <value>
--device-id <value>
[--aws-location <value>]
[--description <value>]
[--type <value>]
[--vendor <value>]
[--model <value>]
[--serial-number <value>]
[--location <value>]
[--site-id <value>]
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

`--global-network-id` (string)

The ID of the global network.

`--device-id` (string)

The ID of the device.

`--aws-location` (structure)

The Amazon Web Services location of the device, if applicable. For an on-premises device, you can omit this parameter.

Zone -> (string)

The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.

SubnetArn -> (string)

The Amazon Resource Name (ARN) of the subnet that the device is located in.

Shorthand Syntax:

```
Zone=string,SubnetArn=string
```

JSON Syntax:

```
{
  "Zone": "string",
  "SubnetArn": "string"
}
```

`--description` (string)

A description of the device.

Constraints: Maximum length of 256 characters.

`--type` (string)

The type of the device.

`--vendor` (string)

The vendor of the device.

Constraints: Maximum length of 128 characters.

`--model` (string)

The model of the device.

Constraints: Maximum length of 128 characters.

`--serial-number` (string)

The serial number of the device.

Constraints: Maximum length of 128 characters.

`--location` (structure)

Describes a location.

Address -> (string)

The physical address.

Latitude -> (string)

The latitude.

Longitude -> (string)

The longitude.

Shorthand Syntax:

```
Address=string,Latitude=string,Longitude=string
```

JSON Syntax:

```
{
  "Address": "string",
  "Latitude": "string",
  "Longitude": "string"
}
```

`--site-id` (string)

The ID of the site.

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

**To update a device**

The following `update-device` example updates device `device-07f6fd08867abc123` by specifying a site ID for the device.

```
aws networkmanager update-device \
    --global-network-id global-network-01231231231231231 \
    --device-id device-07f6fd08867abc123 \
    --site-id site-444555aaabbb11223 \
    --region us-west-2
```

Output:

```
{
    "Device": {
        "DeviceId": "device-07f6fd08867abc123",
        "DeviceArn": "arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123",
        "GlobalNetworkId": "global-network-01231231231231231",
        "Description": "NY office device",
        "Type": "Office device",
        "Vendor": "anycompany",
        "Model": "abcabc",
        "SerialNumber": "1234",
        "SiteId": "site-444555aaabbb11223",
        "CreatedAt": 1575554005.0,
        "State": "UPDATING"
    }
}
```

For more information, see [Working with Devices](https://docs.aws.amazon.com/vpc/latest/tgw/on-premises-networks.html#working-with-devices) in the *Transit Gateway Network Manager Guide*.

## Output

Device -> (structure)

Information about the device.

DeviceId -> (string)

The ID of the device.

DeviceArn -> (string)

The Amazon Resource Name (ARN) of the device.

GlobalNetworkId -> (string)

The ID of the global network.

AWSLocation -> (structure)

The Amazon Web Services location of the device.

Zone -> (string)

The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.

SubnetArn -> (string)

The Amazon Resource Name (ARN) of the subnet that the device is located in.

Description -> (string)

The description of the device.

Type -> (string)

The device type.

Vendor -> (string)

The device vendor.

Model -> (string)

The device model.

SerialNumber -> (string)

The device serial number.

Location -> (structure)

The site location.

Address -> (string)

The physical address.

Latitude -> (string)

The latitude.

Longitude -> (string)

The longitude.

SiteId -> (string)

The site ID.

CreatedAt -> (timestamp)

The date and time that the site was created.

State -> (string)

The device state.

Tags -> (list)

The tags for the device.

(structure)

Describes a tag.

Key -> (string)

The tag key.

Constraints: Maximum length of 128 characters.

Value -> (string)

The tag value.

Constraints: Maximum length of 256 characters.