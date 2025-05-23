# put-action-interactionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/put-action-interactions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/put-action-interactions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize-events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-events/index.html#cli-aws-personalize-events) ]

# put-action-interactions

## Description

Records action interaction event data. An *action interaction* event is an interaction between a user and an *action* . For example, a user taking an action, such a enrolling in a membership program or downloading your app.

For more information about recording action interactions, see [Recording action interaction events](https://docs.aws.amazon.com/personalize/latest/dg/recording-action-interaction-events.html) . For more information about actions in an Actions dataset, see [Actions dataset](https://docs.aws.amazon.com/personalize/latest/dg/actions-datasets.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-events-2018-03-22/PutActionInteractions)

## Synopsis

```
put-action-interactions
--tracking-id <value>
--action-interactions <value>
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

`--tracking-id` (string)

The ID of your action interaction event tracker. When you create an Action interactions dataset, Amazon Personalize creates an action interaction event tracker for you. For more information, see [Action interaction event tracker ID](https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-tracker-id.html) .

`--action-interactions` (list)

A list of action interaction events from the session.

(structure)

Represents an action interaction event sent using the `PutActionInteractions` API.

actionId -> (string)

The ID of the action the user interacted with. This corresponds to the `ACTION_ID` field of the Action interaction schema.

userId -> (string)

The ID of the user who interacted with the action. This corresponds to the `USER_ID` field of the Action interaction schema.

sessionId -> (string)

The ID associated with the userâs visit. Your application generates a unique `sessionId` when a user first visits your website or uses your application.

timestamp -> (timestamp)

The timestamp for when the action interaction event occurred. Timestamps must be in Unix epoch time format, in seconds.

eventType -> (string)

The type of action interaction event. You can specify `Viewed` , `Taken` , and `Not Taken` event types. For more information about action interaction event type data, see [Event type data](https://docs.aws.amazon.com/personalize/latest/dg/action-interaction-event-type-data.html) .

eventId -> (string)

An ID associated with the event. If an event ID is not provided, Amazon Personalize generates a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses the event ID to distinguish unique events. Any subsequent events after the first with the same event ID are not used in model training.

recommendationId -> (string)

The ID of the list of recommendations that contains the action the user interacted with.

impression -> (list)

A list of action IDs that represents the sequence of actions you have shown the user. For example, `["actionId1", "actionId2", "actionId3"]` . Amazon Personalize doesnât use impressions data from action interaction events. Instead, record multiple events for each action and use the `Viewed` event type.

(string)

properties -> (string)

A string map of event-specific data that you might choose to record. For example, if a user takes an action, other than the action ID, you might also send the number of actions taken by the user.

Each item in the map consists of a key-value pair. For example,

`{"numberOfActions": "12"}`

The keys use camel case names that match the fields in the Action interactions schema. In the above example, the `numberOfActions` would match the âNUMBER_OF_ACTIONSâ field defined in the Action interactions schema.

The following canât be included as a keyword for properties (case insensitive).

- userId
- sessionId
- eventType
- timestamp
- recommendationId
- impression

Shorthand Syntax:

```
actionId=string,userId=string,sessionId=string,timestamp=timestamp,eventType=string,eventId=string,recommendationId=string,impression=string,string,properties=string ...
```

JSON Syntax:

```
[
  {
    "actionId": "string",
    "userId": "string",
    "sessionId": "string",
    "timestamp": timestamp,
    "eventType": "string",
    "eventId": "string",
    "recommendationId": "string",
    "impression": ["string", ...],
    "properties": "string"
  }
  ...
]
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