# converseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/converse.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/converse.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-runtime/index.html#cli-aws-bedrock-runtime) ]

# converse

## Description

Sends messages to the specified Amazon Bedrock model. `Converse` provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.

Amazon Bedrock doesnât store any text, images, or documents that you provide as content. The data is only used to generate the response.

You can submit a prompt by including it in the `messages` field, specifying the `modelId` of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.

You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the `promptVariables` field. You can append more messages to the prompt by using the `messages` field. If you use a prompt from Prompt management, you canât include the following fields in the request: `additionalModelRequestFields` , `inferenceConfig` , `system` , or `toolConfig` . Instead, these fields must be defined through Prompt management. For more information, see [Use a prompt from Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html) .

For information about the Converse API, see *Use the Converse API* in the *Amazon Bedrock User Guide* . To use a guardrail, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide* . To use a tool with a model, see *Tool use (Function calling)* in the *Amazon Bedrock User Guide*

For example code, see *Converse API examples* in the *Amazon Bedrock User Guide* .

This operation requires permission for the `bedrock:InvokeModel` action.

### Warning

To deny all inference access to resources that you specify in the modelId field, you need to deny access to the `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` actions. Doing this also denies access to the resource through the base inference actions ([InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) and [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) ). For more information see [Deny access for inference on specific models](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference) .

For troubleshooting some of the common errors you might encounter when using the `Converse` API, see [Troubleshooting Amazon Bedrock API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html) in the Amazon Bedrock User Guide

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-runtime-2023-09-30/Converse)

`converse` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
converse
--model-id <value>
[--messages <value>]
[--system <value>]
[--inference-config <value>]
[--tool-config <value>]
[--guardrail-config <value>]
[--additional-model-request-fields <value>]
[--prompt-variables <value>]
[--additional-model-response-field-paths <value>]
[--request-metadata <value>]
[--performance-config <value>]
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

`--model-id` (string)

Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:

- If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see [Amazon Bedrock base model IDs (on-demand throughput)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns) in the Amazon Bedrock User Guide.
- If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see [Supported Regions and models for cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html) in the Amazon Bedrock User Guide.
- If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see [Run inference using a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html) in the Amazon Bedrock User Guide.
- If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see [Use a custom model in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html) in the Amazon Bedrock User Guide.
- To include a prompt that was defined in [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) , specify the ARN of the prompt version to use.

The Converse API doesnât support [imported models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) .

`--messages` (list)

The messages that you want to send to the model.

(structure)

A message input, or returned from, a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) .

role -> (string)

The role that the message plays in the message.

content -> (list)

The message content. Note the following restrictions:

- You can include up to 20 images. Each imageâs size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.
- You can include up to five documents. Each documentâs size must be no more than 4.5 MB.
- If you include a `ContentBlock` with a `document` field in the array, you must also include a `ContentBlock` with a `text` field.
- You can only include images and documents if the `role` is `user` .

(tagged union structure)

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`, `document`, `video`, `toolUse`, `toolResult`, `guardContent`, `cachePoint`, `reasoningContent`.

text -> (string)

Text to include in the message.

image -> (structure)

Image to include in the message.

### Note

This field is only supported by Anthropic Claude 3 models.

format -> (string)

The format of the image.

source -> (tagged union structure)

The source for the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw image bytes for the image. If you use an AWS SDK, you donât need to encode the image bytes in base64.

s3Location -> (structure)

The location of an image object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

document -> (structure)

A document to include in the message.

format -> (string)

The format of a document, or its extension.

name -> (string)

A name for the document. The name can only contain the following characters:

- Alphanumeric characters
- Whitespace characters (no more than one in a row)
- Hyphens
- Parentheses
- Square brackets

### Note

This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.

source -> (tagged union structure)

Contains the content of the document.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw bytes for the document. If you use an Amazon Web Services SDK, you donât need to encode the bytes in base64.

s3Location -> (structure)

The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

video -> (structure)

Video to include in the message.

format -> (string)

The blockâs format.

source -> (tagged union structure)

The blockâs source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

Video content encoded in base64.

s3Location -> (structure)

The location of a video object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

toolUse -> (structure)

Information about a tool use request from a model.

toolUseId -> (string)

The ID for the tool request.

name -> (string)

The name of the tool that the model wants to use.

input -> (document)

The input to pass to the tool.

toolResult -> (structure)

The result for a tool request that a model makes.

toolUseId -> (string)

The ID of the tool request that this is the result for.

content -> (list)

The content for tool result content block.

(tagged union structure)

The tool result content block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `json`, `text`, `image`, `document`, `video`.

json -> (document)

A tool result that is JSON format data.

text -> (string)

A tool result that is text.

image -> (structure)

A tool result that is an image.

### Note

This field is only supported by Anthropic Claude 3 models.

format -> (string)

The format of the image.

source -> (tagged union structure)

The source for the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw image bytes for the image. If you use an AWS SDK, you donât need to encode the image bytes in base64.

s3Location -> (structure)

The location of an image object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

document -> (structure)

A tool result that is a document.

format -> (string)

The format of a document, or its extension.

name -> (string)

A name for the document. The name can only contain the following characters:

- Alphanumeric characters
- Whitespace characters (no more than one in a row)
- Hyphens
- Parentheses
- Square brackets

### Note

This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.

source -> (tagged union structure)

Contains the content of the document.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw bytes for the document. If you use an Amazon Web Services SDK, you donât need to encode the bytes in base64.

s3Location -> (structure)

The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

video -> (structure)

A tool result that is video.

format -> (string)

The blockâs format.

source -> (tagged union structure)

The blockâs source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

Video content encoded in base64.

s3Location -> (structure)

The location of a video object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

status -> (string)

The status for the tool result content block.

### Note

This field is only supported Anthropic Claude 3 models.

guardContent -> (tagged union structure)

Contains the content to assess with the guardrail. If you donât specify `guardContent` in a call to the Converse API, the guardrail (if passed in the Converse API) assesses the entire message.

For more information, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide* . `</p>`

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`.

