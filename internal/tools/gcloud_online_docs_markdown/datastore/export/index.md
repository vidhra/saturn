# gcloud datastore export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/export](https://cloud.google.com/sdk/gcloud/reference/datastore/export)*

**NAME**

: **gcloud datastore export - export Cloud Datastore entities to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud datastore export` `[OUTPUT_URL_PREFIX](https://cloud.google.com/sdk/gcloud/reference/datastore/export#OUTPUT_URL_PREFIX)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/datastore/export#--async)`] [`[--kinds](https://cloud.google.com/sdk/gcloud/reference/datastore/export#--kinds)`=[`KIND`,…]] [`[--namespaces](https://cloud.google.com/sdk/gcloud/reference/datastore/export#--namespaces)`=[`NAMESPACE`,…]] [`[--operation-labels](https://cloud.google.com/sdk/gcloud/reference/datastore/export#--operation-labels)`=[`OPERATION_LABEL`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export a copy of all or a subset of entities from Google Cloud Datastore to
another storage system, such as Google Cloud Storage. Recent updates to entities
may not be reflected in the export. The export occurs in the background and its
progress can be monitored and managed via the operation commands. The output of
an export may only be used once the operation has completed. If an export
operation is cancelled before completion then it may leave partial data behind
in Google Cloud Storage.

**EXAMPLES**

: To export all kinds in the `exampleNs` namespace in the
`exampleProject` project to the `exampleBucket`, run:

```
gcloud datastore export gs://exampleBucket --namespaces='exampleNs' --project='exampleProject'
```

To export the `exampleKind` and `otherKind` kinds in the
`exampleNs` namespace in the `exampleProject` project to
the `exampleBucket`, run:

```
gcloud datastore export gs://exampleBucket --kinds='exampleKind','otherKind' --namespaces='exampleNs' --project='exampleProject'
```

To export all namespaces and kinds in the currently set project to the
`exampleBucket` without waiting for the operation to complete, run:

```
gcloud datastore export gs://exampleBucket --async
```

To export the `exampleKind` in all namespaces in the currently set
project to the `exampleBucket`, and output the result in JSON, run:

```
gcloud datastore export gs://exampleBucket --kinds='exampleKind' --format=json
```

**POSITIONAL ARGUMENTS**

: **`OUTPUT_URL_PREFIX`**:
Location for the export metadata and data files. Must be a valid Google Cloud
Storage bucket with an optional path prefix. For example:

```
gcloud datastore export gs://mybucket/my/path
```

Will place the export in the `mybucket` bucket in objects prefixed
with `my/path`.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--kinds**:
A list specifying what kinds will be included in the operation. When omitted,
all Kinds are included. For example, to operate on only the 'Customer' and
'Order' Kinds:

```
gcloud datastore export --kinds='Customer','Order'
```

**--namespaces**:
A list specifying what namespaces will be included in the operation. When
omitted, all namespaces are included in the operation, including the default
namespace. To specify that `only` the default namespace should be
operated on, use the special symbol '(default)'. For example, to operate on
entities from both the 'customers' and default namespaces:

```
gcloud datastore export --namespaces='(default)','customers'
```

**--operation-labels**:
A string:string map of custom labels to associate with this operation. For
example:

```
gcloud datastore export --operation-labels=comment='customer orders','sales rep'=pending
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
gcloud alpha datastore export
```

```
gcloud beta datastore export
```