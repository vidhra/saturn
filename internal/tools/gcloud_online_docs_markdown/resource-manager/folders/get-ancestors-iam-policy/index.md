# gcloud resource-manager folders get-ancestors-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy)*

**NAME**

: **gcloud resource-manager folders get-ancestors-iam-policy - get IAM policies for a folder and its ancestors**

**SYNOPSIS**

: **`gcloud resource-manager folders get-ancestors-iam-policy` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#FOLDER_ID)` [`[--include-deny](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#--include-deny)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/get-ancestors-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get IAM policies for a folder and its ancestors, given a folder ID.

**EXAMPLES**

: To get IAM policies for folder ``3589215982``
and its ancestors, run:

```
gcloud resource-manager folders get-ancestors-iam-policy 3589215982
```

**POSITIONAL ARGUMENTS**

: **Folder resource - ID for the folder you want to get IAM policy for. This
represents a Cloud resource.
This must be specified.

**`FOLDER_ID`**:
ID of the folder or fully qualified identifier for the folder.
To set the `folder` attribute:

- provide the argument `folder_id` on the command line.**

**FLAGS**

: **--include-deny**:
Include deny policies on the project and its ancestors in the result

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

: These variants are also available:

```
gcloud alpha resource-manager folders get-ancestors-iam-policy
```

```
gcloud beta resource-manager folders get-ancestors-iam-policy
```