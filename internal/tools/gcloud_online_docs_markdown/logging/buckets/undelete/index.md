# gcloud logging buckets undelete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete)*

**NAME**

: **gcloud logging buckets undelete - undelete a bucket**

**SYNOPSIS**

: **`gcloud logging buckets undelete` `[BUCKET_ID](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#BUCKET_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#--location)`=`LOCATION` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/undelete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To undelete bucket 'my-bucket' in location 'global', run:

```
gcloud logging buckets undelete my-bucket --location=global
```

**POSITIONAL ARGUMENTS**

: **`BUCKET_ID`**:
ID of the bucket to undelete.

**REQUIRED FLAGS**

: **--location**:
Location of the bucket.

**OPTIONAL FLAGS**

: **--billing-account**

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
gcloud alpha logging buckets undelete
```

```
gcloud beta logging buckets undelete
```