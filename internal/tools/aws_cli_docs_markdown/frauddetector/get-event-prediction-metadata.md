# get-event-prediction-metadataÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction-metadata.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction-metadata.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [frauddetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html#cli-aws-frauddetector) ]

# get-event-prediction-metadata

## Description

Gets details of the past fraud predictions for the specified event ID, event type, detector ID, and detector version ID that was generated in the specified time period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/frauddetector-2019-11-15/GetEventPredictionMetadata)

## Synopsis

```
get-event-prediction-metadata
--event-id <value>
--event-type-name <value>
--detector-id <value>
--detector-version-id <value>
--prediction-timestamp <value>
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

`--event-id` (string)

The event ID.

`--event-type-name` (string)

The event type associated with the detector specified for the prediction.

`--detector-id` (string)

The detector ID.

`--detector-version-id` (string)

The detector version ID.

`--prediction-timestamp` (string)

The timestamp that defines when the prediction was generated. The timestamp must be specified using ISO 8601 standard in UTC.

We recommend calling [ListEventPredictions](https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html) first, and using the `predictionTimestamp` value in the response to provide an accurate prediction timestamp value.

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

eventId -> (string)

The event ID.

eventTypeName -> (string)

The event type associated with the detector specified for this prediction.

entityId -> (string)

The entity ID.

entityType -> (string)

The entity type.

eventTimestamp -> (string)

The timestamp for when the prediction was generated for the associated event ID.

detectorId -> (string)

The detector ID.

detectorVersionId -> (string)

The detector version ID.

detectorVersionStatus -> (string)

The status of the detector version.

eventVariables -> (list)

A list of event variables that influenced the prediction scores.

(structure)

Information about the summary of an event variable that was evaluated for generating prediction.

name -> (string)

The event variable name.

value -> (string)

The value of the event variable.

source -> (string)

The event variable source.

rules -> (list)

List of rules associated with the detector version that were used for evaluating variable values.

(structure)

The details of the rule used for evaluating variable values.

ruleId -> (string)

The rule ID.

ruleVersion -> (string)

The rule version.

expression -> (string)

The rule expression.

expressionWithValues -> (string)

The rule expression value.

outcomes -> (list)

The rule outcome.

(string)

evaluated -> (boolean)

Indicates whether the rule was evaluated.

matched -> (boolean)

Indicates whether the rule matched.

ruleExecutionMode -> (string)

The execution mode of the rule used for evaluating variable values.

outcomes -> (list)

The outcomes of the matched rule, based on the rule execution mode.

(string)

evaluatedModelVersions -> (list)

Model versions that were evaluated for generating predictions.

(structure)

The model version evaluated for generating prediction.

modelId -> (string)

The model ID.

modelVersion -> (string)

The model version.

modelType -> (string)

The model type.

Valid values: `ONLINE_FRAUD_INSIGHTS` | `TRANSACTION_FRAUD_INSIGHTS`

evaluations -> (list)

Evaluations generated for the model version.

(structure)

The model version evalutions.

outputVariableName -> (string)

The output variable name.

evaluationScore -> (string)

The evaluation score generated for the model version.

predictionExplanations -> (structure)

The prediction explanations generated for the model version.

variableImpactExplanations -> (list)

The details of the event variableâs impact on the prediction score.

(structure)

The details of the event variableâs impact on the prediction score.

eventVariableName -> (string)

The event variable name.

relativeImpact -> (string)

The event variableâs relative impact in terms of magnitude on the prediction scores. The relative impact values consist of a numerical rating (0-5, 5 being the highest) and direction (increased/decreased) impact of the fraud risk.

logOddsImpact -> (float)

The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to +10, but range from - infinity to + infinity.

- A positive value indicates that the variable drove the risk score up.
- A negative value indicates that the variable drove the risk score down.

aggregatedVariablesImpactExplanations -> (list)

The details of the aggregated variables impact on the prediction score.

Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user` .

(structure)

The details of the impact of aggregated variables on the prediction score.

Account Takeover Insights (ATI) model uses the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, the model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user` .

eventVariableNames -> (list)

The names of all the event variables that were used to derive the aggregated variables.

(string)

relativeImpact -> (string)

The relative impact of the aggregated variables in terms of magnitude on the prediction scores.

logOddsImpact -> (float)

The raw, uninterpreted value represented as log-odds of the fraud. These values are usually between -10 to +10, but range from -infinity to +infinity.

- A positive value indicates that the variables drove the risk score up.
- A negative value indicates that the variables drove the risk score down.

evaluatedExternalModels -> (list)

External (Amazon SageMaker) models that were evaluated for generating predictions.

(structure)

The details of the external (Amazon Sagemaker) model evaluated for generating predictions.

modelEndpoint -> (string)

The endpoint of the external (Amazon Sagemaker) model.

useEventVariables -> (boolean)

Indicates whether event variables were used to generate predictions.

inputVariables -> (map)

Input variables use for generating predictions.

key -> (string)

value -> (string)

outputVariables -> (map)

Output variables.

key -> (string)

value -> (string)

predictionTimestamp -> (string)

The timestamp that defines when the prediction was generated.