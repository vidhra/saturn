# describe-test-set-discrepancy-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-test-set-discrepancy-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/describe-test-set-discrepancy-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# describe-test-set-discrepancy-report

## Description

Gets metadata information about the test set discrepancy report.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/DescribeTestSetDiscrepancyReport)

## Synopsis

```
describe-test-set-discrepancy-report
--test-set-discrepancy-report-id <value>
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

`--test-set-discrepancy-report-id` (string)

The unique identifier of the test set discrepancy report.

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

testSetDiscrepancyReportId -> (string)

The unique identifier of the test set discrepancy report to describe.

testSetId -> (string)

The test set Id for the test set discrepancy report.

creationDateTime -> (timestamp)

The time and date of creation for the test set discrepancy report.

target -> (structure)

The target bot location for the test set discrepancy report.

botAliasTarget -> (structure)

Contains information about the bot alias used as the resource for the test set discrepancy report.

botId -> (string)

The unique identifier for the bot alias.

botAliasId -> (string)

The unique identifier for the bot associated with the bot alias.

localeId -> (string)

The unique identifier of the locale associated with the bot alias.

testSetDiscrepancyReportStatus -> (string)

The status for the test set discrepancy report.

lastUpdatedDataTime -> (timestamp)

The date and time of the last update for the test set discrepancy report.

testSetDiscrepancyTopErrors -> (structure)

The top 200 error results from the test set discrepancy report.

intentDiscrepancies -> (list)

Contains information about discrepancies found for intents between the test set and the bot.

(structure)

Contains information about discrepancy in an intent information between the test set and the bot.

intentName -> (string)

The name of the intent in the discrepancy report.

errorMessage -> (string)

The error message for a discrepancy for an intent between the test set and the bot.

slotDiscrepancies -> (list)

Contains information about discrepancies found for slots between the test set and the bot.

(structure)

Contains information about discrepancy in a slot information between the test set and the bot.

intentName -> (string)

The name of the intent associated with the slot in the discrepancy report.

slotName -> (string)

The name of the slot in the discrepancy report.

errorMessage -> (string)

The error message for a discrepancy for an intent between the test set and the bot.

testSetDiscrepancyRawOutputUrl -> (string)

Pre-signed Amazon S3 URL to download the test set discrepancy report.

failureReasons -> (list)

The failure report for the test set discrepancy report generation action.

(string)