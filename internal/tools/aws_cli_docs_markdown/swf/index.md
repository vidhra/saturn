# swfÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# swf

## Description

The Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that use Amazonâs cloud to coordinate work across distributed components. In Amazon SWF, a *task* represents a logical unit of work that is performed by a component of your workflow. Coordinating tasks in a workflow involves managing intertask dependencies, scheduling, and concurrency in accordance with the logical flow of the application.

Amazon SWF gives you full control over implementing tasks and coordinating them without worrying about underlying complexities such as tracking their progress and maintaining their state.

This documentation serves as reference only. For a broader overview of the Amazon SWF programming model, see the * [Amazon SWF Developer Guide](https://docs.aws.amazon.com/amazonswf/latest/developerguide/) * .

## Available Commands

- [count-closed-workflow-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-closed-workflow-executions.html)
- [count-open-workflow-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-open-workflow-executions.html)
- [count-pending-activity-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-pending-activity-tasks.html)
- [count-pending-decision-tasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/count-pending-decision-tasks.html)
- [delete-activity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/delete-activity-type.html)
- [delete-workflow-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/delete-workflow-type.html)
- [deprecate-activity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-activity-type.html)
- [deprecate-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-domain.html)
- [deprecate-workflow-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-workflow-type.html)
- [describe-activity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-activity-type.html)
- [describe-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html)
- [describe-workflow-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-execution.html)
- [describe-workflow-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-workflow-type.html)
- [get-workflow-execution-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/get-workflow-execution-history.html)
- [list-activity-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-activity-types.html)
- [list-closed-workflow-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-closed-workflow-executions.html)
- [list-domains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-domains.html)
- [list-open-workflow-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-open-workflow-executions.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-tags-for-resource.html)
- [list-workflow-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-workflow-types.html)
- [poll-for-activity-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/poll-for-activity-task.html)
- [poll-for-decision-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/poll-for-decision-task.html)
- [record-activity-task-heartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/record-activity-task-heartbeat.html)
- [register-activity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-activity-type.html)
- [register-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-domain.html)
- [register-workflow-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-workflow-type.html)
- [request-cancel-workflow-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/request-cancel-workflow-execution.html)
- [respond-activity-task-canceled](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/respond-activity-task-canceled.html)
- [respond-activity-task-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/respond-activity-task-completed.html)
- [respond-activity-task-failed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/respond-activity-task-failed.html)
- [respond-decision-task-completed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/respond-decision-task-completed.html)
- [signal-workflow-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/signal-workflow-execution.html)
- [start-workflow-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/start-workflow-execution.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/tag-resource.html)
- [terminate-workflow-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/terminate-workflow-execution.html)
- [undeprecate-activity-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-activity-type.html)
- [undeprecate-domain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-domain.html)
- [undeprecate-workflow-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-workflow-type.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/untag-resource.html)