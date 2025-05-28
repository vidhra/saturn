# gcloud transfer jobs monitor  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/monitor](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/monitor)*

**NAME**

: **gcloud transfer jobs monitor - track progress in real time for a transfer job's latest operation**

**SYNOPSIS**

: **`gcloud transfer jobs monitor` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/monitor#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/monitor#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Track progress in real time for a transfer job's latest operation.

**EXAMPLES**

: To monitor a job, run:

```
gcloud transfer jobs monitor JOB-NAME
```

If you're looking for recent error details, use the "Operation name" returned by
this command as input to the "operations describe" command:

```
gcloud transfer jobs monitor JOB-NAME
```

```
gcloud transfer operations describe OPERATION-NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the job you want to monitor (you'll see details for the job's latest
operation).

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
gcloud alpha transfer jobs monitor
```