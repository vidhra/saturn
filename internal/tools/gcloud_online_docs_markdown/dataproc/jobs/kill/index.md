# gcloud dataproc jobs kill  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill)*

**NAME**

: **gcloud dataproc jobs kill - kill an active job**

**SYNOPSIS**

: **`gcloud dataproc jobs kill` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill#JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Kill an active job.

**EXAMPLES**

: To cancel a job, run:

```
gcloud dataproc jobs kill job_id
```

**POSITIONAL ARGUMENTS**

: **Job resource - The ID of the job to kill. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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

**--region**:
Dataproc region for the job. Each Dataproc region constitutes an independent
resource namespace constrained to deploying instances into Compute Engine zones
inside the region. Overrides the default `dataproc/region` property
value for this command invocation.
To set the `region` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**FLAGS**

: **--async**:
Return immediately without waiting for the operation in progress to complete.

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
gcloud alpha dataproc jobs kill
```

```
gcloud beta dataproc jobs kill
```