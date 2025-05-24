# get-q-app-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/get-q-app-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/get-q-app-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qapps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qapps/index.html#cli-aws-qapps) ]

# get-q-app-session

## Description

Retrieves the current state and results for an active session of an Amazon Q App.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qapps-2023-11-27/GetQAppSession)

`get-q-app-session` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-q-app-session
--instance-id <value>
--session-id <value>
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

`--instance-id` (string)

The unique identifier of the Amazon Q Business application environment instance.

`--session-id` (string)

The unique identifier of the Q App session to retrieve.

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

sessionId -> (string)

The unique identifier of the Q App session.

sessionArn -> (string)

The Amazon Resource Name (ARN) of the Q App session.

sessionName -> (string)

The name of the Q App session.

appVersion -> (integer)

The version of the Q App used for the session.

latestPublishedAppVersion -> (integer)

The latest published version of the Q App used for the session.

status -> (string)

The current status of the Q App session.

cardStatus -> (map)

The current status for each card in the Q App session.

key -> (string)

value -> (structure)

The current status and value of a card in an active Amazon Q App session.

currentState -> (string)

The current state of the card.

currentValue -> (string)

The current value or result associated with the card.

submissions -> (list)

A list of previous submissions, if the card is a form card.

(structure)

A record created when a user submits a form card.

value -> (document)

The data submitted by the user.

submissionId -> (string)

The unique identifier of the submission.

timestamp -> (timestamp)

The date and time when the card is submitted.

userIsHost -> (boolean)

Indicates whether the current user is the owner of the Q App data collection session.