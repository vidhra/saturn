# athenaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# athena

## Description

Amazon Athena is an interactive query service that lets you use standard SQL to analyze data directly in Amazon S3. You can point Athena at your data in Amazon S3 and run ad-hoc queries and get results in seconds. Athena is serverless, so there is no infrastructure to set up or manage. You pay only for the queries you run. Athena scales automaticallyâexecuting queries in parallelâso results are fast, even with large datasets and complex queries. For more information, see [What is Amazon Athena](http://docs.aws.amazon.com/athena/latest/ug/what-is.html) in the *Amazon Athena User Guide* .

If you connect to Athena using the JDBC driver, use version 1.1.0 of the driver or later with the Amazon Athena API. Earlier version drivers do not support the API. For more information and to download the driver, see [Accessing Amazon Athena with JDBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html) .

## Available Commands

- [batch-get-named-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-named-query.html)
- [batch-get-prepared-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-prepared-statement.html)
- [batch-get-query-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-query-execution.html)
- [cancel-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/cancel-capacity-reservation.html)
- [create-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-capacity-reservation.html)
- [create-data-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html)
- [create-named-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html)
- [create-notebook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-notebook.html)
- [create-prepared-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-prepared-statement.html)
- [create-presigned-notebook-url](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-presigned-notebook-url.html)
- [create-work-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html)
- [delete-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-capacity-reservation.html)
- [delete-data-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html)
- [delete-named-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-named-query.html)
- [delete-notebook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-notebook.html)
- [delete-prepared-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-prepared-statement.html)
- [delete-work-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-work-group.html)
- [export-notebook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/export-notebook.html)
- [get-calculation-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-calculation-execution.html)
- [get-calculation-execution-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-calculation-execution-code.html)
- [get-calculation-execution-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-calculation-execution-status.html)
- [get-capacity-assignment-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-capacity-assignment-configuration.html)
- [get-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-capacity-reservation.html)
- [get-data-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html)
- [get-database](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-database.html)
- [get-named-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html)
- [get-notebook-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-notebook-metadata.html)
- [get-prepared-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-prepared-statement.html)
- [get-query-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html)
- [get-query-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-results.html)
- [get-query-runtime-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-runtime-statistics.html)
- [get-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-session.html)
- [get-session-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-session-status.html)
- [get-table-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html)
- [get-work-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-work-group.html)
- [import-notebook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/import-notebook.html)
- [list-application-dpu-sizes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-application-dpu-sizes.html)
- [list-calculation-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-calculation-executions.html)
- [list-capacity-reservations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-capacity-reservations.html)
- [list-data-catalogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html)
- [list-databases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-databases.html)
- [list-engine-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-engine-versions.html)
- [list-executors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-executors.html)
- [list-named-queries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html)
- [list-notebook-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-notebook-metadata.html)
- [list-notebook-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-notebook-sessions.html)
- [list-prepared-statements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-prepared-statements.html)
- [list-query-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html)
- [list-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-sessions.html)
- [list-table-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-table-metadata.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-tags-for-resource.html)
- [list-work-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-work-groups.html)
- [put-capacity-assignment-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/put-capacity-assignment-configuration.html)
- [start-calculation-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-calculation-execution.html)
- [start-query-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html)
- [start-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-session.html)
- [stop-calculation-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/stop-calculation-execution.html)
- [stop-query-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/stop-query-execution.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/tag-resource.html)
- [terminate-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/terminate-session.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/untag-resource.html)
- [update-capacity-reservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-capacity-reservation.html)
- [update-data-catalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-data-catalog.html)
- [update-named-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-named-query.html)
- [update-notebook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-notebook.html)
- [update-notebook-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-notebook-metadata.html)
- [update-prepared-statement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-prepared-statement.html)
- [update-work-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html)