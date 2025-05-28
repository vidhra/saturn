# gcloud scheduler jobs create pubsub  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub)*

**NAME**

: **gcloud scheduler jobs create pubsub - create a Cloud Scheduler job with a Pub/Sub target**

**SYNOPSIS**

: **`gcloud scheduler jobs create pubsub` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#JOB)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--location)`=`LOCATION`) `[--schedule](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--schedule)`=`SCHEDULE` `[--topic](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--topic)`=`TOPIC` (`[--attributes](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--attributes)`=`ATTRIBUTES` `[--message-body](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--message-body)`=`MESSAGE_BODY`     | `[--message-body-from-file](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--message-body-from-file)`=`PATH_TO_FILE`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--description)`=`DESCRIPTION`] [`[--max-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--max-backoff)`=`MAX_BACKOFF`; default="1h"] [`[--max-doublings](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--max-doublings)`=`MAX_DOUBLINGS`; default=16] [`[--max-retry-attempts](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--max-retry-attempts)`=`MAX_RETRY_ATTEMPTS`] [`[--max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--max-retry-duration)`=`MAX_RETRY_DURATION`] [`[--min-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--min-backoff)`=`MIN_BACKOFF`; default="5s"] [`[--time-zone](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#--time-zone)`=`TIME_ZONE`; default="Etc/UTC"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/pubsub#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Scheduler job with a Pub/Sub target.

**EXAMPLES**

: The following command creates a job that publishes a message with the body
'Hello' to the Pub/Sub topic 'cron-topic' every 3 hours:

```
gcloud scheduler jobs create pubsub my-job --schedule="0 */3 * * *" --topic=cron-topic --message-body="Hello"
```

**POSITIONAL ARGUMENTS**

: **Job resource - Job to create. The arguments in this group can be used to specify
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

**REQUIRED FLAGS**

: **--schedule**:
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

**--attributes**

**OPTIONAL FLAGS**

: **--description**:
Human-readable description of the job.

**--max-backoff**:
Maximum amount of time to wait before retrying a task after it fails. For
example, `10m`. Default is `1h`.

**--max-doublings**:
Maximum number of times that the interval between failed job retries will be
doubled before the increase becomes constant.

**--max-retry-attempts**:
Number of times to retry the request if it fails or times out. Must be in range
0-5 inclusive. Default is 0.

**--max-retry-duration**:
Time limit for retrying a failed task, measured from when the task was first
run. If specified with `--max-retry-attempts` greater than 0, the
task will be retried until both limits are reached. Default is 0 (which means
unlimited).

**--min-backoff**:
Minimum amount of time to wait before retrying a task after it fails. For
example, `10s`. Default is `5s`.

**--time-zone**:
Specifies the time zone to be used in interpreting --schedule. The value of this
field must be a time zone name from the tz database
(https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
Note that some time zones include a provision for daylight savings time. The
rules for daylight saving time are determined by the chosen time zone.
For UTC use the string "utc". Default is "utc".

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
gcloud alpha scheduler jobs create pubsub
```

```
gcloud beta scheduler jobs create pubsub
```