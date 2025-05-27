# gcloud datastore import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/import](https://cloud.google.com/sdk/gcloud/reference/datastore/import)*

**NAME**

: **gcloud datastore import - import Cloud Datastore entities from Google Cloud Storage**

**SYNOPSIS**

: **`gcloud datastore import` `[INPUT_URL](https://cloud.google.com/sdk/gcloud/reference/datastore/import#INPUT_URL)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/datastore/import#--async)`] [`[--kinds](https://cloud.google.com/sdk/gcloud/reference/datastore/import#--kinds)`=[`KIND`,…]] [`[--namespaces](https://cloud.google.com/sdk/gcloud/reference/datastore/import#--namespaces)`=[`NAMESPACE`,…]] [`[--operation-labels](https://cloud.google.com/sdk/gcloud/reference/datastore/import#--operation-labels)`=[`OPERATION_LABEL`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Imports entities into Google Cloud Datastore. Existing entities with the same
key are overwritten. The import occurs in the background and its progress can be
monitored and managed via the Operation resource that is created. If an Import
operation is cancelled, it is possible that a subset of the data has already
been imported to Cloud Datastore. This data will not be removed.

**EXAMPLES**

: To import all data exported to the output URL
`gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata`,
run:

```
gcloud datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata
```

To import all data exported to the output URL
`gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata`
without waiting for the operation to complete, run:

```
gcloud datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata --async
```

To import only the `exampleKind` from the data exported to the output
URL
`gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata`,
run:

```
gcloud datastore import gs://exampleBucket/exampleExport/exampleExport.overall_export_metadata --kinds='exampleKind'
```

**POSITIONAL ARGUMENTS**

: **`INPUT_URL`**:
Location of the import metadata. Must be a valid Google Cloud Storage object.
The file extension is 'overall_export_metadata'.
This location is the 'output_url' field of a previous export, and can be found
via the 'operations describe' command.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--kinds**:
A list specifying what kinds will be included in the operation. When omitted,
all Kinds are included. For example, to operate on only the 'Customer' and
'Order' Kinds:

```
gcloud datastore import --kinds='Customer','Order'
```

**--namespaces**:
A list specifying what namespaces will be included in the operation. When
omitted, all namespaces are included in the operation, including the default
namespace. To specify that `only` the default namespace should be
operated on, use the special symbol '(default)'. For example, to operate on
entities from both the 'customers' and default namespaces:

```
gcloud datastore import --namespaces='(default)','customers'
```

**--operation-labels**:
A string:string map of custom labels to associate with this operation. For
example:

```
gcloud datastore import --operation-labels=comment='customer orders','sales rep'=pending
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
gcloud alpha datastore import
```

```
gcloud beta datastore import
```