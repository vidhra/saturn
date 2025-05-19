# gcloud alpha asset saved-queries list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list)*

**NAME**

: **gcloud alpha asset saved-queries list - list Cloud Asset Inventory saved query**

**SYNOPSIS**

: **`gcloud alpha asset saved-queries list` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List Cloud Asset Inventory saved queries under a parent
resource.

**EXAMPLES**

: To list saved queries in organization 'org1', run:

```
gcloud alpha asset saved-queries list --organization=org1
```

**REQUIRED FLAGS**

: **--folder**

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
gcloud asset saved-queries list
```

```
gcloud beta asset saved-queries list
```