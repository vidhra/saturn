# gcloud logging buckets delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete)*

**NAME**

: **gcloud logging buckets delete - delete a bucket**

**SYNOPSIS**

: **`gcloud logging buckets delete` `[BUCKET_ID](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#BUCKET_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#--location)`=`LOCATION` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/buckets/delete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete bucket 'my-bucket' in location 'global', run:

```
gcloud logging buckets delete my-bucket --location=global
```

**POSITIONAL ARGUMENTS**

: **`BUCKET_ID`**:
ID of the bucket to delete.

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
gcloud alpha logging buckets delete
```

```
gcloud beta logging buckets delete
```