# create-bot-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# create-bot-version

## Description

Creates an immutable version of the bot. When you create the first version of a bot, Amazon Lex sets the version number to 1. Subsequent bot versions increase in an increment of 1. The version number will always represent the total number of versions created of the bot, not the current number of versions. If a bot version is deleted, that bot version number will not be reused.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/CreateBotVersion)

## Synopsis

```
create-bot-version
--bot-id <value>
[--description <value>]
--bot-version-locale-specification <value>
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

The identifier of the bot to create the version for.

`--description` (string)

A description of the version. Use the description to help identify the version in lists.

`--bot-version-locale-specification` (map)

Specifies the locales that Amazon Lex adds to this version. You can choose the `Draft` version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.

key -> (string)

value -> (structure)

The version of a bot used for a bot locale.

sourceBotVersion -> (string)

The version of a bot used for a bot locale.

Shorthand Syntax:

```
KeyName1=sourceBotVersion=string,KeyName2=sourceBotVersion=string
```

JSON Syntax:

```
{"string": {
      "sourceBotVersion": "string"
    }
  ...}
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

botId -> (string)

The bot identifier specified in the request.

description -> (string)

The description of the version specified in the request.

botVersion -> (string)

The version number assigned to the version.

botVersionLocaleSpecification -> (map)

The source versions used for each locale in the new version.

key -> (string)

value -> (structure)

The version of a bot used for a bot locale.

sourceBotVersion -> (string)

The version of a bot used for a bot locale.

botStatus -> (string)

When you send a request to create or update a bot, Amazon Lex sets the status response element to `Creating` . After Amazon Lex builds the bot, it sets status to `Available` . If Amazon Lex canât build the bot, it sets status to `Failed` .

creationDateTime -> (timestamp)

A timestamp of the date and time that the version was created.