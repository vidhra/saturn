# poll-for-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/poll-for-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/poll-for-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datapipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/index.html#cli-aws-datapipeline) ]

# poll-for-task

## Description

Task runners call `PollForTask` to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the `workerGroup` parameter. The task returned can come from any of the pipelines that match the `workerGroup` value passed in by the task runner and that was launched using the IAM user credentials specified by the task runner.

If tasks are ready in the work queue, `PollForTask` returns a response immediately. If no tasks are available in the queue, `PollForTask` uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call `PollForTask` again on the same `workerGroup` until it receives a response, and this can take up to 90 seconds.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datapipeline-2012-10-29/PollForTask)

## Synopsis

```
poll-for-task
--worker-group <value>
[--hostname <value>]
[--instance-identity <value>]
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

`--worker-group` (string)

The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for `workerGroup` in the call to `PollForTask` . There are no wildcard values permitted in `workerGroup` ; the string must be an exact, case-sensitive, match.

`--hostname` (string)

The public DNS name of the calling task runner.

`--instance-identity` (structure)

Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using `http://169.254.169.254/latest/meta-data/instance-id` . For more information, see [Instance Metadata](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html) in the *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.

document -> (string)

A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.

signature -> (string)

A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.

Shorthand Syntax:

```
document=string,signature=string
```

JSON Syntax:

```
{
  "document": "string",
  "signature": "string"
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

taskObject -> (structure)

The information needed to complete the task that is being assigned to the task runner. One of the fields returned in this object is `taskId` , which contains an identifier for the task being assigned. The calling task runner uses `taskId` in subsequent calls to  ReportTaskProgress and  SetTaskStatus .

taskId -> (string)

An internal identifier for the task. This ID is passed to the  SetTaskStatus and  ReportTaskProgress actions.

pipelineId -> (string)

The ID of the pipeline that provided the task.

attemptId -> (string)

The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how many times a task is attempted.

objects -> (map)

Connection information for the location where the task runner will publish the output of the task.

key -> (string)

value -> (structure)

Contains information about a pipeline object. This can be a logical, physical, or physical attempt pipeline object. The complete set of components of a pipeline defines the pipeline.

id -> (string)

The ID of the object.

name -> (string)

The name of the object.

fields -> (list)

Key-value pairs that define the properties of the object.

(structure)

A key-value pair that describes a property of a pipeline object. The value is specified as either a string value (`StringValue` ) or a reference to another object (`RefValue` ) but not as both.

key -> (string)

The field identifier.

stringValue -> (string)

The field value, expressed as a String.

refValue -> (string)

The field value, expressed as the identifier of another object.