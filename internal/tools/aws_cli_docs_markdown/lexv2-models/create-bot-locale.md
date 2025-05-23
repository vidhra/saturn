# create-bot-localeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-locale.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-locale.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# create-bot-locale

## Description

Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/CreateBotLocale)

## Synopsis

```
create-bot-locale
--bot-id <value>
--bot-version <value>
--locale-id <value>
[--description <value>]
--nlu-intent-confidence-threshold <value>
[--voice-settings <value>]
[--generative-ai-settings <value>]
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

`--bot-id` (string)

The identifier of the bot to create the locale for.

`--bot-version` (string)

The version of the bot to create the locale for. This can only be the draft version of the bot.

`--locale-id` (string)

The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html) .

`--description` (string)

A description of the bot locale. Use this to help identify the bot locale in lists.

`--nlu-intent-confidence-threshold` (double)

Determines the threshold where Amazon Lex will insert the `AMAZON.FallbackIntent` , `AMAZON.KendraSearchIntent` , or both when returning alternative intents. `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` are only inserted if they are configured for the bot.

For example, suppose a bot is configured with the confidence threshold of 0.80 and the `AMAZON.FallbackIntent` . Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the `RecognizeText` operation would be:

- AMAZON.FallbackIntent
- IntentA
- IntentB
- IntentC

`--voice-settings` (structure)

The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.

voiceId -> (string)

The identifier of the Amazon Polly voice to use.

engine -> (string)

Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the ` `engine` parameter of the `SynthesizeSpeech` operation <[https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine)>`__ in the *Amazon Polly developer guide* .

If you do not specify a value, the default is `standard` .

Shorthand Syntax:

```
voiceId=string,engine=string
```

JSON Syntax:

```
{
  "voiceId": "string",
  "engine": "standard"|"neural"|"long-form"|"generative"
}
```

`--generative-ai-settings` (structure)

Contains specifications about the generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

runtimeSettings -> (structure)

Contains specifications about the Amazon Lex runtime generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

slotResolutionImprovement -> (structure)

An object containing specifications for the assisted slot resolution feature.

enabled -> (boolean)

Specifies whether assisted slot resolution is turned on or off.

bedrockModelSpecification -> (structure)

An object containing information about the Amazon Bedrock model used to assist slot resolution.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

buildtimeSettings -> (structure)

Contains specifications about the Amazon Lex build time generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

descriptiveBotBuilder -> (structure)

An object containing specifications for the descriptive bot building feature.

enabled -> (boolean)

Specifies whether the descriptive bot building feature is activated or not.

bedrockModelSpecification -> (structure)

An object containing information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

sampleUtteranceGeneration -> (structure)

Contains specifications for the sample utterance generation feature.

enabled -> (boolean)

Specifies whether to enable sample utterance generation or not.

bedrockModelSpecification -> (structure)

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

JSON Syntax:

```
{
  "runtimeSettings": {
    "slotResolutionImprovement": {
      "enabled": true|false,
      "bedrockModelSpecification": {
        "modelArn": "string",
        "guardrail": {
          "identifier": "string",
          "version": "string"
        },
        "traceStatus": "ENABLED"|"DISABLED",
        "customPrompt": "string"
      }
    }
  },
  "buildtimeSettings": {
    "descriptiveBotBuilder": {
      "enabled": true|false,
      "bedrockModelSpecification": {
        "modelArn": "string",
        "guardrail": {
          "identifier": "string",
          "version": "string"
        },
        "traceStatus": "ENABLED"|"DISABLED",
        "customPrompt": "string"
      }
    },
    "sampleUtteranceGeneration": {
      "enabled": true|false,
      "bedrockModelSpecification": {
        "modelArn": "string",
        "guardrail": {
          "identifier": "string",
          "version": "string"
        },
        "traceStatus": "ENABLED"|"DISABLED",
        "customPrompt": "string"
      }
    }
  }
}
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

botId -> (string)

The specified bot identifier.

botVersion -> (string)

The specified bot version.

localeName -> (string)

The specified locale name.

localeId -> (string)

The specified locale identifier.

description -> (string)

The specified description of the bot locale.

nluIntentConfidenceThreshold -> (double)

The specified confidence threshold for inserting the `AMAZON.FallbackIntent` and `AMAZON.KendraSearchIntent` intents.

voiceSettings -> (structure)

The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.

voiceId -> (string)

The identifier of the Amazon Polly voice to use.

engine -> (string)

Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the ` `engine` parameter of the `SynthesizeSpeech` operation <[https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine)>`__ in the *Amazon Polly developer guide* .

If you do not specify a value, the default is `standard` .

botLocaleStatus -> (string)

The status of the bot.

When the status is `Creating` the bot locale is being configured. When the status is `Building` Amazon Lex is building the bot for testing and use.

If the status of the bot is `ReadyExpressTesting` , you can test the bot using the exact utterances specified in the botsâ intents. When the bot is ready for full testing or to run, the status is `Built` .

If there was a problem with building the bot, the status is `Failed` . If the bot was saved but not built, the status is `NotBuilt` .

creationDateTime -> (timestamp)

A timestamp specifying the date and time that the bot locale was created.

generativeAISettings -> (structure)

Contains specifications about the generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

runtimeSettings -> (structure)

Contains specifications about the Amazon Lex runtime generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

slotResolutionImprovement -> (structure)

An object containing specifications for the assisted slot resolution feature.

enabled -> (boolean)

Specifies whether assisted slot resolution is turned on or off.

bedrockModelSpecification -> (structure)

An object containing information about the Amazon Bedrock model used to assist slot resolution.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

buildtimeSettings -> (structure)

Contains specifications about the Amazon Lex build time generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

descriptiveBotBuilder -> (structure)

An object containing specifications for the descriptive bot building feature.

enabled -> (boolean)

Specifies whether the descriptive bot building feature is activated or not.

bedrockModelSpecification -> (structure)

An object containing information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.

sampleUtteranceGeneration -> (structure)

Contains specifications for the sample utterance generation feature.

enabled -> (boolean)

Specifies whether to enable sample utterance generation or not.

bedrockModelSpecification -> (structure)

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

modelArn -> (string)

The ARN of the foundation model used in descriptive bot building.

guardrail -> (structure)

The guardrail configuration in the Bedrock model specification details.

identifier -> (string)

The unique guardrail id for the Bedrock guardrail configuration.

version -> (string)

The guardrail version for the Bedrock guardrail configuration.

traceStatus -> (string)

The Bedrock trace status in the Bedrock model specification details.

customPrompt -> (string)

The custom prompt used in the Bedrock model specification details.