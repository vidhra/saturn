# gcloud iam list-grantable-roles  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles)*

**NAME**

: **gcloud iam list-grantable-roles - list IAM grantable roles for a resource**

**SYNOPSIS**

: **`gcloud iam list-grantable-roles` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles#RESOURCE)` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles#--filter)`=`EXPRESSION`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles#--page-size)`=`PAGE_SIZE`; default=300] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command displays the list of grantable roles for a resource. The resource
can be referenced either via the full resource name or via a URI. User can then
add IAM policy bindings to grant the roles.

**EXAMPLES**

: List grantable roles for a project:

```
gcloud iam list-grantable-roles //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
```

List grantable roles for a resource identified via full resource name:

```
gcloud iam list-grantable-roles //compute.googleapis.com/projects/example-project/zones/us-central1-f/instances/example-instance
```

List grantable roles for a resource identified via URI:

```
gcloud iam list-grantable-roles https://www.googleapis.com/compute/v1/projects/example-project/\
zones/us-central1-f/instances/example-instance
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
The full resource name or URI to get the list of roles for.
See ["Resource
Names"](https://cloud.google.com/apis/design/resource_names) for details. To get a URI from most `list` commands in
`[gcloud](https://cloud.google.com/sdk/gcloud/reference)`, pass the
`--uri` flag. For example:

```
gcloud compute instances list --project prj --uri https://compute.googleapis.com/compute/v1/projects/prj/zones/us-east1-c/instances/i1 https://compute.googleapis.com/compute/v1/projects/prj/zones/us-east1-d/instances/i2
```

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `300`. Paging
may be applied before or after `--filter` and `--limit`
depending on the service.

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
gcloud alpha iam list-grantable-roles
```

```
gcloud beta iam list-grantable-roles
```