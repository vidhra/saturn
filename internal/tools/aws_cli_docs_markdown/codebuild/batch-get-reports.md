# batch-get-reportsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-reports.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-reports.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# batch-get-reports

## Description

Returns an array of reports.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/BatchGetReports)

## Synopsis

```
batch-get-reports
--report-arns <value>
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

`--report-arns` (list)

An array of ARNs that identify the `Report` objects to return.

(string)

Syntax:

```
"string" "string" ...
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

**To get information about one or more reports in AWS CodeBuild.**

The following `batch-get-reports` example retrieves information about the reports with the specified ARNs.

```
aws codebuild batch-get-reports \
    --report-arns arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 1 ID> arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 2 ID>
```

Output:

```
{
    "reports": [
        {
            "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 1 ID>",
            "type": "TEST",
            "name": "<report-group-name>",
            "reportGroupArn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>",
            "executionId": "arn:aws:codebuild:<region-ID>:<user-ID>:build/test-reports:<ID>",
            "status": "FAILED",
            "created": "2020-10-01T11:25:22.531000-07:00",
            "expired": "2020-10-31T11:25:22-07:00",
            "exportConfig": {
                "exportConfigType": "NO_EXPORT"
            },
            "truncated": false,
            "testSummary": {
                "total": 28,
                "statusCounts": {
                    "ERROR": 5,
                    "FAILED": 1,
                    "SKIPPED": 4,
                    "SUCCEEDED": 18,
                    "UNKNOWN": 0
                },
                "durationInNanoSeconds": 94000000
            }
        },
        {
            "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 2 ID>",
            "type": "TEST",
            "name": "<report-group-name>",
            "reportGroupArn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>",
            "executionId": "arn:aws:codebuild:<region-ID>:<user-ID>:build/test-reports:<ID>",
            "status": "FAILED",
            "created": "2020-10-01T11:13:05.816000-07:00",
            "expired": "2020-10-31T11:13:05-07:00",
            "exportConfig": {
                "exportConfigType": "NO_EXPORT"
            },
            "truncated": false,
            "testSummary": {
                "total": 28,
                "statusCounts": {
                    "ERROR": 5,
                    "FAILED": 1,
                    "SKIPPED": 4,
                    "SUCCEEDED": 18,
                    "UNKNOWN": 0
                },
                "durationInNanoSeconds": 94000000
            }
        }
    ],
    "reportsNotFound": []
}
```

For more information, see [Working with reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report.html) in the *AWS CodeBuild User Guide*.

## Output

reports -> (list)

The array of `Report` objects returned by `BatchGetReports` .

(structure)

Information about the results from running a series of test cases during the run of a build project. The test cases are specified in the buildspec for the build project using one or more paths to the test case files. You can specify any type of tests you want, such as unit tests, integration tests, and functional tests.

arn -> (string)

The ARN of the report run.

type -> (string)

The type of the report that was run.

CODE_COVERAGE

A code coverage report.

TEST

A test report.

name -> (string)

The name of the report that was run.

reportGroupArn -> (string)

The ARN of the report group associated with this report.

executionId -> (string)

The ARN of the build run that generated this report.

status -> (string)

The status of this report.

created -> (timestamp)

The date and time this report run occurred.

expired -> (timestamp)

The date and time a report expires. A report expires 30 days after it is created. An expired report is not available to view in CodeBuild.

exportConfig -> (structure)

Information about where the raw data used to generate this report was exported.

exportConfigType -> (string)

The export configuration type. Valid values are:

- `S3` : The report results are exported to an S3 bucket.
- `NO_EXPORT` : The report results are not exported.

s3Destination -> (structure)

A `S3ReportExportConfig` object that contains information about the S3 bucket where the run of a report is exported.

bucket -> (string)

The name of the S3 bucket where the raw data of a report are exported.

bucketOwner -> (string)

The Amazon Web Services account identifier of the owner of the Amazon S3 bucket. This allows report data to be exported to an Amazon S3 bucket that is owned by an account other than the account running the build.

path -> (string)

The path to the exported reportâs raw data results.

packaging -> (string)

The type of build output artifact to create. Valid values include:

- `NONE` : CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
- `ZIP` : CodeBuild creates a ZIP file with the raw data in the output bucket.

encryptionKey -> (string)

The encryption key for the reportâs encrypted raw data.

encryptionDisabled -> (boolean)

A boolean value that specifies if the results of a report are encrypted.

truncated -> (boolean)

A boolean that specifies if this report run is truncated. The list of test cases is truncated after the maximum number of test cases is reached.

testSummary -> (structure)

A `TestReportSummary` object that contains information about this test report.

total -> (integer)

The number of test cases in this `TestReportSummary` . The total includes truncated test cases.

statusCounts -> (map)

A map that contains the number of each type of status returned by the test results in this `TestReportSummary` .

key -> (string)

value -> (integer)

durationInNanoSeconds -> (long)

The number of nanoseconds it took to run all of the test cases in this report.

codeCoverageSummary -> (structure)

A `CodeCoverageReportSummary` object that contains a code coverage summary for this report.

lineCoveragePercentage -> (double)

The percentage of lines that are covered by your tests.

linesCovered -> (integer)

The number of lines that are covered by your tests.

linesMissed -> (integer)

The number of lines that are not covered by your tests.

branchCoveragePercentage -> (double)

The percentage of branches that are covered by your tests.

branchesCovered -> (integer)

The number of conditional branches that are covered by your tests.

branchesMissed -> (integer)

The number of conditional branches that are not covered by your tests.

reportsNotFound -> (list)

An array of ARNs passed to `BatchGetReportGroups` that are not associated with a `Report` .

(string)