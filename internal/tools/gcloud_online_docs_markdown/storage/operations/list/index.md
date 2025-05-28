# gcloud storage operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/operations/list](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list)*

**NAME**

: **gcloud storage operations list - list storage operations**

**SYNOPSIS**

: **`gcloud storage operations list` `[PARENT_RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#PARENT_RESOURCE_NAME)` [`[--server-filter](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#--server-filter)`=`SERVER_FILTER`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List storage operations.

**EXAMPLES**

: To list all storage operations that belong to the bucket "my-bucket", run:

```
gcloud storage operations list projects/_/buckets/my-bucket
```

To list operations in JSON format, run:

```
gcloud storage operations list projects/_/buckets/my-bucket --format=json
```

An alternative bucket format is available:

```
gcloud storage operations list gs://my-bucket
```

**POSITIONAL ARGUMENTS**

: **`PARENT_RESOURCE_NAME`**:
The operation parent resource in the format
"projects/`_`/buckets/BUCKET".

**FLAGS**

: **--server-filter**:
Server-side filter string used to determine what operations to return. Example:
'(done = true AND complete_time >= "2023-01-01T00:00:00Z") OR
requested_cancellation = true' Note that the entire filter string must be in
quotes and date strings within the filter must be in embedded quotes.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha storage operations list
```