# apply-guardrailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/apply-guardrail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/apply-guardrail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/index.html#cli-aws-bedrock-runtime) ]

# apply-guardrail

## Description

The action to apply a guardrail.

For troubleshooting some of the common errors you might encounter when using the `ApplyGuardrail` API, see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-runtime-2023-09-30/ApplyGuardrail)

## Synopsis

```
apply-guardrail
--guardrail-identifier <value>
--guardrail-version <value>
--source <value>
--content <value>
[--output-scope <value>]
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

The guardrail identifier used in the request to apply the guardrail.

`--guardrail-version` (string)

The guardrail version used in the request to apply the guardrail.

`--source` (string)

The source of data used in the request to apply the guardrail.

Possible values:

- `INPUT`
- `OUTPUT`

`--content` (list)

The content details used in the request to apply the guardrail.

(tagged union structure)

The content block to be evaluated by the guardrail.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`.

text -> (structure)

Text within content block to be evaluated by the guardrail.

text -> (string)

The input text details to be evaluated by the guardrail.

qualifiers -> (list)

The qualifiers describing the text block.

(string)

image -> (structure)

Image within guardrail content block to be evaluated by the guardrail.

format -> (string)

The format details for the file type of the image blocked by the guardrail.

source -> (tagged union structure)

The image source (image bytes) details of the image blocked by the guardrail.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`.

bytes -> (blob)

The bytes details of the guardrail image source. Object used in independent api.

Shorthand Syntax:

```
text={text=string,qualifiers=[string,string]},image={format=string,source={bytes=blob}} ...
```

JSON Syntax:

```
[
  {
    "text": {
      "text": "string",
      "qualifiers": ["grounding_source"|"query"|"guard_content", ...]
    },
    "image": {
      "format": "png"|"jpeg",
      "source": {
        "bytes": blob
      }
    }
  }
  ...
]
```

`--output-scope` (string)

Specifies the scope of the output that you get in the response. Set to `FULL` to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.

Note that the full output scope doesnât apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).

Possible values:

- `INTERVENTIONS`
- `FULL`

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

usage -> (structure)

The usage details in the response from the guardrail.

topicPolicyUnits -> (integer)

The topic policy units processed by the guardrail.

contentPolicyUnits -> (integer)

The content policy units processed by the guardrail.

wordPolicyUnits -> (integer)

The word policy units processed by the guardrail.

sensitiveInformationPolicyUnits -> (integer)

The sensitive information policy units processed by the guardrail.

sensitiveInformationPolicyFreeUnits -> (integer)

The sensitive information policy free units processed by the guardrail.

contextualGroundingPolicyUnits -> (integer)

The contextual grounding policy units processed by the guardrail.

contentPolicyImageUnits -> (integer)

The content policy image units processed by the guardrail.

action -> (string)

The action taken in the response from the guardrail.

actionReason -> (string)

The reason for the action taken when harmful content is detected.

outputs -> (list)

The output details in the response from the guardrail.

(structure)

The output content produced by the guardrail.

text -> (string)

The specific text for the output content produced by the guardrail.

assessments -> (list)

The assessment details in the response from the guardrail.

(structure)

A behavior assessment of the guardrail policies used in a call to the Converse API.

topicPolicy -> (structure)

The topic policy.

topics -> (list)

The topics in the assessment.

(structure)

Information about a topic guardrail.

name -> (string)

The name for the guardrail.

type -> (string)

The type behavior that the guardrail should perform when the model detects the topic.

action -> (string)

The action the guardrail should take when it intervenes on a topic.

detected -> (boolean)

Indicates whether topic content that breaches the guardrail configuration is detected.

contentPolicy -> (structure)

The content policy.

filters -> (list)

The content policy filters.

(structure)

The content filter for a guardrail.

type -> (string)

The guardrail type.

confidence -> (string)

The guardrail confidence.

filterStrength -> (string)

The filter strength setting for the guardrail content filter.

action -> (string)

The guardrail action.

detected -> (boolean)

Indicates whether content that breaches the guardrail configuration is detected.

wordPolicy -> (structure)

The word policy.

customWords -> (list)

Custom words in the assessment.

(structure)

A custom word configured in a guardrail.

match -> (string)

The match for the custom word.

action -> (string)

The action for the custom word.

detected -> (boolean)

Indicates whether custom word content that breaches the guardrail configuration is detected.

managedWordLists -> (list)

Managed word lists in the assessment.

(structure)

A managed word configured in a guardrail.

match -> (string)

The match for the managed word.

type -> (string)

The type for the managed word.

action -> (string)

The action for the managed word.

detected -> (boolean)

Indicates whether managed word content that breaches the guardrail configuration is detected.

sensitiveInformationPolicy -> (structure)

The sensitive information policy.

piiEntities -> (list)

The PII entities in the assessment.

(structure)

A Personally Identifiable Information (PII) entity configured in a guardrail.

match -> (string)

The PII entity filter match.

type -> (string)

The PII entity filter type.

action -> (string)

The PII entity filter action.

detected -> (boolean)

Indicates whether personally identifiable information (PII) that breaches the guardrail configuration is detected.

regexes -> (list)

The regex queries in the assessment.

(structure)

A Regex filter configured in a guardrail.

name -> (string)

The regex filter name.

match -> (string)

The regesx filter match.

regex -> (string)

The regex query.

action -> (string)

The region filter action.

detected -> (boolean)

Indicates whether custom regex entities that breach the guardrail configuration are detected.

contextualGroundingPolicy -> (structure)

The contextual grounding policy used for the guardrail assessment.

filters -> (list)

The filter details for the guardrails contextual grounding filter.

(structure)

The details for the guardrails contextual grounding filter.

type -> (string)

The contextual grounding filter type.

threshold -> (double)

The threshold used by contextual grounding filter to determine whether the content is grounded or not.

score -> (double)

The score generated by contextual grounding filter.

action -> (string)

The action performed by the guardrails contextual grounding filter.

detected -> (boolean)

Indicates whether content that fails the contextual grounding evaluation (grounding or relevance score less than the corresponding threshold) was detected.

invocationMetrics -> (structure)

The invocation metrics for the guardrail assessment.

guardrailProcessingLatency -> (long)

The processing latency details for the guardrail invocation metrics.

usage -> (structure)

The usage details for the guardrail invocation metrics.

topicPolicyUnits -> (integer)

The topic policy units processed by the guardrail.

contentPolicyUnits -> (integer)

The content policy units processed by the guardrail.

wordPolicyUnits -> (integer)

The word policy units processed by the guardrail.

sensitiveInformationPolicyUnits -> (integer)

The sensitive information policy units processed by the guardrail.

sensitiveInformationPolicyFreeUnits -> (integer)

The sensitive information policy free units processed by the guardrail.

contextualGroundingPolicyUnits -> (integer)

The contextual grounding policy units processed by the guardrail.

contentPolicyImageUnits -> (integer)

The content policy image units processed by the guardrail.

guardrailCoverage -> (structure)

The coverage details for the guardrail invocation metrics.

textCharacters -> (structure)

The text characters of the guardrail coverage details.

guarded -> (integer)

The text characters that were guarded by the guardrail coverage.

total -> (integer)

The total text characters by the guardrail coverage.

images -> (structure)

The guardrail coverage for images (the number of images that guardrails guarded).

guarded -> (integer)

The count (integer) of images guardrails guarded.

total -> (integer)

Represents the total number of images (integer) that were in the request (guarded and unguarded).

guardrailCoverage -> (structure)

The guardrail coverage details in the apply guardrail response.

textCharacters -> (structure)

The text characters of the guardrail coverage details.

guarded -> (integer)

The text characters that were guarded by the guardrail coverage.

total -> (integer)

The total text characters by the guardrail coverage.

images -> (structure)

The guardrail coverage for images (the number of images that guardrails guarded).

guarded -> (integer)

The count (integer) of images guardrails guarded.

total -> (integer)

Represents the total number of images (integer) that were in the request (guarded and unguarded).