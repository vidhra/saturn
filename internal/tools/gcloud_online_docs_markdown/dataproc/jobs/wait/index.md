# gcloud dataproc jobs wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait)*

**NAME**

: **gcloud dataproc jobs wait - view the output of a job as it runs or after it completes**

**SYNOPSIS**

: **`gcloud dataproc jobs wait` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait#JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: View the output of a job as it runs or after it completes.

**EXAMPLES**

: To see a list of all jobs, run:

```
gcloud dataproc jobs list
```

To display these jobs with their respective IDs and underlying REST calls, run:

```
gcloud dataproc jobs list --format "table(reference.jobId)" --limit 1 --log-http
```

To view the output of a job as it runs, run:

```
gcloud dataproc jobs wait job_id
```

**POSITIONAL ARGUMENTS**

: **Job resource - The ID of the job to wait for. The arguments in this group can be
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
gcloud alpha dataproc jobs wait
```

```
gcloud beta dataproc jobs wait
```