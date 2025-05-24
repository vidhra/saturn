# codepipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# codepipeline

## Description

**Overview**

This is the CodePipeline API Reference. This guide provides descriptions of the actions and data types for CodePipeline. Some functionality for your pipeline can only be configured through the API. For more information, see the [CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) .

You can use the CodePipeline API to work with pipelines, stages, actions, and transitions.

*Pipelines* are models of automated release processes. Each pipeline is uniquely named, and consists of stages, actions, and transitions.

You can work with pipelines by calling:

- CreatePipeline , which creates a uniquely named pipeline.
- DeletePipeline , which deletes the specified pipeline.
- GetPipeline , which returns information about the pipeline structure and pipeline metadata, including the pipeline Amazon Resource Name (ARN).
- GetPipelineExecution , which returns information about a specific execution of a pipeline.
- GetPipelineState , which returns information about the current state of the stages and actions of a pipeline.
- ListActionExecutions , which returns action-level details for past executions. The details include full stage and action-level details, including individual action duration, status, any errors that occurred during the execution, and input and output artifact location details.
- ListPipelines , which gets a summary of all of the pipelines associated with your account.
- ListPipelineExecutions , which gets a summary of the most recent executions for a pipeline.
- StartPipelineExecution , which runs the most recent revision of an artifact through the pipeline.
- StopPipelineExecution , which stops the specified pipeline execution from continuing through the pipeline.
- UpdatePipeline , which updates a pipeline with edits or changes to the structure of the pipeline.

Pipelines include *stages* . Each stage contains one or more actions that must complete before the next stage begins. A stage results in success or failure. If a stage fails, the pipeline stops at that stage and remains stopped until either a new version of an artifact appears in the source location, or a user takes action to rerun the most recent artifact through the pipeline. You can call  GetPipelineState , which displays the status of a pipeline, including the status of stages in the pipeline, or  GetPipeline , which returns the entire structure of the pipeline, including the stages of that pipeline. For more information about the structure of stages and actions, see [CodePipeline Pipeline Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-structure.html) .

Pipeline stages include *actions* that are categorized into categories such as source or build actions performed in a stage of a pipeline. For example, you can use a source action to import artifacts into a pipeline from a source such as Amazon S3. Like stages, you do not work with actions directly in most cases, but you do define and interact with actions when working with pipeline operations such as  CreatePipeline and  GetPipelineState . Valid action categories are:

- Source
- Build
- Test
- Deploy
- Approval
- Invoke
- Compute

Pipelines also include *transitions* , which allow the transition of artifacts from one stage to the next in a pipeline after the actions in one stage complete.

You can work with transitions by calling:

- DisableStageTransition , which prevents artifacts from transitioning to the next stage in a pipeline.
- EnableStageTransition , which enables transition of artifacts between stages in a pipeline.

**Using the API to integrate with CodePipeline**

For third-party integrators or developers who want to create their own integrations with CodePipeline, the expected sequence varies from the standard API user. To integrate with CodePipeline, developers need to work with the following items:

**Jobs** , which are instances of an action. For example, a job for a source action might import a revision of an artifact from a source.

You can work with jobs by calling:

- AcknowledgeJob , which confirms whether a job worker has received the specified job.
- GetJobDetails , which returns the details of a job.
- PollForJobs , which determines whether there are any jobs to act on.
- PutJobFailureResult , which provides details of a job failure.
- PutJobSuccessResult , which provides details of a job success.

**Third party jobs** , which are instances of an action created by a partner action and integrated into CodePipeline. Partner actions are created by members of the Amazon Web Services Partner Network.

You can work with third party jobs by calling:

- AcknowledgeThirdPartyJob , which confirms whether a job worker has received the specified job.
- GetThirdPartyJobDetails , which requests the details of a job for a partner action.
- PollForThirdPartyJobs , which determines whether there are any jobs to act on.
- PutThirdPartyJobFailureResult , which provides details of a job failure.
- PutThirdPartyJobSuccessResult , which provides details of a job success.

## Available Commands

- [acknowledge-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-job.html)
- [acknowledge-third-party-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/acknowledge-third-party-job.html)
- [create-custom-action-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-custom-action-type.html)
- [create-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/create-pipeline.html)
- [delete-custom-action-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-custom-action-type.html)
- [delete-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-pipeline.html)
- [delete-webhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/delete-webhook.html)
- [deregister-webhook-with-third-party](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/deregister-webhook-with-third-party.html)
- [disable-stage-transition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/disable-stage-transition.html)
- [enable-stage-transition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/enable-stage-transition.html)
- [get-action-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-action-type.html)
- [get-job-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-job-details.html)
- [get-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline.html)
- [get-pipeline-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-execution.html)
- [get-pipeline-state](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-pipeline-state.html)
- [get-third-party-job-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/get-third-party-job-details.html)
- [list-action-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-executions.html)
- [list-action-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-action-types.html)
- [list-deploy-action-execution-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-deploy-action-execution-targets.html)
- [list-pipeline-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipeline-executions.html)
- [list-pipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-pipelines.html)
- [list-rule-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-executions.html)
- [list-rule-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-rule-types.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-tags-for-resource.html)
- [list-webhooks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/list-webhooks.html)
- [override-stage-condition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/override-stage-condition.html)
- [poll-for-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/poll-for-jobs.html)
- [poll-for-third-party-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/poll-for-third-party-jobs.html)
- [put-action-revision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-action-revision.html)
- [put-approval-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-approval-result.html)
- [put-job-failure-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-job-failure-result.html)
- [put-job-success-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-job-success-result.html)
- [put-third-party-job-failure-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-third-party-job-failure-result.html)
- [put-third-party-job-success-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-third-party-job-success-result.html)
- [put-webhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/put-webhook.html)
- [register-webhook-with-third-party](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/register-webhook-with-third-party.html)
- [retry-stage-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/retry-stage-execution.html)
- [rollback-stage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/rollback-stage.html)
- [start-pipeline-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html)
- [stop-pipeline-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/stop-pipeline-execution.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/untag-resource.html)
- [update-action-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/update-action-type.html)
- [update-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/update-pipeline.html)