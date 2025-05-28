# gcloud logging links delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/links/delete](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete)*

**NAME**

: **gcloud logging links delete - delete a linked dataset**

**SYNOPSIS**

: **`gcloud logging links delete` `[LINK_ID](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#LINK_ID)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--location)`=`LOCATION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--async)`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/links/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a bucket's linked dataset.

**EXAMPLES**

: To delete a bucket's linked dataset, run:

```
gcloud logging links delete my-link --bucket=my-bucket --location=global
```

**POSITIONAL ARGUMENTS**

: **`LINK_ID`**:
ID of the linked dataset to delete.

**REQUIRED FLAGS**

: **--bucket**:
ID of bucket

**--location**:
Location of the bucket.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--billing-account**

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
gcloud alpha logging links delete
```

```
gcloud beta logging links delete
```