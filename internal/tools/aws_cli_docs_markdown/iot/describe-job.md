# describe-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# describe-job

## Description

Describes a job.

Requires permission to access the [DescribeJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJob)

## Synopsis

```
describe-job
--job-id <value>
[--before-substitution | --no-before-substitution]
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

The unique identifier you assigned to this job when it was created.

`--before-substitution` | `--no-before-substitution` (boolean)

Provides a view of the job document before and after the substitution parameters have been resolved with their exact values.

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

**To get detailed status for a job**

The following `describe-job` example gets detailed status for the job whose ID is `example-job-01`.

```
aws iot describe-job \
    --job-id "example-job-01"
```

Output:

```
{
    "job": {
        "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01",
        "jobId": "example-job-01",
        "targetSelection": "SNAPSHOT",
        "status": "IN_PROGRESS",
        "targets": [
            "arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi"
        ],
        "description": "example job test",
        "presignedUrlConfig": {},
        "jobExecutionsRolloutConfig": {},
        "createdAt": 1560787022.733,
        "lastUpdatedAt": 1560787026.294,
        "jobProcessDetails": {
            "numberOfCanceledThings": 0,
            "numberOfSucceededThings": 0,
            "numberOfFailedThings": 0,
            "numberOfRejectedThings": 0,
            "numberOfQueuedThings": 1,
            "numberOfInProgressThings": 0,
            "numberOfRemovedThings": 0,
            "numberOfTimedOutThings": 0
        },
        "timeoutConfig": {}
    }
}
```

For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html) in the *AWS IoT Developer Guide*.

## Output

documentSource -> (string)

An S3 link to the job document.

job -> (structure)

Information about the job.

jobArn -> (string)

An ARN identifying the job with format âarn:aws:iot:region:account:job/jobIdâ.

jobId -> (string)

The unique identifier you assigned to this job when it was created.

targetSelection -> (string)

Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group.

### Note

We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.

status -> (string)

The status of the job, one of `IN_PROGRESS` , `CANCELED` , `DELETION_IN_PROGRESS` or `COMPLETED` .

forceCanceled -> (boolean)

Will be `true` if the job was canceled with the optional `force` parameter set to `true` .

reasonCode -> (string)

If the job was updated, provides the reason code for the update.

comment -> (string)

If the job was updated, describes the reason for the update.

targets -> (list)

A list of IoT things and thing groups to which the job should be sent.

(string)

description -> (string)

A short text description of the job.

presignedUrlConfig -> (structure)

Configuration for pre-signed S3 URLs.

roleArn -> (string)

The ARN of an IAM role that grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.

### Warning

For information about addressing the confused deputy problem, see [cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html) in the *Amazon Web Services IoT Core developer guide* .

expiresInSec -> (long)

How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

jobExecutionsRolloutConfig -> (structure)

Allows you to create a staged rollout of a job.

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

abortConfig -> (structure)

Configuration for criteria to abort the job.

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

createdAt -> (timestamp)

The time, in seconds since the epoch, when the job was created.

lastUpdatedAt -> (timestamp)

The time, in seconds since the epoch, when the job was last updated.

completedAt -> (timestamp)

The time, in seconds since the epoch, when the job was completed.

jobProcessDetails -> (structure)

Details about the job process.

processingTargets -> (list)

The target devices to which the job execution is being rolled out. This value will be null after the job execution has finished rolling out to all the target devices.

(string)

numberOfCanceledThings -> (integer)

The number of things that cancelled the job.

numberOfSucceededThings -> (integer)

The number of things which successfully completed the job.

numberOfFailedThings -> (integer)

The number of things that failed executing the job.

numberOfRejectedThings -> (integer)

The number of things that rejected the job.

numberOfQueuedThings -> (integer)

The number of things that are awaiting execution of the job.

numberOfInProgressThings -> (integer)

The number of things currently executing the job.

numberOfRemovedThings -> (integer)

The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.

numberOfTimedOutThings -> (integer)

The number of things whose job execution status is `TIMED_OUT` .

timeoutConfig -> (structure)

Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT` .

inProgressTimeoutInMinutes -> (long)

Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer canât be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal `TIMED_OUT` status.

namespaceId -> (string)

The namespace used to indicate that a job is a customer-managed job.

When you specify a value for this parameter, Amazon Web Services IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.

`$aws/things/*THING_NAME* /jobs/*JOB_ID* /notify-namespace-*NAMESPACE_ID* /`

### Note

The `namespaceId` feature is only supported by IoT Greengrass at this time. For more information, see [Setting up IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)

jobTemplateArn -> (string)

The ARN of the job template used to create the job.

jobExecutionsRetryConfig -> (structure)

The configuration for the criteria to retry the job.

criteriaList -> (list)

The list of criteria that determines how many retries are allowed for each failure type for a job.

(structure)

The criteria that determines how many retries are allowed for each failure type for a job.

failureType -> (string)

The type of job execution failures that can initiate a job retry.

numberOfRetries -> (integer)

The number of retries allowed for a failure type for the job.

documentParameters -> (map)

A key-value map that pairs the patterns that need to be replaced in a managed template job document schema. You can use the description of each key as a guidance to specify the inputs during runtime when creating a job.

### Note

`documentParameters` can only be used when creating jobs from Amazon Web Services managed templates. This parameter canât be used with custom job templates or to create jobs from them.

key -> (string)

value -> (string)

isConcurrent -> (boolean)

Indicates whether a job is concurrent. Will be true when a job is rolling out new job executions or canceling previously created executions, otherwise false.

schedulingConfig -> (structure)

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

scheduledJobRollouts -> (list)

Displays the next seven maintenance window occurrences and their start times.

(structure)

Displays the next seven maintenance window occurrences and their start times.

startTime -> (string)

Displays the start times of the next seven maintenance window occurrences.

destinationPackageVersions -> (list)

The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle) .The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle) .

**Note:** The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.

(string)