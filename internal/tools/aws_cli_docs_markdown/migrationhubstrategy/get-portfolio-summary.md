# get-portfolio-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/get-portfolio-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/get-portfolio-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhubstrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/index.html#cli-aws-migrationhubstrategy) ]

# get-portfolio-summary

## Description

Retrieves overall summary including the number of servers to rehost and the overall number of anti-patterns.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhubstrategy-2020-02-19/GetPortfolioSummary)

## Synopsis

```
get-portfolio-summary
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

assessmentSummary -> (structure)

An assessment summary for the portfolio including the number of servers to rehost and the overall number of anti-patterns.

antipatternReportS3Object -> (structure)

The Amazon S3 object containing the anti-pattern report.

s3Bucket -> (string)

The S3 bucket name.

s3key -> (string)

The Amazon S3 key name.

antipatternReportStatus -> (string)

The status of the anti-pattern report.

antipatternReportStatusMessage -> (string)

The status message of the anti-pattern report.

lastAnalyzedTimestamp -> (timestamp)

The time the assessment was performed.

listAntipatternSeveritySummary -> (list)

List of AntipatternSeveritySummary.

(structure)

Contains the summary of anti-patterns and their severity.

count -> (integer)

Contains the count of anti-patterns.

severity -> (string)

Contains the severity of anti-patterns.

listApplicationComponentStatusSummary -> (list)

List of status summaries of the analyzed application components.

(structure)

Summary of the analysis status of the application component.

count -> (integer)

The number of application components successfully analyzed, partially successful or failed analysis.

srcCodeOrDbAnalysisStatus -> (string)

The status of database analysis.

listApplicationComponentStrategySummary -> (list)

List of ApplicationComponentStrategySummary.

(structure)

Object containing the summary of the strategy recommendations.

count -> (integer)

The count of recommendations per strategy.

strategy -> (string)

The name of recommended strategy.

listApplicationComponentSummary -> (list)

List of ApplicationComponentSummary.

(structure)

Contains the summary of application components.

appType -> (string)

Contains the name of application types.

count -> (integer)

Contains the count of application type.

listServerStatusSummary -> (list)

List of status summaries of the analyzed servers.

(structure)

The status summary of the server analysis.

count -> (integer)

The number of servers successfully analyzed, partially successful or failed analysis.

runTimeAssessmentStatus -> (string)

The status of the run time.

listServerStrategySummary -> (list)

List of ServerStrategySummary.

(structure)

Object containing the summary of the strategy recommendations.

count -> (integer)

The count of recommendations per strategy.

strategy -> (string)

The name of recommended strategy.

listServerSummary -> (list)

List of ServerSummary.

(structure)

Object containing details about the servers imported by Application Discovery Service

ServerOsType -> (string)

Type of operating system for the servers.

count -> (integer)

Number of servers.