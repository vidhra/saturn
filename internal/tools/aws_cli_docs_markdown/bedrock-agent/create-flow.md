# create-flowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-flow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/create-flow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# create-flow

## Description

Creates a prompt flow that you can use to send an input through various steps to yield an output. Configure nodes, each of which corresponds to a step of the flow, and create connections between the nodes to create paths to different outputs. For more information, see [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html) and [Create a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html) in the Amazon Bedrock User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/CreateFlow)

`create-flow` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-flow
[--client-token <value>]
[--customer-encryption-key-arn <value>]
[--definition <value>]
[--description <value>]
--execution-role-arn <value>
--name <value>
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

`--customer-encryption-key-arn` (string)

The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.

`--definition` (structure)

A definition of the nodes and connections between nodes in the flow.

connections -> (list)

An array of connection definitions in the flow.

(structure)

Contains information about a connection between two nodes in the flow.

configuration -> (tagged union structure)

The configuration of the connection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conditional`, `data`.

conditional -> (structure)

The configuration of a connection originating from a Condition node.

condition -> (string)

The condition that triggers this connection. For more information about how to write conditions, see the **Condition** node type in the [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html) topic in the Amazon Bedrock User Guide.

data -> (structure)

The configuration of a connection originating from a node that isnât a Condition node.

sourceOutput -> (string)

The name of the output in the source node that the connection begins from.

targetInput -> (string)

The name of the input in the target node that the connection ends at.

name -> (string)

A name for the connection that you can reference.

source -> (string)

The node that the connection starts at.

target -> (string)

The node that the connection ends at.

type -> (string)

Whether the source node that the connection begins from is a condition node (`Conditional` ) or not (`Data` ).

nodes -> (list)

An array of node definitions in the flow.

(structure)

Contains configurations about a node in the flow.

configuration -> (tagged union structure)

Contains configurations for the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agent`, `collector`, `condition`, `inlineCode`, `input`, `iterator`, `knowledgeBase`, `lambdaFunction`, `lex`, `loop`, `loopController`, `loopInput`, `output`, `prompt`, `retrieval`, `storage`.

agent -> (structure)

Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.

agentAliasArn -> (string)

The Amazon Resource Name (ARN) of the alias of the agent to invoke.

collector -> (structure)

Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.

condition -> (structure)

Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.

conditions -> (list)

An array of conditions. Each member contains the name of a condition and an expression that defines the condition.

(structure)

Defines a condition in the condition node.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

inlineCode -> (structure)

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

code -> (string)

The code thatâs executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.

The code must be valid in the programming `language` that you specify.

language -> (string)

The programming language used by your inline code node.

The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3` ) is supported.

input -> (structure)

Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` canât be specified for this node.

iterator -> (structure)

Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.

The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.

knowledgeBase -> (structure)

Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

knowledgeBaseId -> (string)

The unique identifier of the knowledge base to query.

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.

numberOfResults -> (integer)

The number of results to retrieve from the knowledge base.

orchestrationConfiguration -> (structure)

The configuration for orchestrating the retrieval and generation process in the knowledge base node.

additionalModelRequestFields -> (map)

The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.

key -> (string)

value -> (document)

inferenceConfig -> (tagged union structure)

Contains inference configurations for the prompt.

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

performanceConfig -> (structure)

The performance configuration options for the knowledge base retrieval and generation process.

latency -> (string)

The latency optimization setting.

promptTemplate -> (structure)

A custom prompt template for orchestrating the retrieval and generation process.

textPromptTemplate -> (string)

The text of the prompt template.

promptTemplate -> (structure)

A custom prompt template to use with the knowledge base for generating responses.

textPromptTemplate -> (string)

The text of the prompt template.

rerankingConfiguration -> (structure)

The configuration for reranking the retrieved results from the knowledge base to improve relevance.

bedrockRerankingConfiguration -> (structure)

Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.

metadataConfiguration -> (structure)

Specifies how metadata fields should be handled during the reranking process.

selectionMode -> (string)

The mode for selecting metadata fields for reranking.

selectiveModeConfiguration -> (tagged union structure)

The configuration for selective metadata field inclusion or exclusion during reranking.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldsToExclude`, `fieldsToInclude`.

fieldsToExclude -> (list)

Specifies the metadata fields to exclude from the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

fieldsToInclude -> (list)

Specifies the metadata fields to include in the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

modelConfiguration -> (structure)

Specifies the configuration for the Amazon Bedrock reranker model.

additionalModelRequestFields -> (map)

Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.

key -> (string)

value -> (document)

modelArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.

numberOfRerankedResults -> (integer)

Specifies the number of results to return after reranking.

type -> (string)

Specifies the type of reranking model to use. Currently, the only supported value is `BEDROCK_RERANKING_MODEL` .

lambdaFunction -> (structure)

Contains configurations for a Lambda function node in your flow. Invokes an Lambda function.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function to invoke.

lex -> (structure)

Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.

botAliasArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.

localeId -> (string)

The Region to invoke the Amazon Lex bot in.

loop -> (structure)

Contains configurations for a DoWhile loop in your flow.

definition -> (structure)

The definition of the DoWhile loop nodes and connections between nodes in the flow.

connections -> (list)

An array of connection definitions in the flow.

(structure)

Contains information about a connection between two nodes in the flow.

configuration -> (tagged union structure)

The configuration of the connection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conditional`, `data`.

