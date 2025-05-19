# gcloud asset feeds list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list)*

**NAME**

: **gcloud asset feeds list - list Cloud Asset Inventory Feeds**

**SYNOPSIS**

: **`gcloud asset feeds list` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/feeds/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Cloud Asset Inventory Feeds under a parent resource.

**EXAMPLES**

: To list feeds in organization 'org1', run:

```
gcloud asset feeds list --organization=org1
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

: These variants are also available:

```
gcloud alpha asset feeds list
```

```
gcloud beta asset feeds list
```