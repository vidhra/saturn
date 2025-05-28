# gcloud workflows execute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workflows/execute](https://cloud.google.com/sdk/gcloud/reference/workflows/execute)*

**NAME**

: **gcloud workflows execute - execute a workflow**

**SYNOPSIS**

: **`gcloud workflows execute` (`[WORKFLOW](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#WORKFLOW)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--location)`=`LOCATION`) [`[--call-log-level](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--call-log-level)`=`CALL_LOG_LEVEL`; default="none"] [`[--data](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--data)`=`DATA`] [`[--disable-concurrency-quota-overflow-buffering](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--disable-concurrency-quota-overflow-buffering)`] [`[--execution-history-level](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--execution-history-level)`=`EXECUTION_HISTORY_LEVEL`; default="none"] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workflows/execute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Execute a workflow.

**EXAMPLES**

: To execute a workflow named 'my-workflow' with the data that will be passed to
the workflow, run:

```
gcloud workflows execute my-workflow --data=my-data
```

**POSITIONAL ARGUMENTS**

: **Workflow resource - Name of the workflow to execute. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKFLOW`**:
ID of the workflow or fully qualified identifier for the workflow.
To set the `workflow` attribute:

- provide the argument `workflow` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the workflow. Alternatively, set the property
[workflows/location].
To set the `location` attribute:

- provide the argument `workflow` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `workflows/location`.**

**FLAGS**

: **--call-log-level**:
Level of call logging to apply during execution.
`CALL_LOG_LEVEL` must be one of:

**`log-all-calls`**:
Log all calls to subworkflows or library functions and their results.

**`log-errors-only`**:
Log when a call is stopped due to an exception.

**`log-none`**:
Perform no call logging.

**`none`**:
No call logging level specified.

**--data**:
JSON string with data that will be passed to the workflow as an argument.

**--disable-concurrency-quota-overflow-buffering**:
If set, the execution will not be backlogged when the concurrency quota is
exhausted. Backlogged executions start when the concurrency quota becomes
available.

**--execution-history-level**:
Level of execution history to apply during execution.
`EXECUTION_HISTORY_LEVEL` must be one of:

**`execution-history-basic`**:
Enable basic execution history.

**`execution-history-detailed`**:
Enable detailed execution history, including expected iterations and in-scope
variable values.

**`none`**:
No execution history level specified.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens,
underscores, lowercase characters, and numbers. Values must contain only
hyphens, underscores, lowercase characters, and numbers.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `workflowexecutions/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/workflows](https://cloud.google.com/workflows)

**NOTES**

: This variant is also available:

```
gcloud beta workflows execute
```