# gcloud alpha compute instance-groups list-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances)*

**NAME**

: **gcloud alpha compute instance-groups list-instances - list instances present in the instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups list-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#NAME)` [`[--regexp](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--regexp)`=`REGEXP`, `[-r](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#-r)` `[REGEXP](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#REGEXP)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--zone)`=`ZONE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups
list-instances` list instances in an instance group.
The required permission to execute this command is
`compute.instanceGroups.list`. If needed, you can include this
permission, or choose any of the following preexisting IAM roles that contain
this particular permission:

- Compute Admin
- Compute Viewer
- Compute Instance Admin (v1)
- Compute Instance Admin (beta)
- Compute Network Admin
- Compute Network Viewer
- Editor
- Owner
- Security Reviewer
- Viewer

For more information regarding permissions required by instance groups, refer to
Compute Engine's access control guide: [https://cloud.google.com/compute/docs/access/iam](https://cloud.google.com/compute/docs/access/iam).

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to operate on.

**FLAGS**

: **--regexp**:
A regular expression to filter the names of the results on. Any names that do
not match the entire regular expression will be filtered out.

**--region**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups list-instances
```

```
gcloud beta compute instance-groups list-instances
```