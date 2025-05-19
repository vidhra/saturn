# gcloud alpha artifacts packages  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages)*

**NAME**

: **gcloud alpha artifacts packages - manage Artifact Registry packages**

**SYNOPSIS**

: **`gcloud alpha artifacts packages` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all packages in the current project and
`artifacts/repository` and `artifacts/location` properties
are set, run:

```
gcloud alpha artifacts packages list
```

To list packages under repository my-repo in the current project and location,
run:

```
gcloud alpha artifacts packages list --repository=my-repo
```

To delete package `my-pkg` under repository my-repo in the current
project and location, run:

```
gcloud alpha artifacts packages delete my-pkg --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages/delete)`**:
`(ALPHA)` Delete an Artifact Registry package.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/packages/list)`**:
`(ALPHA)` List Artifact Registry packages.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts packages
```

```
gcloud beta artifacts packages
```