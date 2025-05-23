# stop-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/stop-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# stop-run

## Description

Initiates a stop request for the current test run. AWS Device Farm immediately stops the run on devices where tests have not started. You are not billed for these devices. On devices where tests have started executing, setup suite and teardown suite tests run to completion on those devices. You are billed for setup, teardown, and any tests that were in progress or already completed.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/StopRun)

## Synopsis

```
stop-run
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

Represents the Amazon Resource Name (ARN) of the Device Farm run to stop.

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

run -> (structure)

The run that was stopped.

arn -> (string)

The runâs ARN.

name -> (string)

The runâs name.

type -> (string)

The runâs type.

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

platform -> (string)

The runâs platform.

Allowed values include:

- ANDROID
- IOS

created -> (timestamp)

When the run was created.

status -> (string)

The runâs status.

Allowed values include:

- PENDING
- PENDING_CONCURRENCY
- PENDING_DEVICE
- PROCESSING
- SCHEDULING
- PREPARING
- RUNNING
- COMPLETED
- STOPPING

result -> (string)

The runâs result.

Allowed values include:

- PENDING
- PASSED
- WARNED
- FAILED
- SKIPPED
- ERRORED
- STOPPED

started -> (timestamp)

The runâs start time.

stopped -> (timestamp)

The runâs stop time.

counters -> (structure)

The runâs result counters.

total -> (integer)

The total number of entities.

passed -> (integer)

The number of passed entities.

failed -> (integer)

The number of failed entities.

warned -> (integer)

The number of warned entities.

errored -> (integer)

The number of errored entities.

stopped -> (integer)

The number of stopped entities.

skipped -> (integer)

The number of skipped entities.

message -> (string)

A message about the runâs result.

totalJobs -> (integer)

The total number of jobs for the run.

completedJobs -> (integer)

The total number of completed jobs.

billingMethod -> (string)

Specifies the billing method for a test run: `metered` or `unmetered` . If the parameter is not specified, the default value is `metered` .

### Note

If you have unmetered device slots, you must set this to `unmetered` to use them. Otherwise, the run is counted toward metered device minutes.

deviceMinutes -> (structure)

Represents the total (metered or unmetered) minutes used by the test run.

total -> (double)

When specified, represents the total minutes used by the resource to run tests.

metered -> (double)

When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered -> (double)

When specified, represents only the sum of unmetered minutes used by the resource to run tests.

networkProfile -> (structure)

The network profile being used for a test run.

arn -> (string)

The Amazon Resource Name (ARN) of the network profile.

name -> (string)

The name of the network profile.

description -> (string)

The description of the network profile.

type -> (string)

The type of network profile. Valid values are listed here.

uplinkBandwidthBits -> (long)

The data throughput rate in bits per second, as an integer from 0 to 104857600.

downlinkBandwidthBits -> (long)

The data throughput rate in bits per second, as an integer from 0 to 104857600.

uplinkDelayMs -> (long)

Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

downlinkDelayMs -> (long)

Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.

uplinkJitterMs -> (long)

Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

downlinkJitterMs -> (long)

Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.

uplinkLossPercent -> (integer)

Proportion of transmitted packets that fail to arrive from 0 to 100 percent.

downlinkLossPercent -> (integer)

Proportion of received packets that fail to arrive from 0 to 100 percent.

deviceProxy -> (structure)

The device proxy configured for the devices in the run.

host -> (string)

Hostname or IPv4 address of the proxy.

port -> (integer)

The port number on which the http/s proxy is listening.

parsingResultUrl -> (string)

Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesnât parse, the reason why it doesnât parse appears in the file that this URL points to.

resultCode -> (string)

Supporting field for the result field. Set only if `result` is `SKIPPED` . `PARSING_FAILED` if the result is skipped because of test package parsing failure.

seed -> (integer)

For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.

appUpload -> (string)

An app to upload or that has been uploaded.

eventCount -> (integer)

For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.

jobTimeoutMinutes -> (integer)

The number of minutes the job executes before it times out.

devicePoolArn -> (string)

The ARN of the device pool for the run.

locale -> (string)

Information about the locale that is used for the run.

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

location -> (structure)

Information about the location that is used for the run.

latitude -> (double)

The latitude.

longitude -> (double)

The longitude.

customerArtifactPaths -> (structure)

Output `CustomerArtifactPaths` object for the test run.

iosPaths -> (list)

Comma-separated list of paths on the iOS device where the artifacts generated by the customerâs tests are pulled from.

(string)

androidPaths -> (list)

Comma-separated list of paths on the Android device where the artifacts generated by the customerâs tests are pulled from.

(string)

deviceHostPaths -> (list)

Comma-separated list of paths in the test execution environment where the artifacts generated by the customerâs tests are pulled from.

(string)

webUrl -> (string)

The Device Farm console URL for the recording of the run.

skipAppResign -> (boolean)

When set to `true` , for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.

For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs* .

testSpecArn -> (string)

The ARN of the YAML-formatted test specification for the run.

deviceSelectionResult -> (structure)

The results of a device filter used to select the devices for a test run.

filters -> (list)

The filters in a device selection result.

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

matchedDevicesCount -> (integer)

The number of devices that matched the device filter selection criteria.

maxDevices -> (integer)

The maximum number of devices to be selected by a device filter and included in a test run.

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