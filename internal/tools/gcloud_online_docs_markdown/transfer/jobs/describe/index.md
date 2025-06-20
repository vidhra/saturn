# gcloud transfer jobs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/describe](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/describe)*

**NAME**

: **gcloud transfer jobs describe - get configuration and latest operation details about transfer job**

**SYNOPSIS**

: **`gcloud transfer jobs describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/describe#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get configuration and latest operation details about a specific transfer job.

**EXAMPLES**

: To describe a job, run:

```
gcloud transfer jobs describe JOB-NAME
```

If you're looking for recent error details, use the "latestOperationName"
returned by this command as input to the "operations describe" command:

```
gcloud transfer jobs describe JOB-NAME --format="json(latestOperationName)"
```

```
gcloud transfer operations describe OPERATION-NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the job you want to describe.

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
gcloud alpha transfer jobs describe
```