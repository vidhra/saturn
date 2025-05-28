# gcloud resource-manager folders delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/delete](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/delete)*

**NAME**

: **gcloud resource-manager folders delete - delete a folder**

**SYNOPSIS**

: **`gcloud resource-manager folders delete` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/delete#FOLDER_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a folder, given a valid folder ID.
This command can fail for the following reasons:

- There is no folder with the given ID.
- The active account does not have permission to delete the given folder.
- The folder to be deleted is not empty.

**EXAMPLES**

: The following command deletes a folder with the ID `123456789`:

```
gcloud resource-manager folders delete 123456789
```

**POSITIONAL ARGUMENTS**

: **`FOLDER_ID`**:
ID for the folder you want to delete.

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
gcloud alpha resource-manager folders delete
```

```
gcloud beta resource-manager folders delete
```