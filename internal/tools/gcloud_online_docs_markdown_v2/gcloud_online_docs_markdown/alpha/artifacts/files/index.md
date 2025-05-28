# gcloud alpha artifacts files  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files)*

**NAME**

: **gcloud alpha artifacts files - manage Artifact Registry files**

**SYNOPSIS**

: **`gcloud alpha artifacts files` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all files in the current project and `artifacts/repository`
and `artifacts/location` properties are set, run:

```
gcloud alpha artifacts files list
```

To list files under repository my-repo in the current project and location, run:

```
gcloud alpha artifacts files list --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/files/list)`**:
`(ALPHA)` List Artifact Registry files.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts files
```

```
gcloud beta artifacts files
```