# describe-campaignÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-campaign.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-campaign.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# describe-campaign

## Description

Describes the given campaign, including its status.

A campaign can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

When the `status` is `CREATE FAILED` , the response includes the `failureReason` key, which describes why.

For more information on campaigns, see [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/DescribeCampaign)

## Synopsis

```
describe-campaign
--campaign-arn <value>
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

The Amazon Resource Name (ARN) of the campaign.

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

campaign -> (structure)

The properties of the campaign.

name -> (string)

The name of the campaign.

campaignArn -> (string)

The Amazon Resource Name (ARN) of the campaign.

solutionVersionArn -> (string)

The Amazon Resource Name (ARN) of the solution version the campaign uses.

minProvisionedTPS -> (integer)

Specifies the requested minimum provisioned transactions (recommendations) per second. A high `minProvisionedTPS` will increase your bill. We recommend starting with 1 for `minProvisionedTPS` (the default). Track your usage using Amazon CloudWatch metrics, and increase the `minProvisionedTPS` as necessary.

campaignConfig -> (structure)

The configuration details of a campaign.

itemExplorationConfig -> (map)

Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff` , you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your solution uses the [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) recipe.

key -> (string)

value -> (string)

enableMetadataWithRecommendations -> (boolean)

Whether metadata with recommendations is enabled for the campaign. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata) .

If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/) .

syncWithLatestSolutionVersion -> (boolean)

Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify `True` , you must specify the ARN of your *solution* for the `SolutionVersionArn` parameter. It must be in `SolutionArn/$LATEST` format. The default is `False` and you must manually update the campaign to deploy the latest solution version.

For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update) .

status -> (string)

The status of the campaign.

A campaign can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

failureReason -> (string)

If a campaign fails, the reason behind the failure.

creationDateTime -> (timestamp)

The date and time (in Unix format) that the campaign was created.

lastUpdatedDateTime -> (timestamp)

The date and time (in Unix format) that the campaign was last updated.

latestCampaignUpdate -> (structure)

Provides a summary of the properties of a campaign update. For a complete listing, call the [DescribeCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html) API.

solutionVersionArn -> (string)

The Amazon Resource Name (ARN) of the deployed solution version.

minProvisionedTPS -> (integer)

Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.

campaignConfig -> (structure)

The configuration details of a campaign.

itemExplorationConfig -> (map)

Specifies the exploration configuration hyperparameters, including `explorationWeight` and `explorationItemAgeCutOff` , you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide `itemExplorationConfig` data only if your solution uses the [User-Personalization](https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html) recipe.

key -> (string)

value -> (string)

enableMetadataWithRecommendations -> (boolean)

Whether metadata with recommendations is enabled for the campaign. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a campaign, see [Enabling metadata in recommendations for a campaign](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata) .

If you enable metadata in recommendations, you will incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/) .

syncWithLatestSolutionVersion -> (boolean)

Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify `True` , you must specify the ARN of your *solution* for the `SolutionVersionArn` parameter. It must be in `SolutionArn/$LATEST` format. The default is `False` and you must manually update the campaign to deploy the latest solution version.

For more information about automatic campaign updates, see [Enabling automatic campaign updates](https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update) .

status -> (string)

The status of the campaign update.

A campaign update can be in one of the following states:

- CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
- DELETE PENDING > DELETE IN_PROGRESS

failureReason -> (string)

If a campaign update fails, the reason behind the failure.

creationDateTime -> (timestamp)

The date and time (in Unix time) that the campaign update was created.

lastUpdatedDateTime -> (timestamp)

The date and time (in Unix time) that the campaign update was last updated.