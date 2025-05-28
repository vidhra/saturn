# gcloud logging views update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/views/update](https://cloud.google.com/sdk/gcloud/reference/logging/views/update)*

**NAME**

: **gcloud logging views update - update a view**

**SYNOPSIS**

: **`gcloud logging views update` `[VIEW_ID](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#VIEW_ID)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--location)`=`LOCATION` [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--description)`=`DESCRIPTION`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--log-filter)`=`LOG_FILTER`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/views/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the properties of a view.

**EXAMPLES**

: To update a view in your project, run:

```
gcloud logging views update my-view --bucket=my-bucket --location=global --description=my-new-description
```

**POSITIONAL ARGUMENTS**

: **`VIEW_ID`**:
Id of the view to update.

**REQUIRED FLAGS**

: **--bucket**:
ID of the bucket that holds the view

**--location**:
Location of the bucket that contains the view.

**OPTIONAL FLAGS**

: **--description**:
New description for the view.

**--log-filter**:
New filter for the view.

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
gcloud alpha logging views update
```

```
gcloud beta logging views update
```