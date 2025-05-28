# gcloud firestore bulk-delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete)*

**NAME**

: **gcloud firestore bulk-delete - bulk delete Cloud Firestore documents**

**SYNOPSIS**

: **`gcloud firestore bulk-delete` [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete#--async)`] [`[--collection-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete#--collection-ids)`=[`COLLECTION_IDS`,…]] [`[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete#--database)`=`DATABASE`; default="(default)"] [`[--namespace-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete#--namespace-ids)`=[`NAMESPACE_IDS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/bulk-delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: bulk delete Cloud Firestore documents.

**EXAMPLES**

: To bulk delete a specific set of collections groups asynchronously, run:

```
gcloud firestore bulk-delete --collection-ids='specific collection group1','specific
 collection group2' --async
```

To bulk delete all collection groups from certain namespace, run:

```
gcloud firestore bulk-delete --namespace-ids='specific namespace id'
```

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--collection-ids**:
List specifying which collections will be included in the operation. When
omitted, all collections are included.
For example, to operate on only the `customers` and
`orders` collections:

```
gcloud firestore bulk-delete --collection-ids='customers','orders'
```

**--database**:
The database to operate on. The default value is `(default)`.
For example, to operate on database `foo`:

```
gcloud firestore bulk-delete --database='foo'
```

**--namespace-ids**:
List specifying which namespaces will be included in the operation. When
omitted, all namespaces are included.
This is only supported for Datastore Mode databases.
For example, to operate on only the `customers` and
`orders` namespaces:

```
gcloud firestore bulk-delete --namespaces-ids='customers','orders'
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
gcloud alpha firestore bulk-delete
```

```
gcloud beta firestore bulk-delete
```