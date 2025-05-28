# gcloud sql instances reencrypt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt)*

**NAME**

: **gcloud sql instances reencrypt - reencrypts a Cloud SQL CMEK instance**

**SYNOPSIS**

: **`gcloud sql instances reencrypt` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Reencrypt a Cloud SQL CMEK instance with the primary key version.

**EXAMPLES**

: To reencrypt a Cloud SQL CMEK instance with the primary key version:

```
gcloud sql instances reencrypt instance-foo
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

**FLAGS**

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

: These variants are also available:

```
gcloud alpha sql instances reencrypt
```

```
gcloud beta sql instances reencrypt
```