# get-canary-runsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [synthetics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/index.html#cli-aws-synthetics) ]

# get-canary-runs

## Description

Retrieves a list of runs for a specified canary.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/synthetics-2017-10-11/GetCanaryRuns)

## Synopsis

```
get-canary-runs
--name <value>
[--next-token <value>]
[--max-results <value>]
[--dry-run-id <value>]
[--run-type <value>]
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

The name of the canary that you want to see runs for.

`--next-token` (string)

A token that indicates that there is more data available. You can use this token in a subsequent `GetCanaryRuns` operation to retrieve the next set of results.

### Note

When auto retry is enabled for the canary, the first subsequent retry is suffixed with [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html#id1)1 indicating its the first retry and the next subsequent try is suffixed with [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html#id3)2.

`--max-results` (integer)

Specify this parameter to limit how many runs are returned each time you use the `GetCanaryRuns` operation. If you omit this parameter, the default of 100 is used.

`--dry-run-id` (string)

The DryRunId associated with an existing canaryâs dry run. You can use this DryRunId to retrieve information about the dry run.

`--run-type` (string)

- When you provide `RunType=CANARY_RUN` and `dryRunId` , you will get an exception
- When a value is not provided for `RunType` , the default value is `CANARY_RUN`
- When `CANARY_RUN` is provided, all canary runs excluding dry runs are returned
- When `DRY_RUN` is provided, all dry runs excluding canary runs are returned

Possible values:

- `CANARY_RUN`
- `DRY_RUN`

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

**To retrieve a list of runs for a specified canary**

The following `get-canary-runs` example retrieves a list of runs for the canary named `demo_canary`.

```
aws synthetics get-canary-runs \
    --name demo_canary
```

Output:

```
{
    "CanaryRuns": [
        {
            "Id": "a1b2c3d4-5678-90ab-cdef-example11111",
            "Name": "demo_canary",
            "Status": {
                "State": "PASSED",
                "StateReason": "",
                "StateReasonCode": ""
            },
            "Timeline": {
                "Started": "2024-10-16T10:38:57.013000+05:30",
                "Completed": "2024-10-16T10:39:25.793000+05:30"
            },
            "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-abc-example1234/2024/10/15/13/50-39-690"
        }
    ]
}
```

For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) in the *Amazon CloudWatch User Guide*.

## Output

CanaryRuns -> (list)

An array of structures. Each structure contains the details of one of the retrieved canary runs.

(structure)

This structure contains the details about one run of one canary.

Id -> (string)

A unique ID that identifies this canary run.

ScheduledRunId -> (string)

The ID of the scheduled canary run.

RetryAttempt -> (integer)

The count in number of the retry attempt.

Name -> (string)

The name of the canary.

Status -> (structure)

The status of this run.

State -> (string)

The current state of the run.

StateReason -> (string)

If run of the canary failed, this field contains the reason for the error.

StateReasonCode -> (string)

If this value is `CANARY_FAILURE` , an exception occurred in the canary code. If this value is `EXECUTION_FAILURE` , an exception occurred in CloudWatch Synthetics.

Timeline -> (structure)

A structure that contains the start and end times of this run.

Started -> (timestamp)

The start time of the run.

Completed -> (timestamp)

The end time of the run.

MetricTimestampForRunAndRetries -> (timestamp)

The time at which the metrics will be generated for this run or retries.

ArtifactS3Location -> (string)

The location where the canary stored artifacts from the run. Artifacts include the log file, screenshots, and HAR files.

DryRunConfig -> (structure)

Returns the dry run configurations for a canary.

DryRunId -> (string)

The DryRunId associated with an existing canaryâs dry run. You can use this DryRunId to retrieve information about the dry run.

NextToken -> (string)

A token that indicates that there is more data available. You can use this token in a subsequent `GetCanaryRuns` operation to retrieve the next set of results.