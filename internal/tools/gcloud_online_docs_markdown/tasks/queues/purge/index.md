# gcloud tasks queues purge  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/purge](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/purge)*

**NAME**

: **gcloud tasks queues purge - purge a queue by deleting all of its tasks**

**SYNOPSIS**

: **`gcloud tasks queues purge` `[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/purge#QUEUE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/purge#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/purge#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command purges a queue by deleting all of its tasks. Purge operations can
take up to one minute to take effect. Tasks might be dispatched before the purge
takes effect. A purge is irreversible. All tasks created before this command is
run are permanently deleted.

**EXAMPLES**

: To purge a queue:

```
gcloud tasks queues purge my-queue
```

**POSITIONAL ARGUMENTS**

: **`QUEUE`**:
The queue to purge.

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
gcloud alpha tasks queues purge
```

```
gcloud beta tasks queues purge
```