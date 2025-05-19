# gcloud alpha batch jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs)*

**NAME**

: **gcloud alpha batch jobs - manage Batch job resources**

**SYNOPSIS**

: **`gcloud alpha batch jobs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud batch jobs command group lets you submit,
describe, list and delete Batch jobs.
With Batch, you can utilize the fully managed service to schedule, queue, and
execute batch jobs on Google's infrastructure.
For more information about Batch, see the [Batch overview](https://cloud.google.com/batch) and the [Batch documentation](https://cloud.google.com/batch/docs/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/cancel)`**:
`(ALPHA)` Cancel a job.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/delete)`**:
`(ALPHA)` Delete a job.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/describe)`**:
`(ALPHA)` Show details of a job.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/list)`**:
`(ALPHA)` List jobs for a specified Batch project/location.

**`[submit](https://cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/submit)`**:
`(ALPHA)` Submit a Batch job.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud batch jobs
```

```
gcloud beta batch jobs
```