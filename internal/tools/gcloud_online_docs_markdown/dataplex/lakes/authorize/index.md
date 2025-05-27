# gcloud dataplex lakes authorize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize)*

**NAME**

: **gcloud dataplex lakes authorize - authorize a service agent to manage resources**

**SYNOPSIS**

: **`gcloud dataplex lakes authorize` (`[--project-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize#--project-resource)`=`PROJECT_RESOURCE`     | `[--storage-bucket-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize#--storage-bucket-resource)`=`STORAGE_BUCKET_RESOURCE`     | `[--bigquery-dataset-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize#--bigquery-dataset-resource)`=`BIGQUERY_DATASET_RESOURCE` `[--secondary-project](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize#--secondary-project)`=`SECONDARY_PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/lakes/authorize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The service agent for the primary project will be granted an IAM role on a
secondary project, a Cloud Storage bucket, or a BigQuery dataset.

**EXAMPLES**

: To authorize the service agent in project `test-project` to manage
resources in the project `test-project2`, run:

```
gcloud dataplex lakes authorize --project=test-project --project-resource=test-project2
```

To authorize the service agent in project `test-project` to manage
the Cloud Storage bucket `dataplex-storage-bucket`, run:

```
gcloud dataplex lakes authorize --project=test-project --storage-bucket-resource=dataplex-storage-bucket
```

To authorize the service agent in project `test-project` to manage
the BigQuery dataset `test-dataset` in project
`test-project2`, run:

```
gcloud dataplex lakes authorize --project=test-project --bigquery-dataset-resource=test-dataset --secondary-project=test-project2
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
gcloud alpha dataplex lakes authorize
```