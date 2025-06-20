# gcloud dns operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/operations/list](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list)*

**NAME**

: **gcloud dns operations list - list Cloud DNS operations**

**SYNOPSIS**

: **`gcloud dns operations list` `[--zones](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list#--zones)`=[`ZONES`,…] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays Cloud DNS operations for one or more Cloud DNS
managed-zones (see `$ [gcloud dns managed-zones](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones)
--help`).

**EXAMPLES**

: To see the list of all operations for two managed-zones, run:

```
gcloud dns operations list --zones=zone1,zone2
```

To see the last 5 operations for two managed-zones, run:

```
gcloud dns operations list --zones=zone1,zone2 --sort-by=~start_time --limit=5
```

**REQUIRED FLAGS**

: **Zone resource - Name of one or more zones to read. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--zones` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--zones**:
IDs of the zones or fully qualified identifiers for the zones.
To set the `zone` attribute:

- provide the argument `--zones` on the command line.**

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

: These variants are also available:

```
gcloud alpha dns operations list
```

```
gcloud beta dns operations list
```