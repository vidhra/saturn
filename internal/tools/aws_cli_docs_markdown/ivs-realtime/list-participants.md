# list-participantsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participants.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participants.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ivs-realtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/index.html#cli-aws-ivs-realtime) ]

# list-participants

## Description

Lists all participants in a specified stage session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ivs-realtime-2020-07-14/ListParticipants)

## Synopsis

```
list-participants
--stage-arn <value>
--session-id <value>
[--filter-by-user-id <value>]
[--filter-by-published | --no-filter-by-published]
[--filter-by-state <value>]
[--next-token <value>]
[--max-results <value>]
[--filter-by-recording-state <value>]
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

`--stage-arn` (string)

Stage ARN.

`--session-id` (string)

ID of the session within the stage.

`--filter-by-user-id` (string)

Filters the response list to match the specified user ID. Only one of `filterByUserId` , `filterByPublished` , `filterByState` , or `filterByRecordingState` can be provided per request. A `userId` is a customer-assigned name to help identify the token; this can be used to link a participant to a user in the customerâs own systems.

`--filter-by-published` | `--no-filter-by-published` (boolean)

Filters the response list to only show participants who published during the stage session. Only one of `filterByUserId` , `filterByPublished` , `filterByState` , or `filterByRecordingState` can be provided per request.

`--filter-by-state` (string)

Filters the response list to only show participants in the specified state. Only one of `filterByUserId` , `filterByPublished` , `filterByState` , or `filterByRecordingState` can be provided per request.

Possible values:

- `CONNECTED`
- `DISCONNECTED`

`--next-token` (string)

The first participant to retrieve. This is used for pagination; see the `nextToken` response field.

`--max-results` (integer)

Maximum number of results to return. Default: 50.

`--filter-by-recording-state` (string)

Filters the response list to only show participants with the specified recording state. Only one of `filterByUserId` , `filterByPublished` , `filterByState` , or `filterByRecordingState` can be provided per request.

Possible values:

- `STARTING`
- `ACTIVE`
- `STOPPING`
- `STOPPED`
- `FAILED`

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

**To get a list of stage participants**

The following `list-participants` example lists all participants for a specified session ID of a specified stage ARN (Amazon Resource Name).

```
aws ivs-realtime list-participants \
    --stage-arn arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh \
    --session-id st-a1b2c3d4e5f6g
```

Output:

```
{
    "participants": [
        {
            "firstJoinTime": "2023-04-26T20:30:34+00:00",
            "participantId": "abCDEf12GHIj"
            "published": true,
            "recordingState": "STOPPED",
            "state": "DISCONNECTED",
            "userId": ""
        }
    ]
}
```

For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html) in the *Amazon Interactive Video Service User Guide*.

## Output

participants -> (list)

List of the matching participants (summary information only).

(structure)

Summary object describing a participant that has joined a stage.

participantId -> (string)

Unique identifier for this participant, assigned by IVS.

userId -> (string)

Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customerâs own systems. This can be any UTF-8 encoded text. *This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information* .

state -> (string)

Whether the participant is connected to or disconnected from the stage.

firstJoinTime -> (timestamp)

ISO 8601 timestamp (returned as a string) when the participant first joined the stage session.

published -> (boolean)

Whether the participant ever published to the stage session.

recordingState -> (string)

The participantâs recording state.

nextToken -> (string)

If there are more participants than `maxResults` , use `nextToken` in the request to get the next set.