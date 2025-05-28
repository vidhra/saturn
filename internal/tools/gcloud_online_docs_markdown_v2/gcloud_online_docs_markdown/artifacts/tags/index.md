# gcloud artifacts tags  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/tags](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags)*

**NAME**

: **gcloud artifacts tags - manage Artifact Registry tags**

**SYNOPSIS**

: **`gcloud artifacts tags` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create tag with the name `my-tag` for version `1.0.0`
of package `my-pkg` in the current project with
`artifacts/repository` and `artifacts/location` properties
are set, run:

```
gcloud artifacts tags create my-tag --package=my-pkg --version=1.0.0
```

To list all tags under package `my-pkg`, run:

```
gcloud artifacts tags list --package=my-pkg
```

To update tag `my-tag` from a different version to version
`1.0.0` of package `my-pkg`, run:

```
gcloud artifacts tags update my-tag --version=1.0.0 --package=my-pkg
```

To delete tag `my-tag` of package `my-pkg`, run:

```
gcloud artifacts tags delete my-tag --package=my-pkg
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags/create)`**:
Create an Artifact Registry tag.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags/delete)`**:
Delete an Artifact Registry tag.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags/list)`**:
List Artifact Registry tags.

**`[update](https://cloud.google.com/sdk/gcloud/reference/artifacts/tags/update)`**:
Update an Artifact Registry tag.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts tags
```

```
gcloud beta artifacts tags
```