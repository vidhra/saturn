# list-command-executionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-command-executions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-command-executions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# list-command-executions

## Description

List all command executions.

### Warning

- You must provide only the `startedTimeFilter` or the `completedTimeFilter` information. If you provide both time filters, the API will generate an error. You can use this information to retrieve a list of command executions within a specific timeframe.
- You must provide only the `commandArn` or the `thingArn` information depending on whether you want to list executions for a specific command or an IoT thing. If you provide both fields, the API will generate an error.

For more information about considerations for using this API, see [List command executions in your account (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-execution-start-monitor.html#iot-remote-command-execution-list-cli) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCommandExecutions)

`list-command-executions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `commandExecutions`

## Synopsis

```
list-command-executions
[--namespace <value>]
[--status <value>]
[--sort-order <value>]
[--started-time-filter <value>]
[--completed-time-filter <value>]
[--target-arn <value>]
[--command-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--namespace` (string)

The namespace of the command.

Possible values:

- `AWS-IoT`
- `AWS-IoT-FleetWise`

`--status` (string)

List all command executions for the device that have a particular status. For example, you can filter the list to display only command executions that have failed or timed out.

Possible values:

- `CREATED`
- `IN_PROGRESS`
- `SUCCEEDED`
- `FAILED`
- `REJECTED`
- `TIMED_OUT`

`--sort-order` (string)

Specify whether to list the command executions that were created in the ascending or descending order. By default, the API returns all commands in the descending order based on the start time or completion time of the executions, that are determined by the `startTimeFilter` and `completeTimeFilter` parameters.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--started-time-filter` (structure)

List all command executions that started any time before or after the date and time that you specify. The date and time uses the format `yyyy-MM-dd'T'HH:mm` .

after -> (string)

Filter to display command executions that started or completed only after a particular date and time.

before -> (string)

Filter to display command executions that started or completed only before a particular date and time.

Shorthand Syntax:

```
after=string,before=string
```

JSON Syntax:

```
{
  "after": "string",
  "before": "string"
}
```

`--completed-time-filter` (structure)

List all command executions that completed any time before or after the date and time that you specify. The date and time uses the format `yyyy-MM-dd'T'HH:mm` .

after -> (string)

Filter to display command executions that started or completed only after a particular date and time.

before -> (string)

Filter to display command executions that started or completed only before a particular date and time.

Shorthand Syntax:

```
after=string,before=string
```

JSON Syntax:

```
{
  "after": "string",
  "before": "string"
}
```

`--target-arn` (string)

The Amazon Resource Number (ARN) of the target device. You can use this information to list all command executions for a particular device.

`--command-arn` (string)

The Amazon Resource Number (ARN) of the command. You can use this information to list all command executions for a particular command.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

commandExecutions -> (list)

The list of command executions.

(structure)

Summary information about a particular command execution.

commandArn -> (string)

The Amazon Resource Name (ARN) of the command execution.

executionId -> (string)

The unique identifier of the command execution.

targetArn -> (string)

The Amazon Resource Name (ARN) of the target device for which the command is being executed.

status -> (string)

The status of the command executions.

createdAt -> (timestamp)

The date and time at which the command execution was created for the target device.

startedAt -> (timestamp)

The date and time at which the command started executing on the target device.

completedAt -> (timestamp)

The date and time at which the command completed executing on the target device.

nextToken -> (string)

The token to use to get the next set of results, or `null` if there are no additional results.