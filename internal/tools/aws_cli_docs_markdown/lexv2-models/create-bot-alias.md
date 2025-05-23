# create-bot-aliasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-alias.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/create-bot-alias.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# create-bot-alias

## Description

Creates an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.

For example, you can create an alias called âPRODâ that your applications use to call the Amazon Lex bot.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/CreateBotAlias)

## Synopsis

```
create-bot-alias
--bot-alias-name <value>
[--description <value>]
[--bot-version <value>]
[--bot-alias-locale-settings <value>]
[--conversation-log-settings <value>]
[--sentiment-analysis-settings <value>]
--bot-id <value>
[--tags <value>]
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

`--bot-alias-name` (string)

The alias to create. The name must be unique for the bot.

`--description` (string)

A description of the alias. Use this description to help identify the alias.

`--bot-version` (string)

The version of the bot that this alias points to. You can use the [UpdateBotAlias](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html) operation to change the bot version associated with the alias.

`--bot-alias-locale-settings` (map)

Maps configuration information to a specific locale. You can use this parameter to specify a specific Lambda function to run different functions in different locales.

key -> (string)

value -> (structure)

Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the botâs locale.

enabled -> (boolean)

Determines whether the locale is enabled for the bot. If the value is `false` , the locale isnât available for use.

codeHookSpecification -> (structure)

Specifies the Lambda function that should be used in the locale.

lambdaCodeHook -> (structure)

Specifies a Lambda function that verifies requests to a bot or fulfills the userâs request to a bot.

lambdaARN -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

codeHookInterfaceVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.

Shorthand Syntax:

```
KeyName1=enabled=boolean,codeHookSpecification={lambdaCodeHook={lambdaARN=string,codeHookInterfaceVersion=string}},KeyName2=enabled=boolean,codeHookSpecification={lambdaCodeHook={lambdaARN=string,codeHookInterfaceVersion=string}}
```

JSON Syntax:

```
{"string": {
      "enabled": true|false,
      "codeHookSpecification": {
        "lambdaCodeHook": {
          "lambdaARN": "string",
          "codeHookInterfaceVersion": "string"
        }
      }
    }
  ...}
```

`--conversation-log-settings` (structure)

Specifies whether Amazon Lex logs text and audio for a conversation with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch Logs. Audio logs store audio input in Amazon S3.

textLogSettings -> (list)

The Amazon CloudWatch Logs settings for logging text and metadata.

(structure)

Defines settings to enable text conversation logs.

enabled -> (boolean)

Determines whether conversation logs should be stored for an alias.

destination -> (structure)

Defines the Amazon CloudWatch Logs destination log group for conversation text logs.

cloudWatch -> (structure)

Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

cloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.

logPrefix -> (string)

The prefix of the log stream name within the log group that you specified

selectiveLoggingEnabled -> (boolean)

The option to enable selective conversation log capture for text.

audioLogSettings -> (list)

The Amazon S3 settings for logging audio to an S3 bucket.

(structure)

Settings for logging audio of conversations between Amazon Lex and a user. You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.

enabled -> (boolean)

Determines whether audio logging in enabled for the bot.

destination -> (structure)

The location of audio log files collected when conversation logging is enabled for a bot.

s3Bucket -> (structure)

The Amazon S3 bucket where the audio log files are stored. The IAM role specified in the `roleArn` parameter of the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation must have permission to write to this bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.

s3BucketArn -> (string)

The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.

logPrefix -> (string)

The S3 prefix to assign to audio log files.

selectiveLoggingEnabled -> (boolean)

The option to enable selective conversation log capture for audio.

JSON Syntax:

```
{
  "textLogSettings": [
    {
      "enabled": true|false,
      "destination": {
        "cloudWatch": {
          "cloudWatchLogGroupArn": "string",
          "logPrefix": "string"
        }
      },
      "selectiveLoggingEnabled": true|false
    }
    ...
  ],
  "audioLogSettings": [
    {
      "enabled": true|false,
      "destination": {
        "s3Bucket": {
          "kmsKeyArn": "string",
          "s3BucketArn": "string",
          "logPrefix": "string"
        }
      },
      "selectiveLoggingEnabled": true|false
    }
    ...
  ]
}
```

`--sentiment-analysis-settings` (structure)

Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

detectSentiment -> (boolean)

Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

Shorthand Syntax:

```
detectSentiment=boolean
```

JSON Syntax:

```
{
  "detectSentiment": true|false
}
```

`--bot-id` (string)

The unique identifier of the bot that the alias applies to.

`--tags` (map)

A list of tags to add to the bot alias. You can only add tags when you create an alias, you canât use the `UpdateBotAlias` operation to update the tags on a bot alias. To update tags, use the `TagResource` operation.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
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

botAliasId -> (string)

The unique identifier of the bot alias.

botAliasName -> (string)

The name specified for the bot alias.

description -> (string)

The description specified for the bot alias.

botVersion -> (string)

The version of the bot associated with this alias.

botAliasLocaleSettings -> (map)

Configuration information for a specific locale.

key -> (string)

value -> (structure)

Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the botâs locale.

enabled -> (boolean)

Determines whether the locale is enabled for the bot. If the value is `false` , the locale isnât available for use.

codeHookSpecification -> (structure)

Specifies the Lambda function that should be used in the locale.

lambdaCodeHook -> (structure)

Specifies a Lambda function that verifies requests to a bot or fulfills the userâs request to a bot.

lambdaARN -> (string)

The Amazon Resource Name (ARN) of the Lambda function.

codeHookInterfaceVersion -> (string)

The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.

conversationLogSettings -> (structure)

The conversation log settings specified for the alias.

textLogSettings -> (list)

The Amazon CloudWatch Logs settings for logging text and metadata.

(structure)

Defines settings to enable text conversation logs.

enabled -> (boolean)

Determines whether conversation logs should be stored for an alias.

destination -> (structure)

Defines the Amazon CloudWatch Logs destination log group for conversation text logs.

cloudWatch -> (structure)

Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

cloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.

logPrefix -> (string)

The prefix of the log stream name within the log group that you specified

selectiveLoggingEnabled -> (boolean)

The option to enable selective conversation log capture for text.

audioLogSettings -> (list)

The Amazon S3 settings for logging audio to an S3 bucket.

(structure)

Settings for logging audio of conversations between Amazon Lex and a user. You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.

enabled -> (boolean)

Determines whether audio logging in enabled for the bot.

destination -> (structure)

The location of audio log files collected when conversation logging is enabled for a bot.

s3Bucket -> (structure)

The Amazon S3 bucket where the audio log files are stored. The IAM role specified in the `roleArn` parameter of the [CreateBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html) operation must have permission to write to this bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.

s3BucketArn -> (string)

The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.

logPrefix -> (string)

The S3 prefix to assign to audio log files.

selectiveLoggingEnabled -> (boolean)

The option to enable selective conversation log capture for audio.

sentimentAnalysisSettings -> (structure)

Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

detectSentiment -> (boolean)

Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

botAliasStatus -> (string)

The current status of the alias. The alias is first put into the `Creating` state. When the alias is ready to be used, it is put into the `Available` state. You can use the `DescribeBotAlias` operation to get the current state of an alias.

botId -> (string)

The unique identifier of the bot that this alias applies to.

creationDateTime -> (timestamp)

A Unix timestamp indicating the date and time that the bot alias was created.

tags -> (map)

A list of tags associated with the bot alias.

key -> (string)

value -> (string)