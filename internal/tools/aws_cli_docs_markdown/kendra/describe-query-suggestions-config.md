# describe-query-suggestions-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-query-suggestions-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-query-suggestions-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# describe-query-suggestions-config

## Description

Gets information on the settings of query suggestions for an index.

This is used to check the current settings applied to query suggestions.

`DescribeQuerySuggestionsConfig` is currently not supported in the Amazon Web Services GovCloud (US-West) region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/DescribeQuerySuggestionsConfig)

## Synopsis

```
describe-query-suggestions-config
--index-id <value>
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

The identifier of the index with query suggestions that you want to get information on.

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

Mode -> (string)

Whether query suggestions are currently in `ENABLED` mode or `LEARN_ONLY` mode.

By default, Amazon Kendra enables query suggestions.``LEARN_ONLY`` turns off query suggestions for your users. You can change the mode using the [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) API.

Status -> (string)

Whether the status of query suggestions settings is currently `ACTIVE` or `UPDATING` .

Active means the current settings apply and Updating means your changed settings are in the process of applying.

QueryLogLookBackWindowInDays -> (integer)

How recent your queries are in your query log time window (in days).

IncludeQueriesWithoutUserInformation -> (boolean)

`TRUE` to use all queries, otherwise use only queries that include user information to generate the query suggestions.

MinimumNumberOfQueryingUsers -> (integer)

The minimum number of unique users who must search a query in order for the query to be eligible to suggest to your users.

MinimumQueryCount -> (integer)

The minimum number of times a query must be searched in order for the query to be eligible to suggest to your users.

LastSuggestionsBuildTime -> (timestamp)

The Unix timestamp when query suggestions for an index was last updated.

Amazon Kendra automatically updates suggestions every 24 hours, after you change a setting or after you apply a [block list](https://docs.aws.amazon.com/kendra/latest/dg/query-suggestions.html#query-suggestions-blocklist) .

LastClearTime -> (timestamp)

The Unix timestamp when query suggestions for an index was last cleared.

After you clear suggestions, Amazon Kendra learns new suggestions based on new queries added to the query log from the time you cleared suggestions. Amazon Kendra only considers re-occurences of a query from the time you cleared suggestions.

TotalSuggestionsCount -> (integer)

The current total count of query suggestions for an index.

This count can change when you update your query suggestions settings, if you filter out certain queries from suggestions using a block list, and as the query log accumulates more queries for Amazon Kendra to learn from.

If the count is much lower than you expected, it could be because Amazon Kendra needs more queries in the query history to learn from or your current query suggestions settings are too strict.

AttributeSuggestionsConfig -> (structure)

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

The mode is set to either `ACTIVE` or `INACTIVE` . If the `Mode` for query history is set to `ENABLED` when calling [UpdateQuerySuggestionsConfig](https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateQuerySuggestionsConfig.html) and `AttributeSuggestionsMode` to use fields/attributes is set to `ACTIVE` , and you havenât set your `SuggestionTypes` preference to `DOCUMENT_ATTRIBUTES` , then Amazon Kendra uses the query history.