text -> (structure)

The text to guard.

text -> (string)

The text that you want to guard.

qualifiers -> (list)

The qualifier details for the guardrails contextual grounding filter.

(string)

image -> (structure)

Image within converse content block to be evaluated by the guardrail.

format -> (string)

The format details for the image type of the guardrail converse image block.

source -> (tagged union structure)

The image source (image bytes) of the guardrail converse image block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`.

bytes -> (blob)

The raw image bytes for the image.

cachePoint -> (structure)

CachePoint to include in the message.

type -> (string)

Specifies the type of cache point within the CachePointBlock.

reasoningContent -> (tagged union structure)

Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `reasoningText`, `redactedContent`.

reasoningText -> (structure)

The reasoning that the model used to return the output.

text -> (string)

The reasoning that the model used to return the output.

signature -> (string)

A token that verifies that the reasoning text was generated by the model. If you pass a reasoning block back to the API in a multi-turn conversation, include the text and its signature unmodified.

redactedContent -> (blob)

The content in the reasoning that was encrypted by the model provider for safety reasons. The encryption doesnât affect the quality of responses.

JSON Syntax:

```
[
  {
    "role": "user"|"assistant",
    "content": [
      {
        "text": "string",
        "image": {
          "format": "png"|"jpeg"|"gif"|"webp",
          "source": {
            "bytes": blob,
            "s3Location": {
              "uri": "string",
              "bucketOwner": "string"
            }
          }
        },
        "document": {
          "format": "pdf"|"csv"|"doc"|"docx"|"xls"|"xlsx"|"html"|"txt"|"md",
          "name": "string",
          "source": {
            "bytes": blob,
            "s3Location": {
              "uri": "string",
              "bucketOwner": "string"
            }
          }
        },
        "video": {
          "format": "mkv"|"mov"|"mp4"|"webm"|"flv"|"mpeg"|"mpg"|"wmv"|"three_gp",
          "source": {
            "bytes": blob,
            "s3Location": {
              "uri": "string",
              "bucketOwner": "string"
            }
          }
        },
        "toolUse": {
          "toolUseId": "string",
          "name": "string",
          "input": {...}
        },
        "toolResult": {
          "toolUseId": "string",
          "content": [
            {
              "json": {...},
              "text": "string",
              "image": {
                "format": "png"|"jpeg"|"gif"|"webp",
                "source": {
                  "bytes": blob,
                  "s3Location": {
                    "uri": "string",
                    "bucketOwner": "string"
                  }
                }
              },
              "document": {
                "format": "pdf"|"csv"|"doc"|"docx"|"xls"|"xlsx"|"html"|"txt"|"md",
                "name": "string",
                "source": {
                  "bytes": blob,
                  "s3Location": {
                    "uri": "string",
                    "bucketOwner": "string"
                  }
                }
              },
              "video": {
                "format": "mkv"|"mov"|"mp4"|"webm"|"flv"|"mpeg"|"mpg"|"wmv"|"three_gp",
                "source": {
                  "bytes": blob,
                  "s3Location": {
                    "uri": "string",
                    "bucketOwner": "string"
                  }
                }
              }
            }
            ...
          ],
          "status": "success"|"error"
        },
        "guardContent": {
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
        },
        "cachePoint": {
          "type": "default"
        },
        "reasoningContent": {
          "reasoningText": {
            "text": "string",
            "signature": "string"
          },
          "redactedContent": blob
        }
      }
      ...
    ]
  }
  ...
]
```

`--system` (list)

A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.

(tagged union structure)

A system content block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `guardContent`, `cachePoint`.

text -> (string)

A system prompt for the model.

guardContent -> (tagged union structure)

A content block to assess with the guardrail. Use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

For more information, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide* .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`.

