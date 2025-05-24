# get-device-pool-compatibilityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool-compatibility.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool-compatibility.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# get-device-pool-compatibility

## Description

Gets information about compatibility with a device pool.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetDevicePoolCompatibility)

## Synopsis

```
get-device-pool-compatibility
--device-pool-arn <value>
[--app-arn <value>]
[--test-type <value>]
[--test <value>]
[--configuration <value>]
[--project-arn <value>]
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

`--device-pool-arn` (string)

The device poolâs ARN.

`--app-arn` (string)

The ARN of the app that is associated with the specified device pool.

`--test-type` (string)

The test type for the specified device pool.

Allowed values include the following:

- BUILTIN_FUZZ.
- APPIUM_JAVA_JUNIT.
- APPIUM_JAVA_TESTNG.
- APPIUM_PYTHON.
- APPIUM_NODE.
- APPIUM_RUBY.
- APPIUM_WEB_JAVA_JUNIT.
- APPIUM_WEB_JAVA_TESTNG.
- APPIUM_WEB_PYTHON.
- APPIUM_WEB_NODE.
- APPIUM_WEB_RUBY.
- INSTRUMENTATION.
- XCTEST.
- XCTEST_UI.

Possible values:

- `BUILTIN_FUZZ`
- `APPIUM_JAVA_JUNIT`
- `APPIUM_JAVA_TESTNG`
- `APPIUM_PYTHON`
- `APPIUM_NODE`
- `APPIUM_RUBY`
- `APPIUM_WEB_JAVA_JUNIT`
- `APPIUM_WEB_JAVA_TESTNG`
- `APPIUM_WEB_PYTHON`
- `APPIUM_WEB_NODE`
- `APPIUM_WEB_RUBY`
- `INSTRUMENTATION`
- `XCTEST`
- `XCTEST_UI`

`--test` (structure)

Information about the uploaded test to be run against the device pool.

type -> (string)

The testâs type.

Must be one of the following values:

- BUILTIN_FUZZ
- APPIUM_JAVA_JUNIT
- APPIUM_JAVA_TESTNG
- APPIUM_PYTHON
- APPIUM_NODE
- APPIUM_RUBY
- APPIUM_WEB_JAVA_JUNIT
- APPIUM_WEB_JAVA_TESTNG
- APPIUM_WEB_PYTHON
- APPIUM_WEB_NODE
- APPIUM_WEB_RUBY
- INSTRUMENTATION
- XCTEST
- XCTEST_UI

testPackageArn -> (string)

The ARN of the uploaded test to be run.

testSpecArn -> (string)

The ARN of the YAML-formatted test specification.

filter -> (string)

The testâs filter.

parameters -> (map)

The testâs parameters, such as test framework parameters and fixture settings. Parameters are represented by name-value pairs of strings.

For all tests:

- `app_performance_monitoring` : Performance monitoring is enabled by default. Set this parameter to false to disable it.

For Appium tests (all types):

- appium_version: The Appium version. Currently supported values are 1.6.5 (and later), latest, and default.
- latest runs the latest Appium version supported by Device Farm (1.9.1).
- For default, Device Farm selects a compatible version of Appium for the device. The current behavior is to run 1.7.2 on Android devices and iOS 9 and earlier and 1.7.2 for iOS 10 and later.
- This behavior is subject to change.

For fuzz tests (Android only):

- event_count: The number of events, between 1 and 10000, that the UI fuzz test should perform.
- throttle: The time, in ms, between 0 and 1000, that the UI fuzz test should wait between events.
- seed: A seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

For Instrumentation:

- filter: A test filter string. Examples:
- Running a single test case: `com.android.abc.Test1`
- Running a single test: `com.android.abc.Test1#smoke`
- Running multiple tests: `com.android.abc.Test1,com.android.abc.Test2`

For XCTest and XCTestUI:

- filter: A test filter string. Examples:
- Running a single test class: `LoginTests`
- Running a multiple test classes: `LoginTests,SmokeTests`
- Running a single test: `LoginTests/testValid`
- Running multiple tests: `LoginTests/testValid,LoginTests/testInvalid`

key -> (string)

value -> (string)

Shorthand Syntax:

```
type=string,testPackageArn=string,testSpecArn=string,filter=string,parameters={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "type": "BUILTIN_FUZZ"|"APPIUM_JAVA_JUNIT"|"APPIUM_JAVA_TESTNG"|"APPIUM_PYTHON"|"APPIUM_NODE"|"APPIUM_RUBY"|"APPIUM_WEB_JAVA_JUNIT"|"APPIUM_WEB_JAVA_TESTNG"|"APPIUM_WEB_PYTHON"|"APPIUM_WEB_NODE"|"APPIUM_WEB_RUBY"|"INSTRUMENTATION"|"XCTEST"|"XCTEST_UI",
  "testPackageArn": "string",
  "testSpecArn": "string",
  "filter": "string",
  "parameters": {"string": "string"
    ...}
}
```

