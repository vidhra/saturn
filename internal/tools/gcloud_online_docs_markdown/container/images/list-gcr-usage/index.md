# gcloud container images list-gcr-usage  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage)*

**NAME**

: **gcloud container images list-gcr-usage - list Container Registry usage**

**SYNOPSIS**

: **`gcloud container images list-gcr-usage` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--project)`=`PROJECT_ID`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/list-gcr-usage#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Container Registry usage for all projects in the specified scope
(project/organization/folder). Caller must have
`cloudasset.assets.searchAllResources` permission on the requested
scope and `storage.objects.list permission` on the Cloud Storage
buckets used by Container Registry.
The tool returns the following lists of usage states:
ACTIVE: Container Registry usage has occurred in the last 30 days. The host
location and project are not redirected.
INACTIVE: No Container Registry usage has occurred in the last 30 days. The host
location and project are not redirected.
REDIRECTED: The project has been redirected to Artifact Registry but still has
Container Registry Cloud Storage buckets. This project will continue to function
after Container Registry is turned down and no further action is required. You
can reduce costs by deleting the Container Registry Cloud Storage buckets.
REDIRECTION_INCOMPLETE: Requests are redirected to Artifact Registry, but data
is still being copied from Container Registry.
LEGACY: Container Registry usage is unknown. This state is caused by legacy
Container Registry projects that store container image metadata files in Cloud
Storage buckets. For more information on legacy Container Registry projects, see
[https://cloud.google.com/container-registry/docs/deprecations/feature-deprecations#container_image_metadata_storage_change](https://cloud.google.com/container-registry/docs/deprecations/feature-deprecations#container_image_metadata_storage_change).

**EXAMPLES**

: To list Container Registry usage in a project:

```
gcloud container images list-gcr-usage --project=my-proj
```

To list Container Registry usage in an organization:

```
gcloud container images list-gcr-usage --organization=my-org
```

To list Container Registry usage in a folder:

```
gcloud container images list-gcr-usage --folder=my-folder
```

To list all active Container Registry usage in an organization:

```
gcloud container images list-gcr-usage --organization=my-org --filter="usage=ACTIVE"
```

To list all projects that aren't redirected yet:

```
gcloud container images list-gcr-usage --organization=my-org --filter="usage!=REDIRECTED"
```

**REQUIRED FLAGS**

: **--folder**

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