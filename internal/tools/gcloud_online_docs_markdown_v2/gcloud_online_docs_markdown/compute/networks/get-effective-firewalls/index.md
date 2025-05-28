# gcloud compute networks get-effective-firewalls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls)*

**NAME**

: **gcloud compute networks get-effective-firewalls - get the effective firewalls of a Compute Engine network**

**SYNOPSIS**

: **`gcloud compute networks get-effective-firewalls` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#NAME)` …] [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#REGEXP)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks get-effective-firewalls` is used to get the
effective firewalls applied to the network.

**EXAMPLES**

: To get the effective firewalls of network with name example-network, run:

```
gcloud compute networks get-effective-firewalls example-network
```

To show all fields of the firewall rules, please show in JSON format with option
--format=json
To list more the fields of the rules of network example-network in table format,
run:

```
gcloud compute networks get-effective-firewalls example-network --format="table(
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

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the network to get effective firewalls.

**[`NAME` …]**:
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
gcloud alpha compute networks get-effective-firewalls
```

```
gcloud beta compute networks get-effective-firewalls
```