text -> (structure)

The text to guard.

text -> (string)

The text that you want to guard.

qualifiers -> (list)

The qualifier details for the guardrails contextual grounding filter.

(string)

image -> (structure)

Image within converse content block to be evaluated by the guardrail.

format -> (string)

The format details for the image type of the guardrail converse image block.

source -> (tagged union structure)

The image source (image bytes) of the guardrail converse image block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`.

bytes -> (blob)

The raw image bytes for the image.

cachePoint -> (structure)

CachePoint to include in the system prompt.

type -> (string)

Specifies the type of cache point within the CachePointBlock.

JSON Syntax:

```
[
  {
    "text": "string",
    "guardContent": {
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
    },
    "cachePoint": {
      "type": "default"
    }
  }
  ...
]
```

`--inference-config` (structure)

Inference parameters to pass to the model. `Converse` and `ConverseStream` support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the `additionalModelRequestFields` request field.

maxTokens -> (integer)

The maximum number of tokens to allow in the generated response. The default value is the maximum allowed value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

temperature -> (float)

The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.

The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

topP -> (float)

The percentage of most-likely candidates that the model considers for the next token. For example, if you choose a value of 0.8 for `topP` , the model selects from the top 80% of the probability distribution of tokens that could be next in the sequence.

The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

stopSequences -> (list)

A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.

(string)

Shorthand Syntax:

```
maxTokens=integer,temperature=float,topP=float,stopSequences=string,string
```

JSON Syntax:

```
{
  "maxTokens": integer,
  "temperature": float,
  "topP": float,
  "stopSequences": ["string", ...]
}
```

`--tool-config` (structure)

Configuration information for the tools that the model can use when generating a response.

For information about models that support tool use, see [Supported models and model features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features) .

tools -> (list)

An array of tools that you want to pass to a model.

(tagged union structure)

Information about a tool that you can use with the Converse API. For more information, see [Tool use (function calling)](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `toolSpec`, `cachePoint`.

toolSpec -> (structure)

The specfication for the tool.

name -> (string)

The name for the tool.

description -> (string)

The description for the tool.

inputSchema -> (tagged union structure)

The input schema for the tool in JSON format.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `json`.

json -> (document)

The JSON schema for the tool. For more information, see [JSON Schema Reference](https://json-schema.org/understanding-json-schema/reference) .

cachePoint -> (structure)

CachePoint to include in the tool configuration.

type -> (string)

Specifies the type of cache point within the CachePointBlock.

toolChoice -> (tagged union structure)

If supported by model, forces the model to request a tool.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `auto`, `any`, `tool`.

auto -> (structure)

(Default). The Model automatically decides if a tool should be called or whether to generate text instead.

any -> (structure)

The model must request at least one tool (no text is generated).

tool -> (structure)

The Model must request the specified tool. Only supported by Anthropic Claude 3 models.

name -> (string)

The name of the tool that the model must request.

JSON Syntax:

```
{
  "tools": [
    {
      "toolSpec": {
        "name": "string",
        "description": "string",
        "inputSchema": {
          "json": {...}
        }
      },
      "cachePoint": {
        "type": "default"
      }
    }
    ...
  ],
  "toolChoice": {
    "auto": {

    },
    "any": {

    },
    "tool": {
      "name": "string"
    }
  }
}
```

`--guardrail-config` (structure)

Configuration information for a guardrail that you want to use in the request. If you include `guardContent` blocks in the `content` field in the `messages` field, the guardrail operates only on those messages. If you include no `guardContent` blocks, the guardrail operates on all messages in the request body and in any included prompt resource.

guardrailIdentifier -> (string)

The identifier for the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

trace -> (string)

The trace behavior for the guardrail.

Shorthand Syntax:

```
guardrailIdentifier=string,guardrailVersion=string,trace=string
```

JSON Syntax:

```
{
  "guardrailIdentifier": "string",
  "guardrailVersion": "string",
  "trace": "enabled"|"disabled"|"enabled_full"
}
```

`--additional-model-request-fields` (document)

Additional inference parameters that the model supports, beyond the base set of inference parameters that `Converse` and `ConverseStream` support in the `inferenceConfig` field. For more information, see [Model parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html) .

JSON Syntax:

```
{...}
```

`--prompt-variables` (map)

Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you donât specify a prompt resource in the `modelId` field.

key -> (string)

value -> (tagged union structure)

Contains a map of variables in a prompt from Prompt management to an object containing the values to fill in for them when running model invocation. For more information, see [How Prompt management works](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-how.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.

text -> (string)

The text value that the variable maps to.

Shorthand Syntax:

```
KeyName1=text=string,KeyName2=text=string
```

JSON Syntax:

```
{"string": {
      "text": "string"
    }
  ...}
