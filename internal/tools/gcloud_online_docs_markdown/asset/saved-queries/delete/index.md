# gcloud asset saved-queries delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete)*

**NAME**

: **gcloud asset saved-queries delete - delete a Cloud Asset Inventory saved query**

**SYNOPSIS**

: **`gcloud asset saved-queries delete` `[QUERY_ID](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete#QUERY_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Asset Inventory saved query.

**EXAMPLES**

: To delete a saved query with id 'query1' in project 'p1', run:

```
gcloud asset saved-queries delete query1 --project=p1
```

**POSITIONAL ARGUMENTS**

: **`QUERY_ID`**:
Asset saved query identifier to be deleted. It must be unique under the
specified parent resource project/folder/organization.

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
gcloud alpha asset saved-queries delete
```

```
gcloud beta asset saved-queries delete
```