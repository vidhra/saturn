# gcloud datastore operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list)*

**NAME**

: **gcloud datastore operations list - list pending Cloud Datastore admin operations and their status**

**SYNOPSIS**

: **`gcloud datastore operations list` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#--limit)`=`LIMIT`; default=100] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastore/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Filters are case-sensitive and have the following syntax:

```
field = value [AND [field = value]] …
```

where `field` is one of `kind`, `namespace`,
`type`, or `labels.[KEY]`, and `[KEY]` is a
label key. `kind` and `namespace` may be `*` to
query for operations on all kinds and/or all namespaces. `type` may
be one of `export_entities` or `import_entities`.
Only the logical `AND` operator is supported; space-separated items
are treated as having an implicit `AND` operator.

**EXAMPLES**

: To see the list of all operations, run:

```
gcloud datastore operations list
```

To see the list of all export operations, run:

```
gcloud datastore operations list --filter='type:export_entities'
```

To see the list of all export operations for kind 'MyKind', run:

```
gcloud datastore operations list --filter='type:export_entities AND kind:MyKind'
```

To see the list of all operations with particular labels, run:

```
gcloud datastore operations list --filter='labels.run = daily'
```

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `100`. This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `100`. Paging
may be applied before or after `--filter` and `--limit`
depending on the service.

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

: These variants are also available:

```
gcloud alpha datastore operations list
```

```
gcloud beta datastore operations list
```