# get-report-group-trendÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/get-report-group-trend.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/get-report-group-trend.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# get-report-group-trend

## Description

Analyzes and accumulates test report values for the specified test reports.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/GetReportGroupTrend)

## Synopsis

```
get-report-group-trend
--report-group-arn <value>
[--num-of-reports <value>]
--trend-field <value>
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

`--report-group-arn` (string)

The ARN of the report group that contains the reports to analyze.

`--num-of-reports` (integer)

The number of reports to analyze. This operation always retrieves the most recent reports.

If this parameter is omitted, the most recent 100 reports are analyzed.

`--trend-field` (string)

The test report value to accumulate. This must be one of the following values:

Test reports:   DURATION

Accumulate the test run times for the specified reports.

PASS_RATE

Accumulate the percentage of tests that passed for the specified test reports.

TOTAL

Accumulate the total number of tests for the specified test reports.

Code coverage reports:   BRANCH_COVERAGE

Accumulate the branch coverage percentages for the specified test reports.

BRANCHES_COVERED

Accumulate the branches covered values for the specified test reports.

BRANCHES_MISSED

Accumulate the branches missed values for the specified test reports.

LINE_COVERAGE

Accumulate the line coverage percentages for the specified test reports.

LINES_COVERED

Accumulate the lines covered values for the specified test reports.

LINES_MISSED

Accumulate the lines not covered values for the specified test reports.

Possible values:

- `PASS_RATE`
- `DURATION`
- `TOTAL`
- `LINE_COVERAGE`
- `LINES_COVERED`
- `LINES_MISSED`
- `BRANCH_COVERAGE`
- `BRANCHES_COVERED`
- `BRANCHES_MISSED`

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

stats -> (structure)

Contains the accumulated trend data.

average -> (string)

Contains the average of all values analyzed.

max -> (string)

Contains the maximum value analyzed.

min -> (string)

Contains the minimum value analyzed.

rawData -> (list)

An array that contains the raw data for each report.

(structure)

Contains the unmodified data for the report. For more information, see .

reportArn -> (string)

The ARN of the report.

data -> (string)

The value of the requested data field from the report.