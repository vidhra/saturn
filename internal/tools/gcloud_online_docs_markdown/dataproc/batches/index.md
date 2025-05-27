# gcloud dataproc batches  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/batches](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches)*

**NAME**

: **gcloud dataproc batches - submit Dataproc batch jobs**

**SYNOPSIS**

: **`gcloud dataproc batches` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit Dataproc batch jobs.
Submit a job:

```
gcloud dataproc batches submit
```

List all batch jobs:

```
gcloud dataproc batches list
```

List job details:

```
gcloud dataproc batches describe JOB_ID
```

Delete a batch job:

```
gcloud dataproc batches delete JOB_ID
```

Cancel a running batch job without removing the batch resource:

```
gcloud dataproc batches cancel JOB_ID
```

View job output:

```
gcloud dataproc batches wait JOB_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[submit](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit)`**:
Submit a Dataproc batch job.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/cancel)`**:
Cancel a batch job without removing batch resources.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/delete)`**:
Delete a batch job.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/describe)`**:
Describe a batch job.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/list)`**:
List batch jobs in a project.

**`[wait](https://cloud.google.com/sdk/gcloud/reference/dataproc/batches/wait)`**:
View the output of a batch as it runs or after it completes.

**NOTES**

: This variant is also available:

```
gcloud beta dataproc batches
```