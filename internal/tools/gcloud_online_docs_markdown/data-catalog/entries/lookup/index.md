# gcloud data-catalog entries lookup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/lookup](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/lookup)*

**NAME**

: **gcloud data-catalog entries lookup - lookup a Data Catalog entry by its target name**

**SYNOPSIS**

: **`gcloud data-catalog entries lookup` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/lookup#RESOURCE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/lookup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)`
instead.
Lookup a Data Catalog entry by its target name.

**EXAMPLES**

: To lookup the entry for a Cloud Pub/Sub topic by its Google Cloud Platform
resource name, run:

```
gcloud data-catalog entries lookup //pubsub.googleapis.com/projects/project1/topics/topic1
```

To lookup the entry for a Cloud Pub/Sub topic by its SQL name, run:

```
gcloud data-catalog entries lookup 'pubsub.topic.`my-project1`.topic1'
```

To lookup the entry for a BigQuery table by its SQL name, run:

```
gcloud data-catalog entries lookup 'bigquery.table.`my-project1`.my_dataset.my_table'
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
The name of the target resource to lookup. This can be either the Google Cloud
Platform resource name or the SQL name of a Google Cloud Platform resource. SQL
names follow Standard SQL lexical structure: [https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical)

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

**API REFERENCE**

: This command uses the `datacatalog/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/data-catalog/docs/](https://cloud.google.com/data-catalog/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog entries lookup
```

```
gcloud beta data-catalog entries lookup
```