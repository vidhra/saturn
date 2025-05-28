# gcloud scc postures list-revisions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions)*

**NAME**

: **gcloud scc postures list-revisions - list the revisions of a Cloud Security Command Center posture**

**SYNOPSIS**

: **`gcloud scc postures list-revisions` (`[POSTURE](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#POSTURE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--organization)`=`ORGANIZATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/postures/list-revisions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List the revisions of a Cloud Security Command Center (SCC) posture.

**EXAMPLES**

: To list Cloud Security Command Center posture revisions for posture
`organizations/123/locations/global/postures/posture123` , run:

```
gcloud scc postures list-revisions organizations/123/locations/global/postures/posture123
```

**POSITIONAL ARGUMENTS**

: **Posture resource - The posture whose revisions are to be listed. For example
organizations/<organizationID>/locations/<location>/postures/<postureID>.
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`POSTURE`**:
ID of the posture or fully qualified identifier for the posture.
To set the `posture` attribute:

- provide the argument `posture` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

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

: This command uses the `securityposture/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc postures list-revisions
```