# gcloud compute network-firewall-policies get-effective-firewalls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls)*

**NAME**

: **gcloud compute network-firewall-policies get-effective-firewalls - get the effective firewalls for a network**

**SYNOPSIS**

: **`gcloud compute network-firewall-policies get-effective-firewalls` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--network)`=`NETWORK` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute network-firewall-policies get-effective-firewalls` is
used to get the effective firewalls applied to the network, including regional
firewalls in a specified region.

**EXAMPLES**

: To get the effective firewalls of network with name
``example-network``, including effective
regional firewalls for that network, in region
``region-a``, run:

```
gcloud compute network-firewall-policies get-effective-firewalls --network=example-network --region=region-a
```

To show all fields of the firewall rules, please show in JSON format with option
--format=json
To list more the fields of the rules of network
``example-network`` in table format, run:

```
gcloud compute network-firewall-policies get-effective-firewalls --network=example-network --region=region-a --format="table(
  type,
  firewall_policy_name,
  rule_type,
  priority,
  action,
  direction,
  ip_ranges.list():label=IP_RANGES,
  target_svc_acct,
  enableLogging,
  description,
  name,
  disabled,
  target_tags,
  src_svc_acct,
  src_tags,
  ruleTupleCount,
  targetResources:label=TARGET_RESOURCES)"
```

**REQUIRED FLAGS**

: **--network**:
The network to get the effective firewalls for.

**FLAGS**

: **--region**:
The region to get the effective regional firewalls.

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
gcloud alpha compute network-firewall-policies get-effective-firewalls
```

```
gcloud beta compute network-firewall-policies get-effective-firewalls
```