# gcloud dataplex zones list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list)*

**NAME**

: **gcloud dataplex zones list - list Dataplex zone resources under a lake**

**SYNOPSIS**

: **`gcloud dataplex zones list` (`[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--lake)`=`LAKE` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Dataplex zone resource under a specific project. location, and lake.

**EXAMPLES**

: To list all Dataplex zone resources within lake `test-lake` in
location `us-central`, run:

```
gcloud dataplex zones list --location=us-central1 --lake=test-lake
```

**REQUIRED FLAGS**

: **Lake resource - Arguments and flags that define the Dataplex zone you want to
list. The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--lake` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--lake**:
ID of the lake or fully qualified identifier for the lake.
To set the `lake` attribute:

- provide the argument `--lake` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `--lake` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex zones list
```