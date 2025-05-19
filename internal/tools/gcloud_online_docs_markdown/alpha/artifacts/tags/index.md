# gcloud alpha artifacts tags  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags)*

**NAME**

: **gcloud alpha artifacts tags - manage Artifact Registry tags**

**SYNOPSIS**

: **`gcloud alpha artifacts tags` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create tag with the name `my-tag` for version `1.0.0`
of package `my-pkg` in the current project with
`artifacts/repository` and `artifacts/location` properties
are set, run:

```
gcloud alpha artifacts tags create my-tag --package=my-pkg --version=1.0.0
```

To list all tags under package `my-pkg`, run:

```
gcloud alpha artifacts tags list --package=my-pkg
```

To update tag `my-tag` from a different version to version
`1.0.0` of package `my-pkg`, run:

```
gcloud alpha artifacts tags update my-tag --version=1.0.0 --package=my-pkg
```

To delete tag `my-tag` of package `my-pkg`, run:

```
gcloud alpha artifacts tags delete my-tag --package=my-pkg
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/create)`**:
`(ALPHA)` Create an Artifact Registry tag.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/delete)`**:
`(ALPHA)` Delete an Artifact Registry tag.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list)`**:
`(ALPHA)` List Artifact Registry tags.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/update)`**:
`(ALPHA)` Update an Artifact Registry tag.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts tags
```

```
gcloud beta artifacts tags
```