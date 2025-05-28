# gcloud artifacts packages update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update)*

**NAME**

: **gcloud artifacts packages update - update annotations on an Artifact Registry package**

**SYNOPSIS**

: **`gcloud artifacts packages update` (`[PACKAGE](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update#PACKAGE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update#--repository)`=`REPOSITORY`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update#--annotations)`=[`ANNOTATIONS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update annotations on an Artifact Registry package.

**EXAMPLES**

: To update annotations on a package named `my-pkg` when the project
ID, repository and location defaults are set, run the following command:
CAUTION: This command will overwrite any existing annotations on the package.

```
gcloud artifacts packages update my-pkg --annotations=key1=value1,key2=value2
```

To clear all annotations on the package run the following command:

```
gcloud artifacts packages update my-pkg --annotations={}
```

**POSITIONAL ARGUMENTS**

: **Package resource - The Artifact Registry package to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `package` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PACKAGE`**:
ID of the package or fully qualified identifier for the package.
To set the `package` attribute:

- provide the argument `package` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the package. Overrides the default artifacts/location property value
for this command invocation. To configure the default location, use the command:
gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `package` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
The repository associated with the package. Overrides the default
artifacts/repository property value for this command invocation. To configure
the default repository, use the command: gcloud config set artifacts/repository.
To set the `repository` attribute:

- provide the argument `package` on the command line with a fully
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