```

`--additional-model-response-field-paths` (list)

Additional model parameters field paths to return in the response. `Converse` and `ConverseStream` return the requested fields as a JSON Pointer object in the `additionalModelResponseFields` field. The following is example JSON for `additionalModelResponseFieldPaths` .

`[ "/stop_sequence" ]`

For information about the JSON Pointer syntax, see the [Internet Engineering Task Force (IETF)](https://datatracker.ietf.org/doc/html/rfc6901) documentation.

`Converse` and `ConverseStream` reject an empty JSON Pointer or incorrectly structured JSON Pointer with a `400` error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by `Converse` .

(string)

Syntax:

```
"string" "string" ...
```

`--request-metadata` (map)

Key-value pairs that you can use to filter invocation logs.

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

`--performance-config` (structure)

Model performance settings for the request.

latency -> (string)

To use a latency-optimized version of the model, set to `optimized` .

Shorthand Syntax:

```
latency=string
```

JSON Syntax:

```
{
  "latency": "standard"|"optimized"
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

output -> (tagged union structure)

The result from the call to `Converse` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `message`.

message -> (structure)

The message that the model generates.

role -> (string)

The role that the message plays in the message.

content -> (list)

The message content. Note the following restrictions:

- You can include up to 20 images. Each imageâs size, height, and width must be no more than 3.75 MB, 8000 px, and 8000 px, respectively.
- You can include up to five documents. Each documentâs size must be no more than 4.5 MB.
- If you include a `ContentBlock` with a `document` field in the array, you must also include a `ContentBlock` with a `text` field.
- You can only include images and documents if the `role` is `user` .

(tagged union structure)

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`, `document`, `video`, `toolUse`, `toolResult`, `guardContent`, `cachePoint`, `reasoningContent`.

text -> (string)

Text to include in the message.

image -> (structure)

Image to include in the message.

### Note

This field is only supported by Anthropic Claude 3 models.

format -> (string)

The format of the image.

source -> (tagged union structure)

The source for the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw image bytes for the image. If you use an AWS SDK, you donât need to encode the image bytes in base64.

s3Location -> (structure)

The location of an image object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

document -> (structure)

A document to include in the message.

format -> (string)

The format of a document, or its extension.

name -> (string)

A name for the document. The name can only contain the following characters:

- Alphanumeric characters
- Whitespace characters (no more than one in a row)
- Hyphens
- Parentheses
- Square brackets

### Note

This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.

source -> (tagged union structure)

Contains the content of the document.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw bytes for the document. If you use an Amazon Web Services SDK, you donât need to encode the bytes in base64.

s3Location -> (structure)

The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

video -> (structure)

Video to include in the message.

format -> (string)

The blockâs format.

source -> (tagged union structure)

The blockâs source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

Video content encoded in base64.

s3Location -> (structure)

The location of a video object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

toolUse -> (structure)

Information about a tool use request from a model.

toolUseId -> (string)

The ID for the tool request.

name -> (string)

The name of the tool that the model wants to use.

input -> (document)

The input to pass to the tool.

toolResult -> (structure)

The result for a tool request that a model makes.

toolUseId -> (string)

The ID of the tool request that this is the result for.

content -> (list)

The content for tool result content block.

(tagged union structure)

The tool result content block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `json`, `text`, `image`, `document`, `video`.

json -> (document)

A tool result that is JSON format data.

text -> (string)

A tool result that is text.

image -> (structure)

A tool result that is an image.

### Note

This field is only supported by Anthropic Claude 3 models.

format -> (string)

The format of the image.

source -> (tagged union structure)

The source for the image.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw image bytes for the image. If you use an AWS SDK, you donât need to encode the image bytes in base64.

s3Location -> (structure)

The location of an image object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

document -> (structure)

A tool result that is a document.

format -> (string)

The format of a document, or its extension.

name -> (string)

A name for the document. The name can only contain the following characters:

- Alphanumeric characters
- Whitespace characters (no more than one in a row)
- Hyphens
- Parentheses
- Square brackets

### Note

This field is vulnerable to prompt injections, because the model might inadvertently interpret it as instructions. Therefore, we recommend that you specify a neutral name.

source -> (tagged union structure)

Contains the content of the document.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

The raw bytes for the document. If you use an Amazon Web Services SDK, you donât need to encode the bytes in base64.

s3Location -> (structure)

The location of a document object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

video -> (structure)

A tool result that is video.

format -> (string)

The blockâs format.

source -> (tagged union structure)

The blockâs source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`, `s3Location`.

bytes -> (blob)

Video content encoded in base64.

s3Location -> (structure)

The location of a video object in an Amazon S3 bucket. To see which models support S3 uploads, see [Supported models and features for Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html) .

uri -> (string)

An object URI starting with `s3://` .

bucketOwner -> (string)

If the bucket belongs to another AWS account, specify that accountâs ID.

status -> (string)

The status for the tool result content block.

### Note

This field is only supported Anthropic Claude 3 models.

guardContent -> (tagged union structure)

Contains the content to assess with the guardrail. If you donât specify `guardContent` in a call to the Converse API, the guardrail (if passed in the Converse API) assesses the entire message.

For more information, see *Use a guardrail with the Converse API* in the *Amazon Bedrock User Guide* . `</p>`

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `image`.

text -> (structure)

The text to guard.

text -> (string)

The text that you want to guard.

qualifiers -> (list)

The qualifier details for the guardrails contextual grounding filter.

(string)

image -> (structure)

Image within converse content block to be evaluated by the guardrail.

format -> (string)

The format details for the image type of the guardrail converse image block.

source -> (tagged union structure)

The image source (image bytes) of the guardrail converse image block.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bytes`.

bytes -> (blob)

The raw image bytes for the image.

cachePoint -> (structure)

CachePoint to include in the message.

type -> (string)

Specifies the type of cache point within the CachePointBlock.

reasoningContent -> (tagged union structure)

Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `reasoningText`, `redactedContent`.

reasoningText -> (structure)

The reasoning that the model used to return the output.

text -> (string)

The reasoning that the model used to return the output.

signature -> (string)

A token that verifies that the reasoning text was generated by the model. If you pass a reasoning block back to the API in a multi-turn conversation, include the text and its signature unmodified.

redactedContent -> (blob)

The content in the reasoning that was encrypted by the model provider for safety reasons. The encryption doesnât affect the quality of responses.

stopReason -> (string)

The reason why the model stopped generating output.

usage -> (structure)

The total number of tokens used in the call to `Converse` . The total includes the tokens input to the model and the tokens generated by the model.

inputTokens -> (integer)

The number of tokens sent in the request to the model.

outputTokens -> (integer)

The number of tokens that the model generated for the request.

totalTokens -> (integer)

The total of input tokens and tokens generated by the model.

cacheReadInputTokens -> (integer)

The number of input tokens read from the cache for the request.

cacheWriteInputTokens -> (integer)

The number of input tokens written to the cache for the request.

metrics -> (structure)

Metrics for the call to `Converse` .

latencyMs -> (long)

The latency of the call to `Converse` , in milliseconds.

additionalModelResponseFields -> (document)

Additional fields in the response that are unique to the model.

trace -> (structure)

A trace object that contains information about the Guardrail behavior.

guardrail -> (structure)

The guardrail trace object.

modelOutput -> (list)

The output from the model.

(string)

inputAssessment -> (map)

The input assessment.

key -> (string)

value -> (structure)

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

outputAssessments -> (map)

the output assessments.

key -> (string)

value -> (list)

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

actionReason -> (string)

Provides the reason for the action taken when harmful content is detected.

promptRouter -> (structure)

The requestâs prompt router.

invokedModelId -> (string)

The ID of the invoked model.

performanceConfig -> (structure)

Model performance settings for the request.

latency -> (string)

To use a latency-optimized version of the model, set to `optimized` .