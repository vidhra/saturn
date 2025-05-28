# gcloud run jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs](https://cloud.google.com/sdk/gcloud/reference/run/jobs)*

**NAME**

: **gcloud run jobs - view and manage your Cloud Run jobs**

**SYNOPSIS**

: **`gcloud run jobs` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/run/jobs#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/jobs#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your Cloud Run jobs.

**EXAMPLES**

: To list your existing jobs, run:

```
gcloud run jobs list
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[executions](https://cloud.google.com/sdk/gcloud/reference/run/jobs/executions)`**:
View and manage your Cloud Run jobs executions.

**`[logs](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs)`**:
Read logs for Cloud Run jobs.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/run/jobs/add-iam-policy-binding)`**:
Add IAM policy binding to a Cloud Run job.

**`[create](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create)`**:
Create a Cloud Run job.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/run/jobs/delete)`**:
Delete a job.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/run/jobs/deploy)`**:
Create or update a Cloud Run job.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/jobs/describe)`**:
Obtain details about jobs.

**`[execute](https://cloud.google.com/sdk/gcloud/reference/run/jobs/execute)`**:
Execute a job.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/run/jobs/get-iam-policy)`**:
Get the IAM policy for a Cloud Run job.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/jobs/list)`**:
List jobs.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/run/jobs/remove-iam-policy-binding)`**:
Remove IAM policy binding of a Cloud Run job.

**`[replace](https://cloud.google.com/sdk/gcloud/reference/run/jobs/replace)`**:
Create or replace a job from a YAML job specification.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy)`**:
Set the IAM policy for a job.

**`[update](https://cloud.google.com/sdk/gcloud/reference/run/jobs/update)`**:
Update a Cloud Run Job.

**NOTES**

: These variants are also available:

```
gcloud alpha run jobs
```

```
gcloud beta run jobs
```