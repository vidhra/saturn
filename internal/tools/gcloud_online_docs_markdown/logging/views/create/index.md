# gcloud logging views create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/views/create](https://cloud.google.com/sdk/gcloud/reference/logging/views/create)*

**NAME**

: **gcloud logging views create - create a log view on a log bucket**

**SYNOPSIS**

: **`gcloud logging views create` `[VIEW_ID](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#VIEW_ID)` `[--bucket](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--bucket)`=`BUCKET` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--location)`=`LOCATION` [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--description)`=`DESCRIPTION`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--log-filter)`=`LOG_FILTER`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/views/create#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create a view that matches all Google Compute Engine logs in a bucket, run:

```
gcloud logging views create my-view --bucket=my-bucket --location=global --log-filter='resource.type="gce_instance"'
```

**POSITIONAL ARGUMENTS**

: **`VIEW_ID`**:
ID of the view to create.

**REQUIRED FLAGS**

: **--bucket**:
ID of the bucket that will hold the view

**--location**:
Location of the bucket that will hold the view.

**OPTIONAL FLAGS**

: **--description**:
A textual description for the view.

**--log-filter**:
A filter for the view.

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
gcloud alpha logging views create
```

```
gcloud beta logging views create
```