# create-evaluation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-evaluation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/create-evaluation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# create-evaluation-job

## Description

Creates an evaluation job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/CreateEvaluationJob)

`create-evaluation-job` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
create-evaluation-job
--job-name <value>
[--job-description <value>]
[--client-request-token <value>]
--role-arn <value>
[--customer-encryption-key-id <value>]
[--job-tags <value>]
[--application-type <value>]
--evaluation-config <value>
--inference-config <value>
--output-data-config <value>
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

`--job-name` (string)

A name for the evaluation job. Names must unique with your Amazon Web Services account, and your accountâs Amazon Web Services region.

`--job-description` (string)

A description of the evaluation job.

`--client-request-token` (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see [Required permissions for model evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html) .

`--customer-encryption-key-id` (string)

Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.

`--job-tags` (list)

Tags to attach to the model evaluation job.

(structure)

Definition of the key/value pair for a tag.

key -> (string)

Key for the tag.

value -> (string)

Value for the tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--application-type` (string)

Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).

Possible values:

- `ModelEvaluation`
- `RagEvaluation`

`--evaluation-config` (tagged union structure)

Contains the configuration details of either an automated or human-based evaluation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `automated`, `human`.

automated -> (structure)

Contains the configuration details of an automated evaluation job that computes metrics.

datasetMetricConfigs -> (list)

Configuration details of the prompt datasets and metrics you want to use for your evaluation job.

(structure)

Defines the prompt datasets, built-in metric names and custom metric names, and the task type.

taskType -> (string)

The the type of task you want to evaluate for your evaluation job. This applies only to model evaluation jobs and is ignored for knowledge base evaluation jobs.

dataset -> (structure)

Specifies the prompt dataset.

name -> (string)

Used to specify supported built-in prompt datasets. Valid values are `Builtin.Bold` , `Builtin.BoolQ` , `Builtin.NaturalQuestions` , `Builtin.Gigaword` , `Builtin.RealToxicityPrompts` , `Builtin.TriviaQA` , `Builtin.T-Rex` , `Builtin.WomensEcommerceClothingReviews` and `Builtin.Wikitext2` .

datasetLocation -> (tagged union structure)

For custom prompt datasets, you must specify the location in Amazon S3 where the prompt dataset is saved.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3Uri`.

s3Uri -> (string)

The S3 URI of the S3 bucket specified in the job.

metricNames -> (list)

The names of the metrics you want to use for your evaluation job.

For knowledge base evaluation jobs that evaluate retrieval only, valid values are â`Builtin.ContextRelevance` â, â`Builtin.ContextCoverage` â.

For knowledge base evaluation jobs that evaluate retrieval with response generation, valid values are â`Builtin.Correctness` â, â`Builtin.Completeness` â, â`Builtin.Helpfulness` â, â`Builtin.LogicalCoherence` â, â`Builtin.Faithfulness` â, â`Builtin.Harmfulness` â, â`Builtin.Stereotyping` â, â`Builtin.Refusal` â.

For automated model evaluation jobs, valid values are â`Builtin.Accuracy` â, â`Builtin.Robustness` â, and â`Builtin.Toxicity` â. In model evaluation jobs that use a LLM as judge you can specify â`Builtin.Correctness` â, â`Builtin.Completeness"` , â`Builtin.Faithfulness"` , â`Builtin.Helpfulness` â, â`Builtin.Coherence` â, â`Builtin.Relevance` â, â`Builtin.FollowingInstructions` â, â`Builtin.ProfessionalStyleAndTone` â, You can also specify the following responsible AI related metrics only for model evaluation job that use a LLM as judge â`Builtin.Harmfulness` â, â`Builtin.Stereotyping` â, and â`Builtin.Refusal` â.

For human-based model evaluation jobs, the list of strings must match the `name` parameter specified in `HumanEvaluationCustomMetric` .

(string)

evaluatorModelConfig -> (tagged union structure)

Contains the evaluator model configuration details. `EvaluatorModelConfig` is required for evaluation jobs that use a knowledge base or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockEvaluatorModels`.

bedrockEvaluatorModels -> (list)

The evaluator model used in knowledge base evaluation job or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.

(structure)

The evaluator model used in knowledge base evaluation job or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.

modelIdentifier -> (string)

The Amazon Resource Name (ARN) of the evaluator model used used in knowledge base evaluation job or in model evaluation job that use a model as judge.

customMetricConfig -> (structure)

Defines the configuration of custom metrics to be used in an evaluation job.

customMetrics -> (list)

Defines a list of custom metrics to be used in an Amazon Bedrock evaluation job.

(tagged union structure)

An array item definining a single custom metric for use in an Amazon Bedrock evaluation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `customMetricDefinition`.

customMetricDefinition -> (structure)

The definition of a custom metric for use in an Amazon Bedrock evaluation job.

name -> (string)

The name for a custom metric. Names must be unique in your Amazon Web Services region.

instructions -> (string)

The prompt for a custom metric that instructs the evaluator model how to rate the model or RAG source under evaluation.

ratingScale -> (list)

Defines the rating scale to be used for a custom metric. We recommend that you always define a ratings scale when creating a custom metric. If you donât define a scale, Amazon Bedrock wonât be able to visually display the results of the evaluation in the console or calculate average values of numerical scores. For more information on specifying a rating scale, see [Specifying an output schema (rating scale)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html#model-evaluation-custom-metrics-prompt-formats-schema) .

(structure)

Defines the value and corresponding definition for one rating in a custom metric rating scale.

definition -> (string)

Defines the definition for one rating in a custom metric rating scale.

value -> (tagged union structure)

Defines the value for one rating in a custom metric rating scale.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `floatValue`.

stringValue -> (string)

A string representing the value for a rating in a custom metric rating scale.

floatValue -> (float)

A floating point number representing the value for a rating in a custom metric rating scale.

evaluatorModelConfig -> (structure)

Configuration of the evaluator model you want to use to evaluate custom metrics in an Amazon Bedrock evaluation job.

bedrockEvaluatorModels -> (list)

Defines the model you want to evaluate custom metrics in an Amazon Bedrock evaluation job.

(structure)

Defines the model you want to evaluate custom metrics in an Amazon Bedrock evaluation job.

modelIdentifier -> (string)

The Amazon Resource Name (ARN) of the evaluator model for custom metrics. For a list of supported evaluator models, see [Evaluate model performance using another LLM as a judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) and [Evaluate the performance of RAG sources using Amazon Bedrock evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html) .

human -> (structure)

Contains the configuration details of an evaluation job that uses human workers.

humanWorkflowConfig -> (structure)

The parameters of the human workflow.

flowDefinitionArn -> (string)

The Amazon Resource Number (ARN) for the flow definition

instructions -> (string)

Instructions for the flow definition

customMetrics -> (list)

A `HumanEvaluationCustomMetric` object. It contains the names the metrics, how the metrics are to be evaluated, an optional description.

(structure)

In a model evaluation job that uses human workers you must define the name of the metric, and how you want that metric rated `ratingMethod` , and an optional description of the metric.

name -> (string)

The name of the metric. Your human evaluators will see this name in the evaluation UI.

description -> (string)

An optional description of the metric. Use this parameter to provide more details about the metric.

ratingMethod -> (string)

Choose how you want your human workers to evaluation your model. Valid values for rating methods are `ThumbsUpDown` , `IndividualLikertScale` ,``ComparisonLikertScale`` , `ComparisonChoice` , and `ComparisonRank`

datasetMetricConfigs -> (list)

Use to specify the metrics, task, and prompt dataset to be used in your model evaluation job.

(structure)

Defines the prompt datasets, built-in metric names and custom metric names, and the task type.

taskType -> (string)

The the type of task you want to evaluate for your evaluation job. This applies only to model evaluation jobs and is ignored for knowledge base evaluation jobs.

dataset -> (structure)

Specifies the prompt dataset.

name -> (string)

Used to specify supported built-in prompt datasets. Valid values are `Builtin.Bold` , `Builtin.BoolQ` , `Builtin.NaturalQuestions` , `Builtin.Gigaword` , `Builtin.RealToxicityPrompts` , `Builtin.TriviaQA` , `Builtin.T-Rex` , `Builtin.WomensEcommerceClothingReviews` and `Builtin.Wikitext2` .

datasetLocation -> (tagged union structure)

For custom prompt datasets, you must specify the location in Amazon S3 where the prompt dataset is saved.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3Uri`.

s3Uri -> (string)

The S3 URI of the S3 bucket specified in the job.

metricNames -> (list)

The names of the metrics you want to use for your evaluation job.

For knowledge base evaluation jobs that evaluate retrieval only, valid values are â`Builtin.ContextRelevance` â, â`Builtin.ContextCoverage` â.

For knowledge base evaluation jobs that evaluate retrieval with response generation, valid values are â`Builtin.Correctness` â, â`Builtin.Completeness` â, â`Builtin.Helpfulness` â, â`Builtin.LogicalCoherence` â, â`Builtin.Faithfulness` â, â`Builtin.Harmfulness` â, â`Builtin.Stereotyping` â, â`Builtin.Refusal` â.

For automated model evaluation jobs, valid values are â`Builtin.Accuracy` â, â`Builtin.Robustness` â, and â`Builtin.Toxicity` â. In model evaluation jobs that use a LLM as judge you can specify â`Builtin.Correctness` â, â`Builtin.Completeness"` , â`Builtin.Faithfulness"` , â`Builtin.Helpfulness` â, â`Builtin.Coherence` â, â`Builtin.Relevance` â, â`Builtin.FollowingInstructions` â, â`Builtin.ProfessionalStyleAndTone` â, You can also specify the following responsible AI related metrics only for model evaluation job that use a LLM as judge â`Builtin.Harmfulness` â, â`Builtin.Stereotyping` â, and â`Builtin.Refusal` â.

For human-based model evaluation jobs, the list of strings must match the `name` parameter specified in `HumanEvaluationCustomMetric` .

(string)

JSON Syntax:

```
{
  "automated": {
    "datasetMetricConfigs": [
      {
        "taskType": "Summarization"|"Classification"|"QuestionAndAnswer"|"Generation"|"Custom",
        "dataset": {
          "name": "string",
          "datasetLocation": {
            "s3Uri": "string"
          }
        },
        "metricNames": ["string", ...]
      }
      ...
    ],
    "evaluatorModelConfig": {
      "bedrockEvaluatorModels": [
        {
          "modelIdentifier": "string"
        }
        ...
      ]
    },
    "customMetricConfig": {
      "customMetrics": [
        {
          "customMetricDefinition": {
            "name": "string",
            "instructions": "string",
            "ratingScale": [
              {
                "definition": "string",
                "value": {
                  "stringValue": "string",
                  "floatValue": float
                }
              }
              ...
            ]
          }
        }
        ...
      ],
      "evaluatorModelConfig": {
        "bedrockEvaluatorModels": [
          {
            "modelIdentifier": "string"
          }
          ...
        ]
      }
    }
  },
  "human": {
    "humanWorkflowConfig": {
      "flowDefinitionArn": "string",
      "instructions": "string"
    },
    "customMetrics": [
      {
        "name": "string",
        "description": "string",
        "ratingMethod": "string"
      }
      ...
    ],
    "datasetMetricConfigs": [
      {
        "taskType": "Summarization"|"Classification"|"QuestionAndAnswer"|"Generation"|"Custom",
        "dataset": {
          "name": "string",
          "datasetLocation": {
            "s3Uri": "string"
          }
        },
        "metricNames": ["string", ...]
      }
      ...
    ]
  }
}
```

`--inference-config` (tagged union structure)

Contains the configuration details of the inference model for the evaluation job.

For model evaluation jobs, automated jobs support a single model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) , and jobs that use human workers support two models or inference profiles.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `models`, `ragConfigs`.

