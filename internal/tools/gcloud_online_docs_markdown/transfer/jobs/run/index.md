# gcloud transfer jobs run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/run](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/run)*

**NAME**

: **gcloud transfer jobs run - run a Transfer Service transfer job**

**SYNOPSIS**

: **`gcloud transfer jobs run` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/run#NAME)` [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/run#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Run a Transfer Service transfer job.

**EXAMPLES**

: To run job 'foo', run:

```
gcloud transfer jobs run foo
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the job you want to run.

**FLAGS**

: **--no-async**:
Blocks other tasks in your terminal until the transfer operation has completed.
If not included, tasks will run asynchronously.

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
gcloud alpha transfer jobs run
```