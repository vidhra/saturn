# get-remaining-free-trial-daysÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-remaining-free-trial-days.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-remaining-free-trial-days.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# get-remaining-free-trial-days

## Description

Provides the number of days left for each data source used in the free trial period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetRemainingFreeTrialDays)

## Synopsis

```
get-remaining-free-trial-days
--detector-id <value>
[--account-ids <value>]
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

`--detector-id` (string)

The unique ID of the detector of the GuardDuty member account.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--account-ids` (list)

A list of account identifiers of the GuardDuty member account.

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

## Output

Accounts -> (list)

The member accounts which were included in a request and were processed successfully.

(structure)

Provides details of the GuardDuty member account that uses a free trial service.

AccountId -> (string)

The account identifier of the GuardDuty member account.

DataSources -> (structure)

Describes the data source enabled for the GuardDuty member account.

CloudTrail -> (structure)

Describes whether any Amazon Web Services CloudTrail management event logs are enabled as data sources.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

DnsLogs -> (structure)

Describes whether any DNS logs are enabled as data sources.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

FlowLogs -> (structure)

Describes whether any VPC Flow logs are enabled as data sources.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

S3Logs -> (structure)

Describes whether any S3 data event logs are enabled as data sources.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

Kubernetes -> (structure)

Describes whether any Kubernetes logs are enabled as data sources.

AuditLogs -> (structure)

Describes whether Kubernetes audit logs are enabled as a data source.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

MalwareProtection -> (structure)

Describes whether Malware Protection is enabled as a data source.

ScanEc2InstanceWithFindings -> (structure)

Describes whether Malware Protection for EC2 instances with findings is enabled as a data source.

FreeTrialDaysRemaining -> (integer)

A value that specifies the number of days left to use each enabled data source.

Features -> (list)

A list of features enabled for the GuardDuty account.

(structure)

Contains information about the free trial period for a feature.

Name -> (string)

The name of the feature for which the free trial is configured.

FreeTrialDaysRemaining -> (integer)

The number of the remaining free trial days for the feature.

UnprocessedAccounts -> (list)

The member account that was included in a request but for which the request could not be processed.

(structure)

Contains information about the accounts that werenât processed.

AccountId -> (string)

The Amazon Web Services account ID.

Result -> (string)

A reason why the account hasnât been processed.