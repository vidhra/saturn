# create-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# create-job

## Description

Creates a job.

Requires permission to access the [CreateJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateJob)

## Synopsis

```
create-job
--job-id <value>
--targets <value>
[--document-source <value>]
[--document <value>]
[--description <value>]
[--presigned-url-config <value>]
[--target-selection <value>]
[--job-executions-rollout-config <value>]
[--abort-config <value>]
[--timeout-config <value>]
[--tags <value>]
[--namespace-id <value>]
[--job-template-arn <value>]
[--job-executions-retry-config <value>]
[--document-parameters <value>]
[--scheduling-config <value>]
[--destination-package-versions <value>]
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

`--job-id` (string)

A job identifier which must be unique for your account. We recommend using a UUID. Alpha-numeric characters, â-â and â_â are valid for use here.

`--targets` (list)

A list of things and thing groups to which the job should be sent.

(string)

Syntax:

```
"string" "string" ...
```

`--document-source` (string)

An S3 link, or S3 object URL, to the job document. The link is an Amazon S3 object URL and is required if you donât specify a value for `document` .

For example, `--document-source https://s3.*region-code* .amazonaws.com/example-firmware/device-firmware.1.0`

For more information, see [Methods for accessing a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-bucket-intro.html) .

`--document` (string)

The job document. Required if you donât specify a value for `documentSource` .

`--description` (string)

A short text description of the job.

`--presigned-url-config` (structure)

Configuration information for pre-signed S3 URLs.

roleArn -> (string)

The ARN of an IAM role that grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.

### Warning

For information about addressing the confused deputy problem, see [cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html) in the *Amazon Web Services IoT Core developer guide* .

expiresInSec -> (long)

How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

Shorthand Syntax:

```
roleArn=string,expiresInSec=long
```

JSON Syntax:

```
{
  "roleArn": "string",
  "expiresInSec": long
}
```

`--target-selection` (string)

Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

### Note

We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.

Possible values:

- `CONTINUOUS`
- `SNAPSHOT`

`--job-executions-rollout-config` (structure)

Allows you to create a staged rollout of the job.

maximumPerMinute -> (integer)

The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.

exponentialRate -> (structure)

The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.

baseRatePerMinute -> (integer)

The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.

incrementFactor -> (double)

The exponential factor to increase the rate of rollout for a job.

Amazon Web Services IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).

rateIncreaseCriteria -> (structure)

The criteria to initiate the increase in rate of rollout for a job.

numberOfNotifiedThings -> (integer)

The threshold for number of notified things that will initiate the increase in rate of rollout.

numberOfSucceededThings -> (integer)

The threshold for number of succeeded things that will initiate the increase in rate of rollout.

Shorthand Syntax:

```
maximumPerMinute=integer,exponentialRate={baseRatePerMinute=integer,incrementFactor=double,rateIncreaseCriteria={numberOfNotifiedThings=integer,numberOfSucceededThings=integer}}
```

JSON Syntax:

```
{
  "maximumPerMinute": integer,
  "exponentialRate": {
    "baseRatePerMinute": integer,
    "incrementFactor": double,
    "rateIncreaseCriteria": {
      "numberOfNotifiedThings": integer,
      "numberOfSucceededThings": integer
    }
  }
}
```

`--abort-config` (structure)

Allows you to create the criteria to abort a job.

criteriaList -> (list)

The list of criteria that determine when and how to abort the job.

(structure)

The criteria that determine when and how a job abort takes place.

failureType -> (string)

The type of job execution failures that can initiate a job abort.

action -> (string)

The type of job action to take to initiate the job abort.

thresholdPercentage -> (double)

The minimum percentage of job execution failures that must occur to initiate the job abort.

Amazon Web Services IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).

minNumberOfExecutedThings -> (integer)

The minimum number of things which must receive job execution notifications before the job can be aborted.

Shorthand Syntax:

```
criteriaList=[{failureType=string,action=string,thresholdPercentage=double,minNumberOfExecutedThings=integer},{failureType=string,action=string,thresholdPercentage=double,minNumberOfExecutedThings=integer}]
```

JSON Syntax:

```
{
  "criteriaList": [
    {
      "failureType": "FAILED"|"REJECTED"|"TIMED_OUT"|"ALL",
      "action": "CANCEL",
      "thresholdPercentage": double,
      "minNumberOfExecutedThings": integer
    }
    ...
  ]
}
```

`--timeout-config` (structure)

Specifies the amount of time each device has to finish its execution of the job. The timer is started when the job execution status is set to `IN_PROGRESS` . If the job execution status is not set to another terminal state before the time expires, it will be automatically set to `TIMED_OUT` .

inProgressTimeoutInMinutes -> (long)

Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer canât be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal `TIMED_OUT` status.

Shorthand Syntax:

```
inProgressTimeoutInMinutes=long
```

