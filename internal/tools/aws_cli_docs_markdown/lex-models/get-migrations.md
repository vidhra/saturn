# get-migrationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-migrations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-migrations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# get-migrations

## Description

Gets a list of migrations between Amazon Lex V1 and Amazon Lex V2.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetMigrations)

## Synopsis

```
get-migrations
[--sort-by-attribute <value>]
[--sort-by-order <value>]
[--v1-bot-name-contains <value>]
[--migration-status-equals <value>]
[--max-results <value>]
[--next-token <value>]
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

`--sort-by-attribute` (string)

The field to sort the list of migrations by. You can sort by the Amazon Lex V1 bot name or the date and time that the migration was started.

Possible values:

- `V1_BOT_NAME`
- `MIGRATION_DATE_TIME`

`--sort-by-order` (string)

The order so sort the list.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--v1-bot-name-contains` (string)

Filters the list to contain only bots whose name contains the specified string. The string is matched anywhere in bot name.

`--migration-status-equals` (string)

Filters the list to contain only migrations in the specified state.

Possible values:

- `IN_PROGRESS`
- `COMPLETED`
- `FAILED`

`--max-results` (integer)

The maximum number of migrations to return in the response. The default is 10.

`--next-token` (string)

A pagination token that fetches the next page of migrations. If the response to this operation is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of migrations, specify the pagination token in the request.

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

migrationSummaries -> (list)

An array of summaries for migrations from Amazon Lex V1 to Amazon Lex V2. To see details of the migration, use the `migrationId` from the summary in a call to the operation.

(structure)

Provides information about migrating a bot from Amazon Lex V1 to Amazon Lex V2.

migrationId -> (string)

The unique identifier that Amazon Lex assigned to the migration.

v1BotName -> (string)

The name of the Amazon Lex V1 bot that is the source of the migration.

v1BotVersion -> (string)

The version of the Amazon Lex V1 bot that is the source of the migration.

v1BotLocale -> (string)

The locale of the Amazon Lex V1 bot that is the source of the migration.

v2BotId -> (string)

The unique identifier of the Amazon Lex V2 that is the destination of the migration.

v2BotRole -> (string)

The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot.

migrationStatus -> (string)

The status of the operation. When the status is `COMPLETE` the bot is available in Amazon Lex V2. There may be alerts and warnings that need to be resolved to complete the migration.

migrationStrategy -> (string)

The strategy used to conduct the migration.

migrationTimestamp -> (timestamp)

The date and time that the migration started.

nextToken -> (string)

If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of migrations.