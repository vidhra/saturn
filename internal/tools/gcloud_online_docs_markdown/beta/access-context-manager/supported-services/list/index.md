# gcloud beta access-context-manager supported-services list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list)*

**NAME**

: **gcloud beta access-context-manager supported-services list - lists all VPC Service Controls supported services**

**SYNOPSIS**

: **`gcloud beta access-context-manager supported-services list` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Lists the services that VPC Service Controls supports. The
services that are in this list fully support VPC Service Controls or the
integration of this service with VPC Service Controls is in [Preview
stage](https://cloud.google.com/products#product-launch-stages), or the service integration is scheduled to be shut down and removed
which is in [Deprecation stage]
(https://cloud.google.com/products#product-launch-stages). Services that aren't
in this list don't support VPC Service Controls and aren't guaranteed to
function properly in a VPC Service Controls environment.

**EXAMPLES**

: To list VPC Service Controls supported services, run:

```
gcloud beta access-context-manager supported-services list
```

This command prints out a list of all supported services in a tabular form:

```
NAME                    TITLE                SERVICE_SUPPORT_STAGE  AVAILABLE_ON_RESTRICTED_VIP KNOWN_LIMITATIONS
vpcsc_supported_service VPC-SC Supported API GA                     True                        False
```

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

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager supported-services list
```

```
gcloud alpha access-context-manager supported-services list
```