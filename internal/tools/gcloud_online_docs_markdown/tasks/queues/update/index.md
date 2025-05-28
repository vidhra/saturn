# gcloud tasks queues update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update)*

**NAME**

: **gcloud tasks queues update - update a Cloud Tasks queue**

**SYNOPSIS**

: **`gcloud tasks queues update` `[QUEUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#QUEUE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--location)`=`LOCATION`] [`[--clear-http-header-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-header-override)`     | `[--http-header-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-header-override)`=`HEADER_FIELD`: `[HEADER_VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#HEADER_VALUE)`] [`[--clear-http-method-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-method-override)`     | `[--http-method-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-method-override)`=`HTTP_METHOD_OVERRIDE`] [`[--clear-http-oauth-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-oauth-service-account-email-override)`     | `[--http-oauth-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-oauth-service-account-email-override)`=`HTTP_OAUTH_SERVICE_ACCOUNT_EMAIL_OVERRIDE`] [`[--clear-http-oauth-token-scope-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-oauth-token-scope-override)`     | `[--http-oauth-token-scope-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-oauth-token-scope-override)`=`HTTP_OAUTH_TOKEN_SCOPE_OVERRIDE`] [`[--clear-http-oidc-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-oidc-service-account-email-override)`     | `[--http-oidc-service-account-email-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-oidc-service-account-email-override)`=`HTTP_OIDC_SERVICE_ACCOUNT_EMAIL_OVERRIDE`] [`[--clear-http-oidc-token-audience-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-oidc-token-audience-override)`     | `[--http-oidc-token-audience-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-oidc-token-audience-override)`=`HTTP_OIDC_TOKEN_AUDIENCE_OVERRIDE`] [`[--clear-http-uri-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-http-uri-override)`     | `[--http-uri-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--http-uri-override)`=`KEY`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#VALUE)`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#KEY)`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#VALUE)`,…]] [`[--clear-log-sampling-ratio](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-log-sampling-ratio)`     | `[--log-sampling-ratio](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--log-sampling-ratio)`=`LOG_SAMPLING_RATIO`] [`[--clear-max-attempts](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-attempts)`     | `[--max-attempts](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-attempts)`=`MAX_ATTEMPTS`] [`[--clear-max-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-backoff)`     | `[--max-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-backoff)`=`MAX_BACKOFF`] [`[--clear-max-concurrent-dispatches](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-concurrent-dispatches)`     | `[--max-concurrent-dispatches](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-concurrent-dispatches)`=`MAX_CONCURRENT_DISPATCHES`] [`[--clear-max-dispatches-per-second](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-dispatches-per-second)`     | `[--max-dispatches-per-second](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-dispatches-per-second)`=`MAX_DISPATCHES_PER_SECOND`] [`[--clear-max-doublings](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-doublings)`     | `[--max-doublings](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-doublings)`=`MAX_DOUBLINGS`] [`[--clear-max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-max-retry-duration)`     | `[--max-retry-duration](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--max-retry-duration)`=`MAX_RETRY_DURATION`] [`[--clear-min-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-min-backoff)`     | `[--min-backoff](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--min-backoff)`=`MIN_BACKOFF`] [`[--clear-routing-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--clear-routing-override)`     | `[--routing-override](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#--routing-override)`=`KEY`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#VALUE)`,[…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/queues/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The flags available to this command represent the fields of a queue that are
mutable.

**EXAMPLES**

: To update a Cloud Tasks queue:

```
gcloud tasks queues update my-queue --clear-max-attempts --clear-max-retry-duration --clear-max-doublings --clear-min-backoff --clear-max-backoff --clear-max-dispatches-per-second --clear-max-concurrent-dispatches --clear-routing-override
```

**POSITIONAL ARGUMENTS**

: **`QUEUE`**:
The queue to update.

**FLAGS**

: **--location**:
The location where we want to manage the queue or task. If not specified, uses
the location of the current project's App Engine app if there is an associated
app.

**--clear-http-header-override**

**--clear-http-method-override**

**--clear-http-oauth-service-account-email-override**

**--clear-http-oauth-token-scope-override**

**--clear-http-oidc-service-account-email-override**

**--clear-http-oidc-token-audience-override**

**--clear-http-uri-override**

**--clear-log-sampling-ratio**

**--clear-max-attempts**

**--clear-max-backoff**

**--clear-max-concurrent-dispatches**

**--clear-max-dispatches-per-second**

**--clear-max-doublings**

**--clear-max-retry-duration**

**--clear-min-backoff**

**--clear-routing-override**

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
gcloud alpha tasks queues update
```

```
gcloud beta tasks queues update
```