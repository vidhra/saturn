# gcloud storage insights inventory-reports create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create)*

**NAME**

: **gcloud storage insights inventory-reports create - create a new inventory report config**

**SYNOPSIS**

: **`gcloud storage insights inventory-reports create` `[SOURCE_BUCKET_URL](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#SOURCE_BUCKET_URL)` [`[--destination](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--destination)`=`DESTINATION_URL`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--display-name)`=`DISPLAY_NAME`] [`[--metadata-fields](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--metadata-fields)`=[`METADATA_FIELDS`,…]; default="project,bucket,name,location,size,timeCreated,timeDeleted,updated,storageClass,etag,retentionExpirationTime,crc32c,md5Hash,generation,metageneration,contentType,contentEncoding,timeStorageClassUpdated"] [`[--schedule-repeats](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--schedule-repeats)`=`FREQUENCY`; default="daily"] [`[--schedule-repeats-until](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--schedule-repeats-until)`=`END_DATE`] [`[--schedule-starts](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--schedule-starts)`=`START_DATE`] [`[--parquet](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--parquet)`     | `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--csv-delimiter)`=`DELIMITER` `[--[no-]csv-header](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--[no-]csv-header)` `[--csv-separator](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#--csv-separator)`=`SEPARATOR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an inventory report config that defines how often inventory reports are
generated, the metadata fields you want the reports to include, and a
bucket/prefix in which to store the reports, also known as the destination.

**EXAMPLES**

: To create an inventory report about "my-bucket" that will store report details
in "report-bucket" with the prefix "save-path/".

```
gcloud storage insights inventory-reports create gs://my-bucket --destination=gs://report-bucket/save-path/
```

**POSITIONAL ARGUMENTS**

: **`SOURCE_BUCKET_URL`**:
URL of the source bucket that will contain the inventory report configuration.

**FLAGS**

: **--destination**:
Sets the URL of the destination bucket and path where generated reports are
stored. Defaults to <SOURCE_BUCKET_URL>/inventory_reports/.

**--display-name**:
Sets the editable name of the report configuration.

**--metadata-fields**:
The metadata fields to be included in the inventory report. The fields:
"project, bucket, name" are REQUIRED. Defaults to all fields being included.
`METADATA_FIELDS` must be one of: `project`,
`bucket`, `name`, `location`,
`size`, `timeCreated`, `timeDeleted`,
`updated`, `storageClass`, `etag`,
`retentionExpirationTime`, `crc32c`, `md5Hash`,
`generation`, `metageneration`, `contentType`,
`contentEncoding`, `timeStorageClassUpdated`.

**--schedule-repeats**:
Sets how often the inventory report configuration will run. Defaults to DAILY.
`FREQUENCY` must be one of: `daily`,
`weekly`.

**--schedule-repeats-until**:
Sets date after which you want to stop generating inventory reports. For
example, 2022-03-30. Defaults to one year from --schedule-starts value.

**--schedule-starts**:
Sets the date you want to start generating inventory reports. For example,
2022-01-30. Should be tomorrow or later based on UTC timezone. Defaults to
tomorrow.

**--parquet**

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

: This variant is also available:

```
gcloud alpha storage insights inventory-reports create
```