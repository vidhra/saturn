# get-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/get-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/get-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces-thin-client](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-thin-client/index.html#cli-aws-workspaces-thin-client) ]

# get-environment

## Description

Returns information for an environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-thin-client-2023-08-22/GetEnvironment)

## Synopsis

```
get-environment
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

The ID of the environment for which to return information.

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

environment -> (structure)

Describes an environment.

id -> (string)

The ID of the environment.

name -> (string)

The name of the environment.

desktopArn -> (string)

The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or AppStream 2.0.

desktopEndpoint -> (string)

The URL for the identity provider login (only for environments that use AppStream 2.0).

desktopType -> (string)

The type of streaming desktop for the environment.

activationCode -> (string)

The activation code to register a device to the environment.

registeredDevicesCount -> (integer)

The number of devices registered to the environment.

softwareSetUpdateSchedule -> (string)

An option to define if software updates should be applied within a maintenance window.

maintenanceWindow -> (structure)

A specification for a time window to apply software updates.

type -> (string)

An option to select the default or custom maintenance window.

startTimeHour -> (integer)

The hour for the maintenance window start (`00` -`23` ).

startTimeMinute -> (integer)

The minutes past the hour for the maintenance window start (`00` -`59` ).

endTimeHour -> (integer)

The hour for the maintenance window end (`00` -`23` ).

endTimeMinute -> (integer)

The minutes for the maintenance window end (`00` -`59` ).

daysOfTheWeek -> (list)

The days of the week during which the maintenance window is open.

(string)

applyTimeOf -> (string)

The option to set the maintenance window during the device local time or Universal Coordinated Time (UTC).

softwareSetUpdateMode -> (string)

An option to define which software updates to apply.

desiredSoftwareSetId -> (string)

The ID of the software set to apply.

pendingSoftwareSetId -> (string)

The ID of the software set that is pending to be installed.

pendingSoftwareSetVersion -> (string)

The version of the software set that is pending to be installed.

softwareSetComplianceStatus -> (string)

Describes if the software currently installed on all devices in the environment is a supported version.

createdAt -> (timestamp)

The timestamp of when the environment was created.

updatedAt -> (timestamp)

The timestamp of when the device was updated.

arn -> (string)

The Amazon Resource Name (ARN) of the environment.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the Key Management Service key used to encrypt the environment.

tags -> (map)

The tag keys and optional values for the resource.

key -> (string)

value -> (string)

deviceCreationTags -> (map)

The tag keys and optional values for the newly created devices for this environment.

key -> (string)

value -> (string)