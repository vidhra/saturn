# gcloud batch tasks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe](https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe)*

**NAME**

: **gcloud batch tasks describe - show details of a task**

**SYNOPSIS**

: **`gcloud batch tasks describe` (`[TASK](https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe#TASK)` : `[--job](https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe#--job)`=`JOB` `[--location](https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe#--location)`=`LOCATION` `--task_group`=`TASK_GROUP`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/batch/tasks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The task specified does not exist.
- The active account does not have permission to access the given task.

**EXAMPLES**

: To print details of the task with name
`projects/foo/locations/us-central1/jobs/bar/taskGroups/group0/tasks/0`,
run:

```
gcloud batch tasks describe projects/foo/locations/us-central1/jobs/bar/taskGroups/group0/tasks/0
```

**POSITIONAL ARGUMENTS**

: **Task resource - The Batch task resource. If not specified,the current
batch/location is used. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `TASK` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TASK`**:
ID of the task or fully qualified identifier for the task.
To set the `task` attribute:

- provide the argument `TASK` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--job**:
The job ID for the task.
To set the `job` attribute:

- provide the argument `TASK` on the command line with a fully
specified name;
- provide the argument `--job` on the command line.

**--location**:
Google Cloud location for the task.
To set the `location` attribute:

- provide the argument `TASK` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `batch/location`.

**--task_group**:
The task_group ID for the task.
To set the `task_group` attribute:

- provide the argument `TASK` on the command line with a fully
specified name;
- provide the argument `--task_group` on the command line.**

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
gcloud alpha batch tasks describe
```

```
gcloud beta batch tasks describe
```