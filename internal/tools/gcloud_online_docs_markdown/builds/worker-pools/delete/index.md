# gcloud builds worker-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/delete](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/delete)*

**NAME**

: **gcloud builds worker-pools delete - delete a worker pool from Cloud Build**

**SYNOPSIS**

: **`gcloud builds worker-pools delete` `[WORKER_POOL](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/delete#WORKER_POOL)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/worker-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a worker pool from Cloud Build.

**EXAMPLES**

: To delete a worker pool named `wp1` in region
`us-central1`, run:

```
gcloud builds worker-pools delete wp1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`WORKER_POOL`**:
The ID of the worker pool to delete.

**FLAGS**

: **--region**:
The Cloud region where the worker pool is.

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
gcloud alpha builds worker-pools delete
```

```
gcloud beta builds worker-pools delete
```