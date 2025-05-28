# gcloud compute instant-snapshots list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list)*

**NAME**

: **gcloud compute instant-snapshots list - list Google Compute Engine instant snapshots**

**SYNOPSIS**

: **`gcloud compute instant-snapshots list` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#NAME)` …] [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#REGEXP)`] [`[--regions](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--regions)`=[`REGION`,…]     | `[--zones](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--zones)`=[`ZONE`,…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instant-snapshots list` displays all Google Compute
Engine instant snapshots in a project.
By default, instant snapshots from all regions and instant snapshots from all
zones are listed. The results can be narrowed down by providing the
``--regions`` or
``--zones`` flag.

**EXAMPLES**

: To list all instant snapshots in a project in table form, run:

```
gcloud compute instant-snapshots list
```

To list the URIs of all instant snapshots in a project, run:

```
gcloud compute instant-snapshots list --uri
```

To list all instant snapshots in the
``us-central1`` and
``europe-west1`` regions, given they are
regional resources, run:

```
gcloud compute instant-snapshots list --filter="region:( europe-west1 us-central1 )"
```

To list all instant snapshots in zones
``us-central1-b`` and
``europe-west1-d``, given they are zonal
resources, run:

```
gcloud compute instant-snapshots list --filter="zone:( europe-west1-d us-central1-b )"
```

**POSITIONAL ARGUMENTS**

: **[`NAME` …]**:
(DEPRECATED) If provided, show details for the specified names and/or URIs of
resources.
Argument `NAME` is deprecated. Use `--filter="name=( 'NAME'
… )"` instead.

**FLAGS**

: **--regexp**:
(DEPRECATED) Regular expression to filter the names of the results on. Any names
that do not match the entire regular expression will be filtered out.
Flag `--regexp` is deprecated. Use
`--filter="name~'REGEXP'"` instead.

**--regions**

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
gcloud alpha compute instant-snapshots list
```

```
gcloud beta compute instant-snapshots list
```