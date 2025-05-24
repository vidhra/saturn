# get-model-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [frauddetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html#cli-aws-frauddetector) ]

# get-model-version

## Description

Gets the details of the specified model version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/frauddetector-2019-11-15/GetModelVersion)

## Synopsis

```
get-model-version
--model-id <value>
--model-type <value>
--model-version-number <value>
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

`--model-type` (string)

The model type.

Possible values:

- `ONLINE_FRAUD_INSIGHTS`
- `TRANSACTION_FRAUD_INSIGHTS`
- `ACCOUNT_TAKEOVER_INSIGHTS`

`--model-version-number` (string)

The model version number.

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

modelId -> (string)

The model ID.

modelType -> (string)

The model type.

modelVersionNumber -> (string)

The model version number.

trainingDataSource -> (string)

The training data source.

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

The details of the external events data used for training the model version. This will be populated if the `trainingDataSource` is `EXTERNAL_EVENTS`

dataLocation -> (string)

The Amazon S3 bucket location for the data.

dataAccessRoleArn -> (string)

The ARN of the role that provides Amazon Fraud Detector access to the data location.

ingestedEventsDetail -> (structure)

The details of the ingested events data used for training the model version. This will be populated if the `trainingDataSource` is `INGESTED_EVENTS` .

ingestedEventsTimeWindow -> (structure)

The start and stop time of the ingested events.

startTime -> (string)

Timestamp of the first ingensted event.

endTime -> (string)

Timestamp of the final ingested event.

status -> (string)

The model version status.

Possible values are:

- `TRAINING_IN_PROGRESS`
- `TRAINING_COMPLETE`
- `ACTIVATE_REQUESTED`
- `ACTIVATE_IN_PROGRESS`
- `ACTIVE`
- `INACTIVATE_REQUESTED`
- `INACTIVATE_IN_PROGRESS`
- `INACTIVE`
- `ERROR`

arn -> (string)

The model version ARN.