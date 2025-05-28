# gcloud tasks buffer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/buffer](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer)*

**NAME**

: **gcloud tasks buffer - buffers a task into a queue**

**SYNOPSIS**

: **`gcloud tasks buffer` `[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer#--location)`=`LOCATION` `[--queue](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer#--queue)`=`QUEUE` [`[--task-id](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer#--task-id)`=`TASK_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Buffers a task into a queue.

**EXAMPLES**

: To buffer into a queue:

```
gcloud tasks buffer --queue=my-queue --location=us-central1
```

**REQUIRED FLAGS**

: **--location**:
The location where the queue exists.

**--queue**:
The queue the task belongs to.

**OPTIONAL FLAGS**

: **--task-id**:
The task ID for the task being created.

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
gcloud alpha tasks buffer
```

```
gcloud beta tasks buffer
```