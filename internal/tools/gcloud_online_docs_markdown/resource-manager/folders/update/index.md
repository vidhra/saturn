# gcloud resource-manager folders update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/update](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/update)*

**NAME**

: **gcloud resource-manager folders update - update the display name of a folder**

**SYNOPSIS**

: **`gcloud resource-manager folders update` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/update#FOLDER_ID)` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/update#--display-name)`=`DISPLAY_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the given folder with new folder name.
This command can fail for the following reasons:

- There is no folder with the given ID.
- The active account does not have permission to update the given folder.
- The new display name is taken by another folder under this folder's parent.

**EXAMPLES**

: The following command updates a folder with the ID `123456789` to
have the name "Foo Bar and Grill":

```
gcloud resource-manager folders update 123456789 --display-name="Foo Bar and Grill"
```

**POSITIONAL ARGUMENTS**

: **`FOLDER_ID`**:
ID for the folder you want to update.

**REQUIRED FLAGS**

: **--display-name**:
New display name for the folder (unique under the same parent).

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
gcloud alpha resource-manager folders update
```

```
gcloud beta resource-manager folders update
```