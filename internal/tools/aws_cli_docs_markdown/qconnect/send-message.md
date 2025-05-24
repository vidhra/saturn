# send-messageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/send-message.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/send-message.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# send-message

## Description

Submits a message to the Amazon Q in Connect session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/SendMessage)

## Synopsis

```
send-message
--assistant-id <value>
--session-id <value>
--type <value>
--message <value>
[--conversation-context <value>]
[--configuration <value>]
[--client-token <value>]
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

`--assistant-id` (string)

The identifier of the Amazon Q in Connect assistant.

`--session-id` (string)

The identifier of the Amazon Q in Connect session.

`--type` (string)

The message type.

Possible values:

- `TEXT`

`--message` (structure)

The message data to submit to the Amazon Q in Connect session.

value -> (tagged union structure)

The message input value.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.

text -> (structure)

The message data in text type.

value -> (string)

The value of the message data in text type.

Shorthand Syntax:

```
value={text={value=string}}
```

JSON Syntax:

```
{
  "value": {
    "text": {
      "value": "string"
    }
  }
}
```

`--conversation-context` (structure)

The conversation context before the Amazon Q in Connect session.

selfServiceConversationHistory -> (list)

The self service conversation history before the Amazon Q in Connect session.

(structure)

The conversation history data to included in conversation context data before the Amazon Q in Connect session.

turnNumber -> (integer)

The number of turn of the conversation history data.

inputTranscript -> (string)

The input transcript of the conversation history data.

botResponse -> (string)

The bot response of the conversation history data.

Shorthand Syntax:

```
selfServiceConversationHistory=[{turnNumber=integer,inputTranscript=string,botResponse=string},{turnNumber=integer,inputTranscript=string,botResponse=string}]
```

JSON Syntax:

```
{
  "selfServiceConversationHistory": [
    {
      "turnNumber": integer,
      "inputTranscript": "string",
      "botResponse": "string"
    }
    ...
  ]
}
```

`--configuration` (structure)

The configuration of the [SendMessage](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html) request.

generateFillerMessage -> (boolean)

Generates a filler response when tool selection is `QUESTION` .

Shorthand Syntax:

```
generateFillerMessage=boolean
```

JSON Syntax:

```
{
  "generateFillerMessage": true|false
}
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field.For more information about idempotency, see Making retries safe with idempotent APIs.

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

requestMessageId -> (string)

The identifier of the submitted message.

configuration -> (structure)

The configuration of the [SendMessage](https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html) request.

generateFillerMessage -> (boolean)

Generates a filler response when tool selection is `QUESTION` .

nextMessageToken -> (string)

The token for the next message, used by GetNextMessage.