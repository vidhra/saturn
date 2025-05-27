# gcloud dataproc jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs)*

**NAME**

: **gcloud dataproc jobs - submit and manage Dataproc jobs**

**SYNOPSIS**

: **`gcloud dataproc jobs` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Submit and manage Dataproc jobs.

**EXAMPLES**

: To learn about the types of jobs that can be submitted, run:

```
gcloud dataproc jobs submit
```

To view the output of a job as it runs, run:

```
gcloud dataproc jobs wait job_id
```

To cancel an active job, run:

```
gcloud dataproc jobs kill job_id
```

To view the details of a job, run:

```
gcloud dataproc jobs describe job_id
```

To see the list of all jobs, run:

```
gcloud dataproc jobs list
```

To delete the record of an inactive job, run:

```
gcloud dataproc jobs delete job_id
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[submit](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit)`**:
Submit Dataproc jobs to execute on a cluster.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/delete)`**:
Delete the record of an inactive job.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/describe)`**:
View the details of a job.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/get-iam-policy)`**:
Get IAM policy for a job.

**`[kill](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/kill)`**:
Kill an active job.

**`[list](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list)`**:
List jobs in a project.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/set-iam-policy)`**:
Set IAM policy for a job.

**`[update](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/update)`**:
Update the labels for a job.

**`[wait](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/wait)`**:
View the output of a job as it runs or after it completes.

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc jobs
```

```
gcloud beta dataproc jobs
```