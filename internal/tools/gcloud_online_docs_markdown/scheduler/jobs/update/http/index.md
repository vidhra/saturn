# gcloud scheduler jobs update http  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http)*

**NAME**

: **gcloud scheduler jobs update http - update a Cloud Scheduler job that triggers an action via HTTP**

**SYNOPSIS**

: **`gcloud scheduler jobs update http` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#JOB)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--location)`=`LOCATION`) [`[--attempt-deadline](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--attempt-deadline)`=`ATTEMPT_DEADLINE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--description)`=`DESCRIPTION`] [`[--http-method](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--http-method)`=`HTTP_METHOD`; default="post"] [`[--schedule](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--schedule)`=`SCHEDULE`] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--uri)`=`URI`] [`[--clear-auth-token](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-auth-token)`     | [`[--oauth-service-account-email](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--oauth-service-account-email)`=`OAUTH_SERVICE_ACCOUNT_EMAIL` : `[--oauth-token-scope](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--oauth-token-scope)`=`OAUTH_TOKEN_SCOPE`]     | [`[--oidc-service-account-email](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--oidc-service-account-email)`=`OIDC_SERVICE_ACCOUNT_EMAIL` : `[--oidc-token-audience](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--oidc-token-audience)`=`OIDC_TOKEN_AUDIENCE`]] [`[--clear-headers](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-headers)`     | `[--remove-headers](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--remove-headers)`=[`REMOVE_HEADERS`,…] `[--update-headers](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--update-headers)`=[`KEY`=`VALUE`,…]] [`[--clear-max-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-max-backoff)`     | `[--max-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--max-backoff)`=`MAX_BACKOFF`; default="1h"] [`[--clear-max-doublings](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-max-doublings)`     | `[--max-doublings](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--max-doublings)`=`MAX_DOUBLINGS`; default=16] [`[--clear-max-retry-attempts](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-max-retry-attempts)`     | `[--max-retry-attempts](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--max-retry-attempts)`=`MAX_RETRY_ATTEMPTS`] [`[--clear-max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-max-retry-duration)`     | `[--max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--max-retry-duration)`=`MAX_RETRY_DURATION`] [`[--clear-message-body](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-message-body)`     | `[--message-body](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--message-body)`=`MESSAGE_BODY`     | `[--message-body-from-file](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--message-body-from-file)`=`PATH_TO_FILE`] [`[--clear-min-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-min-backoff)`     | `[--min-backoff](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--min-backoff)`=`MIN_BACKOFF`; default="5s"] [`[--clear-time-zone](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--clear-time-zone)`     | `[--time-zone](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#--time-zone)`=`TIME_ZONE`; default="Etc/UTC"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/update/http#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Scheduler job that triggers an action via HTTP.

**EXAMPLES**

: Update my-job's retry attempt limit:

```
gcloud scheduler jobs update http my-job --max-retry-attempts=2
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

: **--attempt-deadline**:
The deadline for job attempts. If the request handler doesn't respond by this
dealine, the request is cancelled and the attempt is marked as failed. For
example, 20s.

**--description**:
Human-readable description of the job.

**--http-method**:
HTTP method to use for the request. `HTTP_METHOD` must be
one of: `delete`, `get`, `head`,
`post`, `put`.

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

**--uri**:
The full URI path that the request will be sent to. This string must begin with
either "http://" or "https://". For example, `http://acme.com` or
`https://acme.com/sales:8080`. Cloud Scheduler will encode some
characters for safety and compatibility. The maximum allowed URL length is 2083
characters after encoding.

**--clear-auth-token**

**--clear-headers**

**--clear-max-backoff**

**--clear-max-doublings**

**--clear-max-retry-attempts**

**--clear-max-retry-duration**

**--clear-message-body**

**--clear-min-backoff**

**--clear-time-zone**

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
gcloud alpha scheduler jobs update http
```

```
gcloud beta scheduler jobs update http
```