# gcloud compute backend-services list-usable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable)*

**NAME**

: **gcloud compute backend-services list-usable - list usable backend services**

**SYNOPSIS**

: **`gcloud compute backend-services list-usable` [`[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#BACKEND_SERVICE_NAME)`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/list-usable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute backend-services list-usable` retrieves the list of
backend service resources in the specified project for which you have
compute.backendService.get and compute.backendService.use permissions. This
command is useful when you're creating load balancers in a Shared VPC
environment and you want to use [cross-project
service referencing](https://cloud.google.com/load-balancing/docs/https#cross-project). You can use this command to find out which backend
services in other projects are available to you for referencing.

**EXAMPLES**

: To list all global backend services in a project, run:

```
gcloud compute backend-services list-usable --global
```

To list all backend services in a region, run:

```
gcloud compute backend-services list-usable --region=REGION
```

**POSITIONAL ARGUMENTS**

: **[`BACKEND_SERVICE_NAME`]**:
Name of the backend service to operate on.

**FLAGS**

: **--global**

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
gcloud alpha compute backend-services list-usable
```

```
gcloud beta compute backend-services list-usable
```