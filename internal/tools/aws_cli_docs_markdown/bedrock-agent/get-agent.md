# get-agentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/get-agent.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/get-agent.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# get-agent

## Description

Gets information about an agent.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/GetAgent)

`get-agent` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-agent
--agent-id <value>
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

`--agent-id` (string)

The unique identifier of the agent.

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

agent -> (structure)

Contains details about the agent.

agentArn -> (string)

The Amazon Resource Name (ARN) of the agent.

agentCollaboration -> (string)

The agentâs collaboration settings.

agentId -> (string)

The unique identifier of the agent.

agentName -> (string)

The name of the agent.

agentResourceRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.

agentStatus -> (string)

The status of the agent and whether it is ready for use. The following statuses are possible:

- CREATING â The agent is being created.
- PREPARING â The agent is being prepared.
- PREPARED â The agent is prepared and ready to be invoked.
- NOT_PREPARED â The agent has been created but not yet prepared.
- FAILED â The agent API operation failed.
- UPDATING â The agent is being updated.
- DELETING â The agent is being deleted.

agentVersion -> (string)

The version of the agent.

clientToken -> (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

createdAt -> (timestamp)

The time at which the agent was created.

customOrchestration -> (structure)

Contains custom orchestration configurations for the agent.

executor -> (tagged union structure)

The structure of the executor invoking the actions in custom orchestration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`.

lambda -> (string)

The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action.

customerEncryptionKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key that encrypts the agent.

description -> (string)

The description of the agent.

failureReasons -> (list)

Contains reasons that the agent-related API that you invoked failed.

(string)

foundationModel -> (string)

The foundation model used for orchestration by the agent.

guardrailConfiguration -> (structure)

Details about the guardrail associated with the agent.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

idleSessionTTLInSeconds -> (integer)

The number of seconds for which Amazon Bedrock keeps information about a userâs conversation with the agent.

A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.

instruction -> (string)

Instructions that tell the agent what it should do and how it should interact with users.

memoryConfiguration -> (structure)

Contains memory configuration for the agent.

enabledMemoryTypes -> (list)

The type of memory that is stored.

(string)

sessionSummaryConfiguration -> (structure)

Contains the configuration for SESSION_SUMMARY memory type enabled for the agent.

maxRecentSessions -> (integer)

Maximum number of recent session summaries to include in the agentâs prompt context.

storageDays -> (integer)

The number of days the agent is configured to retain the conversational context.

orchestrationType -> (string)

Specifies the orchestration strategy for the agent.

preparedAt -> (timestamp)

The time at which the agent was last prepared.

promptOverrideConfiguration -> (structure)

Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html) .

overrideLambda -> (string)

The ARN of the Lambda function to use when parsing the raw foundation model output in parts of the agent sequence. If you specify this field, at least one of the `promptConfigurations` must contain a `parserMode` value that is set to `OVERRIDDEN` . For more information, see [Parser Lambda function in Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/lambda-parser.html) .

promptConfigurations -> (list)

Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html) .

(structure)

Contains configurations to override a prompt template in one part of an agent sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html) .

additionalModelRequestFields -> (document)

If the Converse or ConverseStream operations support the model, `additionalModelRequestFields` contains additional inference parameters, beyond the base set of inference parameters in the `inferenceConfiguration` field.

For more information, see *Inference request parameters and response fields for foundation models* in the Amazon Bedrock user guide.

basePromptTemplate -> (string)

Defines the prompt template with which to replace the default prompt template. You can use placeholder variables in the base prompt template to customize the prompt. For more information, see [Prompt template placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html) . For more information, see [Configure the prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-configure.html) .

foundationModel -> (string)

The agentâs foundation model.

inferenceConfiguration -> (structure)

Contains inference parameters to use when the agent invokes a foundation model in the part of the agent sequence defined by the `promptType` . For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

maximumLength -> (integer)

The maximum number of tokens to allow in the generated response.

stopSequences -> (list)

A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.

(string)

temperature -> (float)

The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.

topK -> (integer)

While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for `topK` is the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set `topK` to 50, the model selects the next token from among the top 50 most likely choices.

topP -> (float)

While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for `Top P` determines the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set `topP` to 0.8, the model only selects the next token from the top 80% of the probability distribution of next tokens.

parserMode -> (string)

Specifies whether to override the default parser Lambda function when parsing the raw foundation model output in the part of the agent sequence defined by the `promptType` . If you set the field as `OVERRIDDEN` , the `overrideLambda` field in the [PromptOverrideConfiguration](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptOverrideConfiguration.html) must be specified with the ARN of a Lambda function.

promptCreationMode -> (string)

Specifies whether to override the default prompt template for this `promptType` . Set this value to `OVERRIDDEN` to use the prompt that you provide in the `basePromptTemplate` . If you leave it as `DEFAULT` , the agent uses a default prompt template.

promptState -> (string)

Specifies whether to allow the agent to carry out the step specified in the `promptType` . If you set this value to `DISABLED` , the agent skips that step. The default state for each `promptType` is as follows.

- `PRE_PROCESSING` â `ENABLED`
- `ORCHESTRATION` â `ENABLED`
- `KNOWLEDGE_BASE_RESPONSE_GENERATION` â `ENABLED`
- `POST_PROCESSING` â `DISABLED`

promptType -> (string)

The step in the agent sequence that this prompt configuration applies to.

recommendedActions -> (list)

Contains recommended actions to take for the agent-related API that you invoked to succeed.

(string)

updatedAt -> (timestamp)

The time at which the agent was last updated.