# gcloud bigtable authorized-views list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list)*

**NAME**

: **gcloud bigtable authorized-views list - list all authorized views of a Cloud Bigtable table**

**SYNOPSIS**

: **`gcloud bigtable authorized-views list` (`[--table](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--table)`=`TABLE` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--instance)`=`INSTANCE`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all authorized views of a Cloud Bigtable table.

**EXAMPLES**

: To list the authorized views in instance 'my-instance' and table 'my-table':

```
gcloud bigtable authorized-views list --instance=test-instance --table=test-table
```

**REQUIRED FLAGS**

: **Table resource - Cloud Bigtable table for which to list all authorized views.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--table` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--table**:
ID of the table or fully qualified identifier for the table.
To set the `table` attribute:

- provide the argument `--table` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--instance**:
Name of the Cloud Bigtable instance.
To set the `instance` attribute:

- provide the argument `--table` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

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

: This command uses the `bigtableadmin/v2` API. The full documentation
for this API can be found at: [https://cloud.google.com/bigtable/](https://cloud.google.com/bigtable/)

**NOTES**

: These variants are also available:

```
gcloud alpha bigtable authorized-views list
```

```
gcloud beta bigtable authorized-views list
```