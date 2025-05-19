# gcloud alpha asset feeds delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete)*

**NAME**

: **gcloud alpha asset feeds delete - delete a Cloud Asset Inventory Feed**

**SYNOPSIS**

: **`gcloud alpha asset feeds delete` `[FEED_ID](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete#FEED_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete a Cloud Asset Inventory Feed.

**EXAMPLES**

: To delete a feed 'feed1' in project 'p1', run:

```
gcloud alpha asset feeds delete feed1 --project=p1
```

**POSITIONAL ARGUMENTS**

: **`FEED_ID`**:
Asset feed identifier to delete.

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
gcloud asset feeds delete
```

```
gcloud beta asset feeds delete
```