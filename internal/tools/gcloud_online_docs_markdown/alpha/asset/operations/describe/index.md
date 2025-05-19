# gcloud alpha asset operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/operations/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/operations/describe)*

**NAME**

: **gcloud alpha asset operations describe - describe a Cloud Asset Inventory operation**

**SYNOPSIS**

: **`gcloud alpha asset operations describe` `[OPERATION_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/operations/describe#OPERATION_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Cloud Asset Inventory operation.

**EXAMPLES**

: To describe the operation
'projects/19306908007/operations/ExportAssets/RESOURCE/78689643348272423423',
run:

```
gcloud alpha asset operations describe projects/19306908007/operations/ExportAssets/RESOURCE/78689643348272423423
```

**POSITIONAL ARGUMENTS**

: **`OPERATION_NAME`**:
Name of the operation to describe.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset operations describe
```

```
gcloud beta asset operations describe
```