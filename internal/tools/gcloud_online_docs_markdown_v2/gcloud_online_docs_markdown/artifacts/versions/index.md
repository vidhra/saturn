# gcloud artifacts versions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/versions](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions)*

**NAME**

: **gcloud artifacts versions - manage Artifact Registry package versions**

**SYNOPSIS**

: **`gcloud artifacts versions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all versions for a package when the `artifacts/repository`
and `artifacts/location` properties are set to a repository in the
current project, run:

```
gcloud artifacts versions list --package=my-pkg
```

To delete version `1.0.0` under package `my-pkg`, run:

```
gcloud artifacts versions delete 1.0.0 --package=my-pkg
```

To delete version `1.0.0` under package `my-pkg` with its
tags, run:

```
gcloud artifacts versions delete 1.0.0 --package=my-pkg --delete-tags
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions/delete)`**:
Delete an Artifact Registry package version.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions/describe)`**:
Describe an Artifact Registry package version.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions/list)`**:
List Artifact Registry package versions.

**`[update](https://cloud.google.com/sdk/gcloud/reference/artifacts/versions/update)`**:
Update annotations on an Artifact Registry package version.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts versions
```

```
gcloud beta artifacts versions
```