# gcloud artifacts files delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete)*

**NAME**

: **gcloud artifacts files delete - delete an Artifact Registry file**

**SYNOPSIS**

: **`gcloud artifacts files delete` (`[FILE](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete#FILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete#--repository)`=`REPOSITORY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Artifact Registry file.
This command can fail for the following reasons:

- The specified file does not exist.
- The active account does not have permission to delete files.
- The repository is not a Generic repository.

**EXAMPLES**

: To delete a file named `pkg:1.0.0:file1.txt` under the current
project, repository, and location, run:

```
gcloud artifacts files delete pkg:v0.0.1:file1.txt
```

**POSITIONAL ARGUMENTS**

: **File resource - The Artifact Registry file to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FILE`**:
ID of the file or fully qualified identifier for the file.
To set the `file` attribute:

- provide the argument `file` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the file. Overrides the default artifacts/location property value
for this command invocation. To configure the default location, use the command:
gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
The repository associated with the file. Overrides the default
artifacts/repository property value for this command invocation. To configure
the default repository, use the command: gcloud config set artifacts/repository.
To set the `repository` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

**FLAGS**

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

**API REFERENCE**

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)