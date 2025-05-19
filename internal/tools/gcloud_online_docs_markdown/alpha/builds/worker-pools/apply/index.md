# gcloud alpha builds worker-pools apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply)*

**NAME**

: **gcloud alpha builds worker-pools apply - create a private pool for use by Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds worker-pools apply` `[--file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply#--file)`=`FILE` [`[--generation](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply#--generation)`=`GENERATION`; default=2] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/worker-pools/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a private pool for use by Cloud Build.

**REQUIRED FLAGS**

: **--file**:
The YAML file to use as the worker pool configuration file.

**OPTIONAL FLAGS**

: **--generation**:
Generation of the worker pool.

**--region**:
Region for Cloud Build.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.