conditional -> (structure)

The configuration of a connection originating from a Condition node.

condition -> (string)

The condition that triggers this connection. For more information about how to write conditions, see the **Condition** node type in the [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html) topic in the Amazon Bedrock User Guide.

data -> (structure)

The configuration of a connection originating from a node that isnât a Condition node.

sourceOutput -> (string)

The name of the output in the source node that the connection begins from.

targetInput -> (string)

The name of the input in the target node that the connection ends at.

name -> (string)

A name for the connection that you can reference.

source -> (string)

The node that the connection starts at.

target -> (string)

The node that the connection ends at.

type -> (string)

Whether the source node that the connection begins from is a condition node (`Conditional` ) or not (`Data` ).

nodes -> (list)

An array of node definitions in the flow.

(structure)

Contains configurations about a node in the flow.

configuration -> (tagged union structure)

Contains configurations for the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agent`, `collector`, `condition`, `inlineCode`, `input`, `iterator`, `knowledgeBase`, `lambdaFunction`, `lex`, `loop`, `loopController`, `loopInput`, `output`, `prompt`, `retrieval`, `storage`.

agent -> (structure)

Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.

agentAliasArn -> (string)

The Amazon Resource Name (ARN) of the alias of the agent to invoke.

collector -> (structure)

Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.

condition -> (structure)

Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.

conditions -> (list)

An array of conditions. Each member contains the name of a condition and an expression that defines the condition.

(structure)

Defines a condition in the condition node.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

inlineCode -> (structure)

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

code -> (string)

The code thatâs executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.

The code must be valid in the programming `language` that you specify.

language -> (string)

The programming language used by your inline code node.

The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3` ) is supported.

input -> (structure)

Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` canât be specified for this node.

iterator -> (structure)

Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.

The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.

knowledgeBase -> (structure)

Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

knowledgeBaseId -> (string)

The unique identifier of the knowledge base to query.

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.

numberOfResults -> (integer)

The number of results to retrieve from the knowledge base.

orchestrationConfiguration -> (structure)

The configuration for orchestrating the retrieval and generation process in the knowledge base node.

additionalModelRequestFields -> (map)

The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.

key -> (string)

value -> (document)

inferenceConfig -> (tagged union structure)

Contains inference configurations for the prompt.

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

performanceConfig -> (structure)

The performance configuration options for the knowledge base retrieval and generation process.

latency -> (string)

The latency optimization setting.

promptTemplate -> (structure)

A custom prompt template for orchestrating the retrieval and generation process.

textPromptTemplate -> (string)

The text of the prompt template.

promptTemplate -> (structure)

A custom prompt template to use with the knowledge base for generating responses.

textPromptTemplate -> (string)

The text of the prompt template.

rerankingConfiguration -> (structure)

The configuration for reranking the retrieved results from the knowledge base to improve relevance.

bedrockRerankingConfiguration -> (structure)

Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.

metadataConfiguration -> (structure)

Specifies how metadata fields should be handled during the reranking process.

selectionMode -> (string)

The mode for selecting metadata fields for reranking.

selectiveModeConfiguration -> (tagged union structure)

The configuration for selective metadata field inclusion or exclusion during reranking.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldsToExclude`, `fieldsToInclude`.

fieldsToExclude -> (list)

Specifies the metadata fields to exclude from the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

fieldsToInclude -> (list)

Specifies the metadata fields to include in the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

modelConfiguration -> (structure)

Specifies the configuration for the Amazon Bedrock reranker model.

additionalModelRequestFields -> (map)

Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.

key -> (string)

value -> (document)

modelArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.

numberOfRerankedResults -> (integer)

Specifies the number of results to return after reranking.

type -> (string)

Specifies the type of reranking model to use. Currently, the only supported value is `BEDROCK_RERANKING_MODEL` .

lambdaFunction -> (structure)

Contains configurations for a Lambda function node in your flow. Invokes an Lambda function.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function to invoke.

lex -> (structure)

Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.

botAliasArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.

localeId -> (string)

The Region to invoke the Amazon Lex bot in.

loop -> (structure)

Contains configurations for a DoWhile loop in your flow.

( â¦ recursive â¦ )

loopController -> (structure)

Contains controller node configurations for a DoWhile loop in your flow.

continueCondition -> (structure)

Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

maxIterations -> (integer)

Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.

loopInput -> (structure)

Contains input node configurations for a DoWhile loop in your flow.

