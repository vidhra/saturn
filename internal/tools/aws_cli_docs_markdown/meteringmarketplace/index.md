# meteringmarketplaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# meteringmarketplace

## Description

This reference provides descriptions of the low-level Marketplace Metering Service API.

Amazon Web Services Marketplace sellers can use this API to submit usage data for custom usage dimensions.

For information about the permissions that you need to use this API, see [Amazon Web Services Marketplace metering and entitlement API permissions](https://docs.aws.amazon.com/marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.html) in the *Amazon Web Services Marketplace Seller Guide.*

**Submitting metering records**

*MeterUsage*

- Submits the metering record for an Amazon Web Services Marketplace product.
- Called from: Amazon Elastic Compute Cloud (Amazon EC2) instance or a container running on either Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS)
- Supported product types: Amazon Machine Images (AMIs) and containers
- Vendor-metered tagging: Supported allocation tagging

*BatchMeterUsage*

- Submits the metering record for a set of customers. `BatchMeterUsage` API calls are captured by CloudTrail. You can use CloudTrail to verify that the software as a subscription (SaaS) metering records that you sent are accurate by searching for records with the `eventName` of `BatchMeterUsage` . You can also use CloudTrail to audit records over time. For more information, see the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html) .
- Called from: SaaS applications
- Supported product type: SaaS
- Vendor-metered tagging: Supports allocation tagging

**Accepting new customers**

*ResolveCustomer*

- Resolves the registration token that the buyer submits through the browser during the registration process. Obtains a `CustomerIdentifier` along with the `CustomerAWSAccountId` and `ProductCode` .
- Called from: SaaS application during the registration process
- Supported product type: SaaS
- Vendor-metered tagging: Not applicable

**Entitlement and metering for paid container products**

*RegisteredUsage*

- Provides software entitlement and metering. Paid container software products sold through Amazon Web Services Marketplace must integrate with the Marketplace Metering Service and call the `RegisterUsage` operation. Free and Bring Your Own License model (BYOL) products for Amazon ECS or Amazon EKS arenât required to call `RegisterUsage` . However, you can do so if you want to receive usage data in your seller reports. For more information about using the `RegisterUsage` operation, see [Container-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html) .
- Called from: Paid container software products
- Supported product type: Containers
- Vendor-metered tagging: Not applicable

**Entitlement custom metering for container products**

- MeterUsage API is available in GovCloud Regions but only supports AMI FCP products in GovCloud Regions. Flexible Consumption Pricing (FCP) Container products arenât supported in GovCloud Regions: us-gov-west-1 and us-gov-east-1. For more information, see [Container-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html) .
- Custom metering for container products are called using the MeterUsage API. The API is used for FCP AMI and FCP Container product metering.

**Custom metering for Amazon EKS is available in 17 Amazon Web Services Regions**

- The metering service supports Amazon ECS and EKS for Flexible Consumption Pricing (FCP) products using MeterUsage API. Amazon ECS is supported in all Amazon Web Services Regions that MeterUsage API is available except for GovCloud.
- Amazon EKS is supported in the following: us-east-1, us-east-2, us-west-1, us-west-2, eu-west-1, eu-central-1, eu-west-2, eu-west-3, eu-north-1, ap-east-1, ap-southeast-1, ap-northeast-1, ap-southeast-2, ap-northeast-2, ap-south-1, ca-central-1, sa-east-1.

### Note

For questions about adding Amazon Web Services Regions for metering, contact [Amazon Web Services Marketplace Seller Operations](mailto://aws.amazon.com/marketplace/management/contact-us/) .

## Available Commands

- [batch-meter-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/batch-meter-usage.html)
- [meter-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/meter-usage.html)
- [register-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/register-usage.html)
- [resolve-customer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/resolve-customer.html)