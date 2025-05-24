# describe-job-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# describe-job-template

## Description

Returns information about a job template.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJobTemplate)

## Synopsis

```
describe-job-template
--job-template-id <value>
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

`--job-template-id` (string)

The unique identifier of the job template.

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

jobTemplateArn -> (string)

The ARN of the job template.

jobTemplateId -> (string)

The unique identifier of the job template.

description -> (string)

A description of the job template.

documentSource -> (string)

An S3 link to the job document.

document -> (string)

The job document.

createdAt -> (timestamp)

The time, in seconds since the epoch, when the job template was created.

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

The criteria that determine when and how a job abort takes place.

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

timeoutConfig -> (structure)

Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT` .

inProgressTimeoutInMinutes -> (long)

Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer canât be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal `TIMED_OUT` status.

jobExecutionsRetryConfig -> (structure)

The configuration that determines how many retries are allowed for each failure type for a job.

criteriaList -> (list)

The list of criteria that determines how many retries are allowed for each failure type for a job.

(structure)

The criteria that determines how many retries are allowed for each failure type for a job.

failureType -> (string)

The type of job execution failures that can initiate a job retry.

numberOfRetries -> (integer)

The number of retries allowed for a failure type for the job.

maintenanceWindows -> (list)

Allows you to configure an optional maintenance window for the rollout of a job document to all devices in the target group for a job.

(structure)

An optional configuration within the `SchedulingConfig` to setup a recurring maintenance window with a predetermined start time and duration for the rollout of a job document to all devices in a target group for a job.

startTime -> (string)

Displays the start time of the next maintenance window.

durationInMinutes -> (integer)

Displays the duration of the next maintenance window.

destinationPackageVersions -> (list)

The package version Amazon Resource Names (ARNs) that are installed on the device when the job successfully completes. The package version must be in either the Published or Deprecated state when the job deploys. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle) .

**Note:** The following Length Constraints relates to a single ARN. Up to 25 package version ARNs are allowed.

(string)