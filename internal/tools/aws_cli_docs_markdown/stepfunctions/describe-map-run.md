# describe-map-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-map-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-map-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [stepfunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html#cli-aws-stepfunctions) ]

# describe-map-run

## Description

Provides information about a Map Runâs configuration, progress, and results. If youâve [redriven](https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html) a Map Run, this API action also returns information about the redrives of that Map Run. For more information, see [Examining Map Run](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html) in the *Step Functions Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/DescribeMapRun)

## Synopsis

```
describe-map-run
--map-run-arn <value>
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

`--map-run-arn` (string)

The Amazon Resource Name (ARN) that identifies a Map Run.

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

mapRunArn -> (string)

The Amazon Resource Name (ARN) that identifies a Map Run.

executionArn -> (string)

The Amazon Resource Name (ARN) that identifies the execution in which the Map Run was started.

status -> (string)

The current status of the Map Run.

startDate -> (timestamp)

The date when the Map Run was started.

stopDate -> (timestamp)

The date when the Map Run was stopped.

maxConcurrency -> (integer)

The maximum number of child workflow executions configured to run in parallel for the Map Run at the same time.

toleratedFailurePercentage -> (float)

The maximum percentage of failed child workflow executions before the Map Run fails.

toleratedFailureCount -> (long)

The maximum number of failed child workflow executions before the Map Run fails.

itemCounts -> (structure)

A JSON object that contains information about the total number of items, and the item count for each processing status, such as `pending` and `failed` .

pending -> (long)

The total number of items to process in child workflow executions that havenât started running yet.

running -> (long)

The total number of items being processed in child workflow executions that are currently in-progress.

succeeded -> (long)

The total number of items processed in child workflow executions that have completed successfully.

failed -> (long)

The total number of items processed in child workflow executions that have failed.

timedOut -> (long)

The total number of items processed in child workflow executions that have timed out.

aborted -> (long)

The total number of items processed in child workflow executions that were either stopped by the user or by Step Functions, because the Map Run failed.

total -> (long)

The total number of items processed in all the child workflow executions started by a Map Run.

resultsWritten -> (long)

Returns the count of items whose results were written by `ResultWriter` . For more information, see [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html) in the *Step Functions Developer Guide* .

failuresNotRedrivable -> (long)

The number of `FAILED` , `ABORTED` , or `TIMED_OUT` items in child workflow executions that cannot be redriven because the execution status of those child workflows is terminal. For example, child workflows with an execution status of `FAILED` , `ABORTED` , or `TIMED_OUT` and a `redriveStatus` of `NOT_REDRIVABLE` .

pendingRedrive -> (long)

The number of unsuccessful items in child workflow executions currently waiting to be redriven.

executionCounts -> (structure)

A JSON object that contains information about the total number of child workflow executions for the Map Run, and the count of child workflow executions for each status, such as `failed` and `succeeded` .

pending -> (long)

The total number of child workflow executions that were started by a Map Run, but havenât started executing yet.

running -> (long)

The total number of child workflow executions that were started by a Map Run and are currently in-progress.

succeeded -> (long)

The total number of child workflow executions that were started by a Map Run and have completed successfully.

failed -> (long)

The total number of child workflow executions that were started by a Map Run, but have failed.

timedOut -> (long)

The total number of child workflow executions that were started by a Map Run and have timed out.

aborted -> (long)

The total number of child workflow executions that were started by a Map Run and were running, but were either stopped by the user or by Step Functions because the Map Run failed.

total -> (long)

The total number of child workflow executions that were started by a Map Run.

resultsWritten -> (long)

Returns the count of child workflow executions whose results were written by `ResultWriter` . For more information, see [ResultWriter](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultwriter.html) in the *Step Functions Developer Guide* .

failuresNotRedrivable -> (long)

The number of `FAILED` , `ABORTED` , or `TIMED_OUT` child workflow executions that cannot be redriven because their execution status is terminal. For example, child workflows with an execution status of `FAILED` , `ABORTED` , or `TIMED_OUT` and a `redriveStatus` of `NOT_REDRIVABLE` .

pendingRedrive -> (long)

The number of unsuccessful child workflow executions currently waiting to be redriven. The status of these child workflow executions could be `FAILED` , `ABORTED` , or `TIMED_OUT` in the original execution attempt or a previous redrive attempt.

redriveCount -> (integer)

The number of times youâve redriven a Map Run. If you have not yet redriven a Map Run, the `redriveCount` is 0. This count is only updated if you successfully redrive a Map Run.

redriveDate -> (timestamp)

The date a Map Run was last redriven. If you have not yet redriven a Map Run, the `redriveDate` is null.