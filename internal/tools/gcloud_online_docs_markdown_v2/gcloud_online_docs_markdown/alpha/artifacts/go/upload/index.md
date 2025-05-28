# gcloud alpha artifacts go upload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload)*

**NAME**

: **gcloud alpha artifacts go upload - upload a Go module to an artifact repository**

**SYNOPSIS**

: **`gcloud alpha artifacts go upload` `[--module-path](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--module-path)`=`MODULE_PATH` `[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--version)`=`VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--async)`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--source)`=`SOURCE`; default="."] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#--repository)`=`REPOSITORY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/go/upload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Upload a Go module to an artifact repository.

**EXAMPLES**

: To upload version v0.1.0 of a Go module located in /path/to/code/ to a
repository in "us-central1":

```
gcloud alpha artifacts go upload --location=us-central1 --project=myproject --repository=myrepo --module-path=the/module/path --version=v0.1.0 --source=/path/to/code
```

**REQUIRED FLAGS**

: **--module-path**:
The module path of the Go module.

**--version**:
The version of the Go module.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--source**:
The root directory of the go module source code, defaults to the current
directory.

**Repository resource - The Artifact Registry repository. If not specified, the
current artifacts/repository is used. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
Location of the repository.
To set the `location` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

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
gcloud artifacts go upload
```

```
gcloud beta artifacts go upload
```