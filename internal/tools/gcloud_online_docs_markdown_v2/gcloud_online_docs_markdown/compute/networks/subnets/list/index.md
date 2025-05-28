# gcloud compute networks subnets list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list)*

**NAME**

: **gcloud compute networks subnets list - list Google Compute Engine subnetworks**

**SYNOPSIS**

: **`gcloud compute networks subnets list` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#NAME)` …] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--network)`=`NETWORK`] [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#REGEXP)`] [`[--regions](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--regions)`=`REGION`,[`[REGION](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#REGION)`,…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks subnets list` displays all Google Compute
Engine subnetworks in a project.
By default, subnetworks from all regions are listed. The results can be narrowed
down using a filter: `--filter="region:( REGION … )"`.

**EXAMPLES**

: To list all subnetworks in a project in table form, run:

```
gcloud compute networks subnets list
```

To list the URIs of all subnetworks in a project, run:

```
gcloud compute networks subnets list --uri
```

To list all subnetworks in the ``us-central1``
and ``europe-west1`` regions, run:

```
gcloud compute networks subnets list --filter="region:( us-central1 europe-west1 )"
```

**POSITIONAL ARGUMENTS**

: **[`NAME` …]**:
(DEPRECATED) If provided, show details for the specified names and/or URIs of
resources.
Argument `NAME` is deprecated. Use `--filter="name=( 'NAME'
… )"` instead.

**FLAGS**

: **--network**:
Only show subnetworks of a specific network.

**--regexp**:
(DEPRECATED) Regular expression to filter the names of the results on. Any names
that do not match the entire regular expression will be filtered out.
Flag `--regexp` is deprecated. Use
`--filter="name~'REGEXP'"` instead.

**--regions**:
If provided, only resources from the given regions are queried.

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

: These variants are also available:

```
gcloud alpha compute networks subnets list
```

```
gcloud beta compute networks subnets list
```