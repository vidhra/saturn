# gcloud artifacts files download  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download)*

**NAME**

: **gcloud artifacts files download - download an Artifact Registry file**

**SYNOPSIS**

: **`gcloud artifacts files download` (`[FILE](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#FILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#--repository)`=`REPOSITORY`) `[--destination](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#--destination)`=`DESTINATION` [`[--allow-overwrite](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#--allow-overwrite)`] [`[--local-filename](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#--local-filename)`=`LOCAL_FILENAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/download#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Downloads an Artifact Registry file based on file name.

**EXAMPLES**

: To download a file named `myfile` in project `my-project`
under repository `my-repo` in `us-central1` to the local
path `~/`:

```
gcloud artifacts files download --location=us-central1 --project=my-project --repository=my-repo --destination=~/ myfile
```

To download a file named `myfile` in project `my-project`
under repository `my-repo` in `us-central1` to the local
path `~/` with file overwriting enabled:

```
gcloud artifacts files download --location=us-central1 --project=my-project --repository=my-repo --destination=~/ myfile --allow-overwrite
```

**POSITIONAL ARGUMENTS**

: **File resource - The Artifact Registry file name. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FILE`**:
ID of the file or fully qualified identifier for the file.
To set the `name` attribute:

- provide the argument `file` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the file.
To set the `location` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
Repository of the file.
To set the `repository` attribute:

- provide the argument `file` on the command line with a fully
specified name;
- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

**REQUIRED FLAGS**

: **--destination**:
The path where you want to download the file.

**OPTIONAL FLAGS**

: **--allow-overwrite**:
If specified, the command overwrites an existing file

**--local-filename**:
If specified, the name of the downloaded file on the local system is set to the
value you use for LOCAL_FILENAME. Otherwise the name of the downloaded file is
based on the file name in the registry.

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