output -> (structure)

Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` canât be specified for this node.

prompt -> (structure)

Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

sourceConfiguration -> (tagged union structure)

Specifies whether the prompt is from Prompt management or defined inline.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `inline`, `resource`.

inline -> (structure)

Contains configurations for a prompt that is defined inline

additionalModelRequestFields -> (document)

Additional fields to be included in the model request for the Prompt node.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.

templateConfiguration -> (tagged union structure)

Contains a prompt and variables in the prompt that can be replaced with values at runtime.

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

The type of prompt template.

resource -> (structure)

Contains configurations for a prompt from Prompt management.

promptArn -> (string)

The Amazon Resource Name (ARN) of the prompt from Prompt management.

retrieval -> (structure)

Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for retrieving data to return as the output from the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.

bucketName -> (string)

The name of the Amazon S3 bucket from which to retrieve data.

storage -> (structure)

Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for storing the input into the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location in which to store the input into the node.

bucketName -> (string)

The name of the Amazon S3 bucket in which to store the input into the node.

inputs -> (list)

An array of objects, each of which contains information about an input into the node.

(structure)

Contains configurations for an input in an Amazon Bedrock Flows node.

category -> (string)

Specifies how input data flows between iterations in a DoWhile loop.

- `LoopCondition` - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue.
- `ReturnValueToLoopStart` - Defines data to pass back to the start of the loopâs next iteration. Use this category for variables that you want to update for each loop iteration.
- `ExitLoop` - Defines the value thatâs available once the loop ends. Use this category to expose loop results to nodes outside the loop.

expression -> (string)

An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html) .

name -> (string)

Specifies a name for the input that you can reference.

type -> (string)

Specifies the data type of the input. If the input doesnât match this type at runtime, a validation error will be thrown.

name -> (string)

A name for the node.

outputs -> (list)

A list of objects, each of which contains information about an output from the node.

(structure)

Contains configurations for an output from a node.

name -> (string)

A name for the output that you can reference.

type -> (string)

The data type of the output. If the output doesnât match this type at runtime, a validation error will be thrown.

type -> (string)

The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.

loopController -> (structure)

Contains controller node configurations for a DoWhile loop in your flow.

continueCondition -> (structure)

Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

maxIterations -> (integer)

Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.

loopInput -> (structure)

Contains input node configurations for a DoWhile loop in your flow.

output -> (structure)

Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` canât be specified for this node.

prompt -> (structure)

Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

sourceConfiguration -> (tagged union structure)

Specifies whether the prompt is from Prompt management or defined inline.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `inline`, `resource`.

inline -> (structure)

Contains configurations for a prompt that is defined inline

additionalModelRequestFields -> (document)

Additional fields to be included in the model request for the Prompt node.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.

templateConfiguration -> (tagged union structure)

Contains a prompt and variables in the prompt that can be replaced with values at runtime.

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

The type of prompt template.

resource -> (structure)

Contains configurations for a prompt from Prompt management.

promptArn -> (string)

The Amazon Resource Name (ARN) of the prompt from Prompt management.

retrieval -> (structure)

Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for retrieving data to return as the output from the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.

bucketName -> (string)

The name of the Amazon S3 bucket from which to retrieve data.

storage -> (structure)

Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for storing the input into the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location in which to store the input into the node.

bucketName -> (string)

The name of the Amazon S3 bucket in which to store the input into the node.

inputs -> (list)

An array of objects, each of which contains information about an input into the node.

(structure)

Contains configurations for an input in an Amazon Bedrock Flows node.

category -> (string)

Specifies how input data flows between iterations in a DoWhile loop.

- `LoopCondition` - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue.
- `ReturnValueToLoopStart` - Defines data to pass back to the start of the loopâs next iteration. Use this category for variables that you want to update for each loop iteration.
- `ExitLoop` - Defines the value thatâs available once the loop ends. Use this category to expose loop results to nodes outside the loop.

expression -> (string)

An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html) .

name -> (string)

Specifies a name for the input that you can reference.

type -> (string)

Specifies the data type of the input. If the input doesnât match this type at runtime, a validation error will be thrown.

name -> (string)

A name for the node.

outputs -> (list)

A list of objects, each of which contains information about an output from the node.

(structure)

Contains configurations for an output from a node.

name -> (string)

A name for the output that you can reference.

type -> (string)

The data type of the output. If the output doesnât match this type at runtime, a validation error will be thrown.

type -> (string)

The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.

JSON Syntax:

