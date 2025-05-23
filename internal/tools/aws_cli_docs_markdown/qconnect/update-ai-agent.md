# update-ai-agentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-ai-agent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-ai-agent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# update-ai-agent

## Description

Updates an AI Agent.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/UpdateAIAgent)

## Synopsis

```
update-ai-agent
[--client-token <value>]
--assistant-id <value>
--ai-agent-id <value>
--visibility-status <value>
[--configuration <value>]
[--description <value>]
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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) ..

`--assistant-id` (string)

The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.

`--ai-agent-id` (string)

The identifier of the Amazon Q in Connect AI Agent.

`--visibility-status` (string)

The visbility status of the Amazon Q in Connect AI Agent.

Possible values:

- `SAVED`
- `PUBLISHED`

`--configuration` (tagged union structure)

The configuration of the Amazon Q in Connect AI Agent.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `manualSearchAIAgentConfiguration`, `answerRecommendationAIAgentConfiguration`, `selfServiceAIAgentConfiguration`.

manualSearchAIAgentConfiguration -> (structure)

The configuration for AI Agents of type `MANUAL_SEARCH` .

answerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Answer Generation prompt used by the MANUAL_SEARCH AI Agent.

answerGenerationAIGuardrailId -> (string)

The AI Guardrail identifier for the Answer Generation guardrail used by the MANUAL_SEARCH AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

locale -> (string)

The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html) .

answerRecommendationAIAgentConfiguration -> (structure)

The configuration for AI Agents of type `ANSWER_RECOMMENDATION` .

intentLabelingGenerationAIPromptId -> (string)

The AI Prompt identifier for the Intent Labeling prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

queryReformulationAIPromptId -> (string)

The AI Prompt identifier for the Query Reformulation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

answerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Answer Generation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

answerGenerationAIGuardrailId -> (string)

The AI Guardrail identifier for the Answer Generation Guardrail used by the `ANSWER_RECOMMENDATION` AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

locale -> (string)

The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html) .

### Note

Changing this locale to anything other than `en_US` , `en_GB` , or `en_AU` will turn off recommendations triggered by contact transcripts for agent assistance, as this feature is not supported in multiple languages.

selfServiceAIAgentConfiguration -> (structure)

The configuration for AI Agents of type SELF_SERVICE.

selfServicePreProcessingAIPromptId -> (string)

The AI Prompt identifier for the Self Service Pre-Processing prompt used by the SELF_SERVICE AI Agent

selfServiceAnswerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Self Service Answer Generation prompt used by the SELF_SERVICE AI Agent

selfServiceAIGuardrailId -> (string)

The AI Guardrail identifier used by the SELF_SERVICE AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

JSON Syntax:

```
{
  "manualSearchAIAgentConfiguration": {
    "answerGenerationAIPromptId": "string",
    "answerGenerationAIGuardrailId": "string",
    "associationConfigurations": [
      {
        "associationId": "string",
        "associationType": "KNOWLEDGE_BASE",
        "associationConfigurationData": {
          "knowledgeBaseAssociationConfigurationData": {
            "contentTagFilter": {
              "tagCondition": {
                "key": "string",
                "value": "string"
              },
              "andConditions": [
                {
                  "key": "string",
                  "value": "string"
                }
                ...
              ],
              "orConditions": [
                {
                  "andConditions": [
                    {
                      "key": "string",
                      "value": "string"
                    }
                    ...
                  ],
                  "tagCondition": {
                    "key": "string",
                    "value": "string"
                  }
                }
                ...
              ]
            },
            "maxResults": integer,
            "overrideKnowledgeBaseSearchType": "HYBRID"|"SEMANTIC"
          }
        }
      }
      ...
    ],
    "locale": "string"
  },
  "answerRecommendationAIAgentConfiguration": {
    "intentLabelingGenerationAIPromptId": "string",
    "queryReformulationAIPromptId": "string",
    "answerGenerationAIPromptId": "string",
    "answerGenerationAIGuardrailId": "string",
    "associationConfigurations": [
      {
        "associationId": "string",
        "associationType": "KNOWLEDGE_BASE",
        "associationConfigurationData": {
          "knowledgeBaseAssociationConfigurationData": {
            "contentTagFilter": {
              "tagCondition": {
                "key": "string",
                "value": "string"
              },
              "andConditions": [
                {
                  "key": "string",
                  "value": "string"
                }
                ...
              ],
              "orConditions": [
                {
                  "andConditions": [
                    {
                      "key": "string",
                      "value": "string"
                    }
                    ...
                  ],
                  "tagCondition": {
                    "key": "string",
                    "value": "string"
                  }
                }
                ...
              ]
            },
            "maxResults": integer,
            "overrideKnowledgeBaseSearchType": "HYBRID"|"SEMANTIC"
          }
        }
      }
      ...
    ],
    "locale": "string"
  },
  "selfServiceAIAgentConfiguration": {
    "selfServicePreProcessingAIPromptId": "string",
    "selfServiceAnswerGenerationAIPromptId": "string",
    "selfServiceAIGuardrailId": "string",
    "associationConfigurations": [
      {
        "associationId": "string",
        "associationType": "KNOWLEDGE_BASE",
        "associationConfigurationData": {
          "knowledgeBaseAssociationConfigurationData": {
            "contentTagFilter": {
              "tagCondition": {
                "key": "string",
                "value": "string"
              },
              "andConditions": [
                {
                  "key": "string",
                  "value": "string"
                }
                ...
              ],
              "orConditions": [
                {
                  "andConditions": [
                    {
                      "key": "string",
                      "value": "string"
                    }
                    ...
                  ],
                  "tagCondition": {
                    "key": "string",
                    "value": "string"
                  }
                }
                ...
              ]
            },
            "maxResults": integer,
            "overrideKnowledgeBaseSearchType": "HYBRID"|"SEMANTIC"
          }
        }
      }
      ...
    ]
  }
}
```

`--description` (string)

The description of the Amazon Q in Connect AI Agent.

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

aiAgent -> (structure)

The data of the updated Amazon Q in Connect AI Agent.

assistantId -> (string)

The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.

assistantArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

aiAgentId -> (string)

The identifier of the AI Agent.

aiAgentArn -> (string)

The Amazon Resource Name (ARN) of the AI agent.

name -> (string)

The name of the AI Agent.

type -> (string)

The type of the AI Agent.

configuration -> (tagged union structure)

Configuration for the AI Agent.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `manualSearchAIAgentConfiguration`, `answerRecommendationAIAgentConfiguration`, `selfServiceAIAgentConfiguration`.

manualSearchAIAgentConfiguration -> (structure)

The configuration for AI Agents of type `MANUAL_SEARCH` .

answerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Answer Generation prompt used by the MANUAL_SEARCH AI Agent.

answerGenerationAIGuardrailId -> (string)

The AI Guardrail identifier for the Answer Generation guardrail used by the MANUAL_SEARCH AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

locale -> (string)

The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html) .

answerRecommendationAIAgentConfiguration -> (structure)

The configuration for AI Agents of type `ANSWER_RECOMMENDATION` .

intentLabelingGenerationAIPromptId -> (string)

The AI Prompt identifier for the Intent Labeling prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

queryReformulationAIPromptId -> (string)

The AI Prompt identifier for the Query Reformulation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

answerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Answer Generation prompt used by the `ANSWER_RECOMMENDATION` AI Agent.

answerGenerationAIGuardrailId -> (string)

The AI Guardrail identifier for the Answer Generation Guardrail used by the `ANSWER_RECOMMENDATION` AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

locale -> (string)

The locale to which specifies the language and region settings that determine the response language for [QueryAssistant](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html) .

### Note

Changing this locale to anything other than `en_US` , `en_GB` , or `en_AU` will turn off recommendations triggered by contact transcripts for agent assistance, as this feature is not supported in multiple languages.

selfServiceAIAgentConfiguration -> (structure)

The configuration for AI Agents of type SELF_SERVICE.

selfServicePreProcessingAIPromptId -> (string)

The AI Prompt identifier for the Self Service Pre-Processing prompt used by the SELF_SERVICE AI Agent

selfServiceAnswerGenerationAIPromptId -> (string)

The AI Prompt identifier for the Self Service Answer Generation prompt used by the SELF_SERVICE AI Agent

selfServiceAIGuardrailId -> (string)

The AI Guardrail identifier used by the SELF_SERVICE AI Agent.

associationConfigurations -> (list)

The association configurations for overriding behavior on this AI Agent.

(structure)

The configuration for an Amazon Q in Connect Assistant Association.

associationId -> (string)

The identifier of the association for this Association Configuration.

associationType -> (string)

The type of the association for this Association Configuration.

associationConfigurationData -> (tagged union structure)

The data of the configuration for an Amazon Q in Connect Assistant Association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseAssociationConfigurationData`.

knowledgeBaseAssociationConfigurationData -> (structure)

The data of the configuration for a `KNOWLEDGE_BASE` type Amazon Q in Connect Assistant Association.

contentTagFilter -> (tagged union structure)

An object that can be used to specify Tag conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tagCondition`, `andConditions`, `orConditions`.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

orConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(tagged union structure)

A list of conditions which would be applied together with an `OR` condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `andConditions`, `tagCondition`.

andConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

tagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

key -> (string)

The tag key in the tag condition.

value -> (string)

The tag value in the tag condition.

maxResults -> (integer)

The maximum number of results to return per page.

overrideKnowledgeBaseSearchType -> (string)

The search type to be used against the Knowledge Base for this request. The values can be `SEMANTIC` which uses vector embeddings or `HYBRID` which use vector embeddings and raw text

modifiedTime -> (timestamp)

The time the AI Agent was last modified.

description -> (string)

The description of the AI Agent.

visibilityStatus -> (string)

The visibility status of the AI Agent.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

origin -> (string)

Specifies the origin of the AI Agent. `SYSTEM` for a default AI Agent created by Q in Connect or `CUSTOMER` for an AI Agent created by calling AI Agent creation APIs.

status -> (string)

The status of the AI Agent.