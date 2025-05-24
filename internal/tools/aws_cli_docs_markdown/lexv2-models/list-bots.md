# list-botsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-bots.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-bots.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-bots

## Description

Gets a list of available bots.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListBots)

## Synopsis

```
list-bots
[--sort-by <value>]
[--filters <value>]
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

`--sort-by` (structure)

Specifies sorting parameters for the list of bots. You can specify that the list be sorted by bot name in ascending or descending order.

attribute -> (string)

The attribute to use to sort the list of bots.

order -> (string)

The order to sort the list. You can choose ascending or descending.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "BotName",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.

(structure)

Filters the responses returned by the `ListBots` operation.

name -> (string)

The name of the field to filter the list of bots.

values -> (list)

The value to use for filtering the list of bots.

(string)

operator -> (string)

The operator to use for the filter. Specify `EQ` when the `ListBots` operation should return only aliases that equal the specified value. Specify `CO` when the `ListBots` operation should return aliases that contain the specified value.

Shorthand Syntax:

```
name=string,values=string,string,operator=string ...
```

JSON Syntax:

```
[
  {
    "name": "BotName"|"BotType",
    "values": ["string", ...],
    "operator": "CO"|"EQ"|"NE"
  }
  ...
]
```

`--max-results` (integer)

The maximum number of bots to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the `ListBots` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response.

Use the returned token in the `nextToken` parameter of a `ListBots` request to return the next page of results. For a complete set of results, call the `ListBots` operation until the `nextToken` returned in the response is null.

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

botSummaries -> (list)

Summary information for the bots that meet the filter criteria specified in the request. The length of the list is specified in the `maxResults` parameter of the request. If there are more bots available, the `nextToken` field contains a token to the next page of results.

(structure)

Summary information about a bot returned by the [ListBots](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListBots.html) operation.

botId -> (string)

The unique identifier assigned to the bot. Use this ID to get detailed information about the bot with the [DescribeBot](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeBot.html) operation.

botName -> (string)

The name of the bot.

description -> (string)

The description of the bot.

botStatus -> (string)

The current status of the bot. When the status is `Available` the bot is ready for use.

latestBotVersion -> (string)

The latest numerical version in use for the bot.

lastUpdatedDateTime -> (timestamp)

The date and time that the bot was last updated.

botType -> (string)

The type of the bot.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the `ListBots` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListBots` operation request to get the next page of results.