models -> (list)

Specifies the inference models.

(tagged union structure)

Defines the models used in the model evaluation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockModel`, `precomputedInferenceSource`.

bedrockModel -> (structure)

Defines the Amazon Bedrock model or inference profile and inference parameters you want used.

modelIdentifier -> (string)

The ARN of the Amazon Bedrock model or inference profile specified.

inferenceParams -> (string)

Each Amazon Bedrock support different inference parameters that change how the model behaves during inference.

performanceConfig -> (structure)

Specifies performance settings for the model or inference profile.

latency -> (string)

Specifies whether to use the latency-optimized or standard version of a model or inference profile.

precomputedInferenceSource -> (structure)

Defines the model used to generate inference response data for a model evaluation job where you provide your own inference response data.

inferenceSourceIdentifier -> (string)

A label that identifies a model used in a model evaluation job where you provide your own inference response data.

ragConfigs -> (list)

Contains the configuration details of the inference for a knowledge base evaluation job, including either the retrieval only configuration or the retrieval with response generation configuration.

(tagged union structure)

Contains configuration details for retrieval of information and response generation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `knowledgeBaseConfig`, `precomputedRagSourceConfig`.

knowledgeBaseConfig -> (tagged union structure)

Contains configuration details for knowledge base retrieval and response generation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `retrieveConfig`, `retrieveAndGenerateConfig`.

retrieveConfig -> (structure)

Contains configuration details for retrieving information from a knowledge base.

knowledgeBaseId -> (string)

The unique identifier of the knowledge base.

knowledgeBaseRetrievalConfiguration -> (structure)

Contains configuration details for knowledge base retrieval.

vectorSearchConfiguration -> (structure)

Contains configuration details for returning the results from the vector search.

numberOfResults -> (integer)

The number of text chunks to retrieve; the number of results to return.

overrideSearchType -> (string)

By default, Amazon Bedrock decides a search strategy for you. If youâre using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a `HYBRID` search using both vector embeddings and raw text, or `SEMANTIC` search using only vector embeddings. For other vector store configurations, only `SEMANTIC` search is available.

filter -> (tagged union structure)

Specifies the filters to use on the metadata fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes/fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes/fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

retrieveAndGenerateConfig -> (structure)

Contains configuration details for retrieving information from a knowledge base and generating responses.

type -> (string)

The type of resource that contains your data for retrieving information and generating responses.

If you choose to use `EXTERNAL_SOURCES` , then currently only Claude 3 Sonnet models for knowledge bases are supported.

knowledgeBaseConfiguration -> (structure)

Contains configuration details for the knowledge base retrieval and response generation.

knowledgeBaseId -> (string)

The unique identifier of the knowledge base.

modelArn -> (string)

The Amazon Resource Name (ARN) of the foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) used to generate responses.

retrievalConfiguration -> (structure)

Contains configuration details for retrieving text chunks.

vectorSearchConfiguration -> (structure)

Contains configuration details for returning the results from the vector search.

numberOfResults -> (integer)

The number of text chunks to retrieve; the number of results to return.

overrideSearchType -> (string)

By default, Amazon Bedrock decides a search strategy for you. If youâre using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a `HYBRID` search using both vector embeddings and raw text, or `SEMANTIC` search using only vector embeddings. For other vector store configurations, only `SEMANTIC` search is available.

filter -> (tagged union structure)

Specifies the filters to use on the metadata fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes/fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

(tagged union structure)

Specifies the filters to use on the metadata attributes/fields in the knowledge base data sources before returning results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equals`, `notEquals`, `greaterThan`, `greaterThanOrEquals`, `lessThan`, `lessThanOrEquals`, `in`, `notIn`, `startsWith`, `listContains`, `stringContains`, `andAll`, `orAll`.

