# gcloud compute network-endpoint-groups list-network-endpoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints)*

**NAME**

: **gcloud compute network-endpoint-groups list-network-endpoints - list network endpoints in a network endpoint group**

**SYNOPSIS**

: **`gcloud compute network-endpoint-groups list-network-endpoints` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--zone)`=`ZONE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups/list-network-endpoints#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List network endpoints in a network endpoint group.

**EXAMPLES**

: To list network endpoints of a network endpoint group named
``my-neg`` in zone
``us-central1-a``:

```
gcloud compute network-endpoint-groups list-network-endpoints my-neg --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network endpoint group to operate on.

**FLAGS**

: **--global**

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

**NOTES**

: These variants are also available:

```
gcloud alpha compute network-endpoint-groups list-network-endpoints
```

```
gcloud beta compute network-endpoint-groups list-network-endpoints
```