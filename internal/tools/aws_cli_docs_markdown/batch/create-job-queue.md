# create-job-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# create-job-queue

## Description

Creates an Batch job queue. When you create a job queue, you associate one or more compute environments to the queue and assign an order of preference for the compute environments.

You also set a priority to the job queue that determines the order that the Batch scheduler places jobs onto its associated compute environments. For example, if a compute environment is associated with more than one job queue, the job queue with a higher priority is given preference for scheduling jobs to that compute environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateJobQueue)

## Synopsis

```
create-job-queue
--job-queue-name <value>
[--state <value>]
[--scheduling-policy-arn <value>]
--priority <value>
--compute-environment-order <value>
[--tags <value>]
[--job-state-time-limit-actions <value>]
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

`--job-queue-name` (string)

The name of the job queue. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

`--state` (string)

The state of the job queue. If the job queue state is `ENABLED` , it is able to accept jobs. If the job queue state is `DISABLED` , new jobs canât be added to the queue, but jobs already in the queue can finish.

Possible values:

- `ENABLED`
- `DISABLED`

`--scheduling-policy-arn` (string)

The Amazon Resource Name (ARN) of the fair-share scheduling policy. Job queues that donât have a fair-share scheduling policy are scheduled in a first-in, first-out (FIFO) model. After a job queue has a fair-share scheduling policy, it can be replaced but canât be removed.

The format is [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html#id1)aws:*Partition* :batch:*Region* :*Account* :scheduling-policy/*Name* `` .

An example is `aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy` .

A job queue without a fair-share scheduling policy is scheduled as a FIFO job queue and canât have a fair-share scheduling policy added. Jobs queues with a fair-share scheduling policy can have a maximum of 500 active share identifiers. When the limit has been reached, submissions of any jobs that add a new share identifier fail.

`--priority` (integer)

The priority of the job queue. Job queues with a higher priority (or a higher integer value for the `priority` parameter) are evaluated first when associated with the same compute environment. Priority is determined in descending order. For example, a job queue with a priority value of `10` is given scheduling preference over a job queue with a priority value of `1` . All of the compute environments must be either EC2 (`EC2` or `SPOT` ) or Fargate (`FARGATE` or `FARGATE_SPOT` ); EC2 and Fargate compute environments canât be mixed.

`--compute-environment-order` (list)

The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment runs a specific job. Compute environments must be in the `VALID` state before you can associate them with a job queue. You can associate up to three compute environments with a job queue. All of the compute environments must be either EC2 (`EC2` or `SPOT` ) or Fargate (`FARGATE` or `FARGATE_SPOT` ); EC2 and Fargate compute environments canât be mixed.

### Note

All compute environments that are associated with a job queue must share the same architecture. Batch doesnât support mixing compute environment architecture types in a single job queue.

(structure)

The order that compute environments are tried in for job placement within a queue. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower order integer value is tried for job placement first. Compute environments must be in the `VALID` state before you can associate them with a job queue. All of the compute environments must be either EC2 (`EC2` or `SPOT` ) or Fargate (`FARGATE` or `FARGATE_SPOT` ); Amazon EC2 and Fargate compute environments canât be mixed.

### Note

All compute environments that are associated with a job queue must share the same architecture. Batch doesnât support mixing compute environment architecture types in a single job queue.

order -> (integer)

The order of the compute environment. Compute environments are tried in ascending order. For example, if two compute environments are associated with a job queue, the compute environment with a lower `order` integer value is tried for job placement first.

computeEnvironment -> (string)

The Amazon Resource Name (ARN) of the compute environment.

Shorthand Syntax:

```
order=integer,computeEnvironment=string ...
```

JSON Syntax:

```
[
  {
    "order": integer,
    "computeEnvironment": "string"
  }
  ...
]
```

`--tags` (map)

The tags that you apply to the job queue to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging your Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) in *Batch User Guide* .

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

`--job-state-time-limit-actions` (list)

The set of actions that Batch performs on jobs that remain at the head of the job queue in the specified state longer than specified times. Batch will perform each action after `maxTimeSeconds` has passed. (**Note** : The minimum value for maxTimeSeconds is 600 (10 minutes) and its maximum value is 86,400 (24 hours).)

(structure)

Specifies an action that Batch will take after the job has remained at the head of the queue in the specified state for longer than the specified time.

reason -> (string)

The reason to log for the action being taken.

state -> (string)

The state of the job needed to trigger the action. The only supported value is `RUNNABLE` .

maxTimeSeconds -> (integer)

The approximate amount of time, in seconds, that must pass with the job in the specified state before the action is taken. The minimum value is 600 (10 minutes) and the maximum value is 86,400 (24 hours).

action -> (string)

The action to take when a job is at the head of the job queue in the specified state for the specified period of time. The only supported value is `CANCEL` , which will cancel the job.

Shorthand Syntax:

```
reason=string,state=string,maxTimeSeconds=integer,action=string ...
```

JSON Syntax:

```
[
  {
    "reason": "string",
    "state": "RUNNABLE",
    "maxTimeSeconds": integer,
    "action": "CANCEL"
  }
  ...
]
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

**To create a low priority job queue with a single compute environment**

This example creates a job queue called LowPriority that uses the M4Spot compute environment.

Command:

```
aws batch create-job-queue --cli-input-json file://<path_to_json_file>/LowPriority.json
```

JSON file format:

```
{
  "jobQueueName": "LowPriority",
  "state": "ENABLED",
  "priority": 10,
  "computeEnvironmentOrder": [
    {
      "order": 1,
      "computeEnvironment": "M4Spot"
    }
  ]
}
```

Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/LowPriority",
    "jobQueueName": "LowPriority"
}
```

**To create a high priority job queue with two compute environments**

This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2. The scheduler will attempt to place jobs on the C4OnDemand compute environment first.

Command:

```
aws batch create-job-queue --cli-input-json file://<path_to_json_file>/HighPriority.json
```

JSON file format:

```
{
  "jobQueueName": "HighPriority",
  "state": "ENABLED",
  "priority": 1,
  "computeEnvironmentOrder": [
    {
      "order": 1,
      "computeEnvironment": "C4OnDemand"
    },
    {
      "order": 2,
      "computeEnvironment": "M4Spot"
    }
  ]
}
```

Output:

```
{
    "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority",
    "jobQueueName": "HighPriority"
}
```

## Output

jobQueueName -> (string)

The name of the job queue.

jobQueueArn -> (string)

The Amazon Resource Name (ARN) of the job queue.