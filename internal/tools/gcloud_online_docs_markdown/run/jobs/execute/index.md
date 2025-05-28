# gcloud run jobs execute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute)*

**NAME**

: **gcloud run jobs execute - execute a job**

**SYNOPSIS**

: **`gcloud run jobs execute` [`[JOB](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#JOB)`] [`[--container](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--container)`=`CONTAINER`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--region)`=`REGION`] [`[--task-timeout](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--task-timeout)`=`TASK_TIMEOUT`] [`[--tasks](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--tasks)`=`TASKS`] [`[--args](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--args)`=[`ARG`,…] `[--update-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--update-env-vars)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--async)`     | `[--wait](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#--wait)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Execute a job.

**EXAMPLES**

: To execute a job:

```
gcloud run jobs execute my-job
```

**POSITIONAL ARGUMENTS**

: **Job resource - Job to execute. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- specify the job name from an interactive prompt with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`JOB`]**:
ID of the Job or fully qualified identifier for the Job.
To set the `jobs` attribute:

- provide the argument `JOB` on the command line;
- specify the job name from an interactive prompt.**

**FLAGS**

: **--container**:
Specifies a container by name. Flags following --container will apply to the
specified container.
Flags that are not container-specific must be specified before --container.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**--task-timeout**:
The existing maximum time (deadline) a job task attempt can run for. If
provided, an execution will be created with this value. Otherwise existing
maximum time of the job is used. In the case of retries, this deadline applies
to each attempt of a task. If the task attempt does not complete within this
time, it will be killed. It is specified as a duration; for example, "10m5s" is
ten minutes, and five seconds. If you don't specify a unit, seconds is assumed.
For example, "10" is 10 seconds.

**--tasks**:
Number of tasks that must run to completion for the execution to be considered
done. If provided, an execution will be created with this value. Otherwise the
existing task count of the job is used.

Container Flags

```
If the --container is specified the following arguments may only be specified after a --container flag.
```

**--args**:
Comma-separated arguments passed to the command run by the container image. If
provided, an execution will be created with the input values. Otherwise, the
existing arguments of the job are used.

**--update-env-vars**:
List of key-value pairs to set as environment variables overrides for an
execution of a job. If provided, an execution will be created with the merge
result of the input values and the existing environment variables. New value
overrides existing value if they have the same key. If not provided, existing
environment variables are used.

**--async**

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
gcloud alpha run jobs execute
```

```
gcloud beta run jobs execute
```