equals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value matches the value in this object.

The following example would return data sources with an animal attribute whose value is âcatâ: `"equals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notEquals -> (structure)

Knowledge base data sources that contain a metadata attribute whose name matches the key and whose value doesnât match the value in this object are returned.

The following example would return data sources that donât contain an animal attribute whose value is âcatâ: `"notEquals": { "key": "animal", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than the value in this object.

The following example would return data sources with an year attribute whose value is greater than â1989â: `"greaterThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

greaterThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is greater than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is greater than or equal to â1989â: `"greaterThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThan -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than the value in this object.

The following example would return data sources with an year attribute whose value is less than to â1989â: `"lessThan": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

lessThanOrEquals -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is less than or equal to the value in this object.

The following example would return data sources with an year attribute whose value is less than or equal to â1989â: `"lessThanOrEquals": { "key": "year", "value": 1989 }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

in -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is in the list specified in the value in this object.

The following example would return data sources with an animal attribute that is either âcatâ or âdogâ: `"in": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

notIn -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value isnât in the list specified in the value in this object.

The following example would return data sources whose animal attribute is neither âcatâ nor âdogâ: `"notIn": { "key": "animal", "value": ["cat", "dog"] }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

startsWith -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value starts with the value in this object. This filter is currently only supported for Amazon OpenSearch Serverless vector stores.

The following example would return data sources with an animal attribute starts with âcaâ (for example, âcatâ or âcamelâ). `"startsWith": { "key": "animal", "value": "ca" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

listContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is a list that contains the value as one of its members.

The following example would return data sources with an animals attribute that is a list containing a cat member (for example, `["dog", "cat"]` ): `"listContains": { "key": "animals", "value": "cat" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

stringContains -> (structure)

Knowledge base data sources are returned if they contain a metadata attribute whose name matches the key and whose value is one of the following:

A string that contains the value as a substring. The following example would return data sources with an animal attribute that contains the substring at (for example, âcatâ): `"stringContains": { "key": "animal", "value": "at" }`

A list with a member that contains the value as a substring. The following example would return data sources with an animals attribute that is a list containing a member that contains the substring at (for example, `["dog", "cat"]` ): `"stringContains": { "key": "animals", "value": "at" }`

key -> (string)

The name of metadata attribute/field, which must match the name in your data source/document metadata.

value -> (document)

The value of the metadata attribute/field.

andAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill all the filter conditions inside this list.

( â¦ recursive â¦ )

orAll -> (list)

Knowledge base data sources are returned if their metadata attributes fulfill at least one of the filter conditions inside this list.

( â¦ recursive â¦ )

generationConfiguration -> (structure)

Contains configurations details for response generation based on retrieved text chunks.

promptTemplate -> (structure)

Contains the template for the prompt thatâs sent to the model for response generation.

textPromptTemplate -> (string)

The template for the prompt thatâs sent to the model for response generation. You can include prompt placeholders, which become replaced before the prompt is sent to the model to provide instructions and context to the model. In addition, you can include XML tags to delineate meaningful sections of the prompt template.

For more information, see [Knowledge base prompt template](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) and [Use XML tags with Anthropic Claude models](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) .

guardrailConfiguration -> (structure)

Contains configuration details for the guardrail.

guardrailId -> (string)

The unique identifier for the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

kbInferenceConfig -> (structure)

Contains configuration details for inference for knowledge base retrieval and response generation.

textInferenceConfig -> (structure)

Contains configuration details for text generation using a language model via the `RetrieveAndGenerate` function.

temperature -> (float)

Controls the random-ness of text generated by the language model, influencing how much the model sticks to the most predictable next words versus exploring more surprising options. A lower temperature value (e.g. 0.2 or 0.3) makes model outputs more deterministic or predictable, while a higher temperature (e.g. 0.8 or 0.9) makes the outputs more creative or unpredictable.

topP -> (float)

A probability distribution threshold which controls what the model considers for the set of possible next tokens. The model will only consider the top p% of the probability distribution when generating the next token.

maxTokens -> (integer)

The maximum number of tokens to generate in the output text. Do not use the minimum of 0 or the maximum of 65536. The limit values described here are arbitrary values, for actual values consult the limits defined by your specific model.

stopSequences -> (list)

A list of sequences of characters that, if generated, will cause the model to stop generating further tokens. Do not use a minimum length of 1 or a maximum length of 1000. The limit values described here are arbitrary values, for actual values consult the limits defined by your specific model.

(string)

additionalModelRequestFields -> (map)

Additional model parameters and corresponding values not included in the `textInferenceConfig` structure for a knowledge base. This allows you to provide custom model parameters specific to the language model being used.

key -> (string)

value -> (document)

orchestrationConfiguration -> (structure)

Contains configuration details for the model to process the prompt prior to retrieval and response generation.

queryTransformationConfiguration -> (structure)

Contains configuration details for transforming the prompt.

type -> (string)

The type of transformation to apply to the prompt.

externalSourcesConfiguration -> (structure)

The configuration for the external source wrapper object in the `retrieveAndGenerate` function.

modelArn -> (string)

The Amazon Resource Name (ARN) of the foundation model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) used to generate responses.

sources -> (list)

The document for the external source wrapper object in the `retrieveAndGenerate` function.

(structure)

The unique external source of the content contained in the wrapper object.

sourceType -> (string)

The source type of the external source wrapper object.

s3Location -> (structure)

The S3 location of the external source wrapper object.

uri -> (string)

The S3 URI location for the wrapper object of the document.

byteContent -> (structure)

The identifier, content type, and data of the external source wrapper object.

identifier -> (string)

The file name of the document contained in the wrapper object.

contentType -> (string)

The MIME type of the document contained in the wrapper object.

data -> (blob)

The byte value of the file to upload, encoded as a Base-64 string.

generationConfiguration -> (structure)

Contains configurations details for response generation based on retrieved text chunks.

promptTemplate -> (structure)

Contains the template for the prompt for the external source wrapper object.

textPromptTemplate -> (string)

The template for the prompt thatâs sent to the model for response generation. You can include prompt placeholders, which become replaced before the prompt is sent to the model to provide instructions and context to the model. In addition, you can include XML tags to delineate meaningful sections of the prompt template.

For more information, see [Knowledge base prompt template](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html) and [Use XML tags with Anthropic Claude models](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) .

guardrailConfiguration -> (structure)

Configuration details for the guardrail.

guardrailId -> (string)

The unique identifier for the guardrail.

guardrailVersion -> (string)

The version of the guardrail.

kbInferenceConfig -> (structure)

Configuration details for inference when using `RetrieveAndGenerate` to generate responses while using an external source.

textInferenceConfig -> (structure)

Contains configuration details for text generation using a language model via the `RetrieveAndGenerate` function.

temperature -> (float)

Controls the random-ness of text generated by the language model, influencing how much the model sticks to the most predictable next words versus exploring more surprising options. A lower temperature value (e.g. 0.2 or 0.3) makes model outputs more deterministic or predictable, while a higher temperature (e.g. 0.8 or 0.9) makes the outputs more creative or unpredictable.

topP -> (float)

A probability distribution threshold which controls what the model considers for the set of possible next tokens. The model will only consider the top p% of the probability distribution when generating the next token.

maxTokens -> (integer)

The maximum number of tokens to generate in the output text. Do not use the minimum of 0 or the maximum of 65536. The limit values described here are arbitrary values, for actual values consult the limits defined by your specific model.

stopSequences -> (list)

A list of sequences of characters that, if generated, will cause the model to stop generating further tokens. Do not use a minimum length of 1 or a maximum length of 1000. The limit values described here are arbitrary values, for actual values consult the limits defined by your specific model.

(string)

additionalModelRequestFields -> (map)

Additional model parameters and their corresponding values not included in the text inference configuration for an external source. Takes in custom model parameters specific to the language model being used.

key -> (string)

value -> (document)

precomputedRagSourceConfig -> (tagged union structure)

Contains configuration details about the RAG source used to generate inference response data for a Knowledge Base evaluation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `retrieveSourceConfig`, `retrieveAndGenerateSourceConfig`.

retrieveSourceConfig -> (structure)

A summary of a RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.

ragSourceIdentifier -> (string)

A label that identifies the RAG source used for a retrieve-only Knowledge Base evaluation job where you provide your own inference response data.

retrieveAndGenerateSourceConfig -> (structure)

A summary of a RAG source used for a retrieve-and-generate Knowledge Base evaluation job where you provide your own inference response data.

ragSourceIdentifier -> (string)

A label that identifies the RAG source used for a retrieve-and-generate Knowledge Base evaluation job where you provide your own inference response data.

JSON Syntax:

```
{
  "models": [
    {
      "bedrockModel": {
        "modelIdentifier": "string",
        "inferenceParams": "string",
        "performanceConfig": {
          "latency": "standard"|"optimized"
        }
      },
      "precomputedInferenceSource": {
        "inferenceSourceIdentifier": "string"
      }
    }
    ...
  ],
  "ragConfigs": [
    {
      "knowledgeBaseConfig": {
        "retrieveConfig": {
          "knowledgeBaseId": "string",
          "knowledgeBaseRetrievalConfiguration": {
            "vectorSearchConfiguration": {
              "numberOfResults": integer,
              "overrideSearchType": "HYBRID"|"SEMANTIC",
              "filter": {
                "equals": {
                  "key": "string",
                  "value": {...}
                },
                "notEquals": {
                  "key": "string",
                  "value": {...}
                },
                "greaterThan": {
                  "key": "string",
                  "value": {...}
                },
                "greaterThanOrEquals": {
                  "key": "string",
                  "value": {...}
                },
                "lessThan": {
                  "key": "string",
                  "value": {...}
                },
                "lessThanOrEquals": {
                  "key": "string",
                  "value": {...}
                },
                "in": {
                  "key": "string",
                  "value": {...}
                },
                "notIn": {
                  "key": "string",
                  "value": {...}
                },
                "startsWith": {
                  "key": "string",
                  "value": {...}
                },
                "listContains": {
                  "key": "string",
                  "value": {...}
                },
                "stringContains": {
                  "key": "string",
                  "value": {...}
                },
                "andAll": [
                  {
                    "equals": {
                      "key": "string",
                      "value": {...}
                    },
                    "notEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "greaterThan": {
                      "key": "string",
                      "value": {...}
                    },
                    "greaterThanOrEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "lessThan": {
                      "key": "string",
                      "value": {...}
                    },
                    "lessThanOrEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "in": {
                      "key": "string",
                      "value": {...}
                    },
                    "notIn": {
                      "key": "string",
                      "value": {...}
                    },
                    "startsWith": {
                      "key": "string",
                      "value": {...}
                    },
                    "listContains": {
                      "key": "string",
                      "value": {...}
                    },
                    "stringContains": {
                      "key": "string",
                      "value": {...}
                    },
                    "andAll": [
                      { ... recursive ... }
                      ...
                    ],
                    "orAll": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ],
                "orAll": [
                  {
                    "equals": {
                      "key": "string",
                      "value": {...}
                    },
                    "notEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "greaterThan": {
                      "key": "string",
                      "value": {...}
                    },
                    "greaterThanOrEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "lessThan": {
                      "key": "string",
                      "value": {...}
                    },
                    "lessThanOrEquals": {
                      "key": "string",
                      "value": {...}
                    },
                    "in": {
                      "key": "string",
                      "value": {...}
                    },
                    "notIn": {
                      "key": "string",
                      "value": {...}
                    },
                    "startsWith": {
                      "key": "string",
                      "value": {...}
                    },
                    "listContains": {
                      "key": "string",
                      "value": {...}
                    },
                    "stringContains": {
                      "key": "string",
                      "value": {...}
                    },
                    "andAll": [
                      { ... recursive ... }
                      ...
                    ],
                    "orAll": [
                      { ... recursive ... }
                      ...
                    ]
                  }
                  ...
                ]
              }
            }
          }
        },
        "retrieveAndGenerateConfig": {
          "type": "KNOWLEDGE_BASE"|"EXTERNAL_SOURCES",
          "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "string",
            "modelArn": "string",
            "retrievalConfiguration": {
              "vectorSearchConfiguration": {
                "numberOfResults": integer,
                "overrideSearchType": "HYBRID"|"SEMANTIC",
                "filter": {
                  "equals": {
                    "key": "string",
                    "value": {...}
                  },
                  "notEquals": {
                    "key": "string",
                    "value": {...}
                  },
                  "greaterThan": {
                    "key": "string",
                    "value": {...}
                  },
                  "greaterThanOrEquals": {
                    "key": "string",
                    "value": {...}
                  },
                  "lessThan": {
                    "key": "string",
                    "value": {...}
                  },
                  "lessThanOrEquals": {
                    "key": "string",
                    "value": {...}
                  },
                  "in": {
                    "key": "string",
                    "value": {...}
                  },
                  "notIn": {
                    "key": "string",
                    "value": {...}
                  },
                  "startsWith": {
                    "key": "string",
                    "value": {...}
                  },
                  "listContains": {
                    "key": "string",
                    "value": {...}
                  },
                  "stringContains": {
                    "key": "string",
                    "value": {...}
                  },
                  "andAll": [
                    {
                      "equals": {
                        "key": "string",
                        "value": {...}
                      },
                      "notEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "greaterThan": {
                        "key": "string",
                        "value": {...}
                      },
                      "greaterThanOrEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "lessThan": {
                        "key": "string",
                        "value": {...}
                      },
                      "lessThanOrEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "in": {
                        "key": "string",
                        "value": {...}
                      },
                      "notIn": {
                        "key": "string",
                        "value": {...}
                      },
                      "startsWith": {
                        "key": "string",
                        "value": {...}
                      },
                      "listContains": {
                        "key": "string",
                        "value": {...}
                      },
                      "stringContains": {
                        "key": "string",
                        "value": {...}
                      },
                      "andAll": [
                        { ... recursive ... }
                        ...
                      ],
                      "orAll": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ],
                  "orAll": [
                    {
                      "equals": {
                        "key": "string",
                        "value": {...}
                      },
                      "notEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "greaterThan": {
                        "key": "string",
                        "value": {...}
                      },
                      "greaterThanOrEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "lessThan": {
                        "key": "string",
                        "value": {...}
                      },
                      "lessThanOrEquals": {
                        "key": "string",
                        "value": {...}
                      },
                      "in": {
                        "key": "string",
                        "value": {...}
                      },
                      "notIn": {
                        "key": "string",
                        "value": {...}
                      },
                      "startsWith": {
                        "key": "string",
                        "value": {...}
                      },
                      "listContains": {
                        "key": "string",
                        "value": {...}
                      },
                      "stringContains": {
                        "key": "string",
                        "value": {...}
                      },
                      "andAll": [
                        { ... recursive ... }
                        ...
                      ],
                      "orAll": [
                        { ... recursive ... }
                        ...
                      ]
                    }
                    ...
                  ]
                }
              }
            },
            "generationConfiguration": {
              "promptTemplate": {
                "textPromptTemplate": "string"
              },
              "guardrailConfiguration": {
                "guardrailId": "string",
                "guardrailVersion": "string"
              },
              "kbInferenceConfig": {
                "textInferenceConfig": {
                  "temperature": float,
                  "topP": float,
                  "maxTokens": integer,
                  "stopSequences": ["string", ...]
                }
              },
              "additionalModelRequestFields": {"string": {...}
                ...}
            },
            "orchestrationConfiguration": {
              "queryTransformationConfiguration": {
                "type": "QUERY_DECOMPOSITION"
              }
            }
          },
          "externalSourcesConfiguration": {
            "modelArn": "string",
            "sources": [
              {
                "sourceType": "S3"|"BYTE_CONTENT",
                "s3Location": {
                  "uri": "string"
                },
                "byteContent": {
                  "identifier": "string",
                  "contentType": "string",
                  "data": blob
                }
              }
              ...
            ],
            "generationConfiguration": {
              "promptTemplate": {
                "textPromptTemplate": "string"
              },
              "guardrailConfiguration": {
                "guardrailId": "string",
                "guardrailVersion": "string"
              },
              "kbInferenceConfig": {
                "textInferenceConfig": {
                  "temperature": float,
                  "topP": float,
                  "maxTokens": integer,
                  "stopSequences": ["string", ...]
                }
              },
              "additionalModelRequestFields": {"string": {...}
                ...}
            }
          }
        }
      },
      "precomputedRagSourceConfig": {
        "retrieveSourceConfig": {
          "ragSourceIdentifier": "string"
        },
        "retrieveAndGenerateSourceConfig": {
          "ragSourceIdentifier": "string"
        }
      }
    }
    ...
  ]
}
```

`--output-data-config` (structure)

Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.

s3Uri -> (string)

The Amazon S3 URI where the results of the evaluation job are saved.

Shorthand Syntax:

```
s3Uri=string
```

JSON Syntax:

```
{
  "s3Uri": "string"
}
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

jobArn -> (string)

The Amazon Resource Name (ARN) of the evaluation job.