# gcloud network-connectivity hubs groups get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy)*

**NAME**

: **gcloud network-connectivity hubs groups get-iam-policy - get the IAM policy for a group resource**

**SYNOPSIS**

: **`gcloud network-connectivity hubs groups get-iam-policy` (`[GROUP](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#GROUP)` : `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#--hub)`=`HUB`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the IAM policy of a group. If formatted as JSON, the output can be edited
and used as a policy file for `set-iam-policy`.

**EXAMPLES**

: To get the IAM policy for a group named
``my-group`` in the hub named
``my-hub``, run:

```
gcloud network-connectivity hubs groups get-iam-policy my-group --hub="my-hub"
```

**POSITIONAL ARGUMENTS**

: **Group resource - The group for which you want the IAM policy. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GROUP`**:
ID of the group or fully qualified identifier for the group.
To set the `group` attribute:

- provide the argument `group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--hub**:
Id of the hub.
To set the `hub` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--hub` on the command line.**

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

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs groups get-iam-policy
```