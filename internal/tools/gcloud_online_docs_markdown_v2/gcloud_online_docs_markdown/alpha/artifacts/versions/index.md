# gcloud alpha artifacts versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions)*

**NAME**

: **gcloud alpha artifacts versions - manage Artifact Registry package versions**

**SYNOPSIS**

: **`gcloud alpha artifacts versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all versions for a package when the `artifacts/repository`
and `artifacts/location` properties are set to a repository in the
current project, run:

```
gcloud alpha artifacts versions list --package=my-pkg
```

To delete version `1.0.0` under package `my-pkg`, run:

```
gcloud alpha artifacts versions delete 1.0.0 --package=my-pkg
```

To delete version `1.0.0` under package `my-pkg` with its
tags, run:

```
gcloud alpha artifacts versions delete 1.0.0 --package=my-pkg --delete-tags
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions/delete)`**:
`(ALPHA)` Delete an Artifact Registry package version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/versions/list)`**:
`(ALPHA)` List Artifact Registry package versions.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts versions
```

```
gcloud beta artifacts versions
```