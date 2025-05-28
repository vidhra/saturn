# gcloud spanner backups list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list)*

**NAME**

: **gcloud spanner backups list - list existing Cloud Spanner Cloud Spanner backups**

**SYNOPSIS**

: **`gcloud spanner backups list` [`[--database](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--database)`=`DATABASE`] [`[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--instance)`=`INSTANCE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/backups/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List existing Cloud Spanner Cloud Spanner backups.

**EXAMPLES**

: To list existing backups for the instance, run:

```
gcloud spanner backups list --instance=INSTANCE_NAME
```

To list existing backups for a database, run:

```
gcloud spanner backups list --instance=INSTANCE_NAME --database=DATABASE
```

**FLAGS**

: **--database**:
ID of the source database. The database flag will take precedence over filters
added for database.

**Instance resource - Cloud Spanner instance ID. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--instance` on the command line with a fully
specified name;
- set the property `spanner/instance` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--instance**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

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

: This command uses the `spanner/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/spanner/](https://cloud.google.com/spanner/)

**NOTES**

: These variants are also available:

```
gcloud alpha spanner backups list
```

```
gcloud beta spanner backups list
```