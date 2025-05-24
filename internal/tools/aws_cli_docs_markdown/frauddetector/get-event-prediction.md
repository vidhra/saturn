# get-event-predictionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-event-prediction.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [frauddetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/index.html#cli-aws-frauddetector) ]

# get-event-prediction

## Description

Evaluates an event against a detector version. If a version ID is not provided, the detectorâs (`ACTIVE` ) version is used.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/frauddetector-2019-11-15/GetEventPrediction)

## Synopsis

```
get-event-prediction
--detector-id <value>
[--detector-version-id <value>]
--event-id <value>
--event-type-name <value>
--entities <value>
--event-timestamp <value>
--event-variables <value>
[--external-model-endpoint-data-blobs <value>]
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

`--detector-id` (string)

The detector ID.

`--detector-version-id` (string)

The detector version ID.

`--event-id` (string)

The unique ID used to identify the event.

`--event-type-name` (string)

The event type associated with the detector specified for the prediction.

`--entities` (list)

The entity type (associated with the detectorâs event type) and specific entity ID representing who performed the event. If an entity id is not available, use âUNKNOWN.â

(structure)

The entity details.

entityType -> (string)

The entity type.

entityId -> (string)

The entity ID. If you do not know the `entityId` , you can pass `unknown` , which is areserved string literal.

Shorthand Syntax:

```
entityType=string,entityId=string ...
```

JSON Syntax:

```
[
  {
    "entityType": "string",
    "entityId": "string"
  }
  ...
]
```

`--event-timestamp` (string)

Timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.

`--event-variables` (map)

Names of the event typeâs variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.

### Warning

You must provide at least one eventVariable

To ensure most accurate fraud prediction and to simplify your data preparation, Amazon Fraud Detector will replace all missing variables or values as follows:

**For Amazon Fraud Detector trained models:**

If a null value is provided explicitly for a variable or if a variable is missing, model will replace the null value or the missing variable (no variable name in the eventVariables map) with calculated default mean/medians for numeric variables and with special values for categorical variables.

**For imported SageMaker models:**

If a null value is provided explicitly for a variable, the model and rules will use ânullâ as the value. If a variable is not provided (no variable name in the eventVariables map), model and rules will use the default value that is provided for the variable.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--external-model-endpoint-data-blobs` (map)

The Amazon SageMaker model endpoint input data blobs.

key -> (string)

value -> (structure)

A pre-formed Amazon SageMaker model input you can include if your detector version includes an imported Amazon SageMaker model endpoint with pass-through input configuration.

byteBuffer -> (blob)

The byte buffer of the Amazon SageMaker model endpoint input data blob.

contentType -> (string)

The content type of the Amazon SageMaker model endpoint input data blob.

Shorthand Syntax:

```
KeyName1=byteBuffer=blob,contentType=string,KeyName2=byteBuffer=blob,contentType=string
```

JSON Syntax:

```
{"string": {
      "byteBuffer": blob,
      "contentType": "string"
    }
  ...}
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

modelScores -> (list)

The model scores. Amazon Fraud Detector generates model scores between 0 and 1000, where 0 is low fraud risk and 1000 is high fraud risk. Model scores are directly related to the false positive rate (FPR). For example, a score of 600 corresponds to an estimated 10% false positive rate whereas a score of 900 corresponds to an estimated 2% false positive rate.

(structure)

The fraud prediction scores.

modelVersion -> (structure)

The model version.

modelId -> (string)

The model ID.

modelType -> (string)

The model type.

modelVersionNumber -> (string)

The model version number.

arn -> (string)

The model version ARN.

scores -> (map)

The modelâs fraud prediction scores.

key -> (string)

value -> (float)

ruleResults -> (list)

The results from the rules.

(structure)

The rule results.

ruleId -> (string)

The rule ID that was matched, based on the rule execution mode.

outcomes -> (list)

The outcomes of the matched rule, based on the rule execution mode.

(string)

externalModelOutputs -> (list)

The model scores for Amazon SageMaker models.

(structure)

The fraud prediction scores from Amazon SageMaker model.

externalModel -> (structure)

The Amazon SageMaker model.

modelEndpoint -> (string)

The endpoint of the Amazon SageMaker model.

modelSource -> (string)

The source of the model.

outputs -> (map)

The fraud prediction scores from Amazon SageMaker model.

key -> (string)

value -> (string)