```
{
  "connections": [
    {
      "configuration": {
        "conditional": {
          "condition": "string"
        },
        "data": {
          "sourceOutput": "string",
          "targetInput": "string"
        }
      },
      "name": "string",
      "source": "string",
      "target": "string",
      "type": "Data"|"Conditional"
    }
    ...
  ],
  "nodes": [
    {
      "configuration": {
        "agent": {
          "agentAliasArn": "string"
        },
        "collector": {

        },
        "condition": {
          "conditions": [
            {
              "expression": "string",
              "name": "string"
            }
            ...
          ]
        },
        "inlineCode": {
          "code": "string",
          "language": "Python_3"
        },
        "input": {

        },
        "iterator": {

        },
        "knowledgeBase": {
          "guardrailConfiguration": {
            "guardrailIdentifier": "string",
            "guardrailVersion": "string"
          },
          "inferenceConfiguration": {
            "text": {
              "maxTokens": integer,
              "stopSequences": ["string", ...],
              "temperature": float,
              "topP": float
            }
          },
          "knowledgeBaseId": "string",
          "modelId": "string",
          "numberOfResults": integer,
          "orchestrationConfiguration": {
            "additionalModelRequestFields": {"string": {...}
              ...},
            "inferenceConfig": {
              "text": {
                "maxTokens": integer,
                "stopSequences": ["string", ...],
                "temperature": float,
                "topP": float
              }
            },
            "performanceConfig": {
              "latency": "standard"|"optimized"
            },
            "promptTemplate": {
              "textPromptTemplate": "string"
            }
          },
          "promptTemplate": {
            "textPromptTemplate": "string"
          },
          "rerankingConfiguration": {
            "bedrockRerankingConfiguration": {
              "metadataConfiguration": {
                "selectionMode": "SELECTIVE"|"ALL",
                "selectiveModeConfiguration": {
                  "fieldsToExclude": [
                    {
                      "fieldName": "string"
                    }
                    ...
                  ],
                  "fieldsToInclude": [
                    {
                      "fieldName": "string"
                    }
                    ...
                  ]
                }
              },
              "modelConfiguration": {
                "additionalModelRequestFields": {"string": {...}
                  ...},
                "modelArn": "string"
              },
              "numberOfRerankedResults": integer
            },
            "type": "BEDROCK_RERANKING_MODEL"
          }
        },
        "lambdaFunction": {
          "lambdaArn": "string"
        },
        "lex": {
          "botAliasArn": "string",
          "localeId": "string"
        },
        "loop": {
          "definition": {
            "connections": [
              {
                "configuration": {
                  "conditional": {
                    "condition": "string"
                  },
                  "data": {
                    "sourceOutput": "string",
                    "targetInput": "string"
                  }
                },
                "name": "string",
                "source": "string",
                "target": "string",
                "type": "Data"|"Conditional"
              }
              ...
            ],
            "nodes": [
              {
                "configuration": {
                  "agent": {
                    "agentAliasArn": "string"
                  },
                  "collector": {

                  },
                  "condition": {
                    "conditions": [
                      {
                        "expression": "string",
                        "name": "string"
                      }
                      ...
                    ]
                  },
                  "inlineCode": {
                    "code": "string",
                    "language": "Python_3"
                  },
                  "input": {

                  },
                  "iterator": {

                  },
                  "knowledgeBase": {
                    "guardrailConfiguration": {
                      "guardrailIdentifier": "string",
                      "guardrailVersion": "string"
                    },
                    "inferenceConfiguration": {
                      "text": {
                        "maxTokens": integer,
                        "stopSequences": ["string", ...],
                        "temperature": float,
                        "topP": float
                      }
                    },
                    "knowledgeBaseId": "string",
                    "modelId": "string",
                    "numberOfResults": integer,
                    "orchestrationConfiguration": {
                      "additionalModelRequestFields": {"string": {...}
                        ...},
                      "inferenceConfig": {
                        "text": {
                          "maxTokens": integer,
                          "stopSequences": ["string", ...],
                          "temperature": float,
                          "topP": float
                        }
                      },
                      "performanceConfig": {
                        "latency": "standard"|"optimized"
                      },
                      "promptTemplate": {
                        "textPromptTemplate": "string"
                      }
                    },
                    "promptTemplate": {
                      "textPromptTemplate": "string"
                    },
                    "rerankingConfiguration": {
                      "bedrockRerankingConfiguration": {
                        "metadataConfiguration": {
                          "selectionMode": "SELECTIVE"|"ALL",
                          "selectiveModeConfiguration": {
                            "fieldsToExclude": [
                              {
                                "fieldName": "string"
                              }
                              ...
                            ],
                            "fieldsToInclude": [
                              {
                                "fieldName": "string"
                              }
                              ...
                            ]
                          }
                        },
                        "modelConfiguration": {
                          "additionalModelRequestFields": {"string": {...}
                            ...},
                          "modelArn": "string"
                        },
                        "numberOfRerankedResults": integer
                      },
                      "type": "BEDROCK_RERANKING_MODEL"
                    }
                  },
                  "lambdaFunction": {
                    "lambdaArn": "string"
                  },
                  "lex": {
                    "botAliasArn": "string",
                    "localeId": "string"
                  },
                  "loop": {
                    "definition": { ... recursive ... }
                  },
                  "loopController": {
                    "continueCondition": {
                      "expression": "string",
                      "name": "string"
                    },
                    "maxIterations": integer
                  },
                  "loopInput": {

                  },
                  "output": {

                  },
                  "prompt": {
                    "guardrailConfiguration": {
                      "guardrailIdentifier": "string",
                      "guardrailVersion": "string"
                    },
                    "sourceConfiguration": {
                      "inline": {
                        "additionalModelRequestFields": {...},
                        "inferenceConfiguration": {
                          "text": {
                            "maxTokens": integer,
                            "stopSequences": ["string", ...],
                            "temperature": float,
                            "topP": float
                          }
                        },
                        "modelId": "string",
                        "templateConfiguration": {
                          "chat": {
                            "inputVariables": [
                              {
                                "name": "string"
                              }
                              ...
                            ],
                            "messages": [
                              {
                                "content": [
                                  {
                                    "cachePoint": {
                                      "type": "default"
                                    },
                                    "text": "string"
                                  }
                                  ...
                                ],
                                "role": "user"|"assistant"
                              }
                              ...
                            ],
                            "system": [
                              {
                                "cachePoint": {
                                  "type": "default"
                                },
                                "text": "string"
                              }
                              ...
                            ],
                            "toolConfiguration": {
                              "toolChoice": {
                                "any": {

                                },
                                "auto": {

                                },
                                "tool": {
                                  "name": "string"
                                }
                              },
                              "tools": [
                                {
                                  "cachePoint": {
                                    "type": "default"
                                  },
                                  "toolSpec": {
                                    "description": "string",
                                    "inputSchema": {
                                      "json": {...}
                                    },
                                    "name": "string"
                                  }
                                }
                                ...
                              ]
                            }
                          },
                          "text": {
                            "cachePoint": {
                              "type": "default"
                            },
                            "inputVariables": [
                              {
                                "name": "string"
                              }
                              ...
                            ],
                            "text": "string"
                          }
                        },
                        "templateType": "TEXT"|"CHAT"
                      },
                      "resource": {
                        "promptArn": "string"
                      }
                    }
                  },
                  "retrieval": {
                    "serviceConfiguration": {
                      "s3": {
                        "bucketName": "string"
                      }
                    }
                  },
                  "storage": {
                    "serviceConfiguration": {
                      "s3": {
                        "bucketName": "string"
                      }
                    }
                  }
                },
                "inputs": [
                  {
                    "category": "LoopCondition"|"ReturnValueToLoopStart"|"ExitLoop",
                    "expression": "string",
                    "name": "string",
                    "type": "String"|"Number"|"Boolean"|"Object"|"Array"
                  }
                  ...
                ],
                "name": "string",
                "outputs": [
                  {
                    "name": "string",
                    "type": "String"|"Number"|"Boolean"|"Object"|"Array"
                  }
                  ...
                ],
                "type": "Input"|"Output"|"KnowledgeBase"|"Condition"|"Lex"|"Prompt"|"LambdaFunction"|"Storage"|"Agent"|"Retrieval"|"Iterator"|"Collector"|"InlineCode"|"Loop"|"LoopInput"|"LoopController"
              }
              ...
            ]
          }
        },
        "loopController": {
          "continueCondition": {
            "expression": "string",
            "name": "string"
          },
          "maxIterations": integer
        },
        "loopInput": {

        },
        "output": {

        },
        "prompt": {
          "guardrailConfiguration": {
            "guardrailIdentifier": "string",
            "guardrailVersion": "string"
          },
          "sourceConfiguration": {
            "inline": {
              "additionalModelRequestFields": {...},
              "inferenceConfiguration": {
                "text": {
                  "maxTokens": integer,
                  "stopSequences": ["string", ...],
                  "temperature": float,
                  "topP": float
                }
              },
              "modelId": "string",
              "templateConfiguration": {
                "chat": {
                  "inputVariables": [
                    {
                      "name": "string"
                    }
                    ...
                  ],
                  "messages": [
                    {
                      "content": [
                        {
                          "cachePoint": {
                            "type": "default"
                          },
                          "text": "string"
                        }
                        ...
                      ],
                      "role": "user"|"assistant"
                    }
                    ...
                  ],
                  "system": [
                    {
                      "cachePoint": {
                        "type": "default"
                      },
                      "text": "string"
                    }
                    ...
                  ],
                  "toolConfiguration": {
                    "toolChoice": {
                      "any": {

                      },
                      "auto": {

                      },
                      "tool": {
                        "name": "string"
                      }
                    },
                    "tools": [
                      {
                        "cachePoint": {
                          "type": "default"
                        },
                        "toolSpec": {
                          "description": "string",
                          "inputSchema": {
                            "json": {...}
                          },
                          "name": "string"
                        }
                      }
                      ...
                    ]
                  }
                },
                "text": {
                  "cachePoint": {
                    "type": "default"
                  },
                  "inputVariables": [
                    {
                      "name": "string"
                    }
                    ...
                  ],
                  "text": "string"
                }
              },
              "templateType": "TEXT"|"CHAT"
            },
            "resource": {
              "promptArn": "string"
            }
          }
        },
        "retrieval": {
          "serviceConfiguration": {
            "s3": {
              "bucketName": "string"
            }
          }
        },
        "storage": {
          "serviceConfiguration": {
            "s3": {
              "bucketName": "string"
            }
          }
        }
      },
      "inputs": [
        {
          "category": "LoopCondition"|"ReturnValueToLoopStart"|"ExitLoop",
          "expression": "string",
          "name": "string",
          "type": "String"|"Number"|"Boolean"|"Object"|"Array"
        }
        ...
      ],
      "name": "string",
      "outputs": [
        {
          "name": "string",
          "type": "String"|"Number"|"Boolean"|"Object"|"Array"
        }
        ...
      ],
      "type": "Input"|"Output"|"KnowledgeBase"|"Condition"|"Lex"|"Prompt"|"LambdaFunction"|"Storage"|"Agent"|"Retrieval"|"Iterator"|"Collector"|"InlineCode"|"Loop"|"LoopInput"|"LoopController"
    }
    ...
  ]
}
```

