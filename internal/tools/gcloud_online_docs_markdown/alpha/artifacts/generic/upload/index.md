# gcloud alpha artifacts generic upload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload)*

**NAME**

: **gcloud alpha artifacts generic upload - uploads an artifact to a generic repository**

**SYNOPSIS**

: **`gcloud alpha artifacts generic upload` `[--package](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--package)`=`PACKAGE` `[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--version)`=`VERSION` (`[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--source)`=`SOURCE`     | `[--source-directory](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--source-directory)`=`SOURCE_DIRECTORY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--async)`] [`[--destination-path](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--destination-path)`=`DESTINATION_PATH`] [`[--skip-existing](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--skip-existing)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#--repository)`=`REPOSITORY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/upload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Uploads an artifact to a generic repository.

**EXAMPLES**

: To upload version v0.1.0 of a generic artifact located in /path/to/file/ to a
repository in "us-central1":

```
gcloud alpha artifacts generic upload --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --source=/path/to/file/
```

To upload version v0.1.0 of a generic artifact located in /path/to/file/ to a
repository in "us-central1" within a folder structure:

```
gcloud alpha artifacts generic upload --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --source=/path/to/file/ --destination-path=folder/file
```

**REQUIRED FLAGS**

: **--package**:
The package to upload.

**--version**:
The version of the package. You cannot overwrite an existing version in the
repository.

**--source**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--destination-path**:
Use to specify the path to upload a generic artifact to within a folder
structure.

**--skip-existing**:
If specified, skip uploading files that already exist in the repository, and
continue to upload the remaining files.

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
gcloud artifacts generic upload
```

```
gcloud beta artifacts generic upload
```