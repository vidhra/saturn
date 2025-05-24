# list-check-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/list-check-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/list-check-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wellarchitected](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/index.html#cli-aws-wellarchitected) ]

# list-check-details

## Description

List of Trusted Advisor check details by account related to the workload.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wellarchitected-2020-03-31/ListCheckDetails)

## Synopsis

```
list-check-details
--workload-id <value>
[--next-token <value>]
[--max-results <value>]
--lens-arn <value>
--pillar-id <value>
--question-id <value>
--choice-id <value>
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

`--workload-id` (string)

The ID assigned to the workload. This ID is unique within an Amazon Web Services Region.

`--next-token` (string)

The token to use to retrieve the next set of results.

`--max-results` (integer)

The maximum number of results to return for this request.

`--lens-arn` (string)

Well-Architected Lens ARN.

`--pillar-id` (string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

`--question-id` (string)

The ID of the question.

`--choice-id` (string)

The ID of a choice.

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

CheckDetails -> (list)

The details about the Trusted Advisor checks related to the Well-Architected best practice.

(structure)

Account details for a Well-Architected best practice in relation to Trusted Advisor checks.

Id -> (string)

Trusted Advisor check ID.

Name -> (string)

Trusted Advisor check name.

Description -> (string)

Trusted Advisor check description.

Provider -> (string)

Provider of the check related to the best practice.

LensArn -> (string)

Well-Architected Lens ARN associated to the check.

PillarId -> (string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

QuestionId -> (string)

The ID of the question.

ChoiceId -> (string)

The ID of a choice.

Status -> (string)

Status associated to the check.

AccountId -> (string)

An Amazon Web Services account ID.

FlaggedResources -> (integer)

Count of flagged resources associated to the check.

Reason -> (string)

Reason associated to the check.

UpdatedAt -> (timestamp)

The date and time recorded.

NextToken -> (string)

The token to use to retrieve the next set of results.