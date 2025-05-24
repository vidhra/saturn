# get-savings-plan-purchase-recommendation-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plan-purchase-recommendation-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plan-purchase-recommendation-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# get-savings-plan-purchase-recommendation-details

## Description

Retrieves the details for a Savings Plan recommendation. These details include the hourly data-points that construct the cost, coverage, and utilization charts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/GetSavingsPlanPurchaseRecommendationDetails)

## Synopsis

```
get-savings-plan-purchase-recommendation-details
--recommendation-detail-id <value>
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

`--recommendation-detail-id` (string)

The ID that is associated with the Savings Plan recommendation.

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

RecommendationDetailId -> (string)

The ID that is associated with the Savings Plan recommendation.

RecommendationDetailData -> (structure)

Contains detailed information about a specific Savings Plan recommendation.

AccountScope -> (string)

The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to PAYER. If the value is LINKED, recommendations are calculated for individual member accounts only.

LookbackPeriodInDays -> (string)

How many days of previous usage that Amazon Web Services considers when making this recommendation.

SavingsPlansType -> (string)

The requested Savings Plan recommendation type.

TermInYears -> (string)

The term of the commitment in years.

PaymentOption -> (string)

The payment option for the commitment (for example, All Upfront or No Upfront).

AccountId -> (string)

The AccountID that the recommendation is generated for.

CurrencyCode -> (string)

The currency code that Amazon Web Services used to generate the recommendation and present potential savings.

InstanceFamily -> (string)

The instance family of the recommended Savings Plan.

Region -> (string)

The region the recommendation is generated for.

OfferingId -> (string)

The unique ID thatâs used to distinguish Savings Plans from one another.

GenerationTimestamp -> (string)

The period of time that you want the usage and costs for.

LatestUsageTimestamp -> (string)

The period of time that you want the usage and costs for.

CurrentAverageHourlyOnDemandSpend -> (string)

The average value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentMaximumHourlyOnDemandSpend -> (string)

The highest value of hourly On-Demand spend over the lookback period of the applicable usage type.

CurrentMinimumHourlyOnDemandSpend -> (string)

The lowest value of hourly On-Demand spend over the lookback period of the applicable usage type.

EstimatedAverageUtilization -> (string)

The estimated utilization of the recommended Savings Plan.

EstimatedMonthlySavingsAmount -> (string)

The estimated monthly savings amount based on the recommended Savings Plan.

EstimatedOnDemandCost -> (string)

The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.

EstimatedOnDemandCostWithCurrentCommitment -> (string)

The estimated On-Demand costs you expect with no additional commitment, based on your usage of the selected time period and the Savings Plan you own.

EstimatedROI -> (string)

The estimated return on investment thatâs based on the recommended Savings Plan that you purchased. This is calculated as estimatedSavingsAmount/estimatedSPCost*100.

EstimatedSPCost -> (string)

The cost of the recommended Savings Plan over the length of the lookback period.

EstimatedSavingsAmount -> (string)

The estimated savings amount thatâs based on the recommended Savings Plan over the length of the lookback period.

EstimatedSavingsPercentage -> (string)

The estimated savings percentage relative to the total cost of applicable On-Demand usage over the lookback period.

ExistingHourlyCommitment -> (string)

The existing hourly commitment for the Savings Plan type.

HourlyCommitmentToPurchase -> (string)

The recommended hourly commitment level for the Savings Plan type and the configuration thatâs based on the usage during the lookback period.

UpfrontCost -> (string)

The upfront cost of the recommended Savings Plan, based on the selected payment option.

CurrentAverageCoverage -> (string)

The average value of hourly coverage over the lookback period.

EstimatedAverageCoverage -> (string)

The estimated coverage of the recommended Savings Plan.

MetricsOverLookbackPeriod -> (list)

The related hourly cost, coverage, and utilization metrics over the lookback period.

(structure)

Contains the hourly metrics for the given recommendation over the lookback period.

StartTime -> (string)

The period of time that you want the usage and costs for.

EstimatedOnDemandCost -> (string)

The remaining On-Demand cost estimated to not be covered by the recommended Savings Plan, over the length of the lookback period.

CurrentCoverage -> (string)

The current amount of Savings Plans eligible usage that the Savings Plan covered.

EstimatedCoverage -> (string)

The estimated coverage amount based on the recommended Savings Plan.

EstimatedNewCommitmentUtilization -> (string)

The estimated utilization for the recommended Savings Plan.