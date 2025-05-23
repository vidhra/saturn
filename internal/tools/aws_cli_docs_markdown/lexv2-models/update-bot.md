# update-botÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/update-bot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/update-bot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# update-bot

## Description

Updates the configuration of an existing bot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/UpdateBot)

## Synopsis

```
update-bot
--bot-id <value>
--bot-name <value>
[--description <value>]
--role-arn <value>
--data-privacy <value>
--idle-session-ttl-in-seconds <value>
[--bot-type <value>]
[--bot-members <value>]
[--error-log-settings <value>]
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

The unique identifier of the bot to update. This identifier is returned by the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation.

`--bot-name` (string)

The new name of the bot. The name must be unique in the account that creates the bot.

`--description` (string)

A description of the bot.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that has permissions to access the bot.

`--data-privacy` (structure)

Provides information on additional privacy protections Amazon Lex should use with the botâs data.

childDirected -> (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ](http://aws.amazon.com/lex/faqs#data-security) .

Shorthand Syntax:

```
childDirected=boolean
```

JSON Syntax:

```
{
  "childDirected": true|false
}
```

`--idle-session-ttl-in-seconds` (integer)

The time, in seconds, that Amazon Lex should keep information about a userâs conversation with the bot.

A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.

You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.

`--bot-type` (string)

The type of the bot to be updated.

Possible values:

- `Bot`
- `BotNetwork`

`--bot-members` (list)

The list of bot members in the network associated with the update action.

(structure)

A bot that is a member of a network of bots.

botMemberId -> (string)

The unique ID of a bot that is a member of this network of bots.

botMemberName -> (string)

The unique name of a bot that is a member of this network of bots.

botMemberAliasId -> (string)

The alias ID of a bot that is a member of this network of bots.

botMemberAliasName -> (string)

The alias name of a bot that is a member of this network of bots.

botMemberVersion -> (string)

The version of a bot that is a member of this network of bots.

Shorthand Syntax:

```
botMemberId=string,botMemberName=string,botMemberAliasId=string,botMemberAliasName=string,botMemberVersion=string ...
```

JSON Syntax:

```
[
  {
    "botMemberId": "string",
    "botMemberName": "string",
    "botMemberAliasId": "string",
    "botMemberAliasName": "string",
    "botMemberVersion": "string"
  }
  ...
]
```

`--error-log-settings` (structure)

Allows you to modify how Amazon Lex logs errors during bot interactions, including destinations for error logs and the types of errors to be captured.

enabled -> (boolean)

Settings parameters for the error logs, when it is enabled.

Shorthand Syntax:

```
enabled=boolean
```

JSON Syntax:

```
{
  "enabled": true|false
}
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

The unique identifier of the bot that was updated.

botName -> (string)

The name of the bot after the update.

description -> (string)

The description of the bot after the update.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used by the bot after the update.

dataPrivacy -> (structure)

The data privacy settings for the bot after the update.

childDirected -> (boolean)

For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Childrenâs Online Privacy Protection Act (COPPA) by specifying `true` or `false` in the `childDirected` field. By specifying `true` in the `childDirected` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying `false` in the `childDirected` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the `childDirected` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the [Amazon Lex FAQ](http://aws.amazon.com/lex/faqs#data-security) .

idleSessionTTLInSeconds -> (integer)

The session timeout, in seconds, for the bot after the update.

botStatus -> (string)

Shows the current status of the bot. The bot is first in the `Creating` status. Once the bot is read for use, it changes to the `Available` status. After the bot is created, you can use the `DRAFT` version of the bot.

creationDateTime -> (timestamp)

A timestamp of the date and time that the bot was created.

lastUpdatedDateTime -> (timestamp)

A timestamp of the date and time that the bot was last updated.

botType -> (string)

The type of the bot that was updated.

botMembers -> (list)

The list of bot members in the network that was updated.

(structure)

A bot that is a member of a network of bots.

botMemberId -> (string)

The unique ID of a bot that is a member of this network of bots.

botMemberName -> (string)

The unique name of a bot that is a member of this network of bots.

botMemberAliasId -> (string)

The alias ID of a bot that is a member of this network of bots.

botMemberAliasName -> (string)

The alias name of a bot that is a member of this network of bots.

botMemberVersion -> (string)

The version of a bot that is a member of this network of bots.

errorLogSettings -> (structure)

Settings for managing error logs within the response of an update bot operation.

enabled -> (boolean)

Settings parameters for the error logs, when it is enabled.