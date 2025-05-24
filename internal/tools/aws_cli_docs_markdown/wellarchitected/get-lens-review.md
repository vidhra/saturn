# get-lens-reviewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/get-lens-review.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/get-lens-review.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wellarchitected](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/index.html#cli-aws-wellarchitected) ]

# get-lens-review

## Description

Get lens review.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wellarchitected-2020-03-31/GetLensReview)

## Synopsis

```
get-lens-review
--workload-id <value>
--lens-alias <value>
[--milestone-number <value>]
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

`--lens-alias` (string)

The alias of the lens.

For Amazon Web Services official lenses, this is either the lens alias, such as `serverless` , or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless` . Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.

For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef` .

Each lens is identified by its  LensSummary$LensAlias .

`--milestone-number` (integer)

The milestone number.

A workload can have a maximum of 100 milestones.

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

WorkloadId -> (string)

The ID assigned to the workload. This ID is unique within an Amazon Web Services Region.

MilestoneNumber -> (integer)

The milestone number.

A workload can have a maximum of 100 milestones.

LensReview -> (structure)

A lens review of a question.

LensAlias -> (string)

The alias of the lens.

For Amazon Web Services official lenses, this is either the lens alias, such as `serverless` , or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless` . Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.

For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef` .

Each lens is identified by its  LensSummary$LensAlias .

LensArn -> (string)

The ARN for the lens.

LensVersion -> (string)

The version of the lens.

LensName -> (string)

The full name of the lens.

LensStatus -> (string)

The status of the lens.

PillarReviewSummaries -> (list)

List of pillar review summaries of lens review in a workload.

(structure)

A pillar review summary of a lens review.

PillarId -> (string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

PillarName -> (string)

The name of the pillar.

Notes -> (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

RiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.

PrioritizedRiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.

JiraConfiguration -> (structure)

Jira configuration status of the Lens review.

SelectedPillars -> (list)

Selected pillars in the workload.

(structure)

The selected pillar.

PillarId -> (string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

SelectedQuestionIds -> (list)

Selected question IDs in the selected pillar.

(string)

UpdatedAt -> (timestamp)

The date and time recorded.

Notes -> (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

RiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.

NextToken -> (string)

The token to use to retrieve the next set of results.

Profiles -> (list)

The profiles associated with the workload.

(structure)

The profile associated with a workload.

ProfileArn -> (string)

The profile ARN.

ProfileVersion -> (string)

The profile version.

PrioritizedRiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.