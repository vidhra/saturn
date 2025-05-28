# gcloud resource-manager tags holds list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list)*

**NAME**

: **gcloud resource-manager tags holds list - list TagHolds under the specified TagValue**

**SYNOPSIS**

: **`gcloud resource-manager tags holds list` `[PARENT](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#PARENT)` [`[--holder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--holder)`=`HOLDER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--location)`=`LOCATION`] [`[--origin](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--origin)`=`ORIGIN`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/tags/holds/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List TagHolds under a TagValue. The TagValue can be represented with its numeric
id or its namespaced name of
{parent_namespace}/{tag_key_short_name}/{tag_value_short_name}. Limited to
TagHolds stored in a single --location: if none is provided, the API will assume
the "global" location. Optional filters are --holder and --origin: if provided,
returned TagHolds' holder and origin fields must match the exact flag value.

**EXAMPLES**

: To list TagHolds for tagValues/456 in us-central1-a, run:

```
gcloud resource-manager tags holds list tagValues/456 --location=us-central1-a
```

To list TagHolds for tagValues/456, with holder cloud-holder-resource and origin
creator-origin, run:

```
gcloud resource-manager tags holds list tagValues/456 --holder=cloud-holder-resource --origin=creator-origin
```

**POSITIONAL ARGUMENTS**

: **`PARENT`**:
TagValue resource name or namespaced name to list TagHolds for. This field
should be in the form tagValues/<id> or
<parent_namespace>/<tagkey_short_name>/<short_name>.

**FLAGS**

: **--holder**:
The holder field of the TagHold to match exactly. If not provided, the API will
return all matching TagHolds disregarding the holder field.

**--location**:
Region where the matching TagHolds are stored. If not provided, the API will
attempt to retrieve matching TagHolds from the "global" region.

**--origin**:
The origin field of the TagHold to match exactly. If not provided, the API will
return all matching TagHolds disregarding the origin field.

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
gcloud alpha resource-manager tags holds list
```

```
gcloud beta resource-manager tags holds list
```