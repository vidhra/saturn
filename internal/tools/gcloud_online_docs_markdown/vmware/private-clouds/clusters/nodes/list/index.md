# gcloud vmware private-clouds clusters nodes list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list)*

**NAME**

: **gcloud vmware private-clouds clusters nodes list - list nodes in a Google Cloud VMware Engine private cloud's cluster**

**SYNOPSIS**

: **`gcloud vmware private-clouds clusters nodes list` (`[--cluster](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--cluster)`=`CLUSTER` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--private-cloud)`=`PRIVATE_CLOUD`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/nodes/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List nodes in a VMware Engine private cloud's cluster.

**EXAMPLES**

: To list nodes in the `my-private-cloud` private cloud and
`my-cluster` cluster:

```
gcloud vmware private-clouds clusters nodes list --location=us-west2-a --project=my-project --private-cloud=my-private-cloud --cluster=my-cluster
```

```
Or:
```

```
gcloud vmware private-clouds clusters nodes list --private-cloud=my-private-cloud --cluster=my-cluster
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/zone.

**REQUIRED FLAGS**

: **Cluster resource - cluster. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--cluster**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `--cluster` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--private-cloud` on the command line.**

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