`--description` (string)

A description for the flow.

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.

`--name` (string)

A name for the flow.

`--tags` (map)

Any tags that you want to attach to the flow. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html) .

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

The Amazon Resource Name (ARN) of the flow.

createdAt -> (timestamp)

The time at which the flow was created.

customerEncryptionKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key that you encrypted the flow with.

definition -> (structure)

A definition of the nodes and connections between nodes in the flow.

connections -> (list)

An array of connection definitions in the flow.

(structure)

Contains information about a connection between two nodes in the flow.

configuration -> (tagged union structure)

The configuration of the connection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conditional`, `data`.

conditional -> (structure)

The configuration of a connection originating from a Condition node.

condition -> (string)

The condition that triggers this connection. For more information about how to write conditions, see the **Condition** node type in the [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html) topic in the Amazon Bedrock User Guide.

data -> (structure)

The configuration of a connection originating from a node that isnât a Condition node.

sourceOutput -> (string)

The name of the output in the source node that the connection begins from.

targetInput -> (string)

The name of the input in the target node that the connection ends at.

name -> (string)

A name for the connection that you can reference.

source -> (string)

The node that the connection starts at.

target -> (string)

The node that the connection ends at.

type -> (string)

Whether the source node that the connection begins from is a condition node (`Conditional` ) or not (`Data` ).

nodes -> (list)

An array of node definitions in the flow.

(structure)

Contains configurations about a node in the flow.

configuration -> (tagged union structure)

Contains configurations for the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agent`, `collector`, `condition`, `inlineCode`, `input`, `iterator`, `knowledgeBase`, `lambdaFunction`, `lex`, `loop`, `loopController`, `loopInput`, `output`, `prompt`, `retrieval`, `storage`.

