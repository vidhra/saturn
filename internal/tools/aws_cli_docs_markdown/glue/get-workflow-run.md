# get-workflow-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-workflow-run

## Description

Retrieves the metadata for a given workflow run. Job run history is accessible for 90 days for your workflow and job run.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetWorkflowRun)

## Synopsis

```
get-workflow-run
--name <value>
--run-id <value>
[--include-graph | --no-include-graph]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--name` (string)

Name of the workflow being run.

`--run-id` (string)

The ID of the workflow run.

`--include-graph` | `--no-include-graph` (boolean)

Specifies whether to include the workflow graph in response or not.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

Run -> (structure)

The requested workflow run metadata.

Name -> (string)

Name of the workflow that was run.

WorkflowRunId -> (string)

The ID of this workflow run.

PreviousRunId -> (string)

The ID of the previous workflow run.

WorkflowRunProperties -> (map)

The workflow run properties which were set during the run.

key -> (string)

value -> (string)

StartedOn -> (timestamp)

The date and time when the workflow run was started.

CompletedOn -> (timestamp)

The date and time when the workflow run completed.

Status -> (string)

The status of the workflow run.

ErrorMessage -> (string)

This error message describes any error that may have occurred in starting the workflow run. Currently the only error message is âConcurrent runs exceeded for workflow: `foo` .â

Statistics -> (structure)

The statistics of the run.

TotalActions -> (integer)

Total number of Actions in the workflow run.

TimeoutActions -> (integer)

Total number of Actions that timed out.

FailedActions -> (integer)

Total number of Actions that have failed.

StoppedActions -> (integer)

Total number of Actions that have stopped.

SucceededActions -> (integer)

Total number of Actions that have succeeded.

RunningActions -> (integer)

Total number Actions in running state.

ErroredActions -> (integer)

Indicates the count of job runs in the ERROR state in the workflow run.

WaitingActions -> (integer)

Indicates the count of job runs in WAITING state in the workflow run.

Graph -> (structure)

The graph representing all the Glue components that belong to the workflow as nodes and directed connections between them as edges.

Nodes -> (list)

A list of the the Glue components belong to the workflow represented as nodes.

(structure)

A node represents an Glue component (trigger, crawler, or job) on a workflow graph.

Type -> (string)

The type of Glue component represented by the node.

Name -> (string)

The name of the Glue component represented by the node.

UniqueId -> (string)

The unique Id assigned to the node within the workflow.

TriggerDetails -> (structure)

Details of the Trigger when the node represents a Trigger.

Trigger -> (structure)

The information of the trigger represented by the trigger node.

Name -> (string)

The name of the trigger.

WorkflowName -> (string)

The name of the workflow associated with the trigger.

Id -> (string)

Reserved for future use.

Type -> (string)

The type of trigger that this is.

State -> (string)

The current state of the trigger.

Description -> (string)

A description of this trigger.

Schedule -> (string)

A `cron` expression used to specify the schedule (see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html) . For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)` .

Actions -> (list)

The actions initiated by this trigger.

(structure)

Defines an action to be initiated by a trigger.

JobName -> (string)

The name of a job to be run.

Arguments -> (map)

The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.

For information about how to specify and consume your own Job arguments, see the [Calling Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.

For information about the key-value pairs that Glue consumes to set up your job, see the [Special Parameters Used by Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.

key -> (string)

value -> (string)

Timeout -> (integer)

The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used with this action.

NotificationProperty -> (structure)

Specifies configuration properties of a job run notification.

NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.

CrawlerName -> (string)

The name of the crawler to be used with this action.

Predicate -> (structure)

The predicate of this trigger, which defines when it will fire.

Logical -> (string)

An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.

Conditions -> (list)

A list of the conditions that determine when the trigger will fire.

(structure)

Defines a condition under which a trigger fires.

LogicalOperator -> (string)

A logical operator.

JobName -> (string)

The name of the job whose `JobRuns` this condition applies to, and on which this trigger waits.

State -> (string)

The condition state. Currently, the only job states that a trigger can listen for are `SUCCEEDED` , `STOPPED` , `FAILED` , and `TIMEOUT` . The only crawler states that a trigger can listen for are `SUCCEEDED` , `FAILED` , and `CANCELLED` .

CrawlerName -> (string)

The name of the crawler to which this condition applies.

CrawlState -> (string)

The state of the crawler to which this condition applies.

EventBatchingCondition -> (structure)

Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.

BatchSize -> (integer)

Number of events that must be received from Amazon EventBridge before EventBridge event trigger fires.

BatchWindow -> (integer)

Window of time in seconds after which EventBridge event trigger fires. Window starts when first event is received.

JobDetails -> (structure)

Details of the Job when the node represents a Job.

JobRuns -> (list)

The information for the job runs represented by the job node.

(structure)

Contains information about a job run.

Id -> (string)

The ID of this job run.

Attempt -> (integer)

The number of the attempt to run this job.

PreviousRunId -> (string)

The ID of the previous run of this job. For example, the `JobRunId` specified in the `StartJobRun` action.

TriggerName -> (string)

The name of the trigger that started this job run.

JobName -> (string)

The name of the job definition being used in this run.

JobMode -> (string)

A mode that describes how a job was created. Valid values are:

- `SCRIPT` - The job was created using the Glue Studio script editor.
- `VISUAL` - The job was created using the Glue Studio visual editor.
- `NOTEBOOK` - The job was created using an interactive sessions notebook.

When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.

JobRunQueuingEnabled -> (boolean)

Specifies whether job run queuing is enabled for the job run.

A value of true means job run queuing is enabled for the job run. If false or not populated, the job run will not be considered for queueing.

StartedOn -> (timestamp)

The date and time at which this job run was started.

LastModifiedOn -> (timestamp)

The last time that this job run was modified.

CompletedOn -> (timestamp)

The date and time that this job run completed.

JobRunState -> (string)

The current state of the job run. For more information about the statuses of jobs that have terminated abnormally, see [Glue Job Run Statuses](https://docs.aws.amazon.com/glue/latest/dg/job-run-statuses.html) .

Arguments -> (map)

The job arguments associated with this run. For this job run, they replace the default arguments set in the job definition itself.

You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.

Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

For information about how to specify and consume your own Job arguments, see the [Calling Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.

For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.

For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.

key -> (string)

value -> (string)

ErrorMessage -> (string)

An error message associated with this job run.

PredecessorRuns -> (list)

A list of predecessors to this job run.

(structure)

A job run that was used in the predicate of a conditional trigger that triggered this job run.

JobName -> (string)

The name of the job definition used by the predecessor job run.

RunId -> (string)

The job-run ID of the predecessor job run.

AllocatedCapacity -> (integer)

This field is deprecated. Use `MaxCapacity` instead.

The number of Glue data processing units (DPUs) allocated to this JobRun. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

ExecutionTime -> (integer)

The amount of time (in seconds) that the job run consumed resources.

Timeout -> (integer)

The `JobRun` timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status. This value overrides the timeout value set in the parent job.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.

MaxCapacity -> (double)

For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

For Glue version 2.0+ jobs, you cannot specify a `Maximum capacity` . Instead, you should specify a `Worker type` and the `Number of workers` .

Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers` .

