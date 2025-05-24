# get-utterances-viewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-utterances-view.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-utterances-view.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# get-utterances-view

## Description

Use the `GetUtterancesView` operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.

For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the `GetUtterancesView` operation to see the requests that they have made and whether they have been successful. You might find that the utterance âI want flowersâ is not being recognized. You could add this utterance to the `OrderFlowers` intent so that your bot recognizes that utterance.

After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions.

Utterance statistics are generated once a day. Data is available for the last 15 days. You can request information for up to 5 versions of your bot in each request. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days. The response contains information about a maximum of 100 utterances for each version.

If you set `childDirected` field to true when you created your bot, if you are using slot obfuscation with one or more slots, or if you opted out of participating in improving Amazon Lex, utterances are not available.

This operation requires permissions for the `lex:GetUtterancesView` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetUtterancesView)

## Synopsis

```
get-utterances-view
--bot-name <value>
--bot-versions <value>
--status-type <value>
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

`--bot-name` (string)

The name of the bot for which utterance information should be returned.

`--bot-versions` (list)

An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.

(string)

Syntax:

```
"string" "string" ...
```

`--status-type` (string)

To return utterances that were recognized and handled, use `Detected` . To return utterances that were not recognized, use `Missed` .

Possible values:

- `Detected`
- `Missed`

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

botName -> (string)

The name of the bot for which utterance information was returned.

utterances -> (list)

An array of  UtteranceList objects, each containing a list of  UtteranceData objects describing the utterances that were processed by your bot. The response contains a maximum of 100 `UtteranceData` objects for each version. Amazon Lex returns the most frequent utterances received by the bot in the last 15 days.

(structure)

Provides a list of utterances that have been made to a specific version of your bot. The list contains a maximum of 100 utterances.

botVersion -> (string)

The version of the bot that processed the list.

utterances -> (list)

One or more  UtteranceData objects that contain information about the utterances that have been made to a bot. The maximum number of object is 100.

(structure)

Provides information about a single utterance that was made to your bot.

utteranceString -> (string)

The text that was entered by the user or the text representation of an audio clip.

count -> (integer)

The number of times that the utterance was processed.

distinctUsers -> (integer)

The total number of individuals that used the utterance.

firstUtteredDate -> (timestamp)

The date that the utterance was first recorded.

lastUtteredDate -> (timestamp)

The date that the utterance was last recorded.