# gcloud scheduler jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create)*

**NAME**

: **gcloud scheduler jobs create - create Cloud Scheduler jobs for various types of targets**

**SYNOPSIS**

: **`gcloud scheduler jobs create` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create Cloud Scheduler jobs for various types of targets.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[app-engine](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/app-engine)`**:
Create a Cloud Scheduler job with an App Engine target.

**`[http](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/http)`**:
Create a Cloud Scheduler job that triggers an action via HTTP.

**`[pubsub](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub)`**:
Create a Cloud Scheduler job with a Pub/Sub target.

**NOTES**

: These variants are also available:

```
gcloud alpha scheduler jobs create
```

```
gcloud beta scheduler jobs create
```