# get-findings-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-findings-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-findings-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# get-findings-statistics

## Description

Retrieves a list of aggregated finding statistics for an external access or unused access analyzer.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/GetFindingsStatistics)

## Synopsis

```
get-findings-statistics
--analyzer-arn <value>
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

`--analyzer-arn` (string)

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) used to generate the statistics.

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

findingsStatistics -> (list)

A group of external access or unused access findings statistics.

(tagged union structure)

Contains information about the aggregate statistics for an external or unused access analyzer. Only one parameter can be used in a `FindingsStatistics` object.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `externalAccessFindingsStatistics`, `unusedAccessFindingsStatistics`.

externalAccessFindingsStatistics -> (structure)

The aggregate statistics for an external access analyzer.

resourceTypeStatistics -> (map)

The total number of active cross-account and public findings for each resource type of the specified external access analyzer.

key -> (string)

value -> (structure)

Contains information about the total number of active cross-account and public findings for a resource type of an external access analyzer.

totalActivePublic -> (integer)

The total number of active public findings for the resource type.

totalActiveCrossAccount -> (integer)

The total number of active cross-account findings for the resource type.

totalActiveFindings -> (integer)

The number of active findings for the specified external access analyzer.

totalArchivedFindings -> (integer)

The number of archived findings for the specified external access analyzer.

totalResolvedFindings -> (integer)

The number of resolved findings for the specified external access analyzer.

unusedAccessFindingsStatistics -> (structure)

The aggregate statistics for an unused access analyzer.

unusedAccessTypeStatistics -> (list)

A list of details about the total number of findings for each type of unused access for the analyzer.

(structure)

Contains information about the total number of findings for a type of unused access.

unusedAccessType -> (string)

The type of unused access.

total -> (integer)

The total number of findings for the specified unused access type.

topAccounts -> (list)

A list of one to ten Amazon Web Services accounts that have the most active findings for the unused access analyzer.

(structure)

Contains information about the findings for an Amazon Web Services account in an organization unused access analyzer.

account -> (string)

The ID of the Amazon Web Services account for which unused access finding details are provided.

numberOfActiveFindings -> (integer)

The number of active unused access findings for the specified Amazon Web Services account.

details -> (map)

Provides the number of active findings for each type of unused access for the specified Amazon Web Services account.

key -> (string)

value -> (integer)

totalActiveFindings -> (integer)

The total number of active findings for the unused access analyzer.

totalArchivedFindings -> (integer)

The total number of archived findings for the unused access analyzer.

totalResolvedFindings -> (integer)

The total number of resolved findings for the unused access analyzer.

lastUpdatedAt -> (timestamp)

The time at which the retrieval of the findings statistics was last updated. If the findings statistics have not been previously retrieved for the specified analyzer, this field will not be populated.