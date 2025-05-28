# gcloud resource-manager folders create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create)*

**NAME**

: **gcloud resource-manager folders create - create a new folder**

**SYNOPSIS**

: **`gcloud resource-manager folders create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#--display-name)`=`DISPLAY_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#--async)`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#--folder)`=`FOLDER_ID`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#--organization)`=`ORGANIZATION_ID`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#--tags)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new folder in the given parent folder or organization.

**EXAMPLES**

: The following command creates a folder with the name `abc` into a
folder with the ID `2345`:

```
gcloud resource-manager folders create --display-name=abc --folder=2345
```

The following command creates a folder with the name `abc` into an
organization with ID `1234`:

```
gcloud resource-manager folders create --display-name=abc --organization=1234
```

**REQUIRED FLAGS**

: **--display-name**:
Friendly display name to use for the new folder.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--folder**:
ID for the folder to use as a parent

**--organization**:
ID for the organization to use as a parent

**--tags**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`
Note: Currently this field is in Preview.

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
gcloud alpha resource-manager folders create
```

```
gcloud beta resource-manager folders create
```