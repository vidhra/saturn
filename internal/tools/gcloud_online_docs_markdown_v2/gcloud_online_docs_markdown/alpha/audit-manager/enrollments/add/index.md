# gcloud alpha audit-manager enrollments add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add)*

**NAME**

: **gcloud alpha audit-manager enrollments add - enroll a new scope**

**SYNOPSIS**

: **`gcloud alpha audit-manager enrollments add` `[--eligible-gcs-buckets](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#--eligible-gcs-buckets)`=`BUCKET` `[URI](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#URI)`,[`[BUCKET](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#BUCKET)` `[URI](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#URI)`,…] (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#--project)`=`PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager/enrollments/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Enroll a new scope.

**EXAMPLES**

: To enroll a project with ID `123` with
`gs://test-bucket-1` and `gs://my-bucket-2` as eligible
storage buckets, run:

```
gcloud alpha audit-manager enrollments add --project=123 --eligible-gcs-buckets="gs://test-bucket-1,gs://my-bucket-2"
```

**REQUIRED FLAGS**

: **--eligible-gcs-buckets**:
Eligible cloud storage buckets where report and evidence can be uploaded.

**--folder**

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
allowlist. This variant is also available:

```
gcloud audit-manager enrollments add
```