# update-job-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/update-job-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot-jobs-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/index.html#cli-aws-iot-jobs-data) ]

# update-job-execution

## Description

Updates the status of a job execution.

Requires permission to access the [UpdateJobExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotjobsdataplane.html) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-jobs-data-2017-09-29/UpdateJobExecution)

## Synopsis

```
update-job-execution
--job-id <value>
--thing-name <value>
--status <value>
[--status-details <value>]
[--step-timeout-in-minutes <value>]
[--expected-version <value>]
[--include-job-execution-state | --no-include-job-execution-state]
[--include-job-document | --no-include-job-document]
[--execution-number <value>]
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

The unique identifier assigned to this job when it was created.

`--thing-name` (string)

The name of the thing associated with the device.

`--status` (string)

The new status for the job execution (IN_PROGRESS, FAILED, SUCCESS, or REJECTED). This must be specified on every update.

Possible values:

- `QUEUED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `TIMED_OUT`
- `REJECTED`
- `REMOVED`
- `CANCELED`

`--status-details` (map)

Optional. A collection of name/value pairs that describe the status of the job execution. If not specified, the statusDetails are unchanged.

The maximum length of the value in the name/value pair is 1,024 characters.

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

`--step-timeout-in-minutes` (long)

Specifies the amount of time this device has to finish execution of this job. If the job execution status is not set to a terminal state before this timer expires, or before the timer is reset (by again calling `UpdateJobExecution` , setting the status to `IN_PROGRESS` , and specifying a new timeout value in this field) the job execution status will be automatically set to `TIMED_OUT` . Note that setting or resetting the step timeout has no effect on the in progress timeout that may have been specified when the job was created (`CreateJob` using field `timeoutConfig` ).

Valid values for this parameter range from 1 to 10080 (1 minute to 7 days). A value of -1 is also valid and will cancel the current step timer (created by an earlier use of `UpdateJobExecutionRequest` ).

`--expected-version` (long)

Optional. The expected current version of the job execution. Each time you update the job execution, its version is incremented. If the version of the job execution stored in Jobs does not match, the update is rejected with a VersionMismatch error, and an ErrorResponse that contains the current job execution status data is returned. (This makes it unnecessary to perform a separate DescribeJobExecution request in order to obtain the job execution status data.)

`--include-job-execution-state` | `--no-include-job-execution-state` (boolean)

Optional. When included and set to true, the response contains the JobExecutionState data. The default is false.

`--include-job-document` | `--no-include-job-document` (boolean)

Optional. When set to true, the response contains the job document. The default is false.

`--execution-number` (long)

Optional. A number that identifies a particular job execution on a particular device.

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

**To update the status of a job execution**

The following `update-job-execution` example updates the status of the specified job and thing.

```
aws iot-jobs-data update-job-execution \
    --job-id SampleJob \
    --thing-name MotionSensor1 \
    --status REMOVED \
    --endpoint-url https://1234567890abcd.jobs.iot.us-west-2.amazonaws.com
```

Output:

```
{
    "executionState": {
        "status": "REMOVED",
        "versionNumber": 3
    },
}
```

For more information, see [Devices and Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html) in the *AWS IoT Developer Guide*.

## Output

executionState -> (structure)

A JobExecutionState object.

status -> (string)

The status of the job execution. Can be one of: âQUEUEDâ, âIN_PROGRESSâ, âFAILEDâ, âSUCCESSâ, âCANCELEDâ, âTIMED_OUTâ, âREJECTEDâ, or âREMOVEDâ.

statusDetails -> (map)

A collection of name/value pairs that describe the status of the job execution.

The maximum length of the value in the name/value pair is 1,024 characters.

key -> (string)

value -> (string)

versionNumber -> (long)

The version of the job execution. Job execution versions are incremented each time they are updated by a device.

jobDocument -> (string)

The contents of the Job Documents.