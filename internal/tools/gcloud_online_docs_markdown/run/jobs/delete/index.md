# gcloud run jobs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete)*

**NAME**

: **gcloud run jobs delete - delete a job**

**SYNOPSIS**

: **`gcloud run jobs delete` `[JOB](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete#JOB)` [`[--[no-]async](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete#--[no-]async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a job.

**EXAMPLES**

: To delete a job:

```
gcloud run jobs delete job-name
```

**POSITIONAL ARGUMENTS**

: **Job resource - Job to delete. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`JOB`**:
ID of the Job or fully qualified identifier for the Job.
To set the `jobs` attribute:

- provide the argument `JOB` on the command line.**

**FLAGS**

: **--[no-]async**:
Return immediately, without waiting for the operation in progress to complete.
Defaults to --no-async. Use `--async` to enable and
`--no-async` to disable.

**--region**:
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
gcloud alpha run jobs delete
```

```
gcloud beta run jobs delete
```