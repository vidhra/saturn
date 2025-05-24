# dynamodbÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# dynamodb

## Description

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you donât have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

With DynamoDB, you can create database tables that can store and retrieve any amount of data, and serve any level of request traffic. You can scale up or scale down your tablesâ throughput capacity without downtime or performance degradation, and use the Amazon Web Services Management Console to monitor resource utilization and performance metrics.

DynamoDB automatically spreads the data and traffic for your tables over a sufficient number of servers to handle your throughput and storage requirements, while maintaining consistent and fast performance. All of your data is stored on solid state disks (SSDs) and automatically replicated across multiple Availability Zones in an Amazon Web Services Region, providing built-in high availability and data durability.

## Available Commands

- [batch-execute-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-execute-statement.html)
- [batch-get-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-get-item.html)
- [batch-write-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-write-item.html)
- [create-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-backup.html)
- [create-global-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-global-table.html)
- [create-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/create-table.html)
- [delete-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-backup.html)
- [delete-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-item.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-resource-policy.html)
- [delete-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-table.html)
- [describe-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-backup.html)
- [describe-continuous-backups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-continuous-backups.html)
- [describe-contributor-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-contributor-insights.html)
- [describe-endpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-endpoints.html)
- [describe-export](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-export.html)
- [describe-global-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table.html)
- [describe-global-table-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-global-table-settings.html)
- [describe-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-import.html)
- [describe-kinesis-streaming-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-kinesis-streaming-destination.html)
- [describe-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-limits.html)
- [describe-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-table.html)
- [describe-table-replica-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-table-replica-auto-scaling.html)
- [describe-time-to-live](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-time-to-live.html)
- [disable-kinesis-streaming-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/disable-kinesis-streaming-destination.html)
- [enable-kinesis-streaming-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/enable-kinesis-streaming-destination.html)
- [execute-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/execute-statement.html)
- [execute-transaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/execute-transaction.html)
- [export-table-to-point-in-time](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/export-table-to-point-in-time.html)
- [get-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-item.html)
- [get-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-resource-policy.html)
- [import-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/import-table.html)
- [list-backups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-backups.html)
- [list-contributor-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-contributor-insights.html)
- [list-exports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-exports.html)
- [list-global-tables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-global-tables.html)
- [list-imports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-imports.html)
- [list-tables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tables.html)
- [list-tags-of-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/list-tags-of-resource.html)
- [put-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/put-item.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/put-resource-policy.html)
- [query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/query.html)
- [restore-table-from-backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/restore-table-from-backup.html)
- [restore-table-to-point-in-time](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/restore-table-to-point-in-time.html)
- [scan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/scan.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/tag-resource.html)
- [transact-get-items](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/transact-get-items.html)
- [transact-write-items](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/transact-write-items.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/untag-resource.html)
- [update-continuous-backups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-continuous-backups.html)
- [update-contributor-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-contributor-insights.html)
- [update-global-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table.html)
- [update-global-table-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-global-table-settings.html)
- [update-item](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-item.html)
- [update-kinesis-streaming-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-kinesis-streaming-destination.html)
- [update-table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table.html)
- [update-table-replica-auto-scaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-table-replica-auto-scaling.html)
- [update-time-to-live](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-time-to-live.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/wait/index.html)
- [wizard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/wizard/index.html)