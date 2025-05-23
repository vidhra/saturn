# create-prompt-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-prompt-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-prompt-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# create-prompt-version

## Description

Creates a static snapshot of your prompt that can be deployed to production. For more information, see [Deploy prompts using Prompt management by creating versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html) in the Amazon Bedrock User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/CreatePromptVersion)

`create-prompt-version` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-prompt-version
[--client-token <value>]
[--description <value>]
--prompt-identifier <value>
[--tags <value>]
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

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--description` (string)

A description for the version of the prompt.

`--prompt-identifier` (string)

The unique identifier of the prompt that you want to create a version of.

`--tags` (map)

Any tags that you want to attach to the version of the prompt. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html) .

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

arn -> (string)

The Amazon Resource Name (ARN) of the version of the prompt.

createdAt -> (timestamp)

The time at which the prompt was created.

customerEncryptionKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key to encrypt the version of the prompt.

defaultVariant -> (string)

The name of the default variant for the prompt. This value must match the `name` field in the relevant [PromptVariant](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html) object.

description -> (string)

A description for the version.

id -> (string)

The unique identifier of the prompt.

name -> (string)

The name of the prompt.

updatedAt -> (timestamp)

The time at which the prompt was last updated.

variants -> (list)

A list of objects, each containing details about a variant of the prompt.

(structure)

Contains details about a variant of the prompt.

additionalModelRequestFields -> (document)

Contains model-specific inference configurations that arenât in the `inferenceConfiguration` field. To see model-specific inference parameters, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

genAiResource -> (tagged union structure)

Specifies a generative AI resource with which to use the prompt.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agent`.

agent -> (structure)

Specifies an Amazon Bedrock agent with which to use the prompt.

agentIdentifier -> (string)

The ARN of the agent with which to use the prompt.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt variant.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.

text -> (structure)

Contains inference configurations for a text prompt.

maxTokens -> (integer)

The maximum number of tokens to return in the response.

stopSequences -> (list)

A list of strings that define sequences after which the model will stop generating.

(string)

temperature -> (float)

Controls the randomness of the response. Choose a lower value for more predictable outputs and a higher value for more surprising outputs.

topP -> (float)

The percentage of most-likely candidates that the model considers for the next token.

metadata -> (list)

An array of objects, each containing a key-value pair that defines a metadata tag and value to attach to a prompt variant.

(structure)

Contains a key-value pair that defines a metadata tag and value to attach to a prompt variant. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) .

key -> (string)

The key of a metadata tag for a prompt variant.

value -> (string)

The value of a metadata tag for a prompt variant.

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) with which to run inference on the prompt.

name -> (string)

The name of the prompt variant.

templateConfiguration -> (tagged union structure)

Contains configurations for the prompt template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `chat`, `text`.

chat -> (structure)

Contains configurations to use the prompt in a conversational format.

inputVariables -> (list)

An array of the variables in the prompt template.

(structure)

Contains information about a variable in the prompt.

name -> (string)

The name of the variable.

messages -> (list)

Contains messages in the chat for the prompt.

(structure)

A message input or response from a model. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) .

content -> (list)

The content in the message.

(tagged union structure)

Contains the content for the message you pass to, or receive from a model. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cachePoint`, `text`.

cachePoint -> (structure)

Creates a cache checkpoint within a message.

type -> (string)

Indicates that the CachePointBlock is of the default type

text -> (string)

The text in the message.

role -> (string)

The role that the message belongs to.

system -> (list)

Contains system prompts to provide context to the model or to describe how it should behave.

(tagged union structure)

Contains a system prompt to provide context to the model or to describe how it should behave. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cachePoint`, `text`.

cachePoint -> (structure)

Creates a cache checkpoint within a tool designation

type -> (string)

Indicates that the CachePointBlock is of the default type

text -> (string)

The text in the system prompt.

toolConfiguration -> (structure)

Configuration information for the tools that the model can use when generating a response.

toolChoice -> (tagged union structure)

Defines which tools the model should request when invoked.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `any`, `auto`, `tool`.

any -> (structure)

Defines tools, at least one of which must be requested by the model. No text is generated but the results of tool use are sent back to the model to help generate a response.

auto -> (structure)

Defines tools. The model automatically decides whether to call a tool or to generate text instead.

tool -> (structure)

Defines a specific tool that the model must request. No text is generated but the results of tool use are sent back to the model to help generate a response.

name -> (string)

The name of the tool.

tools -> (list)

An array of tools to pass to a model.

(tagged union structure)

Contains configurations for a tool that a model can use when generating a response. For more information, see [Use a tool to complete an Amazon Bedrock model response](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cachePoint`, `toolSpec`.

cachePoint -> (structure)

Creates a cache checkpoint within a tool designation

type -> (string)

Indicates that the CachePointBlock is of the default type

toolSpec -> (structure)

The specification for the tool.

description -> (string)

The description of the tool.

inputSchema -> (tagged union structure)

The input schema for the tool.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `json`.

json -> (document)

A JSON object defining the input schema for the tool.

name -> (string)

The name of the tool.

text -> (structure)

Contains configurations for the text in a message for a prompt.

cachePoint -> (structure)

A cache checkpoint within a template configuration.

type -> (string)

Indicates that the CachePointBlock is of the default type

inputVariables -> (list)

An array of the variables in the prompt template.

(structure)

Contains information about a variable in the prompt.

name -> (string)

The name of the variable.

text -> (string)

The message for the prompt.

templateType -> (string)

The type of prompt template to use.

version -> (string)

The version of the prompt that was created. Versions are numbered incrementally, starting from 1.