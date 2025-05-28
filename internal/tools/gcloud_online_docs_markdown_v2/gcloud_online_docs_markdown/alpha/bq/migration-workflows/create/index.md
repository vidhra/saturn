# gcloud alpha bq migration-workflows create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create)*

**NAME**

: **gcloud alpha bq migration-workflows create - create migration workflows**

**SYNOPSIS**

: **`gcloud alpha bq migration-workflows create` `[--config-file](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create#--config-file)`=`CONFIG_FILE` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create#--location)`=`LOCATION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bq/migration-workflows/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a migration workflow

**EXAMPLES**

: To create a migration workflow in EU synchronously based on a config file, run:

```
gcloud alpha bq migration-workflows create --location=EU --config-file=config_file.yaml --no-async
```

**REQUIRED FLAGS**

: **--config-file**:
Path to the migration workflows config file.

**--location**:
Location of the migration workflow.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
allowlist. These variants are also available:

```
gcloud bq migration-workflows create
```

```
gcloud beta bq migration-workflows create
```