# gcloud tasks queues pause  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/pause](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/pause)*

**NAME**

: **gcloud tasks queues pause - pause a queue**

**SYNOPSIS**

: **`gcloud tasks queues pause` `[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/pause#QUEUE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/pause#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/pause#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If a queue is paused then the system will stop executing the tasks in the queue
until it is resumed. Tasks can still be added when the queue is paused.

**EXAMPLES**

: To pause a queue:

```
gcloud tasks queues pause my-queue
```

**POSITIONAL ARGUMENTS**

: **`QUEUE`**:
The queue to pause.

**FLAGS**

: **--location**:
The location where we want to manage the queue or task. If not specified, uses
the location of the current project's App Engine app if there is an associated
app.

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
gcloud alpha tasks queues pause
```

```
gcloud beta tasks queues pause
```