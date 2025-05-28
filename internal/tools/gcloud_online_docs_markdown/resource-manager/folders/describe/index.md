# gcloud resource-manager folders describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/describe](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/describe)*

**NAME**

: **gcloud resource-manager folders describe - show metadata for a folder**

**SYNOPSIS**

: **`gcloud resource-manager folders describe` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/describe#FOLDER_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Shows metadata for a folder, given a valid folder ID.
This command can fail for the following reasons:

- The folder specified does not exist.
- The active account does not have permission to access the given folder.

**EXAMPLES**

: The following command prints metadata for a folder with the ID
`3589215982`:

```
gcloud resource-manager folders describe 3589215982
```

**POSITIONAL ARGUMENTS**

: **`FOLDER_ID`**:
ID for the folder you want to describe.

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
gcloud alpha resource-manager folders describe
```

```
gcloud beta resource-manager folders describe
```