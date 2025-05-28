# gcloud tasks run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/run](https://cloud.google.com/sdk/gcloud/reference/tasks/run)*

**NAME**

: **gcloud tasks run - force a task to run now**

**SYNOPSIS**

: **`gcloud tasks run` `[TASK](https://cloud.google.com/sdk/gcloud/reference/tasks/run#TASK)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/run#--location)`=`LOCATION`] [`[--queue](https://cloud.google.com/sdk/gcloud/reference/tasks/run#--queue)`=`QUEUE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Force a task to run now.

**EXAMPLES**

: To run a task:

```
gcloud tasks run --queue=my-queue my-task
```

**POSITIONAL ARGUMENTS**

: **`TASK`**:
The task to run.

**FLAGS**

: **--location**:
The location where we want to manage the queue or task. If not specified, uses
the location of the current project's App Engine app if there is an associated
app.

**--queue**:
The queue the task belongs to.

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

**NOTES**

: These variants are also available:

```
gcloud alpha tasks run
```

```
gcloud beta tasks run
```