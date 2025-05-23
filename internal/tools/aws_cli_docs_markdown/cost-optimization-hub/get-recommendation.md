# get-recommendationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/get-recommendation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/get-recommendation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cost-optimization-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cost-optimization-hub/index.html#cli-aws-cost-optimization-hub) ]

# get-recommendation

## Description

Returns both the current and recommended resource configuration and the estimated cost impact for a recommendation.

The `recommendationId` is only valid for up to a maximum of 24 hours as recommendations are refreshed daily. To retrieve the `recommendationId` , use the `ListRecommendations` API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cost-optimization-hub-2022-07-26/GetRecommendation)

## Synopsis

```
get-recommendation
--recommendation-id <value>
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

`--recommendation-id` (string)

The ID for the recommendation.

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

recommendationId -> (string)

The ID for the recommendation.

resourceId -> (string)

The unique identifier for the resource. This is the same as the Amazon Resource Name (ARN), if available.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the resource.

accountId -> (string)

The account to which the recommendation applies.

currencyCode -> (string)

The currency code used for the recommendation.

recommendationLookbackPeriodInDays -> (integer)

The lookback period thatâs used to generate the recommendation.

costCalculationLookbackPeriodInDays -> (integer)

The lookback period used to calculate cost impact for a recommendation.

estimatedSavingsPercentage -> (double)

The estimated savings percentage relative to the total cost over the cost calculation lookback period.

estimatedSavingsOverCostCalculationLookbackPeriod -> (double)

The estimated savings amount over the lookback period used to calculate cost impact for a recommendation.

currentResourceType -> (string)

The type of resource.

recommendedResourceType -> (string)

The resource type of the recommendation.

region -> (string)

The Amazon Web Services Region of the resource.

source -> (string)

The source of the recommendation.

lastRefreshTimestamp -> (timestamp)

The time when the recommendation was last generated.

estimatedMonthlySavings -> (double)

The estimated monthly savings amount for the recommendation.

estimatedMonthlyCost -> (double)

The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.

implementationEffort -> (string)

The effort required to implement the recommendation.

restartNeeded -> (boolean)

Whether or not implementing the recommendation requires a restart.

actionType -> (string)

The type of action you can take by adopting the recommendation.

rollbackPossible -> (boolean)

Whether or not implementing the recommendation can be rolled back.

currentResourceDetails -> (tagged union structure)

The details for the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `lambdaFunction`, `ecsService`, `ec2Instance`, `ebsVolume`, `ec2AutoScalingGroup`, `ec2ReservedInstances`, `rdsReservedInstances`, `elastiCacheReservedInstances`, `openSearchReservedInstances`, `redshiftReservedInstances`, `ec2InstanceSavingsPlans`, `computeSavingsPlans`, `sageMakerSavingsPlans`, `rdsDbInstance`, `rdsDbInstanceStorage`, `dynamoDbReservedCapacity`, `memoryDbReservedInstances`.

lambdaFunction -> (structure)

The Lambda function recommendation details.

configuration -> (structure)

The Lambda function configuration used for recommendations.

compute -> (structure)

Details about the compute configuration.

vCpu -> (double)

The number of vCPU cores in the resource.

memorySizeInMB -> (integer)

The memory size of the resource.

architecture -> (string)

The architecture of the resource.

platform -> (string)

The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ecsService -> (structure)

The ECS service recommendation details.

configuration -> (structure)

The ECS service configuration used for recommendations.

compute -> (structure)

Details about the compute configuration.

vCpu -> (double)

The number of vCPU cores in the resource.

memorySizeInMB -> (integer)

The memory size of the resource.

architecture -> (string)

The architecture of the resource.

platform -> (string)

The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2Instance -> (structure)

The EC2 instance recommendation details.

configuration -> (structure)

The EC2 instance configuration used for recommendations.

instance -> (structure)

Details about the instance.

type -> (string)

The instance type of the configuration.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ebsVolume -> (structure)

The Amazon Elastic Block Store volume recommendation details.

configuration -> (structure)

The Amazon Elastic Block Store volume configuration used for recommendations.

storage -> (structure)

The disk storage of the Amazon Elastic Block Store volume.

type -> (string)

The storage type.

sizeInGb -> (double)

The storage volume.

performance -> (structure)

The Amazon Elastic Block Store performance configuration.

iops -> (double)

The number of I/O operations per second.

throughput -> (double)

The throughput that the volume supports.

attachmentState -> (string)

The Amazon Elastic Block Store attachment state.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2AutoScalingGroup -> (structure)

The EC2 Auto Scaling group recommendation details.

configuration -> (structure)

The EC2 Auto Scaling group configuration used for recommendations.

instance -> (structure)

Details about the instance for the EC2 Auto Scaling group with a single instance type.

type -> (string)

The instance type of the configuration.

mixedInstances -> (list)

A list of instance types for an EC2 Auto Scaling group with mixed instance types.

(structure)

The configuration for the EC2 Auto Scaling group with mixed instance types.

type -> (string)

The instance type of the configuration.

type -> (string)

The type of EC2 Auto Scaling group, showing whether it consists of a single instance type or mixed instance types.

allocationStrategy -> (string)

The strategy used for allocating instances, based on a predefined priority order or based on the lowest available price.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2ReservedInstances -> (structure)

The EC2 reserved instances recommendation details.

configuration -> (structure)

The EC2 reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

offeringClass -> (string)

Indicates whether the recommendation is for standard or convertible reservations.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

platform -> (string)

The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.

tenancy -> (string)

Determines whether the recommended reservation is dedicated or shared.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

rdsReservedInstances -> (structure)

The RDS reserved instances recommendation details.

configuration -> (structure)

The RDS reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing this instance costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

licenseModel -> (string)

The license model that the recommended reservation supports.

databaseEdition -> (string)

The database edition that the recommended reservation supports.

databaseEngine -> (string)

The database engine that the recommended reservation supports.

deploymentOption -> (string)

Determines whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

elastiCacheReservedInstances -> (structure)

The ElastiCache reserved instances recommendation details.

configuration -> (structure)

The ElastiCache reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

openSearchReservedInstances -> (structure)

The OpenSearch reserved instances recommendation details.

configuration -> (structure)

The OpenSearch reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

redshiftReservedInstances -> (structure)

The Redshift reserved instances recommendation details.

configuration -> (structure)

The Redshift reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

ec2InstanceSavingsPlans -> (structure)

The EC2 instance Savings Plans recommendation details.

configuration -> (structure)

The EC2 instance Savings Plans configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

instanceFamily -> (string)

The instance family of the recommended Savings Plan.

savingsPlansRegion -> (string)

The Amazon Web Services Region of the commitment.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

computeSavingsPlans -> (structure)

The Compute Savings Plans recommendation details.

configuration -> (structure)

Configuration details of the Compute Savings Plans to purchase.

accountScope -> (string)

The account scope for which you want recommendations. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to `PAYER` . If the value is `LINKED` , recommendations are calculated for individual member accounts only.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

sageMakerSavingsPlans -> (structure)

The SageMaker AI Savings Plans recommendation details.

configuration -> (structure)

The SageMaker Savings Plans configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

rdsDbInstance -> (structure)

The DB instance recommendation details.

configuration -> (structure)

The Amazon RDS DB instance configuration used for recommendations.

instance -> (structure)

Details about the instance configuration.

dbInstanceClass -> (string)

The DB instance class of the DB instance.

costCalculation -> (structure)

Cost impact of the resource recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

rdsDbInstanceStorage -> (structure)

The DB instance storage recommendation details.

configuration -> (structure)

The Amazon RDS DB instance storage configuration used for recommendations.

storageType -> (string)

The storage type to associate with the DB instance.

allocatedStorageInGb -> (double)

The new amount of storage in GB to allocate for the DB instance.

iops -> (double)

The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.

storageThroughput -> (double)

The storage throughput for the DB instance.

costCalculation -> (structure)

Cost impact of the resource recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

dynamoDbReservedCapacity -> (structure)

The DynamoDB reserved capacity recommendation details.

configuration -> (structure)

The DynamoDB reserved capacity configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved capacity recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this reserved capacity costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing this reserved capacity costs you on a monthly basis.

numberOfCapacityUnitsToPurchase -> (string)

The number of reserved capacity units that Amazon Web Services recommends that you purchase.

capacityUnits -> (string)

The capacity unit of the recommended reservation.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

memoryDbReservedInstances -> (structure)

The MemoryDB reserved instances recommendation details.

configuration -> (structure)

The MemoryDB reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing these reserved instances costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

instanceFamily -> (string)

The instance family of the recommended reservation.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

recommendedResourceDetails -> (tagged union structure)

The details about the recommended resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `lambdaFunction`, `ecsService`, `ec2Instance`, `ebsVolume`, `ec2AutoScalingGroup`, `ec2ReservedInstances`, `rdsReservedInstances`, `elastiCacheReservedInstances`, `openSearchReservedInstances`, `redshiftReservedInstances`, `ec2InstanceSavingsPlans`, `computeSavingsPlans`, `sageMakerSavingsPlans`, `rdsDbInstance`, `rdsDbInstanceStorage`, `dynamoDbReservedCapacity`, `memoryDbReservedInstances`.

lambdaFunction -> (structure)

The Lambda function recommendation details.

configuration -> (structure)

The Lambda function configuration used for recommendations.

compute -> (structure)

Details about the compute configuration.

vCpu -> (double)

The number of vCPU cores in the resource.

memorySizeInMB -> (integer)

The memory size of the resource.

architecture -> (string)

The architecture of the resource.

platform -> (string)

The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ecsService -> (structure)

The ECS service recommendation details.

configuration -> (structure)

The ECS service configuration used for recommendations.

compute -> (structure)

Details about the compute configuration.

vCpu -> (double)

The number of vCPU cores in the resource.

memorySizeInMB -> (integer)

The memory size of the resource.

architecture -> (string)

The architecture of the resource.

platform -> (string)

The platform of the resource. The platform is the specific combination of operating system, license model, and software on an instance.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2Instance -> (structure)

The EC2 instance recommendation details.

configuration -> (structure)

The EC2 instance configuration used for recommendations.

instance -> (structure)

Details about the instance.

type -> (string)

The instance type of the configuration.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ebsVolume -> (structure)

The Amazon Elastic Block Store volume recommendation details.

configuration -> (structure)

The Amazon Elastic Block Store volume configuration used for recommendations.

storage -> (structure)

The disk storage of the Amazon Elastic Block Store volume.

type -> (string)

The storage type.

sizeInGb -> (double)

The storage volume.

performance -> (structure)

The Amazon Elastic Block Store performance configuration.

iops -> (double)

The number of I/O operations per second.

throughput -> (double)

The throughput that the volume supports.

attachmentState -> (string)

The Amazon Elastic Block Store attachment state.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2AutoScalingGroup -> (structure)

The EC2 Auto Scaling group recommendation details.

configuration -> (structure)

The EC2 Auto Scaling group configuration used for recommendations.

instance -> (structure)

Details about the instance for the EC2 Auto Scaling group with a single instance type.

type -> (string)

The instance type of the configuration.

mixedInstances -> (list)

A list of instance types for an EC2 Auto Scaling group with mixed instance types.

(structure)

The configuration for the EC2 Auto Scaling group with mixed instance types.

type -> (string)

The instance type of the configuration.

type -> (string)

The type of EC2 Auto Scaling group, showing whether it consists of a single instance type or mixed instance types.

allocationStrategy -> (string)

The strategy used for allocating instances, based on a predefined priority order or based on the lowest available price.

costCalculation -> (structure)

Cost impact of the recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

ec2ReservedInstances -> (structure)

The EC2 reserved instances recommendation details.

configuration -> (structure)

The EC2 reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

offeringClass -> (string)

Indicates whether the recommendation is for standard or convertible reservations.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

platform -> (string)

The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.

tenancy -> (string)

Determines whether the recommended reservation is dedicated or shared.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

rdsReservedInstances -> (structure)

The RDS reserved instances recommendation details.

configuration -> (structure)

The RDS reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing this instance costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

licenseModel -> (string)

The license model that the recommended reservation supports.

databaseEdition -> (string)

The database edition that the recommended reservation supports.

databaseEngine -> (string)

The database engine that the recommended reservation supports.

deploymentOption -> (string)

Determines whether the recommendation is for a reservation in a single Availability Zone or a reservation with a backup in a second Availability Zone.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

elastiCacheReservedInstances -> (structure)

The ElastiCache reserved instances recommendation details.

configuration -> (structure)

The ElastiCache reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

openSearchReservedInstances -> (structure)

The OpenSearch reserved instances recommendation details.

configuration -> (structure)

The OpenSearch reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

redshiftReservedInstances -> (structure)

The Redshift reserved instances recommendation details.

configuration -> (structure)

The Redshift reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this instance costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceFamily -> (string)

The instance family of the recommended reservation.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

ec2InstanceSavingsPlans -> (structure)

The EC2 instance Savings Plans recommendation details.

configuration -> (structure)

The EC2 instance Savings Plans configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

instanceFamily -> (string)

The instance family of the recommended Savings Plan.

savingsPlansRegion -> (string)

The Amazon Web Services Region of the commitment.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

computeSavingsPlans -> (structure)

The Compute Savings Plans recommendation details.

configuration -> (structure)

Configuration details of the Compute Savings Plans to purchase.

accountScope -> (string)

The account scope for which you want recommendations. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to `PAYER` . If the value is `LINKED` , recommendations are calculated for individual member accounts only.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

sageMakerSavingsPlans -> (structure)

The SageMaker AI Savings Plans recommendation details.

configuration -> (structure)

The SageMaker Savings Plans configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

term -> (string)

The Savings Plans recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

hourlyCommitment -> (string)

The hourly commitment for the Savings Plans type.

costCalculation -> (structure)

Cost impact of the Savings Plans purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

monthlySavingsPlansEligibleCost -> (double)

The cost of paying for the recommended Savings Plan monthly.

estimatedMonthlyCommitment -> (double)

Estimated monthly commitment for the Savings Plan.

savingsPercentage -> (double)

Estimated savings as a percentage of your overall costs after buying the Savings Plan.

estimatedOnDemandCost -> (double)

Estimated On-Demand cost you will pay after buying the Savings Plan.

rdsDbInstance -> (structure)

The DB instance recommendation details.

configuration -> (structure)

The Amazon RDS DB instance configuration used for recommendations.

instance -> (structure)

Details about the instance configuration.

dbInstanceClass -> (string)

The DB instance class of the DB instance.

costCalculation -> (structure)

Cost impact of the resource recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

rdsDbInstanceStorage -> (structure)

The DB instance storage recommendation details.

configuration -> (structure)

The Amazon RDS DB instance storage configuration used for recommendations.

storageType -> (string)

The storage type to associate with the DB instance.

allocatedStorageInGb -> (double)

The new amount of storage in GB to allocate for the DB instance.

iops -> (double)

The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.

storageThroughput -> (double)

The storage throughput for the DB instance.

costCalculation -> (structure)

Cost impact of the resource recommendation.

usages -> (list)

Usage details of the resource recommendation.

(structure)

Details about the usage.

usageType -> (string)

The usage type.

usageAmount -> (double)

The usage amount.

operation -> (string)

The operation value.

productCode -> (string)

The product code.

unit -> (string)

The usage unit.

pricing -> (structure)

Pricing details of the resource recommendation.

estimatedCostBeforeDiscounts -> (double)

The savings estimate using Amazon Web Services public pricing without incorporating any discounts.

estimatedNetUnusedAmortizedCommitments -> (double)

The estimated net unused amortized commitment for the recommendation.

estimatedDiscounts -> (structure)

The estimated discounts for a recommendation.

savingsPlansDiscount -> (double)

Estimated Savings Plans discounts.

reservedInstancesDiscount -> (double)

Estimated reserved instance discounts.

otherDiscount -> (double)

Estimated other discounts include all discounts that are not itemized. Itemized discounts include `reservedInstanceDiscount` and `savingsPlansDiscount` .

estimatedCostAfterDiscounts -> (double)

The savings estimate incorporating all discounts with Amazon Web Services, such as Reserved Instances and Savings Plans.

dynamoDbReservedCapacity -> (structure)

The DynamoDB reserved capacity recommendation details.

configuration -> (structure)

The DynamoDB reserved capacity configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved capacity recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing this reserved capacity costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing this reserved capacity costs you on a monthly basis.

numberOfCapacityUnitsToPurchase -> (string)

The number of reserved capacity units that Amazon Web Services recommends that you purchase.

capacityUnits -> (string)

The capacity unit of the recommended reservation.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

memoryDbReservedInstances -> (structure)

The MemoryDB reserved instances recommendation details.

configuration -> (structure)

The MemoryDB reserved instances configuration used for recommendations.

accountScope -> (string)

The account scope for which you want recommendations.

service -> (string)

The service for which you want recommendations.

term -> (string)

The reserved instances recommendation term in years.

paymentOption -> (string)

The payment option for the commitment.

reservedInstancesRegion -> (string)

The Amazon Web Services Region of the commitment.

upfrontCost -> (string)

How much purchasing these reserved instances costs you upfront.

monthlyRecurringCost -> (string)

How much purchasing these reserved instances costs you on a monthly basis.

normalizedUnitsToPurchase -> (string)

The number of normalized units that Amazon Web Services recommends that you purchase.

numberOfInstancesToPurchase -> (string)

The number of instances that Amazon Web Services recommends that you purchase.

instanceType -> (string)

The type of instance that Amazon Web Services recommends.

instanceFamily -> (string)

The instance family of the recommended reservation.

sizeFlexEligible -> (boolean)

Determines whether the recommendation is size flexible.

currentGeneration -> (string)

Determines whether the recommendation is for a current generation instance.

costCalculation -> (structure)

Cost impact of the purchase recommendation.

pricing -> (structure)

Pricing details of the purchase recommendation.

estimatedOnDemandCost -> (double)

The remaining On-Demand cost estimated to not be covered by the recommended reserved instance, over the length of the lookback period.

monthlyReservationEligibleCost -> (double)

The cost of paying for the recommended reserved instance monthly.

savingsPercentage -> (double)

The savings percentage relative to the total On-Demand costs that are associated with this instance.

estimatedMonthlyAmortizedReservationCost -> (double)

The estimated cost of your recurring monthly fees for the recommended reserved instance across the month.

tags -> (list)

A list of tags associated with the resource for which the recommendation exists.

(structure)

The tag structure that contains a tag key and value.

key -> (string)

The key thatâs associated with the tag.

value -> (string)

The value thatâs associated with the tag.