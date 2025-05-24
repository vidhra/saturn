# list-test-execution-result-itemsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-test-execution-result-items.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-test-execution-result-items.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-test-execution-result-items

## Description

Gets a list of test execution result items.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListTestExecutionResultItems)

## Synopsis

```
list-test-execution-result-items
--test-execution-id <value>
--result-filter-by <value>
[--max-results <value>]
[--next-token <value>]
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

`--test-execution-id` (string)

The unique identifier of the test execution to list the result items.

`--result-filter-by` (structure)

The filter for the list of results from the test set execution.

resultTypeFilter -> (string)

Specifies which results to filter. See [Test result detailsâ>Test results details](https://docs.aws.amazon.com/lexv2/latest/dg/test-results-details-test-set.html) for details about different types of results.

conversationLevelTestResultsFilterBy -> (structure)

Contains information about the method for filtering Conversation level test results.

endToEndResult -> (string)

The selection of matched or mismatched end-to-end status to filter test set results data at the conversation level.

Shorthand Syntax:

```
resultTypeFilter=string,conversationLevelTestResultsFilterBy={endToEndResult=string}
```

JSON Syntax:

```
{
  "resultTypeFilter": "OverallTestResults"|"ConversationLevelTestResults"|"IntentClassificationTestResults"|"SlotResolutionTestResults"|"UtteranceLevelResults",
  "conversationLevelTestResultsFilterBy": {
    "endToEndResult": "Matched"|"Mismatched"|"ExecutionError"
  }
}
```

`--max-results` (integer)

The maximum number of test execution result items to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the `ListTestExecutionResultItems` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response. Use that token in the `nextToken` parameter to return the next page of results.

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

testExecutionResults -> (structure)

The list of results from the test execution.

overallTestResults -> (structure)

Overall results for the test execution, including the breakdown of conversations and single-input utterances.

items -> (list)

A list of the overall test results.

(structure)

Information about the overall results for a test execution result.

multiTurnConversation -> (boolean)

Indicates whether the conversation contains multiple turns or not.

totalResultCount -> (integer)

The total number of overall results in the result of the test execution.

speechTranscriptionResultCounts -> (map)

The number of speech transcription results in the overall test.

key -> (string)

value -> (integer)

endToEndResultCounts -> (map)

The number of results that succeeded.

key -> (string)

value -> (integer)

conversationLevelTestResults -> (structure)

Results related to conversations in the test set, including metrics about success and failure of conversations and intent and slot failures.

items -> (list)

The item list in the test set results data at the conversation level.

(structure)

The test result evaluation item at the conversation level.

conversationId -> (string)

The conversation Id of the test result evaluation item.

endToEndResult -> (string)

The end-to-end success or failure of the test result evaluation item.

speechTranscriptionResult -> (string)

The speech transcription success or failure of the test result evaluation item.

intentClassificationResults -> (list)

The intent classification of the test result evaluation item.

(structure)

The item listing the evaluation of intent level success or failure.

intentName -> (string)

The intent name used in the evaluation of intent level success or failure.

matchResult -> (string)

The number of times the specific intent is used in the evaluation of intent level success or failure.

slotResolutionResults -> (list)

The slot success or failure of the test result evaluation item.

(structure)

The slots used for the slot resolution in the conversation.

intentName -> (string)

The intents used in the slots list for the slot resolution details.

slotName -> (string)

The slot name in the slots list for the slot resolution details.

matchResult -> (string)

The number of matching slots used in the slots listings for the slot resolution evaluation.

intentClassificationTestResults -> (structure)

Intent recognition results aggregated by intent name. The aggregated results contain success and failure rates of intent recognition, speech transcriptions, and end-to-end conversations.

items -> (list)

A list of the results for the intent classification test.

(structure)

Information for an intent that is classified by the test workbench.

intentName -> (string)

The name of the intent.

multiTurnConversation -> (boolean)

Indicates whether the conversation involves multiple turns or not.

resultCounts -> (structure)

The result of the intent classification test.

totalResultCount -> (integer)

The total number of results in the intent classification test.

speechTranscriptionResultCounts -> (map)

The number of matched, mismatched, and execution error results for speech transcription for the intent.

key -> (string)

value -> (integer)

intentMatchResultCounts -> (map)

The number of matched and mismatched results for intent recognition for the intent.

key -> (string)

value -> (integer)

intentLevelSlotResolutionTestResults -> (structure)

Slot resolution results aggregated by intent and slot name. The aggregated results contain success and failure rates of slot resolution, speech transcriptions, and end-to-end conversations

items -> (list)

Indicates the items for the slot level resolution for the intents.

(structure)

Information about intent-level slot resolution in a test result.

intentName -> (string)

The name of the intent that was recognized.

multiTurnConversation -> (boolean)

Indicates whether the conversation involves multiple turns or not.

slotResolutionResults -> (list)

The results for the slot resolution in the test execution result.

(structure)

Information about the success and failure rate of slot resolution in the results of a test execution.

slotName -> (string)

The name of the slot.

resultCounts -> (structure)

A result for slot resolution in the results of a test execution.

totalResultCount -> (integer)

The total number of results.

speechTranscriptionResultCounts -> (map)

The number of matched, mismatched and execution error results for speech transcription for the slot.

key -> (string)

value -> (integer)

slotMatchResultCounts -> (map)

The number of matched and mismatched results for slot resolution for the slot.

key -> (string)

value -> (integer)

utteranceLevelTestResults -> (structure)

Results related to utterances in the test set.

items -> (list)

Contains information about an utterance in the results of the test set execution.

(structure)

Contains information about multiple utterances in the results of a test set execution.

recordNumber -> (long)

The record number of the result.

conversationId -> (string)

The unique identifier for the conversation associated with the result.

turnResult -> (structure)

Contains information about the turn associated with the result.

agent -> (structure)

Contains information about the agent messages in the turn.

expectedAgentPrompt -> (string)

The expected agent prompt for the agent turn in a test set execution.

actualAgentPrompt -> (string)

The actual agent prompt for the agent turn in a test set execution.

errorDetails -> (structure)

Details about an error in an execution of a test set.

errorCode -> (string)

The error code for the error.

errorMessage -> (string)

The message describing the error.

actualElicitedSlot -> (string)

The actual elicited slot for the agent turn in a test set execution.

actualIntent -> (string)

The actual intent for the agent turn in a test set execution.

user -> (structure)

Contains information about the user messages in the turn.

input -> (structure)

Contains information about the user messages in the turn in the input.

utteranceInput -> (structure)

The utterance input in the user turn.

textInput -> (string)

A text input transcription of the utterance. It is only applicable for test-sets containing text data.

audioInput -> (structure)

Contains information about the audio input for an utterance.

audioFileS3Location -> (string)

Amazon S3 file pointing to the audio.

requestAttributes -> (map)

Request attributes of the user turn.

key -> (string)

value -> (string)

sessionState -> (structure)

Contains information about the session state in the input.

sessionAttributes -> (map)

Session attributes for the session state.

key -> (string)

value -> (string)

activeContexts -> (list)

Active contexts for the session state.

(structure)

The active context used in the test execution.

name -> (string)

The name of active context.

runtimeHints -> (structure)

Runtime hints for the session state.

slotHints -> (map)

A list of the slots in the intent that should have runtime hints added, and the phrases that should be added for each slot.

The first level of the `slotHints` map is the name of the intent. The second level is the name of the slot within the intent. For more information, see [Using hints to improve accuracy](https://docs.aws.amazon.com/lexv2/latest/dg/using-hints.html) .

The intent name and slot name must exist.

key -> (string)

value -> (map)

key -> (string)

value -> (structure)

Provides an array of phrases that should be given preference when resolving values for a slot.

runtimeHintValues -> (list)

One or more strings that Amazon Lex should look for in the input to the bot. Each phrase is given preference when deciding on slot values.

(structure)

Provides the phrase that Amazon Lex should look for in the userâs input to the bot.

phrase -> (string)

The phrase that Amazon Lex should look for in the userâs input to the bot.

subSlotHints -> (map)

A map of constituent sub slot names inside a composite slot in the intent and the phrases that should be added for each sub slot. Inside each composite slot hints, this structure provides a mechanism to add granular sub slot phrases. Only sub slot hints are supported for composite slots. The intent name, composite slot name and the constituent sub slot names must exist.

key -> (string)

value -> (structure)

Provides an array of phrases that should be given preference when resolving values for a slot.

runtimeHintValues -> (list)

One or more strings that Amazon Lex should look for in the input to the bot. Each phrase is given preference when deciding on slot values.

(structure)

Provides the phrase that Amazon Lex should look for in the userâs input to the bot.

phrase -> (string)

The phrase that Amazon Lex should look for in the userâs input to the bot.

expectedOutput -> (structure)

Contains information about the expected output for the user turn.

intent -> (structure)

Contains information about the intent.

name -> (string)

The name of the intent.

slots -> (map)

The slots associated with the intent.

key -> (string)

value -> (structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

(structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

( â¦ recursive â¦ )

subSlots -> (map)

A list of items mapping the name of the subslots to information about those subslots.

key -> (string)

( â¦ recursive â¦ )

subSlots -> (map)

A list of items mapping the name of the subslots to information about those subslots.

key -> (string)

value -> (structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

( â¦ recursive â¦ )

activeContexts -> (list)

The contexts that are active in the turn.

(structure)

The active context used in the test execution.

name -> (string)

The name of active context.

transcript -> (string)

The transcript that is output for the user turn by the test execution.

actualOutput -> (structure)

Contains information about the actual output for the user turn.

intent -> (structure)

Contains information about the intent.

name -> (string)

The name of the intent.

slots -> (map)

The slots associated with the intent.

key -> (string)

value -> (structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

(structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

( â¦ recursive â¦ )

subSlots -> (map)

A list of items mapping the name of the subslots to information about those subslots.

key -> (string)

( â¦ recursive â¦ )

subSlots -> (map)

A list of items mapping the name of the subslots to information about those subslots.

key -> (string)

value -> (structure)

Contains information about a slot output by the test set execution.

value -> (string)

The value output by the slot recognition.

values -> (list)

Values that are output by the slot recognition.

( â¦ recursive â¦ )

activeContexts -> (list)

The contexts that are active in the turn.

(structure)

The active context used in the test execution.

name -> (string)

The name of active context.

transcript -> (string)

The transcript that is output for the user turn by the test execution.

errorDetails -> (structure)

Details about an error in an execution of a test set.

errorCode -> (string)

The error code for the error.

errorMessage -> (string)

The message describing the error.

endToEndResult -> (string)

Specifies whether the expected and actual outputs match or not, or if there is an error in execution.

intentMatchResult -> (string)

Specifies whether the expected and actual intents match or not.

slotMatchResult -> (string)

Specifies whether the expected and actual slots match or not.

speechTranscriptionResult -> (string)

Specifies whether the expected and actual speech transcriptions match or not, or if there is an error in execution.

conversationLevelResult -> (structure)

Contains information about the results related to the conversation associated with the user turn.

endToEndResult -> (string)

The success or failure of the streaming of the conversation.

speechTranscriptionResult -> (string)

The speech transcription success or failure details of the conversation.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the `ListTestExecutionResultItems` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListTestExecutionResultItems` operation request to get the next page of results.