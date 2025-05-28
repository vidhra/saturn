# gcloud logging copy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/copy](https://cloud.google.com/sdk/gcloud/reference/logging/copy)*

**NAME**

: **gcloud logging copy - copy log entries**

**SYNOPSIS**

: **`gcloud logging copy` `[BUCKET_ID](https://cloud.google.com/sdk/gcloud/reference/logging/copy#BUCKET_ID)` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/logging/copy#DESTINATION)` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--location)`=`LOCATION` [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--log-filter)`=`LOG_FILTER`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/copy#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/copy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud logging copy starts the process to copy log entries from a log bucket to
a destination.

**EXAMPLES**

: To start a copy log entries operation, run:

```
gcloud logging copy BUCKET_ID DESTINATION --location=LOCATION
```

To copy log entries in a specific time window, run:

```
gcloud logging copy BUCKET_ID DESTINATION --location=LOCATION --log-filter='timestamp<="2021-05-31T23:59:59Z" AND
 timestamp>="2021-05-31T00:00:00Z"'
```

**POSITIONAL ARGUMENTS**

: **`BUCKET_ID`**:
Id of the log bucket to copy logs from. Example: my-bucket

**`DESTINATION`**:
Destination to copy logs to. Example: Cloud Storage bucket:
storage.googleapis.com/my-cloud-storage-bucket

**REQUIRED FLAGS**

: **--location**:
Location of the log bucket.

**OPTIONAL FLAGS**

: **--log-filter**:
A filter specifying which log entries to copy. The filter must be no more than
20k characters. An empty filter matches all log entries.

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
gcloud alpha logging copy
```

```
gcloud beta logging copy
```