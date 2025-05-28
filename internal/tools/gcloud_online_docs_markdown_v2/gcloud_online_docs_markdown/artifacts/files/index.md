# gcloud artifacts files  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/files](https://cloud.google.com/sdk/gcloud/reference/artifacts/files)*

**NAME**

: **gcloud artifacts files - manage Artifact Registry files**

**SYNOPSIS**

: **`gcloud artifacts files` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/files#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/files#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all files in the current project and `artifacts/repository`
and `artifacts/location` properties are set, run:

```
gcloud artifacts files list
```

To list files under repository my-repo in the current project and location, run:

```
gcloud artifacts files list --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete)`**:
Delete an Artifact Registry file.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/describe)`**:
Describe an Artifact Registry file.

**`[download](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download)`**:
Download an Artifact Registry file.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/list)`**:
List Artifact Registry files.

**`[update](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update)`**:
Update annotations on an Artifact Registry file.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts files
```

```
gcloud beta artifacts files
```