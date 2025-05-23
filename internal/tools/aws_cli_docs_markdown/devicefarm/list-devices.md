# list-devicesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-devices.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-devices.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# list-devices

## Description

Gets information about unique device types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListDevices)

`list-devices` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `devices`

## Synopsis

```
list-devices
[--arn <value>]
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--arn` (string)

The Amazon Resource Name (ARN) of the project.

`--filters` (list)

Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.

- Attribute: The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:
- ARN: The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example` ).
- PLATFORM: The device platform. Valid values are ANDROID or IOS.
- OS_VERSION: The operating system version (for example, 10.3.2).
- MODEL: The device model (for example, iPad 5th Gen).
- AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
- FORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.
- MANUFACTURER: The device manufacturer (for example, Apple).
- REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
- REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) , this attribute is ignored.
- INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
- INSTANCE_LABELS: The label of the device instance.
- FLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.
- Operator: The filter operator.
- The EQUALS operator is available for every attribute except INSTANCE_LABELS.
- The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
- The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
- The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.
- Values: An array of one or more filter values.
- The IN and NOT_IN operators take a values array that has one or more elements.
- The other operators require an array with a single element.
- In a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.

(structure)

Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the `deviceSelectionConfiguration` parameter to `ScheduleRun` . For an example of the JSON request syntax, see  ScheduleRun .

It is also passed in as the `filters` parameter to `ListDevices` . For an example of the JSON request syntax, see  ListDevices .

attribute -> (string)

The aspect of a device such as platform or model used as the selection criteria in a device filter.

The supported operators for each attribute are provided in the following list.

ARN

The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example` ).

Supported operators: `EQUALS` , `IN` , `NOT_IN`

PLATFORM

The device platform. Valid values are ANDROID or IOS.

Supported operators: `EQUALS`

OS_VERSION

The operating system version (for example, 10.3.2).

Supported operators: `EQUALS` , `GREATER_THAN` , `GREATER_THAN_OR_EQUALS` , `IN` , `LESS_THAN` , `LESS_THAN_OR_EQUALS` , `NOT_IN`

MODEL

The device model (for example, iPad 5th Gen).

Supported operators: `CONTAINS` , `EQUALS` , `IN` , `NOT_IN`

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.

Supported operators: `EQUALS`

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.

Supported operators: `EQUALS`

MANUFACTURER

The device manufacturer (for example, Apple).

Supported operators: `EQUALS` , `IN` , `NOT_IN`

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.

Supported operators: `EQUALS`

Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) , this filter is ignored.

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.

Supported operators: `EQUALS` , `IN` , `NOT_IN`

INSTANCE_LABELS

The label of the device instance.

Supported operators: `CONTAINS`

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.

Supported operators: `EQUALS`

operator -> (string)

Specifies how Device Farm compares the filterâs attribute to the value. See the attribute descriptions.

values -> (list)

An array of one or more filter values used in a device filter.

**Operator Values**

- The IN and NOT_IN operators can take a values array that has more than one element.
- The other operators require an array with a single element.

**Attribute Values**

- The PLATFORM attribute can be set to ANDROID or IOS.
- The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
- The FORM_FACTOR attribute can be set to PHONE or TABLET.
- The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.

(string)

Shorthand Syntax:

```
attribute=string,operator=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "attribute": "ARN"|"PLATFORM"|"OS_VERSION"|"MODEL"|"AVAILABILITY"|"FORM_FACTOR"|"MANUFACTURER"|"REMOTE_ACCESS_ENABLED"|"REMOTE_DEBUG_ENABLED"|"INSTANCE_ARN"|"INSTANCE_LABELS"|"FLEET_TYPE",
    "operator": "EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS"|"GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"IN"|"NOT_IN"|"CONTAINS",
    "values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

devices -> (list)

Information about the devices.

(structure)

Represents a device type that an app is tested against.

arn -> (string)

The deviceâs ARN.

name -> (string)

The deviceâs display name.

manufacturer -> (string)

The deviceâs manufacturer name.

model -> (string)

The deviceâs model name.

modelId -> (string)

The deviceâs model ID.

formFactor -> (string)

The deviceâs form factor.

Allowed values include:

- PHONE
- TABLET

platform -> (string)

The deviceâs platform.

Allowed values include:

- ANDROID
- IOS

os -> (string)

The deviceâs operating system type.

cpu -> (structure)

Information about the deviceâs CPU.

frequency -> (string)

The CPUâs frequency.

architecture -> (string)

The CPUâs architecture (for example, x86 or ARM).

clock -> (double)

The clock speed of the deviceâs CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.

resolution -> (structure)

The resolution of the device.

width -> (integer)

The screen resolutionâs width, expressed in pixels.

height -> (integer)

The screen resolutionâs height, expressed in pixels.

heapSize -> (long)

The deviceâs heap size, expressed in bytes.

memory -> (long)

The deviceâs total memory size, expressed in bytes.

image -> (string)

The deviceâs image name.

carrier -> (string)

The deviceâs carrier.

radio -> (string)

The deviceâs radio.

remoteAccessEnabled -> (boolean)

Specifies whether remote access has been enabled for the specified device.

remoteDebugEnabled -> (boolean)

This flag is set to `true` if remote debugging is enabled for the device.

Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) .

fleetType -> (string)

The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.

fleetName -> (string)

The name of the fleet to which this device belongs.

instances -> (list)

The instances that belong to this device.

(structure)

Represents the device instance.

arn -> (string)

The Amazon Resource Name (ARN) of the device instance.

deviceArn -> (string)

The ARN of the device.

labels -> (list)

An array of strings that describe the device instance.

(string)

status -> (string)

The status of the device instance. Valid values are listed here.

udid -> (string)

Unique device identifier for the device instance.

instanceProfile -> (structure)

A object that contains information about the instance profile.

arn -> (string)

The Amazon Resource Name (ARN) of the instance profile.

packageCleanup -> (boolean)

When set to `true` , Device Farm removes app packages after a test run. The default value is `false` for private devices.

excludeAppPackagesFromCleanup -> (list)

An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.

The list of packages is considered only if you set `packageCleanup` to `true` .

(string)

rebootAfterUse -> (boolean)

When set to `true` , Device Farm reboots the instance after a test run. The default value is `true` .

name -> (string)

The name of the instance profile.

description -> (string)

The description of the instance profile.

availability -> (string)

Indicates how likely a device is available for a test run. Currently available in the  ListDevices and GetDevice API methods.

nextToken -> (string)

If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.