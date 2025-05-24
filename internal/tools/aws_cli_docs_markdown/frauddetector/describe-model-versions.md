# describe-model-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [frauddetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html#cli-aws-frauddetector) ]

# describe-model-versions

## Description

Gets all of the model versions for the specified model type or for the specified model type and model ID. You can also get details for a single, specified model version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/frauddetector-2019-11-15/DescribeModelVersions)

## Synopsis

```
describe-model-versions
[--model-id <value>]
[--model-version-number <value>]
[--model-type <value>]
[--next-token <value>]
[--max-results <value>]
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

`--model-id` (string)

The model ID.

`--model-version-number` (string)

The model version number.

`--model-type` (string)

The model type.

Possible values:

- `ONLINE_FRAUD_INSIGHTS`
- `TRANSACTION_FRAUD_INSIGHTS`
- `ACCOUNT_TAKEOVER_INSIGHTS`

`--next-token` (string)

The next token from the previous results.

`--max-results` (integer)

The maximum number of results to return.

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

modelVersionDetails -> (list)

The model version details.

(structure)

The details of the model version.

modelId -> (string)

The model ID.

modelType -> (string)

The model type.

modelVersionNumber -> (string)

The model version number.

status -> (string)

The status of the model version.

trainingDataSource -> (string)

The model version training data source.

trainingDataSchema -> (structure)

The training data schema.

modelVariables -> (list)

The training data schema variables.

(string)

labelSchema -> (structure)

The label schema.

labelMapper -> (map)

The label mapper maps the Amazon Fraud Detector supported model classification labels (`FRAUD` , `LEGIT` ) to the appropriate event type labels. For example, if â`FRAUD` â and â`LEGIT` â are Amazon Fraud Detector supported labels, this mapper could be: `{"FRAUD" => ["0"]` , `"LEGIT" => ["1"]}` or `{"FRAUD" => ["false"]` , `"LEGIT" => ["true"]}` or `{"FRAUD" => ["fraud", "abuse"]` , `"LEGIT" => ["legit", "safe"]}` . The value part of the mapper is a list, because you may have multiple label variants from your event type for a single Amazon Fraud Detector label.

key -> (string)

value -> (list)

(string)

unlabeledEventsTreatment -> (string)

The action to take for unlabeled events.

- Use `IGNORE` if you want the unlabeled events to be ignored. This is recommended when the majority of the events in the dataset are labeled.
- Use `FRAUD` if you want to categorize all unlabeled events as âFraudâ. This is recommended when most of the events in your dataset are fraudulent.
- Use `LEGIT` if you want to categorize all unlabeled events as âLegitâ. This is recommended when most of the events in your dataset are legitimate.
- Use `AUTO` if you want Amazon Fraud Detector to decide how to use the unlabeled data. This is recommended when there is significant unlabeled events in the dataset.

By default, Amazon Fraud Detector ignores the unlabeled data.

externalEventsDetail -> (structure)

The external events data details. This will be populated if the `trainingDataSource` for the model version is specified as `EXTERNAL_EVENTS` .

dataLocation -> (string)

The Amazon S3 bucket location for the data.

dataAccessRoleArn -> (string)

The ARN of the role that provides Amazon Fraud Detector access to the data location.

ingestedEventsDetail -> (structure)

The ingested events data details. This will be populated if the `trainingDataSource` for the model version is specified as `INGESTED_EVENTS` .

ingestedEventsTimeWindow -> (structure)

The start and stop time of the ingested events.

startTime -> (string)

Timestamp of the first ingensted event.

endTime -> (string)

Timestamp of the final ingested event.

trainingResult -> (structure)

The training results.

dataValidationMetrics -> (structure)

The validation metrics.

fileLevelMessages -> (list)

The file-specific model training data validation messages.

(structure)

The message details.

title -> (string)

The message title.

content -> (string)

The message content.

type -> (string)

The message type.

fieldLevelMessages -> (list)

The field-specific model training validation messages.

(structure)

The message details.

fieldName -> (string)

The field name.

identifier -> (string)

The message ID.

title -> (string)

The message title.

content -> (string)

The message content.

type -> (string)

The message type.

trainingMetrics -> (structure)

The training metric details.

auc -> (float)

The area under the curve. This summarizes true positive rate (TPR) and false positive rate (FPR) across all possible model score thresholds. A model with no predictive power has an AUC of 0.5, whereas a perfect model has a score of 1.0.

metricDataPoints -> (list)

The data points details.

(structure)

Model performance metrics data points.

fpr -> (float)

The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud.

precision -> (float)

The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent.

tpr -> (float)

The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate.

threshold -> (float)

The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.

variableImportanceMetrics -> (structure)

The variable importance metrics.

logOddsMetrics -> (list)

List of variable metrics.

(structure)

The log odds metric details.

variableName -> (string)

The name of the variable.

variableType -> (string)

The type of variable.

variableImportance -> (float)

The relative importance of the variable. For more information, see [Model variable importance](https://docs.aws.amazon.com/frauddetector/latest/ug/model-variable-importance.html) .

lastUpdatedTime -> (string)

The timestamp when the model was last updated.

createdTime -> (string)

The timestamp when the model was created.

arn -> (string)

The model version ARN.

trainingResultV2 -> (structure)

The training result details. The details include the relative importance of the variables.

dataValidationMetrics -> (structure)

The model training data validation metrics.

fileLevelMessages -> (list)

The file-specific model training data validation messages.

(structure)

The message details.

title -> (string)

The message title.

content -> (string)

The message content.

type -> (string)

The message type.

fieldLevelMessages -> (list)

The field-specific model training validation messages.

(structure)

The message details.

fieldName -> (string)

The field name.

identifier -> (string)

The message ID.

title -> (string)

The message title.

content -> (string)

The message content.

type -> (string)

The message type.

trainingMetricsV2 -> (structure)

The training metric details.

ofi -> (structure)

The Online Fraud Insights (OFI) model training metric details.

metricDataPoints -> (list)

The modelâs performance metrics data points.

(structure)

The Online Fraud Insights (OFI) model performance metrics data points.

fpr -> (float)

The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud.

precision -> (float)

The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent.

tpr -> (float)

The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate.

threshold -> (float)

The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.

modelPerformance -> (structure)

The modelâs overall performance score.

auc -> (float)

The area under the curve (auc). This summarizes the total positive rate (tpr) and false positive rate (FPR) across all possible model score thresholds.

uncertaintyRange -> (structure)

Indicates the range of area under curve (auc) expected from the OFI model. A range greater than 0.1 indicates higher model uncertainity.

lowerBoundValue -> (float)

The lower bound value of the area under curve (auc).

upperBoundValue -> (float)

The upper bound value of the area under curve (auc).

tfi -> (structure)

The Transaction Fraud Insights (TFI) model training metric details.

metricDataPoints -> (list)

The modelâs performance metrics data points.

(structure)

The performance metrics data points for Transaction Fraud Insights (TFI) model.

fpr -> (float)

The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud.

precision -> (float)

The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent.

tpr -> (float)

The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate.

threshold -> (float)

The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.

modelPerformance -> (structure)

The model performance score.

auc -> (float)

The area under the curve (auc). This summarizes the total positive rate (tpr) and false positive rate (FPR) across all possible model score thresholds.

uncertaintyRange -> (structure)

Indicates the range of area under curve (auc) expected from the TFI model. A range greater than 0.1 indicates higher model uncertainity.

lowerBoundValue -> (float)

The lower bound value of the area under curve (auc).

upperBoundValue -> (float)

The upper bound value of the area under curve (auc).

ati -> (structure)

The Account Takeover Insights (ATI) model training metric details.

metricDataPoints -> (list)

The modelâs performance metrics data points.

(structure)

The Account Takeover Insights (ATI) model performance metrics data points.

cr -> (float)

The challenge rate. This indicates the percentage of login events that the model recommends to challenge such as one-time password, multi-factor authentication, and investigations.

adr -> (float)

The anomaly discovery rate. This metric quantifies the percentage of anomalies that can be detected by the model at the selected score threshold. A lower score threshold increases the percentage of anomalies captured by the model, but would also require challenging a larger percentage of login events, leading to a higher customer friction.

threshold -> (float)

The modelâs threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud.

atodr -> (float)

The account takeover discovery rate. This metric quantifies the percentage of account compromise events that can be detected by the model at the selected score threshold. This metric is only available if 50 or more entities with at-least one labeled account takeover event is present in the ingested dataset.

modelPerformance -> (structure)

The modelâs overall performance scores.

asi -> (float)

The anomaly separation index (ASI) score. This metric summarizes the overall ability of the model to separate anomalous activities from the normal behavior. Depending on the business, a large fraction of these anomalous activities can be malicious and correspond to the account takeover attacks. A model with no separability power will have the lowest possible ASI score of 0.5, whereas the a model with a high separability power will have the highest possible ASI score of 1.0

variableImportanceMetrics -> (structure)

The variable importance metrics details.

logOddsMetrics -> (list)

List of variable metrics.

(structure)

The log odds metric details.

variableName -> (string)

The name of the variable.

variableType -> (string)

The type of variable.

variableImportance -> (float)

The relative importance of the variable. For more information, see [Model variable importance](https://docs.aws.amazon.com/frauddetector/latest/ug/model-variable-importance.html) .

aggregatedVariablesImportanceMetrics -> (structure)

The variable importance metrics of the aggregated variables.

Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user` .

logOddsMetrics -> (list)

List of variablesâ metrics.

(structure)

The log odds metric details.

Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user` .

variableNames -> (list)

The names of all the variables.

(string)

aggregatedVariablesImportance -> (float)

The relative importance of the variables in the list to the other event variable.

nextToken -> (string)

The next token.