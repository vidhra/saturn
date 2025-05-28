# gcloud firestore export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/export](https://cloud.google.com/sdk/gcloud/reference/firestore/export)*

**NAME**

: **gcloud firestore export - export Cloud Firestore documents to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud firestore export` `[OUTPUT_URI_PREFIX](https://cloud.google.com/sdk/gcloud/reference/firestore/export#OUTPUT_URI_PREFIX)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/export#--async)`] [`[--collection-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/export#--collection-ids)`=[`COLLECTION_IDS`,…]] [`[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/export#--database)`=`DATABASE`; default="(default)"] [`[--namespace-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/export#--namespace-ids)`=[`NAMESPACE_IDS`,…]] [`[--snapshot-time](https://cloud.google.com/sdk/gcloud/reference/firestore/export#--snapshot-time)`=`SNAPSHOT_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: export Cloud Firestore documents to Google Cloud Storage.

**EXAMPLES**

: To export all collection groups to `mybucket` in objects prefixed
with `my/path`, run:

```
gcloud firestore export gs://mybucket/my/path
```

To export a specific set of collections groups asynchronously, run:

```
gcloud firestore export gs://mybucket/my/path --collection-ids='specific collection group1','specific
 collection group2' --async
```

To export all collection groups from certain namespace, run:

```
gcloud firestore export gs://mybucket/my/path --namespace-ids='specific namespace id'
```

To export from a snapshot at '2023-05-26T10:20:00.00Z', run:

```
gcloud firestore export gs://mybucket/my/path --snapshot-time='2023-05-26T10:20:00.00Z'
```

**POSITIONAL ARGUMENTS**

: **`OUTPUT_URI_PREFIX`**:
Location where the export files will be stored. Must be a valid Google Cloud
Storage bucket with an optional path prefix.
For example:

```
gcloud firestore export gs://mybucket/my/path
```

Will place the export in the `mybucket` bucket in objects prefixed
with `my/path`.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--collection-ids**:
List specifying which collections will be included in the operation. When
omitted, all collections are included.
For example, to operate on only the `customers` and
`orders` collections:

```
gcloud firestore export --collection-ids='customers','orders'
```

**--database**:
The database to operate on. The default value is `(default)`.
For example, to operate on database `foo`:

```
gcloud firestore export --database='foo'
```

**--namespace-ids**:
List specifying which namespaces will be included in the operation. When
omitted, all namespaces are included.
This is only supported for Datastore Mode databases.
For example, to operate on only the `customers` and
`orders` namespaces:

```
gcloud firestore export --namespaces-ids='customers','orders'
```

**--snapshot-time**:
The version of the database to export.
The timestamp must be in the past, rounded to the minute and not older than
`earliestVersionTime`. If specified, then the exported documents will
represent a consistent view of the database at the provided time. Otherwise,
there are no guarantees about the consistency of the exported documents.
For example, to operate on snapshot time `2023-05-26T10:20:00.00Z`:

```
gcloud firestore export --snapshot-time='2023-05-26T10:20:00.00Z'
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
gcloud alpha firestore export
```

```
gcloud beta firestore export
```