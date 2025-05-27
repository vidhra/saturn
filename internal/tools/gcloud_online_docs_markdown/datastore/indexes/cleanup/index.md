# gcloud datastore indexes cleanup  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup)*

**NAME**

: **gcloud datastore indexes cleanup - remove unused datastore indexes based on your local index configuration**

**SYNOPSIS**

: **`gcloud datastore indexes cleanup` `[INDEX_FILE](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup#INDEX_FILE)` [`[--database](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup#--database)`=`DATABASE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/indexes/cleanup#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command removes unused datastore indexes based on your local index
configuration. Any indexes that exist that are not in the index file will be
removed.

**EXAMPLES**

: To remove unused indexes based on your local configuration, run:

```
gcloud datastore indexes cleanup ~/myapp/index.yaml
```

**POSITIONAL ARGUMENTS**

: **`INDEX_FILE`**:
The path to your `index.yaml` file. For a detailed look into defining
your `index.yaml` file, refer to this configuration guide: [https://cloud.google.com/datastore/docs/tools/indexconfig#Datastore_About_index_yaml](https://cloud.google.com/datastore/docs/tools/indexconfig#Datastore_About_index_yaml)

**FLAGS**

: **--database**:
The database to operate on. If not specified, the CLI refers the
`(default)` database by default.
For example, to operate on database `testdb`:

```
gcloud datastore indexes cleanup --database='testdb'
```

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
gcloud alpha datastore indexes cleanup
```

```
gcloud beta datastore indexes cleanup
```