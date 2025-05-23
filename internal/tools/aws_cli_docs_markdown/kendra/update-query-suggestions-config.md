# update-query-suggestions-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-query-suggestions-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-query-suggestions-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# update-query-suggestions-config

## Description

Updates the settings of query suggestions for an index.

Amazon Kendra supports partial updates, so you only need to provide the fields you want to update.

If an update is currently processing, you need to wait for the update to finish before making another update.

Updates to query suggestions settings might not take effect right away. The time for your updated settings to take effect depends on the updates made and the number of search queries in your index.

You can still enable/disable query suggestions at any time.

`UpdateQuerySuggestionsConfig` is currently not supported in the Amazon Web Services GovCloud (US-West) region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/UpdateQuerySuggestionsConfig)

## Synopsis

```
update-query-suggestions-config
--index-id <value>
[--mode <value>]
[--query-log-look-back-window-in-days <value>]
[--include-queries-without-user-information | --no-include-queries-without-user-information]
[--minimum-number-of-querying-users <value>]
[--minimum-query-count <value>]
[--attribute-suggestions-config <value>]
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

`--index-id` (string)

The identifier of the index with query suggestions you want to update.

`--mode` (string)

Set the mode to `ENABLED` or `LEARN_ONLY` .

By default, Amazon Kendra enables query suggestions. `LEARN_ONLY` mode allows you to turn off query suggestions. You can to update this at any time.

In `LEARN_ONLY` mode, Amazon Kendra continues to learn from new queries to keep suggestions up to date for when you are ready to switch to ENABLED mode again.

Possible values:

- `ENABLED`
- `LEARN_ONLY`

`--query-log-look-back-window-in-days` (integer)

How recent your queries are in your query log time window.

The time window is the number of days from current day to past days.

By default, Amazon Kendra sets this to 180.

`--include-queries-without-user-information` | `--no-include-queries-without-user-information` (boolean)

`TRUE` to include queries without user information (i.e. all queries, irrespective of the user), otherwise `FALSE` to only include queries with user information.

If you pass user information to Amazon Kendra along with the queries, you can set this flag to `FALSE` and instruct Amazon Kendra to only consider queries with user information.

If you set to `FALSE` , Amazon Kendra only considers queries searched at least `MinimumQueryCount` times across `MinimumNumberOfQueryingUsers` unique users for suggestions.

If you set to `TRUE` , Amazon Kendra ignores all user information and learns from all queries.

`--minimum-number-of-querying-users` (integer)

The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.

Increasing this number might decrease the number of suggestions. However, this ensures a query is searched by many users and is truly popular to suggest to users.

How you tune this setting depends on your specific needs.

`--minimum-query-count` (integer)

The the minimum number of times a query must be searched in order to be eligible to suggest to your users.

Decreasing this number increases the number of suggestions. However, this affects the quality of suggestions as it sets a low bar for a query to be considered popular to suggest to users.

How you tune this setting depends on your specific needs.

`--attribute-suggestions-config` (structure)

Configuration information for the document fields/attributes that you want to base query suggestions on.

SuggestableConfigList -> (list)

The list of fields/attributes that you want to set as suggestible for query suggestions.

(structure)

Provides the configuration information for a document field/attribute that you want to base query suggestions on.

AttributeName -> (string)

The name of the document field/attribute.

Suggestable -> (boolean)

`TRUE` means the document field/attribute is suggestible, so the contents within the field can be used for query suggestions.

AttributeSuggestionsMode -> (string)

You can set the mode to `ACTIVE` or `INACTIVE` . You must also set `SuggestionTypes` as either `QUERY` or `DOCUMENT_ATTRIBUTES` and then call [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html) . If `Mode` to use query history is set to `ENABLED` when calling [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) and `AttributeSuggestionsMode` to use fields/attributes is set to `ACTIVE` , and you havenât set your `SuggestionTypes` preference to `DOCUMENT_ATTRIBUTES` , then Amazon Kendra uses the query history.

Shorthand Syntax:

```
SuggestableConfigList=[{AttributeName=string,Suggestable=boolean},{AttributeName=string,Suggestable=boolean}],AttributeSuggestionsMode=string
```

JSON Syntax:

```
{
  "SuggestableConfigList": [
    {
      "AttributeName": "string",
      "Suggestable": true|false
    }
    ...
  ],
  "AttributeSuggestionsMode": "ACTIVE"|"INACTIVE"
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

None