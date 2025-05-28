# gcloud tasks create-http-task  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task)*

**NAME**

: **gcloud tasks create-http-task - create and add a task that targets a HTTP endpoint**

**SYNOPSIS**

: **`gcloud tasks create-http-task` [`[TASK_ID](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#TASK_ID)`] `[--queue](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--queue)`=`QUEUE` `[--url](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--url)`=`URL` [`[--header](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--header)`=`HEADER_FIELD`: `[HEADER_VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#HEADER_VALUE)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--location)`=`LOCATION`] [`[--method](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--method)`=`METHOD`] [`[--schedule-time](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--schedule-time)`=`SCHEDULE_TIME`] [`[--body-content](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--body-content)`=`BODY_CONTENT`     | `[--body-file](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--body-file)`=`BODY_FILE`] [[`[--oauth-service-account-email](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--oauth-service-account-email)`=`OAUTH_SERVICE_ACCOUNT_EMAIL` : `[--oauth-token-scope](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--oauth-token-scope)`=`OAUTH_TOKEN_SCOPE`]     | [`[--oidc-service-account-email](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--oidc-service-account-email)`=`OIDC_SERVICE_ACCOUNT_EMAIL` : `[--oidc-token-audience](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#--oidc-token-audience)`=`OIDC_TOKEN_AUDIENCE`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and add a task that targets a HTTP endpoint.

**EXAMPLES**

: To create a task:

```
gcloud tasks create-http-task --queue=my-queue --url=http://example.com/handler-path my-task
```

**POSITIONAL ARGUMENTS**

: **[`TASK_ID`]**:
The task to create.
If not specified then the system will generate a random unique task ID.
Explicitly specifying a task ID enables task de-duplication. If a task's ID is
identical to that of an existing task or a task that was deleted or completed
recently then the call will fail.
Because there is an extra lookup cost to identify duplicate task names, tasks
created with IDs have significantly increased latency. Using hashed strings for
the task ID or for the prefix of the task ID is recommended.

**REQUIRED FLAGS**

: **--queue**:
The queue the task belongs to.

**--url**:
The full URL path that the request will be sent to. This string must begin with
either "http://" or "https://".

**OPTIONAL FLAGS**

: **--header**:
An HTTP request header. Header values can contain commas. This flag can be
repeated. Repeated header fields will have their values overridden.

**--location**:
The location where we want to manage the queue or task. If not specified, uses
the location of the current project's App Engine app if there is an associated
app.

**--method**:
The HTTP method to use for the request. If not specified, "POST" will be used.

**--schedule-time**:
The time when the task is scheduled to be first attempted. Defaults to "now" if
not specified.

**--body-content**

**--oauth-service-account-email**

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
gcloud alpha tasks create-http-task
```

```
gcloud beta tasks create-http-task
```