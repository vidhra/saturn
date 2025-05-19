# gcloud artifacts packages  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/packages](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages)*

**NAME**

: **gcloud artifacts packages - manage Artifact Registry packages**

**SYNOPSIS**

: **`gcloud artifacts packages` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all packages in the current project and
`artifacts/repository` and `artifacts/location` properties
are set, run:

```
gcloud artifacts packages list
```

To list packages under repository my-repo in the current project and location,
run:

```
gcloud artifacts packages list --repository=my-repo
```

To delete package `my-pkg` under repository my-repo in the current
project and location, run:

```
gcloud artifacts packages delete my-pkg --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/delete)`**:
Delete an Artifact Registry package.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/describe)`**:
Describe an Artifact Registry package.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list)`**:
List Artifact Registry packages.

**`[update](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update)`**:
Update annotations on an Artifact Registry package.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts packages
```

```
gcloud beta artifacts packages
```