agent -> (structure)

Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.

agentAliasArn -> (string)

The Amazon Resource Name (ARN) of the alias of the agent to invoke.

collector -> (structure)

Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.

condition -> (structure)

Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.

conditions -> (list)

An array of conditions. Each member contains the name of a condition and an expression that defines the condition.

(structure)

Defines a condition in the condition node.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

inlineCode -> (structure)

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

code -> (string)

The code thatâs executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.

The code must be valid in the programming `language` that you specify.

language -> (string)

The programming language used by your inline code node.

The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3` ) is supported.

input -> (structure)

Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` canât be specified for this node.

iterator -> (structure)

Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.

The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.

knowledgeBase -> (structure)

Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

knowledgeBaseId -> (string)

The unique identifier of the knowledge base to query.

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.

numberOfResults -> (integer)

The number of results to retrieve from the knowledge base.

orchestrationConfiguration -> (structure)

The configuration for orchestrating the retrieval and generation process in the knowledge base node.

additionalModelRequestFields -> (map)

The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.

key -> (string)

value -> (document)

inferenceConfig -> (tagged union structure)

Contains inference configurations for the prompt.

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

performanceConfig -> (structure)

The performance configuration options for the knowledge base retrieval and generation process.

latency -> (string)

The latency optimization setting.

promptTemplate -> (structure)

A custom prompt template for orchestrating the retrieval and generation process.

textPromptTemplate -> (string)

The text of the prompt template.

promptTemplate -> (structure)

A custom prompt template to use with the knowledge base for generating responses.

textPromptTemplate -> (string)

The text of the prompt template.

rerankingConfiguration -> (structure)

The configuration for reranking the retrieved results from the knowledge base to improve relevance.

bedrockRerankingConfiguration -> (structure)

Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.

metadataConfiguration -> (structure)

Specifies how metadata fields should be handled during the reranking process.

selectionMode -> (string)

The mode for selecting metadata fields for reranking.

selectiveModeConfiguration -> (tagged union structure)

The configuration for selective metadata field inclusion or exclusion during reranking.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldsToExclude`, `fieldsToInclude`.

fieldsToExclude -> (list)

Specifies the metadata fields to exclude from the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

fieldsToInclude -> (list)

Specifies the metadata fields to include in the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

modelConfiguration -> (structure)

Specifies the configuration for the Amazon Bedrock reranker model.

additionalModelRequestFields -> (map)

Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.

key -> (string)

value -> (document)

modelArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.

numberOfRerankedResults -> (integer)

Specifies the number of results to return after reranking.

type -> (string)

Specifies the type of reranking model to use. Currently, the only supported value is `BEDROCK_RERANKING_MODEL` .

lambdaFunction -> (structure)

Contains configurations for a Lambda function node in your flow. Invokes an Lambda function.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function to invoke.

lex -> (structure)

Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.

botAliasArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.

localeId -> (string)

The Region to invoke the Amazon Lex bot in.

loop -> (structure)

Contains configurations for a DoWhile loop in your flow.

definition -> (structure)

The definition of the DoWhile loop nodes and connections between nodes in the flow.

connections -> (list)

An array of connection definitions in the flow.

(structure)

Contains information about a connection between two nodes in the flow.

configuration -> (tagged union structure)

The configuration of the connection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conditional`, `data`.

conditional -> (structure)

The configuration of a connection originating from a Condition node.

condition -> (string)

The condition that triggers this connection. For more information about how to write conditions, see the **Condition** node type in the [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html) topic in the Amazon Bedrock User Guide.

data -> (structure)

The configuration of a connection originating from a node that isnât a Condition node.

sourceOutput -> (string)

The name of the output in the source node that the connection begins from.

targetInput -> (string)

The name of the input in the target node that the connection ends at.

name -> (string)

A name for the connection that you can reference.

source -> (string)

The node that the connection starts at.

target -> (string)

The node that the connection ends at.

type -> (string)

Whether the source node that the connection begins from is a condition node (`Conditional` ) or not (`Data` ).

nodes -> (list)

An array of node definitions in the flow.

(structure)

Contains configurations about a node in the flow.

configuration -> (tagged union structure)

Contains configurations for the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `agent`, `collector`, `condition`, `inlineCode`, `input`, `iterator`, `knowledgeBase`, `lambdaFunction`, `lex`, `loop`, `loopController`, `loopInput`, `output`, `prompt`, `retrieval`, `storage`.

agent -> (structure)

Contains configurations for an agent node in your flow. Invokes an alias of an agent and returns the response.

agentAliasArn -> (string)

The Amazon Resource Name (ARN) of the alias of the agent to invoke.

collector -> (structure)

Contains configurations for a collector node in your flow. Collects an iteration of inputs and consolidates them into an array of outputs.

condition -> (structure)

