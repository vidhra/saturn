# gcloud run jobs executions tasks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe)*

**NAME**

: **gcloud run jobs executions tasks describe - obtain details about tasks**

**SYNOPSIS**

: **`gcloud run jobs executions tasks describe` `[TASK](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe#TASK)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions/tasks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Obtain details about tasks.

**EXAMPLES**

: To describe a task:

```
gcloud run jobs executions tasks describe my-task
```

**POSITIONAL ARGUMENTS**

: **Task resource - Task to describe. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `TASK` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TASK`**:
ID of the Task or fully qualified identifier for the Task.
To set the `tasks` attribute:

- provide the argument `TASK` on the command line.**

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

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
gcloud alpha run jobs executions tasks describe
```

```
gcloud beta run jobs executions tasks describe
```