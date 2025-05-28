# gcloud network-connectivity hubs query-status  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status)*

**NAME**

: **gcloud network-connectivity hubs query-status - query the status of Private Service Connect propagation for a hub**

**SYNOPSIS**

: **`gcloud network-connectivity hubs query-status` `[HUB](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#HUB)` [`[--group-by](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#--group-by)`=`GROUP_BY`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Query the status of Private Service Connect propagation for a hub.

**EXAMPLES**

: To query the Private Service Connect propagation status of a hub, run:

```
gcloud network-connectivity hubs query-status HUB
```

To query the Private Service Connect propagation status of a hub grouped by
source spoke and code, run:

```
gcloud network-connectivity hubs query-status HUB --group-by="psc_propagation_status.source_spoke,psc_propagation_status.code"
```

To query the Private Service Connect propagation status of a hub sorted by the
source forwarding rule, run:

```
gcloud network-connectivity hubs query-status HUB --sort-by="psc_propagation_status.source_forwarding_rule"
```

**POSITIONAL ARGUMENTS**

: **Hub resource - Name of the hub to query Private Service Connect propagation for.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `hub` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HUB`**:
ID of the hub or fully qualified identifier for the hub.
To set the `hub` attribute:

- provide the argument `hub` on the command line.**

**FLAGS**

: **--group-by**:
Comma-separated list of resource field key names to group by. Aggregated values
will be displayed for each group. If `--group-by` is set, the value
of the `--sort-by` flag must be the same as or a subset of the
`--group-by` flag.
Accepted values are:

- 'psc_propagation_status.source_spoke'
- 'psc_propagation_status.source_group'
- 'psc_propagation_status.source_forwarding_rule'
- 'psc_propagation_status.target_spoke'
- 'psc_propagation_status.target_group'
- 'psc_propagation_status.code'

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)