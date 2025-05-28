# gcloud resource-manager folders move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move)*

**NAME**

: **gcloud resource-manager folders move - move a folder to a new position within the same organization**

**SYNOPSIS**

: **`gcloud resource-manager folders move` `[FOLDER_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move#FOLDER_ID)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move#--async)`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move#--folder)`=`FOLDER_ID`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move#--organization)`=`ORGANIZATION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/folders/move#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Move the given folder under a new parent folder or under the organization.
Exactly one of --folder or --organization must be provided.
This command can fail for the following reasons:

- There is no folder with the given ID.
- There is no parent with the given type and ID.
- The new parent is not in the same organization of the given folder.
- Permission missing for performing this move.

**EXAMPLES**

: The following command moves a folder with the ID `123456789` into a
folder with the ID `2345`:

```
gcloud resource-manager folders move 123456789 --folder=2345
```

The following command moves a folder with the ID `123456789` into an
organization with ID `1234`:

```
gcloud resource-manager folders move 123456789 --organization=1234
```

**POSITIONAL ARGUMENTS**

: **`FOLDER_ID`**:
ID for the folder you want to move.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--folder**:
ID for the folder to use as a parent

**--organization**:
ID for the organization to use as a parent

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
gcloud alpha resource-manager folders move
```

```
gcloud beta resource-manager folders move
```