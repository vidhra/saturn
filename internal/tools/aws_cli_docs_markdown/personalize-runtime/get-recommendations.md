# get-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-runtime/get-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-runtime/get-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize-runtime/index.html#cli-aws-personalize-runtime) ]

# get-recommendations

## Description

Returns a list of recommended items. For campaigns, the campaignâs Amazon Resource Name (ARN) is required and the required user and item input depends on the recipe type used to create the solution backing the campaign as follows:

- USER_PERSONALIZATION - `userId` required, `itemId` not used
- RELATED_ITEMS - `itemId` required, `userId` not used

### Note

Campaigns that are backed by a solution created using a recipe of type PERSONALIZED_RANKING use the API.

For recommenders, the recommenderâs ARN is required and the required item and user input depends on the use case (domain-based recipe) backing the recommender. For information on use case requirements see [Choosing recommender use cases](https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-runtime-2018-05-22/GetRecommendations)

## Synopsis

```
get-recommendations
[--campaign-arn <value>]
[--item-id <value>]
[--user-id <value>]
[--num-results <value>]
[--context <value>]
[--filter-arn <value>]
[--filter-values <value>]
[--recommender-arn <value>]
[--promotions <value>]
[--metadata-columns <value>]
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

`--campaign-arn` (string)

The Amazon Resource Name (ARN) of the campaign to use for getting recommendations.

`--item-id` (string)

The item ID to provide recommendations for.

Required for `RELATED_ITEMS` recipe type.

`--user-id` (string)

The user ID to provide recommendations for.

Required for `USER_PERSONALIZATION` recipe type.

`--num-results` (integer)

The number of results to return. The default is 25. If you are including metadata in recommendations, the maximum is 50. Otherwise, the maximum is 500.

`--context` (map)

The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a userâs recommendations, such as the userâs current location or device type.

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

`--filter-arn` (string)

The ARN of the filter to apply to the returned recommendations. For more information, see [Filtering Recommendations](https://docs.aws.amazon.com/personalize/latest/dg/filter.html) .

When using this parameter, be sure the filter resource is `ACTIVE` .

`--filter-values` (map)

The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.

For filter expressions that use an `INCLUDE` element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an `EXCLUDE` element to exclude items, you can omit the `filter-values` .In this case, Amazon Personalize doesnât use that portion of the expression to filter recommendations.

For more information, see [Filtering recommendations and user segments](https://docs.aws.amazon.com/personalize/latest/dg/filter.html) .

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

`--recommender-arn` (string)

The Amazon Resource Name (ARN) of the recommender to use to get recommendations. Provide a recommender ARN if you created a Domain dataset group with a recommender for a domain use case.

`--promotions` (list)

The promotions to apply to the recommendation request. A promotion defines additional business rules that apply to a configurable subset of recommended items.

(structure)

Contains information on a promotion. A promotion defines additional business rules that apply to a configurable subset of recommended items.

name -> (string)

The name of the promotion.

percentPromotedItems -> (integer)

The percentage of recommended items to apply the promotion to.

filterArn -> (string)

The Amazon Resource Name (ARN) of the filter used by the promotion. This filter defines the criteria for promoted items. For more information, see [Promotion filters](https://docs.aws.amazon.com/personalize/latest/dg/promoting-items.html#promotion-filters) .

filterValues -> (map)

The values to use when promoting items. For each placeholder parameter in your promotionâs filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.

For filter expressions that use an `INCLUDE` element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an `EXCLUDE` element to exclude items, you can omit the `filter-values` . In this case, Amazon Personalize doesnât use that portion of the expression to filter recommendations.

For more information on creating filters, see [Filtering recommendations and user segments](https://docs.aws.amazon.com/personalize/latest/dg/filter.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
name=string,percentPromotedItems=integer,filterArn=string,filterValues={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "percentPromotedItems": integer,
    "filterArn": "string",
    "filterValues": {"string": "string"
      ...}
  }
  ...
]
```

`--metadata-columns` (map)

If you enabled metadata in recommendations when you created or updated the campaign or recommender, specify the metadata columns from your Items dataset to include in item recommendations. The map key is `ITEMS` and the value is a list of column names from your Items dataset. The maximum number of columns you can provide is 10.

For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata) . For information about enabling metadata for a recommender, see [Enabling metadata in recommendations for a recommender](https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata) .

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
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

itemList -> (list)

A list of recommendations sorted in descending order by prediction score. There can be a maximum of 500 items in the list.

(structure)

An object that identifies an item.

The and APIs return a list of `PredictedItem` s.

itemId -> (string)

The recommended item ID.

score -> (double)

A numeric representation of the modelâs certainty that the item will be the next user selection. For more information on scoring logic, see  how-scores-work .

promotionName -> (string)

The name of the promotion that included the predicted item.

metadata -> (map)

Metadata about the item from your Items dataset.

key -> (string)

value -> (string)

reason -> (list)

If you use User-Personalization-v2, a list of reasons for why the item was included in recommendations. Possible reasons include the following:

- Promoted item - Indicates the item was included as part of a promotion that you applied in your recommendation request.
- Exploration - Indicates the item was included with exploration. With exploration, recommendations include items with less interactions data or relevance for the user. For more information about exploration, see [Exploration](https://docs.aws.amazon.com/personalize/latest/dg/use-case-recipe-features.html#about-exploration) .
- Popular item - Indicates the item was included as a placeholder popular item. If you use a filter, depending on how many recommendations the filter removes, Amazon Personalize might add placeholder items to meet the `numResults` for your recommendation request. These items are popular items, based on interactions data, that satisfy your filter criteria. They donât have a relevance score for the user.

(string)

recommendationId -> (string)

The ID of the recommendation.