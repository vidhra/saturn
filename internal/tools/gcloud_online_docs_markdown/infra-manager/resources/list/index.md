# gcloud infra-manager resources list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list)*

**NAME**

: **gcloud infra-manager resources list - list resources**

**SYNOPSIS**

: **`gcloud infra-manager resources list` (`[--revision](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--revision)`=`REVISION` : `[--deployment](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--deployment)`=`DEPLOYMENT` `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/resources/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List resources for a deployment revision

**EXAMPLES**

: To list all resources for a deployment revision,
projects/p1/locations/l1/deployments/d1/revisions/r-0, run:

```
gcloud infra-manager resources list --revision=projects/p1/locations/l1/deployments/d1/revisions/r-0
```

**REQUIRED FLAGS**

: **Revision resource - The deployment revision for which we want to list all
resources. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--revision` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--revision**:
ID of the revision or fully qualified identifier for the revision.
To set the `revision` attribute:

- provide the argument `--revision` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--deployment**:
deployments TBD
To set the `deployment` attribute:

- provide the argument `--revision` on the command line with a fully
specified name;
- provide the argument `--deployment` on the command line.

**--location**:
locations TBD
To set the `location` attribute:

- provide the argument `--revision` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

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

**API REFERENCE**

: This command uses the `config/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/infrastructure-manager/docs](https://cloud.google.com/infrastructure-manager/docs)