Contains configurations for a condition node in your flow. Defines conditions that lead to different branches of the flow.

conditions -> (list)

An array of conditions. Each member contains the name of a condition and an expression that defines the condition.

(structure)

Defines a condition in the condition node.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

inlineCode -> (structure)

Contains configurations for an inline code node in your flow. Inline code nodes let you write and execute code directly within your flow, enabling data transformations, custom logic, and integrations without needing an external Lambda function.

code -> (string)

The code thatâs executed in your inline code node. The code can access input data from previous nodes in the flow, perform operations on that data, and produce output that can be used by other nodes in your flow.

The code must be valid in the programming `language` that you specify.

language -> (string)

The programming language used by your inline code node.

The code must be valid in the programming `language` that you specify. Currently, only Python 3 (`Python_3` ) is supported.

input -> (structure)

Contains configurations for an input flow node in your flow. The first node in the flow. `inputs` canât be specified for this node.

iterator -> (structure)

Contains configurations for an iterator node in your flow. Takes an input that is an array and iteratively sends each item of the array as an output to the following node. The size of the array is also returned in the output.

The output flow node at the end of the flow iteration will return a response for each member of the array. To return only one response, you can include a collector node downstream from the iterator node.

knowledgeBase -> (structure)

Contains configurations for a knowledge base node in your flow. Queries a knowledge base and returns the retrieved results or generated response.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply during query and response generation for the knowledge base in this configuration.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

knowledgeBaseId -> (string)

The unique identifier of the knowledge base to query.

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to use to generate a response from the query results. Omit this field if you want to return the retrieved results as an array.

numberOfResults -> (integer)

The number of results to retrieve from the knowledge base.

orchestrationConfiguration -> (structure)

The configuration for orchestrating the retrieval and generation process in the knowledge base node.

additionalModelRequestFields -> (map)

The additional model-specific request parameters as key-value pairs to be included in the request to the foundation model.

key -> (string)

value -> (document)

inferenceConfig -> (tagged union structure)

Contains inference configurations for the prompt.

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

performanceConfig -> (structure)

The performance configuration options for the knowledge base retrieval and generation process.

latency -> (string)

The latency optimization setting.

promptTemplate -> (structure)

A custom prompt template for orchestrating the retrieval and generation process.

textPromptTemplate -> (string)

The text of the prompt template.

promptTemplate -> (structure)

A custom prompt template to use with the knowledge base for generating responses.

textPromptTemplate -> (string)

The text of the prompt template.

rerankingConfiguration -> (structure)

The configuration for reranking the retrieved results from the knowledge base to improve relevance.

bedrockRerankingConfiguration -> (structure)

Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.

metadataConfiguration -> (structure)

Specifies how metadata fields should be handled during the reranking process.

selectionMode -> (string)

The mode for selecting metadata fields for reranking.

selectiveModeConfiguration -> (tagged union structure)

The configuration for selective metadata field inclusion or exclusion during reranking.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldsToExclude`, `fieldsToInclude`.

fieldsToExclude -> (list)

Specifies the metadata fields to exclude from the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

fieldsToInclude -> (list)

Specifies the metadata fields to include in the reranking process.

(structure)

Specifies a metadata field to include or exclude during the reranking process.

fieldName -> (string)

The name of the metadata field to include or exclude during reranking.

modelConfiguration -> (structure)

Specifies the configuration for the Amazon Bedrock reranker model.

additionalModelRequestFields -> (map)

Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.

key -> (string)

value -> (document)

modelArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.

numberOfRerankedResults -> (integer)

Specifies the number of results to return after reranking.

type -> (string)

Specifies the type of reranking model to use. Currently, the only supported value is `BEDROCK_RERANKING_MODEL` .

lambdaFunction -> (structure)

Contains configurations for a Lambda function node in your flow. Invokes an Lambda function.

lambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function to invoke.

lex -> (structure)

Contains configurations for a Lex node in your flow. Invokes an Amazon Lex bot to identify the intent of the input and return the intent as the output.

botAliasArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Lex bot alias to invoke.

localeId -> (string)

The Region to invoke the Amazon Lex bot in.

loop -> (structure)

Contains configurations for a DoWhile loop in your flow.

( â¦ recursive â¦ )

loopController -> (structure)

Contains controller node configurations for a DoWhile loop in your flow.

continueCondition -> (structure)

Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

maxIterations -> (integer)

Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.

loopInput -> (structure)

Contains input node configurations for a DoWhile loop in your flow.

output -> (structure)

Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` canât be specified for this node.

prompt -> (structure)

Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

sourceConfiguration -> (tagged union structure)

Specifies whether the prompt is from Prompt management or defined inline.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `inline`, `resource`.

inline -> (structure)

Contains configurations for a prompt that is defined inline

additionalModelRequestFields -> (document)

Additional fields to be included in the model request for the Prompt node.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.

templateConfiguration -> (tagged union structure)

Contains a prompt and variables in the prompt that can be replaced with values at runtime.

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

The type of prompt template.

resource -> (structure)

Contains configurations for a prompt from Prompt management.

promptArn -> (string)

The Amazon Resource Name (ARN) of the prompt from Prompt management.

retrieval -> (structure)

Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for retrieving data to return as the output from the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.

bucketName -> (string)

The name of the Amazon S3 bucket from which to retrieve data.

storage -> (structure)

Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for storing the input into the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location in which to store the input into the node.

