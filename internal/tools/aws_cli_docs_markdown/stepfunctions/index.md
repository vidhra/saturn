# stepfunctionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# stepfunctions

## Description

Step Functions coordinates the components of distributed applications and microservices using visual workflows.

You can use Step Functions to build applications from individual components, each of which performs a discrete function, or *task* , allowing you to scale and change applications quickly. Step Functions provides a console that helps visualize the components of your application as a series of steps. Step Functions automatically triggers and tracks each step, and retries steps when there are errors, so your application executes predictably and in the right order every time. Step Functions logs the state of each step, so you can quickly diagnose and debug any issues.

Step Functions manages operations and underlying infrastructure to ensure your application is available at any scale. You can run tasks on Amazon Web Services, your own servers, or any system that has access to Amazon Web Services. You can access and use Step Functions using the console, the Amazon Web Services SDKs, or an HTTP API. For more information about Step Functions, see the * [Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) * .

### Warning

If you use the Step Functions API actions using Amazon Web Services SDK integrations, make sure the API actions are in camel case and parameter names are in Pascal case. For example, you could use Step Functions API action `startSyncExecution` and specify its parameter as `StateMachineArn` .

## Available Commands

- [create-activity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-activity.html)
- [create-state-machine](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html)
- [create-state-machine-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine-alias.html)
- [delete-activity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-activity.html)
- [delete-state-machine](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine.html)
- [delete-state-machine-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine-alias.html)
- [delete-state-machine-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine-version.html)
- [describe-activity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-activity.html)
- [describe-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-execution.html)
- [describe-map-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-map-run.html)
- [describe-state-machine](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html)
- [describe-state-machine-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine-alias.html)
- [describe-state-machine-for-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine-for-execution.html)
- [get-activity-task](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/get-activity-task.html)
- [get-execution-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/get-execution-history.html)
- [list-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-activities.html)
- [list-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-executions.html)
- [list-map-runs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-map-runs.html)
- [list-state-machine-aliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machine-aliases.html)
- [list-state-machine-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machine-versions.html)
- [list-state-machines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machines.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-tags-for-resource.html)
- [publish-state-machine-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/publish-state-machine-version.html)
- [redrive-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/redrive-execution.html)
- [send-task-failure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/send-task-failure.html)
- [send-task-heartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/send-task-heartbeat.html)
- [send-task-success](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/send-task-success.html)
- [start-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/start-execution.html)
- [start-sync-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/start-sync-execution.html)
- [stop-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/stop-execution.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/tag-resource.html)
- [test-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/test-state.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/untag-resource.html)
- [update-map-run](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-map-run.html)
- [update-state-machine](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine.html)
- [update-state-machine-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/update-state-machine-alias.html)
- [validate-state-machine-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/validate-state-machine-definition.html)