# gcloud asset analyze-iam-policy-longrunning  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning)*

**NAME**

: **gcloud asset analyze-iam-policy-longrunning - analyzes IAM policies that match a request asynchronously and writes the results to Google Cloud Storage or BigQuery destination**

**SYNOPSIS**

: **`gcloud asset analyze-iam-policy-longrunning` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--project)`=`PROJECT_ID`) (`[--gcs-output-path](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--gcs-output-path)`=`GCS_OUTPUT_PATH`     | [`[--bigquery-dataset](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--bigquery-dataset)`=`BIGQUERY_DATASET` `[--bigquery-table-prefix](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--bigquery-table-prefix)`=`BIGQUERY_TABLE_PREFIX` : `[--bigquery-partition-key](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--bigquery-partition-key)`=`BIGQUERY_PARTITION_KEY` `[--bigquery-write-disposition](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--bigquery-write-disposition)`=`BIGQUERY_WRITE_DISPOSITION`]) [`[--access-time](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--access-time)`=`ACCESS_TIME`] [`[--full-resource-name](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--full-resource-name)`=`FULL_RESOURCE_NAME`] [`[--identity](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--identity)`=`IDENTITY`] [`[--analyze-service-account-impersonation](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--analyze-service-account-impersonation)` `[--expand-groups](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--expand-groups)` `[--expand-resources](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--expand-resources)` `[--expand-roles](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--expand-roles)` `[--output-group-edges](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--output-group-edges)` `[--output-resource-edges](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--output-resource-edges)`] [`[--permissions](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--permissions)`=[`PERMISSIONS`,…] `[--roles](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#--roles)`=[`ROLES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Analyzes IAM policies that match a request asynchronously and writes the results
to Google Cloud Storage or BigQuery destination.

**EXAMPLES**

: To find out which users have been granted the iam.serviceAccounts.actAs
permission on a service account, and write analysis results to Google Cloud
Storage, run:

```
gcloud asset analyze-iam-policy-longrunning --organization=YOUR_ORG_ID --full-resource-name=YOUR_SERVICE_ACCOUNT_FULL_RESOURCE_NAME --permissions='iam.serviceAccounts.actAs' --gcs-output-path='gs://YOUR_BUCKET_NAME/YOUR_OBJECT_NAME'
```

To find out which resources a user can access, and write analysis results to
Google Cloud Storage, run:

```
gcloud asset analyze-iam-policy-longrunning --organization=YOUR_ORG_ID --identity='user:u1@foo.com' --gcs-output-path='gs://YOUR_BUCKET_NAME/YOUR_OBJECT_NAME'
```

To find out which roles or permissions a user has been granted on a project, and
write analysis results to BigQuery, run:

```
gcloud asset analyze-iam-policy-longrunning --organization=YOUR_ORG_ID --full-resource-name=YOUR_PROJECT_FULL_RESOURCE_NAME --identity='user:u1@foo.com' --bigquery-dataset='projects/YOUR_PROJECT_ID/datasets/YOUR_DATASET_ID' --bigquery-table-prefix='YOUR_BIGQUERY_TABLE_PREFIX'
```

To find out which users have been granted the iam.serviceAccounts.actAs
permission on any applicable resources, and write analysis results to BigQuery,
run:

```
gcloud asset analyze-iam-policy-longrunning --organization=YOUR_ORG_ID --permissions='iam.serviceAccounts.actAs' --bigquery-dataset='projects/YOUR_PROJECT_ID/datasets/YOUR_DATASET_ID' --bigquery-table-prefix='YOUR_BIGQUERY_TABLE_PREFIX'
```

**REQUIRED FLAGS**

: **--folder**

**--gcs-output-path**

**OPTIONAL FLAGS**

: **--access-time**

**--full-resource-name**

**--identity**

**--analyze-service-account-impersonation**

**--permissions**

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
gcloud alpha asset analyze-iam-policy-longrunning
```

```
gcloud beta asset analyze-iam-policy-longrunning
```