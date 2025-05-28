# gcloud tasks create-app-engine-task  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task)*

**NAME**

: **gcloud tasks create-app-engine-task - create and add a task that targets App Engine**

**SYNOPSIS**

: **`gcloud tasks create-app-engine-task` [`[TASK_ID](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#TASK_ID)`] `[--queue](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--queue)`=`QUEUE` [`[--header](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--header)`=`HEADER_FIELD`: `[HEADER_VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#HEADER_VALUE)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--location)`=`LOCATION`] [`[--method](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--method)`=`METHOD`] [`[--relative-uri](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--relative-uri)`=`RELATIVE_URI`] [`[--routing](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--routing)`=`KEY`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#VALUE)`,[…]] [`[--schedule-time](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--schedule-time)`=`SCHEDULE_TIME`] [`[--body-content](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--body-content)`=`BODY_CONTENT`     | `[--body-file](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#--body-file)`=`BODY_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and add a task that targets App Engine.

**EXAMPLES**

: To create a task:

```
gcloud tasks create-app-engine-task --queue=my-queue --relative-uri=/handler-path my-task
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

**--relative-uri**:
The relative URI of the request. Must begin with "/" and must be a valid HTTP
relative URI. It can contain a path and query string arguments. If not
specified, then the root path "/" will be used.

**--routing**:
The route to be used for this task. KEY must be at least one of: [service,
version, instance]. Any missing keys will use the default.
Routing can be overridden by the queue-level `--routing-override`
flag.

**--schedule-time**:
The time when the task is scheduled to be first attempted. Defaults to "now" if
not specified.

**--body-content**

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
gcloud alpha tasks create-app-engine-task
```

```
gcloud beta tasks create-app-engine-task
```