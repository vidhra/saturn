# gcloud alloydb clusters import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import)*

**NAME**

: **gcloud alloydb clusters import - import data into an AlloyDB cluster from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud alloydb clusters import` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#CLUSTER)` `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--gcs-uri)`=`GCS_URI` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--region)`=`REGION` (`[--sql](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--sql)`     | [`[--csv](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--csv)` `[--table](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--table)`=`TABLE` : `[--columns](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--columns)`=`COLUMNS` `[--escape-character](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--escape-character)`=`ESCAPE_CHARACTER` `[--field-delimiter](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--field-delimiter)`=`FIELD_DELIMITER` `[--quote-character](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--quote-character)`=`QUOTE_CHARACTER`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--database)`=`DATABASE`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#--user)`=`USER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import data into an AlloyDB cluster from Google Cloud Storage.

**EXAMPLES**

: To import data into a cluster, run:

```
gcloud alloydb clusters import my-cluster --region=us-central1 --database=my-database --gcs-uri=gs://my-bucket/source-file-path --sql --user=my-user"
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--gcs-uri**

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**--sql**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--database**:
Database name.

**--user**:
Database user for the import.

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
gcloud alpha alloydb clusters import
```

```
gcloud beta alloydb clusters import
```