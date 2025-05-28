# gcloud run jobs logs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs)*

**NAME**

: **gcloud run jobs logs - read logs for Cloud Run jobs**

**SYNOPSIS**

: **`gcloud run jobs logs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read logs for Cloud Run jobs.

**EXAMPLES**

: To tail logs executions for a job, run:

```
gcloud run jobs logs tail my-job
```

To read logs executions for a job, run:

```
gcloud run jobs logs read my-job
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[read](https://cloud.google.com/sdk/gcloud/reference/run/jobs/logs/read)`**:
Read logs for Cloud Run jobs.

**NOTES**

: These variants are also available:

```
gcloud alpha run jobs logs
```

```
gcloud beta run jobs logs
```