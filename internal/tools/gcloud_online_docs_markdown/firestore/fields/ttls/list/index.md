# gcloud firestore fields ttls list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list)*

**NAME**

: **gcloud firestore fields ttls list - list all fields used as a Time To Live expiration setting**

**SYNOPSIS**

: **`gcloud firestore fields ttls list` [`[--collection-group](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--collection-group)`=`COLLECTION_GROUP` `[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--database)`=`DATABASE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/fields/ttls/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List fields that give an expiration timestamp for documents in a collection
group or kind.

**EXAMPLES**

: The following command lists all TTL fields for the whole database:

```
gcloud firestore fields ttls list
```

**FLAGS**

: **Collection group resource - Collection group of the ttl.
This can be omitted to include fields across all collection groups (kinds). The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--collection-group` on the command line with a
fully specified name;
- provide the argument [--collection-group] on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--collection-group**:
ID of the collection group or fully qualified identifier for the collection
group.
To set the `collection-group` attribute:

- provide the argument `--collection-group` on the command line;
- provide the argument [--collection-group] on the command line.

**--database**:
Database of the collection group.
To set the `database` attribute:

- provide the argument `--collection-group` on the command line with a
fully specified name;
- provide the argument [--collection-group] on the command line with a fully
specified name;
- provide the argument `--database` on the command line;
- the default value of argument [--database] is `(default)`.**

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

**API REFERENCE**

: This command uses the `firestore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/firestore](https://cloud.google.com/firestore)

**NOTES**

: These variants are also available:

```
gcloud alpha firestore fields ttls list
```

```
gcloud beta firestore fields ttls list
```