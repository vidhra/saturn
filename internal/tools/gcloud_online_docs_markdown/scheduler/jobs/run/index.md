# gcloud scheduler jobs run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run)*

**NAME**

: **gcloud scheduler jobs run - trigger an on-demand execution of a job**

**SYNOPSIS**

: **`gcloud scheduler jobs run` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run#JOB)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scheduler/jobs/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Trigger an on-demand execution of a job.

**EXAMPLES**

: The following command runs a jobs:

```
gcloud scheduler jobs run my-job
```

**POSITIONAL ARGUMENTS**

: **Job resource - The job you want to run. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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
gcloud alpha scheduler jobs run
```

```
gcloud beta scheduler jobs run
```