# update-triggerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-trigger.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-trigger.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-trigger

## Description

Updates a trigger definition.

Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Amazon Web Services Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateTrigger)

## Synopsis

```
update-trigger
--name <value>
--trigger-update <value>
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

`--name` (string)

The name of the trigger to update.

`--trigger-update` (structure)

The new values with which to update the trigger.

Name -> (string)

Reserved for future use.

Description -> (string)

A description of this trigger.

Schedule -> (string)

A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html) . For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)` .

Actions -> (list)

The actions initiated by this trigger.

(structure)

Defines an action to be initiated by a trigger.

JobName -> (string)

The name of a job to be run.

Arguments -> (map)

The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.

For information about how to specify and consume your own Job arguments, see the [Calling Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.

For information about the key-value pairs that Glue consumes to set up your job, see the [Special Parameters Used by Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.

key -> (string)

value -> (string)

Timeout -> (integer)

The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used with this action.

NotificationProperty -> (structure)

Specifies configuration properties of a job run notification.

NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.

CrawlerName -> (string)

The name of the crawler to be used with this action.

Predicate -> (structure)

The predicate of this trigger, which defines when it will fire.

Logical -> (string)

An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions -> (list)

A list of the conditions that determine when the trigger will fire.

(structure)

Defines a condition under which a trigger fires.

LogicalOperator -> (string)

A logical operator.

JobName -> (string)

The name of the job whose `JobRuns` this condition applies to, and on which this trigger waits.

State -> (string)

The condition state. Currently, the only job states that a trigger can listen for are `SUCCEEDED` , `STOPPED` , `FAILED` , and `TIMEOUT` . The only crawler states that a trigger can listen for are `SUCCEEDED` , `FAILED` , and `CANCELLED` .

CrawlerName -> (string)

The name of the crawler to which this condition applies.

CrawlState -> (string)

The state of the crawler to which this condition applies.

EventBatchingCondition -> (structure)

Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

BatchSize -> (integer)

Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.

BatchWindow -> (integer)

Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.

JSON Syntax:

```
{
  "Name": "string",
  "Description": "string",
  "Schedule": "string",
  "Actions": [
    {
      "JobName": "string",
      "Arguments": {"string": "string"
        ...},
      "Timeout": integer,
      "SecurityConfiguration": "string",
      "NotificationProperty": {
        "NotifyDelayAfter": integer
      },
      "CrawlerName": "string"
    }
    ...
  ],
  "Predicate": {
    "Logical": "AND"|"ANY",
    "Conditions": [
      {
        "LogicalOperator": "EQUALS",
        "JobName": "string",
        "State": "STARTING"|"RUNNING"|"STOPPING"|"STOPPED"|"SUCCEEDED"|"FAILED"|"TIMEOUT"|"ERROR"|"WAITING"|"EXPIRED",
        "CrawlerName": "string",
        "CrawlState": "RUNNING"|"CANCELLING"|"CANCELLED"|"SUCCEEDED"|"FAILED"|"ERROR"
      }
      ...
    ]
  },
  "EventBatchingCondition": {
    "BatchSize": integer,
    "BatchWindow": integer
  }
}
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

## Output

Trigger -> (structure)

The resulting trigger definition.

Name -> (string)

The name of the trigger.

WorkflowName -> (string)

The name of the workflow associated with the trigger.

Id -> (string)

Reserved for future use.

Type -> (string)

The type of trigger that this is.

State -> (string)

The current state of the trigger.

Description -> (string)

A description of this trigger.

Schedule -> (string)

A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html) . For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)` .

Actions -> (list)

The actions initiated by this trigger.

(structure)

Defines an action to be initiated by a trigger.

JobName -> (string)

The name of a job to be run.

Arguments -> (map)

The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.

For information about how to specify and consume your own Job arguments, see the [Calling Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.

For information about the key-value pairs that Glue consumes to set up your job, see the [Special Parameters Used by Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.

key -> (string)

value -> (string)

Timeout -> (integer)

The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used with this action.

NotificationProperty -> (structure)

Specifies configuration properties of a job run notification.

NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.

CrawlerName -> (string)

The name of the crawler to be used with this action.

Predicate -> (structure)

The predicate of this trigger, which defines when it will fire.

Logical -> (string)

An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions -> (list)

A list of the conditions that determine when the trigger will fire.

(structure)

Defines a condition under which a trigger fires.

LogicalOperator -> (string)

A logical operator.

JobName -> (string)

The name of the job whose `JobRuns` this condition applies to, and on which this trigger waits.

State -> (string)

The condition state. Currently, the only job states that a trigger can listen for are `SUCCEEDED` , `STOPPED` , `FAILED` , and `TIMEOUT` . The only crawler states that a trigger can listen for are `SUCCEEDED` , `FAILED` , and `CANCELLED` .

CrawlerName -> (string)

The name of the crawler to which this condition applies.

CrawlState -> (string)

The state of the crawler to which this condition applies.

EventBatchingCondition -> (structure)

Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

BatchSize -> (integer)

Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.

BatchWindow -> (integer)

Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.