JSON Syntax:

```
{
  "inProgressTimeoutInMinutes": long
}
```

`--tags` (list)

Metadata which can be used to manage the job.

(structure)

A set of key/value pairs that are used to manage the resource.

Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--namespace-id` (string)

The namespace used to indicate that a job is a customer-managed job.

When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.

`$aws/things/*THING_NAME* /jobs/*JOB_ID* /notify-namespace-*NAMESPACE_ID* /`

### Note

The `namespaceId` feature is only supported by IoT Greengrass at this time. For more information, see [Setting up IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)

`--job-template-arn` (string)

The ARN of the job template used to create the job.

`--job-executions-retry-config` (structure)

Allows you to create the criteria to retry a job.

criteriaList -> (list)

The list of criteria that determines how many retries are allowed for each failure type for a job.

(structure)

The criteria that determines how many retries are allowed for each failure type for a job.

failureType -> (string)

The type of job execution failures that can initiate a job retry.

numberOfRetries -> (integer)

The number of retries allowed for a failure type for the job.

Shorthand Syntax:

```
criteriaList=[{failureType=string,numberOfRetries=integer},{failureType=string,numberOfRetries=integer}]
```

JSON Syntax:

```
{
  "criteriaList": [
    {
      "failureType": "FAILED"|"TIMED_OUT"|"ALL",
      "numberOfRetries": integer
    }
    ...
  ]
}
```

`--document-parameters` (map)

Parameters of an Amazon Web Services managed template that you can specify to create the job document.

### Note

`documentParameters` can only be used when creating jobs from Amazon Web Services managed templates. This parameter canât be used with custom job templates or to create jobs from them.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--scheduling-config` (structure)

The configuration that allows you to schedule a job for a future date and time in addition to specifying the end behavior for each job execution.

startTime -> (string)

The time a job will begin rollout of the job document to all devices in the target group for a job. The `startTime` can be scheduled up to a year in advance and must be scheduled a minimum of thirty minutes from the current time. The date and time format for the `startTime` is YYYY-MM-DD for the date and HH:MM for the time.

For more information on the syntax for `startTime` when using an API command or the Command Line Interface, see [Timestamp](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp) .

endTime -> (string)

The time a job will stop rollout of the job document to all devices in the target group for a job. The `endTime` must take place no later than two years from the current time and be scheduled a minimum of thirty minutes from the current time. The minimum duration between `startTime` and `endTime` is thirty minutes. The maximum duration between `startTime` and `endTime` is two years. The date and time format for the `endTime` is YYYY-MM-DD for the date and HH:MM for the time.

For more information on the syntax for `endTime` when using an API command or the Command Line Interface, see [Timestamp](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp) .

endBehavior -> (string)

Specifies the end behavior for all job executions after a job reaches the selected `endTime` . If `endTime` is not selected when creating the job, then `endBehavior` does not apply.

maintenanceWindows -> (list)

An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.

(structure)

An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.

startTime -> (string)

Displays the start time of the next maintenance window.

durationInMinutes -> (integer)

Displays the duration of the next maintenance window.

Shorthand Syntax:

```
startTime=string,endTime=string,endBehavior=string,maintenanceWindows=[{startTime=string,durationInMinutes=integer},{startTime=string,durationInMinutes=integer}]
```

JSON Syntax:

```
{
  "startTime": "string",
  "endTime": "string",
  "endBehavior": "STOP_ROLLOUT"|"CANCEL"|"FORCE_CANCEL",
  "maintenanceWindows": [
    {
      "startTime": "string",
      "durationInMinutes": integer
    }
    ...
  ]
}
```

`--destination-package-versions` (list)

The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle) .

**Note:** The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create a job**

The following `create-job` example creates a simple AWS IoT job that sends a JSON document to the `MyRaspberryPi` device.

```
aws iot create-job \
    --job-id "example-job-01" \
    --targets "arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi" \
    --document file://example-job.json \
    --description "example job test" \
    --target-selection SNAPSHOT
```

Output:

```
{
    "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01",
    "jobId": "example-job-01",
    "description": "example job test"
}
```

**Example 2: To create a continuous job**

The following `create-job` example creates a job that continues to run after the things specified as targets have completed the job. In this example, the target is a thing group, so when new devices are added to the group, the continuous job runs on those new things.

**aws iot create-job**:
âjob-id âexample-job-04â âtargets âarn:aws:iot:us-west-2:123456789012:thinggroup/DeadBulbsâ âdocument file://example-job.json âdescription âexample continuous jobâ âtarget-selection CONTINUOUS

Output:

```
{
    "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-04",
    "jobId": "example-job-04",
    "description": "example continuous job"
}
```

For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html) in the *AWS IoT Developer Guide*.

## Output

jobArn -> (string)

The job ARN.

jobId -> (string)

The unique identifier you assigned to this job.

description -> (string)

The job description.