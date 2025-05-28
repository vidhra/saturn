# gcloud pubsub schemas list-revisions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions)*

**NAME**

: **gcloud pubsub schemas list-revisions - list revisions of a Pub/Sub schema**

**SYNOPSIS**

: **`gcloud pubsub schemas list-revisions` `[SCHEMA](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#SCHEMA)` [`[--view](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--view)`=`VIEW`; default="basic"] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List revisions of a Pub/Sub schema.

**EXAMPLES**

: To list the revisions for a schema, run:

```
gcloud pubsub schemas list-revisions my-schema
```

**POSITIONAL ARGUMENTS**

: **Schema resource - Parent Pub/Sub schema to list all contained revisions. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `schema` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCHEMA`**:
ID of the schema or fully qualified identifier for the schema.
To set the `schema` attribute:

- provide the argument `schema` on the command line.**

**FLAGS**

: **--view**:
There are two possible views, 'basic' and 'full', default is 'basic'.
`VIEW` must be one of:

**`basic`**:
Include the name and type of the schema, but not the definition.

**`full`**:
Include all Schema object fields.

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

: This command uses the `pubsub/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/pubsub/docs](https://cloud.google.com/pubsub/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub schemas list-revisions
```

```
gcloud beta pubsub schemas list-revisions
```