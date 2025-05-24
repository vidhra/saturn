# describe-solution-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-solution-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# describe-solution-version

## Description

Describes a specific version of a solution. For more information on solutions, see [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/DescribeSolutionVersion)

## Synopsis

```
describe-solution-version
--solution-version-arn <value>
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

`--solution-version-arn` (string)

The Amazon Resource Name (ARN) of the solution version.

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

solutionVersion -> (structure)

The solution version.

name -> (string)

The name of the solution version.

solutionVersionArn -> (string)

The ARN of the solution version.

solutionArn -> (string)

The ARN of the solution.

performHPO -> (boolean)

Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is `false` .

performAutoML -> (boolean)

When true, Amazon Personalize searches for the most optimal recipe according to the solution configuration. When false (the default), Amazon Personalize uses `recipeArn` .

recipeArn -> (string)

The ARN of the recipe used in the solution.

eventType -> (string)

The event type (for example, âclickâ or âlikeâ) that is used for training the model.

datasetGroupArn -> (string)

The Amazon Resource Name (ARN) of the dataset group providing the training data.

solutionConfig -> (structure)

Describes the configuration properties for the solution.

eventValueThreshold -> (string)

Only events with a value greater than or equal to this threshold are used for training a model.

hpoConfig -> (structure)

Describes the properties for hyperparameter optimization (HPO).

hpoObjective -> (structure)

The metric to optimize during HPO.

### Note

Amazon Personalize doesnât support configuring the `hpoObjective` at this time.

type -> (string)

The type of the metric. Valid values are `Maximize` and `Minimize` .

metricName -> (string)

The name of the metric.

metricRegex -> (string)

A regular expression for finding the metric in the training job logs.

hpoResourceConfig -> (structure)

Describes the resource configuration for HPO.

maxNumberOfTrainingJobs -> (string)

The maximum number of training jobs when you create a solution version. The maximum value for `maxNumberOfTrainingJobs` is `40` .

maxParallelTrainingJobs -> (string)

The maximum number of parallel training jobs when you create a solution version. The maximum value for `maxParallelTrainingJobs` is `10` .

algorithmHyperParameterRanges -> (structure)

The hyperparameters and their allowable ranges.

integerHyperParameterRanges -> (list)

The integer-valued hyperparameters and their ranges.

(structure)

Provides the name and range of an integer-valued hyperparameter.

name -> (string)

The name of the hyperparameter.

minValue -> (integer)

The minimum allowable value for the hyperparameter.

maxValue -> (integer)

The maximum allowable value for the hyperparameter.

continuousHyperParameterRanges -> (list)

The continuous hyperparameters and their ranges.

(structure)

Provides the name and range of a continuous hyperparameter.

name -> (string)

The name of the hyperparameter.

minValue -> (double)

The minimum allowable value for the hyperparameter.

maxValue -> (double)

The maximum allowable value for the hyperparameter.

categoricalHyperParameterRanges -> (list)

The categorical hyperparameters and their ranges.

(structure)

Provides the name and range of a categorical hyperparameter.

name -> (string)

The name of the hyperparameter.

values -> (list)

A list of the categories for the hyperparameter.

(string)

algorithmHyperParameters -> (map)

Lists the algorithm hyperparameters and their values.

key -> (string)

value -> (string)

featureTransformationParameters -> (map)

Lists the feature transformation parameters.

key -> (string)

value -> (string)

autoMLConfig -> (structure)

The [AutoMLConfig](https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html) object containing a list of recipes to search when AutoML is performed.

metricName -> (string)

The metric to optimize.

recipeList -> (list)

The list of candidate recipes.

(string)

eventsConfig -> (structure)

Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.

eventParametersList -> (list)

A list of event parameters, which includes event types and their event value thresholds and weights.

(structure)

Describes the parameters of events, which are used in solution creation.

eventType -> (string)

The name of the event type to be considered for solution creation.

eventValueThreshold -> (double)

The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.

weight -> (double)

The weight of the event type. A higher weight means higher importance of the event type for the created solution.

optimizationObjective -> (structure)

Describes the additional objective for the solution, such as maximizing streaming minutes or increasing revenue. For more information see [Optimizing a solution](https://docs.aws.amazon.com/personalize/latest/dg/optimizing-solution-for-objective.html) .

itemAttribute -> (string)

The numerical metadata column in an Items dataset related to the optimization objective. For example, VIDEO_LENGTH (to maximize streaming minutes), or PRICE (to maximize revenue).

objectiveSensitivity -> (string)

Specifies how Amazon Personalize balances the importance of your optimization objective versus relevance.

trainingDataConfig -> (structure)

Specifies the training data configuration to use when creating a custom solution version (trained model).

excludedDatasetColumns -> (map)

Specifies the columns to exclude from training. Each key is a dataset type, and each value is a list of columns. Exclude columns to control what data Amazon Personalize uses to generate recommendations.

For example, you might have a column that you want to use only to filter recommendations. You can exclude this column from training and Amazon Personalize considers it only when filtering.

key -> (string)

value -> (list)

(string)

autoTrainingConfig -> (structure)

Specifies the automatic training configuration to use.

schedulingExpression -> (string)

Specifies how often to automatically train new solution versions. Specify a rate expression in rate(*value* *unit* ) format. For value, specify a number between 1 and 30. For unit, specify `day` or `days` . For example, to automatically create a new solution version every 5 days, specify `rate(5 days)` . The default is every 7 days.

For more information about auto training, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html) .

trainingHours -> (double)

The time used to train the model. You are billed for the time it takes to train a model. This field is visible only after Amazon Personalize successfully trains a model.

trainingMode -> (string)

The scope of training to be performed when creating the solution version. A `FULL` training considers all of the data in your dataset group. An `UPDATE` processes only the data that has changed since the latest training. Only solution versions created with the User-Personalization recipe can use `UPDATE` .

tunedHPOParams -> (structure)

If hyperparameter optimization was performed, contains the hyperparameter values of the best performing model.

algorithmHyperParameters -> (map)

A list of the hyperparameter values of the best performing model.

key -> (string)

value -> (string)

status -> (string)

The status of the solution version.

A solution version can be in one of the following states:

- CREATE PENDING
- CREATE IN_PROGRESS
- ACTIVE
- CREATE FAILED
- CREATE STOPPING
- CREATE STOPPED

failureReason -> (string)

If training a solution version fails, the reason for the failure.

creationDateTime -> (timestamp)

The date and time (in Unix time) that this version of the solution was created.

lastUpdatedDateTime -> (timestamp)

The date and time (in Unix time) that the solution was last updated.

trainingType -> (string)

Whether the solution version was created automatically or manually.