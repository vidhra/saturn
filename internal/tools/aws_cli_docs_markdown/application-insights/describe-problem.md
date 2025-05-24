# describe-problemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-problem.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/describe-problem.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/index.html#cli-aws-application-insights) ]

# describe-problem

## Description

Describes an application problem.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-insights-2018-11-25/DescribeProblem)

## Synopsis

```
describe-problem
--problem-id <value>
[--account-id <value>]
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

`--problem-id` (string)

The ID of the problem.

`--account-id` (string)

The Amazon Web Services account ID for the owner of the resource group affected by the problem.

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

Problem -> (structure)

Information about the problem.

Id -> (string)

The ID of the problem.

Title -> (string)

The name of the problem.

ShortName -> (string)

The short name of the problem associated with the SNS notification.

Insights -> (string)

A detailed analysis of the problem using machine learning.

Status -> (string)

The status of the problem.

AffectedResource -> (string)

The resource affected by the problem.

StartTime -> (timestamp)

The time when the problem started, in epoch seconds.

EndTime -> (timestamp)

The time when the problem ended, in epoch seconds.

SeverityLevel -> (string)

A measure of the level of impact of the problem.

AccountId -> (string)

The Amazon Web Services account ID for the owner of the resource group affected by the problem.

ResourceGroupName -> (string)

The name of the resource group affected by the problem.

Feedback -> (map)

Feedback provided by the user about the problem.

key -> (string)

value -> (string)

RecurringCount -> (long)

The number of times that the same problem reoccurred after the first time it was resolved.

LastRecurrenceTime -> (timestamp)

The last time that the problem reoccurred after its last resolution.

Visibility -> (string)

Specifies whether or not you can view the problem. Updates to ignored problems do not generate notifications.

ResolutionMethod -> (string)

Specifies how the problem was resolved. If the value is `AUTOMATIC` , the system resolved the problem. If the value is `MANUAL` , the user resolved the problem. If the value is `UNRESOLVED` , then the problem is not resolved.

SNSNotificationArn -> (string)

The SNS notification topic ARN of the problem.