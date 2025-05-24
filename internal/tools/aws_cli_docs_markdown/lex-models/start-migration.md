# start-migrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/start-migration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/start-migration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# start-migration

## Description

Starts migrating a bot from Amazon Lex V1 to Amazon Lex V2. Migrate your bot when you want to take advantage of the new features of Amazon Lex V2.

For more information, see [Migrating a bot](https://docs.aws.amazon.com/lex/latest/dg/migrate.html) in the *Amazon Lex developer guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/StartMigration)

## Synopsis

```
start-migration
--v1-bot-name <value>
--v1-bot-version <value>
--v2-bot-name <value>
--v2-bot-role <value>
--migration-strategy <value>
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

`--v1-bot-name` (string)

The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.

`--v1-bot-version` (string)

The version of the bot to migrate to Amazon Lex V2. You can migrate the `$LATEST` version as well as any numbered version.

`--v2-bot-name` (string)

The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to.

- If the Amazon Lex V2 bot doesnât exist, you must use the `CREATE_NEW` migration strategy.
- If the Amazon Lex V2 bot exists, you must use the `UPDATE_EXISTING` migration strategy to change the contents of the Amazon Lex V2 bot.

`--v2-bot-role` (string)

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

`--migration-strategy` (string)

The strategy used to conduct the migration.

- `CREATE_NEW` - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.
- `UPDATE_EXISTING` - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesnât change any other locales in the Amazon Lex V2 bot. If the locale doesnât exist, a new locale is created in the Amazon Lex V2 bot.

Possible values:

- `CREATE_NEW`
- `UPDATE_EXISTING`

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

v1BotName -> (string)

The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2.

v1BotVersion -> (string)

The version of the bot to migrate to Amazon Lex V2.

v1BotLocale -> (string)

The locale used for the Amazon Lex V1 bot.

v2BotId -> (string)

The unique identifier for the Amazon Lex V2 bot.

v2BotRole -> (string)

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

migrationId -> (string)

The unique identifier that Amazon Lex assigned to the migration.

migrationStrategy -> (string)

The strategy used to conduct the migration.

migrationTimestamp -> (timestamp)

The date and time that the migration started.