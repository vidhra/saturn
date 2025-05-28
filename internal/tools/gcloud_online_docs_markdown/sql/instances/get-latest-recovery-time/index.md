# gcloud sql instances get-latest-recovery-time  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time)*

**NAME**

: **gcloud sql instances get-latest-recovery-time - displays the latest recovery time to which a Cloud SQL instance can be restored to**

**SYNOPSIS**

: **`gcloud sql instances get-latest-recovery-time` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time#INSTANCE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud sql instances get-latest-recovery-time` retrieves the latest
recovery time for a Cloud SQL instance. This is the latest time that can be used
to perform point in time recovery for the Cloud SQL instance.

**EXAMPLES**

: To retrieve the latest recovery time for an instance:

```
gcloud sql instances get-latest-recovery-time instance-foo
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud SQL instance ID.

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
gcloud alpha sql instances get-latest-recovery-time
```

```
gcloud beta sql instances get-latest-recovery-time
```