# application-autoscalingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# application-autoscaling

## Description

With Application Auto Scaling, you can configure automatic scaling for the following resources:

- Amazon AppStream 2.0 fleets
- Amazon Aurora Replicas
- Amazon Comprehend document classification and entity recognizer endpoints
- Amazon DynamoDB tables and global secondary indexes throughput capacity
- Amazon ECS services
- Amazon ElastiCache replication groups (Redis OSS and Valkey) and Memcached clusters
- Amazon EMR clusters
- Amazon Keyspaces (for Apache Cassandra) tables
- Lambda function provisioned concurrency
- Amazon Managed Streaming for Apache Kafka broker storage
- Amazon Neptune clusters
- Amazon SageMaker endpoint variants
- Amazon SageMaker inference components
- Amazon SageMaker serverless endpoint provisioned concurrency
- Spot Fleets (Amazon EC2)
- Pool of WorkSpaces
- Custom resources provided by your own applications or services

To learn more about Application Auto Scaling, see the [Application Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) .

**API Summary**

The Application Auto Scaling service API includes three key sets of actions:

- Register and manage scalable targets - Register Amazon Web Services or custom resources as scalable targets (a resource that Application Auto Scaling can scale), set minimum and maximum capacity limits, and retrieve information on existing scalable targets.
- Configure and manage automatic scaling - Define scaling policies to dynamically scale your resources in response to CloudWatch alarms, schedule one-time or recurring scaling actions, and retrieve your recent scaling activity history.
- Suspend and resume scaling - Temporarily suspend and later resume automatic scaling by calling the [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) API action for any Application Auto Scaling scalable target. You can suspend and resume (individually or in combination) scale-out activities that are triggered by a scaling policy, scale-in activities that are triggered by a scaling policy, and scheduled scaling.

## Available Commands

- [delete-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scaling-policy.html)
- [delete-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scheduled-action.html)
- [deregister-scalable-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/deregister-scalable-target.html)
- [describe-scalable-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scalable-targets.html)
- [describe-scaling-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-activities.html)
- [describe-scaling-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-policies.html)
- [describe-scheduled-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scheduled-actions.html)
- [get-predictive-scaling-forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/get-predictive-scaling-forecast.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/list-tags-for-resource.html)
- [put-scaling-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scaling-policy.html)
- [put-scheduled-action](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scheduled-action.html)
- [register-scalable-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/register-scalable-target.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/untag-resource.html)