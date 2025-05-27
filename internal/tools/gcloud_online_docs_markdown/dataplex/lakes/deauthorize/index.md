# gcloud dataplex lakes deauthorize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize)*

**NAME**

: **gcloud dataplex lakes deauthorize - deauthorize a service agent from managing resources**

**SYNOPSIS**

: **`gcloud dataplex lakes deauthorize` (`[--project-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize#--project-resource)`=`PROJECT_RESOURCE`     | `[--storage-bucket-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize#--storage-bucket-resource)`=`STORAGE_BUCKET_RESOURCE`     | `[--bigquery-dataset-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize#--bigquery-dataset-resource)`=`BIGQUERY_DATASET_RESOURCE` `[--secondary-project](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize#--secondary-project)`=`SECONDARY_PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/deauthorize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The service agent for the primary project will have its IAM role revoked from a
secondary project, a Cloud Storage bucket, or a BigQuery dataset.

**EXAMPLES**

: To deauthorize the service agent in project `test-project` from
managing resources in the project `test-project2`, run:

```
gcloud dataplex lakes deauthorize --project=test-project --project-resource=test-project2
```

To deauthorize the service agent in project `test-project` from
managing the Cloud Storage bucket `dataplex-storage-bucket`, run:

```
gcloud dataplex lakes deauthorize --project=test-project --storage-bucket-resource=dataplex-storage-bucket
```

To deauthorize the service agent in project `test-project` from
managing the BigQuery dataset `test-dataset` in project
`test-project2`, run:

```
gcloud dataplex lakes deauthorize --project=test-project --bigquery-dataset-resource=test-dataset --secondary-project=test-project2
```

**REQUIRED FLAGS**

: **--project-resource**

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
gcloud alpha dataplex lakes deauthorize
```