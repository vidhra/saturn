# update-answerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/update-answer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/update-answer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wellarchitected](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/index.html#cli-aws-wellarchitected) ]

# update-answer

## Description

Update the answer to a specific question in a workload review.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wellarchitected-2020-03-31/UpdateAnswer)

## Synopsis

```
update-answer
--workload-id <value>
--lens-alias <value>
--question-id <value>
[--selected-choices <value>]
[--choice-updates <value>]
[--notes <value>]
[--is-applicable | --no-is-applicable]
[--reason <value>]
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

`--question-id` (string)

The ID of the question.

`--selected-choices` (list)

List of selected choice IDs in a question answer.

The values entered replace the previously selected choices.

(string)

The ID of a choice.

Syntax:

```
"string" "string" ...
```

`--choice-updates` (map)

A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated.

key -> (string)

The ID of a choice.

value -> (structure)

A list of choices to be updated.

Status -> (string)

The status of a choice.

Reason -> (string)

The reason why a choice is non-applicable to a question in your workload.

Notes -> (string)

The notes associated with a choice.

Shorthand Syntax:

```
KeyName1=Status=string,Reason=string,Notes=string,KeyName2=Status=string,Reason=string,Notes=string
```

JSON Syntax:

```
{"string": {
      "Status": "SELECTED"|"NOT_APPLICABLE"|"UNSELECTED",
      "Reason": "OUT_OF_SCOPE"|"BUSINESS_PRIORITIES"|"ARCHITECTURE_CONSTRAINTS"|"OTHER"|"NONE",
      "Notes": "string"
    }
  ...}
```

`--notes` (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

`--is-applicable` | `--no-is-applicable` (boolean)

Defines whether this question is applicable to a lens review.

`--reason` (string)

The reason why a question is not applicable to your workload.

Possible values:

- `OUT_OF_SCOPE`
- `BUSINESS_PRIORITIES`
- `ARCHITECTURE_CONSTRAINTS`
- `OTHER`
- `NONE`

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

LensAlias -> (string)

The alias of the lens.

For Amazon Web Services official lenses, this is either the lens alias, such as `serverless` , or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless` . Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.

For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef` .

Each lens is identified by its  LensSummary$LensAlias .

LensArn -> (string)

The ARN for the lens.

Answer -> (structure)

An answer of the question.

QuestionId -> (string)

The ID of the question.

PillarId -> (string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

QuestionTitle -> (string)

The title of the question.

QuestionDescription -> (string)

The description of the question.

ImprovementPlanUrl -> (string)

The improvement plan URL for a question in an Amazon Web Services official lenses.

This value is only available if the question has been answered.

This value does not apply to custom lenses.

HelpfulResourceUrl -> (string)

The helpful resource URL.

For Amazon Web Services official lenses, this is the helpful resource URL for a question or choice.

For custom lenses, this is the helpful resource URL for a question and is only provided if `HelpfulResourceDisplayText` was specified for the question.

HelpfulResourceDisplayText -> (string)

The helpful resource text to be displayed for a custom lens.

This field does not apply to Amazon Web Services official lenses.

Choices -> (list)

List of choices available for a question.

(structure)

A choice available to answer question.

ChoiceId -> (string)

The ID of a choice.

Title -> (string)

The title of a choice.

Description -> (string)

The description of a choice.

HelpfulResource -> (structure)

The helpful resource (both text and URL) for a particular choice.

This field only applies to custom lenses. Each choice can have only one helpful resource.

DisplayText -> (string)

The display text for the choice content.

Url -> (string)

The URL for the choice content.

ImprovementPlan -> (structure)

The improvement plan (both text and URL) for a particular choice.

This field only applies to custom lenses. Each choice can have only one improvement plan.

DisplayText -> (string)

The display text for the choice content.

Url -> (string)

The URL for the choice content.

AdditionalResources -> (list)

The additional resources for a choice in a custom lens.

A choice can have up to two additional resources: one of type `HELPFUL_RESOURCE` , one of type `IMPROVEMENT_PLAN` , or both.

(structure)

The choice level additional resources for a custom lens.

This field does not apply to Amazon Web Services official lenses.

Type -> (string)

Type of additional resource for a custom lens.

Content -> (list)

The URLs for additional resources, either helpful resources or improvement plans, for a custom lens. Up to five additional URLs can be specified.

(structure)

The choice content.

DisplayText -> (string)

The display text for the choice content.

Url -> (string)

The URL for the choice content.

SelectedChoices -> (list)

List of selected choice IDs in a question answer.

The values entered replace the previously selected choices.

(string)

The ID of a choice.

ChoiceAnswers -> (list)

A list of selected choices to a question in your workload.

(structure)

A choice that has been answered on a question in your workload.

ChoiceId -> (string)

The ID of a choice.

Status -> (string)

The status of a choice.

Reason -> (string)

The reason why a choice is non-applicable to a question in your workload.

Notes -> (string)

The notes associated with a choice.

IsApplicable -> (boolean)

Defines whether this question is applicable to a lens review.

Risk -> (string)

The risk for a given workload, lens review, pillar, or question.

Notes -> (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

Reason -> (string)

The reason why the question is not applicable to your workload.

JiraConfiguration -> (structure)

Configuration of the Jira integration.

JiraIssueUrl -> (string)

The URL of the associated Jira issue.

LastSyncedTime -> (timestamp)

The date and time recorded.