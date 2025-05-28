# gcloud scheduler jobs update pubsub  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub)*

**NAME**

: **gcloud scheduler jobs update pubsub - update a Cloud Scheduler job with a Pub/Sub target**

**SYNOPSIS**

: **`gcloud scheduler jobs update pubsub` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#JOB)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--description)`=`DESCRIPTION`] [`[--schedule](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--schedule)`=`SCHEDULE`] [`[--topic](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--topic)`=`TOPIC`] [`[--clear-attributes](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-attributes)`     | `[--remove-attributes](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--remove-attributes)`=[`REMOVE_ATTRIBUTES`,…] `[--update-attributes](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--update-attributes)`=[`KEY`=`VALUE`,…]] [`[--clear-max-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-max-backoff)`     | `[--max-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--max-backoff)`=`MAX_BACKOFF`; default="1h"] [`[--clear-max-doublings](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-max-doublings)`     | `[--max-doublings](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--max-doublings)`=`MAX_DOUBLINGS`; default=16] [`[--clear-max-retry-attempts](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-max-retry-attempts)`     | `[--max-retry-attempts](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--max-retry-attempts)`=`MAX_RETRY_ATTEMPTS`] [`[--clear-max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-max-retry-duration)`     | `[--max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--max-retry-duration)`=`MAX_RETRY_DURATION`] [`[--clear-min-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-min-backoff)`     | `[--min-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--min-backoff)`=`MIN_BACKOFF`; default="5s"] [`[--clear-time-zone](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--clear-time-zone)`     | `[--time-zone](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--time-zone)`=`TIME_ZONE`; default="Etc/UTC"] [`[--message-body](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--message-body)`=`MESSAGE_BODY`     | `[--message-body-from-file](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#--message-body-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/pubsub#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Scheduler job with a Pub/Sub target.

**EXAMPLES**

: Update my-job's retry attempt limit:

```
gcloud scheduler jobs update pubsub my-job --max-retry-attempts=2
```

**POSITIONAL ARGUMENTS**

: **Job resource - Job to update. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`JOB`**:
ID of the job or fully qualified identifier for the job.
To set the `job` attribute:

- provide the argument `job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the job. By default, uses the location of the current project's
App Engine app if there is an associated app.
To set the `location` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- defaults to App Engine's app location if not provided & an app exists.**

**FLAGS**

: **--description**:
Human-readable description of the job.

**--schedule**:
Schedule on which the job will be executed.
As a general rule, execution `n + 1` of a job will not begin until
execution `n` has finished. Cloud Scheduler will never allow two
simultaneously outstanding executions. For example, this implies that if the
`n+1` execution is scheduled to run at `16:00` but the
`n` execution takes until `16:15`, the `n+1`
execution will not start until `16:15`. A scheduled start time will
be delayed if the previous execution has not ended when its scheduled time
occurs.
If --retry-count > 0 and a job attempt fails, the job will be tried a total
of --retry-count times, with exponential backoff, until the next scheduled start
time.
The schedule can be either of the following types:

- Crontab: [http://en.wikipedia.org/wiki/Cron#Overview](http://en.wikipedia.org/wiki/Cron#Overview)
- English-like schedule: [https://cloud.google.com/scheduler/docs/quickstart#defining_the_job_schedule](https://cloud.google.com/scheduler/docs/quickstart#defining_the_job_schedule)

**--topic**:
Name of the Google Cloud Pub/Sub topic to publish to when the job runs.

**--clear-attributes**

**--clear-max-backoff**

**--clear-max-doublings**

**--clear-max-retry-attempts**

**--clear-max-retry-duration**

**--clear-min-backoff**

**--clear-time-zone**

**--message-body**

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

: This command uses the `cloudscheduler/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/scheduler/](https://cloud.google.com/scheduler/)

**NOTES**

: These variants are also available:

```
gcloud alpha scheduler jobs update pubsub
```

```
gcloud beta scheduler jobs update pubsub
```