# update-chat-controls-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/update-chat-controls-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/update-chat-controls-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# update-chat-controls-configuration

## Description

Updates a set of chat controls configured for an existing Amazon Q Business application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/UpdateChatControlsConfiguration)

## Synopsis

```
update-chat-controls-configuration
--application-id <value>
[--client-token <value>]
[--response-scope <value>]
[--orchestration-configuration <value>]
[--blocked-phrases-configuration-update <value>]
[--topic-configurations-to-create-or-update <value>]
[--topic-configurations-to-delete <value>]
[--creator-mode-configuration <value>]
[--hallucination-reduction-configuration <value>]
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

`--application-id` (string)

The identifier of the application for which the chat controls are configured.

`--client-token` (string)

A token that you provide to identify the request to update a Amazon Q Business application chat configuration.

`--response-scope` (string)

The response scope configured for your application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.

Possible values:

- `ENTERPRISE_CONTENT_ONLY`
- `EXTENDED_KNOWLEDGE_ENABLED`

`--orchestration-configuration` (structure)

The chat response orchestration settings for your application.

control -> (string)

Status information about whether chat orchestration is activated or deactivated for your Amazon Q Business application.

Shorthand Syntax:

```
control=string
```

JSON Syntax:

```
{
  "control": "ENABLED"|"DISABLED"
}
```

`--blocked-phrases-configuration-update` (structure)

The phrases blocked from chat by your chat control configuration.

blockedPhrasesToCreateOrUpdate -> (list)

Creates or updates a blocked phrases configuration in your Amazon Q Business application.

(string)

blockedPhrasesToDelete -> (list)

Deletes a blocked phrases configuration in your Amazon Q Business application.

(string)

systemMessageOverride -> (string)

The configured custom message displayed to your end user when they use blocked phrase during chat.

Shorthand Syntax:

```
blockedPhrasesToCreateOrUpdate=string,string,blockedPhrasesToDelete=string,string,systemMessageOverride=string
```

JSON Syntax:

```
{
  "blockedPhrasesToCreateOrUpdate": ["string", ...],
  "blockedPhrasesToDelete": ["string", ...],
  "systemMessageOverride": "string"
}
```

`--topic-configurations-to-create-or-update` (list)

The configured topic specific chat controls you want to update.

(structure)

The topic specific controls configured for an Amazon Q Business application.

name -> (string)

A name for your topic control configuration.

description -> (string)

A description for your topic control configuration. Use this to outline how the large language model (LLM) should use this topic control configuration.

exampleChatMessages -> (list)

A list of example phrases that you expect the end user to use in relation to the topic.

(string)

rules -> (list)

Rules defined for a topic configuration.

(structure)

Guardrail rules for an Amazon Q Business application. Amazon Q Business supports only one rule at a time.

includedUsersAndGroups -> (structure)

Users and groups to be included in a rule.

userIds -> (list)

The user ids associated with a topic control rule.

(string)

userGroups -> (list)

The user group names associated with a topic control rule.

(string)

excludedUsersAndGroups -> (structure)

Users and groups to be excluded from a rule.

userIds -> (list)

The user ids associated with a topic control rule.

(string)

userGroups -> (list)

The user group names associated with a topic control rule.

(string)

ruleType -> (string)

The type of rule.

ruleConfiguration -> (tagged union structure)

The configuration information for a rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `contentBlockerRule`, `contentRetrievalRule`.

contentBlockerRule -> (structure)

A rule for configuring how Amazon Q Business responds when it encounters a a blocked topic.

systemMessageOverride -> (string)

The configured custom message displayed to an end user informing them that theyâve used a blocked phrase during chat.

contentRetrievalRule -> (structure)

Rules for retrieving content from data sources connected to a Amazon Q Business application for a specific topic control configuration.

eligibleDataSources -> (list)

Specifies data sources in a Amazon Q Business application to use for content generation.

(structure)

The identifier of the data source Amazon Q Business will generate responses from.

indexId -> (string)

The identifier of the index the data source is attached to.

dataSourceId -> (string)

The identifier of the data source.

JSON Syntax:

```
[
  {
    "name": "string",
    "description": "string",
    "exampleChatMessages": ["string", ...],
    "rules": [
      {
        "includedUsersAndGroups": {
          "userIds": ["string", ...],
          "userGroups": ["string", ...]
        },
        "excludedUsersAndGroups": {
          "userIds": ["string", ...],
          "userGroups": ["string", ...]
        },
        "ruleType": "CONTENT_BLOCKER_RULE"|"CONTENT_RETRIEVAL_RULE",
        "ruleConfiguration": {
          "contentBlockerRule": {
            "systemMessageOverride": "string"
          },
          "contentRetrievalRule": {
            "eligibleDataSources": [
              {
                "indexId": "string",
                "dataSourceId": "string"
              }
              ...
            ]
          }
        }
      }
      ...
    ]
  }
  ...
]
```

`--topic-configurations-to-delete` (list)

The configured topic specific chat controls you want to delete.

(structure)

The topic specific controls configured for an Amazon Q Business application.

name -> (string)

A name for your topic control configuration.

description -> (string)

A description for your topic control configuration. Use this to outline how the large language model (LLM) should use this topic control configuration.

exampleChatMessages -> (list)

A list of example phrases that you expect the end user to use in relation to the topic.

(string)

rules -> (list)

Rules defined for a topic configuration.

(structure)

Guardrail rules for an Amazon Q Business application. Amazon Q Business supports only one rule at a time.

includedUsersAndGroups -> (structure)

Users and groups to be included in a rule.

userIds -> (list)

The user ids associated with a topic control rule.

(string)

userGroups -> (list)

The user group names associated with a topic control rule.

(string)

excludedUsersAndGroups -> (structure)

Users and groups to be excluded from a rule.

userIds -> (list)

The user ids associated with a topic control rule.

(string)

userGroups -> (list)

The user group names associated with a topic control rule.

(string)

ruleType -> (string)

The type of rule.

ruleConfiguration -> (tagged union structure)

The configuration information for a rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `contentBlockerRule`, `contentRetrievalRule`.

contentBlockerRule -> (structure)

A rule for configuring how Amazon Q Business responds when it encounters a a blocked topic.

systemMessageOverride -> (string)

The configured custom message displayed to an end user informing them that theyâve used a blocked phrase during chat.

contentRetrievalRule -> (structure)

Rules for retrieving content from data sources connected to a Amazon Q Business application for a specific topic control configuration.

eligibleDataSources -> (list)

Specifies data sources in a Amazon Q Business application to use for content generation.

(structure)

The identifier of the data source Amazon Q Business will generate responses from.

indexId -> (string)

The identifier of the index the data source is attached to.

dataSourceId -> (string)

The identifier of the data source.

JSON Syntax:

```
[
  {
    "name": "string",
    "description": "string",
    "exampleChatMessages": ["string", ...],
    "rules": [
      {
        "includedUsersAndGroups": {
          "userIds": ["string", ...],
          "userGroups": ["string", ...]
        },
        "excludedUsersAndGroups": {
          "userIds": ["string", ...],
          "userGroups": ["string", ...]
        },
        "ruleType": "CONTENT_BLOCKER_RULE"|"CONTENT_RETRIEVAL_RULE",
        "ruleConfiguration": {
          "contentBlockerRule": {
            "systemMessageOverride": "string"
          },
          "contentRetrievalRule": {
            "eligibleDataSources": [
              {
                "indexId": "string",
                "dataSourceId": "string"
              }
              ...
            ]
          }
        }
      }
      ...
    ]
  }
  ...
]
```

`--creator-mode-configuration` (structure)

The configuration details for `CREATOR_MODE` .

creatorModeControl -> (string)

Status information about whether `CREATOR_MODE` has been enabled or disabled. The default status is `DISABLED` .

Shorthand Syntax:

```
creatorModeControl=string
```

JSON Syntax:

```
{
  "creatorModeControl": "ENABLED"|"DISABLED"
}
```

`--hallucination-reduction-configuration` (structure)

The hallucination reduction settings for your application.

hallucinationReductionControl -> (string)

Controls whether hallucination reduction has been enabled or disabled for your application. The default status is `DISABLED` .

Shorthand Syntax:

```
hallucinationReductionControl=string
```

JSON Syntax:

```
{
  "hallucinationReductionControl": "ENABLED"|"DISABLED"
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

None