bucketName -> (string)

The name of the Amazon S3 bucket in which to store the input into the node.

inputs -> (list)

An array of objects, each of which contains information about an input into the node.

(structure)

Contains configurations for an input in an Amazon Bedrock Flows node.

category -> (string)

Specifies how input data flows between iterations in a DoWhile loop.

- `LoopCondition` - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue.
- `ReturnValueToLoopStart` - Defines data to pass back to the start of the loopâs next iteration. Use this category for variables that you want to update for each loop iteration.
- `ExitLoop` - Defines the value thatâs available once the loop ends. Use this category to expose loop results to nodes outside the loop.

expression -> (string)

An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html) .

name -> (string)

Specifies a name for the input that you can reference.

type -> (string)

Specifies the data type of the input. If the input doesnât match this type at runtime, a validation error will be thrown.

name -> (string)

A name for the node.

outputs -> (list)

A list of objects, each of which contains information about an output from the node.

(structure)

Contains configurations for an output from a node.

name -> (string)

A name for the output that you can reference.

type -> (string)

The data type of the output. If the output doesnât match this type at runtime, a validation error will be thrown.

type -> (string)

The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.

loopController -> (structure)

Contains controller node configurations for a DoWhile loop in your flow.

continueCondition -> (structure)

Specifies the condition that determines when the flow exits the DoWhile loop. The loop executes until this condition evaluates to true.

expression -> (string)

Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in [Node types in prompt flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes) .

name -> (string)

A name for the condition that you can reference.

maxIterations -> (integer)

Specifies the maximum number of times the DoWhile loop can iterate before the flow exits the loop.

loopInput -> (structure)

Contains input node configurations for a DoWhile loop in your flow.

output -> (structure)

Contains configurations for an output flow node in your flow. The last node in the flow. `outputs` canât be specified for this node.

prompt -> (structure)

Contains configurations for a prompt node in your flow. Runs a prompt and generates the model response as the output. You can use a prompt from Prompt management or you can configure one in this node.

guardrailConfiguration -> (structure)

Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.

guardrailIdentifier -> (string)

The unique identifier of the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

sourceConfiguration -> (tagged union structure)

Specifies whether the prompt is from Prompt management or defined inline.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `inline`, `resource`.

inline -> (structure)

Contains configurations for a prompt that is defined inline

additionalModelRequestFields -> (document)

Additional fields to be included in the model request for the Prompt node.

inferenceConfiguration -> (tagged union structure)

Contains inference configurations for the prompt.

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

modelId -> (string)

The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to run inference with.

templateConfiguration -> (tagged union structure)

Contains a prompt and variables in the prompt that can be replaced with values at runtime.

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

The type of prompt template.

resource -> (structure)

Contains configurations for a prompt from Prompt management.

promptArn -> (string)

The Amazon Resource Name (ARN) of the prompt from Prompt management.

retrieval -> (structure)

Contains configurations for a retrieval node in your flow. Retrieves data from an Amazon S3 location and returns it as the output.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for retrieving data to return as the output from the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location from which to retrieve data to return as the output from the node.

bucketName -> (string)

The name of the Amazon S3 bucket from which to retrieve data.

storage -> (structure)

Contains configurations for a storage node in your flow. Stores an input in an Amazon S3 location.

serviceConfiguration -> (tagged union structure)

Contains configurations for the service to use for storing the input into the node.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.

s3 -> (structure)

Contains configurations for the Amazon S3 location in which to store the input into the node.

bucketName -> (string)

The name of the Amazon S3 bucket in which to store the input into the node.

inputs -> (list)

An array of objects, each of which contains information about an input into the node.

(structure)

Contains configurations for an input in an Amazon Bedrock Flows node.

category -> (string)

Specifies how input data flows between iterations in a DoWhile loop.

- `LoopCondition` - Controls whether the loop continues by evaluating condition expressions against the input data. Use this category to define the condition that determines if the loop should continue.
- `ReturnValueToLoopStart` - Defines data to pass back to the start of the loopâs next iteration. Use this category for variables that you want to update for each loop iteration.
- `ExitLoop` - Defines the value thatâs available once the loop ends. Use this category to expose loop results to nodes outside the loop.

expression -> (string)

An expression that formats the input for the node. For an explanation of how to create expressions, see [Expressions in Prompt flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html) .

name -> (string)

Specifies a name for the input that you can reference.

type -> (string)

Specifies the data type of the input. If the input doesnât match this type at runtime, a validation error will be thrown.

name -> (string)

A name for the node.

outputs -> (list)

A list of objects, each of which contains information about an output from the node.

(structure)

Contains configurations for an output from a node.

name -> (string)

A name for the output that you can reference.

type -> (string)

The data type of the output. If the output doesnât match this type at runtime, a validation error will be thrown.

type -> (string)

The type of node. This value must match the name of the key that you provide in the configuration you provide in the `FlowNodeConfiguration` field.

description -> (string)

The description of the flow.

executionRoleArn -> (string)

The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.

id -> (string)

The unique identifier of the flow.

name -> (string)

The name of the flow.

status -> (string)

The status of the flow. When you submit this request, the status will be `NotPrepared` . If creation fails, the status becomes `Failed` .

updatedAt -> (timestamp)

The time at which the flow was last updated.

version -> (string)

The version of the flow. When you create a flow, the version created is the `DRAFT` version.