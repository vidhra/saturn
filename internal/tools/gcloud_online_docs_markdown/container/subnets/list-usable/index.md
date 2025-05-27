# gcloud container subnets list-usable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable)*

**NAME**

: **gcloud container subnets list-usable - list subnets usable for cluster creation in a specific project**

**SYNOPSIS**

: **`gcloud container subnets list-usable` [`[--network-project](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--network-project)`=`NETWORK_PROJECT`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/subnets/list-usable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Usability of subnetworks for cluster creation is dependent on the IAM policy of
the project's Google Kubernetes Engine Service Account. Use the
`--project` flag to evaluate subnet usability in different projects.
This list may differ from the list returned by Google Compute Engine's
`list-usable` command, which returns subnets only usable by the
caller.
To show subnetworks shared from a Shared-VPC host project, use
`--network-project` to specify the project that owns the subnetworks.

**EXAMPLES**

: List all subnetworks usable for cluster creation in project
`my-project`.

```
gcloud container subnets list-usable --project=my-project
```

List all subnetworks existing in project `my-shared-host-project`
usable for cluster creation in project `my-service-project`.

```
gcloud container subnets list-usable --project=my-service-project --network-project=my-shared-host-project
```

**FLAGS**

: **--network-project**:
The project owning the subnetworks returned. This field is translated into the
expression `networkProjectId=[PROJECT_ID]` and ANDed to the
`--filter` flag value.
Defaults to the `--project` value.

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
gcloud alpha container subnets list-usable
```

```
gcloud beta container subnets list-usable
```