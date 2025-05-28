# gcloud vmware network-policies external-access-rules list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list)*

**NAME**

: **gcloud vmware network-policies external-access-rules list - list VMware Engine external access rules**

**SYNOPSIS**

: **`gcloud vmware network-policies external-access-rules list` (`[--network-policy](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--network-policy)`=`NETWORK_POLICY` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List VMware Engine external access firewall rules.

**EXAMPLES**

: To list external access firewall rules in your project in the region
`us-west2` associated with network policy
`my-network-policy`, sorted from oldest to newest, run:

```
gcloud vmware network-policies external-access-rules list --location=us-west2 --project=my-project --network-policy=my-network-policy --sort-by=~create_time
```

Or:

```
gcloud vmware network-policies external-access-rules list --sort-by=~create_time --network-policy=my-network-policy
```

In the second example, the project and the location are taken from gcloud
properties `core/project` and `compute/region`
respectively.
To list custom set of fields of external access firewall rules in a project,
run:

```
gcloud vmware network-policies external-access-rules list --format="table(
        name.segment(-1):label=NAME,,
        priority,
        ipProtocol,
        sourceIpRanges.flatten(show='values'),
        sourcePorts.list(),
        destinationIpRanges.flatten(show='values'),
        destinationPorts.list(),
        action
    )"
```

**REQUIRED FLAGS**

: **VMware Engine Network Policy resource - network_policy. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--network-policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--network-policy**:
ID of the VMware Engine Network Policy or fully qualified identifier for the
VMware Engine Network Policy.
To set the `network-policy` attribute:

- provide the argument `--network-policy` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `--network-policy` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.**

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