`--configuration` (structure)

An object that contains information about the settings for a run.

extraDataPackageArn -> (string)

The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the appâs sandbox for iOS.

networkProfileArn -> (string)

Reserved for internal use.

locale -> (string)

Information about the locale that is used for the run.

location -> (structure)

Information about the location that is used for the run.

latitude -> (double)

The latitude.

longitude -> (double)

The longitude.

vpceConfigurationArns -> (list)

An array of ARNs for your VPC endpoint configurations.

(string)

deviceProxy -> (structure)

The device proxy to be configured on the device for the run.

host -> (string)

Hostname or IPv4 address of the proxy.

port -> (integer)

The port number on which the http/s proxy is listening.

customerArtifactPaths -> (structure)

Input `CustomerArtifactPaths` object for the scheduled run configuration.

iosPaths -> (list)

Comma-separated list of paths on the iOS device where the artifacts generated by the customerâs tests are pulled from.

(string)

androidPaths -> (list)

Comma-separated list of paths on the Android device where the artifacts generated by the customerâs tests are pulled from.

(string)

deviceHostPaths -> (list)

Comma-separated list of paths in the test execution environment where the artifacts generated by the customerâs tests are pulled from.

(string)

radios -> (structure)

Information about the radio states for the run.

wifi -> (boolean)

True if Wi-Fi is enabled at the beginning of the test. Otherwise, false.

bluetooth -> (boolean)

True if Bluetooth is enabled at the beginning of the test. Otherwise, false.

nfc -> (boolean)

True if NFC is enabled at the beginning of the test. Otherwise, false.

gps -> (boolean)

True if GPS is enabled at the beginning of the test. Otherwise, false.

auxiliaryApps -> (list)

A list of upload ARNs for app packages to be installed with your app.

(string)

billingMethod -> (string)

Specifies the billing method for a test run: `metered` or `unmetered` . If the parameter is not specified, the default value is `metered` .

### Note

If you have purchased unmetered device slots, you must set this parameter to `unmetered` to make use of them. Otherwise, your run counts against your metered time.

Shorthand Syntax:

```
extraDataPackageArn=string,networkProfileArn=string,locale=string,location={latitude=double,longitude=double},vpceConfigurationArns=string,string,deviceProxy={host=string,port=integer},customerArtifactPaths={iosPaths=[string,string],androidPaths=[string,string],deviceHostPaths=[string,string]},radios={wifi=boolean,bluetooth=boolean,nfc=boolean,gps=boolean},auxiliaryApps=string,string,billingMethod=string
```

JSON Syntax:

```
{
  "extraDataPackageArn": "string",
  "networkProfileArn": "string",
  "locale": "string",
  "location": {
    "latitude": double,
    "longitude": double
  },
  "vpceConfigurationArns": ["string", ...],
  "deviceProxy": {
    "host": "string",
    "port": integer
  },
  "customerArtifactPaths": {
    "iosPaths": ["string", ...],
    "androidPaths": ["string", ...],
    "deviceHostPaths": ["string", ...]
  },
  "radios": {
    "wifi": true|false,
    "bluetooth": true|false,
    "nfc": true|false,
    "gps": true|false
  },
  "auxiliaryApps": ["string", ...],
  "billingMethod": "METERED"|"UNMETERED"
}
```

`--project-arn` (string)

The ARN of the project for which you want to check device pool compatibility.

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

compatibleDevices -> (list)

Information about compatible devices.

(structure)

Represents a device pool compatibility result.

device -> (structure)

The device (phone or tablet) to return information about.

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

compatible -> (boolean)

Whether the result was compatible with the device pool.

incompatibilityMessages -> (list)

Information about the compatibility.

(structure)

Represents information about incompatibility.

message -> (string)

A message about the incompatibility.

type -> (string)

The type of incompatibility.

Allowed values include:

- ARN
- FORM_FACTOR (for example, phone or tablet)
- MANUFACTURER
- PLATFORM (for example, Android or iOS)
- REMOTE_ACCESS_ENABLED
- APPIUM_VERSION

incompatibleDevices -> (list)

Information about incompatible devices.

(structure)

Represents a device pool compatibility result.

device -> (structure)

The device (phone or tablet) to return information about.

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

compatible -> (boolean)

Whether the result was compatible with the device pool.

incompatibilityMessages -> (list)

Information about the compatibility.

(structure)

Represents information about incompatibility.

message -> (string)

A message about the incompatibility.

type -> (string)

The type of incompatibility.

Allowed values include:

- ARN
- FORM_FACTOR (for example, phone or tablet)
- MANUFACTURER
- PLATFORM (for example, Android or iOS)
- REMOTE_ACCESS_ENABLED
- APPIUM_VERSION