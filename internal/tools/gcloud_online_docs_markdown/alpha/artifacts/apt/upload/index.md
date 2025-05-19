# gcloud alpha artifacts apt upload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload)*

**NAME**

: **gcloud alpha artifacts apt upload - upload a Debian package to an artifact repository**

**SYNOPSIS**

: **`gcloud alpha artifacts apt upload` [[`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload#REPOSITORY)`] `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload#--location)`=`LOCATION`] `[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload#--source)`=`SOURCE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/apt/upload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha artifacts apt upload` uploads a
Debian package to the specified artifact repository.

**EXAMPLES**

: To upload the package `my-package.deb` to `my-repo`, run:

```
gcloud alpha artifacts apt upload my-repo --location=us-central1 --source=my-package.deb
```

**POSITIONAL ARGUMENTS**

: **Repository resource - The Artifact Registry repository. If not specified, the
current artifacts/repository is used. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`REPOSITORY`]**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line;
- set the property `artifacts/repository`.

**--location**:
Location of the repository.
To set the `location` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

**REQUIRED FLAGS**

: **--source**:
The path of a package to upload.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts apt upload
```

```
gcloud beta artifacts apt upload
```