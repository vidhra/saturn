# gcloud storage batch-operations jobs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/delete](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/delete)*

**NAME**

: **gcloud storage batch-operations jobs delete - delete a batch-operations job**

**SYNOPSIS**

: **`gcloud storage batch-operations jobs delete` `[BATCH_JOB](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/delete#BATCH_JOB)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations/jobs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete the batch operation job.

**EXAMPLES**

: To delete a batch job with the name `my-job` in location
`us-central1`:

```
gcloud storage batch-operations jobs delete my-job --location=us-central1
```

To delete the same batch job with fully specified name:

```
gcloud storage batch-operations jobs delete projects/my-project/locations/us-central1/jobs/my-job
```

**POSITIONAL ARGUMENTS**

: **Batch job resource - The batch job to delete. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `batch_job` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `batch_job` on the command line with a fully
specified name;
- The default is `global`.

This must be specified.

**`BATCH_JOB`**:
ID of the batch-job or fully qualified identifier for the batch-job.
To set the `batch-job` attribute:

- provide the argument `batch_job` on the command line.**

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

: This variant is also available:

```
gcloud alpha storage batch-operations jobs delete
```