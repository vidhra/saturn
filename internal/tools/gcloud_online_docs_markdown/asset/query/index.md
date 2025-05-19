# gcloud asset query  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/query](https://cloud.google.com/sdk/gcloud/reference/asset/query)*

**NAME**

: **gcloud asset query - query the Cloud assets**

**SYNOPSIS**

: **`gcloud asset query` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/query#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/query#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/query#--project)`=`PROJECT_ID`) (`[--job-reference](https://cloud.google.com/sdk/gcloud/reference/asset/query#--job-reference)`=`JOB_REFERENCE`     | `[--statement](https://cloud.google.com/sdk/gcloud/reference/asset/query#--statement)`=`STATEMENT`) [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/asset/query#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/asset/query#--page-token)`=`PAGE_TOKEN`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/asset/query#--timeout)`=`TIMEOUT`] [`[--snapshot-time](https://cloud.google.com/sdk/gcloud/reference/asset/query#--snapshot-time)`=`SNAPSHOT_TIME`     | [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/asset/query#--start-time)`=`START_TIME` : `[--end-time](https://cloud.google.com/sdk/gcloud/reference/asset/query#--end-time)`=`END_TIME`]] [`[--write-disposition](https://cloud.google.com/sdk/gcloud/reference/asset/query#--write-disposition)`=`WRITE_DISPOSITION` [`[--bigquery-table](https://cloud.google.com/sdk/gcloud/reference/asset/query#--bigquery-table)`=`BIGQUERY_TABLE` : `[--bigquery-dataset](https://cloud.google.com/sdk/gcloud/reference/asset/query#--bigquery-dataset)`=`BIGQUERY_DATASET`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/query#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Issue an analytical query on Cloud assets using a BigQuery Standard SQL
compatible statement.

**EXAMPLES**

: To count the number of compute instances, run:

```
gcloud asset query --project='test-project' --statement='SELECT * FROM compute_googleapis_com_Instance'
```

To see the query result of the previous job, pass the job-reference from the
previous response:

```
gcloud asset query --project='test-project' --job-reference=<job-reference-from>
```

**REQUIRED FLAGS**

: **--folder**

**--job-reference**

**OPTIONAL FLAGS**

: **--page-size**:
The maximum number of rows to return in the results. One page is also limited to
10 MB.

**--page-token**:
A page token received from previous call.

**--timeout**:
Maximum amount of time that the client will wait for the query to complete.

**--snapshot-time**

**--write-disposition**

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
gcloud alpha asset query
```

```
gcloud beta asset query
```