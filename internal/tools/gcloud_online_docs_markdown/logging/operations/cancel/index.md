# gcloud logging operations cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel)*

**NAME**

: **gcloud logging operations cancel - cancel a long running operation**

**SYNOPSIS**

: **`gcloud logging operations cancel` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#OPERATION_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#--location)`=`LOCATION` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/operations/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel a long running operation with given OPERATION_ID in given LOCATION. This
operation can be a copy_log_entries operation which is scheduled before.

**EXAMPLES**

: To cancel an operation, run:

```
gcloud logging operations cancel OPERATION_ID --location=LOCATION
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_ID`**:
The Id of the operation.

**REQUIRED FLAGS**

: **--location**:
Location of the operation.

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
gcloud alpha logging operations cancel
```

```
gcloud beta logging operations cancel
```