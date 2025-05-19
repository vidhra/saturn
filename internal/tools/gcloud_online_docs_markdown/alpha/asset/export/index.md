# gcloud alpha asset export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export)*

**NAME**

: **gcloud alpha asset export - export the cloud assets to Google Cloud Storage/BigQuery**

**SYNOPSIS**

: **`gcloud alpha asset export` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--project)`=`PROJECT_ID`) (`[--output-path](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--output-path)`=`OUTPUT_PATH`     | `[--output-path-prefix](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--output-path-prefix)`=`OUTPUT_PATH_PREFIX`     | [(`[--bigquery-table](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--bigquery-table)`=`BIGQUERY_TABLE` : `[--bigquery-dataset](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--bigquery-dataset)`=`BIGQUERY_DATASET`) : `[--output-bigquery-force](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--output-bigquery-force)` `[--partition-key](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--partition-key)`=`PARTITION_KEY` `[--per-asset-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--per-asset-type)`]) [`[--asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--asset-types)`=[`ASSET_TYPES`,…]] [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--content-type)`=`CONTENT_TYPE`] [`[--relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--relationship-types)`=[`RELATIONSHIP_TYPES`,…]] [`[--snapshot-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#--snapshot-time)`=`SNAPSHOT_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Export the cloud assets to Google Cloud Storage or
BigQuery. Use gcloud asset operations describe to get the latest status of the
operation. Note that to export a project different from the project you want to
bill, you can use --billing-project or authenticate with a service account. See
[https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/gcloud-asset](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/gcloud-asset)
for examples of using a service account.

**EXAMPLES**

: To export a snapshot of assets of type 'compute.googleapis.com/Disk' in project
'test-project' at '2019-03-05T00:00:00Z' to 'gs://bucket-name/object-name' and
only export the asset metadata, run:

```
gcloud alpha asset export --project='test-project' --asset-types='compute.googleapis.com/Disk' --snapshot-time='2019-03-05T00:00:00Z' --output-path='gs://bucket-name/object-name' --content-type='resource'
```

To export a snapshot of assets of type 'compute.googleapis.com/Disk' in project
'test-project' at '2019-03-05T00:00:00Z' to
'projects/projectId/datasets/datasetId/tables/table_name', overwrite the table
if existed, run:

```
gcloud alpha asset export --project='test-project' --asset-types='compute.googleapis.com/Disk' --snapshot-time='2019-03-05T00:00:00Z' --bigquery-table='projects/projectId/datasets/datasetId/tables/table_name' --output-bigquery-force --content-type='resource'
```

**REQUIRED FLAGS**

: **--folder**

**--output-path**

**OPTIONAL FLAGS**

: **--asset-types**:
A list of asset types (i.e., "compute.googleapis.com/Disk") to take a snapshot.
If specified and non-empty, only assets matching the specified types will be
returned. See [http://cloud.google.com/asset-inventory/docs/supported-asset-types](http://cloud.google.com/asset-inventory/docs/supported-asset-types)
for supported asset types.

**--content-type**:
Asset content type. If specified, only content matching the specified type will
be returned. Otherwise, no content but the asset name will be returned.
Specifying `resource` will export resource metadata, specifying
`iam-policy` will export the IAM policy for each child asset,
specifying `org-policy` will export the Org Policy set on child
assets, specifying `access-policy` will export the Access Policy set
on child assets, specifying `os-inventory` will export the OS
inventory of VM instances, and specifying `relationship` will export
relationships of the assets. `CONTENT_TYPE` must be one
of: `resource`, `iam-policy`, `org-policy`,
`access-policy`, `os-inventory`,
`relationship`.

**--relationship-types**:
A list of relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to take a
snapshot. This argument will only be honoured if content_type=RELATIONSHIP. If
specified and non-empty, only relationships matching the specified types will be
returned. See [http://cloud.google.com/asset-inventory/docs/supported-asset-types](http://cloud.google.com/asset-inventory/docs/supported-asset-types)
for supported relationship types.

**--snapshot-time**:
Timestamp to take a snapshot on assets. This can only be a current or past time.
If not specified, the current time will be used. Due to delays in resource data
collection and indexing, there is a volatile window during which running the
same query at different times may return different results. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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
gcloud asset export
```

```
gcloud beta asset export
```