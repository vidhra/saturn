# gcloud tasks queues resume  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/resume](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/resume)*

**NAME**

: **gcloud tasks queues resume - request to resume a paused or disabled queue**

**SYNOPSIS**

: **`gcloud tasks queues resume` `[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/resume#QUEUE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/resume#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/resume#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request to resume a paused or disabled queue.

**EXAMPLES**

: To resume a queue:

```
gcloud tasks queues resume my-queue
```

**POSITIONAL ARGUMENTS**

: **`QUEUE`**:
The queue to resume.

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
gcloud alpha tasks queues resume
```

```
gcloud beta tasks queues resume
```