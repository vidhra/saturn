# gcloud run jobs executions tasks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks)*

**NAME**

: **gcloud run jobs executions tasks - view and manage your Cloud Run jobs tasks**

**SYNOPSIS**

: **`gcloud run jobs executions tasks` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your Cloud Run jobs tasks.

**EXAMPLES**

: To list your existing tasks for an execution, run:

```
gcloud run jobs executions tasks list --execution my_execution
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe)`**:
Obtain details about tasks.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/list)`**:
List tasks.

**NOTES**

: These variants are also available:

```
gcloud alpha run jobs executions tasks
```

```
gcloud beta run jobs executions tasks
```