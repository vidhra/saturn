# search-associated-transcriptsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/search-associated-transcripts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/search-associated-transcripts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# search-associated-transcripts

## Description

Search for associated transcripts that meet the specified criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/SearchAssociatedTranscripts)

## Synopsis

```
search-associated-transcripts
--bot-id <value>
--bot-version <value>
--locale-id <value>
--bot-recommendation-id <value>
[--search-order <value>]
--filters <value>
[--max-results <value>]
[--next-index <value>]
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

The unique identifier of the bot associated with the transcripts that you are searching.

`--bot-version` (string)

The version of the bot containing the transcripts that you are searching.

`--locale-id` (string)

The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)

`--bot-recommendation-id` (string)

The unique identifier of the bot recommendation associated with the transcripts to search.

`--search-order` (string)

How SearchResults are ordered. Valid values are Ascending or Descending. The default is Descending.

Possible values:

- `Ascending`
- `Descending`

`--filters` (list)

A list of filter objects.

(structure)

Filters to search for the associated transcript.

name -> (string)

The name of the field to use for filtering. The allowed names are IntentId and SlotTypeId.

values -> (list)

The values to use to filter the transcript.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "IntentId"|"SlotTypeId",
    "values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.

`--next-index` (integer)

If the response from the SearchAssociatedTranscriptsRequest operation contains more results than specified in the maxResults parameter, an index is returned in the response. Use that index in the nextIndex parameter to return the next page of results.

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

The unique identifier of the bot associated with the transcripts that you are searching.

botVersion -> (string)

The version of the bot containing the transcripts that you are searching.

localeId -> (string)

The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see [Supported languages](https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html)

botRecommendationId -> (string)

The unique identifier of the bot recommendation associated with the transcripts to search.

nextIndex -> (integer)

A index that indicates whether there are more results to return in a response to the SearchAssociatedTranscripts operation. If the nextIndex field is present, you send the contents as the nextIndex parameter of a SearchAssociatedTranscriptsRequest operation to get the next page of results.

associatedTranscripts -> (list)

The object that contains the associated transcript that meet the criteria you specified.

(structure)

The object containing information that associates the recommended intent/slot type with a conversation.

transcript -> (string)

The content of the transcript that meets the search filter criteria. For the JSON format of the transcript, see [Output transcript format](https://docs.aws.amazon.com/lexv2/latest/dg/designing-output-format.html) .

totalResults -> (integer)

The total number of transcripts returned by the search.