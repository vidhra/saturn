# list-importsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-imports.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-imports.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-imports

## Description

Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListImports)

## Synopsis

```
list-imports
[--bot-id <value>]
[--bot-version <value>]
[--sort-by <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
[--locale-id <value>]
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

The unique identifier that Amazon Lex assigned to the bot.

`--bot-version` (string)

The version of the bot to list imports for.

`--sort-by` (structure)

Determines the field that the list of imports is sorted by. You can sort by the `LastUpdatedDateTime` field in ascending or descending order.

attribute -> (string)

The export field to use for sorting.

order -> (string)

The order to sort the list.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "LastUpdatedDateTime",
  "order": "Ascending"|"Descending"
}
```

`--filters` (list)

Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.

(structure)

Filters the response from the [ListImports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListImports.html) operation.

name -> (string)

The name of the field to use for filtering.

values -> (list)

The values to use to filter the response. The values must be `Bot` , `BotLocale` , or `CustomVocabulary` .

(string)

operator -> (string)

The operator to use for the filter. Specify EQ when the `ListImports` operation should return only resource types that equal the specified value. Specify CO when the `ListImports` operation should return resource types that contain the specified value.

Shorthand Syntax:

```
name=string,values=string,string,operator=string ...
```

JSON Syntax:

```
[
  {
    "name": "ImportResourceType",
    "values": ["string", ...],
    "operator": "CO"|"EQ"
  }
  ...
]
```

`--max-results` (integer)

The maximum number of imports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the `ListImports` operation contains more results than specified in the `maxResults` parameter, a token is returned in the response.

Use the returned token in the `nextToken` parameter of a `ListImports` request to return the next page of results. For a complete set of results, call the `ListImports` operation until the `nextToken` returned in the response is null.

`--locale-id` (string)

Specifies the locale that should be present in the list. If you donât specify a resource type in the `filters` parameter, the list contains both bot locales and custom vocabularies.

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

The unique identifier assigned by Amazon Lex to the bot.

botVersion -> (string)

The version of the bot that was imported. It will always be `DRAFT` .

importSummaries -> (list)

Summary information for the imports that meet the filter criteria specified in the request. The length of the list is specified in the `maxResults` parameter. If there are more imports available, the `nextToken` field contains a token to get the next page of results.

(structure)

Provides summary information about an import in an import list.

importId -> (string)

The unique identifier that Amazon Lex assigned to the import.

importedResourceId -> (string)

The unique identifier that Amazon Lex assigned to the imported resource.

importedResourceName -> (string)

The name that you gave the imported resource.

importStatus -> (string)

The status of the resource. When the status is `Completed` the resource is ready to build.

mergeStrategy -> (string)

The strategy used to merge existing bot or bot locale definitions with the imported definition.

creationDateTime -> (timestamp)

The date and time that the import was created.

lastUpdatedDateTime -> (timestamp)

The date and time that the import was last updated.

importedResourceType -> (string)

The type of resource that was imported.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the `ListImports` operation. If the `nextToken` field is present, you send the contents as the `nextToken` parameter of a `ListImports` operation request to get the next page of results.

localeId -> (string)

The locale specified in the request.