# create-device-poolÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# create-device-pool

## Description

Creates a device pool.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateDevicePool)

## Synopsis

```
create-device-pool
--project-arn <value>
--name <value>
[--description <value>]
--rules <value>
[--max-devices <value>]
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

`--project-arn` (string)

The ARN of the project for the device pool.

`--name` (string)

The device poolâs name.

`--description` (string)

The device poolâs description.

`--rules` (list)

The device poolâs rules.

(structure)

Represents a condition for a device pool.

attribute -> (string)

The ruleâs stringified attribute. For example, specify the value as `"\"abc\""` .

The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.

Supported operators: `CONTAINS`

ARN

The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example` .

Supported operators: `EQUALS` , `IN` , `NOT_IN`

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.

Supported operators: `EQUALS`

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.

Supported operators: `EQUALS`

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.

Supported operators: `EQUALS` , `IN` , `NOT_IN`

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.

Supported operators: `IN` , `NOT_IN`

INSTANCE_LABELS

The label of the device instance.

Supported operators: `CONTAINS`

MANUFACTURER

The device manufacturer (for example, Apple).

Supported operators: `EQUALS` , `IN` , `NOT_IN`

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.

Supported operators: `CONTAINS` , `EQUALS` , `IN` , `NOT_IN`

OS_VERSION

The operating system version (for example, 10.3.2).

Supported operators: `EQUALS` , `GREATER_THAN` , `GREATER_THAN_OR_EQUALS` , `IN` , `LESS_THAN` , `LESS_THAN_OR_EQUALS` , `NOT_IN`

PLATFORM

The device platform. Valid values are ANDROID or IOS.

Supported operators: `EQUALS` , `IN` , `NOT_IN`

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) , this filter is ignored.

operator -> (string)

Specifies how Device Farm compares the ruleâs attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value -> (string)

The ruleâs value.

Shorthand Syntax:

```
attribute=string,operator=string,value=string ...
```

JSON Syntax:

```
[
  {
    "attribute": "ARN"|"PLATFORM"|"FORM_FACTOR"|"MANUFACTURER"|"REMOTE_ACCESS_ENABLED"|"REMOTE_DEBUG_ENABLED"|"APPIUM_VERSION"|"INSTANCE_ARN"|"INSTANCE_LABELS"|"FLEET_TYPE"|"OS_VERSION"|"MODEL"|"AVAILABILITY",
    "operator": "EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS"|"GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"IN"|"NOT_IN"|"CONTAINS",
    "value": "string"
  }
  ...
]
```

`--max-devices` (integer)

The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the `rules` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.

By specifying the maximum number of devices, you can control the costs that you incur by running tests.

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

**To create a device pool**

The following command creates an Android device pool for a project:

```
aws devicefarm create-device-pool --name pool1 --rules file://device-pool-rules.json --project-arn "arn:aws:devicefarm:us-west-2:123456789012:project:070fc3ca-7ec1-4741-9c1f-d3e044efc506"
```

You can get the project ARN from the output of `create-project` or `list-projects`. The file `device-pool-rules.json` is a JSON document in the current folder that specifies the device platform:

```
[
    {
        "attribute": "PLATFORM",
        "operator": "EQUALS",
        "value": "\"ANDROID\""
    }
]
```

Output:

```
{
    "devicePool": {
        "rules": [
            {
                "operator": "EQUALS",
                "attribute": "PLATFORM",
                "value": "\"ANDROID\""
            }
        ],
        "type": "PRIVATE",
        "name": "pool1",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:devicepool:070fc3ca-7ec1-4741-9c1f-d3e044efc506/2aa8d2a9-5e73-47ca-b929-659cb34b7dcd"
    }
}
```

## Output

devicePool -> (structure)

The newly created device pool.

arn -> (string)

The device poolâs ARN.

name -> (string)

The device poolâs name.

description -> (string)

The device poolâs description.

type -> (string)

The device poolâs type.

Allowed values include:

- CURATED: A device pool that is created and managed by AWS Device Farm.
- PRIVATE: A device pool that is created and managed by the device pool developer.

rules -> (list)

Information about the device poolâs rules.

(structure)

Represents a condition for a device pool.

attribute -> (string)

The ruleâs stringified attribute. For example, specify the value as `"\"abc\""` .

The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.

Supported operators: `CONTAINS`

ARN

The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example` .

Supported operators: `EQUALS` , `IN` , `NOT_IN`

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.

Supported operators: `EQUALS`

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.

Supported operators: `EQUALS`

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.

Supported operators: `EQUALS` , `IN` , `NOT_IN`

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.

Supported operators: `IN` , `NOT_IN`

INSTANCE_LABELS

The label of the device instance.

Supported operators: `CONTAINS`

MANUFACTURER

The device manufacturer (for example, Apple).

Supported operators: `EQUALS` , `IN` , `NOT_IN`

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.

Supported operators: `CONTAINS` , `EQUALS` , `IN` , `NOT_IN`

OS_VERSION

The operating system version (for example, 10.3.2).

Supported operators: `EQUALS` , `GREATER_THAN` , `GREATER_THAN_OR_EQUALS` , `IN` , `LESS_THAN` , `LESS_THAN_OR_EQUALS` , `NOT_IN`

PLATFORM

The device platform. Valid values are ANDROID or IOS.

Supported operators: `EQUALS` , `IN` , `NOT_IN`

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) , this filter is ignored.

operator -> (string)

Specifies how Device Farm compares the ruleâs attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value -> (string)

The ruleâs value.

maxDevices -> (integer)

The number of devices that Device Farm can add to your device pool. Device Farm adds devices that are available and meet the criteria that you assign for the `rules` parameter. Depending on how many devices meet these constraints, your device pool might contain fewer devices than the value for this parameter.

By specifying the maximum number of devices, you can control the costs that you incur by running tests.