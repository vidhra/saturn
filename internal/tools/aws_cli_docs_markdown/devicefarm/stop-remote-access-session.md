# stop-remote-access-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-remote-access-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-remote-access-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# stop-remote-access-session

## Description

Ends a specified remote access session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRemoteAccessSession)

## Synopsis

```
stop-remote-access-session
--arn <value>
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

`--arn` (string)

The Amazon Resource Name (ARN) of the remote access session to stop.

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

remoteAccessSession -> (structure)

A container that represents the metadata from the service about the remote access session you are stopping.

arn -> (string)

The Amazon Resource Name (ARN) of the remote access session.

name -> (string)

The name of the remote access session.

created -> (timestamp)

The date and time the remote access session was created.

status -> (string)

The status of the remote access session. Can be any of the following:

- PENDING.
- PENDING_CONCURRENCY.
- PENDING_DEVICE.
- PROCESSING.
- SCHEDULING.
- PREPARING.
- RUNNING.
- COMPLETED.
- STOPPING.

result -> (string)

The result of the remote access session. Can be any of the following:

- PENDING.
- PASSED.
- WARNED.
- FAILED.
- SKIPPED.
- ERRORED.
- STOPPED.

message -> (string)

A message about the remote access session.

started -> (timestamp)

The date and time the remote access session was started.

stopped -> (timestamp)

The date and time the remote access session was stopped.

device -> (structure)

The device (phone or tablet) used in the remote access session.

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

instanceArn -> (string)

The ARN of the instance.

remoteDebugEnabled -> (boolean)

This flag is set to `true` if remote debugging is enabled for the remote access session.

Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) .

remoteRecordEnabled -> (boolean)

This flag is set to `true` if remote recording is enabled for the remote access session.

remoteRecordAppArn -> (string)

The ARN for the app to be recorded in the remote access session.

hostAddress -> (string)

IP address of the EC2 host where you need to connect to remotely debug devices. Only returned if remote debugging is enabled for the remote access session.

Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) .

clientId -> (string)

Unique identifier of your client for the remote access session. Only returned if remote debugging is enabled for the remote access session.

Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) .

billingMethod -> (string)

The billing method of the remote access session. Possible values include `METERED` or `UNMETERED` . For more information about metered devices, see [AWS Device Farm terminology](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology) .

deviceMinutes -> (structure)

The number of minutes a device is used in a remote access session (including setup and teardown minutes).

total -> (double)

When specified, represents the total minutes used by the resource to run tests.

metered -> (double)

When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered -> (double)

When specified, represents only the sum of unmetered minutes used by the resource to run tests.

endpoint -> (string)

The endpoint for the remote access sesssion.

deviceUdid -> (string)

Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.

Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html) .

interactionMode -> (string)

The interaction mode of the remote access session. Valid values are:

- INTERACTIVE: You can interact with the iOS device by viewing, touching, and rotating the screen. You cannot run XCUITest framework-based tests in this mode.
- NO_VIDEO: You are connected to the device, but cannot interact with it or view the screen. This mode has the fastest test execution speed. You can run XCUITest framework-based tests in this mode.
- VIDEO_ONLY: You can view the screen, but cannot touch or rotate it. You can run XCUITest framework-based tests and watch the screen in this mode.

skipAppResign -> (boolean)

When set to `true` , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.

For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs* .

vpcConfig -> (structure)

The VPC security groups and subnets that are attached to a project.

securityGroupIds -> (list)

An array of one or more security groups IDs in your Amazon VPC.

(string)

subnetIds -> (list)

An array of one or more subnet IDs in your Amazon VPC.

(string)

vpcId -> (string)

The ID of the Amazon VPC.

deviceProxy -> (structure)

The device proxy configured for the remote access session.

host -> (string)

Hostname or IPv4 address of the proxy.

port -> (integer)

The port number on which the http/s proxy is listening.