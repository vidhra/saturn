# gcloud firestore import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/import](https://cloud.google.com/sdk/gcloud/reference/firestore/import)*

**NAME**

: **gcloud firestore import - import Cloud Firestore documents from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud firestore import` `[INPUT_URI_PREFIX](https://cloud.google.com/sdk/gcloud/reference/firestore/import#INPUT_URI_PREFIX)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/import#--async)`] [`[--collection-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/import#--collection-ids)`=[`COLLECTION_IDS`,…]] [`[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/import#--database)`=`DATABASE`; default="(default)"] [`[--namespace-ids](https://cloud.google.com/sdk/gcloud/reference/firestore/import#--namespace-ids)`=[`NAMESPACE_IDS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: import Cloud Firestore documents from Google Cloud Storage.

**EXAMPLES**

: To import all collection groups from `mybucket/my/path`, run:

```
gcloud firestore import gs://mybucket/my/path
```

To import a specific set of collections groups asynchronously, run:

```
gcloud firestore import gs://mybucket/my/path --collection-ids='specific collection group1','specific
 collection group2' --async
```

To import all collection groups from certain namespace, run:

```
gcloud firestore import gs://mybucket/my/path --namespace-ids='specific namespace id'
```

**POSITIONAL ARGUMENTS**

: **`INPUT_URI_PREFIX`**:
Location of the import files.
This location is the 'output_uri_prefix' field of a previous export, and can be
found via the 'gcloud firestore operations describe' command.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--collection-ids**:
List specifying which collections will be included in the operation. When
omitted, all collections are included.
For example, to operate on only the `customers` and
`orders` collections:

```
gcloud firestore import --collection-ids='customers','orders'
```

**--database**:
The database to operate on. The default value is `(default)`.
For example, to operate on database `foo`:

```
gcloud firestore import --database='foo'
```

**--namespace-ids**:
List specifying which namespaces will be included in the operation. When
omitted, all namespaces are included.
This is only supported for Datastore Mode databases.
For example, to operate on only the `customers` and
`orders` namespaces:

```
gcloud firestore import --namespaces-ids='customers','orders'
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
gcloud alpha firestore import
```

```
gcloud beta firestore import
```