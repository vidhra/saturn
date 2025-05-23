# create-intent-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-intent-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/create-intent-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# create-intent-version

## Description

Creates a new version of an intent based on the `$LATEST` version of the intent. If the `$LATEST` version of this intent hasnât changed since you last updated it, Amazon Lex doesnât create a new version. It returns the last version you created.

### Note

You can update only the `$LATEST` version of the intent. You canât update the numbered versions that you create with the `CreateIntentVersion` operation.

When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro .

This operation requires permissions to perform the `lex:CreateIntentVersion` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateIntentVersion)

## Synopsis

```
create-intent-version
--name <value>
[--checksum <value>]
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

`--name` (string)

The name of the intent that you want to create a new version of. The name is case sensitive.

`--checksum` (string)

Checksum of the `$LATEST` version of the intent that should be used to create the new version. If you specify a checksum and the `$LATEST` version of the intent has a different checksum, Amazon Lex returns a `PreconditionFailedException` exception and doesnât publish a new version. If you donât specify a checksum, Amazon Lex publishes the `$LATEST` version.

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

The name of the intent.

description -> (string)

A description of the intent.

slots -> (list)

An array of slot types that defines the information required to fulfill the intent.

(structure)

Identifies the version of a specific slot.

name -> (string)

The name of the slot.

description -> (string)

A description of the slot.

slotConstraint -> (string)

Specifies whether the slot is required or optional.

slotType -> (string)

The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

slotTypeVersion -> (string)

The version of the slot type.

valueElicitationPrompt -> (structure)

The prompt that Amazon Lex uses to elicit the slot value from the user.

messages -> (list)

An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

maxAttempts -> (integer)

The number of times to prompt the user for information.

responseCard -> (string)

A response card. Amazon Lex uses this prompt at runtime, in the `PostText` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .

priority -> (integer)

Directs Amazon Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Amazon Lex first elicits a value for the slot with priority 1.

If multiple slots share the same priority, the order in which Amazon Lex elicits values is arbitrary.

sampleUtterances -> (list)

If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

(string)

responseCard -> (string)

A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply.

obfuscationSetting -> (string)

Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is âfull_nameâ, obfuscated values are replaced with â{full_name}â. For more information, see [Slot Obfuscation](https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html) .

defaultValueSpec -> (structure)

A list of default values for the slot. Default values are used when Amazon Lex hasnât determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.

defaultValueList -> (list)

The default values for a slot. You can specify more than one default. For example, you can specify a default value to use from a matching context variable, a session attribute, or a fixed value.

The default value chosen is selected based on the order that you specify them in the list. For example, if you specify a context variable and a fixed value in that order, Amazon Lex uses the context variable if it is available, else it uses the fixed value.

(structure)

A default value for a slot.

defaultValue -> (string)

The default value for the slot. You can specify one of the following:

- `#context-name.slot-name` - The slot value âslot-nameâ in the context âcontext-name.â
- `{attribute}` - The slot value of the session attribute âattribute.â
- `'value'` - The discrete value âvalue.â

sampleUtterances -> (list)

An array of sample utterances configured for the intent.

(string)

confirmationPrompt -> (structure)

If defined, the prompt that Amazon Lex uses to confirm the userâs intent before fulfilling it.

messages -> (list)

An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

maxAttempts -> (integer)

The number of times to prompt the user for information.

responseCard -> (string)

A response card. Amazon Lex uses this prompt at runtime, in the `PostText` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .

rejectionStatement -> (structure)

If the user answers ânoâ to the question defined in `confirmationPrompt` , Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages -> (list)

A collection of message objects.

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

responseCard -> (string)

At runtime, if the client is using the [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.

followUpPrompt -> (structure)

If defined, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.

prompt -> (structure)

Prompts for information from the user.

messages -> (list)

An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

maxAttempts -> (integer)

The number of times to prompt the user for information.

responseCard -> (string)

A response card. Amazon Lex uses this prompt at runtime, in the `PostText` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card .

rejectionStatement -> (structure)

If the user answers ânoâ to the question defined in the `prompt` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled.

messages -> (list)

A collection of message objects.

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

responseCard -> (string)

At runtime, if the client is using the [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.

conclusionStatement -> (structure)

After the Lambda function specified in the `fulfillmentActivity` field fulfills the intent, Amazon Lex conveys this statement to the user.

messages -> (list)

A collection of message objects.

(structure)

The message object that provides the message text and its type.

contentType -> (string)

The content type of the message string.

content -> (string)

The text of the message.

groupNumber -> (integer)

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

responseCard -> (string)

At runtime, if the client is using the [PostText](http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html) API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.

dialogCodeHook -> (structure)

If defined, Amazon Lex invokes this Lambda function for each user input.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

fulfillmentActivity -> (structure)

Describes how the intent is fulfilled.

type -> (string)

How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

codeHook -> (structure)

A description of the Lambda function that is run to fulfill the intent.

uri -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

messageVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

parentIntentSignature -> (string)

A unique identifier for a built-in intent.

lastUpdatedDate -> (timestamp)

The date that the intent was updated.

createdDate -> (timestamp)

The date that the intent was created.

version -> (string)

The version number assigned to the new version of the intent.

checksum -> (string)

Checksum of the intent version created.

kendraConfiguration -> (structure)

Configuration information, if any, for connecting an Amazon Kendra index with the `AMAZON.KendraSearchIntent` intent.

kendraIndex -> (string)

The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the AMAZON.KendraSearchIntent intent to search. The index must be in the same account and Region as the Amazon Lex bot. If the Amazon Kendra index does not exist, you get an exception when you call the `PutIntent` operation.

queryFilterString -> (string)

A query filter that Amazon Lex sends to Amazon Kendra to filter the response from the query. The filter is in the format defined by Amazon Kendra. For more information, see [Filtering queries](http://docs.aws.amazon.com/kendra/latest/dg/filtering.html) .

You can override this filter string with a new filter string at runtime.

role -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permission to search the Amazon Kendra index. The role must be in the same account and Region as the Amazon Lex bot. If the role does not exist, you get an exception when you call the `PutIntent` operation.

inputContexts -> (list)

An array of `InputContext` objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.

(structure)

The name of a context that must be active for an intent to be selected by Amazon Lex.

name -> (string)

The name of the context.

outputContexts -> (list)

An array of `OutputContext` objects that lists the contexts that the intent activates when the intent is fulfilled.

(structure)

The specification of an output context that is set when an intent is fulfilled.

name -> (string)

The name of the context.

timeToLiveInSeconds -> (integer)

The number of seconds that the context should be active after it is first sent in a `PostContent` or `PostText` response. You can set the value between 5 and 86,400 seconds (24 hours).

turnsToLive -> (integer)

The number of conversation turns that the context should be active. A conversation turn is one `PostContent` or `PostText` request and the corresponding response from Amazon Lex.