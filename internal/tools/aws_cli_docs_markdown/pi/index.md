# piÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# pi

## Description

Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. The guide provides detailed information about Performance Insights data types, parameters and errors.

When Performance Insights is enabled, the Amazon RDS Performance Insights API provides visibility into the performance of your DB instance. Amazon CloudWatch provides the authoritative source for Amazon Web Services service-vended monitoring metrics. Performance Insights offers a domain-specific view of DB load.

DB load is measured as average active sessions. Performance Insights provides the data to API consumers as a two-dimensional time-series dataset. The time dimension provides DB load data for each time point in the queried time range. Each time point decomposes overall load in relation to the requested dimensions, measured at that time point. Examples include SQL, Wait event, User, and Host.

- To learn more about Performance Insights and Amazon Aurora DB instances, go to the * [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html) * .
- To learn more about Performance Insights and Amazon RDS DB instances, go to the * [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html) * .
- To learn more about Performance Insights and Amazon DocumentDB clusters, go to the * [Amazon DocumentDB Developer Guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/performance-insights.html) * .

## Available Commands

- [create-performance-analysis-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/create-performance-analysis-report.html)
- [delete-performance-analysis-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/delete-performance-analysis-report.html)
- [describe-dimension-keys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/describe-dimension-keys.html)
- [get-dimension-key-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-dimension-key-details.html)
- [get-performance-analysis-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-performance-analysis-report.html)
- [get-resource-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metadata.html)
- [get-resource-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/get-resource-metrics.html)
- [list-available-resource-dimensions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-dimensions.html)
- [list-available-resource-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-metrics.html)
- [list-performance-analysis-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-performance-analysis-reports.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/untag-resource.html)