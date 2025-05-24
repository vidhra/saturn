# create-roomÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-room.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-room.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivschat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/index.html#cli-aws-ivschat) ]

# create-room

## Description

Creates a room that allows clients to connect and pass messages.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivschat-2020-07-14/CreateRoom)

## Synopsis

```
create-room
[--name <value>]
[--maximum-message-rate-per-second <value>]
[--maximum-message-length <value>]
[--message-review-handler <value>]
[--tags <value>]
[--logging-configuration-identifiers <value>]
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

Room name. The value does not need to be unique.

`--maximum-message-rate-per-second` (integer)

Maximum number of messages per second that can be sent to the room (by all clients). Default: 10.

`--maximum-message-length` (integer)

Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500.

`--message-review-handler` (structure)

Configuration information for optional review of messages.

uri -> (string)

Identifier of the message review handler. Currently this must be an ARN of a lambda function.

fallbackResult -> (string)

Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out. (For the timeout period, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html) .) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user. Default: `ALLOW` .

Shorthand Syntax:

```
uri=string,fallbackResult=string
```

JSON Syntax:

```
{
  "uri": "string",
  "fallbackResult": "ALLOW"|"DENY"
}
```

`--tags` (map)

Tags to attach to the resource. Array of maps, each of the form `string:string (key:value)` . See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging Amazon Web Services Resources and Tag Editor* for details, including restrictions that apply to tags and âTag naming limits and requirementsâ; Amazon IVS Chat has no constraints beyond what is documented there.

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

`--logging-configuration-identifiers` (list)

Array of logging-configuration identifiers attached to the room.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a room**

The following `create-room` example creates a new room.

```
aws ivschat create-room \
    --name "test-room-1" \
    --logging-configuration-identifiers "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ" \
    --maximum-message-length 256 \
    --maximum-message-rate-per-second 5
```

Output:

```
{
    "arn": "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6",
    "id": "g1H2I3j4k5L6",
    "createTime": "2022-03-16T04:44:09+00:00",
    "loggingConfigurationIdentifiers": ["arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"],
    "maximumMessageLength": 256,
    "maximumMessageRatePerSecond": 5,
    "name": "test-room-1",
    "tags": {}
    "updateTime": "2022-03-16T07:22:09+00:00"
}
```

For more information, see [Step 2: Create a Chat Room](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html) in the *Amazon Interactive Video Service User Guide*.

## Output

arn -> (string)

Room ARN, assigned by the system.

id -> (string)

Room ID, generated by the system. This is a relative identifier, the part of the ARN that uniquely identifies the room.

name -> (string)

Room name, from the request (if specified).

createTime -> (timestamp)

Time when the room was created. This is an ISO 8601 timestamp; *note that this is returned as a string* .

updateTime -> (timestamp)

Time of the roomâs last update. This is an ISO 8601 timestamp; *note that this is returned as a string* .

maximumMessageRatePerSecond -> (integer)

Maximum number of messages per second that can be sent to the room (by all clients), from the request (if specified).

maximumMessageLength -> (integer)

Maximum number of characters in a single message, from the request (if specified).

messageReviewHandler -> (structure)

Configuration information for optional review of messages.

uri -> (string)

Identifier of the message review handler. Currently this must be an ARN of a lambda function.

fallbackResult -> (string)

Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out. (For the timeout period, see [Service Quotas](https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html) .) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user. Default: `ALLOW` .

tags -> (map)

Tags attached to the resource, from the request (if specified).

key -> (string)

value -> (string)

loggingConfigurationIdentifiers -> (list)

Array of logging configurations attached to the room, from the request (if specified).

(string)