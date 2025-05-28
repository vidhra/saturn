# gcloud iam workload-identity-pools namespaces list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list)*

**NAME**

: **gcloud iam workload-identity-pools namespaces list - list workload identity pool namespaces**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools namespaces list` (`[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--location)`=`LOCATION`) [`[--show-deleted](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--show-deleted)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/namespaces/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List workload identity pool namespaces.

**EXAMPLES**

: The following command lists all namespaces in the workload identity pool,
including soft-deleted namespaces:

```
gcloud iam workload-identity-pools namespaces list --workload-identity-pool="my-workload-identity-pool" --location="global" --show-deleted
```

**REQUIRED FLAGS**

: **Workload identity pool resource - The parent workload identity pool to list
namespaces for. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--workload-identity-pool` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--workload-identity-pool**:
ID of the workload identity pool or fully qualified identifier for the workload
identity pool.
To set the `workload-identity-pool` attribute:

- provide the argument `--workload-identity-pool` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `--workload-identity-pool` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--show-deleted**:
Whether to return soft-deleted resources.

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)