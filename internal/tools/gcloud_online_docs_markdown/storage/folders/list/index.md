# gcloud storage folders list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/folders/list](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list)*

**NAME**

: **gcloud storage folders list - list folders**

**SYNOPSIS**

: **`gcloud storage folders list` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--additional-headers)`=`HEADER`=`VALUE`] [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--raw)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/folders/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List folders.

**EXAMPLES**

: The following command lists all folders in a hierarchical namespace bucket:

```
gcloud storage folders list gs://my-bucket/
```

The following command lists all folders under a parent folder:

```
gcloud storage folders list gs://my-bucket/parent-folder/
```

You can use [wildcards](https://cloud.google.com/storage/docs/wildcards) to match
multiple paths (including multiple buckets). Bucket wildcards are expanded to
match only buckets contained in your current project. The following command
matches folders that are stored in buckets in your project that begin with
``my-b``:

```
gcloud storage folders list gs://my-b*/
```

Following is another example where we are listing all folders that begin with
``B´´ under a given bucket:

```
gcloud storage folders list gs://my-bucket/B*
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The URLs of the resources to list.

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
gcloud alpha storage folders list
```