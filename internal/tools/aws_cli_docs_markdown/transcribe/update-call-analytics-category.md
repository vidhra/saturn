# update-call-analytics-categoryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-call-analytics-category.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-call-analytics-category.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# update-call-analytics-category

## Description

Updates the specified Call Analytics category with new rules. Note that the `UpdateCallAnalyticsCategory` operation overwrites all existing rules contained in the specified category. You cannot append additional rules onto an existing category.

To create a new category, see .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/UpdateCallAnalyticsCategory)

## Synopsis

```
update-call-analytics-category
--category-name <value>
--rules <value>
[--input-type <value>]
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

`--category-name` (string)

The name of the Call Analytics category you want to update. Category names are case sensitive.

`--rules` (list)

The rules used for the updated Call Analytics category. The rules you provide in this field replace the ones that are currently being used in the specified category.

(tagged union structure)

A rule is a set of criteria that you can specify to flag an attribute in your Call Analytics output. Rules define a Call Analytics category.

Rules can include these parameters: , , , and .

To learn more about Call Analytics rules and categories, see [Creating categories for post-call transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html) and [Creating categories for real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html) .

To learn more about Call Analytics, see [Analyzing call center audio with Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `NonTalkTimeFilter`, `InterruptionFilter`, `TranscriptFilter`, `SentimentFilter`.

NonTalkTimeFilter -> (structure)

Flag the presence or absence of periods of silence in your Call Analytics transcription output. Refer to for more detail.

Threshold -> (long)

Specify the duration, in milliseconds, of the period of silence that you want to flag. For example, you can flag a silent period that lasts 30,000 milliseconds.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for a period of silence. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for a period of silence. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

Negate -> (boolean)

Set to `TRUE` to flag periods of speech. Set to `FALSE` to flag periods of silence

InterruptionFilter -> (structure)

Flag the presence or absence of interruptions in your Call Analytics transcription output. Refer to for more detail.

Threshold -> (long)

Specify the duration of the interruptions in milliseconds. For example, you can flag speech that contains more than 10,000 milliseconds of interruptions.

ParticipantRole -> (string)

Specify the interrupter that you want to flag. Omitting this parameter is equivalent to specifying both participants.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for an interruption. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for an interruption. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

Negate -> (boolean)

Set to `TRUE` to flag speech that does not contain interruptions. Set to `FALSE` to flag speech that contains interruptions.

TranscriptFilter -> (structure)

Flag the presence or absence of specific words or phrases in your Call Analytics transcription output. Refer to for more detail.

TranscriptFilterType -> (string)

Flag the presence or absence of an exact match to the phrases that you specify. For example, if you specify the phrase âspeak to a managerâ as your `Targets` value, only that exact phrase is flagged.

Note that semantic matching is not supported. For example, if your customer says âspeak to *the* managerâ, instead of âspeak to *a* managerâ, your content is not flagged.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified key words or phrases. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified key words or phrases. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

ParticipantRole -> (string)

Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.

Negate -> (boolean)

Set to `TRUE` to flag the absence of the phrase that you specified in your request. Set to `FALSE` to flag the presence of the phrase that you specified in your request.

Targets -> (list)

Specify the phrases that you want to flag.

(string)

SentimentFilter -> (structure)

Flag the presence or absence of specific sentiments in your Call Analytics transcription output. Refer to for more detail.

Sentiments -> (list)

Specify the sentiments that you want to flag.

(string)

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified sentiments. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified sentiments. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

ParticipantRole -> (string)

Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.

Negate -> (boolean)

Set to `TRUE` to flag the sentiments that you didnât include in your request. Set to `FALSE` to flag the sentiments that you specified in your request.

Shorthand Syntax:

```
NonTalkTimeFilter={Threshold=long,AbsoluteTimeRange={StartTime=long,EndTime=long,First=long,Last=long},RelativeTimeRange={StartPercentage=integer,EndPercentage=integer,First=integer,Last=integer},Negate=boolean},InterruptionFilter={Threshold=long,ParticipantRole=string,AbsoluteTimeRange={StartTime=long,EndTime=long,First=long,Last=long},RelativeTimeRange={StartPercentage=integer,EndPercentage=integer,First=integer,Last=integer},Negate=boolean},TranscriptFilter={TranscriptFilterType=string,AbsoluteTimeRange={StartTime=long,EndTime=long,First=long,Last=long},RelativeTimeRange={StartPercentage=integer,EndPercentage=integer,First=integer,Last=integer},ParticipantRole=string,Negate=boolean,Targets=[string,string]},SentimentFilter={Sentiments=[string,string],AbsoluteTimeRange={StartTime=long,EndTime=long,First=long,Last=long},RelativeTimeRange={StartPercentage=integer,EndPercentage=integer,First=integer,Last=integer},ParticipantRole=string,Negate=boolean} ...
```

JSON Syntax:

```
[
  {
    "NonTalkTimeFilter": {
      "Threshold": long,
      "AbsoluteTimeRange": {
        "StartTime": long,
        "EndTime": long,
        "First": long,
        "Last": long
      },
      "RelativeTimeRange": {
        "StartPercentage": integer,
        "EndPercentage": integer,
        "First": integer,
        "Last": integer
      },
      "Negate": true|false
    },
    "InterruptionFilter": {
      "Threshold": long,
      "ParticipantRole": "AGENT"|"CUSTOMER",
      "AbsoluteTimeRange": {
        "StartTime": long,
        "EndTime": long,
        "First": long,
        "Last": long
      },
      "RelativeTimeRange": {
        "StartPercentage": integer,
        "EndPercentage": integer,
        "First": integer,
        "Last": integer
      },
      "Negate": true|false
    },
    "TranscriptFilter": {
      "TranscriptFilterType": "EXACT",
      "AbsoluteTimeRange": {
        "StartTime": long,
        "EndTime": long,
        "First": long,
        "Last": long
      },
      "RelativeTimeRange": {
        "StartPercentage": integer,
        "EndPercentage": integer,
        "First": integer,
        "Last": integer
      },
      "ParticipantRole": "AGENT"|"CUSTOMER",
      "Negate": true|false,
      "Targets": ["string", ...]
    },
    "SentimentFilter": {
      "Sentiments": ["POSITIVE"|"NEGATIVE"|"NEUTRAL"|"MIXED", ...],
      "AbsoluteTimeRange": {
        "StartTime": long,
        "EndTime": long,
        "First": long,
        "Last": long
      },
      "RelativeTimeRange": {
        "StartPercentage": integer,
        "EndPercentage": integer,
        "First": integer,
        "Last": integer
      },
      "ParticipantRole": "AGENT"|"CUSTOMER",
      "Negate": true|false
    }
  }
  ...
]
```

`--input-type` (string)

Choose whether you want to update a real-time or a post-call category. The input type you specify must match the input type specified when the category was created. For example, if you created a category with the `POST_CALL` input type, you must use `POST_CALL` as the input type when updating this category.

Possible values:

- `REAL_TIME`
- `POST_CALL`

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

CategoryProperties -> (structure)

Provides you with the properties of the Call Analytics category you specified in your `UpdateCallAnalyticsCategory` request.

CategoryName -> (string)

The name of the Call Analytics category. Category names are case sensitive and must be unique within an Amazon Web Services account.

Rules -> (list)

The rules used to define a Call Analytics category. Each category can have between 1 and 20 rules.

(tagged union structure)

A rule is a set of criteria that you can specify to flag an attribute in your Call Analytics output. Rules define a Call Analytics category.

Rules can include these parameters: , , , and .

To learn more about Call Analytics rules and categories, see [Creating categories for post-call transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html) and [Creating categories for real-time transcriptions](https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-stream.html) .

To learn more about Call Analytics, see [Analyzing call center audio with Call Analytics](https://docs.aws.amazon.com/transcribe/latest/dg/call-analytics.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `NonTalkTimeFilter`, `InterruptionFilter`, `TranscriptFilter`, `SentimentFilter`.

NonTalkTimeFilter -> (structure)

Flag the presence or absence of periods of silence in your Call Analytics transcription output. Refer to for more detail.

Threshold -> (long)

Specify the duration, in milliseconds, of the period of silence that you want to flag. For example, you can flag a silent period that lasts 30,000 milliseconds.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for a period of silence. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for a period of silence. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

Negate -> (boolean)

Set to `TRUE` to flag periods of speech. Set to `FALSE` to flag periods of silence

InterruptionFilter -> (structure)

Flag the presence or absence of interruptions in your Call Analytics transcription output. Refer to for more detail.

Threshold -> (long)

Specify the duration of the interruptions in milliseconds. For example, you can flag speech that contains more than 10,000 milliseconds of interruptions.

ParticipantRole -> (string)

Specify the interrupter that you want to flag. Omitting this parameter is equivalent to specifying both participants.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for an interruption. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for an interruption. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

Negate -> (boolean)

Set to `TRUE` to flag speech that does not contain interruptions. Set to `FALSE` to flag speech that contains interruptions.

TranscriptFilter -> (structure)

Flag the presence or absence of specific words or phrases in your Call Analytics transcription output. Refer to for more detail.

TranscriptFilterType -> (string)

Flag the presence or absence of an exact match to the phrases that you specify. For example, if you specify the phrase âspeak to a managerâ as your `Targets` value, only that exact phrase is flagged.

Note that semantic matching is not supported. For example, if your customer says âspeak to *the* managerâ, instead of âspeak to *a* managerâ, your content is not flagged.

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified key words or phrases. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified key words or phrases. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

ParticipantRole -> (string)

Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.

Negate -> (boolean)

Set to `TRUE` to flag the absence of the phrase that you specified in your request. Set to `FALSE` to flag the presence of the phrase that you specified in your request.

Targets -> (list)

Specify the phrases that you want to flag.

(string)

SentimentFilter -> (structure)

Flag the presence or absence of specific sentiments in your Call Analytics transcription output. Refer to for more detail.

Sentiments -> (list)

Specify the sentiments that you want to flag.

(string)

AbsoluteTimeRange -> (structure)

Makes it possible to specify a time range (in milliseconds) in your audio, during which you want to search for the specified sentiments. See for more detail.

StartTime -> (long)

The time, in milliseconds, when Amazon Transcribe starts searching for the specified criteria in your audio. If you include `StartTime` in your request, you must also include `EndTime` .

EndTime -> (long)

The time, in milliseconds, when Amazon Transcribe stops searching for the specified criteria in your audio. If you include `EndTime` in your request, you must also include `StartTime` .

First -> (long)

The time, in milliseconds, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (long)

The time, in milliseconds, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

RelativeTimeRange -> (structure)

Makes it possible to specify a time range (in percentage) in your media file, during which you want to search for the specified sentiments. See for more detail.

StartPercentage -> (integer)

The time, in percentage, when Amazon Transcribe starts searching for the specified criteria in your media file. If you include `StartPercentage` in your request, you must also include `EndPercentage` .

EndPercentage -> (integer)

The time, in percentage, when Amazon Transcribe stops searching for the specified criteria in your media file. If you include `EndPercentage` in your request, you must also include `StartPercentage` .

First -> (integer)

The time, in percentage, from the start of your media file until the specified value. Amazon Transcribe searches for your specified criteria in this time segment.

Last -> (integer)

The time, in percentage, from the specified value until the end of your media file. Amazon Transcribe searches for your specified criteria in this time segment.

ParticipantRole -> (string)

Specify the participant that you want to flag. Omitting this parameter is equivalent to specifying both participants.

Negate -> (boolean)

Set to `TRUE` to flag the sentiments that you didnât include in your request. Set to `FALSE` to flag the sentiments that you specified in your request.

CreateTime -> (timestamp)

The date and time the specified Call Analytics category was created.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.

LastUpdateTime -> (timestamp)

The date and time the specified Call Analytics category was last updated.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-05T12:45:32.691000-07:00` represents 12:45 PM UTC-7 on May 5, 2022.

Tags -> (list)

The tags, each in the form of a key:value pair, assigned to the specified call analytics category.

(structure)

Adds metadata, in the form of a key:value pair, to the specified resource.

For example, you could add the tag `Department:Sales` to a resource to indicate that it pertains to your organizationâs sales department. You can also use tags for tag-based access control.

To learn more about tagging, see [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html) .

Key -> (string)

The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the key is âDepartmentâ.

Value -> (string)

The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag `Department:Sales` , the value is âSalesâ.

Note that you can set the value of a tag to an empty string, but you canât set the value of a tag to null. Omitting the tag value is the same as using an empty string.

InputType -> (string)

The input type associated with the specified category. `POST_CALL` refers to a category that is applied to batch transcriptions; `REAL_TIME` refers to a category that is applied to streaming transcriptions.