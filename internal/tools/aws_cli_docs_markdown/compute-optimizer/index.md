# compute-optimizerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# compute-optimizer

## Description

Compute Optimizer is a service that analyzes the configuration and utilization metrics of your Amazon Web Services compute resources, such as Amazon EC2 instances, Amazon EC2 Auto Scaling groups, Lambda functions, Amazon EBS volumes, and Amazon ECS services on Fargate. It reports whether your resources are optimal, and generates optimization recommendations to reduce the cost and improve the performance of your workloads. Compute Optimizer also provides recent utilization metric data, in addition to projected utilization metric data for the recommendations, which you can use to evaluate which recommendation provides the best price-performance trade-off. The analysis of your usage patterns can help you decide when to move or resize your running resources, and still meet your performance and capacity requirements. For more information about Compute Optimizer, including the required permissions to use the service, see the [Compute Optimizer User Guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/) .

## Available Commands

- [delete-recommendation-preferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/delete-recommendation-preferences.html)
- [describe-recommendation-export-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/describe-recommendation-export-jobs.html)
- [export-auto-scaling-group-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-auto-scaling-group-recommendations.html)
- [export-ebs-volume-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-ebs-volume-recommendations.html)
- [export-ec2-instance-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-ec2-instance-recommendations.html)
- [export-ecs-service-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-ecs-service-recommendations.html)
- [export-idle-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-idle-recommendations.html)
- [export-lambda-function-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-lambda-function-recommendations.html)
- [export-license-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-license-recommendations.html)
- [export-rds-database-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/export-rds-database-recommendations.html)
- [get-auto-scaling-group-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-auto-scaling-group-recommendations.html)
- [get-ebs-volume-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ebs-volume-recommendations.html)
- [get-ec2-instance-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-instance-recommendations.html)
- [get-ec2-recommendation-projected-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ec2-recommendation-projected-metrics.html)
- [get-ecs-service-recommendation-projected-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendation-projected-metrics.html)
- [get-ecs-service-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-ecs-service-recommendations.html)
- [get-effective-recommendation-preferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-effective-recommendation-preferences.html)
- [get-enrollment-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-enrollment-status.html)
- [get-enrollment-statuses-for-organization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-enrollment-statuses-for-organization.html)
- [get-idle-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-idle-recommendations.html)
- [get-lambda-function-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-lambda-function-recommendations.html)
- [get-license-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-license-recommendations.html)
- [get-rds-database-recommendation-projected-metrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendation-projected-metrics.html)
- [get-rds-database-recommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-rds-database-recommendations.html)
- [get-recommendation-preferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-preferences.html)
- [get-recommendation-summaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-recommendation-summaries.html)
- [put-recommendation-preferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/put-recommendation-preferences.html)
- [update-enrollment-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/update-enrollment-status.html)