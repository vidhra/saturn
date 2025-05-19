# gcloud compute instance-groups managed list-errors  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors)*

**NAME**

: **gcloud compute instance-groups managed list-errors - list errors produced by managed instances in a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed list-errors` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--zone)`=`ZONE`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed list-errors` List errors that
are produced by managed instances in a managed instance group.
The required permission to execute this command is
`compute.instanceGroupManagers.list`. If needed, you can include this
permission in a custom IAM role, or choose any of the following preexisting IAM
roles that contain this particular permission:

- Compute Admin
- Compute Viewer
- Compute Instance Admin (v1)
- Compute Instance Admin (beta)
- Compute Network Admin
- Editor
- Owner
- Security Reviewer
- Viewer

For more information regarding permissions required by managed instance groups,
refer to Compute Engine's access control guide: [https://cloud.google.com/compute/docs/access/iam#managed-instance-groups-and-iam](https://cloud.google.com/compute/docs/access/iam#managed-instance-groups-and-iam).

**EXAMPLES**

: To list errors on managed instance group 'my-group', run:

```
gcloud compute instance-groups managed list-errors my-group --format=yaml
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed list-errors
```

```
gcloud beta compute instance-groups managed list-errors
```