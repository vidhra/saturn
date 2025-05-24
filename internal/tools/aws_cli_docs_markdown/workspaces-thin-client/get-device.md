# get-deviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/get-device.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/get-device.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces-thin-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/index.html#cli-aws-workspaces-thin-client) ]

# get-device

## Description

Returns information for a thin client device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-thin-client-2023-08-22/GetDevice)

## Synopsis

```
get-device
--id <value>
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

`--id` (string)

The ID of the device for which to return information.

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

device -> (structure)

Describes an device.

id -> (string)

The ID of the device.

serialNumber -> (string)

The hardware serial number of the device.

name -> (string)

The name of the device.

model -> (string)

The model number of the device.

environmentId -> (string)

The ID of the environment the device is associated with.

status -> (string)

The status of the device.

currentSoftwareSetId -> (string)

The ID of the software set currently installed on the device.

currentSoftwareSetVersion -> (string)

The version of the software set currently installed on the device.

desiredSoftwareSetId -> (string)

The ID of the software set which the device has been set to.

pendingSoftwareSetId -> (string)

The ID of the software set that is pending to be installed on the device.

pendingSoftwareSetVersion -> (string)

The version of the software set that is pending to be installed on the device.

softwareSetUpdateSchedule -> (string)

An option to define if software updates should be applied within a maintenance window.

softwareSetComplianceStatus -> (string)

Describes if the software currently installed on the device is a supported version.

softwareSetUpdateStatus -> (string)

Describes if the device has a supported version of software installed.

lastConnectedAt -> (timestamp)

The timestamp of the most recent session on the device.

lastPostureAt -> (timestamp)

The timestamp of the most recent check-in of the device.

createdAt -> (timestamp)

The timestamp of when the device was created.

updatedAt -> (timestamp)

The timestamp of when the device was updated.

arn -> (string)

The Amazon Resource Name (ARN) of the device.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service key used to encrypt the device.

tags -> (map)

The tag keys and optional values for the resource.

key -> (string)

value -> (string)