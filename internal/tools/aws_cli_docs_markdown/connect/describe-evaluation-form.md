# describe-evaluation-formÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-evaluation-form.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-evaluation-form.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# describe-evaluation-form

## Description

Describes an evaluation form in the specified Amazon Connect instance. If the version property is not provided, the latest version of the evaluation form is described.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeEvaluationForm)

## Synopsis

```
describe-evaluation-form
--instance-id <value>
--evaluation-form-id <value>
[--evaluation-form-version <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--evaluation-form-id` (string)

A unique identifier for the contact evaluation.

`--evaluation-form-version` (integer)

A version of the evaluation form.

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

EvaluationForm -> (structure)

Information about the evaluation form.

EvaluationFormId -> (string)

The unique identifier for the evaluation form.

EvaluationFormVersion -> (integer)

A version of the evaluation form.

Locked -> (boolean)

The flag indicating whether the evaluation form is locked for changes.

EvaluationFormArn -> (string)

The Amazon Resource Name (ARN) for the evaluation form resource.

Title -> (string)

A title of the evaluation form.

Description -> (string)

The description of the evaluation form.

Status -> (string)

The status of the evaluation form.

Items -> (list)

Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.

(tagged union structure)

Information about an item from an evaluation form. The item must be either a section or a question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Section`, `Question`.

Section -> (structure)

The information of the section.

Title -> (string)

The title of the section.

RefId -> (string)

The identifier of the section. An identifier must be unique within the evaluation form.

Instructions -> (string)

The instructions of the section.

Items -> (list)

The items of the section.

(tagged union structure)

Information about an item from an evaluation form. The item must be either a section or a question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Section`, `Question`.

Section -> (structure)

The information of the section.

Title -> (string)

The title of the section.

RefId -> (string)

The identifier of the section. An identifier must be unique within the evaluation form.

Instructions -> (string)

The instructions of the section.

Weight -> (double)

The scoring weight of the section.

Question -> (structure)

The information of the question.

Title -> (string)

The title of the question.

Instructions -> (string)

The instructions of the section.

RefId -> (string)

The identifier of the question. An identifier must be unique within the evaluation form.

NotApplicableEnabled -> (boolean)

The flag to enable not applicable answers to the question.

QuestionType -> (string)

The type of the question.

QuestionTypeProperties -> (tagged union structure)

The properties of the type of question. Text questions do not have to define question type properties.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Numeric`, `SingleSelect`.

Numeric -> (structure)

The properties of the numeric question.

MinValue -> (integer)

The minimum answer value.

MaxValue -> (integer)

The maximum answer value.

Options -> (list)

The scoring options of the numeric question.

(structure)

Information about the option range used for scoring in numeric questions.

MinValue -> (integer)

The minimum answer value of the range option.

MaxValue -> (integer)

The maximum answer value of the range option.

Score -> (integer)

The score assigned to answer values within the range option.

AutomaticFail -> (boolean)

The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.

Automation -> (tagged union structure)

The automation properties of the numeric question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PropertyValue`.

PropertyValue -> (structure)

The property value of the automation.

Label -> (string)

The property label of the automation.

SingleSelect -> (structure)

The properties of the numeric question.

Options -> (list)

The answer options of the single select question.

(structure)

Information about the automation configuration in single select questions.

RefId -> (string)

The identifier of the answer option. An identifier must be unique within the question.

Text -> (string)

The title of the answer option.

Score -> (integer)

The score assigned to the answer option.

AutomaticFail -> (boolean)

The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.

DisplayAs -> (string)

The display mode of the single select question.

Automation -> (structure)

The display mode of the single select question.

Options -> (list)

The automation options of the single select question.

(tagged union structure)

Information about the automation option of a single select question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RuleCategory`.

RuleCategory -> (structure)

The automation option based on a rule category for the single select question.

Category -> (string)

The category name, as defined in Rules.

Condition -> (string)

The condition to apply for the automation option. If the condition is `PRESENT` , then the option is applied when the contact data includes the category. Similarly, if the condition is `NOT_PRESENT` , then the option is applied when the contact data does not include the category.

OptionRefId -> (string)

The identifier of the answer option.

DefaultOptionRefId -> (string)

The identifier of the default answer option, when none of the automation options match the criteria.

Weight -> (double)

The scoring weight of the section.

Weight -> (double)

The scoring weight of the section.

Question -> (structure)

The information of the question.

Title -> (string)

The title of the question.

Instructions -> (string)

The instructions of the section.

RefId -> (string)

The identifier of the question. An identifier must be unique within the evaluation form.

NotApplicableEnabled -> (boolean)

The flag to enable not applicable answers to the question.

QuestionType -> (string)

The type of the question.

QuestionTypeProperties -> (tagged union structure)

The properties of the type of question. Text questions do not have to define question type properties.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Numeric`, `SingleSelect`.

Numeric -> (structure)

The properties of the numeric question.

MinValue -> (integer)

The minimum answer value.

MaxValue -> (integer)

The maximum answer value.

Options -> (list)

The scoring options of the numeric question.

(structure)

Information about the option range used for scoring in numeric questions.

MinValue -> (integer)

The minimum answer value of the range option.

MaxValue -> (integer)

The maximum answer value of the range option.

Score -> (integer)

The score assigned to answer values within the range option.

AutomaticFail -> (boolean)

The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.

Automation -> (tagged union structure)

The automation properties of the numeric question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `PropertyValue`.

PropertyValue -> (structure)

The property value of the automation.

Label -> (string)

The property label of the automation.

SingleSelect -> (structure)

The properties of the numeric question.

Options -> (list)

The answer options of the single select question.

(structure)

Information about the automation configuration in single select questions.

RefId -> (string)

The identifier of the answer option. An identifier must be unique within the question.

Text -> (string)

The title of the answer option.

Score -> (integer)

The score assigned to the answer option.

AutomaticFail -> (boolean)

The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.

DisplayAs -> (string)

The display mode of the single select question.

Automation -> (structure)

The display mode of the single select question.

Options -> (list)

The automation options of the single select question.

(tagged union structure)

Information about the automation option of a single select question.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RuleCategory`.

RuleCategory -> (structure)

The automation option based on a rule category for the single select question.

Category -> (string)

The category name, as defined in Rules.

Condition -> (string)

The condition to apply for the automation option. If the condition is `PRESENT` , then the option is applied when the contact data includes the category. Similarly, if the condition is `NOT_PRESENT` , then the option is applied when the contact data does not include the category.

OptionRefId -> (string)

The identifier of the answer option.

DefaultOptionRefId -> (string)

The identifier of the default answer option, when none of the automation options match the criteria.

Weight -> (double)

The scoring weight of the section.

ScoringStrategy -> (structure)

A scoring strategy of the evaluation form.

Mode -> (string)

The scoring mode of the evaluation form.

Status -> (string)

The scoring status of the evaluation form.

CreatedTime -> (timestamp)

The timestamp for when the evaluation form was created.

CreatedBy -> (string)

The Amazon Resource Name (ARN) of the user who created the evaluation form.

LastModifiedTime -> (timestamp)

The timestamp for when the evaluation form was last updated.

LastModifiedBy -> (string)

The Amazon Resource Name (ARN) of the user who last updated the evaluation form.

Tags -> (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

key -> (string)

value -> (string)