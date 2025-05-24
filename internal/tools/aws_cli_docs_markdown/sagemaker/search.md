# searchÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/search.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/search.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# search

## Description

Finds SageMaker resources that match a search query. Matching resources are returned as a list of `SearchRecord` objects in the response. You can sort the search results by any resource property in a ascending or descending order.

You can query against the following value types: numeric, text, Boolean, and timestamp.

### Note

The Search API may provide access to otherwise restricted data. See [Amazon SageMaker API Permissions: Actions, Permissions, and Resources Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html) for more information.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/Search)

`search` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Results`

## Synopsis

```
search
--resource <value>
[--search-expression <value>]
[--sort-by <value>]
[--sort-order <value>]
[--cross-account-filter-option <value>]
[--visibility-conditions <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--resource` (string)

The name of the SageMaker resource to search for.

Possible values:

- `TrainingJob`
- `Experiment`
- `ExperimentTrial`
- `ExperimentTrialComponent`
- `Endpoint`
- `Model`
- `ModelPackage`
- `ModelPackageGroup`
- `Pipeline`
- `PipelineExecution`
- `FeatureGroup`
- `FeatureMetadata`
- `Image`
- `ImageVersion`
- `Project`
- `HyperParameterTuningJob`
- `ModelCard`

`--search-expression` (structure)

A Boolean conditional statement. Resources must satisfy this condition to be included in search results. You must provide at least one subexpression, filter, or nested filter. The maximum number of recursive `SubExpressions` , `NestedFilters` , and `Filters` that can be included in a `SearchExpression` object is 50.

Filters -> (list)

A list of filter objects.

(structure)

A conditional statement for a search expression that includes a resource property, a Boolean operator, and a value. Resources that match the statement are returned in the results from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

If you specify a `Value` , but not an `Operator` , SageMaker uses the equals operator.

In search, there are several property types:

Metrics

To define a metric filter, enter a value using the form `"Metrics.<name>"` , where `<name>` is a metric name. For example, the following filter searches for training jobs with an `"accuracy"` metric greater than `"0.9"` :

`{`

`"Name": "Metrics.accuracy",`

`"Operator": "GreaterThan",`

`"Value": "0.9"`

`}`

HyperParameters

To define a hyperparameter filter, enter a value with the form `"HyperParameters.<name>"` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified `Value` is also a decimal value. If the specified `Value` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a `"learning_rate"` hyperparameter that is less than `"0.5"` :

`{`

`"Name": "HyperParameters.learning_rate",`

`"Operator": "LessThan",`

`"Value": "0.5"`

`}`

Tags

To define a tag filter, enter a value with the form `Tags.<key>` .

Name -> (string)

A resource property name. For example, `TrainingJobName` . For valid property names, see [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html) . You must specify a valid property for the resource.

Operator -> (string)

A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:

Equals

The value of `Name` equals `Value` .

NotEquals

The value of `Name` doesnât equal `Value` .

Exists

The `Name` property exists.

NotExists

The `Name` property does not exist.

GreaterThan

The value of `Name` is greater than `Value` . Not supported for text properties.

GreaterThanOrEqualTo

The value of `Name` is greater than or equal to `Value` . Not supported for text properties.

LessThan

The value of `Name` is less than `Value` . Not supported for text properties.

LessThanOrEqualTo

The value of `Name` is less than or equal to `Value` . Not supported for text properties.

In

The value of `Name` is one of the comma delimited strings in `Value` . Only supported for text properties.

Contains

The value of `Name` contains the string `Value` . Only supported for text properties.

A `SearchExpression` can include the `Contains` operator multiple times when the value of `Name` is one of the following:

- `Experiment.DisplayName`
- `Experiment.ExperimentName`
- `Experiment.Tags`
- `Trial.DisplayName`
- `Trial.TrialName`
- `Trial.Tags`
- `TrialComponent.DisplayName`
- `TrialComponent.TrialComponentName`
- `TrialComponent.Tags`
- `TrialComponent.InputArtifacts`
- `TrialComponent.OutputArtifacts`

A `SearchExpression` can include only one `Contains` operator for all other values of `Name` . In these cases, if you include multiple `Contains` operators in the `SearchExpression` , the result is the following error message: â`'CONTAINS' operator usage limit of 1 exceeded.` â

Value -> (string)

A value used with `Name` and `Operator` to determine which resources satisfy the filterâs condition. For numerical properties, `Value` must be an integer or floating-point decimal. For timestamp properties, `Value` must be an ISO 8601 date-time string of the following format: `YYYY-mm-dd'T'HH:MM:SS` .

NestedFilters -> (list)

A list of nested filter objects.

(structure)

A list of nested [Filter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Filter.html) objects. A resource must satisfy the conditions of all filters to be included in the results returned from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

For example, to filter on a training jobâs `InputDataConfig` property with a specific channel name and `S3Uri` prefix, define the following filters:

- `'{Name:"InputDataConfig.ChannelName", "Operator":"Equals", "Value":"train"}',`
- `'{Name:"InputDataConfig.DataSource.S3DataSource.S3Uri", "Operator":"Contains", "Value":"mybucket/catdata"}'`

NestedPropertyName -> (string)

The name of the property to use in the nested filters. The value must match a listed property name, such as `InputDataConfig` .

Filters -> (list)

A list of filters. Each filter acts on a property. Filters must contain at least one `Filters` value. For example, a `NestedFilters` call might include a filter on the `PropertyName` parameter of the `InputDataConfig` property: `InputDataConfig.DataSource.S3DataSource.S3Uri` .

(structure)

A conditional statement for a search expression that includes a resource property, a Boolean operator, and a value. Resources that match the statement are returned in the results from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

If you specify a `Value` , but not an `Operator` , SageMaker uses the equals operator.

In search, there are several property types:

Metrics

To define a metric filter, enter a value using the form `"Metrics.<name>"` , where `<name>` is a metric name. For example, the following filter searches for training jobs with an `"accuracy"` metric greater than `"0.9"` :

`{`

`"Name": "Metrics.accuracy",`

`"Operator": "GreaterThan",`

`"Value": "0.9"`

`}`

HyperParameters

To define a hyperparameter filter, enter a value with the form `"HyperParameters.<name>"` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified `Value` is also a decimal value. If the specified `Value` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a `"learning_rate"` hyperparameter that is less than `"0.5"` :

`{`

`"Name": "HyperParameters.learning_rate",`

`"Operator": "LessThan",`

`"Value": "0.5"`

`}`

Tags

To define a tag filter, enter a value with the form `Tags.<key>` .

Name -> (string)

A resource property name. For example, `TrainingJobName` . For valid property names, see [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html) . You must specify a valid property for the resource.

Operator -> (string)

A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:

Equals

The value of `Name` equals `Value` .

NotEquals

The value of `Name` doesnât equal `Value` .

Exists

The `Name` property exists.

NotExists

The `Name` property does not exist.

GreaterThan

The value of `Name` is greater than `Value` . Not supported for text properties.

GreaterThanOrEqualTo

The value of `Name` is greater than or equal to `Value` . Not supported for text properties.

LessThan

The value of `Name` is less than `Value` . Not supported for text properties.

LessThanOrEqualTo

The value of `Name` is less than or equal to `Value` . Not supported for text properties.

In

The value of `Name` is one of the comma delimited strings in `Value` . Only supported for text properties.

Contains

The value of `Name` contains the string `Value` . Only supported for text properties.

A `SearchExpression` can include the `Contains` operator multiple times when the value of `Name` is one of the following:

- `Experiment.DisplayName`
- `Experiment.ExperimentName`
- `Experiment.Tags`
- `Trial.DisplayName`
- `Trial.TrialName`
- `Trial.Tags`
- `TrialComponent.DisplayName`
- `TrialComponent.TrialComponentName`
- `TrialComponent.Tags`
- `TrialComponent.InputArtifacts`
- `TrialComponent.OutputArtifacts`

A `SearchExpression` can include only one `Contains` operator for all other values of `Name` . In these cases, if you include multiple `Contains` operators in the `SearchExpression` , the result is the following error message: â`'CONTAINS' operator usage limit of 1 exceeded.` â

Value -> (string)

A value used with `Name` and `Operator` to determine which resources satisfy the filterâs condition. For numerical properties, `Value` must be an integer or floating-point decimal. For timestamp properties, `Value` must be an ISO 8601 date-time string of the following format: `YYYY-mm-dd'T'HH:MM:SS` .

SubExpressions -> (list)

A list of search expression objects.

(structure)

A multi-expression that searches for the specified resource or resources in a search. All resource objects that satisfy the expressionâs condition are included in the search results. You must specify at least one subexpression, filter, or nested filter. A `SearchExpression` can contain up to twenty elements.

A `SearchExpression` contains the following components:

- A list of `Filter` objects. Each filter defines a simple Boolean expression comprised of a resource property name, Boolean operator, and value.
- A list of `NestedFilter` objects. Each nested filter defines a list of Boolean expressions using a list of resource properties. A nested filter is satisfied if a single object in the list satisfies all Boolean expressions.
- A list of `SearchExpression` objects. A search expression object can be nested in a list of search expression objects.
- A Boolean operator: `And` or `Or` .

Filters -> (list)

A list of filter objects.

(structure)

A conditional statement for a search expression that includes a resource property, a Boolean operator, and a value. Resources that match the statement are returned in the results from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

If you specify a `Value` , but not an `Operator` , SageMaker uses the equals operator.

In search, there are several property types:

Metrics

To define a metric filter, enter a value using the form `"Metrics.<name>"` , where `<name>` is a metric name. For example, the following filter searches for training jobs with an `"accuracy"` metric greater than `"0.9"` :

`{`

`"Name": "Metrics.accuracy",`

`"Operator": "GreaterThan",`

`"Value": "0.9"`

`}`

HyperParameters

To define a hyperparameter filter, enter a value with the form `"HyperParameters.<name>"` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified `Value` is also a decimal value. If the specified `Value` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a `"learning_rate"` hyperparameter that is less than `"0.5"` :

`{`

`"Name": "HyperParameters.learning_rate",`

`"Operator": "LessThan",`

`"Value": "0.5"`

`}`

Tags

To define a tag filter, enter a value with the form `Tags.<key>` .

Name -> (string)

A resource property name. For example, `TrainingJobName` . For valid property names, see [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html) . You must specify a valid property for the resource.

Operator -> (string)

A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:

Equals

The value of `Name` equals `Value` .

NotEquals

The value of `Name` doesnât equal `Value` .

Exists

The `Name` property exists.

NotExists

The `Name` property does not exist.

GreaterThan

The value of `Name` is greater than `Value` . Not supported for text properties.

GreaterThanOrEqualTo

The value of `Name` is greater than or equal to `Value` . Not supported for text properties.

LessThan

The value of `Name` is less than `Value` . Not supported for text properties.

LessThanOrEqualTo

The value of `Name` is less than or equal to `Value` . Not supported for text properties.

In

The value of `Name` is one of the comma delimited strings in `Value` . Only supported for text properties.

Contains

The value of `Name` contains the string `Value` . Only supported for text properties.

A `SearchExpression` can include the `Contains` operator multiple times when the value of `Name` is one of the following:

- `Experiment.DisplayName`
- `Experiment.ExperimentName`
- `Experiment.Tags`
- `Trial.DisplayName`
- `Trial.TrialName`
- `Trial.Tags`
- `TrialComponent.DisplayName`
- `TrialComponent.TrialComponentName`
- `TrialComponent.Tags`
- `TrialComponent.InputArtifacts`
- `TrialComponent.OutputArtifacts`

A `SearchExpression` can include only one `Contains` operator for all other values of `Name` . In these cases, if you include multiple `Contains` operators in the `SearchExpression` , the result is the following error message: â`'CONTAINS' operator usage limit of 1 exceeded.` â

Value -> (string)

A value used with `Name` and `Operator` to determine which resources satisfy the filterâs condition. For numerical properties, `Value` must be an integer or floating-point decimal. For timestamp properties, `Value` must be an ISO 8601 date-time string of the following format: `YYYY-mm-dd'T'HH:MM:SS` .

NestedFilters -> (list)

A list of nested filter objects.

(structure)

A list of nested [Filter](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Filter.html) objects. A resource must satisfy the conditions of all filters to be included in the results returned from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

For example, to filter on a training jobâs `InputDataConfig` property with a specific channel name and `S3Uri` prefix, define the following filters:

- `'{Name:"InputDataConfig.ChannelName", "Operator":"Equals", "Value":"train"}',`
- `'{Name:"InputDataConfig.DataSource.S3DataSource.S3Uri", "Operator":"Contains", "Value":"mybucket/catdata"}'`

NestedPropertyName -> (string)

The name of the property to use in the nested filters. The value must match a listed property name, such as `InputDataConfig` .

Filters -> (list)

A list of filters. Each filter acts on a property. Filters must contain at least one `Filters` value. For example, a `NestedFilters` call might include a filter on the `PropertyName` parameter of the `InputDataConfig` property: `InputDataConfig.DataSource.S3DataSource.S3Uri` .

(structure)

A conditional statement for a search expression that includes a resource property, a Boolean operator, and a value. Resources that match the statement are returned in the results from the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

If you specify a `Value` , but not an `Operator` , SageMaker uses the equals operator.

In search, there are several property types:

Metrics

To define a metric filter, enter a value using the form `"Metrics.<name>"` , where `<name>` is a metric name. For example, the following filter searches for training jobs with an `"accuracy"` metric greater than `"0.9"` :

`{`

`"Name": "Metrics.accuracy",`

`"Operator": "GreaterThan",`

`"Value": "0.9"`

`}`

HyperParameters

To define a hyperparameter filter, enter a value with the form `"HyperParameters.<name>"` . Decimal hyperparameter values are treated as a decimal in a comparison if the specified `Value` is also a decimal value. If the specified `Value` is an integer, the decimal hyperparameter values are treated as integers. For example, the following filter is satisfied by training jobs with a `"learning_rate"` hyperparameter that is less than `"0.5"` :

`{`

`"Name": "HyperParameters.learning_rate",`

`"Operator": "LessThan",`

`"Value": "0.5"`

`}`

Tags

To define a tag filter, enter a value with the form `Tags.<key>` .

Name -> (string)

A resource property name. For example, `TrainingJobName` . For valid property names, see [SearchRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html) . You must specify a valid property for the resource.

Operator -> (string)

A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:

Equals

The value of `Name` equals `Value` .

NotEquals

The value of `Name` doesnât equal `Value` .

Exists

The `Name` property exists.

NotExists

The `Name` property does not exist.

GreaterThan

The value of `Name` is greater than `Value` . Not supported for text properties.

GreaterThanOrEqualTo

The value of `Name` is greater than or equal to `Value` . Not supported for text properties.

LessThan

The value of `Name` is less than `Value` . Not supported for text properties.

LessThanOrEqualTo

The value of `Name` is less than or equal to `Value` . Not supported for text properties.

In

The value of `Name` is one of the comma delimited strings in `Value` . Only supported for text properties.

Contains

The value of `Name` contains the string `Value` . Only supported for text properties.

A `SearchExpression` can include the `Contains` operator multiple times when the value of `Name` is one of the following:

- `Experiment.DisplayName`
- `Experiment.ExperimentName`
- `Experiment.Tags`
- `Trial.DisplayName`
- `Trial.TrialName`
- `Trial.Tags`
- `TrialComponent.DisplayName`
- `TrialComponent.TrialComponentName`
- `TrialComponent.Tags`
- `TrialComponent.InputArtifacts`
- `TrialComponent.OutputArtifacts`

A `SearchExpression` can include only one `Contains` operator for all other values of `Name` . In these cases, if you include multiple `Contains` operators in the `SearchExpression` , the result is the following error message: â`'CONTAINS' operator usage limit of 1 exceeded.` â

Value -> (string)

A value used with `Name` and `Operator` to determine which resources satisfy the filterâs condition. For numerical properties, `Value` must be an integer or floating-point decimal. For timestamp properties, `Value` must be an ISO 8601 date-time string of the following format: `YYYY-mm-dd'T'HH:MM:SS` .

SubExpressions -> (list)

A list of search expression objects.

( â¦ recursive â¦ )

Operator -> (string)

A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify `And` . If only a single conditional statement needs to be true for the entire search expression to be true, specify `Or` . The default value is `And` .

Operator -> (string)

A Boolean operator used to evaluate the search expression. If you want every conditional statement in all lists to be satisfied for the entire search expression to be true, specify `And` . If only a single conditional statement needs to be true for the entire search expression to be true, specify `Or` . The default value is `And` .

JSON Syntax:

```
{
  "Filters": [
    {
      "Name": "string",
      "Operator": "Equals"|"NotEquals"|"GreaterThan"|"GreaterThanOrEqualTo"|"LessThan"|"LessThanOrEqualTo"|"Contains"|"Exists"|"NotExists"|"In",
      "Value": "string"
    }
    ...
  ],
  "NestedFilters": [
    {
      "NestedPropertyName": "string",
      "Filters": [
        {
          "Name": "string",
          "Operator": "Equals"|"NotEquals"|"GreaterThan"|"GreaterThanOrEqualTo"|"LessThan"|"LessThanOrEqualTo"|"Contains"|"Exists"|"NotExists"|"In",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "SubExpressions": [
    {
      "Filters": [
        {
          "Name": "string",
          "Operator": "Equals"|"NotEquals"|"GreaterThan"|"GreaterThanOrEqualTo"|"LessThan"|"LessThanOrEqualTo"|"Contains"|"Exists"|"NotExists"|"In",
          "Value": "string"
        }
        ...
      ],
      "NestedFilters": [
        {
          "NestedPropertyName": "string",
          "Filters": [
            {
              "Name": "string",
              "Operator": "Equals"|"NotEquals"|"GreaterThan"|"GreaterThanOrEqualTo"|"LessThan"|"LessThanOrEqualTo"|"Contains"|"Exists"|"NotExists"|"In",
              "Value": "string"
            }
            ...
          ]
        }
        ...
      ],
      "SubExpressions": [
        { ... recursive ... }
        ...
      ],
      "Operator": "And"|"Or"
    }
    ...
  ],
  "Operator": "And"|"Or"
}
```

`--sort-by` (string)

The name of the resource property used to sort the `SearchResults` . The default is `LastModifiedTime` .

`--sort-order` (string)

How `SearchResults` are ordered. Valid values are `Ascending` or `Descending` . The default is `Descending` .

Possible values:

- `Ascending`
- `Descending`

`--cross-account-filter-option` (string)

A cross account filter option. When the value is `"CrossAccount"` the search results will only include resources made discoverable to you from other accounts. When the value is `"SameAccount"` or `null` the search results will only include resources from your account. Default is `null` . For more information on searching for resources made discoverable to your account, see [Search discoverable resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-cross-account-discoverability-use.html) in the SageMaker Developer Guide. The maximum number of `ResourceCatalog` s viewable is 1000.

Possible values:

- `SameAccount`
- `CrossAccount`

`--visibility-conditions` (list)

Limits the results of your search request to the resources that you can access.

(structure)

The list of key-value pairs used to filter your search results. If a search result contains a key from your list, it is included in the final search response if the value associated with the key in the result matches the value you specified. If the value doesnât match, the result is excluded from the search response. Any resources that donât have a key from the list that youâve provided will also be included in the search response.

Key -> (string)

The key that specifies the tag that youâre using to filter the search results. It must be in the following format: `Tags.<key>` .

Value -> (string)

The value for the tag that youâre using to filter the search results.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Results -> (list)

A list of `SearchRecord` objects.

(structure)

A single resource returned as part of the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API response.

TrainingJob -> (structure)

The properties of a training job.

TrainingJobName -> (string)

The name of the training job.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

TuningJobArn -> (string)

The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the labeling job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of the job.

ModelArtifacts -> (structure)

Information about the Amazon S3 location that is configured for storing model artifacts.

S3ModelArtifacts -> (string)

The path of the S3 object that contains the model artifacts. For example, `s3://bucket-name/keynameprefix/model.tar.gz` .

TrainingJobStatus -> (string)

The status of the training job.

Training job statuses are:

- `InProgress` - The training is in progress.
- `Completed` - The training job has completed.
- `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
- `Stopping` - The training job is stopping.
- `Stopped` - The training job has stopped.

For more detailed information, see `SecondaryStatus` .

SecondaryStatus -> (string)

Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html) .

SageMaker provides primary statuses and secondary statuses that apply to each of them:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

### Warning

Valid values for `SecondaryStatus` are subject to change.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTrainingStack`
- `DownloadingTrainingImage`

FailureReason -> (string)

If the training job failed, the reason it failed.

HyperParameters -> (map)

Algorithm-specific parameters.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

Information about the algorithm used for training, and algorithm metadata.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide* . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

For more information, see the note in the `AlgorithmName` parameter description.

AlgorithmName -> (string)

The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on Amazon Web Services Marketplace.

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you canât specify a value for `TrainingImage` , and vice versa.

If you specify values for both parameters, the training job might break; if you donât specify any value for both parameters, the training job might raise a `null` error.

TrainingInputMode -> (string)

The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

**Pipe mode**

If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.

**File mode**

If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.

You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.

For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training wonât be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.

**FastFile mode**

If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.

`FastFile` mode works best when the data is read sequentially. Augmented manifest files arenât supported. The startup time is lower when there are fewer files in the S3 bucket provided.

MetricDefinitions -> (list)

A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

EnableSageMakerMetricsTimeSeries -> (boolean)

To generate and save time-series metrics during training, set to `true` . The default is `false` and time-series metrics arenât generated except in the following cases:

- You use one of the SageMaker built-in algorithms
- You use one of the following [Prebuilt SageMaker Docker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html) :
- Tensorflow (version >= 1.15)
- MXNet (version >= 1.6)
- PyTorch (version >= 1.3)
- You specify at least one [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html)

ContainerEntrypoint -> (list)

The [entrypoint script for a Docker container](https://docs.docker.com/engine/reference/builder/) used to run a training job. This script takes precedence over the default train processing instructions. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for more information.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a training job. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for additional information.

(string)

TrainingImageConfig -> (structure)

The configuration to use an image from a private Docker registry for a training job.

TrainingRepositoryAccessMode -> (string)

The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to `Vpc` .

TrainingRepositoryAuthConfig -> (structure)

An object containing authentication information for a private Docker registry containing your training images.

TrainingRepositoryCredentialsProviderArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function used to give SageMaker access credentials to your private Docker registry.

RoleArn -> (string)

The Amazon Web Services Identity and Access Management (IAM) role configured for the training job.

InputDataConfig -> (list)

An array of `Channel` objects that describes each data input channel.

Your input must be in the same Amazon Web Services region as your training job.

(structure)

A channel is a named input source that training algorithms can consume.

ChannelName -> (string)

The name of the channel.

DataSource -> (structure)

The location of the channel data.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.

If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channelâs input mode is `Pipe` .

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/`
- A manifest might look like this: `s3://bucketname/example.manifest`   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri` . Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets. The following code example shows a valid manifest format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   This JSON is equivalent to the following `S3Uri` list:  `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.

Your input bucket must be located in same Amazon Web Services region as your training job.

S3DataDistributionType -> (string)

If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated` .

If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.

Donât choose more ML compute instances for training than available S3 objects. If you do, some nodes wonât get any data and you will pay for nodes that arenât getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.

In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key` . If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File` ), this copies 1/*n* of the number of objects.

AttributeNames -> (list)

A list of one or more attribute names to use that are found in a specified augmented manifest file.

(string)

InstanceGroupNames -> (list)

A list of names of instance groups that get data from the S3 data source.

(string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.

HubContentArn -> (string)

The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.

FileSystemDataSource -> (structure)

The file system that is associated with a channel.

FileSystemId -> (string)

The file system id.

FileSystemAccessMode -> (string)

The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.

FileSystemType -> (string)

The file system type.

DirectoryPath -> (string)

The full path to the directory to associate with the channel.

ContentType -> (string)

The MIME type of the data.

CompressionType -> (string)

If training data is compressed, the compression type. The default value is `None` . `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.

RecordWrapperType -> (string)

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you donât need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format) .

In File mode, leave this field unset or set it to None.

InputMode -> (string)

(Optional) The input mode to use for the data channel in a training job. If you donât set a value for `InputMode` , SageMaker uses the value set for `TrainingInputMode` . Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training jobâs general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.

To use a model for incremental training, choose `File` input model.

ShuffleConfig -> (structure)

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType` , this shuffles the results of the S3 key prefix matches. If you use `ManifestFile` , the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile` , the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

Seed -> (long)

Determines the shuffling order in `ShuffleConfig` value.

OutputDataConfig -> (structure)

The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide* . If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone

The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob` , `CreateTransformJob` , or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

S3OutputPath -> (string)

Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

CompressionType -> (string)

The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.

ResourceConfig -> (structure)

Resources, including ML compute instances and ML storage volumes, that are configured for model training.

InstanceType -> (string)

The ML compute instance type.

### Note

SageMaker Training on Amazon Elastic Compute Cloud (EC2) P4de instances is in preview release starting December 9th, 2022.

[Amazon EC2 P4de instances](http://aws.amazon.com/ec2/instance-types/p4/) (currently in preview) are powered by 8 NVIDIA A100 GPUs with 80GB high-performance HBM2e GPU memory, which accelerate the speed of training ML models that need to be trained on large datasets of high-resolution data. In this preview release, Amazon SageMaker supports ML training jobs on P4de instances (`ml.p4de.24xlarge` ) to reduce model training time. The `ml.p4de.24xlarge` instances are available in the following Amazon Web Services Regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)

To request quota limit increase and start using P4de instances, contact the SageMaker Training service team through your account team.

InstanceCount -> (integer)

The number of ML compute instances to use. For distributed training, provide a value greater than 1.

VolumeSizeInGB -> (integer)

The size of the ML storage volume that you want to provision.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.

When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes) , SageMaker doesnât provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instanceâs storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d` , `ml.g4dn` , and `ml.g5` .

When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2` .

To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html) .

VolumeKmsKeyId -> (string)

The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be in any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

KeepAlivePeriodInSeconds -> (integer)

The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.

InstanceGroups -> (list)

The configuration of a heterogeneous cluster in JSON format.

(structure)

Defines an instance group for heterogeneous cluster training. When requesting a training job using the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API, you can configure multiple instance groups .

InstanceType -> (string)

Specifies the instance type of the instance group.

InstanceCount -> (integer)

Specifies the number of instances of the instance group.

InstanceGroupName -> (string)

Specifies the name of the instance group.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.

VpcConfig -> (structure)

A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

StoppingCondition -> (structure)

Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

CreationTime -> (timestamp)

A timestamp that indicates when the training job was created.

TrainingStartTime -> (timestamp)

Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of `TrainingEndTime` . The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.

TrainingEndTime -> (timestamp)

Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.

LastModifiedTime -> (timestamp)

A timestamp that indicates when the status of the training job was last modified.

SecondaryStatusTransitions -> (list)

A history of all of the secondary statuses that the training job has transitioned through.

(structure)

An array element of `SecondaryStatusTransitions` for [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) . It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the jobâs secondary status.

Status -> (string)

Contains a secondary status information from a training job.

Status might be one of the following secondary statuses:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTrainingStack`
- `DownloadingTrainingImage`

StartTime -> (timestamp)

A timestamp that shows when the training job transitioned to the current secondary status state.

EndTime -> (timestamp)

A timestamp that shows when the training job transitioned out of this secondary status state into another secondary status state or when the training job has ended.

StatusMessage -> (string)

A detailed description of the progress within a secondary status.

SageMaker provides secondary statuses and status messages that apply to each of them:

Starting

- Starting the training job.
- Launching requested ML instances.
- Insufficient capacity error from EC2 while launching instances, retrying!
- Launched instance was unhealthy, replacing it!
- Preparing the instances for training.

Training
- Training image download completed. Training in progress.

### Warning

Status messages are subject to change. Therefore, we recommend not including them in code that programmatically initiates actions. For examples, donât use status messages in if statements.

To have an overview of your training jobâs progress, view `TrainingJobStatus` and `SecondaryStatus` in [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) , and `StatusMessage` together. For example, at the start of a training job, you might see the following:

- `TrainingJobStatus` - InProgress
- `SecondaryStatus` - Training
- `StatusMessage` - Downloading the training image

FinalMetricDataList -> (list)

A list of final metric values that are set when the training job completes. Used only if the training job was configured to use metrics.

(structure)

The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.

MetricName -> (string)

The name of the metric.

Value -> (float)

The value of the metric.

Timestamp -> (timestamp)

The date and time that the algorithm emitted the metric.

EnableNetworkIsolation -> (boolean)

If the `TrainingJob` was created with network isolation, the value is set to `true` . If network isolation is enabled, nodes canât communicate beyond the VPC they run in.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

When true, enables managed spot training using Amazon EC2 Spot instances to run training jobs instead of on-demand instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) .

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

TrainingTimeInSeconds -> (integer)

The training time in seconds.

BillableTimeInSeconds -> (integer)

The billable time in seconds.

DebugHookConfig -> (structure)

Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

LocalPath -> (string)

Path to local storage location for metrics and tensors. Defaults to `/opt/ml/output/tensors/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for metrics and tensors.

HookParameters -> (map)

Configuration information for the Amazon SageMaker Debugger hook parameters.

key -> (string)

value -> (string)

CollectionConfigurations -> (list)

Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the `CollectionConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

(structure)

Configuration information for the Amazon SageMaker Debugger output tensor collections.

CollectionName -> (string)

The name of the tensor collection. The name must be unique relative to other rule configuration names.

CollectionParameters -> (map)

Parameter values for the tensor collection. The allowed parameters are `"name"` , `"include_regex"` , `"reduction_config"` , `"save_config"` , `"tensor_names"` , and `"save_histogram"` .

key -> (string)

value -> (string)

ExperimentConfig -> (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

DebugRuleConfigurations -> (list)

Information about the debug rule configuration.

(structure)

Configuration information for SageMaker Debugger rules for debugging. To learn more about how to configure the `DebugRuleConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

RuleConfigurationName -> (string)

The name of the rule configuration. It must be unique relative to other rule configuration names.

LocalPath -> (string)

Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for rules.

RuleEvaluatorImage -> (string)

The Amazon Elastic Container (ECR) Image for the managed rule evaluation.

InstanceType -> (string)

The instance type to deploy a custom rule for debugging a training job.

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to the processing instance.

RuleParameters -> (map)

Runtime configuration for rule container.

key -> (string)

value -> (string)

TensorBoardOutputConfig -> (structure)

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

LocalPath -> (string)

Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for TensorBoard output.

DebugRuleEvaluationStatuses -> (list)

Information about the evaluation status of the rules for the training job.

(structure)

Information about the status of the rule evaluation.

RuleConfigurationName -> (string)

The name of the rule configuration.

RuleEvaluationJobArn -> (string)

The Amazon Resource Name (ARN) of the rule evaluation job.

RuleEvaluationStatus -> (string)

Status of the rule evaluation.

StatusDetails -> (string)

Details from the rule evaluation.

LastModifiedTime -> (timestamp)

Timestamp when the rule evaluation status was last modified.

ProfilerConfig -> (structure)

Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.

S3OutputPath -> (string)

Path to Amazon S3 storage location for system and framework metrics.

ProfilingIntervalInMilliseconds -> (long)

A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.

ProfilingParameters -> (map)

Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig` , `PythonProfilingConfig` , and `DataLoaderProfilingConfig` . The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

key -> (string)

value -> (string)

DisableProfiler -> (boolean)

Configuration to turn off Amazon SageMaker Debuggerâs system monitoring and profiling functionality. To turn it off, set to `True` .

Environment -> (map)

The environment variables to set in the Docker container.

key -> (string)

value -> (string)

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Tags -> (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Experiment -> (structure)

The properties of an experiment.

ExperimentName -> (string)

The name of the experiment.

ExperimentArn -> (string)

The Amazon Resource Name (ARN) of the experiment.

DisplayName -> (string)

The name of the experiment as displayed. If `DisplayName` isnât specified, `ExperimentName` is displayed.

Source -> (structure)

The source of the experiment.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source.

SourceType -> (string)

The source type.

Description -> (string)

The description of the experiment.

CreationTime -> (timestamp)

When the experiment was created.

CreatedBy -> (structure)

Who created the experiment.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

When the experiment was last modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

Tags -> (list)

The list of tags that are associated with the experiment. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Trial -> (structure)

The properties of a trial.

TrialName -> (string)

The name of the trial.

TrialArn -> (string)

The Amazon Resource Name (ARN) of the trial.

DisplayName -> (string)

The name of the trial as displayed. If `DisplayName` isnât specified, `TrialName` is displayed.

ExperimentName -> (string)

The name of the experiment the trial is part of.

Source -> (structure)

The source of the trial.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source.

SourceType -> (string)

The source job type.

CreationTime -> (timestamp)

When the trial was created.

CreatedBy -> (structure)

Who created the trial.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

Who last modified the trial.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

MetadataProperties -> (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

Tags -> (list)

The list of tags that are associated with the trial. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

TrialComponentSummaries -> (list)

A list of the components associated with the trial. For each component, a summary of the componentâs properties is included.

(structure)

A short summary of a trial component.

TrialComponentName -> (string)

The name of the trial component.

TrialComponentArn -> (string)

The Amazon Resource Name (ARN) of the trial component.

TrialComponentSource -> (structure)

The Amazon Resource Name (ARN) and job type of the source of a trial component.

SourceArn -> (string)

The source Amazon Resource Name (ARN).

SourceType -> (string)

The source job type.

CreationTime -> (timestamp)

When the component was created.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

TrialComponent -> (structure)

The properties of a trial component.

TrialComponentName -> (string)

The name of the trial component.

DisplayName -> (string)

The name of the component as displayed. If `DisplayName` isnât specified, `TrialComponentName` is displayed.

TrialComponentArn -> (string)

The Amazon Resource Name (ARN) of the trial component.

Source -> (structure)

The Amazon Resource Name (ARN) and job type of the source of the component.

SourceArn -> (string)

The source Amazon Resource Name (ARN).

SourceType -> (string)

The source job type.

Status -> (structure)

The status of the trial component.

PrimaryStatus -> (string)

The status of the trial component.

Message -> (string)

If the component failed, a message describing why.

StartTime -> (timestamp)

When the component started.

EndTime -> (timestamp)

When the component ended.

CreationTime -> (timestamp)

When the component was created.

CreatedBy -> (structure)

Who created the trial component.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

When the component was last modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

Parameters -> (map)

The hyperparameters of the component.

key -> (string)

value -> (structure)

The value of a hyperparameter. Only one of `NumberValue` or `StringValue` can be specified.

This object is specified in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

StringValue -> (string)

The string value of a categorical hyperparameter. If you specify a value for this parameter, you canât specify the `NumberValue` parameter.

NumberValue -> (double)

The numeric value of a numeric hyperparameter. If you specify a value for this parameter, you canât specify the `StringValue` parameter.

InputArtifacts -> (map)

The input artifacts of the component.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

OutputArtifacts -> (map)

The output artifacts of the component.

key -> (string)

value -> (structure)

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

MediaType -> (string)

The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.

Value -> (string)

The location of the artifact.

Metrics -> (list)

The metrics for the component.

(structure)

A summary of the metrics of a trial component.

MetricName -> (string)

The name of the metric.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source.

TimeStamp -> (timestamp)

When the metric was last updated.

Max -> (double)

The maximum value of the metric.

Min -> (double)

The minimum value of the metric.

Last -> (double)

The most recent value of the metric.

Count -> (integer)

The number of samples used to generate the metric.

Avg -> (double)

The average value of the metric.

StdDev -> (double)

The standard deviation of the metric.

MetadataProperties -> (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

SourceDetail -> (structure)

Details of the source of the component.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source.

TrainingJob -> (structure)

Information about a training job thatâs the source of a trial component.

TrainingJobName -> (string)

The name of the training job.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

TuningJobArn -> (string)

The Amazon Resource Name (ARN) of the associated hyperparameter tuning job if the training job was launched by a hyperparameter tuning job.

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the labeling job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of the job.

ModelArtifacts -> (structure)

Information about the Amazon S3 location that is configured for storing model artifacts.

S3ModelArtifacts -> (string)

The path of the S3 object that contains the model artifacts. For example, `s3://bucket-name/keynameprefix/model.tar.gz` .

TrainingJobStatus -> (string)

The status of the training job.

Training job statuses are:

- `InProgress` - The training is in progress.
- `Completed` - The training job has completed.
- `Failed` - The training job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTrainingJobResponse` call.
- `Stopping` - The training job is stopping.
- `Stopped` - The training job has stopped.

For more detailed information, see `SecondaryStatus` .

SecondaryStatus -> (string)

Provides detailed information about the state of the training job. For detailed information about the secondary status of the training job, see `StatusMessage` under [SecondaryStatusTransition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SecondaryStatusTransition.html) .

SageMaker provides primary statuses and secondary statuses that apply to each of them:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

### Warning

Valid values for `SecondaryStatus` are subject to change.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTrainingStack`
- `DownloadingTrainingImage`

FailureReason -> (string)

If the training job failed, the reason it failed.

HyperParameters -> (map)

Algorithm-specific parameters.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

Information about the algorithm used for training, and algorithm metadata.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about docker registry paths for SageMaker built-in algorithms, see [Docker Registry Paths and Example Code](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) in the *Amazon SageMaker developer guide* . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information about using your custom training container, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

For more information, see the note in the `AlgorithmName` parameter description.

AlgorithmName -> (string)

The name of the algorithm resource to use for the training job. This must be an algorithm resource that you created or subscribe to on Amazon Web Services Marketplace.

### Note

You must specify either the algorithm name to the `AlgorithmName` parameter or the image URI of the algorithm container to the `TrainingImage` parameter.

Note that the `AlgorithmName` parameter is mutually exclusive with the `TrainingImage` parameter. If you specify a value for the `AlgorithmName` parameter, you canât specify a value for `TrainingImage` , and vice versa.

If you specify values for both parameters, the training job might break; if you donât specify any value for both parameters, the training job might raise a `null` error.

TrainingInputMode -> (string)

The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

**Pipe mode**

If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.

**File mode**

If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.

You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.

For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training wonât be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.

**FastFile mode**

If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.

`FastFile` mode works best when the data is read sequentially. Augmented manifest files arenât supported. The startup time is lower when there are fewer files in the S3 bucket provided.

MetricDefinitions -> (list)

A list of metric definition objects. Each object specifies the metric name and regular expressions used to parse algorithm logs. SageMaker publishes each metric to Amazon CloudWatch.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

EnableSageMakerMetricsTimeSeries -> (boolean)

To generate and save time-series metrics during training, set to `true` . The default is `false` and time-series metrics arenât generated except in the following cases:

- You use one of the SageMaker built-in algorithms
- You use one of the following [Prebuilt SageMaker Docker Images](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-containers-frameworks-deep-learning.html) :
- Tensorflow (version >= 1.15)
- MXNet (version >= 1.6)
- PyTorch (version >= 1.3)
- You specify at least one [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html)

ContainerEntrypoint -> (list)

The [entrypoint script for a Docker container](https://docs.docker.com/engine/reference/builder/) used to run a training job. This script takes precedence over the default train processing instructions. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for more information.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a training job. See [How Amazon SageMaker Runs Your Training Image](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-training-algo-dockerfile.html) for additional information.

(string)

TrainingImageConfig -> (structure)

The configuration to use an image from a private Docker registry for a training job.

TrainingRepositoryAccessMode -> (string)

The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to `Vpc` .

TrainingRepositoryAuthConfig -> (structure)

An object containing authentication information for a private Docker registry containing your training images.

TrainingRepositoryCredentialsProviderArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function used to give SageMaker access credentials to your private Docker registry.

RoleArn -> (string)

The Amazon Web Services Identity and Access Management (IAM) role configured for the training job.

InputDataConfig -> (list)

An array of `Channel` objects that describes each data input channel.

Your input must be in the same Amazon Web Services region as your training job.

(structure)

A channel is a named input source that training algorithms can consume.

ChannelName -> (string)

The name of the channel.

DataSource -> (structure)

The location of the channel data.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.

If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channelâs input mode is `Pipe` .

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/`
- A manifest might look like this: `s3://bucketname/example.manifest`   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri` . Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets. The following code example shows a valid manifest format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   This JSON is equivalent to the following `S3Uri` list:  `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.

Your input bucket must be located in same Amazon Web Services region as your training job.

S3DataDistributionType -> (string)

If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated` .

If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.

Donât choose more ML compute instances for training than available S3 objects. If you do, some nodes wonât get any data and you will pay for nodes that arenât getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.

In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key` . If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File` ), this copies 1/*n* of the number of objects.

AttributeNames -> (list)

A list of one or more attribute names to use that are found in a specified augmented manifest file.

(string)

InstanceGroupNames -> (list)

A list of names of instance groups that get data from the S3 data source.

(string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.

HubContentArn -> (string)

The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.

FileSystemDataSource -> (structure)

The file system that is associated with a channel.

FileSystemId -> (string)

The file system id.

FileSystemAccessMode -> (string)

The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.

FileSystemType -> (string)

The file system type.

DirectoryPath -> (string)

The full path to the directory to associate with the channel.

ContentType -> (string)

The MIME type of the data.

CompressionType -> (string)

If training data is compressed, the compression type. The default value is `None` . `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.

RecordWrapperType -> (string)

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you donât need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format) .

In File mode, leave this field unset or set it to None.

InputMode -> (string)

(Optional) The input mode to use for the data channel in a training job. If you donât set a value for `InputMode` , SageMaker uses the value set for `TrainingInputMode` . Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training jobâs general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.

To use a model for incremental training, choose `File` input model.

ShuffleConfig -> (structure)

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType` , this shuffles the results of the S3 key prefix matches. If you use `ManifestFile` , the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile` , the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

Seed -> (long)

Determines the shuffling order in `ShuffleConfig` value.

OutputDataConfig -> (structure)

The S3 path where model artifacts that you configured when creating the job are stored. SageMaker creates subfolders for model artifacts.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide* . If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone

The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob` , `CreateTransformJob` , or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

S3OutputPath -> (string)

Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

CompressionType -> (string)

The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.

ResourceConfig -> (structure)

Resources, including ML compute instances and ML storage volumes, that are configured for model training.

InstanceType -> (string)

The ML compute instance type.

### Note

SageMaker Training on Amazon Elastic Compute Cloud (EC2) P4de instances is in preview release starting December 9th, 2022.

[Amazon EC2 P4de instances](http://aws.amazon.com/ec2/instance-types/p4/) (currently in preview) are powered by 8 NVIDIA A100 GPUs with 80GB high-performance HBM2e GPU memory, which accelerate the speed of training ML models that need to be trained on large datasets of high-resolution data. In this preview release, Amazon SageMaker supports ML training jobs on P4de instances (`ml.p4de.24xlarge` ) to reduce model training time. The `ml.p4de.24xlarge` instances are available in the following Amazon Web Services Regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)

To request quota limit increase and start using P4de instances, contact the SageMaker Training service team through your account team.

InstanceCount -> (integer)

The number of ML compute instances to use. For distributed training, provide a value greater than 1.

VolumeSizeInGB -> (integer)

The size of the ML storage volume that you want to provision.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.

When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes) , SageMaker doesnât provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instanceâs storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d` , `ml.g4dn` , and `ml.g5` .

When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2` .

To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html) .

VolumeKmsKeyId -> (string)

The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be in any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

KeepAlivePeriodInSeconds -> (integer)

The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.

InstanceGroups -> (list)

The configuration of a heterogeneous cluster in JSON format.

(structure)

Defines an instance group for heterogeneous cluster training. When requesting a training job using the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API, you can configure multiple instance groups .

InstanceType -> (string)

Specifies the instance type of the instance group.

InstanceCount -> (integer)

Specifies the number of instances of the instance group.

InstanceGroupName -> (string)

Specifies the name of the instance group.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.

VpcConfig -> (structure)

A [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that this training job has access to. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

StoppingCondition -> (structure)

Specifies a limit to how long a model training job can run. It also specifies how long a managed Spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

To stop a job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

CreationTime -> (timestamp)

A timestamp that indicates when the training job was created.

TrainingStartTime -> (timestamp)

Indicates the time when the training job starts on training instances. You are billed for the time interval between this time and the value of `TrainingEndTime` . The start time in CloudWatch Logs might be later than this time. The difference is due to the time it takes to download the training data and to the size of the training container.

TrainingEndTime -> (timestamp)

Indicates the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.

LastModifiedTime -> (timestamp)

A timestamp that indicates when the status of the training job was last modified.

SecondaryStatusTransitions -> (list)

A history of all of the secondary statuses that the training job has transitioned through.

(structure)

An array element of `SecondaryStatusTransitions` for [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) . It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the jobâs secondary status.

Status -> (string)

Contains a secondary status information from a training job.

Status might be one of the following secondary statuses:

InProgress

- `Starting` - Starting the training job.
- `Downloading` - An optional stage for algorithms that support `File` training input mode. It indicates that data is being downloaded to the ML storage volumes.
- `Training` - Training is in progress.
- `Uploading` - Training is complete and the model artifacts are being uploaded to the S3 location.

Completed
- `Completed` - The training job has completed.

Failed
- `Failed` - The training job has failed. The reason for the failure is returned in the `FailureReason` field of `DescribeTrainingJobResponse` .

Stopped
- `MaxRuntimeExceeded` - The job stopped because it exceeded the maximum allowed runtime.
- `Stopped` - The training job has stopped.

Stopping
- `Stopping` - Stopping the training job.

We no longer support the following secondary statuses:

- `LaunchingMLInstances`
- `PreparingTrainingStack`
- `DownloadingTrainingImage`

StartTime -> (timestamp)

A timestamp that shows when the training job transitioned to the current secondary status state.

EndTime -> (timestamp)

A timestamp that shows when the training job transitioned out of this secondary status state into another secondary status state or when the training job has ended.

StatusMessage -> (string)

A detailed description of the progress within a secondary status.

SageMaker provides secondary statuses and status messages that apply to each of them:

Starting

- Starting the training job.
- Launching requested ML instances.
- Insufficient capacity error from EC2 while launching instances, retrying!
- Launched instance was unhealthy, replacing it!
- Preparing the instances for training.

Training
- Training image download completed. Training in progress.

### Warning

Status messages are subject to change. Therefore, we recommend not including them in code that programmatically initiates actions. For examples, donât use status messages in if statements.

To have an overview of your training jobâs progress, view `TrainingJobStatus` and `SecondaryStatus` in [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) , and `StatusMessage` together. For example, at the start of a training job, you might see the following:

- `TrainingJobStatus` - InProgress
- `SecondaryStatus` - Training
- `StatusMessage` - Downloading the training image

FinalMetricDataList -> (list)

A list of final metric values that are set when the training job completes. Used only if the training job was configured to use metrics.

(structure)

The name, value, and date and time of a metric that was emitted to Amazon CloudWatch.

MetricName -> (string)

The name of the metric.

Value -> (float)

The value of the metric.

Timestamp -> (timestamp)

The date and time that the algorithm emitted the metric.

EnableNetworkIsolation -> (boolean)

If the `TrainingJob` was created with network isolation, the value is set to `true` . If network isolation is enabled, nodes canât communicate beyond the VPC they run in.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

When true, enables managed spot training using Amazon EC2 Spot instances to run training jobs instead of on-demand instances. For more information, see [Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) .

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

TrainingTimeInSeconds -> (integer)

The training time in seconds.

BillableTimeInSeconds -> (integer)

The billable time in seconds.

DebugHookConfig -> (structure)

Configuration information for the Amazon SageMaker Debugger hook parameters, metric and tensor collections, and storage paths. To learn more about how to configure the `DebugHookConfig` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

LocalPath -> (string)

Path to local storage location for metrics and tensors. Defaults to `/opt/ml/output/tensors/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for metrics and tensors.

HookParameters -> (map)

Configuration information for the Amazon SageMaker Debugger hook parameters.

key -> (string)

value -> (string)

CollectionConfigurations -> (list)

Configuration information for Amazon SageMaker Debugger tensor collections. To learn more about how to configure the `CollectionConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

(structure)

Configuration information for the Amazon SageMaker Debugger output tensor collections.

CollectionName -> (string)

The name of the tensor collection. The name must be unique relative to other rule configuration names.

CollectionParameters -> (map)

Parameter values for the tensor collection. The allowed parameters are `"name"` , `"include_regex"` , `"reduction_config"` , `"save_config"` , `"tensor_names"` , and `"save_histogram"` .

key -> (string)

value -> (string)

ExperimentConfig -> (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

DebugRuleConfigurations -> (list)

Information about the debug rule configuration.

(structure)

Configuration information for SageMaker Debugger rules for debugging. To learn more about how to configure the `DebugRuleConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

RuleConfigurationName -> (string)

The name of the rule configuration. It must be unique relative to other rule configuration names.

LocalPath -> (string)

Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for rules.

RuleEvaluatorImage -> (string)

The Amazon Elastic Container (ECR) Image for the managed rule evaluation.

InstanceType -> (string)

The instance type to deploy a custom rule for debugging a training job.

VolumeSizeInGB -> (integer)

The size, in GB, of the ML storage volume attached to the processing instance.

RuleParameters -> (map)

Runtime configuration for rule container.

key -> (string)

value -> (string)

TensorBoardOutputConfig -> (structure)

Configuration of storage locations for the Amazon SageMaker Debugger TensorBoard output data.

LocalPath -> (string)

Path to local storage location for tensorBoard output. Defaults to `/opt/ml/output/tensorboard` .

S3OutputPath -> (string)

Path to Amazon S3 storage location for TensorBoard output.

DebugRuleEvaluationStatuses -> (list)

Information about the evaluation status of the rules for the training job.

(structure)

Information about the status of the rule evaluation.

RuleConfigurationName -> (string)

The name of the rule configuration.

RuleEvaluationJobArn -> (string)

The Amazon Resource Name (ARN) of the rule evaluation job.

RuleEvaluationStatus -> (string)

Status of the rule evaluation.

StatusDetails -> (string)

Details from the rule evaluation.

LastModifiedTime -> (timestamp)

Timestamp when the rule evaluation status was last modified.

ProfilerConfig -> (structure)

Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.

S3OutputPath -> (string)

Path to Amazon S3 storage location for system and framework metrics.

ProfilingIntervalInMilliseconds -> (long)

A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.

ProfilingParameters -> (map)

Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig` , `PythonProfilingConfig` , and `DataLoaderProfilingConfig` . The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html) .

key -> (string)

value -> (string)

DisableProfiler -> (boolean)

Configuration to turn off Amazon SageMaker Debuggerâs system monitoring and profiling functionality. To turn it off, set to `True` .

Environment -> (map)

The environment variables to set in the Docker container.

key -> (string)

value -> (string)

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Tags -> (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

ProcessingJob -> (structure)

Information about a processing job thatâs the source of a trial component.

ProcessingInputs -> (list)

List of input configurations for the processing job.

(structure)

The inputs for a processing job. The processing input must specify exactly one of either `S3Input` or `DatasetDefinition` types.

InputName -> (string)

The name for the processing job input.

AppManaged -> (boolean)

When `True` , input operations such as data download are managed natively by the processing job application. When `False` (default), input operations are managed by Amazon SageMaker.

S3Input -> (structure)

Configuration for downloading input data from Amazon S3 into the processing container.

S3Uri -> (string)

The URI of the Amazon S3 prefix Amazon SageMaker downloads data required to run a processing job.

LocalPath -> (string)

The local path in your container where you want Amazon SageMaker to write input data to. `LocalPath` is an absolute path to the input data and must begin with `/opt/ml/processing/` . `LocalPath` is a required parameter when `AppManaged` is `False` (default).

S3DataType -> (string)

Whether you use an `S3Prefix` or a `ManifestFile` for the data type. If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for the processing job. If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for the processing job.

S3InputMode -> (string)

Whether to use `File` or `Pipe` input mode. In File mode, Amazon SageMaker copies the data from the input source onto the local ML storage volume before starting your processing container. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your processing container into named pipes without using the ML storage volume.

S3DataDistributionType -> (string)

Whether to distribute the data from Amazon S3 to all processing instances with `FullyReplicated` , or whether the data from Amazon S3 is shared by Amazon S3 key, downloading one shard of data to each processing instance.

S3CompressionType -> (string)

Whether to GZIP-decompress the data in Amazon S3 as it is streamed into the processing container. `Gzip` can only be used when `Pipe` mode is specified as the `S3InputMode` . In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your container without using the EBS volume.

DatasetDefinition -> (structure)

Configuration for a Dataset Definition input.

AthenaDatasetDefinition -> (structure)

Configuration for Athena Dataset Definition input.

Catalog -> (string)

The name of the data catalog used in Athena query execution.

Database -> (string)

The name of the database used in the Athena query execution.

QueryString -> (string)

The SQL query statements, to be executed.

WorkGroup -> (string)

The name of the workgroup in which the Athena query is being started.

OutputS3Uri -> (string)

The location in Amazon S3 where Athena query results are stored.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data generated from an Athena query execution.

OutputFormat -> (string)

The data storage format for Athena query results.

OutputCompression -> (string)

The compression used for Athena query results.

RedshiftDatasetDefinition -> (structure)

Configuration for Redshift Dataset Definition input.

ClusterId -> (string)

The Redshift cluster Identifier.

Database -> (string)

The name of the Redshift database used in Redshift query execution.

DbUser -> (string)

The database user name used in Redshift query execution.

QueryString -> (string)

The SQL query statements to be executed.

ClusterRoleArn -> (string)

The IAM role attached to your Redshift cluster that Amazon SageMaker uses to generate datasets.

OutputS3Uri -> (string)

The location in Amazon S3 where the Redshift query results are stored.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data from a Redshift execution.

OutputFormat -> (string)

The data storage format for Redshift query results.

OutputCompression -> (string)

The compression used for Redshift query results.

LocalPath -> (string)

The local path where you want Amazon SageMaker to download the Dataset Definition inputs to run a processing job. `LocalPath` is an absolute path to the input data. This is a required parameter when `AppManaged` is `False` (default).

DataDistributionType -> (string)

Whether the generated dataset is `FullyReplicated` or `ShardedByS3Key` (default).

InputMode -> (string)

Whether to use `File` or `Pipe` input mode. In `File` (default) mode, Amazon SageMaker copies the data from the input source onto the local Amazon Elastic Block Store (Amazon EBS) volumes before starting your training algorithm. This is the most commonly used input mode. In `Pipe` mode, Amazon SageMaker streams input data from the source directly to your algorithm without using the EBS volume.

ProcessingOutputConfig -> (structure)

Configuration for uploading output from the processing container.

Outputs -> (list)

An array of outputs configuring the data to upload from the processing container.

(structure)

Describes the results of a processing job. The processing output must specify exactly one of either `S3Output` or `FeatureStoreOutput` types.

OutputName -> (string)

The name for the processing job output.

S3Output -> (structure)

Configuration for processing job outputs in Amazon S3.

S3Uri -> (string)

A URI that identifies the Amazon S3 bucket where you want Amazon SageMaker to save the results of a processing job.

LocalPath -> (string)

The local path of a directory where you want Amazon SageMaker to upload its contents to Amazon S3. `LocalPath` is an absolute path to a directory containing output files. This directory will be created by the platform and exist when your containerâs entrypoint is invoked.

S3UploadMode -> (string)

Whether to upload the results of the processing job continuously or after the job completes.

FeatureStoreOutput -> (structure)

Configuration for processing job outputs in Amazon SageMaker Feature Store. This processing output type is only supported when `AppManaged` is specified.

FeatureGroupName -> (string)

The name of the Amazon SageMaker FeatureGroup to use as the destination for processing job output. Note that your processing script is responsible for putting records into your Feature Store.

AppManaged -> (boolean)

When `True` , output operations such as data upload are managed natively by the processing job application. When `False` (default), output operations are managed by Amazon SageMaker.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the processing job output. `KmsKeyId` can be an ID of a KMS key, ARN of a KMS key, or alias of a KMS key. The `KmsKeyId` is applied to all outputs.

ProcessingJobName -> (string)

The name of the processing job.

ProcessingResources -> (structure)

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.

ClusterConfig -> (structure)

The configuration for the resources in a cluster used to run the processing job.

InstanceCount -> (integer)

The number of ML compute instances to use in the processing job. For distributed processing jobs, specify a value greater than 1. The default value is 1.

InstanceType -> (string)

The ML compute instance type for the processing job.

VolumeSizeInGB -> (integer)

The size of the ML storage volume in gigabytes that you want to provision. You must specify sufficient ML storage for your scenario.

### Note

Certain Nitro-based instances include local storage with a fixed total size, dependent on the instance type. When using these instances for processing, Amazon SageMaker mounts the local instance storage instead of Amazon EBS gp2 storage. You canât request a `VolumeSizeInGB` greater than the total size of the local instance storage.

For a list of instance types that support local instance storage, including the total size per instance type, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the processing job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

StoppingCondition -> (structure)

Configures conditions under which the processing job should be stopped, such as how long the processing job has been running. After the condition is met, the processing job is stopped.

MaxRuntimeInSeconds -> (integer)

Specifies the maximum runtime in seconds.

AppSpecification -> (structure)

Configuration to run a processing job in a specified container image.

ImageUri -> (string)

The container image to be run by the processing job.

ContainerEntrypoint -> (list)

The entrypoint for a container used to run a processing job.

(string)

ContainerArguments -> (list)

The arguments for a container used to run a processing job.

(string)

Environment -> (map)

Sets the environment variables in the Docker container.

key -> (string)

value -> (string)

NetworkConfig -> (structure)

Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the processing job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

RoleArn -> (string)

The ARN of the role used to create the processing job.

ExperimentConfig -> (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

ProcessingJobArn -> (string)

The ARN of the processing job.

ProcessingJobStatus -> (string)

The status of the processing job.

ExitMessage -> (string)

A string, up to one KB in size, that contains metadata from the processing container when the processing job exits.

FailureReason -> (string)

A string, up to one KB in size, that contains the reason a processing job failed, if it failed.

ProcessingEndTime -> (timestamp)

The time that the processing job ended.

ProcessingStartTime -> (timestamp)

The time that the processing job started.

LastModifiedTime -> (timestamp)

The time the processing job was last modified.

CreationTime -> (timestamp)

The time the processing job was created.

MonitoringScheduleArn -> (string)

The ARN of a monitoring schedule for an endpoint associated with this processing job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of the AutoML job associated with this processing job.

TrainingJobArn -> (string)

The ARN of the training job associated with this processing job.

Tags -> (list)

An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL) in the *Amazon Web Services Billing and Cost Management User Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

TransformJob -> (structure)

Information about a transform job thatâs the source of a trial component.

TransformJobName -> (string)

The name of the transform job.

TransformJobArn -> (string)

The Amazon Resource Name (ARN) of the transform job.

TransformJobStatus -> (string)

The status of the transform job.

Transform job statuses are:

- `InProgress` - The job is in progress.
- `Completed` - The job has completed.
- `Failed` - The transform job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTransformJob` call.
- `Stopping` - The transform job is stopping.
- `Stopped` - The transform job has stopped.

FailureReason -> (string)

If the transform job failed, the reason it failed.

ModelName -> (string)

The name of the model associated with the transform job.

MaxConcurrentTransforms -> (integer)

The maximum number of parallel requests that can be sent to each instance in a transform job. If `MaxConcurrentTransforms` is set to 0 or left unset, SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is 1. For built-in algorithms, you donât need to set a value for `MaxConcurrentTransforms` .

ModelClientConfig -> (structure)

Configures the timeout and maximum number of retries for processing a transform job invocation.

InvocationsTimeoutInSeconds -> (integer)

The timeout value in seconds for an invocation request. The default value is 600.

InvocationsMaxRetries -> (integer)

The maximum number of retries when invocation requests are failing. The default value is 3.

MaxPayloadInMB -> (integer)

The maximum allowed size of the payload, in MB. A payload is the data portion of a record (without metadata). The value in `MaxPayloadInMB` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is 6 MB. For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0. This feature works only in supported algorithms. Currently, SageMaker built-in algorithms do not support HTTP chunked encoding.

BatchStrategy -> (string)

Specifies the number of records to include in a mini-batch for an HTTP inference request. A record is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.

Environment -> (map)

The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.

key -> (string)

value -> (string)

TransformInput -> (structure)

Describes the input source of a transform job and the way the transform job consumes it.

DataSource -> (structure)

Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.

The following values are compatible: `ManifestFile` , `S3Prefix`

The following value is not compatible: `AugmentedManifestFile`

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/` .
- A manifest might look like this: `s3://bucketname/example.manifest`   The manifest is an S3 object which is a JSON file with the following format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   The preceding JSON matches the following `S3Uris` :   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.

ContentType -> (string)

The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.

CompressionType -> (string)

If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is `None` .

SplitType -> (string)

The method to use to split the transform jobâs data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for `SplitType` is `None` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to `Line` to split records on a newline character boundary. `SplitType` also supports a number of record-oriented binary data formats. Currently, the supported record formats are:

- RecordIO
- TFRecord

When splitting is enabled, the size of a mini-batch depends on the values of the `BatchStrategy` and `MaxPayloadInMB` parameters. When the value of `BatchStrategy` is `MultiRecord` , Amazon SageMaker sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. If the value of `BatchStrategy` is `SingleRecord` , Amazon SageMaker sends individual records in each request.

### Note

Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of `BatchStrategy` is set to `SingleRecord` . Padding is not removed if the value of `BatchStrategy` is set to `MultiRecord` .

For more information about `RecordIO` , see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/faq/recordio) in the MXNet documentation. For more information about `TFRecord` , see [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) in the TensorFlow documentation.

TransformOutput -> (structure)

Describes the results of a transform job.

S3OutputPath -> (string)

The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, `s3://bucket-name/key-name-prefix` .

For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at `s3://bucket-name/input-name-prefix/dataset01/data.csv` , batch transform stores the transformed data at `s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out` . Batch transform doesnât upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.

Accept -> (string)

The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.

AssembleWith -> (string)

Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify `None` . To add a newline character at the end of every transformed record, specify `Line` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

If you donât provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) request. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

DataCaptureConfig -> (structure)

Configuration to control how SageMaker captures inference data for batch transform jobs.

DestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

KmsKeyId -> (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the batch transform job.

The KmsKeyId can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

GenerateInferenceId -> (boolean)

Flag that indicates whether to append inference id to the output.

TransformResources -> (structure)

Describes the resources, including ML instance types and ML instance count, to use for transform job.

InstanceType -> (string)

The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large` instance types.

InstanceCount -> (integer)

The number of ML compute instances to use in the transform job. The default value is `1` , and the maximum is `100` . For distributed transform jobs, specify a value greater than `1` .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

TransformAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.

al2-ami-sagemaker-batch-gpu-470

- Accelerator: GPU
- NVIDIA driver version: 470

al2-ami-sagemaker-batch-gpu-535
- Accelerator: GPU
- NVIDIA driver version: 535

CreationTime -> (timestamp)

A timestamp that shows when the transform Job was created.

TransformStartTime -> (timestamp)

Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of `TransformEndTime` .

TransformEndTime -> (timestamp)

Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of `TransformStartTime` .

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the labeling job that created the transform job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of the AutoML job that created the transform job.

DataProcessing -> (structure)

The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html) .

InputFilter -> (string)

A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the input data to pass to the algorithm. Use the `InputFilter` parameter to exclude fields, such as an ID column, from the input. If you want SageMaker to pass the entire input dataset to the algorithm, accept the default value `$` .

Examples: `"$"` , `"$[1:]"` , `"$.features"`

OutputFilter -> (string)

A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the joined dataset to save in the output file for a batch transform job. If you want SageMaker to store the entire input dataset in the output file, leave the default value, `$` . If you specify indexes that arenât within the dimension size of the joined dataset, you get an error.

Examples: `"$"` , `"$[0,5:]"` , `"$['id','SageMakerOutput']"`

JoinSource -> (string)

Specifies the source of the data to join with the transformed data. The valid values are `None` and `Input` . The default value is `None` , which specifies not to join the input with the transformed data. If you want the batch transform job to join the original input data with the transformed data, set `JoinSource` to `Input` . You can specify `OutputFilter` as an additional filter to select a portion of the joined dataset and store it in the output file.

For JSON or JSONLines objects, such as a JSON array, SageMaker adds the transformed data to the input JSON object in an attribute called `SageMakerOutput` . The joined result for JSON must be a key-value pair object. If the input is not a key-value pair object, SageMaker creates a new JSON file. In the new JSON file, and the input data is stored under the `SageMakerInput` key and the results are stored in `SageMakerOutput` .

For CSV data, SageMaker takes each row as a JSON array and joins the transformed data with the input by appending each transformed row to the end of the input. The joined data has the original input data followed by the transformed data and the output is a CSV file.

For information on how joining in applied, see [Workflow for Associating Inferences with Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#batch-transform-data-processing-workflow) .

ExperimentConfig -> (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

Tags -> (list)

A list of tags associated with the transform job.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

LineageGroupArn -> (string)

The Amazon Resource Name (ARN) of the lineage group resource.

Tags -> (list)

The list of tags that are associated with the component. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Parents -> (list)

An array of the parents of the component. A parent is a trial the component is associated with and the experiment the trial is part of. A component might not have any parents.

(structure)

The trial that a trial component is associated with and the experiment the trial is part of. A component might not be associated with a trial. A component can be associated with multiple trials.

TrialName -> (string)

The name of the trial.

ExperimentName -> (string)

The name of the experiment.

RunName -> (string)

The name of the experiment run.

Endpoint -> (structure)

A hosted endpoint for real-time inference.

EndpointName -> (string)

The name of the endpoint.

EndpointArn -> (string)

The Amazon Resource Name (ARN) of the endpoint.

EndpointConfigName -> (string)

The endpoint configuration associated with the endpoint.

ProductionVariants -> (list)

A list of the production variants hosted on the endpoint. Each production variant is a model.

(structure)

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API and the endpoint status is `Updating` , you get different desired and current values.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight, as specified in the `UpdateEndpointWeightsAndCapacities` request.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in the `UpdateEndpointWeightsAndCapacities` request.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for the endpoint update.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.

DataCaptureConfig -> (structure)

The currently active data capture configuration used by your Endpoint.

EnableCapture -> (boolean)

Whether data capture is enabled or disabled.

CaptureStatus -> (string)

Whether data capture is currently functional.

CurrentSamplingPercentage -> (integer)

The percentage of requests being captured by your Endpoint.

DestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

KmsKeyId -> (string)

The KMS key being used to encrypt the data in Amazon S3.

EndpointStatus -> (string)

The status of the endpoint.

FailureReason -> (string)

If the endpoint failed, the reason it failed.

CreationTime -> (timestamp)

The time that the endpoint was created.

LastModifiedTime -> (timestamp)

The last time the endpoint was modified.

MonitoringSchedules -> (list)

A list of monitoring schedules for the endpoint. For information about model monitoring, see [Amazon SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) .

(structure)

A schedule for a model monitoring job. For information about model monitor, see [Amazon SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) .

MonitoringScheduleArn -> (string)

The Amazon Resource Name (ARN) of the monitoring schedule.

MonitoringScheduleName -> (string)

The name of the monitoring schedule.

MonitoringScheduleStatus -> (string)

The status of the monitoring schedule. This can be one of the following values.

- `PENDING` - The schedule is pending being created.
- `FAILED` - The schedule failed.
- `SCHEDULED` - The schedule was successfully created.
- `STOPPED` - The schedule was stopped.

MonitoringType -> (string)

The type of the monitoring job definition to schedule.

FailureReason -> (string)

If the monitoring schedule failed, the reason it failed.

CreationTime -> (timestamp)

The time that the monitoring schedule was created.

LastModifiedTime -> (timestamp)

The last time the monitoring schedule was changed.

MonitoringScheduleConfig -> (structure)

Configures the monitoring schedule and defines the monitoring job.

ScheduleConfig -> (structure)

Configures the monitoring schedule.

ScheduleExpression -> (string)

A cron expression that describes details about the monitoring schedule.

The supported cron expressions are:

- If you want to set the job to start every hour, use the following:  `Hourly: cron(0 * ? * * *)`
- If you want to start the job daily:  `cron(0 [00-23] ? * * *)`
- If you want to run the job one time, immediately, use the following keyword:  `NOW`

For example, the following are valid cron expressions:

- Daily at noon UTC: `cron(0 12 ? * * *)`
- Daily at midnight UTC: `cron(0 0 ? * * *)`

To support running every 6, 12 hours, the following are also supported:

`cron(0 [00-23]/[01-24] ? * * *)`

For example, the following are valid cron expressions:

- Every 12 hours, starting at 5pm UTC: `cron(0 17/12 ? * * *)`
- Every two hours starting at midnight: `cron(0 0/2 ? * * *)`

### Note

- Even though the cron expression is set to start at 5PM UTC, note that there could be a delay of 0-20 minutes from the actual requested time to run the execution.
- We recommend that if you would like a daily schedule, you do not provide this parameter. Amazon SageMaker AI will pick a time for running every day.

You can also specify the keyword `NOW` to run the monitoring job immediately, one time, without recurring.

DataAnalysisStartTime -> (string)

Sets the start time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to monitor the five hours of data in your dataset that precede the start of each monitoring job, you would specify: `"-PT5H"` .

The start time that you specify must not precede the end time that you specify by more than 24 hours. You specify the end time with the `DataAnalysisEndTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

DataAnalysisEndTime -> (string)

Sets the end time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to end the window one hour before the start of each monitoring job, you would specify: `"-PT1H"` .

The end time that you specify must not follow the start time that you specify by more than 24 hours. You specify the start time with the `DataAnalysisStartTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

MonitoringJobDefinition -> (structure)

Defines the monitoring job.

BaselineConfig -> (structure)

Baseline configuration used to validate that the data conforms to the specified constraints and statistics

BaseliningJobName -> (string)

The name of the job that performs baselining for the monitoring job.

ConstraintsResource -> (structure)

The baseline constraint file in Amazon S3 that the current monitoring job should validated against.

S3Uri -> (string)

The Amazon S3 URI for the constraints resource.

StatisticsResource -> (structure)

The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.

S3Uri -> (string)

The Amazon S3 URI for the statistics resource.

MonitoringInputs -> (list)

The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.

(structure)

The inputs for a monitoring job.

EndpointInput -> (structure)

The endpoint for a monitoring job.

EndpointName -> (string)

An endpoint in customerâs account which has enabled `DataCaptureConfig` enabled.

LocalPath -> (string)

Path to the filesystem where the endpoint data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs substract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

BatchTransformInput -> (structure)

Input object for the batch transform job.

DataCapturedDestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

DatasetFormat -> (structure)

The dataset format for your batch transform job.

Csv -> (structure)

The CSV dataset used in the monitoring job.

Header -> (boolean)

Indicates if the CSV data has a header.

Json -> (structure)

The JSON dataset used in the monitoring job

Line -> (boolean)

Indicates if the file should be read as a JSON object per line.

Parquet -> (structure)

The Parquet dataset used in the monitoring job

LocalPath -> (string)

Path to the filesystem where the batch transform data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

MonitoringOutputConfig -> (structure)

The array of outputs from the monitoring job to be uploaded to Amazon S3.

MonitoringOutputs -> (list)

Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.

(structure)

The output object for a monitoring job.

S3Output -> (structure)

The Amazon S3 storage location where the results of a monitoring job are saved.

S3Uri -> (string)

A URI that identifies the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job.

LocalPath -> (string)

The local path to the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job. LocalPath is an absolute path for the output data.

S3UploadMode -> (string)

Whether to upload the results of the monitoring job continuously or after the job completes.

KmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

MonitoringResources -> (structure)

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.

ClusterConfig -> (structure)

The configuration for the cluster resources used to run the processing job.

InstanceCount -> (integer)

The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.

InstanceType -> (string)

The ML compute instance type for the processing job.

VolumeSizeInGB -> (integer)

The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.

VolumeKmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.

MonitoringAppSpecification -> (structure)

Configures the monitoring job to run a specified Docker container image.

ImageUri -> (string)

The container image to be run by the monitoring job.

ContainerEntrypoint -> (list)

Specifies the entrypoint for a container used to run the monitoring job.

(string)

ContainerArguments -> (list)

An array of arguments for the container used to run the monitoring job.

(string)

RecordPreprocessorSourceUri -> (string)

An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.

PostAnalyticsProcessorSourceUri -> (string)

An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.

StoppingCondition -> (structure)

Specifies a time limit for how long the monitoring job is allowed to run.

MaxRuntimeInSeconds -> (integer)

The maximum runtime allowed in seconds.

### Note

The `MaxRuntimeInSeconds` cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.

Environment -> (map)

Sets the environment variables in the Docker container.

key -> (string)

value -> (string)

NetworkConfig -> (structure)

Specifies networking options for an monitoring job.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the processing job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job definition to schedule.

MonitoringType -> (string)

The type of the monitoring job definition to schedule.

EndpointName -> (string)

The endpoint that hosts the model being monitored.

LastMonitoringExecutionSummary -> (structure)

Summary of information about the last monitoring job to run.

MonitoringScheduleName -> (string)

The name of the monitoring schedule.

ScheduledTime -> (timestamp)

The time the monitoring job was scheduled.

CreationTime -> (timestamp)

The time at which the monitoring job was created.

LastModifiedTime -> (timestamp)

A timestamp that indicates the last time the monitoring job was modified.

MonitoringExecutionStatus -> (string)

The status of the monitoring job.

ProcessingJobArn -> (string)

The Amazon Resource Name (ARN) of the monitoring job.

EndpointName -> (string)

The name of the endpoint used to run the monitoring job.

FailureReason -> (string)

Contains the reason a monitoring job failed, if it failed.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job.

MonitoringType -> (string)

The type of the monitoring job.

Tags -> (list)

A list of the tags associated with the monitoring schedlue. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Tags -> (list)

A list of the tags associated with the endpoint. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

ShadowProductionVariants -> (list)

A list of the shadow variants hosted on the endpoint. Each shadow variant is a model in shadow mode with production traffic replicated from the production variant.

(structure)

Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the `UpdateEndpointWeightsAndCapacities` API and the endpoint status is `Updating` , you get different desired and current values.

VariantName -> (string)

The name of the variant.

DeployedImages -> (list)

An array of `DeployedImage` objects that specify the Amazon EC2 Container Registry paths of the inference images deployed on instances of this `ProductionVariant` .

(structure)

Gets the Amazon EC2 Container Registry path of the docker image of the model that is hosted in this [ProductionVariant](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariant.html) .

If you used the `registry/repository[:tag]` form to specify the image path of the primary container when you created the model hosted in this `ProductionVariant` , the path resolves to a path of the form `registry/repository[@digest]` . A digest is a hash value that identifies a specific version of an image. For information about Amazon ECR paths, see [Pulling an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

SpecifiedImage -> (string)

The image path you specified when you created the model.

ResolvedImage -> (string)

The specific digest path of the image hosted in this `ProductionVariant` .

ResolutionTime -> (timestamp)

The date and time when the image path for the model resolved to the `ResolvedImage`

CurrentWeight -> (float)

The weight associated with the variant.

DesiredWeight -> (float)

The requested weight, as specified in the `UpdateEndpointWeightsAndCapacities` request.

CurrentInstanceCount -> (integer)

The number of instances associated with the variant.

DesiredInstanceCount -> (integer)

The number of instances requested in the `UpdateEndpointWeightsAndCapacities` request.

VariantStatus -> (list)

The endpoint variant status which describes the current deployment stage status or operational status.

(structure)

Describes the status of the production variant.

Status -> (string)

The endpoint variant status which describes the current deployment stage status or operational status.

- `Creating` : Creating inference resources for the production variant.
- `Deleting` : Terminating inference resources for the production variant.
- `Updating` : Updating capacity for the production variant.
- `ActivatingTraffic` : Turning on traffic for the production variant.
- `Baking` : Waiting period to monitor the CloudWatch alarms in the automatic rollback configuration.

StatusMessage -> (string)

A message that describes the status of the production variant.

StartTime -> (timestamp)

The start time of the current status change.

CurrentServerlessConfig -> (structure)

The serverless configuration for the endpoint.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

DesiredServerlessConfig -> (structure)

The serverless configuration requested for the endpoint update.

MemorySizeInMB -> (integer)

The memory size of your serverless endpoint. Valid values are in 1 GB increments: 1024 MB, 2048 MB, 3072 MB, 4096 MB, 5120 MB, or 6144 MB.

MaxConcurrency -> (integer)

The maximum number of concurrent invocations your serverless endpoint can process.

ProvisionedConcurrency -> (integer)

The amount of provisioned concurrency to allocate for the serverless endpoint. Should be less than or equal to `MaxConcurrency` .

### Note

This field is not supported for serverless endpoint recommendations for Inference Recommender jobs. For more information about creating an Inference Recommender job, see [CreateInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html) .

ManagedInstanceScaling -> (structure)

Settings that control the range in the number of instances that the endpoint provisions as it scales up or down to accommodate traffic.

Status -> (string)

Indicates whether managed instance scaling is enabled.

MinInstanceCount -> (integer)

The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.

MaxInstanceCount -> (integer)

The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.

RoutingConfig -> (structure)

Settings that control how the endpoint routes incoming traffic to the instances that the endpoint hosts.

RoutingStrategy -> (string)

Sets how the endpoint routes incoming traffic:

- `LEAST_OUTSTANDING_REQUESTS` : The endpoint routes requests to the specific instances that have more capacity to process them.
- `RANDOM` : The endpoint routes each request to a randomly chosen instance.

ModelPackage -> (structure)

A container for your trained model that can be deployed for SageMaker inference. This can include inference code, artifacts, and metadata. The model package type can be one of the following.

- Versioned model: A part of a model package group in Model Registry.
- Unversioned model: Not part of a model package group and used in Amazon Web Services Marketplace.

For more information, see ` `CreateModelPackage` [https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage).html`__ .

ModelPackageName -> (string)

The name of the model package. The name can be as follows:

- For a versioned model, the name is automatically generated by SageMaker Model Registry and follows the format â`ModelPackageGroupName/ModelPackageVersion` â.
- For an unversioned model, you must provide the name.

ModelPackageGroupName -> (string)

The model group to which the model belongs.

ModelPackageVersion -> (integer)

The version number of a versioned model.

ModelPackageArn -> (string)

The Amazon Resource Name (ARN) of the model package.

ModelPackageDescription -> (string)

The description of the model package.

CreationTime -> (timestamp)

The time that the model package was created.

InferenceSpecification -> (structure)

Defines how to perform inference generation after a training job is run.

Containers -> (list)

The Amazon ECR registry path of the Docker image that contains the inference code.

(structure)

Describes the Docker container for the model package.

ContainerHostname -> (string)

The DNS host name for the Docker container.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.

If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

ImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model package.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ProductId -> (string)

The Amazon Web Services Marketplace product ID of the model package.

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

ModelInput -> (structure)

A structure with Model Input details.

DataInputConfig -> (string)

The input configuration object for the model.

Framework -> (string)

The machine learning framework of the model package container image.

FrameworkVersion -> (string)

The framework version of the Model Package Container Image.

NearestModelName -> (string)

The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata` .

AdditionalS3DataSource -> (structure)

The additional data source that is used during inference in the Docker container for your model package.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

SupportedTransformInstanceTypes -> (list)

A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedRealtimeInferenceInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

This parameter is required for unversioned models, and optional for versioned models.

(string)

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

SourceAlgorithmSpecification -> (structure)

A list of algorithms that were used to create a model package.

SourceAlgorithms -> (list)

A list of the algorithms that were used to create a model package.

(structure)

Specifies an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in Amazon Web Services Marketplace that you are subscribed to.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same Amazon Web Services region as the algorithm.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

AlgorithmName -> (string)

The name of an algorithm that was used to create the model package. The algorithm must be either an algorithm resource in your SageMaker account or an algorithm in Amazon Web Services Marketplace that you are subscribed to.

ValidationSpecification -> (structure)

Specifies batch transform jobs that SageMaker runs to validate your model package.

ValidationRole -> (string)

The IAM roles to be used for the validation of the model package.

ValidationProfiles -> (list)

An array of `ModelPackageValidationProfile` objects, each of which specifies a batch transform job that SageMaker runs to validate your model package.

(structure)

Contains data, such as the inputs and targeted instance types that are used in the process of validating the model package.

The data provided in the validation profile is made available to your buyers on Amazon Web Services Marketplace.

ProfileName -> (string)

The name of the profile for the model package.

TransformJobDefinition -> (structure)

The `TransformJobDefinition` object that describes the transform job used for the validation of the model package.

MaxConcurrentTransforms -> (integer)

The maximum number of parallel requests that can be sent to each instance in a transform job. The default value is 1.

MaxPayloadInMB -> (integer)

The maximum payload size allowed, in MB. A payload is the data portion of a record (without metadata).

BatchStrategy -> (string)

A string that determines the number of records included in a single mini-batch.

`SingleRecord` means only one record is used per mini-batch. `MultiRecord` means a mini-batch is set to contain as many records that can fit within the `MaxPayloadInMB` limit.

Environment -> (map)

The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.

key -> (string)

value -> (string)

TransformInput -> (structure)

A description of the input source and the way the transform job consumes it.

DataSource -> (structure)

Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.

The following values are compatible: `ManifestFile` , `S3Prefix`

The following value is not compatible: `AugmentedManifestFile`

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/` .
- A manifest might look like this: `s3://bucketname/example.manifest`   The manifest is an S3 object which is a JSON file with the following format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   The preceding JSON matches the following `S3Uris` :   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.

ContentType -> (string)

The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.

CompressionType -> (string)

If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is `None` .

SplitType -> (string)

The method to use to split the transform jobâs data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for `SplitType` is `None` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to `Line` to split records on a newline character boundary. `SplitType` also supports a number of record-oriented binary data formats. Currently, the supported record formats are:

- RecordIO
- TFRecord

When splitting is enabled, the size of a mini-batch depends on the values of the `BatchStrategy` and `MaxPayloadInMB` parameters. When the value of `BatchStrategy` is `MultiRecord` , Amazon SageMaker sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. If the value of `BatchStrategy` is `SingleRecord` , Amazon SageMaker sends individual records in each request.

### Note

Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of `BatchStrategy` is set to `SingleRecord` . Padding is not removed if the value of `BatchStrategy` is set to `MultiRecord` .

For more information about `RecordIO` , see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/faq/recordio) in the MXNet documentation. For more information about `TFRecord` , see [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) in the TensorFlow documentation.

TransformOutput -> (structure)

Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.

S3OutputPath -> (string)

The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, `s3://bucket-name/key-name-prefix` .

For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at `s3://bucket-name/input-name-prefix/dataset01/data.csv` , batch transform stores the transformed data at `s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out` . Batch transform doesnât upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.

Accept -> (string)

The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.

AssembleWith -> (string)

Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify `None` . To add a newline character at the end of every transformed record, specify `Line` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

If you donât provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) request. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

TransformResources -> (structure)

Identifies the ML compute instances for the transform job.

InstanceType -> (string)

The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large` instance types.

InstanceCount -> (integer)

The number of ML compute instances to use in the transform job. The default value is `1` , and the maximum is `100` . For distributed transform jobs, specify a value greater than `1` .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

TransformAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.

al2-ami-sagemaker-batch-gpu-470

- Accelerator: GPU
- NVIDIA driver version: 470

al2-ami-sagemaker-batch-gpu-535
- Accelerator: GPU
- NVIDIA driver version: 535

ModelPackageStatus -> (string)

The status of the model package. This can be one of the following values.

- `PENDING` - The model package is pending being created.
- `IN_PROGRESS` - The model package is in the process of being created.
- `COMPLETED` - The model package was successfully created.
- `FAILED` - The model package failed.
- `DELETING` - The model package is in the process of being deleted.

ModelPackageStatusDetails -> (structure)

Specifies the validation and image scan statuses of the model package.

ValidationStatuses -> (list)

The validation status of the model package.

(structure)

Represents the overall status of a model package.

Name -> (string)

The name of the model package for which the overall status is being reported.

Status -> (string)

The current status.

FailureReason -> (string)

if the overall status is `Failed` , the reason for the failure.

ImageScanStatuses -> (list)

The status of the scan of the Docker image container for the model package.

(structure)

Represents the overall status of a model package.

Name -> (string)

The name of the model package for which the overall status is being reported.

Status -> (string)

The current status.

FailureReason -> (string)

if the overall status is `Failed` , the reason for the failure.

CertifyForMarketplace -> (boolean)

Whether the model package is to be certified to be listed on Amazon Web Services Marketplace. For information about listing model packages on Amazon Web Services Marketplace, see [List Your Algorithm or Model Package on Amazon Web Services Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-mkt-list.html) .

ModelApprovalStatus -> (string)

The approval status of the model. This can be one of the following values.

- `APPROVED` - The model is approved
- `REJECTED` - The model is rejected.
- `PENDING_MANUAL_APPROVAL` - The model is waiting for manual approval.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, or project.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

MetadataProperties -> (structure)

Metadata properties of the tracking entity, trial, or trial component.

CommitId -> (string)

The commit ID.

Repository -> (string)

The repository.

GeneratedBy -> (string)

The entity this entity was generated by.

ProjectId -> (string)

The project ID.

ModelMetrics -> (structure)

Metrics for the model.

ModelQuality -> (structure)

Metrics that measure the quality of a model.

Statistics -> (structure)

Model quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

Model quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ModelDataQuality -> (structure)

Metrics that measure the quality of the input data for a model.

Statistics -> (structure)

Data quality statistics for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

Data quality constraints for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Bias -> (structure)

Metrics that measure bias in a model.

Report -> (structure)

The bias report for a model

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PreTrainingReport -> (structure)

The pre-training bias report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PostTrainingReport -> (structure)

The post-training bias report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Explainability -> (structure)

Metrics that help explain a model.

Report -> (structure)

The explainability report for a model.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

LastModifiedTime -> (timestamp)

The last time the model package was modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, or project.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

ApprovalDescription -> (string)

A description provided when the model approval is set.

Domain -> (string)

The machine learning domain of your model package and its components. Common machine learning domains include computer vision and natural language processing.

Task -> (string)

The machine learning task your model package accomplishes. Common machine learning tasks include object detection and image classification.

SamplePayloadUrl -> (string)

The Amazon Simple Storage Service path where the sample payload are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).

AdditionalInferenceSpecifications -> (list)

An array of additional Inference Specification objects.

(structure)

A structure of additional Inference Specification. Additional Inference Specification specifies details about inference jobs that can be run with models based on this model package

Name -> (string)

A unique name to identify the additional inference specification. The name must be unique within the list of your additional inference specifications for a particular model package.

Description -> (string)

A description of the additional Inference specification

Containers -> (list)

The Amazon ECR registry path of the Docker image that contains the inference code.

(structure)

Describes the Docker container for the model package.

ContainerHostname -> (string)

The DNS host name for the Docker container.

Image -> (string)

The Amazon Elastic Container Registry (Amazon ECR) path where inference code is stored.

If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

ImageDigest -> (string)

An MD5 hash of the training algorithm that identifies the Docker image used for training.

ModelDataUrl -> (string)

The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single `gzip` compressed tar archive (`.tar.gz` suffix).

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model package.

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy during endpoint creation.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

ProductId -> (string)

The Amazon Web Services Marketplace product ID of the model package.

Environment -> (map)

The environment variables to set in the Docker container. Each key and value in the `Environment` string to string map can have length of up to 1024. We support up to 16 entries in the map.

key -> (string)

value -> (string)

ModelInput -> (structure)

A structure with Model Input details.

DataInputConfig -> (string)

The input configuration object for the model.

Framework -> (string)

The machine learning framework of the model package container image.

FrameworkVersion -> (string)

The framework version of the Model Package Container Image.

NearestModelName -> (string)

The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model. You can find a list of benchmarked models by calling `ListModelMetadata` .

AdditionalS3DataSource -> (structure)

The additional data source that is used during inference in the Docker container for your model package.

S3DataType -> (string)

The data type of the additional data source that you specify for use in inference or training.

S3Uri -> (string)

The uniform resource identifier (URI) used to identify an additional data source used in inference or training.

CompressionType -> (string)

The type of compression used for an additional data source used in inference or training. Specify `None` if your additional data source is not compressed.

ETag -> (string)

The ETag associated with S3 URI.

ModelDataETag -> (string)

The ETag associated with Model Data URL.

SupportedTransformInstanceTypes -> (list)

A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.

(string)

SupportedRealtimeInferenceInstanceTypes -> (list)

A list of the instance types that are used to generate inferences in real-time.

(string)

SupportedContentTypes -> (list)

The supported MIME types for the input data.

(string)

SupportedResponseMIMETypes -> (list)

The supported MIME types for the output data.

(string)

SourceUri -> (string)

The URI of the source for the model package.

SecurityConfig -> (structure)

An optional Key Management Service key to encrypt, decrypt, and re-encrypt model package information for regulated workloads with highly sensitive data.

KmsKeyId -> (string)

The KMS Key ID (`KMSKeyId` ) used for encryption of model package information.

ModelCard -> (structure)

The model card associated with the model package. Since `ModelPackageModelCard` is tied to a model package, it is a specific usage of a model card and its schema is simplified compared to the schema of `ModelCard` . The `ModelPackageModelCard` schema does not include `model_package_details` , and `model_overview` is composed of the `model_creator` and `model_artifact` properties. For more information about the model package model card schema, see [Model package model card schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema) . For more information about the model card associated with the model package, see [View the Details of a Model Version](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html) .

ModelCardContent -> (string)

The content of the model card. The content must follow the schema described in [Model Package Model Card Schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-details.html#model-card-schema) .

ModelCardStatus -> (string)

The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.

- `Draft` : The model card is a work in progress.
- `PendingReview` : The model card is pending review.
- `Approved` : The model card is approved.
- `Archived` : The model card is archived. No more updates can be made to the model card content. If you try to update the model card content, you will receive the message `Model Card is in Archived state` .

ModelLifeCycle -> (structure)

A structure describing the current state of the model in its life cycle.

Stage -> (string)

The current stage in the model life cycle.

StageStatus -> (string)

The current status of a stage in model life cycle.

StageDescription -> (string)

Describes the stage related details.

Tags -> (list)

A list of the tags associated with the model package. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

CustomerMetadataProperties -> (map)

The metadata properties for the model package.

key -> (string)

value -> (string)

DriftCheckBaselines -> (structure)

Represents the drift check baselines that can be used when the model monitor is set using the model package.

Bias -> (structure)

Represents the drift check bias baselines that can be used when the model monitor is set using the model package.

ConfigFile -> (structure)

The bias config file for a model.

ContentType -> (string)

The type of content stored in the file source.

ContentDigest -> (string)

The digest of the file source.

S3Uri -> (string)

The Amazon S3 URI for the file source.

PreTrainingConstraints -> (structure)

The pre-training constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

PostTrainingConstraints -> (structure)

The post-training constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Explainability -> (structure)

Represents the drift check explainability baselines that can be used when the model monitor is set using the model package.

Constraints -> (structure)

The drift check explainability constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ConfigFile -> (structure)

The explainability config file for the model.

ContentType -> (string)

The type of content stored in the file source.

ContentDigest -> (string)

The digest of the file source.

S3Uri -> (string)

The Amazon S3 URI for the file source.

ModelQuality -> (structure)

Represents the drift check model quality baselines that can be used when the model monitor is set using the model package.

Statistics -> (structure)

The drift check model quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

The drift check model quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

ModelDataQuality -> (structure)

Represents the drift check model data quality baselines that can be used when the model monitor is set using the model package.

Statistics -> (structure)

The drift check model data quality statistics.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

Constraints -> (structure)

The drift check model data quality constraints.

ContentType -> (string)

The metric source content type.

ContentDigest -> (string)

The hash key used for the metrics source.

S3Uri -> (string)

The S3 URI for the metrics source.

SkipModelValidation -> (string)

Indicates if you want to skip model validation.

ModelPackageGroup -> (structure)

A group of versioned models in the Model Registry.

ModelPackageGroupName -> (string)

The name of the model group.

ModelPackageGroupArn -> (string)

The Amazon Resource Name (ARN) of the model group.

ModelPackageGroupDescription -> (string)

The description for the model group.

CreationTime -> (timestamp)

The time that the model group was created.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

ModelPackageGroupStatus -> (string)

The status of the model group. This can be one of the following values.

- `PENDING` - The model group is pending being created.
- `IN_PROGRESS` - The model group is in the process of being created.
- `COMPLETED` - The model group was successfully created.
- `FAILED` - The model group failed.
- `DELETING` - The model group is in the process of being deleted.
- `DELETE_FAILED` - SageMaker failed to delete the model group.

Tags -> (list)

A list of the tags associated with the model group. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

Pipeline -> (structure)

A SageMaker Model Building Pipeline instance.

PipelineArn -> (string)

The Amazon Resource Name (ARN) of the pipeline.

PipelineName -> (string)

The name of the pipeline.

PipelineDisplayName -> (string)

The display name of the pipeline.

PipelineDescription -> (string)

The description of the pipeline.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role that created the pipeline.

PipelineStatus -> (string)

The status of the pipeline.

CreationTime -> (timestamp)

The creation time of the pipeline.

LastModifiedTime -> (timestamp)

The time that the pipeline was last modified.

LastRunTime -> (timestamp)

The time when the pipeline was last run.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

ParallelismConfiguration -> (structure)

The parallelism configuration applied to the pipeline.

MaxParallelExecutionSteps -> (integer)

The max number of steps that can be executed in parallel.

Tags -> (list)

A list of tags that apply to the pipeline.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

PipelineExecution -> (structure)

An execution of a pipeline.

PipelineArn -> (string)

The Amazon Resource Name (ARN) of the pipeline that was executed.

PipelineExecutionArn -> (string)

The Amazon Resource Name (ARN) of the pipeline execution.

PipelineExecutionDisplayName -> (string)

The display name of the pipeline execution.

PipelineExecutionStatus -> (string)

The status of the pipeline status.

PipelineExecutionDescription -> (string)

The description of the pipeline execution.

PipelineExperimentConfig -> (structure)

Specifies the names of the experiment and trial created by a pipeline.

ExperimentName -> (string)

The name of the experiment.

TrialName -> (string)

The name of the trial.

FailureReason -> (string)

If the execution failed, a message describing why.

CreationTime -> (timestamp)

The creation time of the pipeline execution.

LastModifiedTime -> (timestamp)

The time that the pipeline execution was last modified.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

ParallelismConfiguration -> (structure)

The parallelism configuration applied to the pipeline execution.

MaxParallelExecutionSteps -> (integer)

The max number of steps that can be executed in parallel.

SelectiveExecutionConfig -> (structure)

The selective execution configuration applied to the pipeline run.

SourcePipelineExecutionArn -> (string)

The ARN from a reference execution of the current pipeline. Used to copy input collaterals needed for the selected steps to run. The execution status of the pipeline can be either `Failed` or `Success` .

This field is required if the steps you specify for `SelectedSteps` depend on output collaterals from any non-specified pipeline steps. For more information, see [Selective Execution for Pipeline Steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-selective-ex.html) .

SelectedSteps -> (list)

A list of pipeline steps to run. All step(s) in all path(s) between two selected steps should be included.

(structure)

A step selected to run in selective execution mode.

StepName -> (string)

The name of the pipeline step.

PipelineParameters -> (list)

Contains a list of pipeline parameters. This list can be empty.

(structure)

Assigns a value to a named Pipeline parameter.

Name -> (string)

The name of the parameter to assign a value to. This parameter name must match a named parameter in the pipeline definition.

Value -> (string)

The literal value for the parameter.

FeatureGroup -> (structure)

Amazon SageMaker Feature Store stores features in a collection called Feature Group. A Feature Group can be visualized as a table which has rows, with a unique identifier for each row where each column in the table is a feature. In principle, a Feature Group is composed of features and values per features.

FeatureGroupArn -> (string)

The Amazon Resource Name (ARN) of a `FeatureGroup` .

FeatureGroupName -> (string)

The name of the `FeatureGroup` .

RecordIdentifierFeatureName -> (string)

The name of the `Feature` whose value uniquely identifies a `Record` defined in the `FeatureGroup` `FeatureDefinitions` .

EventTimeFeatureName -> (string)

The name of the feature that stores the `EventTime` of a Record in a `FeatureGroup` .

A `EventTime` is point in time when a new event occurs that corresponds to the creation or update of a `Record` in `FeatureGroup` . All `Records` in the `FeatureGroup` must have a corresponding `EventTime` .

FeatureDefinitions -> (list)

A list of `Feature` s. Each `Feature` must include a `FeatureName` and a `FeatureType` .

Valid `FeatureType` s are `Integral` , `Fractional` and `String` .

`FeatureName` s cannot be any of the following: `is_deleted` , `write_time` , `api_invocation_time` .

You can create up to 2,500 `FeatureDefinition` s per `FeatureGroup` .

(structure)

A list of features. You must include `FeatureName` and `FeatureType` . Valid feature `FeatureType` s are `Integral` , `Fractional` and `String` .

FeatureName -> (string)

The name of a feature. The type must be a string. `FeatureName` cannot be any of the following: `is_deleted` , `write_time` , `api_invocation_time` .

The name:

- Must start with an alphanumeric character.
- Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.

FeatureType -> (string)

The value type of a feature. Valid values are Integral, Fractional, or String.

CollectionType -> (string)

A grouping of elements where each element within the collection must have the same feature type (`String` , `Integral` , or `Fractional` ).

- `List` : An ordered collection of elements.
- `Set` : An unordered collection of unique elements.
- `Vector` : A specialized list that represents a fixed-size array of elements. The vector dimension is determined by you. Must have elements with fractional feature types.

CollectionConfig -> (tagged union structure)

Configuration for your collection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `VectorConfig`.

VectorConfig -> (structure)

Configuration for your vector collection type.

- `Dimension` : The number of elements in your vector.

Dimension -> (integer)

The number of elements in your vector.

CreationTime -> (timestamp)

The time a `FeatureGroup` was created.

LastModifiedTime -> (timestamp)

A timestamp indicating the last time you updated the feature group.

OnlineStoreConfig -> (structure)

Use this to specify the Amazon Web Services Key Management Service (KMS) Key ID, or `KMSKeyId` , for at rest data encryption. You can turn `OnlineStore` on or off by specifying the `EnableOnlineStore` flag at General Assembly.

The default value is `False` .

SecurityConfig -> (structure)

Use to specify KMS Key ID (`KMSKeyId` ) for at-rest encryption of your `OnlineStore` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) key ARN that SageMaker Feature Store uses to encrypt the Amazon S3 objects at rest using Amazon S3 server-side encryption.

The caller (either user or IAM role) of `CreateFeatureGroup` must have below permissions to the `OnlineStore` `KmsKeyId` :

- `"kms:Encrypt"`
- `"kms:Decrypt"`
- `"kms:DescribeKey"`
- `"kms:CreateGrant"`
- `"kms:RetireGrant"`
- `"kms:ReEncryptFrom"`
- `"kms:ReEncryptTo"`
- `"kms:GenerateDataKey"`
- `"kms:ListAliases"`
- `"kms:ListGrants"`
- `"kms:RevokeGrant"`

The caller (either user or IAM role) to all DataPlane operations (`PutRecord` , `GetRecord` , `DeleteRecord` ) must have the following permissions to the `KmsKeyId` :

- `"kms:Decrypt"`

EnableOnlineStore -> (boolean)

Turn `OnlineStore` off by specifying `False` for the `EnableOnlineStore` flag. Turn `OnlineStore` on by specifying `True` for the `EnableOnlineStore` flag.

The default value is `False` .

TtlDuration -> (structure)

Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` + `TtlDuration` . For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.

Unit -> (string)

`TtlDuration` time unit.

Value -> (integer)

`TtlDuration` time value.

StorageType -> (string)

Option for different tiers of low latency storage for real-time data retrieval.

- `Standard` : A managed low latency data store for feature groups.
- `InMemory` : A managed data store for feature groups that supports very low latency retrieval.

OfflineStoreConfig -> (structure)

The configuration of an `OfflineStore` .

Provide an `OfflineStoreConfig` in a request to `CreateFeatureGroup` to create an `OfflineStore` .

To encrypt an `OfflineStore` using at rest data encryption, specify Amazon Web Services Key Management Service (KMS) key ID, or `KMSKeyId` , in `S3StorageConfig` .

S3StorageConfig -> (structure)

The Amazon Simple Storage (Amazon S3) location of `OfflineStore` .

S3Uri -> (string)

The S3 URI, or location in Amazon S3, of `OfflineStore` .

S3 URIs have a format similar to the following: `s3://example-bucket/prefix/` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (KMS) key ARN of the key used to encrypt any objects written into the `OfflineStore` S3 location.

The IAM `roleARN` that is passed as a parameter to `CreateFeatureGroup` must have below permissions to the `KmsKeyId` :

- `"kms:GenerateDataKey"`

ResolvedOutputS3Uri -> (string)

The S3 path where offline records are written.

DisableGlueTableCreation -> (boolean)

Set to `True` to disable the automatic creation of an Amazon Web Services Glue table when configuring an `OfflineStore` . If set to `False` , Feature Store will name the `OfflineStore` Glue table following [Athenaâs naming recommendations](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html) .

The default value is `False` .

DataCatalogConfig -> (structure)

The meta data of the Glue table that is autogenerated when an `OfflineStore` is created.

TableName -> (string)

The name of the Glue table.

Catalog -> (string)

The name of the Glue table catalog.

Database -> (string)

The name of the Glue table database.

TableFormat -> (string)

Format for the offline store table. Supported formats are Glue (Default) and [Apache Iceberg](https://iceberg.apache.org/) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM execution role used to create the feature group.

FeatureGroupStatus -> (string)

A `FeatureGroup` status.

OfflineStoreStatus -> (structure)

The status of `OfflineStore` .

Status -> (string)

An `OfflineStore` status.

BlockedReason -> (string)

The justification for why the OfflineStoreStatus is Blocked (if applicable).

LastUpdateStatus -> (structure)

A value that indicates whether the feature group was updated successfully.

Status -> (string)

A value that indicates whether the update was made successful.

FailureReason -> (string)

If the update wasnât successful, indicates the reason why it failed.

FailureReason -> (string)

The reason that the `FeatureGroup` failed to be replicated in the `OfflineStore` . This is failure may be due to a failure to create a `FeatureGroup` in or delete a `FeatureGroup` from the `OfflineStore` .

Description -> (string)

A free form description of a `FeatureGroup` .

Tags -> (list)

Tags used to define a `FeatureGroup` .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

FeatureMetadata -> (structure)

The feature metadata used to search through the features.

FeatureGroupArn -> (string)

The Amazon Resource Number (ARN) of the feature group.

FeatureGroupName -> (string)

The name of the feature group containing the feature.

FeatureName -> (string)

The name of feature.

FeatureType -> (string)

The data type of the feature.

CreationTime -> (timestamp)

A timestamp indicating when the feature was created.

LastModifiedTime -> (timestamp)

A timestamp indicating when the feature was last modified.

Description -> (string)

An optional description that you specify to better describe the feature.

Parameters -> (list)

Optional key-value pairs that you specify to better describe the feature.

(structure)

A key-value pair that you specify to describe the feature.

Key -> (string)

A key that must contain a value to describe the feature.

Value -> (string)

The value that belongs to a key.

Project -> (structure)

The properties of a project.

ProjectArn -> (string)

The Amazon Resource Name (ARN) of the project.

ProjectName -> (string)

The name of the project.

ProjectId -> (string)

The ID of the project.

ProjectDescription -> (string)

The description of the project.

ServiceCatalogProvisioningDetails -> (structure)

Details that you specify to provision a service catalog product. For information about service catalog, see [What is Amazon Web Services Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) .

ProductId -> (string)

The ID of the product to provision.

ProvisioningArtifactId -> (string)

The ID of the provisioning artifact.

PathId -> (string)

The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path.

ProvisioningParameters -> (list)

A list of key value pairs that you specify when you provision a product.

(structure)

A key value pair used when you provision a project as a service catalog product. For information, see [What is Amazon Web Services Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) .

Key -> (string)

The key that identifies a provisioning parameter.

Value -> (string)

The value of the provisioning parameter.

ServiceCatalogProvisionedProductDetails -> (structure)

Details of a provisioned service catalog product. For information about service catalog, see [What is Amazon Web Services Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) .

ProvisionedProductId -> (string)

The ID of the provisioned product.

ProvisionedProductStatusMessage -> (string)

The current status of the product.

- `AVAILABLE` - Stable state, ready to perform any operation. The most recent operation succeeded and completed.
- `UNDER_CHANGE` - Transitive state. Operations performed might not have valid results. Wait for an AVAILABLE status before performing operations.
- `TAINTED` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.
- `ERROR` - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.
- `PLAN_IN_PROGRESS` - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an AVAILABLE status before performing operations.

ProjectStatus -> (string)

The status of the project.

CreatedBy -> (structure)

Who created the project.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

CreationTime -> (timestamp)

A timestamp specifying when the project was created.

Tags -> (list)

An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

LastModifiedTime -> (timestamp)

A timestamp container for when the project was last modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

HyperParameterTuningJob -> (structure)

The properties of a hyperparameter tuning job.

HyperParameterTuningJobName -> (string)

The name of a hyperparameter tuning job.

HyperParameterTuningJobArn -> (string)

The Amazon Resource Name (ARN) of a hyperparameter tuning job.

HyperParameterTuningJobConfig -> (structure)

Configures a hyperparameter tuning job.

Strategy -> (string)

Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job it launches. For information about search strategies, see [How Hyperparameter Tuning Works](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) .

StrategyConfig -> (structure)

The configuration for the `Hyperband` optimization strategy. This parameter should be provided only if `Hyperband` is selected as the strategy for `HyperParameterTuningJobConfig` .

HyperbandStrategyConfig -> (structure)

The configuration for the object that specifies the `Hyperband` strategy. This parameter is only supported for the `Hyperband` selection for `Strategy` within the `HyperParameterTuningJobConfig` API.

MinResource -> (integer)

The minimum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. If the value for `MinResource` has not been reached, the training job is not stopped by `Hyperband` .

MaxResource -> (integer)

The maximum number of resources (such as epochs) that can be used by a training job launched by a hyperparameter tuning job. Once a job reaches the `MaxResource` value, it is stopped. If a value for `MaxResource` is not provided, and `Hyperband` is selected as the hyperparameter tuning strategy, `HyperbandTraining` attempts to infer `MaxResource` from the following keys (if present) in [StaticsHyperParameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters) :

- `epochs`
- `numepochs`
- `n-epochs`
- `n_epochs`
- `num_epochs`

If `HyperbandStrategyConfig` is unable to infer a value for `MaxResource` , it generates a validation error. The maximum value is 20,000 epochs. All metrics that correspond to an objective metric are used to derive [early stopping decisions](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html) . For [distributed](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html) training jobs, ensure that duplicate metrics are not printed in the logs across the individual nodes in a training job. If multiple nodes are publishing duplicate or incorrect metrics, training jobs may make an incorrect stopping decision and stop the job prematurely.

HyperParameterTuningJobObjective -> (structure)

The [HyperParameterTuningJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobObjective.html) specifies the objective metric used to evaluate the performance of training jobs launched by this tuning job.

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

ResourceLimits -> (structure)

The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training and parallel training jobs that can be used for this hyperparameter tuning job.

MaxNumberOfTrainingJobs -> (integer)

The maximum number of training jobs that a hyperparameter tuning job can launch.

MaxParallelTrainingJobs -> (integer)

The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.

MaxRuntimeInSeconds -> (integer)

The maximum time in seconds that a hyperparameter tuning job can run.

ParameterRanges -> (structure)

The [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html) object that specifies the ranges of hyperparameters that this tuning job searches over to find the optimal configuration for the highest model performance against your chosen objective metric.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

TrainingJobEarlyStoppingType -> (string)

Specifies whether to use early stopping for training jobs launched by the hyperparameter tuning job. Because the `Hyperband` strategy has its own advanced internal early stopping mechanism, `TrainingJobEarlyStoppingType` must be `OFF` to use `Hyperband` . This parameter can take on one of the following values (the default value is `OFF` ):

OFF

Training jobs launched by the hyperparameter tuning job do not use early stopping.

AUTO

SageMaker stops training jobs launched by the hyperparameter tuning job when they are unlikely to perform better than previously completed training jobs. For more information, see [Stop Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html) .

TuningJobCompletionCriteria -> (structure)

The tuning jobâs completion criteria.

TargetObjectiveMetricValue -> (float)

The value of the objective metric.

BestObjectiveNotImproving -> (structure)

A flag to stop your hyperparameter tuning job if model performance fails to improve as evaluated against an objective function.

MaxNumberOfTrainingJobsNotImproving -> (integer)

The number of training jobs that have failed to improve model performance by 1% or greater over prior training jobs as evaluated against an objective function.

ConvergenceDetected -> (structure)

A flag to top your hyperparameter tuning job if automatic model tuning (AMT) has detected that your model has converged as evaluated against your objective function.

CompleteOnConvergence -> (string)

A flag to stop a tuning job once AMT has detected that the job has converged.

RandomSeed -> (integer)

A value used to initialize a pseudo-random number generator. Setting a random seed and using the same seed later for the same tuning job will allow hyperparameter optimization to find more a consistent hyperparameter configuration between the two runs.

TrainingJobDefinition -> (structure)

Defines the training jobs launched by a hyperparameter tuning job.

DefinitionName -> (string)

The job definition name.

TuningObjective -> (structure)

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

HyperParameterRanges -> (structure)

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

### Note

The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges canât exceed the maximum number specified.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

StaticHyperParameters -> (map)

Specifies the values of hyperparameters that do not change for the tuning job.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

The [HyperParameterAlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html) object that specifies the resource algorithm to use for the training jobs that the tuning job launches.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see [Algorithms Provided by Amazon SageMaker: Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

TrainingInputMode -> (string)

The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

**Pipe mode**

If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.

**File mode**

If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.

You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.

For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training wonât be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.

**FastFile mode**

If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.

`FastFile` mode works best when the data is read sequentially. Augmented manifest files arenât supported. The startup time is lower when there are fewer files in the S3 bucket provided.

AlgorithmName -> (string)

The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for `TrainingImage` .

MetricDefinitions -> (list)

An array of [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html) objects that specify the metrics that the algorithm emits.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.

InputDataConfig -> (list)

An array of [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) objects that specify the input for the training jobs that the tuning job launches.

(structure)

A channel is a named input source that training algorithms can consume.

ChannelName -> (string)

The name of the channel.

DataSource -> (structure)

The location of the channel data.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.

If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channelâs input mode is `Pipe` .

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/`
- A manifest might look like this: `s3://bucketname/example.manifest`   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri` . Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets. The following code example shows a valid manifest format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   This JSON is equivalent to the following `S3Uri` list:  `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.

Your input bucket must be located in same Amazon Web Services region as your training job.

S3DataDistributionType -> (string)

If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated` .

If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.

Donât choose more ML compute instances for training than available S3 objects. If you do, some nodes wonât get any data and you will pay for nodes that arenât getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.

In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key` . If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File` ), this copies 1/*n* of the number of objects.

AttributeNames -> (list)

A list of one or more attribute names to use that are found in a specified augmented manifest file.

(string)

InstanceGroupNames -> (list)

A list of names of instance groups that get data from the S3 data source.

(string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.

HubContentArn -> (string)

The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.

FileSystemDataSource -> (structure)

The file system that is associated with a channel.

FileSystemId -> (string)

The file system id.

FileSystemAccessMode -> (string)

The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.

FileSystemType -> (string)

The file system type.

DirectoryPath -> (string)

The full path to the directory to associate with the channel.

ContentType -> (string)

The MIME type of the data.

CompressionType -> (string)

If training data is compressed, the compression type. The default value is `None` . `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.

RecordWrapperType -> (string)

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you donât need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format) .

In File mode, leave this field unset or set it to None.

InputMode -> (string)

(Optional) The input mode to use for the data channel in a training job. If you donât set a value for `InputMode` , SageMaker uses the value set for `TrainingInputMode` . Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training jobâs general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.

To use a model for incremental training, choose `File` input model.

ShuffleConfig -> (structure)

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType` , this shuffles the results of the S3 key prefix matches. If you use `ManifestFile` , the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile` , the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

Seed -> (long)

Determines the shuffling order in `ShuffleConfig` value.

VpcConfig -> (structure)

The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

OutputDataConfig -> (structure)

Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide* . If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone

The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob` , `CreateTransformJob` , or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

S3OutputPath -> (string)

Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

CompressionType -> (string)

The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.

ResourceConfig -> (structure)

The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.

Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

### Note

If you want to use hyperparameter optimization with instance type flexibility, use `HyperParameterTuningResourceConfig` instead.

InstanceType -> (string)

The ML compute instance type.

### Note

SageMaker Training on Amazon Elastic Compute Cloud (EC2) P4de instances is in preview release starting December 9th, 2022.

[Amazon EC2 P4de instances](http://aws.amazon.com/ec2/instance-types/p4/) (currently in preview) are powered by 8 NVIDIA A100 GPUs with 80GB high-performance HBM2e GPU memory, which accelerate the speed of training ML models that need to be trained on large datasets of high-resolution data. In this preview release, Amazon SageMaker supports ML training jobs on P4de instances (`ml.p4de.24xlarge` ) to reduce model training time. The `ml.p4de.24xlarge` instances are available in the following Amazon Web Services Regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)

To request quota limit increase and start using P4de instances, contact the SageMaker Training service team through your account team.

InstanceCount -> (integer)

The number of ML compute instances to use. For distributed training, provide a value greater than 1.

VolumeSizeInGB -> (integer)

The size of the ML storage volume that you want to provision.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.

When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes) , SageMaker doesnât provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instanceâs storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d` , `ml.g4dn` , and `ml.g5` .

When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2` .

To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html) .

VolumeKmsKeyId -> (string)

The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be in any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

KeepAlivePeriodInSeconds -> (integer)

The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.

InstanceGroups -> (list)

The configuration of a heterogeneous cluster in JSON format.

(structure)

Defines an instance group for heterogeneous cluster training. When requesting a training job using the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API, you can configure multiple instance groups .

InstanceType -> (string)

Specifies the instance type of the instance group.

InstanceCount -> (integer)

Specifies the number of instances of the instance group.

InstanceGroupName -> (string)

Specifies the name of the instance group.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.

HyperParameterTuningResourceConfig -> (structure)

The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose `File` for `TrainingInputMode` in the `AlgorithmSpecification` parameter to additionally store training data in the storage volume (optional).

InstanceType -> (string)

The instance type used to run hyperparameter optimization tuning jobs. See [descriptions of instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) for more information.

InstanceCount -> (integer)

The number of compute instances of type `InstanceType` to use. For [distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) , select a value greater than 1.

VolumeSizeInGB -> (integer)

The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for `InstanceConfigs` is also specified.

Some instance types have a fixed total local storage size. If you select one of these instances for training, `VolumeSizeInGB` cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) .

### Note

SageMaker supports only the [General Purpose SSD (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) storage volume type.

VolumeKmsKeyId -> (string)

A key used by Amazon Web Services Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.

KMS Key ID:

`"1234abcd-12ab-34cd-56ef-1234567890ab"`

Amazon Resource Name (ARN) of a KMS key:

`"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

Some instances use local storage, which use a [hardware module to encrypt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) storage volumes. If you choose one of these instance types, you cannot request a `VolumeKmsKeyId` . For a list of instance types that use local storage, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) . For more information about Amazon Web Services Key Management Service, see [KMS encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html) for more information.

AllocationStrategy -> (string)

The strategy that determines the order of preference for resources specified in `InstanceConfigs` used in hyperparameter optimization.

InstanceConfigs -> (list)

A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The `AllocationStrategy` controls the order in which multiple configurations provided in `InstanceConfigs` are used.

### Note

If you only want to use a single instance configuration inside the `HyperParameterTuningResourceConfig` API, do not provide a value for `InstanceConfigs` . Instead, use `InstanceType` , `VolumeSizeInGB` and `InstanceCount` . If you use `InstanceConfigs` , do not provide values for `InstanceType` , `VolumeSizeInGB` or `InstanceCount` .

(structure)

The configuration for hyperparameter tuning resources for use in training jobs launched by the tuning job. These resources include compute instances and storage volumes. Specify one or more compute instance configurations and allocation strategies to select resources (optional).

InstanceType -> (string)

The instance type used for processing of hyperparameter optimization jobs. Choose from general purpose (no GPUs) instance types: ml.m5.xlarge, ml.m5.2xlarge, and ml.m5.4xlarge or compute optimized (no GPUs) instance types: ml.c5.xlarge and ml.c5.2xlarge. For more information about instance types, see [instance type descriptions](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) .

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` . Choose an instance count larger than 1 for distributed training algorithms. See [Step 2: Launch a SageMaker Distributed Training Job Using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) for more information.

VolumeSizeInGB -> (integer)

The volume size in GB of the data to be processed for hyperparameter optimization (optional).

StoppingCondition -> (structure)

Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

EnableNetworkIsolation -> (boolean)

Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

A Boolean indicating whether managed spot training is enabled (`True` ) or not (`False` ).

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Environment -> (map)

An environment variable that you can pass into the SageMaker [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. You can use an existing [environment variable from the training container](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment) or use your own. See [Define metrics and variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) for more information.

### Note

The maximum number of items specified for `Map Entries` refers to the maximum number of environment variables for each `TrainingJobDefinition` and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions canât exceed the maximum number specified.

key -> (string)

value -> (string)

TrainingJobDefinitions -> (list)

The job definitions included in a hyperparameter tuning job.

(structure)

Defines the training jobs launched by a hyperparameter tuning job.

DefinitionName -> (string)

The job definition name.

TuningObjective -> (structure)

Defines the objective metric for a hyperparameter tuning job. Hyperparameter tuning uses the value of this metric to evaluate the training jobs it launches, and returns the training job that results in either the highest or lowest value for this metric, depending on the value you specify for the `Type` parameter. If you want to define a custom objective metric, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Type -> (string)

Whether to minimize or maximize the objective metric.

MetricName -> (string)

The name of the metric to use for the objective metric.

HyperParameterRanges -> (structure)

Specifies ranges of integer, continuous, and categorical hyperparameters that a hyperparameter tuning job searches. The hyperparameter tuning job launches training jobs with hyperparameter values within these ranges to find the combination of values that result in the training job with the best performance as measured by the objective metric of the hyperparameter tuning job.

### Note

The maximum number of items specified for `Array Members` refers to the maximum number of hyperparameters for each range and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of hyperparameters for all the ranges canât exceed the maximum number specified.

IntegerParameterRanges -> (list)

The array of [IntegerParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IntegerParameterRange.html) objects that specify ranges of integer hyperparameters that a hyperparameter tuning job searches.

(structure)

For a hyperparameter of the integer type, specifies the range that a hyperparameter tuning job searches.

Name -> (string)

The name of the hyperparameter to search.

MinValue -> (string)

The minimum value of the hyperparameter to search.

MaxValue -> (string)

The maximum value of the hyperparameter to search.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ContinuousParameterRanges -> (list)

The array of [ContinuousParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContinuousParameterRange.html) objects that specify ranges of continuous hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of continuous hyperparameters to tune.

Name -> (string)

The name of the continuous hyperparameter to tune.

MinValue -> (string)

The minimum value for the hyperparameter. The tuning job uses floating-point values between this value and `MaxValue` for tuning.

MaxValue -> (string)

The maximum value for the hyperparameter. The tuning job uses floating-point values between `MinValue` value and this value for tuning.

ScalingType -> (string)

The scale that hyperparameter tuning uses to search the hyperparameter range. For information about choosing a hyperparameter scale, see [Hyperparameter Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-ranges.html#scaling-type) . One of the following values:

Auto

SageMaker hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.

Logarithmic scaling works only for ranges that have only values greater than 0.

ReverseLogarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale.

Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

CategoricalParameterRanges -> (list)

The array of [CategoricalParameterRange](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CategoricalParameterRange.html) objects that specify ranges of categorical hyperparameters that a hyperparameter tuning job searches.

(structure)

A list of categorical hyperparameters to tune.

Name -> (string)

The name of the categorical hyperparameter to tune.

Values -> (list)

A list of the categories for the hyperparameter.

(string)

AutoParameters -> (list)

A list containing hyperparameter names and example values to be used by Autotune to determine optimal ranges for your tuning job.

(structure)

The name and an example value of the hyperparameter that you want to use in Autotune. If Automatic model tuning (AMT) determines that your hyperparameter is eligible for Autotune, an optimal hyperparameter range is selected for you.

Name -> (string)

The name of the hyperparameter to optimize using Autotune.

ValueHint -> (string)

An example value of the hyperparameter to optimize using Autotune.

StaticHyperParameters -> (map)

Specifies the values of hyperparameters that do not change for the tuning job.

key -> (string)

value -> (string)

AlgorithmSpecification -> (structure)

The [HyperParameterAlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterAlgorithmSpecification.html) object that specifies the resource algorithm to use for the training jobs that the tuning job launches.

TrainingImage -> (string)

The registry path of the Docker image that contains the training algorithm. For information about Docker registry paths for built-in algorithms, see [Algorithms Provided by Amazon SageMaker: Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) . SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

TrainingInputMode -> (string)

The training input mode that the algorithm supports. For more information about input modes, see [Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) .

**Pipe mode**

If an algorithm supports `Pipe` mode, Amazon SageMaker streams data directly from Amazon S3 to the container.

**File mode**

If an algorithm supports `File` mode, SageMaker downloads the training data from S3 to the provisioned ML storage volume, and mounts the directory to the Docker volume for the training container.

You must provision the ML storage volume with sufficient capacity to accommodate the data downloaded from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container uses the ML storage volume to also store intermediate information, if any.

For distributed algorithms, training data is distributed uniformly. Your training duration is predictable if the input data objects sizes are approximately the same. SageMaker does not split the files any further for model training. If the object sizes are skewed, training wonât be optimal as the data distribution is also skewed when one host in a training cluster is overloaded, thus becoming a bottleneck in training.

**FastFile mode**

If an algorithm supports `FastFile` mode, SageMaker streams data directly from S3 to the container with no code changes, and provides file system access to the data. Users can author their training script to interact with these files as if they were stored on disk.

`FastFile` mode works best when the data is read sequentially. Augmented manifest files arenât supported. The startup time is lower when there are fewer files in the S3 bucket provided.

AlgorithmName -> (string)

The name of the resource algorithm to use for the hyperparameter tuning job. If you specify a value for this parameter, do not specify a value for `TrainingImage` .

MetricDefinitions -> (list)

An array of [MetricDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDefinition.html) objects that specify the metrics that the algorithm emits.

(structure)

Specifies a metric that the training algorithm writes to `stderr` or `stdout` . You can view these logs to understand how your training job performs and check for any errors encountered during training. SageMaker hyperparameter tuning captures all defined metrics. Specify one of the defined metrics to use as an objective metric using the [TuningObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-TuningObjective) parameter in the `HyperParameterTrainingJobDefinition` API to evaluate job performance during hyperparameter tuning.

Name -> (string)

The name of the metric.

Regex -> (string)

A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see [Defining metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role associated with the training jobs that the tuning job launches.

InputDataConfig -> (list)

An array of [Channel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Channel.html) objects that specify the input for the training jobs that the tuning job launches.

(structure)

A channel is a named input source that training algorithms can consume.

ChannelName -> (string)

The name of the channel.

DataSource -> (structure)

The location of the channel data.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training.

If you choose `AugmentedManifestFile` , `S3Uri` identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. `AugmentedManifestFile` can only be used if the Channelâs input mode is `Pipe` .

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/`
- A manifest might look like this: `s3://bucketname/example.manifest`   A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of `S3Uri` . Note that the prefix must be a valid non-empty `S3Uri` that precludes users from specifying a manifest whose individual `S3Uri` is sourced from different S3 buckets. The following code example shows a valid manifest format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   This JSON is equivalent to the following `S3Uri` list:  `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uri` in this manifest is the input data for the channel for this data source. The object that each `S3Uri` points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf.

Your input bucket must be located in same Amazon Web Services region as your training job.

S3DataDistributionType -> (string)

If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify `FullyReplicated` .

If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify `ShardedByS3Key` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data.

Donât choose more ML compute instances for training than available S3 objects. If you do, some nodes wonât get any data and you will pay for nodes that arenât getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms.

In distributed training, where you use multiple ML compute EC2 instances, you might choose `ShardedByS3Key` . If the algorithm requires copying training data to the ML storage volume (when `TrainingInputMode` is set to `File` ), this copies 1/*n* of the number of objects.

AttributeNames -> (list)

A list of one or more attribute names to use that are found in a specified augmented manifest file.

(string)

InstanceGroupNames -> (list)

A list of names of instance groups that get data from the S3 data source.

(string)

ModelAccessConfig -> (structure)

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` .

- If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
- If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params) .

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.

HubContentArn -> (string)

The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.

FileSystemDataSource -> (structure)

The file system that is associated with a channel.

FileSystemId -> (string)

The file system id.

FileSystemAccessMode -> (string)

The access mode of the mount of the directory associated with the channel. A directory can be mounted either in `ro` (read-only) or `rw` (read-write) mode.

FileSystemType -> (string)

The file system type.

DirectoryPath -> (string)

The full path to the directory to associate with the channel.

ContentType -> (string)

The MIME type of the data.

CompressionType -> (string)

If training data is compressed, the compression type. The default value is `None` . `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.

RecordWrapperType -> (string)

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you donât need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format) .

In File mode, leave this field unset or set it to None.

InputMode -> (string)

(Optional) The input mode to use for the data channel in a training job. If you donât set a value for `InputMode` , SageMaker uses the value set for `TrainingInputMode` . Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training jobâs general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.

To use a model for incremental training, choose `File` input model.

ShuffleConfig -> (structure)

A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType` , this shuffles the results of the S3 key prefix matches. If you use `ManifestFile` , the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile` , the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.

For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key` , the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.

Seed -> (long)

Determines the shuffling order in `ShuffleConfig` value.

VpcConfig -> (structure)

The [VpcConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html) object that specifies the VPC that you want the training jobs that this hyperparameter tuning job launches to connect to. Control access to and from your training container by configuring the VPC. For more information, see [Protect Training Jobs by Using an Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/train-vpc.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

OutputDataConfig -> (structure)

Specifies the path to the Amazon S3 bucket where you store model artifacts from the training jobs that the tuning job launches.

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`
- // KMS Key Alias  `"alias/ExampleAlias"`
- // Amazon Resource Name (ARN) of a KMS Key Alias  `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"`

If you use a KMS key ID or an alias of your KMS key, the SageMaker execution role must include permissions to call `kms:Encrypt` . If you donât provide a KMS key ID, SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide* . If the output data is stored in Amazon S3 Express One Zone, it is encrypted with server-side encryption with Amazon S3 managed keys (SSE-S3). KMS key is not supported for Amazon S3 Express One Zone

The KMS key policy must grant permission to the IAM role that you specify in your `CreateTrainingJob` , `CreateTransformJob` , or `CreateHyperParameterTuningJob` requests. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

S3OutputPath -> (string)

Identifies the S3 path where you want SageMaker to store the model artifacts. For example, `s3://bucket-name/key-name-prefix` .

CompressionType -> (string)

The model output compression type. Select `None` to output an uncompressed model, recommended for large model outputs. Defaults to gzip.

ResourceConfig -> (structure)

The resources, including the compute instances and storage volumes, to use for the training jobs that the tuning job launches.

Storage volumes store model artifacts and incremental states. Training algorithms might also use storage volumes for scratch space. If you want SageMaker to use the storage volume to store the training data, choose `File` as the `TrainingInputMode` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

### Note

If you want to use hyperparameter optimization with instance type flexibility, use `HyperParameterTuningResourceConfig` instead.

InstanceType -> (string)

The ML compute instance type.

### Note

SageMaker Training on Amazon Elastic Compute Cloud (EC2) P4de instances is in preview release starting December 9th, 2022.

[Amazon EC2 P4de instances](http://aws.amazon.com/ec2/instance-types/p4/) (currently in preview) are powered by 8 NVIDIA A100 GPUs with 80GB high-performance HBM2e GPU memory, which accelerate the speed of training ML models that need to be trained on large datasets of high-resolution data. In this preview release, Amazon SageMaker supports ML training jobs on P4de instances (`ml.p4de.24xlarge` ) to reduce model training time. The `ml.p4de.24xlarge` instances are available in the following Amazon Web Services Regions.

- US East (N. Virginia) (us-east-1)
- US West (Oregon) (us-west-2)

To request quota limit increase and start using P4de instances, contact the SageMaker Training service team through your account team.

InstanceCount -> (integer)

The number of ML compute instances to use. For distributed training, provide a value greater than 1.

VolumeSizeInGB -> (integer)

The size of the ML storage volume that you want to provision.

ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose `File` as the `TrainingInputMode` in the algorithm specification.

When using an ML instance with [NVMe SSD volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html#nvme-ssd-volumes) , SageMaker doesnât provision Amazon EBS General Purpose SSD (gp2) storage. Available storage is fixed to the NVMe-type instanceâs storage capacity. SageMaker configures storage paths for training datasets, checkpoints, model artifacts, and outputs to use the entire capacity of the instance storage. For example, ML instance families with the NVMe-type instance storage include `ml.p4d` , `ml.g4dn` , and `ml.g5` .

When using an ML instance with the EBS-only storage option and without instance storage, you must define the size of EBS volume through `VolumeSizeInGB` in the `ResourceConfig` API. For example, ML instance families that use EBS volumes include `ml.c5` and `ml.p2` .

To look up instance types and their instance storage types and volumes, see [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) .

To find the default local paths defined by the SageMaker training platform, see [Amazon SageMaker Training Storage Folders for Training Datasets, Checkpoints, Model Artifacts, and Outputs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-train-storage.html) .

VolumeKmsKeyId -> (string)

The Amazon Web Services KMS key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the training job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be in any of the following formats:

- // KMS Key ID  `"1234abcd-12ab-34cd-56ef-1234567890ab"`
- // Amazon Resource Name (ARN) of a KMS Key  `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

KeepAlivePeriodInSeconds -> (integer)

The duration of time in seconds to retain configured resources in a warm pool for subsequent training jobs.

InstanceGroups -> (list)

The configuration of a heterogeneous cluster in JSON format.

(structure)

Defines an instance group for heterogeneous cluster training. When requesting a training job using the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API, you can configure multiple instance groups .

InstanceType -> (string)

Specifies the instance type of the instance group.

InstanceCount -> (integer)

Specifies the number of instances of the instance group.

InstanceGroupName -> (string)

Specifies the name of the instance group.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan to use for this resource configuration.

HyperParameterTuningResourceConfig -> (structure)

The configuration for the hyperparameter tuning resources, including the compute instances and storage volumes, used for training jobs launched by the tuning job. By default, storage volumes hold model artifacts and incremental states. Choose `File` for `TrainingInputMode` in the `AlgorithmSpecification` parameter to additionally store training data in the storage volume (optional).

InstanceType -> (string)

The instance type used to run hyperparameter optimization tuning jobs. See [descriptions of instance types](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) for more information.

InstanceCount -> (integer)

The number of compute instances of type `InstanceType` to use. For [distributed training](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) , select a value greater than 1.

VolumeSizeInGB -> (integer)

The volume size in GB for the storage volume to be used in processing hyperparameter optimization jobs (optional). These volumes store model artifacts, incremental states and optionally, scratch space for training algorithms. Do not provide a value for this parameter if a value for `InstanceConfigs` is also specified.

Some instance types have a fixed total local storage size. If you select one of these instances for training, `VolumeSizeInGB` cannot be greater than this total size. For a list of instance types with local instance storage and their sizes, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) .

### Note

SageMaker supports only the [General Purpose SSD (gp2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) storage volume type.

VolumeKmsKeyId -> (string)

A key used by Amazon Web Services Key Management Service to encrypt data on the storage volume attached to the compute instances used to run the training job. You can use either of the following formats to specify a key.

KMS Key ID:

`"1234abcd-12ab-34cd-56ef-1234567890ab"`

Amazon Resource Name (ARN) of a KMS key:

`"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"`

Some instances use local storage, which use a [hardware module to encrypt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) storage volumes. If you choose one of these instance types, you cannot request a `VolumeKmsKeyId` . For a list of instance types that use local storage, see [instance store volumes](http://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/) . For more information about Amazon Web Services Key Management Service, see [KMS encryption](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-security-kms-permissions.html) for more information.

AllocationStrategy -> (string)

The strategy that determines the order of preference for resources specified in `InstanceConfigs` used in hyperparameter optimization.

InstanceConfigs -> (list)

A list containing the configuration(s) for one or more resources for processing hyperparameter jobs. These resources include compute instances and storage volumes to use in model training jobs launched by hyperparameter tuning jobs. The `AllocationStrategy` controls the order in which multiple configurations provided in `InstanceConfigs` are used.

### Note

If you only want to use a single instance configuration inside the `HyperParameterTuningResourceConfig` API, do not provide a value for `InstanceConfigs` . Instead, use `InstanceType` , `VolumeSizeInGB` and `InstanceCount` . If you use `InstanceConfigs` , do not provide values for `InstanceType` , `VolumeSizeInGB` or `InstanceCount` .

(structure)

The configuration for hyperparameter tuning resources for use in training jobs launched by the tuning job. These resources include compute instances and storage volumes. Specify one or more compute instance configurations and allocation strategies to select resources (optional).

InstanceType -> (string)

The instance type used for processing of hyperparameter optimization jobs. Choose from general purpose (no GPUs) instance types: ml.m5.xlarge, ml.m5.2xlarge, and ml.m5.4xlarge or compute optimized (no GPUs) instance types: ml.c5.xlarge and ml.c5.2xlarge. For more information about instance types, see [instance type descriptions](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html) .

InstanceCount -> (integer)

The number of instances of the type specified by `InstanceType` . Choose an instance count larger than 1 for distributed training algorithms. See [Step 2: Launch a SageMaker Distributed Training Job Using the SageMaker Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel-use-api.html) for more information.

VolumeSizeInGB -> (integer)

The volume size in GB of the data to be processed for hyperparameter optimization (optional).

StoppingCondition -> (structure)

Specifies a limit to how long a model hyperparameter training job can run. It also specifies how long a managed spot training job has to complete. When the job reaches the time limit, SageMaker ends the training job. Use this API to cap model training costs.

MaxRuntimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.

For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.

For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.

The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.

MaxWaitTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds` . If the job does not complete during this time, SageMaker ends the job.

When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.

MaxPendingTimeInSeconds -> (integer)

The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.

### Note

When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html) , not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:

- The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a planâs start date (waiting for scheduled start time)
- Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods

`MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.

EnableNetworkIsolation -> (boolean)

Isolates the training container. No inbound or outbound network calls can be made, except for calls between peers within a training cluster for distributed training. If network isolation is used for training jobs that are configured to use a VPC, SageMaker downloads and uploads customer data and model artifacts through the specified VPC, but the training container does not have network access.

EnableInterContainerTrafficEncryption -> (boolean)

To encrypt all communications between ML compute instances in distributed training, choose `True` . Encryption provides greater security for distributed training, but training might take longer. How long it takes depends on the amount of communication between compute instances, especially if you use a deep learning algorithm in distributed training.

EnableManagedSpotTraining -> (boolean)

A Boolean indicating whether managed spot training is enabled (`True` ) or not (`False` ).

CheckpointConfig -> (structure)

Contains information about the output location for managed spot training checkpoint data.

S3Uri -> (string)

Identifies the S3 path where you want SageMaker to store checkpoints. For example, `s3://bucket-name/key-name-prefix` .

LocalPath -> (string)

(Optional) The local directory where checkpoints are written. The default directory is `/opt/ml/checkpoints/` .

RetryStrategy -> (structure)

The number of times to retry the job when the job fails due to an `InternalServerError` .

MaximumRetryAttempts -> (integer)

The number of times to retry the job. When the job is retried, itâs `SecondaryStatus` is changed to `STARTING` .

Environment -> (map)

An environment variable that you can pass into the SageMaker [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. You can use an existing [environment variable from the training container](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html#sagemaker-CreateTrainingJob-request-Environment) or use your own. See [Define metrics and variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) for more information.

### Note

The maximum number of items specified for `Map Entries` refers to the maximum number of environment variables for each `TrainingJobDefinition` and also the maximum for the hyperparameter tuning job itself. That is, the sum of the number of environment variables for all the training job definitions canât exceed the maximum number specified.

key -> (string)

value -> (string)

HyperParameterTuningJobStatus -> (string)

The status of a hyperparameter tuning job.

CreationTime -> (timestamp)

The time that a hyperparameter tuning job was created.

HyperParameterTuningEndTime -> (timestamp)

The time that a hyperparameter tuning job ended.

LastModifiedTime -> (timestamp)

The time that a hyperparameter tuning job was last modified.

TrainingJobStatusCounters -> (structure)

The numbers of training jobs launched by a hyperparameter tuning job, categorized by status.

Completed -> (integer)

The number of completed training jobs launched by the hyperparameter tuning job.

InProgress -> (integer)

The number of in-progress training jobs launched by a hyperparameter tuning job.

RetryableError -> (integer)

The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.

NonRetryableError -> (integer)

The number of training jobs that failed and canât be retried. A failed training job canât be retried if it failed because a client error occurred.

Stopped -> (integer)

The number of training jobs launched by a hyperparameter tuning job that were manually stopped.

ObjectiveStatusCounters -> (structure)

Specifies the number of training jobs that this hyperparameter tuning job launched, categorized by the status of their objective metric. The objective metric status shows whether the final objective metric for the training job has been evaluated by the tuning job and used in the hyperparameter tuning process.

Succeeded -> (integer)

The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.

Pending -> (integer)

The number of training jobs that are in progress and pending evaluation of their final objective metric.

Failed -> (integer)

The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.

BestTrainingJob -> (structure)

The container for the summary information about a training job.

TrainingJobDefinitionName -> (string)

The training job definition name.

TrainingJobName -> (string)

The name of the training job.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

TuningJobName -> (string)

The HyperParameter tuning job that launched the training job.

CreationTime -> (timestamp)

The date and time that the training job was created.

TrainingStartTime -> (timestamp)

The date and time that the training job started.

TrainingEndTime -> (timestamp)

Specifies the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.

TrainingJobStatus -> (string)

The status of the training job.

TunedHyperParameters -> (map)

A list of the hyperparameters for which you specified ranges to search.

key -> (string)

value -> (string)

FailureReason -> (string)

The reason that the training job failed.

FinalHyperParameterTuningJobObjectiveMetric -> (structure)

The [FinalHyperParameterTuningJobObjectiveMetric](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalHyperParameterTuningJobObjectiveMetric.html) object that specifies the value of the objective metric of the tuning job that launched this training job.

Type -> (string)

Select if you want to minimize or maximize the objective metric during hyperparameter tuning.

MetricName -> (string)

The name of the objective metric. For SageMaker built-in algorithms, metrics are defined per algorithm. See the [metrics for XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html) as an example. You can also use a custom algorithm for training and define your own metrics. For more information, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Value -> (float)

The value of the objective metric.

ObjectiveStatus -> (string)

The status of the objective metric for the training job:

- Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
- Pending: The training job is in progress and evaluation of its final objective metric is pending.
- Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.

OverallBestTrainingJob -> (structure)

The container for the summary information about a training job.

TrainingJobDefinitionName -> (string)

The training job definition name.

TrainingJobName -> (string)

The name of the training job.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

TuningJobName -> (string)

The HyperParameter tuning job that launched the training job.

CreationTime -> (timestamp)

The date and time that the training job was created.

TrainingStartTime -> (timestamp)

The date and time that the training job started.

TrainingEndTime -> (timestamp)

Specifies the time when the training job ends on training instances. You are billed for the time interval between the value of `TrainingStartTime` and this time. For successful jobs and stopped jobs, this is the time after model artifacts are uploaded. For failed jobs, this is the time when SageMaker detects a job failure.

TrainingJobStatus -> (string)

The status of the training job.

TunedHyperParameters -> (map)

A list of the hyperparameters for which you specified ranges to search.

key -> (string)

value -> (string)

FailureReason -> (string)

The reason that the training job failed.

FinalHyperParameterTuningJobObjectiveMetric -> (structure)

The [FinalHyperParameterTuningJobObjectiveMetric](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalHyperParameterTuningJobObjectiveMetric.html) object that specifies the value of the objective metric of the tuning job that launched this training job.

Type -> (string)

Select if you want to minimize or maximize the objective metric during hyperparameter tuning.

MetricName -> (string)

The name of the objective metric. For SageMaker built-in algorithms, metrics are defined per algorithm. See the [metrics for XGBoost](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html) as an example. You can also use a custom algorithm for training and define your own metrics. For more information, see [Define metrics and environment variables](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html) .

Value -> (float)

The value of the objective metric.

ObjectiveStatus -> (string)

The status of the objective metric for the training job:

- Succeeded: The final objective metric for the training job was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.
- Pending: The training job is in progress and evaluation of its final objective metric is pending.
- Failed: The final objective metric for the training job was not evaluated, and was not used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.

WarmStartConfig -> (structure)

Specifies the configuration for a hyperparameter tuning job that uses one or more previous hyperparameter tuning jobs as a starting point. The results of previous tuning jobs are used to inform which combinations of hyperparameters to search over in the new tuning job.

All training jobs launched by the new hyperparameter tuning job are evaluated by using the objective metric, and the training job that performs the best is compared to the best training jobs from the parent tuning jobs. From these, the training job that performs the best as measured by the objective metric is returned as the overall best training job.

### Note

All training jobs launched by parent hyperparameter tuning jobs and the new hyperparameter tuning jobs count against the limit of training jobs for the tuning job.

ParentHyperParameterTuningJobs -> (list)

An array of hyperparameter tuning jobs that are used as the starting point for the new hyperparameter tuning job. For more information about warm starting a hyperparameter tuning job, see [Using a Previous Hyperparameter Tuning Job as a Starting Point](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html) .

Hyperparameter tuning jobs created before October 1, 2018 cannot be used as parent jobs for warm start tuning jobs.

(structure)

A previously completed or stopped hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.

HyperParameterTuningJobName -> (string)

The name of the hyperparameter tuning job to be used as a starting point for a new hyperparameter tuning job.

WarmStartType -> (string)

Specifies one of the following:

IDENTICAL_DATA_AND_ALGORITHM

The new hyperparameter tuning job uses the same input data and training image as the parent tuning jobs. You can change the hyperparameter ranges to search and the maximum number of training jobs that the hyperparameter tuning job launches. You cannot use a new version of the training algorithm, unless the changes in the new version do not affect the algorithm itself. For example, changes that improve logging or adding support for a different data format are allowed. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.

TRANSFER_LEARNING

The new hyperparameter tuning job can include input data, hyperparameter ranges, maximum number of concurrent training jobs, and maximum number of training jobs that are different than those of its parent hyperparameter tuning jobs. The training image can also be a different version from the version used in the parent hyperparameter tuning job. You can also change hyperparameters from tunable to static, and from static to tunable, but the total number of static plus tunable hyperparameters must remain the same as it is in all parent jobs. The objective metric for the new tuning job must be the same as for all parent jobs.

FailureReason -> (string)

The error that was created when a hyperparameter tuning job failed.

TuningJobCompletionDetails -> (structure)

Information about either a current or completed hyperparameter tuning job.

NumberOfTrainingJobsObjectiveNotImproving -> (integer)

The number of training jobs launched by a tuning job that are not improving (1% or less) as measured by model performance evaluated against an objective function.

ConvergenceDetectedTime -> (timestamp)

The time in timestamp format that AMT detected model convergence, as defined by a lack of significant improvement over time based on criteria developed over a wide range of diverse benchmarking tests.

ConsumedResources -> (structure)

The total amount of resources consumed by a hyperparameter tuning job.

RuntimeInSeconds -> (integer)

The wall clock runtime in seconds used by your hyperparameter tuning job.

Tags -> (list)

The tags associated with a hyperparameter tuning job. For more information see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

ModelCard -> (structure)

An Amazon SageMaker Model Card that documents details about a machine learning model.

ModelCardArn -> (string)

The Amazon Resource Name (ARN) of the model card.

ModelCardName -> (string)

The unique name of the model card.

ModelCardVersion -> (integer)

The version of the model card.

Content -> (string)

The content of the model card. Content uses the [model card JSON schema](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html#model-cards-json-schema) and provided as a string.

ModelCardStatus -> (string)

The approval status of the model card within your organization. Different organizations might have different criteria for model card review and approval.

- `Draft` : The model card is a work in progress.
- `PendingReview` : The model card is pending review.
- `Approved` : The model card is approved.
- `Archived` : The model card is archived. No more updates should be made to the model card, but it can still be exported.

SecurityConfig -> (structure)

The security configuration used to protect model card data.

KmsKeyId -> (string)

A Key Management Service [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) to use for encrypting a model card.

CreationTime -> (timestamp)

The date and time that the model card was created.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

The date and time that the model card was last modified.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

Tags -> (list)

Key-value pairs used to manage metadata for the model card.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

ModelId -> (string)

The unique name (ID) of the model.

RiskRating -> (string)

The risk rating of the model. Different organizations might have different criteria for model card risk ratings. For more information, see [Risk ratings](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-risk-rating.html) .

ModelPackageGroupName -> (string)

The model package group that contains the model package. Only relevant for model cards created for model packages in the Amazon SageMaker Model Registry.

Model -> (structure)

A model displayed in the Amazon SageMaker Model Dashboard.

Model -> (structure)

A model displayed in the Model Dashboard.

ModelName -> (string)

The name of the model.

PrimaryContainer -> (structure)

Describes the container, as part of model definition.

ContainerHostname -> (string)

This parameter is ignored for models that contain only a `PrimaryContainer` .

When a `ContainerDefinition` is part of an inference pipeline, the value of the parameter uniquely identifies the container for the purposes of logging and metrics. For information, see [Use Logs and Metrics to Monitor an Inference Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html) . If you donât specify a value for this parameter for a `ContainerDefinition` that is part of an inference pipeline, a unique name is automatically assigned based on the position of the `ContainerDefinition` in the pipeline. If you specify a value for the `ContainerHostName` for any `ContainerDefinition` that is part of an inference pipeline, you must specify a value for the `ContainerHostName` parameter of every `ContainerDefinition` in that pipeline.

Image -> (string)

The path where inference code is stored. This can be either in Amazon EC2 Container Registry or in a Docker registry that is accessible from the same VPC that you configure for your endpoint. If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

### Note

The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.

ImageConfig -> (structure)

Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC). For information about storing containers in a private Docker registry, see [Use a Private Docker Registry for Real-Time Inference Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html) .

### Note

The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.

RepositoryAccessMode -> (string)

Set this to one of the following values:

- `Platform` - The model image is hosted in Amazon ECR.
- `Vpc` - The model image is hosted in a private Docker registry in your VPC.

RepositoryAuthConfig -> (structure)

(Optional) Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field, and the private Docker registry where the model image is hosted requires authentication.

RepositoryCredentialsProviderArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function that provides credentials to authenticate to the private Docker registry where your model image is hosted. For information about how to create an Amazon Web Services Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the *Amazon Web Services Lambda Developer Guide* .

Mode -> (string)

Whether the container hosts a single model or multiple models.

ModelDataUrl -> (string)

The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). The S3 path is required for SageMaker built-in algorithms, but not if you use your own algorithms. For more information on built-in algorithms, see [Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) .

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model or endpoint you are creating.

If you provide a value for this parameter, SageMaker uses Amazon Web Services Security Token Service to download model artifacts from the S3 path you provide. Amazon Web Services STS is activated in your Amazon Web Services account by default. If you previously deactivated Amazon Web Services STS for a region, you need to reactivate Amazon Web Services STS for that region. For more information, see [Activating and Deactivating Amazon Web Services STS in an Amazon Web Services Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *Amazon Web Services Identity and Access Management User Guide* .

### Warning

If you use a built-in algorithm to create a model, SageMaker requires that you provide a S3 path to the model artifacts in `ModelDataUrl` .

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy.

### Note

Currently you cannot use `ModelDataSource` in conjunction with SageMaker batch transform, SageMaker serverless endpoints, SageMaker multi-model endpoints, and SageMaker Marketplace.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

AdditionalModelDataSources -> (list)

Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.

(structure)

Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.

ChannelName -> (string)

A custom name for this `AdditionalModelDataSource` object.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

Environment -> (map)

The environment variables to set in the Docker container. Donât include any sensitive data in your environment variables.

The maximum length of each key and value in the `Environment` map is 1024 bytes. The maximum length of all keys and values in the map, combined, is 32 KB. If you pass multiple containers to a `CreateModel` request, then the maximum length of all of their maps, combined, is also 32 KB.

key -> (string)

value -> (string)

ModelPackageName -> (string)

The name or Amazon Resource Name (ARN) of the model package to use to create the model.

InferenceSpecificationName -> (string)

The inference specification name in the model package version.

MultiModelConfig -> (structure)

Specifies additional configuration for multi-model endpoints.

ModelCacheSetting -> (string)

Whether to cache models for a multi-model endpoint. By default, multi-model endpoints cache models so that a model does not have to be loaded into memory each time it is invoked. Some use cases do not benefit from model caching. For example, if an endpoint hosts a large number of models that are each invoked infrequently, the endpoint might perform better if you disable model caching. To disable model caching, set the value of this parameter to `Disabled` .

Containers -> (list)

The containers in the inference pipeline.

(structure)

Describes the container, as part of model definition.

ContainerHostname -> (string)

This parameter is ignored for models that contain only a `PrimaryContainer` .

When a `ContainerDefinition` is part of an inference pipeline, the value of the parameter uniquely identifies the container for the purposes of logging and metrics. For information, see [Use Logs and Metrics to Monitor an Inference Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-logs-metrics.html) . If you donât specify a value for this parameter for a `ContainerDefinition` that is part of an inference pipeline, a unique name is automatically assigned based on the position of the `ContainerDefinition` in the pipeline. If you specify a value for the `ContainerHostName` for any `ContainerDefinition` that is part of an inference pipeline, you must specify a value for the `ContainerHostName` parameter of every `ContainerDefinition` in that pipeline.

Image -> (string)

The path where inference code is stored. This can be either in Amazon EC2 Container Registry or in a Docker registry that is accessible from the same VPC that you configure for your endpoint. If you are using your own custom algorithm instead of an algorithm provided by SageMaker, the inference code must meet SageMaker requirements. SageMaker supports both `registry/repository[:tag]` and `registry/repository[@digest]` image path formats. For more information, see [Using Your Own Algorithms with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html) .

### Note

The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.

ImageConfig -> (structure)

Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC). For information about storing containers in a private Docker registry, see [Use a Private Docker Registry for Real-Time Inference Containers](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-containers-inference-private.html) .

### Note

The model artifacts in an Amazon S3 bucket and the Docker image for inference container in Amazon EC2 Container Registry must be in the same region as the model or endpoint you are creating.

RepositoryAccessMode -> (string)

Set this to one of the following values:

- `Platform` - The model image is hosted in Amazon ECR.
- `Vpc` - The model image is hosted in a private Docker registry in your VPC.

RepositoryAuthConfig -> (structure)

(Optional) Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field, and the private Docker registry where the model image is hosted requires authentication.

RepositoryCredentialsProviderArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function that provides credentials to authenticate to the private Docker registry where your model image is hosted. For information about how to create an Amazon Web Services Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the *Amazon Web Services Lambda Developer Guide* .

Mode -> (string)

Whether the container hosts a single model or multiple models.

ModelDataUrl -> (string)

The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). The S3 path is required for SageMaker built-in algorithms, but not if you use your own algorithms. For more information on built-in algorithms, see [Common Parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-algo-docker-registry-paths.html) .

### Note

The model artifacts must be in an S3 bucket that is in the same region as the model or endpoint you are creating.

If you provide a value for this parameter, SageMaker uses Amazon Web Services Security Token Service to download model artifacts from the S3 path you provide. Amazon Web Services STS is activated in your Amazon Web Services account by default. If you previously deactivated Amazon Web Services STS for a region, you need to reactivate Amazon Web Services STS for that region. For more information, see [Activating and Deactivating Amazon Web Services STS in an Amazon Web Services Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html) in the *Amazon Web Services Identity and Access Management User Guide* .

### Warning

If you use a built-in algorithm to create a model, SageMaker requires that you provide a S3 path to the model artifacts in `ModelDataUrl` .

ModelDataSource -> (structure)

Specifies the location of ML model data to deploy.

### Note

Currently you cannot use `ModelDataSource` in conjunction with SageMaker batch transform, SageMaker serverless endpoints, SageMaker multi-model endpoints, and SageMaker Marketplace.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

AdditionalModelDataSources -> (list)

Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.

(structure)

Data sources that are available to your model in addition to the one that you specify for `ModelDataSource` when you use the `CreateModel` action.

ChannelName -> (string)

A custom name for this `AdditionalModelDataSource` object.

S3DataSource -> (structure)

Specifies the S3 location of ML model data to deploy.

S3Uri -> (string)

Specifies the S3 path of ML model data to deploy.

S3DataType -> (string)

Specifies the type of ML model data to deploy.

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix as part of the ML model data to deploy. A valid key name prefix identified by `S3Uri` always ends with a forward slash (/).

If you choose `S3Object` , `S3Uri` identifies an object that is the ML model data to deploy.

CompressionType -> (string)

Specifies how the ML model data is prepared.

If you choose `Gzip` and choose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that is a gzip-compressed TAR archive. SageMaker will attempt to decompress and untar the object during model deployment.

If you choose `None` and chooose `S3Object` as the value of `S3DataType` , `S3Uri` identifies an object that represents an uncompressed ML model to deploy.

If you choose None and choose `S3Prefix` as the value of `S3DataType` , `S3Uri` identifies a key name prefix, under which all objects represents the uncompressed ML model to deploy.

If you choose None, then SageMaker will follow rules below when creating model data files under /opt/ml/model directory for use by your inference code:

- If you choose `S3Object` as the value of `S3DataType` , then SageMaker will split the key of the S3 object referenced by `S3Uri` by slash (/), and use the last part as the filename of the file holding the content of the S3 object.
- If you choose `S3Prefix` as the value of `S3DataType` , then for each S3 object under the key name pefix referenced by `S3Uri` , SageMaker will trim its key by the prefix, and use the remainder as the path (relative to `/opt/ml/model` ) of the file holding the content of the S3 object. SageMaker will split the remainder by slash (/), using intermediate parts as directory names and the last part as filename of the file holding the content of the S3 object.
- Do not use any of the following as file names or directory names:
- An empty or blank string
- A string which contains null bytes
- A string longer than 255 bytes
- A single dot (`.` )
- A double dot (`..` )
- Ambiguous file names will result in model deployment failure. For example, if your uncompressed ML model consists of two S3 objects `s3://mybucket/model/weights` and `s3://mybucket/model/weights/part1` and you specify `s3://mybucket/model/` as the value of `S3Uri` and `S3Prefix` as the value of `S3DataType` , then it will result in name clash between `/opt/ml/model/weights` (a regular file) and `/opt/ml/model/weights/` (a directory).
- Do not organize the model artifacts in [S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) . When you create a folder in S3 console, S3 creates a 0-byte object with a key set to the folder name you provide. They key of the 0-byte object ends with a slash (/) which violates SageMaker restrictions on model artifact file names, leading to model deployment failure.

ModelAccessConfig -> (structure)

Specifies the access configuration file for the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig` . You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

AcceptEula -> (boolean)

Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.

HubAccessConfig -> (structure)

Configuration information for hub access.

HubContentArn -> (string)

The ARN of the hub content for which deployment access is allowed.

ManifestS3Uri -> (string)

The Amazon S3 URI of the manifest file. The manifest file is a CSV file that stores the artifact locations.

ETag -> (string)

The ETag associated with S3 URI.

ManifestEtag -> (string)

The ETag associated with Manifest S3 URI.

Environment -> (map)

The environment variables to set in the Docker container. Donât include any sensitive data in your environment variables.

The maximum length of each key and value in the `Environment` map is 1024 bytes. The maximum length of all keys and values in the map, combined, is 32 KB. If you pass multiple containers to a `CreateModel` request, then the maximum length of all of their maps, combined, is also 32 KB.

key -> (string)

value -> (string)

ModelPackageName -> (string)

The name or Amazon Resource Name (ARN) of the model package to use to create the model.

InferenceSpecificationName -> (string)

The inference specification name in the model package version.

MultiModelConfig -> (structure)

Specifies additional configuration for multi-model endpoints.

ModelCacheSetting -> (string)

Whether to cache models for a multi-model endpoint. By default, multi-model endpoints cache models so that a model does not have to be loaded into memory each time it is invoked. Some use cases do not benefit from model caching. For example, if an endpoint hosts a large number of models that are each invoked infrequently, the endpoint might perform better if you disable model caching. To disable model caching, set the value of this parameter to `Disabled` .

InferenceExecutionConfig -> (structure)

Specifies details about how containers in a multi-container endpoint are run.

Mode -> (string)

How containers in a multi-container are run. The following values are valid.

- `SERIAL` - Containers run as a serial pipeline.
- `DIRECT` - Only the individual container that you specify is run.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that you specified for the model.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

CreationTime -> (timestamp)

A timestamp that indicates when the model was created.

ModelArn -> (string)

The Amazon Resource Name (ARN) of the model.

EnableNetworkIsolation -> (boolean)

Isolates the model container. No inbound or outbound network calls can be made to or from the model container.

Tags -> (list)

A list of key-value pairs associated with the model. For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

DeploymentRecommendation -> (structure)

A set of recommended deployment configurations for the model.

RecommendationStatus -> (string)

Status of the deployment recommendation. The status `NOT_APPLICABLE` means that SageMaker is unable to provide a default recommendation for the model using the information provided. If the deployment status is `IN_PROGRESS` , retry your API call after a few seconds to get a `COMPLETED` deployment recommendation.

RealTimeInferenceRecommendations -> (list)

A list of [RealTimeInferenceRecommendation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RealTimeInferenceRecommendation.html) items.

(structure)

The recommended configuration to use for Real-Time Inference.

RecommendationId -> (string)

The recommendation ID which uniquely identifies each recommendation.

InstanceType -> (string)

The recommended instance type for Real-Time Inference.

Environment -> (map)

The recommended environment variables to set in the model container for Real-Time Inference.

key -> (string)

value -> (string)

Endpoints -> (list)

The endpoints that host a model.

(structure)

An endpoint that hosts a model displayed in the Amazon SageMaker Model Dashboard.

EndpointName -> (string)

The endpoint name.

EndpointArn -> (string)

The Amazon Resource Name (ARN) of the endpoint.

CreationTime -> (timestamp)

A timestamp that indicates when the endpoint was created.

LastModifiedTime -> (timestamp)

The last time the endpoint was modified.

EndpointStatus -> (string)

The endpoint status.

LastBatchTransformJob -> (structure)

A batch transform job. For information about SageMaker batch transform, see [Use Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) .

TransformJobName -> (string)

The name of the transform job.

TransformJobArn -> (string)

The Amazon Resource Name (ARN) of the transform job.

TransformJobStatus -> (string)

The status of the transform job.

Transform job statuses are:

- `InProgress` - The job is in progress.
- `Completed` - The job has completed.
- `Failed` - The transform job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTransformJob` call.
- `Stopping` - The transform job is stopping.
- `Stopped` - The transform job has stopped.

FailureReason -> (string)

If the transform job failed, the reason it failed.

ModelName -> (string)

The name of the model associated with the transform job.

MaxConcurrentTransforms -> (integer)

The maximum number of parallel requests that can be sent to each instance in a transform job. If `MaxConcurrentTransforms` is set to 0 or left unset, SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is 1. For built-in algorithms, you donât need to set a value for `MaxConcurrentTransforms` .

ModelClientConfig -> (structure)

Configures the timeout and maximum number of retries for processing a transform job invocation.

InvocationsTimeoutInSeconds -> (integer)

The timeout value in seconds for an invocation request. The default value is 600.

InvocationsMaxRetries -> (integer)

The maximum number of retries when invocation requests are failing. The default value is 3.

MaxPayloadInMB -> (integer)

The maximum allowed size of the payload, in MB. A payload is the data portion of a record (without metadata). The value in `MaxPayloadInMB` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is 6 MB. For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0. This feature works only in supported algorithms. Currently, SageMaker built-in algorithms do not support HTTP chunked encoding.

BatchStrategy -> (string)

Specifies the number of records to include in a mini-batch for an HTTP inference request. A record is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.

Environment -> (map)

The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.

key -> (string)

value -> (string)

TransformInput -> (structure)

Describes the input source of a transform job and the way the transform job consumes it.

DataSource -> (structure)

Describes the location of the channel data, which is, the S3 location of the input data that the model can consume.

S3DataSource -> (structure)

The S3 location of the data source that is associated with a channel.

S3DataType -> (string)

If you choose `S3Prefix` , `S3Uri` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for batch transform.

If you choose `ManifestFile` , `S3Uri` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for batch transform.

The following values are compatible: `ManifestFile` , `S3Prefix`

The following value is not compatible: `AugmentedManifestFile`

S3Uri -> (string)

Depending on the value specified for the `S3DataType` , identifies either a key name prefix or a manifest. For example:

- A key name prefix might look like this: `s3://bucketname/exampleprefix/` .
- A manifest might look like this: `s3://bucketname/example.manifest`   The manifest is an S3 object which is a JSON file with the following format:   `[ {"prefix": "s3://customer_bucket/some/prefix/"},` `"relative/path/to/custdata-1",` `"relative/path/custdata-2",` `...` `"relative/path/custdata-N"` `]`   The preceding JSON matches the following `S3Uris` :   `s3://customer_bucket/some/prefix/relative/path/to/custdata-1` `s3://customer_bucket/some/prefix/relative/path/custdata-2` `...` `s3://customer_bucket/some/prefix/relative/path/custdata-N`   The complete set of `S3Uris` in this manifest constitutes the input data for the channel for this datasource. The object that each `S3Uris` points to must be readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.

ContentType -> (string)

The multipurpose internet mail extension (MIME) type of the data. Amazon SageMaker uses the MIME type with each http call to transfer data to the transform job.

CompressionType -> (string)

If your transform data is compressed, specify the compression type. Amazon SageMaker automatically decompresses the data for the transform job accordingly. The default value is `None` .

SplitType -> (string)

The method to use to split the transform jobâs data files into smaller batches. Splitting is necessary when the total size of each object is too large to fit in a single request. You can also use data splitting to improve performance by processing multiple concurrent mini-batches. The default value for `SplitType` is `None` , which indicates that input data files are not split, and request payloads contain the entire contents of an input object. Set the value of this parameter to `Line` to split records on a newline character boundary. `SplitType` also supports a number of record-oriented binary data formats. Currently, the supported record formats are:

- RecordIO
- TFRecord

When splitting is enabled, the size of a mini-batch depends on the values of the `BatchStrategy` and `MaxPayloadInMB` parameters. When the value of `BatchStrategy` is `MultiRecord` , Amazon SageMaker sends the maximum number of records in each request, up to the `MaxPayloadInMB` limit. If the value of `BatchStrategy` is `SingleRecord` , Amazon SageMaker sends individual records in each request.

### Note

Some data formats represent a record as a binary payload wrapped with extra padding bytes. When splitting is applied to a binary data format, padding is removed if the value of `BatchStrategy` is set to `SingleRecord` . Padding is not removed if the value of `BatchStrategy` is set to `MultiRecord` .

For more information about `RecordIO` , see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/faq/recordio) in the MXNet documentation. For more information about `TFRecord` , see [Consuming TFRecord data](https://www.tensorflow.org/guide/data#consuming_tfrecord_data) in the TensorFlow documentation.

TransformOutput -> (structure)

Describes the results of a transform job.

S3OutputPath -> (string)

The Amazon S3 path where you want Amazon SageMaker to store the results of the transform job. For example, `s3://bucket-name/key-name-prefix` .

For every S3 object used as input for the transform job, batch transform stores the transformed data with an .``out`` suffix in a corresponding subfolder in the location in the output prefix. For example, for the input data stored at `s3://bucket-name/input-name-prefix/dataset01/data.csv` , batch transform stores the transformed data at `s3://bucket-name/output-name-prefix/input-name-prefix/data.csv.out` . Batch transform doesnât upload partially processed objects. For an input S3 object that contains multiple records, it creates an .``out`` file only if the transform job succeeds on the entire file. When the input contains multiple S3 objects, the batch transform job processes the listed S3 objects and uploads only the output for successfully processed objects. If any object fails in the transform job batch transform marks the job as failed to prompt investigation.

Accept -> (string)

The MIME type used to specify the output data. Amazon SageMaker uses the MIME type with each http call to transfer data from the transform job.

AssembleWith -> (string)

Defines how to assemble the results of the transform job as a single S3 object. Choose a format that is most convenient to you. To concatenate the results in binary format, specify `None` . To add a newline character at the end of every transformed record, specify `Line` .

KmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. The `KmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

If you donât provide a KMS key ID, Amazon SageMaker uses the default KMS key for Amazon S3 for your roleâs account. For more information, see [KMS-Managed Encryption Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html) in the *Amazon Simple Storage Service Developer Guide.*

The KMS key policy must grant permission to the IAM role that you specify in your [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html) request. For more information, see [Using Key Policies in Amazon Web Services KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Amazon Web Services Key Management Service Developer Guide* .

DataCaptureConfig -> (structure)

Configuration to control how SageMaker captures inference data for batch transform jobs.

DestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

KmsKeyId -> (string)

The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the batch transform job.

The KmsKeyId can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

GenerateInferenceId -> (boolean)

Flag that indicates whether to append inference id to the output.

TransformResources -> (structure)

Describes the resources, including ML instance types and ML instance count, to use for transform job.

InstanceType -> (string)

The ML compute instance type for the transform job. If you are using built-in algorithms to transform moderately sized datasets, we recommend using ml.m4.xlarge or `ml.m5.large` instance types.

InstanceCount -> (integer)

The number of ML compute instances to use in the transform job. The default value is `1` , and the maximum is `100` . For distributed transform jobs, specify a value greater than `1` .

VolumeKmsKeyId -> (string)

The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt model data on the storage volume attached to the ML compute instance(s) that run the batch transform job.

### Note

Certain Nitro-based instances include local storage, dependent on the instance type. Local storage volumes are encrypted using a hardware module on the instance. You canât request a `VolumeKmsKeyId` when using an instance type with local storage.

For a list of instance types that support local instance storage, see [Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes) .

For more information about local instance storage encryption, see [SSD Instance Store Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html) .

The `VolumeKmsKeyId` can be any of the following formats:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias name ARN: `arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias`

TransformAmiVersion -> (string)

Specifies an option from a collection of preconfigured Amazon Machine Image (AMI) images. Each image is configured by Amazon Web Services with a set of software and driver versions.

al2-ami-sagemaker-batch-gpu-470

- Accelerator: GPU
- NVIDIA driver version: 470

al2-ami-sagemaker-batch-gpu-535
- Accelerator: GPU
- NVIDIA driver version: 535

CreationTime -> (timestamp)

A timestamp that shows when the transform Job was created.

TransformStartTime -> (timestamp)

Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of `TransformEndTime` .

TransformEndTime -> (timestamp)

Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of `TransformStartTime` .

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) of the labeling job that created the transform job.

AutoMLJobArn -> (string)

The Amazon Resource Name (ARN) of the AutoML job that created the transform job.

DataProcessing -> (structure)

The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html) .

InputFilter -> (string)

A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the input data to pass to the algorithm. Use the `InputFilter` parameter to exclude fields, such as an ID column, from the input. If you want SageMaker to pass the entire input dataset to the algorithm, accept the default value `$` .

Examples: `"$"` , `"$[1:]"` , `"$.features"`

OutputFilter -> (string)

A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the joined dataset to save in the output file for a batch transform job. If you want SageMaker to store the entire input dataset in the output file, leave the default value, `$` . If you specify indexes that arenât within the dimension size of the joined dataset, you get an error.

Examples: `"$"` , `"$[0,5:]"` , `"$['id','SageMakerOutput']"`

JoinSource -> (string)

Specifies the source of the data to join with the transformed data. The valid values are `None` and `Input` . The default value is `None` , which specifies not to join the input with the transformed data. If you want the batch transform job to join the original input data with the transformed data, set `JoinSource` to `Input` . You can specify `OutputFilter` as an additional filter to select a portion of the joined dataset and store it in the output file.

For JSON or JSONLines objects, such as a JSON array, SageMaker adds the transformed data to the input JSON object in an attribute called `SageMakerOutput` . The joined result for JSON must be a key-value pair object. If the input is not a key-value pair object, SageMaker creates a new JSON file. In the new JSON file, and the input data is stored under the `SageMakerInput` key and the results are stored in `SageMakerOutput` .

For CSV data, SageMaker takes each row as a JSON array and joins the transformed data with the input by appending each transformed row to the end of the input. The joined data has the original input data followed by the transformed data and the output is a CSV file.

For information on how joining in applied, see [Workflow for Associating Inferences with Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#batch-transform-data-processing-workflow) .

ExperimentConfig -> (structure)

Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:

- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
- [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)

ExperimentName -> (string)

The name of an existing experiment to associate with the trial component.

TrialName -> (string)

The name of an existing trial to associate the trial component with. If not specified, a new trial is created.

TrialComponentDisplayName -> (string)

The display name for the trial component. If this key isnât specified, the display name is the trial component name.

RunName -> (string)

The name of the experiment run to associate with the trial component.

Tags -> (list)

A list of tags associated with the transform job.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

MonitoringSchedules -> (list)

The monitoring schedules for a model.

(structure)

A monitoring schedule for a model displayed in the Amazon SageMaker Model Dashboard.

MonitoringScheduleArn -> (string)

The Amazon Resource Name (ARN) of a monitoring schedule.

MonitoringScheduleName -> (string)

The name of a monitoring schedule.

MonitoringScheduleStatus -> (string)

The status of the monitoring schedule.

MonitoringType -> (string)

The monitor type of a model monitor.

FailureReason -> (string)

If a monitoring job failed, provides the reason.

CreationTime -> (timestamp)

A timestamp that indicates when the monitoring schedule was created.

LastModifiedTime -> (timestamp)

A timestamp that indicates when the monitoring schedule was last updated.

MonitoringScheduleConfig -> (structure)

Configures the monitoring schedule and defines the monitoring job.

ScheduleConfig -> (structure)

Configures the monitoring schedule.

ScheduleExpression -> (string)

A cron expression that describes details about the monitoring schedule.

The supported cron expressions are:

- If you want to set the job to start every hour, use the following:  `Hourly: cron(0 * ? * * *)`
- If you want to start the job daily:  `cron(0 [00-23] ? * * *)`
- If you want to run the job one time, immediately, use the following keyword:  `NOW`

For example, the following are valid cron expressions:

- Daily at noon UTC: `cron(0 12 ? * * *)`
- Daily at midnight UTC: `cron(0 0 ? * * *)`

To support running every 6, 12 hours, the following are also supported:

`cron(0 [00-23]/[01-24] ? * * *)`

For example, the following are valid cron expressions:

- Every 12 hours, starting at 5pm UTC: `cron(0 17/12 ? * * *)`
- Every two hours starting at midnight: `cron(0 0/2 ? * * *)`

### Note

- Even though the cron expression is set to start at 5PM UTC, note that there could be a delay of 0-20 minutes from the actual requested time to run the execution.
- We recommend that if you would like a daily schedule, you do not provide this parameter. Amazon SageMaker AI will pick a time for running every day.

You can also specify the keyword `NOW` to run the monitoring job immediately, one time, without recurring.

DataAnalysisStartTime -> (string)

Sets the start time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to monitor the five hours of data in your dataset that precede the start of each monitoring job, you would specify: `"-PT5H"` .

The start time that you specify must not precede the end time that you specify by more than 24 hours. You specify the end time with the `DataAnalysisEndTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

DataAnalysisEndTime -> (string)

Sets the end time for a monitoring job window. Express this time as an offset to the times that you schedule your monitoring jobs to run. You schedule monitoring jobs with the `ScheduleExpression` parameter. Specify this offset in ISO 8601 duration format. For example, if you want to end the window one hour before the start of each monitoring job, you would specify: `"-PT1H"` .

The end time that you specify must not follow the start time that you specify by more than 24 hours. You specify the start time with the `DataAnalysisStartTime` parameter.

If you set `ScheduleExpression` to `NOW` , this parameter is required.

MonitoringJobDefinition -> (structure)

Defines the monitoring job.

BaselineConfig -> (structure)

Baseline configuration used to validate that the data conforms to the specified constraints and statistics

BaseliningJobName -> (string)

The name of the job that performs baselining for the monitoring job.

ConstraintsResource -> (structure)

The baseline constraint file in Amazon S3 that the current monitoring job should validated against.

S3Uri -> (string)

The Amazon S3 URI for the constraints resource.

StatisticsResource -> (structure)

The baseline statistics file in Amazon S3 that the current monitoring job should be validated against.

S3Uri -> (string)

The Amazon S3 URI for the statistics resource.

MonitoringInputs -> (list)

The array of inputs for the monitoring job. Currently we support monitoring an Amazon SageMaker AI Endpoint.

(structure)

The inputs for a monitoring job.

EndpointInput -> (structure)

The endpoint for a monitoring job.

EndpointName -> (string)

An endpoint in customerâs account which has enabled `DataCaptureConfig` enabled.

LocalPath -> (string)

Path to the filesystem where the endpoint data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an Amazon S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs substract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

BatchTransformInput -> (structure)

Input object for the batch transform job.

DataCapturedDestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

DatasetFormat -> (structure)

The dataset format for your batch transform job.

Csv -> (structure)

The CSV dataset used in the monitoring job.

Header -> (boolean)

Indicates if the CSV data has a header.

Json -> (structure)

The JSON dataset used in the monitoring job

Line -> (boolean)

Indicates if the file should be read as a JSON object per line.

Parquet -> (structure)

The Parquet dataset used in the monitoring job

LocalPath -> (string)

Path to the filesystem where the batch transform data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

MonitoringOutputConfig -> (structure)

The array of outputs from the monitoring job to be uploaded to Amazon S3.

MonitoringOutputs -> (list)

Monitoring outputs for monitoring jobs. This is where the output of the periodic monitoring jobs is uploaded.

(structure)

The output object for a monitoring job.

S3Output -> (structure)

The Amazon S3 storage location where the results of a monitoring job are saved.

S3Uri -> (string)

A URI that identifies the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job.

LocalPath -> (string)

The local path to the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job. LocalPath is an absolute path for the output data.

S3UploadMode -> (string)

Whether to upload the results of the monitoring job continuously or after the job completes.

KmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.

MonitoringResources -> (structure)

Identifies the resources, ML compute instances, and ML storage volumes to deploy for a monitoring job. In distributed processing, you specify more than one instance.

ClusterConfig -> (structure)

The configuration for the cluster resources used to run the processing job.

InstanceCount -> (integer)

The number of ML compute instances to use in the model monitoring job. For distributed processing jobs, specify a value greater than 1. The default value is 1.

InstanceType -> (string)

The ML compute instance type for the processing job.

VolumeSizeInGB -> (integer)

The size of the ML storage volume, in gigabytes, that you want to provision. You must specify sufficient ML storage for your scenario.

VolumeKmsKeyId -> (string)

The Key Management Service (KMS) key that Amazon SageMaker AI uses to encrypt data on the storage volume attached to the ML compute instance(s) that run the model monitoring job.

MonitoringAppSpecification -> (structure)

Configures the monitoring job to run a specified Docker container image.

ImageUri -> (string)

The container image to be run by the monitoring job.

ContainerEntrypoint -> (list)

Specifies the entrypoint for a container used to run the monitoring job.

(string)

ContainerArguments -> (list)

An array of arguments for the container used to run the monitoring job.

(string)

RecordPreprocessorSourceUri -> (string)

An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.

PostAnalyticsProcessorSourceUri -> (string)

An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.

StoppingCondition -> (structure)

Specifies a time limit for how long the monitoring job is allowed to run.

MaxRuntimeInSeconds -> (integer)

The maximum runtime allowed in seconds.

### Note

The `MaxRuntimeInSeconds` cannot exceed the frequency of the job. For data quality and model explainability, this can be up to 3600 seconds for an hourly schedule. For model bias and model quality hourly schedules, this can be up to 1800 seconds.

Environment -> (map)

Sets the environment variables in the Docker container.

key -> (string)

value -> (string)

NetworkConfig -> (structure)

Specifies networking options for an monitoring job.

EnableInterContainerTrafficEncryption -> (boolean)

Whether to encrypt all communications between distributed processing jobs. Choose `True` to encrypt communications. Encryption provides greater security for distributed processing jobs, but the processing might take longer.

EnableNetworkIsolation -> (boolean)

Whether to allow inbound and outbound network calls to and from the containers used for the processing job.

VpcConfig -> (structure)

Specifies an Amazon Virtual Private Cloud (VPC) that your SageMaker jobs, hosted models, and compute resources have access to. You can control access to and from your resources by configuring a VPC. For more information, see [Give SageMaker Access to Resources in your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html) .

SecurityGroupIds -> (list)

The VPC security group IDs, in the form `sg-xxxxxxxx` . Specify the security groups for the VPC that is specified in the `Subnets` field.

(string)

Subnets -> (list)

The ID of the subnets in the VPC to which you want to connect your training job or model. For information about the availability of specific instance types, see [Supported Instance Types and Availability Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/instance-types-az.html) .

(string)

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job definition to schedule.

MonitoringType -> (string)

The type of the monitoring job definition to schedule.

EndpointName -> (string)

The endpoint which is monitored.

MonitoringAlertSummaries -> (list)

A JSON array where each element is a summary for a monitoring alert.

(structure)

Provides summary information about a monitor alert.

MonitoringAlertName -> (string)

The name of a monitoring alert.

CreationTime -> (timestamp)

A timestamp that indicates when a monitor alert was created.

LastModifiedTime -> (timestamp)

A timestamp that indicates when a monitor alert was last updated.

AlertStatus -> (string)

The current status of an alert.

DatapointsToAlert -> (integer)

Within `EvaluationPeriod` , how many execution failures will raise an alert.

EvaluationPeriod -> (integer)

The number of most recent monitoring executions to consider when evaluating alert status.

Actions -> (structure)

A list of alert actions taken in response to an alert going into `InAlert` status.

ModelDashboardIndicator -> (structure)

An alert action taken to light up an icon on the Model Dashboard when an alert goes into `InAlert` status.

Enabled -> (boolean)

Indicates whether the alert action is turned on.

LastMonitoringExecutionSummary -> (structure)

Summary of information about the last monitoring job to run.

MonitoringScheduleName -> (string)

The name of the monitoring schedule.

ScheduledTime -> (timestamp)

The time the monitoring job was scheduled.

CreationTime -> (timestamp)

The time at which the monitoring job was created.

LastModifiedTime -> (timestamp)

A timestamp that indicates the last time the monitoring job was modified.

MonitoringExecutionStatus -> (string)

The status of the monitoring job.

ProcessingJobArn -> (string)

The Amazon Resource Name (ARN) of the monitoring job.

EndpointName -> (string)

The name of the endpoint used to run the monitoring job.

FailureReason -> (string)

Contains the reason a monitoring job failed, if it failed.

MonitoringJobDefinitionName -> (string)

The name of the monitoring job.

MonitoringType -> (string)

The type of the monitoring job.

BatchTransformInput -> (structure)

Input object for the batch transform job.

DataCapturedDestinationS3Uri -> (string)

The Amazon S3 location being used to capture the data.

DatasetFormat -> (structure)

The dataset format for your batch transform job.

Csv -> (structure)

The CSV dataset used in the monitoring job.

Header -> (boolean)

Indicates if the CSV data has a header.

Json -> (structure)

The JSON dataset used in the monitoring job

Line -> (boolean)

Indicates if the file should be read as a JSON object per line.

Parquet -> (structure)

The Parquet dataset used in the monitoring job

LocalPath -> (string)

Path to the filesystem where the batch transform data is available to the container.

S3InputMode -> (string)

Whether the `Pipe` or `File` is used as the input mode for transferring data for the monitoring job. `Pipe` mode is recommended for large datasets. `File` mode is useful for small files that fit in memory. Defaults to `File` .

S3DataDistributionType -> (string)

Whether input data distributed in Amazon S3 is fully replicated or sharded by an S3 key. Defaults to `FullyReplicated`

FeaturesAttribute -> (string)

The attributes of the input data that are the input features.

InferenceAttribute -> (string)

The attribute of the input data that represents the ground truth label.

ProbabilityAttribute -> (string)

In a classification problem, the attribute that represents the class probability.

ProbabilityThresholdAttribute -> (double)

The threshold for the class probability to be evaluated as a positive result.

StartTimeOffset -> (string)

If specified, monitoring jobs substract this time from the start time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

EndTimeOffset -> (string)

If specified, monitoring jobs subtract this time from the end time. For information about using offsets for scheduling monitoring jobs, see [Schedule Model Quality Monitoring Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality-schedule.html) .

ExcludeFeaturesAttribute -> (string)

The attributes of the input data to exclude from the analysis.

ModelCard -> (structure)

The model card for a model.

ModelCardArn -> (string)

The Amazon Resource Name (ARN) for a model card.

ModelCardName -> (string)

The name of a model card.

ModelCardVersion -> (integer)

The model card version.

ModelCardStatus -> (string)

The model card status.

SecurityConfig -> (structure)

The KMS Key ID (`KMSKeyId` ) for encryption of model card information.

KmsKeyId -> (string)

A Key Management Service [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) to use for encrypting a model card.

CreationTime -> (timestamp)

A timestamp that indicates when the model card was created.

CreatedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

LastModifiedTime -> (timestamp)

A timestamp that indicates when the model card was last updated.

LastModifiedBy -> (structure)

Information about the user who created or modified an experiment, trial, trial component, lineage group, project, or model card.

UserProfileArn -> (string)

The Amazon Resource Name (ARN) of the userâs profile.

UserProfileName -> (string)

The name of the userâs profile.

DomainId -> (string)

The domain associated with the user.

IamIdentity -> (structure)

The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.

Arn -> (string)

The Amazon Resource Name (ARN) of the IAM identity.

PrincipalId -> (string)

The ID of the principal that assumes the IAM identity.

SourceIdentity -> (string)

The person or application which assumes the IAM identity.

Tags -> (list)

The tags associated with a model card.

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

ModelId -> (string)

For models created in SageMaker, this is the model ARN. For models created outside of SageMaker, this is a user-customized string.

RiskRating -> (string)

A model cardâs risk rating. Can be low, medium, or high.

NextToken -> (string)

If the result of the previous `Search` request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request.

TotalHits -> (structure)

The total number of matching results.

Value -> (long)

The total number of matching results. This value may be exact or an estimate, depending on the `Relation` field.

Relation -> (string)

Indicates the relationship between the returned `Value` and the actual total number of matching results. Possible values are:

- `EqualTo` : The `Value` is the exact count of matching results.
- `GreaterThanOrEqualTo` : The `Value` is a lower bound of the actual count of matching results.