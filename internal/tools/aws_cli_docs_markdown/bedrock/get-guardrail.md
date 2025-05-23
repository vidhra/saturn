# get-guardrailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/get-guardrail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/get-guardrail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# get-guardrail

## Description

Gets details about a guardrail. If you donât specify a version, the response returns details for the `DRAFT` version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/GetGuardrail)

## Synopsis

```
get-guardrail
--guardrail-identifier <value>
[--guardrail-version <value>]
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

`--guardrail-identifier` (string)

The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.

`--guardrail-version` (string)

The version of the guardrail for which to get details. If you donât specify a version, the response returns details for the `DRAFT` version.

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

name -> (string)

The name of the guardrail.

description -> (string)

The description of the guardrail.

guardrailId -> (string)

The unique identifier of the guardrail.

guardrailArn -> (string)

The ARN of the guardrail.

version -> (string)

The version of the guardrail.

status -> (string)

The status of the guardrail.

topicPolicy -> (structure)

The topic policy that was configured for the guardrail.

topics -> (list)

A list of policies related to topics that the guardrail should deny.

(structure)

Details about topics for the guardrail to identify and deny.

This data type is used in the following API operations:

- [GetGuardrail response body](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax)

name -> (string)

The name of the topic to deny.

definition -> (string)

A definition of the topic to deny.

examples -> (list)

A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.

(string)

type -> (string)

Specifies to deny the topic.

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

contentPolicy -> (structure)

The content policy that was configured for the guardrail.

filters -> (list)

Contains the type of the content filter and how strongly it should apply to prompts and model responses.

(structure)

Contains filter strengths for harmful content. Guardrails support the following content filters to detect and filter harmful user inputs and FM-generated outputs.

- **Hate** â Describes language or a statement that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
- **Insults** â Describes language or a statement that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
- **Sexual** â Describes language or a statement that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
- **Violence** â Describes language or a statement that includes glorification of or threats to inflict physical pain, hurt, or injury toward a person, group or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

For more information, see [Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-filters.html) .

This data type is used in the following API operations:

- [GetGuardrail response body](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetGuardrail.html#API_GetGuardrail_ResponseSyntax)

type -> (string)

The harmful category that the content filter is applied to.

inputStrength -> (string)

The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

outputStrength -> (string)

The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.

inputModalities -> (list)

The input modalities selected for the guardrail content filter.

(string)

outputModalities -> (list)

The output modalities selected for the guardrail content filter.

(string)

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

wordPolicy -> (structure)

The word policy that was configured for the guardrail.

words -> (list)

A list of words configured for the guardrail.

(structure)

A word configured for the guardrail.

text -> (string)

Text of the word configured for the guardrail to block.

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

managedWordLists -> (list)

A list of managed words configured for the guardrail.

(structure)

The managed word list that was configured for the guardrail. (This is a list of words that are pre-defined and managed by guardrails only.)

type -> (string)

ManagedWords$type The managed word type that was configured for the guardrail. (For now, we only offer profanity word list)

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

sensitiveInformationPolicy -> (structure)

The sensitive information policy that was configured for the guardrail.

piiEntities -> (list)

The list of PII entities configured for the guardrail.

(structure)

The PII entity configured for the guardrail.

type -> (string)

The type of PII entity. For example, Social Security Number.

action -> (string)

The configured guardrail action when PII entity is detected.

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `ANONYMIZE` â Mask the content and replace it with identifier tags.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `ANONYMIZE` â Mask the content and replace it with identifier tags.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

regexes -> (list)

The list of regular expressions configured for the guardrail.

(structure)

The regular expression configured for the guardrail.

name -> (string)

The name of the regular expression for the guardrail.

description -> (string)

The description of the regular expression for the guardrail.

pattern -> (string)

The pattern of the regular expression configured for the guardrail.

action -> (string)

The action taken when a match to the regular expression is detected.

inputAction -> (string)

The action to take when harmful content is detected in the input. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

outputAction -> (string)

The action to take when harmful content is detected in the output. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

inputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the input. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

outputEnabled -> (boolean)

Indicates whether guardrail evaluation is enabled on the output. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

contextualGroundingPolicy -> (structure)

The contextual grounding policy used in the guardrail.

filters -> (list)

The filter details for the guardrails contextual grounding policy.

(structure)

The details for the guardrails contextual grounding filter.

type -> (string)

The filter type details for the guardrails contextual grounding filter.

threshold -> (double)

The threshold details for the guardrails contextual grounding filter.

action -> (string)

The action to take when content fails the contextual grounding evaluation. Supported values include:

- `BLOCK` â Block the content and replace it with blocked messaging.
- `NONE` â Take no action but return detection information in the trace response.

enabled -> (boolean)

Indicates whether contextual grounding is enabled for evaluation. When disabled, you arenât charged for the evaluation. The evaluation doesnât appear in the response.

crossRegionDetails -> (structure)

Details about the system-defined guardrail profile that youâre using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).

guardrailProfileId -> (string)

The ID of the guardrail profile that your guardrail is using. Profile availability depends on your current Amazon Web Services Region. For more information, see the [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html) .

guardrailProfileArn -> (string)

The Amazon Resource Name (ARN) of the guardrail profile that youâre using with your guardrail.

createdAt -> (timestamp)

The date and time at which the guardrail was created.

updatedAt -> (timestamp)

The date and time at which the guardrail was updated.

statusReasons -> (list)

Appears if the `status` is `FAILED` . A list of reasons for why the guardrail failed to be created, updated, versioned, or deleted.

(string)

failureRecommendations -> (list)

Appears if the `status` of the guardrail is `FAILED` . A list of recommendations to carry out before retrying the request.

(string)

blockedInputMessaging -> (string)

The message that the guardrail returns when it blocks a prompt.

blockedOutputsMessaging -> (string)

The message that the guardrail returns when it blocks a model response.

kmsKeyArn -> (string)

The ARN of the KMS key that encrypts the guardrail.