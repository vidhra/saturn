# gcloud artifacts attachments download  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download)*

**NAME**

: **gcloud artifacts attachments download - download an Artifact Registry attachment from a repository**

**SYNOPSIS**

: **`gcloud artifacts attachments download` [`[ATTACHMENT](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#ATTACHMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#--repository)`=`REPOSITORY`] `[--destination](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#--destination)`=`DESTINATION` [`[--chunk-size](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#--chunk-size)`=`CHUNK_SIZE`] [`[--oci-version-name](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#--oci-version-name)`=`OCI_VERSION_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Download an Artifact Registry attachment from a repository.

**EXAMPLES**

: To download the attachment `my-attachment` to
`/path/to/destination/`:

```
gcloud artifacts attachments download my-attachment --destination=/path/to/destination/
```

To download the attachment `my-attachment` in 8000 byte chunks to
`/path/to/destination/`:

```
gcloud artifacts attachments download my-attachment --destination=/path/to/destination/ --chunk-size=8000
```

For Docker-format repositories only: to download the attachment stored in the
OCI version
`projects/my-project/locations/us/repositories/my-repo/packages/my-package/versions/sha256:123`
to `/path/to/destination/`:

```
gcloud artifacts attachments download --oci-version-name=projects/my-project/locations/us/repositories/my-repo/packages/my-package/versions/sha256:123 --destination=/path/to/destination/
```

For Docker-format repositories only: to download the attachment stored in the
OCI version with URI
`us-docker.pkg.dev/my-project/my-repo/my-package@sha256:123` to
`/path/to/destination/`:

```
gcloud artifacts attachments download --oci-version-name=us-docker.pkg.dev/my-project/my-repo/my-package@sha256:123 --destination=/path/to/destination/
```

**POSITIONAL ARGUMENTS**

: **Attachment resource - The Artifact Registry attachment name. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**`ATTACHMENT`**:
ID of the attachment or fully qualified identifier for the attachment.
To set the `name` attribute:

- provide the argument `attachment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the attachment.
To set the `location` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
Repository of the attachment.
To set the `repository` attribute:

- provide the argument `attachment` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

**REQUIRED FLAGS**

: **--destination**:
Path where you want to save the downloaded attachment files.

**OPTIONAL FLAGS**

: **--chunk-size**:
If specified, the chunk size (bytes) to use for downloading the package.

**--oci-version-name**:
For Docker-format repositories only. The version name of the OCI artifact to
download.

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