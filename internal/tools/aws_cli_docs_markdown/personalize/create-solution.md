# create-solutionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-solution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# create-solution

## Description

### Warning

By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html) to turn off automatic training. For information about training costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/) .

Creates the configuration for training a model (creating a solution version). This configuration includes the recipe to use for model training and optional training configuration, such as columns to use in training and feature transformation parameters. For more information about configuring a solution, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html) .

By default, new solutions use automatic training to create solution versions every 7 days. You can change the training frequency. Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information, see [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html) .

To turn off automatic training, set `performAutoTraining` to false. If you turn off automatic training, you must manually create a solution version by calling the [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html) operation.

After training starts, you can get the solution versionâs Amazon Resource Name (ARN) with the [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) API operation. To get its status, use the [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html) .

After training completes you can evaluate model accuracy by calling [GetSolutionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_GetSolutionMetrics.html) . When you are satisfied with the solution version, you deploy it using [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html) . The campaign provides recommendations to a client through the [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html) API.

### Note

Amazon Personalize doesnât support configuring the `hpoObjective` for solution hyperparameter optimization at this time.

**Status**

A solution can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

To get the status of the solution, call [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html) . If you use manual training, the status must be ACTIVE before you call `CreateSolutionVersion` .

**Related APIs**

- [UpdateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html)
- [ListSolutions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html)
- [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html)
- [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html)
- [DeleteSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html)
- [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html)
- [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/CreateSolution)

## Synopsis

```
create-solution
--name <value>
[--perform-hpo | --no-perform-hpo]
[--perform-auto-ml | --no-perform-auto-ml]
[--perform-auto-training | --no-perform-auto-training]
[--recipe-arn <value>]
--dataset-group-arn <value>
[--event-type <value>]
[--solution-config <value>]
[--tags <value>]
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

`--name` (string)

The name for the solution.

`--perform-hpo` | `--no-perform-hpo` (boolean)

Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is `false` .

When performing AutoML, this parameter is always `true` and you should not set it to `false` .

`--perform-auto-ml` | `--no-perform-auto-ml` (boolean)

### Warning

We donât recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see [Choosing a recipe](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) .

Whether to perform automated machine learning (AutoML). The default is `false` . For this case, you must specify `recipeArn` .

When set to `true` , Amazon Personalize analyzes your training data and selects the optimal USER_PERSONALIZATION recipe and hyperparameters. In this case, you must omit `recipeArn` . Amazon Personalize determines the optimal recipe by running tests with different values for the hyperparameters. AutoML lengthens the training process as compared to selecting a specific recipe.

`--perform-auto-training` | `--no-perform-auto-training` (boolean)

Whether the solution uses automatic training to create new solution versions (trained models). The default is `True` and the solution automatically creates new solution versions every 7 days. You can change the training frequency by specifying a `schedulingExpression` in the `AutoTrainingConfig` as part of solution configuration. For more information about automatic training, see [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html) .

Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training.

After training starts, you can get the solution versionâs Amazon Resource Name (ARN) with the [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) API operation. To get its status, use the [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html) .

`--recipe-arn` (string)

The Amazon Resource Name (ARN) of the recipe to use for model training. This is required when `performAutoML` is false. For information about different Amazon Personalize recipes and their ARNs, see [Choosing a recipe](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) .

`--dataset-group-arn` (string)

The Amazon Resource Name (ARN) of the dataset group that provides the training data.

`--event-type` (string)

When your have multiple event types (using an `EVENT_TYPE` schema field), this parameter specifies which event type (for example, âclickâ or âlikeâ) is used for training the model.

If you do not provide an `eventType` , Amazon Personalize will use all interactions for training with equal weight regardless of type.

`--solution-config` (structure)

The configuration properties for the solution. When `performAutoML` is set to true, Amazon Personalize only evaluates the `autoMLConfig` section of the solution configuration.

### Note

Amazon Personalize doesnât support configuring the `hpoObjective` at this time.

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

JSON Syntax:

```
{
  "eventValueThreshold": "string",
  "hpoConfig": {
    "hpoObjective": {
      "type": "string",
      "metricName": "string",
      "metricRegex": "string"
    },
    "hpoResourceConfig": {
      "maxNumberOfTrainingJobs": "string",
      "maxParallelTrainingJobs": "string"
    },
    "algorithmHyperParameterRanges": {
      "integerHyperParameterRanges": [
        {
          "name": "string",
          "minValue": integer,
          "maxValue": integer
        }
        ...
      ],
      "continuousHyperParameterRanges": [
        {
          "name": "string",
          "minValue": double,
          "maxValue": double
        }
        ...
      ],
      "categoricalHyperParameterRanges": [
        {
          "name": "string",
          "values": ["string", ...]
        }
        ...
      ]
    }
  },
  "algorithmHyperParameters": {"string": "string"
    ...},
  "featureTransformationParameters": {"string": "string"
    ...},
  "autoMLConfig": {
    "metricName": "string",
    "recipeList": ["string", ...]
  },
  "eventsConfig": {
    "eventParametersList": [
      {
        "eventType": "string",
        "eventValueThreshold": double,
        "weight": double
      }
      ...
    ]
  },
  "optimizationObjective": {
    "itemAttribute": "string",
    "objectiveSensitivity": "LOW"|"MEDIUM"|"HIGH"|"OFF"
  },
  "trainingDataConfig": {
    "excludedDatasetColumns": {"string": ["string", ...]
      ...}
  },
  "autoTrainingConfig": {
    "schedulingExpression": "string"
  }
}
```

`--tags` (list)

A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the solution.

(structure)

The optional metadata that you apply to resources to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information see [Tagging Amazon Personalize resources](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) .

tagKey -> (string)

One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.

tagValue -> (string)

The optional part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
tagKey=string,tagValue=string ...
```

JSON Syntax:

```
[
  {
    "tagKey": "string",
    "tagValue": "string"
  }
  ...
]
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

solutionArn -> (string)

The ARN of the solution.