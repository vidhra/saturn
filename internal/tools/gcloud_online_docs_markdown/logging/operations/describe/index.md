# gcloud logging operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe)*

**NAME**

: **gcloud logging operations describe - display the information about a long running operation**

**SYNOPSIS**

: **`gcloud logging operations describe` `[OPERATION_ID](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#OPERATION_ID)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#--location)`=`LOCATION` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display the information about a long running operation which was scheduled
before. For example, a copy_log_entries operation scheduled by command: "gcloud
alpha logging copy BUCKET_ID DESTINATION --location=LOCATION" OPERATION_ID and
LOCATION are required to locate such operation.

**EXAMPLES**

: To describe an operation, run:

```
gcloud logging operations describe OPERATION_ID --location=LOCATION
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
gcloud alpha logging operations describe
```

```
gcloud beta logging operations describe
```