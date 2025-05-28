# gcloud artifacts files update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update)*

**NAME**

: **gcloud artifacts files update - update annotations on an Artifact Registry file**

**SYNOPSIS**

: **`gcloud artifacts files update` (`[FILE](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update#FILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update#--repository)`=`REPOSITORY`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update#--annotations)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/files/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update annotations on an Artifact Registry file.

**EXAMPLES**

: To update annotations on a file named `my-file.txt` when the project
ID, repository and location defaults are set, run the following command:
CAUTION: This command will overwrite any existing annotations on the file.

```
gcloud artifacts files update my-file.txt --annotations=key1=value1,key2=value2
```

To clear all annotations on the file run the following command:

```
gcloud artifacts files update my-file.txt --annotations={}
```

**POSITIONAL ARGUMENTS**

: **File resource - The Artifact Registry file to update. The arguments in this
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

: **--annotations**:
List of annotations in the format of KEY=VALUE pairs to add, update, or remove.
Duplicate keys will be overwritten. For more details on annotations, see [https://google.aip.dev/148#annotations](https://google.aip.dev/148#annotations).

**`KEY`**:
Sets `KEY` value.

**`VALUE`**:
Sets `VALUE` value.

`Shorthand Example:`

```
--annotations=string=string
```

`JSON Example:`

```
--annotations='{"string": "string"}'
```

`File Example:`

```
--annotations=path_to_file.(yaml|json)
```

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