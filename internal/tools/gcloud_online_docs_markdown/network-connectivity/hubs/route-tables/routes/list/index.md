# gcloud network-connectivity hubs route-tables routes list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list)*

**NAME**

: **gcloud network-connectivity hubs route-tables routes list - list routes**

**SYNOPSIS**

: **`gcloud network-connectivity hubs route-tables routes list` [`[--effective-location](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--effective-location)`=`EFFECTIVE_LOCATION`] [`[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--hub)`=`HUB` `--route_table`=`ROUTE_TABLE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/route-tables/routes/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve and display a list of all routes in the specified route table.

**EXAMPLES**

: To list all routes across all route tables, run:

```
gcloud network-connectivity hubs route-tables routes list --hub=- --route_table=-
```

To list all routes in route table `my-route-table`, run:

```
gcloud network-connectivity hubs route-tables routes list --hub=my-hub --route_table=my-route-table
```

To list all routes in route table `my-route-table`, effective at a
location/region run:

```
gcloud network-connectivity hubs route-tables routes list --hub=my-hub --route_table=my-route-table --effective-location=location
```

**FLAGS**

: **--effective-location**:
The effective location/region to limit the list of routes. The effective
location must be a valid region name. To list valid region names, use 'gcloud
compute regions list'.

**Route table resource - Parent route table of the routes to display. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--route_table` on the command line with a fully
specified name;
- if route table is empty, will use wildcard '-' to list all route tables with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--hub**:
Id of the hub.
To set the `hub` attribute:

- provide the argument `--route_table` on the command line with a fully
specified name;
- if route table is empty, will use wildcard '-' to list all route tables with a
fully specified name;
- provide the argument `--hub` on the command line;
- if hub is empty, will use the wildcard '-' to indicate all hubs.

**--route_table**:
ID of the route table or fully qualified identifier for the route table.
To set the `route_table` attribute:

- provide the argument `--route_table` on the command line;
- if route table is empty, will use wildcard '-' to list all route tables .**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs route-tables routes list
```