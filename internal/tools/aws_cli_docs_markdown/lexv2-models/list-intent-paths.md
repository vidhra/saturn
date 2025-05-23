# list-intent-pathsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-intent-paths.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-intent-paths.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-intent-paths

## Description

Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:

- `startDateTime` and `endDateTime` â Define a time range for which you want to retrieve results.
- `intentPath` â Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the `intentPath` field with `/BookCar/BookHotel` to see details about how many times users invoked the `BookCar` and `BookHotel` intents in that order.

Use the optional `filters` field to filter the results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListIntentPaths)

## Synopsis

```
list-intent-paths
--bot-id <value>
--start-date-time <value>
--end-date-time <value>
--intent-path <value>
[--filters <value>]
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

`--bot-id` (string)

The identifier for the bot for which you want to retrieve intent path metrics.

`--start-date-time` (timestamp)

The date and time that marks the beginning of the range of time for which you want to see intent path metrics.

`--end-date-time` (timestamp)

The date and time that marks the end of the range of time for which you want to see intent path metrics.

`--intent-path` (string)

The intent path for which you want to retrieve metrics. Use a forward slash to separate intents in the path. For example:

- /BookCar
- /BookCar/BookHotel
- /BookHotel/BookCar

`--filters` (list)

A list of objects, each describes a condition by which you want to filter the results.

(structure)

Contains fields describing a condition by which to filter the paths. The expression may be understood as `name` `operator` `values` . For example:

- `LocaleId EQ en` â The locale is âenâ.
- `BotVersion EQ 2` â The bot version is equal to two.

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .

name -> (string)

The category by which to filter the intent paths. The descriptions for each option are as follows:

- `BotAlias` â The name of the bot alias.
- `BotVersion` â The version of the bot.
- `LocaleId` â The locale of the bot.
- `Modality` â The modality of the session with the bot (audio, DTMF, or text).
- `Channel` â The channel that the bot is integrated with.

operator -> (string)

The operation by which to filter the category. The following operations are possible:

- `CO` â Contains
- `EQ` â Equals
- `GT` â Greater than
- `LT` â Less than

The operators that each filter supports are listed below:

- `BotAlias` â `EQ` .
- `BotVersion` â `EQ` .
- `LocaleId` â `EQ` .
- `Modality` â `EQ` .
- `Channel` â `EQ` .

values -> (list)

An array containing the values of the category by which to apply the operator to filter the results. You can provide multiple values if the operator is `EQ` or `CO` . If you provide multiple values, you filter for results that equal/contain any of the values. For example, if the `name` , `operator` , and `values` fields are `Modality` , `EQ` , and `[Speech, Text]` , the operation filters for results where the modality was either `Speech` or `Text` .

(string)

Shorthand Syntax:

```
name=string,operator=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "BotAliasId"|"BotVersion"|"LocaleId"|"Modality"|"Channel",
    "operator": "EQ"|"GT"|"LT",
    "values": ["string", ...]
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

nodeSummaries -> (list)

A list of objects, each of which contains information about a node in the intent path for which you requested metrics.

(structure)

An object containing information about the requested path.

intentName -> (string)

The name of the intent at the end of the requested path.

intentPath -> (string)

The path.

intentCount -> (integer)

The total number of sessions that follow the given path to the given intent.

intentLevel -> (integer)

The number of intents up to and including the requested path.

nodeType -> (string)

Specifies whether the node is the end of a path (`Exit` ) or not (`Inner` ).