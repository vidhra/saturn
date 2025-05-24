# datapipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# datapipeline

## Description

AWS Data Pipeline configures and manages a data-driven workflow called a pipeline. AWS Data Pipeline handles the details of scheduling and ensuring that data dependencies are met so that your application can focus on processing the data.

AWS Data Pipeline provides a JAR implementation of a task runner called AWS Data Pipeline Task Runner. AWS Data Pipeline Task Runner provides logic for common data management scenarios, such as performing database queries and running data analysis using Amazon Elastic MapReduce (Amazon EMR). You can use AWS Data Pipeline Task Runner as your task runner, or you can write your own task runner to provide custom data management.

AWS Data Pipeline implements two main sets of functionality. Use the first set to create a pipeline and define data sources, schedules, dependencies, and the transforms to be performed on the data. Use the second set in your task runner application to receive the next task ready for processing. The logic for performing the task, such as querying the data, running data analysis, or converting the data from one format to another, is contained within the task runner. The task runner performs the task assigned to it by the web service, reporting progress to the web service as it does so. When the task is done, the task runner reports the final success or failure of the task to the web service.

## Available Commands

- [activate-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html)
- [add-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/add-tags.html)
- [create-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html)
- [deactivate-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/deactivate-pipeline.html)
- [delete-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html)
- [describe-objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-objects.html)
- [describe-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html)
- [evaluate-expression](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/evaluate-expression.html)
- [get-pipeline-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/get-pipeline-definition.html)
- [list-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html)
- [list-runs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-runs.html)
- [poll-for-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/poll-for-task.html)
- [put-pipeline-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/put-pipeline-definition.html)
- [query-objects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/query-objects.html)
- [remove-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/remove-tags.html)
- [report-task-progress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/report-task-progress.html)
- [report-task-runner-heartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/report-task-runner-heartbeat.html)
- [set-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/set-status.html)
- [set-task-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/set-task-status.html)
- [validate-pipeline-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/validate-pipeline-definition.html)