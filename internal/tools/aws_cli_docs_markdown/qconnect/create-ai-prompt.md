# create-ai-promptÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/create-ai-prompt.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/create-ai-prompt.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# create-ai-prompt

## Description

Creates an Amazon Q in Connect AI Prompt.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/CreateAIPrompt)

## Synopsis

```
create-ai-prompt
[--client-token <value>]
--assistant-id <value>
--name <value>
--type <value>
--template-configuration <value>
--visibility-status <value>
--template-type <value>
--model-id <value>
--api-format <value>
[--tags <value>]
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

`--name` (string)

The name of the AI Prompt.

`--type` (string)

The type of this AI Prompt.

Possible values:

- `ANSWER_GENERATION`
- `INTENT_LABELING_GENERATION`
- `QUERY_REFORMULATION`
- `SELF_SERVICE_PRE_PROCESSING`
- `SELF_SERVICE_ANSWER_GENERATION`

`--template-configuration` (tagged union structure)

The configuration of the prompt template for this AI Prompt.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `textFullAIPromptEditTemplateConfiguration`.

textFullAIPromptEditTemplateConfiguration -> (structure)

The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

text -> (string)

The YAML text for the AI Prompt template.

Shorthand Syntax:

```
textFullAIPromptEditTemplateConfiguration={text=string}
```

JSON Syntax:

```
{
  "textFullAIPromptEditTemplateConfiguration": {
    "text": "string"
  }
}
```

`--visibility-status` (string)

The visibility status of the AI Prompt.

Possible values:

- `SAVED`
- `PUBLISHED`

`--template-type` (string)

The type of the prompt template for this AI Prompt.

Possible values:

- `TEXT`

`--model-id` (string)

The identifier of the model used for this AI Prompt.

`--api-format` (string)

The API Format of the AI Prompt.

Recommended values: `MESSAGES | TEXT_COMPLETIONS`

### Note

The values `ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS` will be deprecated.

Possible values:

- `ANTHROPIC_CLAUDE_MESSAGES`
- `ANTHROPIC_CLAUDE_TEXT_COMPLETIONS`
- `MESSAGES`
- `TEXT_COMPLETIONS`

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--description` (string)

The description of the AI Prompt.

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

aiPrompt -> (structure)

The data of the AI Prompt.

assistantId -> (string)

The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.

assistantArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

aiPromptId -> (string)

The identifier of the Amazon Q in Connect AI prompt.

aiPromptArn -> (string)

The Amazon Resource Name (ARN) of the AI Prompt.

name -> (string)

The name of the AI Prompt

type -> (string)

The type of this AI Prompt.

templateType -> (string)

The type of the prompt template for this AI Prompt.

modelId -> (string)

The identifier of the model used for this AI Prompt. The following model Ids are supported:

- `anthropic.claude-3-haiku--v1:0`
- `apac.amazon.nova-lite-v1:0`
- `apac.amazon.nova-micro-v1:0`
- `apac.amazon.nova-pro-v1:0`
- `apac.anthropic.claude-3-5-sonnet--v2:0`
- `apac.anthropic.claude-3-haiku-20240307-v1:0`
- `eu.amazon.nova-lite-v1:0`
- `eu.amazon.nova-micro-v1:0`
- `eu.amazon.nova-pro-v1:0`
- `eu.anthropic.claude-3-7-sonnet-20250219-v1:0`
- `eu.anthropic.claude-3-haiku-20240307-v1:0`
- `us.amazon.nova-lite-v1:0`
- `us.amazon.nova-micro-v1:0`
- `us.amazon.nova-pro-v1:0`
- `us.anthropic.claude-3-5-haiku-20241022-v1:0`
- `us.anthropic.claude-3-7-sonnet-20250219-v1:0`
- `us.anthropic.claude-3-haiku-20240307-v1:0`

apiFormat -> (string)

The API format used for this AI Prompt.

templateConfiguration -> (tagged union structure)

The configuration of the prompt template for this AI Prompt.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `textFullAIPromptEditTemplateConfiguration`.

textFullAIPromptEditTemplateConfiguration -> (structure)

The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

text -> (string)

The YAML text for the AI Prompt template.

modifiedTime -> (timestamp)

The time the AI Prompt was last modified.

description -> (string)

The description of the AI Prompt.

visibilityStatus -> (string)

The visibility status of the AI Prompt.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

origin -> (string)

The origin of the AI Prompt. `SYSTEM` for a default AI Prompt created by Q in Connect or `CUSTOMER` for an AI Prompt created by calling AI Prompt creation APIs.

status -> (string)

The status of the AI Prompt.