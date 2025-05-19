# gcloud alpha artifacts generic download  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download)*

**NAME**

: **gcloud alpha artifacts generic download - download a generic artifact from a generic artifact repository**

**SYNOPSIS**

: **`gcloud alpha artifacts generic download` `[--destination](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--destination)`=`DESTINATION` `[--package](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--package)`=`ARTIFACT` `[--version](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--version)`=`VERSION` [`[--chunk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--chunk-size)`=`CHUNK_SIZE`] [`[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--name)`=`NAME`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#--repository)`=`REPOSITORY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/generic/download#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Download a generic artifact from a generic artifact
repository.

**EXAMPLES**

: To download version v0.1.0 of myfile.txt located in a repository in
"us-central1" to /path/to/destination/:

```
gcloud alpha artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/ --name=myfile.txt
```

To download version v0.1.0 of myfile.txt in 8000 byte chunks located in a
repository in "us-central1" to /path/to/destination/:

```
gcloud alpha artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/ --name=myfile.txt --chunk-size=8000
```

To download all files of version v0.1.0 and package mypackage located in a
repository in "us-central1" to /path/to/destination/ while maintaining the
folder hierarchy:

```
gcloud alpha artifacts generic download --location=us-central1 --project=myproject --repository=myrepo --package=mypackage --version=v0.1.0 --destination=/path/to/destination/
```

**REQUIRED FLAGS**

: **--destination**:
The path where you want to save the downloaded file.

**--package**:
The artifact to download.

**--version**:
The version of the artifact to download.

**OPTIONAL FLAGS**

: **--chunk-size**:
If specified, the chunk size (bytes) to use for downloading the package.

**--name**:
If specified, the file name within the artifact to download.

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
gcloud artifacts generic download
```

```
gcloud beta artifacts generic download
```