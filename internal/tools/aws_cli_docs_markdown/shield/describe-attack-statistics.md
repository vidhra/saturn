# describe-attack-statisticsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-attack-statistics.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-attack-statistics.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [shield](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/index.html#cli-aws-shield) ]

# describe-attack-statistics

## Description

Provides information about the number and type of attacks Shield has detected in the last year for all resources that belong to your account, regardless of whether youâve defined Shield protections for them. This operation is available to Shield customers as well as to Shield Advanced customers.

The operation returns data for the time range of midnight UTC, one year ago, to midnight UTC, today. For example, if the current time is `2020-10-26 15:39:32 PDT` , equal to `2020-10-26 22:39:32 UTC` , then the time range for the attack data returned is from `2019-10-26 00:00:00 UTC` to `2020-10-26 00:00:00 UTC` .

The time range indicates the period covered by the attack statistics data items.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeAttackStatistics)

## Synopsis

```
describe-attack-statistics
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

TimeRange -> (structure)

The time range of the attack.

FromInclusive -> (timestamp)

The start time, in Unix time in seconds.

ToExclusive -> (timestamp)

The end time, in Unix time in seconds.

DataItems -> (list)

The data that describes the attacks detected during the time period.

(structure)

A single attack statistics data record. This is returned by  DescribeAttackStatistics along with a time range indicating the time period that the attack statistics apply to.

AttackVolume -> (structure)

Information about the volume of attacks during the time period. If the accompanying `AttackCount` is zero, this setting might be empty.

BitsPerSecond -> (structure)

A statistics object that uses bits per second as the unit. This is included for network level attacks.

Max -> (double)

The maximum attack volume observed for the given unit.

PacketsPerSecond -> (structure)

A statistics object that uses packets per second as the unit. This is included for network level attacks.

Max -> (double)

The maximum attack volume observed for the given unit.

RequestsPerSecond -> (structure)

A statistics object that uses requests per second as the unit. This is included for application level attacks, and is only available for accounts that are subscribed to Shield Advanced.

Max -> (double)

The maximum attack volume observed for the given unit.

AttackCount -> (long)

The number of attacks detected during the time period. This is always present, but might be zero.