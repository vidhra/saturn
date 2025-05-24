# start-capacity-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/start-capacity-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/start-capacity-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [outposts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/index.html#cli-aws-outposts) ]

# start-capacity-task

## Description

Starts the specified capacity task. You can have one active capacity task for each order and each Outpost.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/outposts-2019-12-03/StartCapacityTask)

## Synopsis

```
start-capacity-task
--outpost-identifier <value>
[--order-id <value>]
[--asset-id <value>]
--instance-pools <value>
[--instances-to-exclude <value>]
[--dry-run | --no-dry-run]
[--task-action-on-blocking-instances <value>]
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

`--outpost-identifier` (string)

The ID or ARN of the Outposts associated with the specified capacity task.

`--order-id` (string)

The ID of the Amazon Web Services Outposts order associated with the specified capacity task.

`--asset-id` (string)

The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.

`--instance-pools` (list)

The instance pools specified in the capacity task.

(structure)

The instance type that you specify determines the combination of CPU, memory, storage, and networking capacity.

InstanceType -> (string)

The instance type of the hosts.

Count -> (integer)

The number of instances for the specified instance type.

Shorthand Syntax:

```
InstanceType=string,Count=integer ...
```

JSON Syntax:

```
[
  {
    "InstanceType": "string",
    "Count": integer
  }
  ...
]
```

`--instances-to-exclude` (structure)

List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task.

Instances -> (list)

List of user-specified instances that must not be stopped.

(string)

AccountIds -> (list)

IDs of the accounts that own each instance that must not be stopped.

(string)

The ID of the Amazon Web Services account.

Services -> (list)

Names of the services that own each instance that must not be stopped in order to free up the capacity needed to run the capacity task.

(string)

Shorthand Syntax:

```
Instances=string,string,AccountIds=string,string,Services=string,string
```

JSON Syntax:

```
{
  "Instances": ["string", ...],
  "AccountIds": ["string", ...],
  "Services": ["AWS"|"EC2"|"ELASTICACHE"|"ELB"|"RDS"|"ROUTE53", ...]
}
```

`--dry-run` | `--no-dry-run` (boolean)

You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan.

`--task-action-on-blocking-instances` (string)

Specify one of the following options in case an instance is blocking the capacity task from running.

- `WAIT_FOR_EVACUATION` - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.
- `FAIL_TASK` - The capacity task fails.

Possible values:

- `WAIT_FOR_EVACUATION`
- `FAIL_TASK`

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

CapacityTaskId -> (string)

ID of the capacity task that you want to start.

OutpostId -> (string)

ID of the Outpost associated with the capacity task.

OrderId -> (string)

ID of the Amazon Web Services Outposts order of the host associated with the capacity task.

AssetId -> (string)

The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.

RequestedInstancePools -> (list)

List of the instance pools requested in the specified capacity task.

(structure)

The instance type that you specify determines the combination of CPU, memory, storage, and networking capacity.

InstanceType -> (string)

The instance type of the hosts.

Count -> (integer)

The number of instances for the specified instance type.

InstancesToExclude -> (structure)

User-specified instances that must not be stopped in order to free up the capacity needed to run the capacity task.

Instances -> (list)

List of user-specified instances that must not be stopped.

(string)

AccountIds -> (list)

IDs of the accounts that own each instance that must not be stopped.

(string)

The ID of the Amazon Web Services account.

Services -> (list)

Names of the services that own each instance that must not be stopped in order to free up the capacity needed to run the capacity task.

(string)

DryRun -> (boolean)

Results of the dry run showing if the specified capacity task is above or below the available instance capacity.

CapacityTaskStatus -> (string)

Status of the specified capacity task.

Failed -> (structure)

Reason that the specified capacity task failed.

Reason -> (string)

The reason that the specified capacity task failed.

Type -> (string)

The type of failure.

CreationDate -> (timestamp)

Date that the specified capacity task was created.

CompletionDate -> (timestamp)

Date that the specified capacity task ran successfully.

LastModifiedDate -> (timestamp)

Date that the specified capacity task was last modified.

TaskActionOnBlockingInstances -> (string)

User-specified option in case an instance is blocking the capacity task from running.

- `WAIT_FOR_EVACUATION` - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.
- `FAIL_TASK` - The capacity task fails.