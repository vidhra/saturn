# gcloud alpha alloydb clusters export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export)*

**NAME**

: **gcloud alpha alloydb clusters export - export data from an AlloyDB cluster to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud alpha alloydb clusters export` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#CLUSTER)` `[--database](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--database)`=`DATABASE` `[--gcs-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--gcs-uri)`=`GCS_URI` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--region)`=`REGION` ([`[--csv](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--csv)` `[--select-query](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--select-query)`=`SELECT_QUERY` : `[--escape-character](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--escape-character)`=`ESCAPE_CHARACTER` `[--field-delimiter](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--field-delimiter)`=`FIELD_DELIMITER` `[--quote-character](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--quote-character)`=`QUOTE_CHARACTER`]     | [`[--sql](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--sql)` : `[--schema-only](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--schema-only)` `[--tables](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--tables)`=`TABLES` [`[--clean-target-objects](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--clean-target-objects)` : `[--if-exist-target-objects](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--if-exist-target-objects)`]]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Export data from an AlloyDB cluster to Google Cloud
Storage.

**EXAMPLES**

: To export a cluster, run:

```
gcloud alpha alloydb clusters export my-cluster --region=us-central1 --database=my-database --gcs-uri=gs://my-bucket/my-export-file-path --csv --select-query="SELECT * FROM my-table"
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
AlloyDB cluster ID

**REQUIRED FLAGS**

: **--database**:
Database name.

**--gcs-uri**

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**--csv**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb clusters export
```

```
gcloud beta alloydb clusters export
```