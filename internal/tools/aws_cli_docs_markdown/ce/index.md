# ceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# ce

## Description

You can use the Cost Explorer API to programmatically query your cost and usage data. You can query for aggregated data such as total monthly costs or total daily usage. You can also query for granular data. This might include the number of daily write operations for Amazon DynamoDB database tables in your production environment.

Service Endpoint

The Cost Explorer API provides the following endpoint:

- `https://ce.us-east-1.amazonaws.com`

For information about the costs that are associated with the Cost Explorer API, see [Amazon Web Services Cost Management Pricing](http://aws.amazon.com/aws-cost-management/pricing/) .

## Available Commands

- [create-anomaly-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-monitor.html)
- [create-anomaly-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-anomaly-subscription.html)
- [create-cost-category-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-cost-category-definition.html)
- [delete-anomaly-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-anomaly-monitor.html)
- [delete-anomaly-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-anomaly-subscription.html)
- [delete-cost-category-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html)
- [describe-cost-category-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html)
- [get-anomalies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomalies.html)
- [get-anomaly-monitors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-monitors.html)
- [get-anomaly-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-anomaly-subscriptions.html)
- [get-approximate-usage-records](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-approximate-usage-records.html)
- [get-commitment-purchase-analysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-commitment-purchase-analysis.html)
- [get-cost-and-usage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-and-usage.html)
- [get-cost-and-usage-with-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-and-usage-with-resources.html)
- [get-cost-categories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-categories.html)
- [get-cost-forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-forecast.html)
- [get-dimension-values](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-dimension-values.html)
- [get-reservation-coverage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-coverage.html)
- [get-reservation-purchase-recommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-purchase-recommendation.html)
- [get-reservation-utilization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-utilization.html)
- [get-rightsizing-recommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-rightsizing-recommendation.html)
- [get-savings-plan-purchase-recommendation-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plan-purchase-recommendation-details.html)
- [get-savings-plans-coverage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-coverage.html)
- [get-savings-plans-purchase-recommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-purchase-recommendation.html)
- [get-savings-plans-utilization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-utilization.html)
- [get-savings-plans-utilization-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-savings-plans-utilization-details.html)
- [get-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-tags.html)
- [get-usage-forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-usage-forecast.html)
- [list-commitment-purchase-analyses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-commitment-purchase-analyses.html)
- [list-cost-allocation-tag-backfill-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-allocation-tag-backfill-history.html)
- [list-cost-allocation-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-allocation-tags.html)
- [list-cost-category-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html)
- [list-savings-plans-purchase-recommendation-generation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-savings-plans-purchase-recommendation-generation.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-tags-for-resource.html)
- [provide-anomaly-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/provide-anomaly-feedback.html)
- [start-commitment-purchase-analysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/start-commitment-purchase-analysis.html)
- [start-cost-allocation-tag-backfill](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/start-cost-allocation-tag-backfill.html)
- [start-savings-plans-purchase-recommendation-generation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/start-savings-plans-purchase-recommendation-generation.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/untag-resource.html)
- [update-anomaly-monitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-monitor.html)
- [update-anomaly-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-anomaly-subscription.html)
- [update-cost-allocation-tags-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-allocation-tags-status.html)
- [update-cost-category-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-category-definition.html)