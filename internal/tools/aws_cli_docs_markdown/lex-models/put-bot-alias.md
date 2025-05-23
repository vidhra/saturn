# put-bot-aliasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot-alias.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-bot-alias.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lex-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/index.html#cli-aws-lex-models) ]

# put-bot-alias

## Description

Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see  versioning-aliases .

This operation requires permissions for the `lex:PutBotAlias` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutBotAlias)

## Synopsis

```
put-bot-alias
--name <value>
[--description <value>]
--bot-version <value>
--bot-name <value>
[--checksum <value>]
[--conversation-logs <value>]
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

`--name` (string)

The name of the alias. The name is *not* case sensitive.

`--description` (string)

A description of the alias.

`--bot-version` (string)

The version of the bot.

`--bot-name` (string)

The name of the bot.

`--checksum` (string)

Identifies a specific revision of the `$LATEST` version.

When you create a new bot alias, leave the `checksum` field blank. If you specify a checksum you get a `BadRequestException` exception.

When you want to update a bot alias, set the `checksum` field to the checksum of the most recent revision of the `$LATEST` version. If you donât specify the `checksum` field, or if the checksum does not match the `$LATEST` version, you get a `PreconditionFailedException` exception.

`--conversation-logs` (structure)

Settings for conversation logs for the alias.

logSettings -> (list)

The settings for your conversation logs. You can log the conversation text, conversation audio, or both.

(structure)

Settings used to configure delivery mode and destination for conversation logs.

logType -> (string)

The type of logging to enable. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.

destination -> (string)

Where the logs will be delivered. Text logs are delivered to a CloudWatch Logs log group. Audio logs are delivered to an S3 bucket.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the AWS KMS customer managed key for encrypting audio logs delivered to an S3 bucket. The key does not apply to CloudWatch Logs and is optional for S3 buckets.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs should be delivered.

iamRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to write to your CloudWatch Logs for text logs and your S3 bucket for audio logs. If audio encryption is enabled, this role also provides access permission for the AWS KMS key used for encrypting audio logs. For more information, see [Creating an IAM Role and Policy for Conversation Logs](https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-role-and-policy.html) .

Shorthand Syntax:

```
logSettings=[{logType=string,destination=string,kmsKeyArn=string,resourceArn=string},{logType=string,destination=string,kmsKeyArn=string,resourceArn=string}],iamRoleArn=string
```

JSON Syntax:

```
{
  "logSettings": [
    {
      "logType": "AUDIO"|"TEXT",
      "destination": "CLOUDWATCH_LOGS"|"S3",
      "kmsKeyArn": "string",
      "resourceArn": "string"
    }
    ...
  ],
  "iamRoleArn": "string"
}
```

`--tags` (list)

A list of tags to add to the bot alias. You can only add tags when you create an alias, you canât use the `PutBotAlias` operation to update the tags on a bot alias. To update tags, use the `TagResource` operation.

(structure)

A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case-sensitive and must be unique.

value -> (string)

The value associated with a key. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

name -> (string)

The name of the alias.

description -> (string)

A description of the alias.

botVersion -> (string)

The version of the bot that the alias points to.

botName -> (string)

The name of the bot that the alias points to.

lastUpdatedDate -> (timestamp)

The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.

createdDate -> (timestamp)

The date that the bot alias was created.

checksum -> (string)

The checksum for the current version of the alias.

conversationLogs -> (structure)

The settings that determine how Amazon Lex uses conversation logs for the alias.

logSettings -> (list)

The settings for your conversation logs. You can log text, audio, or both.

(structure)

The settings for conversation logs.

logType -> (string)

The type of logging that is enabled.

destination -> (string)

The destination where logs are delivered.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the key used to encrypt audio logs in an S3 bucket.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the CloudWatch Logs log group or S3 bucket where the logs are delivered.

resourcePrefix -> (string)

The resource prefix is the first part of the S3 object key within the S3 bucket that you specified to contain audio logs. For CloudWatch Logs it is the prefix of the log stream name within the log group that you specified.

iamRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used to write your logs to CloudWatch Logs or an S3 bucket.

tags -> (list)

A list of tags associated with a bot.

(structure)

A list of key/value pairs that identify a bot, bot alias, or bot channel. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

key -> (string)

The key for the tag. Keys are not case-sensitive and must be unique.

value -> (string)

The value associated with a key. The value may be an empty string but it canât be null.