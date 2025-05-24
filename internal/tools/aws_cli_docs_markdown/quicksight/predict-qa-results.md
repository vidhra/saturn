# predict-qa-resultsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/predict-qa-results.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/predict-qa-results.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# predict-qa-results

## Description

Predicts existing visuals or generates new visuals to answer a given query.

This API uses [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html) to ensure that an end user is authenticated and receives the embed URL that is specific to that user. The IAM Identity Center application that the user has logged into needs to have [trusted Identity Propagation enabled for Amazon QuickSight](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.html) with the scope value set to `quicksight:read` . Before you use this action, make sure that you have configured the relevant Amazon QuickSight resource and permissions.

We recommend enabling the `QSearchStatus` API to unlock the full potential of `PredictQnA` . When `QSearchStatus` is enabled, it first checks the specified dashboard for any existing visuals that match the question. If no matching visuals are found, `PredictQnA` uses generative Q&A to provide an answer. To update the `QSearchStatus` , see [UpdateQuickSightQSearchConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/PredictQAResults)

## Synopsis

```
predict-qa-results
--aws-account-id <value>
--query-text <value>
[--include-quick-sight-q-index <value>]
[--include-generated-answer <value>]
[--max-topics-to-consider <value>]
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

`--aws-account-id` (string)

The ID of the Amazon Web Services account that the user wants to execute Predict QA results in.

`--query-text` (string)

The query text to be used to predict QA results.

`--include-quick-sight-q-index` (string)

Indicates whether Q indicies are included or excluded.

Possible values:

- `INCLUDE`
- `EXCLUDE`

`--include-generated-answer` (string)

Indicates whether generated answers are included or excluded.

Possible values:

- `INCLUDE`
- `EXCLUDE`

`--max-topics-to-consider` (integer)

The number of maximum topics to be considered to predict QA results.

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

PrimaryResult -> (structure)

The primary visual response.

ResultType -> (string)

The type of QA result.

DashboardVisual -> (structure)

The representation of a dashboard visual result.

DashboardId -> (string)

The ID of the dashboard.

DashboardName -> (string)

The name of the dashboard.

SheetId -> (string)

The ID of the sheet.

SheetName -> (string)

The name of the sheet.

VisualId -> (string)

The ID of the visual.

VisualTitle -> (string)

The title of the visual.

VisualSubtitle -> (string)

The subtitle of the visual.

DashboardUrl -> (string)

The URL of the dashboard.

GeneratedAnswer -> (structure)

The representation of a generated answer result.

QuestionText -> (string)

The question text.

AnswerStatus -> (string)

The answer status of the generated answer.

TopicId -> (string)

The ID of the topic.

TopicName -> (string)

The name of the topic.

Restatement -> (string)

The restatement for the answer.

QuestionId -> (string)

The ID of the question.

AnswerId -> (string)

The ID of the answer.

QuestionUrl -> (string)

The URL of the question.

AdditionalResults -> (list)

Additional visual responses.

(structure)

The QA result that is made from the `DashboardVisual` or `GeneratedAnswer` .

ResultType -> (string)

The type of QA result.

DashboardVisual -> (structure)

The representation of a dashboard visual result.

DashboardId -> (string)

The ID of the dashboard.

DashboardName -> (string)

The name of the dashboard.

SheetId -> (string)

The ID of the sheet.

SheetName -> (string)

The name of the sheet.

VisualId -> (string)

The ID of the visual.

VisualTitle -> (string)

The title of the visual.

VisualSubtitle -> (string)

The subtitle of the visual.

DashboardUrl -> (string)

The URL of the dashboard.

GeneratedAnswer -> (structure)

The representation of a generated answer result.

QuestionText -> (string)

The question text.

AnswerStatus -> (string)

The answer status of the generated answer.

TopicId -> (string)

The ID of the topic.

TopicName -> (string)

The name of the topic.

Restatement -> (string)

The restatement for the answer.

QuestionId -> (string)

The ID of the question.

AnswerId -> (string)

The ID of the answer.

QuestionUrl -> (string)

The URL of the question.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.