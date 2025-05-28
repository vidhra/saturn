# gcloud tasks queues create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create)*

**NAME**

: **gcloud tasks queues create - create a Cloud Tasks queue**

**SYNOPSIS**

: **`gcloud tasks queues create` `[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#QUEUE)` [`[--http-header-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-header-override)`=`HEADER_FIELD`: `[HEADER_VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#HEADER_VALUE)`] [`[--http-method-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-method-override)`=`HTTP_METHOD_OVERRIDE`] [`[--http-uri-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-uri-override)`=`KEY`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#VALUE)`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#KEY)`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#VALUE)`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--location)`=`LOCATION`] [`[--log-sampling-ratio](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--log-sampling-ratio)`=`LOG_SAMPLING_RATIO`] [`[--max-attempts](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-attempts)`=`MAX_ATTEMPTS`] [`[--max-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-backoff)`=`MAX_BACKOFF`] [`[--max-concurrent-dispatches](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-concurrent-dispatches)`=`MAX_CONCURRENT_DISPATCHES`] [`[--max-dispatches-per-second](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-dispatches-per-second)`=`MAX_DISPATCHES_PER_SECOND`] [`[--max-doublings](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-doublings)`=`MAX_DOUBLINGS`] [`[--max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--max-retry-duration)`=`MAX_RETRY_DURATION`] [`[--min-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--min-backoff)`=`MIN_BACKOFF`] [`[--routing-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--routing-override)`=`KEY`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#VALUE)`,[…]] [[`[--http-oauth-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-oauth-service-account-email-override)`=`HTTP_OAUTH_SERVICE_ACCOUNT_EMAIL_OVERRIDE` : `[--http-oauth-token-scope-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-oauth-token-scope-override)`=`HTTP_OAUTH_TOKEN_SCOPE_OVERRIDE`]     | [`[--http-oidc-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-oidc-service-account-email-override)`=`HTTP_OIDC_SERVICE_ACCOUNT_EMAIL_OVERRIDE` : `[--http-oidc-token-audience-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#--http-oidc-token-audience-override)`=`HTTP_OIDC_TOKEN_AUDIENCE_OVERRIDE`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The flags available to this command represent the fields of a queue that are
mutable.

**EXAMPLES**

: To create a Cloud Tasks queue:

```
gcloud tasks queues create my-queue --max-attempts=10 --max-retry-duration=5s --max-doublings=4 --min-backoff=1s --max-backoff=10s --max-dispatches-per-second=100 --max-concurrent-dispatches=10 --routing-override=service:abc
```

**POSITIONAL ARGUMENTS**

: **`QUEUE`**:
The queue to create.

**FLAGS**

: **--http-header-override**:
If provided, the specified HTTP headers override the existing headers for all
tasks in the queue. If a task has a header with the same Key as a queue-level
header override, then the value of the task header will be overriden with the
value of the queue-level header. Otherwise, the queue-level header will be added
to the task headers. Header values can contain commas. This flag can be
repeated. Repeated header fields will have their values overridden.

**--http-method-override**:
If provided, the specified HTTP method type override is used for all tasks in
the queue, no matter what is set at the task-level.

**--http-uri-override**:
If provided, the specified HTTP target URI override is used for all tasks in the
queue depending on what is set as the mode. Allowed values for mode are: ALWAYS,
IF_NOT_EXISTS. If not set, mode defaults to ALWAYS.
KEY must be at least one of: [scheme, host, port, path, query, mode]. Any
missing keys will use the default.

**--location**:
The location where we want to manage the queue or task. If not specified, uses
the location of the current project's App Engine app if there is an associated
app.

**--log-sampling-ratio**:
Specifies the fraction of operations to write to Cloud Logging. This field may
contain any value between 0.0 and 1.0, inclusive. 0.0 is the default and means
that no operations are logged.

**--max-attempts**:
The maximum number of attempts per task in the queue.

**--max-backoff**:
The maximum amount of time to wait before retrying a task after it fails. Must
be a string that ends in 's', such as "5s".

**--max-concurrent-dispatches**:
The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched
for this queue. After this threshold has been reached, Cloud Tasks stops
dispatching tasks until the number of outstanding requests decreases.

**--max-dispatches-per-second**:
The maximum rate at which tasks are dispatched from this queue.

**--max-doublings**:
The time between retries will double maxDoublings times.
A tasks retry interval starts at minBackoff, then doubles maxDoublings times,
then increases linearly, and finally retries retries at intervals of maxBackoff
up to maxAttempts times.
For example, if minBackoff is 10s, maxBackoff is 300s, and maxDoublings is 3,
then the a task will first be retried in 10s. The retry interval will double
three times, and then increase linearly by 2^3 * 10s. Finally, the task will
retry at intervals of maxBackoff until the task has been attempted maxAttempts
times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s,
300s.

**--max-retry-duration**:
The time limit for retrying a failed task, measured from when the task was first
run. Once the `--max-retry-duration` time has passed and the task has
been attempted --max-attempts times, no further attempts will be made and the
task will be deleted.
Must be a string that ends in 's', such as "5s".

**--min-backoff**:
The minimum amount of time to wait before retrying a task after it fails. Must
be a string that ends in 's', such as "5s".

**--routing-override**:
If provided, the specified App Engine route is used for all tasks in the queue,
no matter what is set is at the task-level.
KEY must be at least one of: [service, version, instance]. Any missing keys will
use the default.

**If specified, all `Authorization` headers in the HttpRequest.headers
field will be overridden for any tasks executed on this queue.
At most one of these can be specified:

**--http-oauth-service-account-email-override**

**--http-oidc-service-account-email-override****

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
gcloud alpha tasks queues create
```

```
gcloud beta tasks queues create
```