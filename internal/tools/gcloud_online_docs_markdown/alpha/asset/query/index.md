# gcloud alpha asset query  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query)*

**NAME**

: **gcloud alpha asset query - query the Cloud assets**

**SYNOPSIS**

: **`gcloud alpha asset query` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--project)`=`PROJECT_ID`) (`[--job-reference](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--job-reference)`=`JOB_REFERENCE`     | `[--statement](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--statement)`=`STATEMENT`) [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--page-size)`=`PAGE_SIZE`] [`[--page-token](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--page-token)`=`PAGE_TOKEN`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--timeout)`=`TIMEOUT`] [`[--snapshot-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--snapshot-time)`=`SNAPSHOT_TIME`     | [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--start-time)`=`START_TIME` : `[--end-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--end-time)`=`END_TIME`]] [`[--write-disposition](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--write-disposition)`=`WRITE_DISPOSITION` [`[--bigquery-table](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--bigquery-table)`=`BIGQUERY_TABLE` : `[--bigquery-dataset](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#--bigquery-dataset)`=`BIGQUERY_DATASET`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Issue an analytical query on Cloud assets using a BigQuery
Standard SQL compatible statement.

**EXAMPLES**

: To count the number of compute instances, run:

```
gcloud alpha asset query --project='test-project' --statement='SELECT * FROM compute_googleapis_com_Instance'
```

To see the query result of the previous job, pass the job-reference from the
previous response:

```
gcloud alpha asset query --project='test-project' --job-reference=<job-reference-from>
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset query
```

```
gcloud beta asset query
```