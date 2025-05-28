# gcloud iam policy-bindings search-target-policy-bindings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings)*

**NAME**

: **gcloud iam policy-bindings search-target-policy-bindings - search policy bindings by target**

**SYNOPSIS**

: **`gcloud iam policy-bindings search-target-policy-bindings` `[--target](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--target)`=`TARGET` (`[--location](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--location)`=`LOCATION` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--organization)`=`ORGANIZATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search policy bindings by target.

**EXAMPLES**

: To search for policy bindings with target, run:

```
gcloud iam policy-bindings search-target-policy-bindings --organization=123 --location=global --target=//cloudresourcemanager.googleapis.com/organizations/123
```

**REQUIRED FLAGS**

: **--target**:
The target resource, which is bound to the policy in the binding.
Format:

- `//iam.googleapis.com/locations/global/workforcePools/POOL_ID`
- `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID`
- `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
- `//cloudresourcemanager.googleapis.com/projects/{project_number}`
- `//cloudresourcemanager.googleapis.com/folders/{folder_id}`
- `//cloudresourcemanager.googleapis.com/organizations/{organization_id}`

**Location resource - The parent resource where this search will be performed.
This should be the nearest Resource Manager resource (project, folder, or
organization) to the target.
Format:

- `projects/{project_id}/locations/{location}`
- `projects/{project_number}/locations/{location}`
- `folders/{folder_id}/locations/{location}`
- `organizations/{organization_id}/locations/{location}` The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.

To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [iam.folders.locations, iam.organizations.locations,
iam.projects.locations].

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--folder**:
The folder id of the location resource.
To set the `folder` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [iam.folders.locations].

**--organization**:
The organization id of the location resource.
To set the `organization` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type [iam.organizations.locations].**

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

: This command uses the `iam/v3` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: This variant is also available:

```
gcloud beta iam policy-bindings search-target-policy-bindings
```