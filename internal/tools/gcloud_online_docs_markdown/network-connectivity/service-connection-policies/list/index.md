# gcloud network-connectivity service-connection-policies list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list)*

**NAME**

: **gcloud network-connectivity service-connection-policies list - list service connection policies**

**SYNOPSIS**

: **`gcloud network-connectivity service-connection-policies list` `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#--region)`=`REGION` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve and display a list of all service connection policies in the specified
project.

**EXAMPLES**

: To list all service connection policies in region
``us-central1``, run:

```
gcloud network-connectivity service-connection-policies list --region=us-central1
```

**REQUIRED FLAGS**

: **Region resource - A Google Cloud region. Use this flag to filter the list of
service connection policies to a specific region or to all regions. Use ``-`` to
specify all regions. This represents a Cloud resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line.**

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