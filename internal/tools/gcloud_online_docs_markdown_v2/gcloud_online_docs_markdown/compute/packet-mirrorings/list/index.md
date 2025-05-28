# gcloud compute packet-mirrorings list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list)*

**NAME**

: **gcloud compute packet-mirrorings list - list Google Compute Engine packet mirroring policies**

**SYNOPSIS**

: **`gcloud compute packet-mirrorings list` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#NAME)` …] [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#REGEXP)`] [`[--regions](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--regions)`=`REGION`,[`[REGION](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#REGION)`,…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute packet-mirrorings list` displays all Google Compute
Engine packet mirroring policies in a project.
By default, packet mirroring policies from all regions are listed. The results
can be narrowed down using a filter: `--filter="region:( REGION …
)"`.

**EXAMPLES**

: To list all packet mirroring policies in a project in table form, run:

```
gcloud compute packet-mirrorings list
```

To list the URIs of all packet mirroring policies in a project, run:

```
gcloud compute packet-mirrorings list --uri
```

To list all packet mirroring policies in the
``us-central1`` and
``europe-west1`` regions, run:

```
gcloud compute packet-mirrorings list --filter="region:( us-central1 europe-west1 )"
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
gcloud alpha compute packet-mirrorings list
```

```
gcloud beta compute packet-mirrorings list
```