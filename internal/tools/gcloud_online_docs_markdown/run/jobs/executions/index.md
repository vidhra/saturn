# gcloud run jobs executions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions)*

**NAME**

: **gcloud run jobs executions - view and manage your Cloud Run jobs executions**

**SYNOPSIS**

: **`gcloud run jobs executions` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your Cloud Run jobs
executions.

**EXAMPLES**

: To list your executions for a job, run:

```
gcloud run jobs executions list --job=my-job
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[tasks](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks)`**:
View and manage your Cloud Run jobs tasks.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/cancel)`**:
Cancel an execution.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/delete)`**:
Delete an execution.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/describe)`**:
Obtain details about executions.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/list)`**:
List executions.

**NOTES**

: These variants are also available:

```
gcloud alpha run jobs executions
```

```
gcloud beta run jobs executions
```