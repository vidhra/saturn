# get-bot-channel-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-bot-channel-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# get-bot-channel-association

## Description

Returns information about the association between an Amazon Lex bot and a messaging platform.

This operation requires permissions for the `lex:GetBotChannelAssociation` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotChannelAssociation)

## Synopsis

```
get-bot-channel-association
--name <value>
--bot-name <value>
--bot-alias <value>
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

The name of the association between the bot and the channel. The name is case sensitive.

`--bot-name` (string)

The name of the Amazon Lex bot.

`--bot-alias` (string)

An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

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

The name of the association between the bot and the channel.

description -> (string)

A description of the association between the bot and the channel.

botAlias -> (string)

An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

botName -> (string)

The name of the Amazon Lex bot.

createdDate -> (timestamp)

The date that the association between the bot and the channel was created.

type -> (string)

The type of the messaging platform.

botConfiguration -> (map)

Provides information that the messaging platform needs to communicate with the Amazon Lex bot.

key -> (string)

value -> (string)

status -> (string)

The status of the bot channel.

- `CREATED` - The channel has been created and is ready for use.
- `IN_PROGRESS` - Channel creation is in progress.
- `FAILED` - There was an error creating the channel. For information about the reason for the failure, see the `failureReason` field.

failureReason -> (string)

If `status` is `FAILED` , Amazon Lex provides the reason that it failed to create the association.