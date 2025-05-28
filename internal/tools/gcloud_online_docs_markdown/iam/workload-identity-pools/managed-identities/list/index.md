# gcloud iam workload-identity-pools managed-identities list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list)*

**NAME**

: **gcloud iam workload-identity-pools managed-identities list - list workload identity pool managed identities**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools managed-identities list` (`[--namespace](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--namespace)`=`NAMESPACE` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--location)`=`LOCATION` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) [`[--show-deleted](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--show-deleted)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/managed-identities/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List workload identity pool managed identities.

**EXAMPLES**

: The following command lists all managed identities in the workload identity pool
namespace, including soft-deleted managed identities:

```
gcloud iam workload-identity-pools managed-identities list --namespace="my-namespace" --workload-identity-pool="my-workload-identity-pool" --location="global" --show-deleted
```

**REQUIRED FLAGS**

: **Workload identity pool namespace resource - Parent workload identity pool
namespace to list managed identities for. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--namespace` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--namespace**:
ID of the workload identity pool namespace or fully qualified identifier for the
workload identity pool namespace.
To set the `namespace` attribute:

- provide the argument `--namespace` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `--namespace` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--workload-identity-pool**:
The ID to use for the pool, which becomes the final component of the resource
name. This value should be 4-32 characters, and may contain the characters
[a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may
not be specified.
To set the `workload-identity-pool` attribute:

- provide the argument `--namespace` on the command line with a fully
specified name;
- provide the argument `--workload-identity-pool` on the command line.**

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