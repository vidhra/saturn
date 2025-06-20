# gcloud storage buckets list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list)*

**NAME**

: **gcloud storage buckets list - lists Cloud Storage buckets**

**SYNOPSIS**

: **`gcloud storage buckets list` [`[URLS](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#URLS)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--additional-headers)`=`HEADER`=`VALUE`] [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--raw)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/buckets/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Cloud Storage buckets.

**EXAMPLES**

: List all Google Cloud Storage buckets in default project:

```
gcloud storage buckets list
```

List buckets beginning with ``b´´:

```
gcloud storage buckets list gs://b*
```

List buckets with JSON formatting, only returning the
``name`` key:

```
gcloud storage buckets list --format="json(name)"
```

**POSITIONAL ARGUMENTS**

: **[`URLS` …]**:
Specifies URL of buckets to List.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--raw**:
Shows metadata in the format returned by the API instead of standardizing it.

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

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--uri**:
Print a list of resource URIs instead of the default output, and change the
command output to a list of URIs. If this flag is used with
`--format`, the formatting is applied on this URI list. To display
URIs alongside other keys instead, use the `uri()` transform.

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
gcloud alpha storage buckets list
```