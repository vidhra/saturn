# gcloud batch jobs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/batch/jobs/delete](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/delete)*

**NAME**

: **gcloud batch jobs delete - delete a job**

**SYNOPSIS**

: **`gcloud batch jobs delete` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/delete#JOB)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The job specified does not exist.
- The active account does not have permission to delete the given job.

**EXAMPLES**

: To delete the job with name
`projects/foo/locations/us-central1/jobs/bar`, run:

```
gcloud batch jobs delete projects/foo/locations/us-central1/jobs/bar
```

**POSITIONAL ARGUMENTS**

: **Job resource - The Batch job resource. If --location not specified,the current
batch/location is used. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`JOB`**:
ID of the job or fully qualified identifier for the job.
To set the `job` attribute:

- provide the argument `JOB` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the job.
To set the `location` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- set the property `batch/location`.**

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
gcloud alpha batch jobs delete
```

```
gcloud beta batch jobs delete
```