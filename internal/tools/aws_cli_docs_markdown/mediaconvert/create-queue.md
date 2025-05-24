# create-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediaconvert](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/index.html#cli-aws-mediaconvert) ]

# create-queue

## Description

Create a new transcoding queue. For information about queues, see Working With Queues in the User Guide at [https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/CreateQueue)

## Synopsis

```
create-queue
[--concurrent-jobs <value>]
[--description <value>]
--name <value>
[--pricing-plan <value>]
[--reservation-plan-settings <value>]
[--status <value>]
[--tags <value>]
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

`--concurrent-jobs` (integer)
Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead.

`--description` (string)
Optional. A description of the queue that you are creating.

`--name` (string)
The name of the queue that you are creating.

`--pricing-plan` (string)
Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. When you use the API to create a queue, the default is on-demand.

Possible values:

- `ON_DEMAND`
- `RESERVED`

`--reservation-plan-settings` (structure)
Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.Commitment -> (string)

The length of the term of your reserved queue pricing plan commitment.

RenewalType -> (string)

Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term. When your term is auto renewed, you extend your commitment by 12 months from the auto renew date. You can cancel this commitment.

ReservedSlots -> (integer)

Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. You canât decrease the number of RTS in your reserved queue. You can increase the number of RTS by extending your existing commitment with a new 12-month commitment for the larger number. The new commitment begins when you purchase the additional capacity. You canât cancel your commitment or revert to your original commitment after you increase the capacity.

Shorthand Syntax:

```
Commitment=string,RenewalType=string,ReservedSlots=integer
```

JSON Syntax:

```
{
  "Commitment": "ONE_YEAR",
  "RenewalType": "AUTO_RENEW"|"EXPIRE",
  "ReservedSlots": integer
}
```

`--status` (string)
Initial state of the queue. If you create a paused queue, then jobs in that queue wonât begin.

Possible values:

- `ACTIVE`
- `PAUSED`

`--tags` (map)
The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key.key -> (string)

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

**To create a custom queue**

The following `create-queue` example creates a custom transcoding queue.

```
aws mediaconvert create-queue \
    --endpoint-url https://abcd1234.mediaconvert.region-name-1.amazonaws.com \
    --region region-name-1 \
    --name Queue1 \
    --description "Keep this queue empty unless job is urgent."
```

To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.

Output:

```
{
    "Queue": {
        "Status": "ACTIVE",
        "Name": "Queue1",
        "LastUpdated": 1518034928,
        "Arn": "arn:aws:mediaconvert:region-name-1:012345678998:queues/Queue1",
        "Type": "CUSTOM",
        "CreatedAt": 1518034928,
        "Description": "Keep this queue empty unless job is urgent."
    }
}
```

For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html) in the *AWS Elemental MediaConvert User Guide*.

## Output

Queue -> (structure)

You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you donât specify a queue, the service sends all jobs through the default queue. For more information, see [https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html).

Arn -> (string)

An identifier for this resource that is unique within all of AWS.

ConcurrentJobs -> (integer)

The maximum number of jobs your queue can process concurrently.

CreatedAt -> (timestamp)

The timestamp in epoch seconds for when you created the queue.

Description -> (string)

An optional description that you create for each queue.

LastUpdated -> (timestamp)

The timestamp in epoch seconds for when you most recently updated the queue.

Name -> (string)

A name that you create for each queue. Each name must be unique within your account.

PricingPlan -> (string)

Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment.

ProgressingJobsCount -> (integer)

The estimated number of jobs with a PROGRESSING status.

ReservationPlan -> (structure)

Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.

Commitment -> (string)

The length of the term of your reserved queue pricing plan commitment.

ExpiresAt -> (timestamp)

The timestamp in epoch seconds for when the current pricing plan term for this reserved queue expires.

PurchasedAt -> (timestamp)

The timestamp in epoch seconds for when you set up the current pricing plan for this reserved queue.

RenewalType -> (string)

Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term.

ReservedSlots -> (integer)

Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. When you increase this number, you extend your existing commitment with a new 12-month commitment for a larger number of RTS. The new commitment begins when you purchase the additional capacity. You canât decrease the number of RTS in your reserved queue.

Status -> (string)

Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED.

ServiceOverrides -> (list)

A list of any service overrides applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact AWS Support.

(structure)

A service override applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact AWS Support.

Message -> (string)

Details about the service override that MediaConvert has applied.

Name -> (string)

The name of the setting that MediaConvert has applied an override to.

OverrideValue -> (string)

The current value of the service override that MediaConvert has applied.

Value -> (string)

The value of the setting that you configured, prior to any overrides that MediaConvert has applied.

Status -> (string)

Queues can be ACTIVE or PAUSED. If you pause a queue, the service wonât begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error.

SubmittedJobsCount -> (integer)

The estimated number of jobs with a SUBMITTED status.

Type -> (string)

Specifies whether this on-demand queue is system or custom. System queues are built in. You canât modify or delete system queues. You can create and modify custom queues.