# gcloud compute networks peerings list-routes  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes)*

**NAME**

: **gcloud compute networks peerings list-routes - list received or advertised routes for a VPC network peering**

**SYNOPSIS**

: **`gcloud compute networks peerings list-routes` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#NAME)` `[--direction](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--direction)`=`DIRECTION` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--network)`=`NETWORK` `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--region)`=`REGION` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/list-routes#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks peerings list-routes` is used to list
received or advertised routes for a VPC network peering. This includes
subnetwork routes, static custom routes, and dynamic custom routes.

**EXAMPLES**

: List received routes for VPC network peering in us-central1:

```
gcloud compute networks peerings list-routes peering-name --network=network-name --region=us-central1 --direction=INCOMING
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the peering to list routes for.

**REQUIRED FLAGS**

: **--direction**:
Direction of the routes to list. To list received routes, use
`INCOMING`. To list advertised routes, use `OUTGOING`.
`DIRECTION` must be one of:

**`INCOMING`**:
To list received routes.

**`OUTGOING`**:
To list advertised routes.

**--network**:
Network of the peering.

**--region**:
Region to list the routes for.

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
gcloud alpha compute networks peerings list-routes
```

```
gcloud beta compute networks peerings list-routes
```