The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:

- When you specify a Python shell job (`JobCommand.Name` =âpythonshellâ), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
- When you specify an Apache Spark ETL job (`JobCommand.Name` =âglueetlâ) or Apache Spark streaming ETL job (`JobCommand.Name` =âgluestreamingâ), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.

WorkerType -> (string)

The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.

- For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
- For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
- For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
- For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the `G.4X` worker type.
- For the `G.025X` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.
- For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.

NumberOfWorkers -> (integer)

The number of workers of a defined `workerType` that are allocated when a job runs.

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used with this job run.

LogGroupName -> (string)

The name of the log group for secure logging that can be server-side encrypted in Amazon CloudWatch using KMS. This name can be `/aws-glue/jobs/` , in which case the default encryption is `NONE` . If you add a role name and `SecurityConfiguration` name (in other words, `/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/` ), then that security configuration is used to encrypt the log group.

NotificationProperty -> (structure)

Specifies configuration properties of a job run notification.

NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.

GlueVersion -> (string)

In Spark jobs, `GlueVersion` determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark.

Ray jobs should set `GlueVersion` to `4.0` or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the `Runtime` parameter of the Job command.

For more information about the available Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.

Jobs that are created without specifying a Glue version default to Glue 0.9.

DPUSeconds -> (double)

This field can be set for either job runs with execution class `FLEX` or when Auto Scaling is enabled, and represents the total time each executor ran during the lifecycle of a job run in seconds, multiplied by a DPU factor (1 for `G.1X` , 2 for `G.2X` , or 0.25 for `G.025X` workers). This value may be different than the `executionEngineRuntime` * `MaxCapacity` as in the case of Auto Scaling jobs, as the number of executors running at a given time may be less than the `MaxCapacity` . Therefore, it is possible that the value of `DPUSeconds` is less than `executionEngineRuntime` * `MaxCapacity` .

ExecutionClass -> (string)

Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.

Only jobs with Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX` . The flexible execution class is available for Spark jobs.

MaintenanceWindow -> (string)

This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to restart your streaming jobs.

Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

ProfileName -> (string)

The name of an Glue usage profile associated with the job run.

StateDetail -> (string)

This field holds details that pertain to the state of a job run. The field is nullable.

For example, when a job run is in a WAITING state as a result of job run queuing, the field has the reason why the job run is in that state.

CrawlerDetails -> (structure)

Details of the crawler when the node represents a crawler.

Crawls -> (list)

A list of crawls represented by the crawl node.

(structure)

The details of a crawl in the workflow.

State -> (string)

The state of the crawler.

StartedOn -> (timestamp)

The date and time on which the crawl started.

CompletedOn -> (timestamp)

The date and time on which the crawl completed.

ErrorMessage -> (string)

The error message associated with the crawl.

LogGroup -> (string)

The log group associated with the crawl.

LogStream -> (string)

The log stream associated with the crawl.

Edges -> (list)

A list of all the directed connections between the nodes belonging to the workflow.

(structure)

An edge represents a directed connection between two Glue components that are part of the workflow the edge belongs to.

SourceId -> (string)

The unique of the node within the workflow where the edge starts.

DestinationId -> (string)

The unique of the node within the workflow where the edge ends.

StartingEventBatchCondition -> (structure)

The batch condition that started the workflow run.

BatchSize -> (integer)

Number of events in the batch.

BatchWindow -> (integer)

Duration of the batch window in seconds.