# gcloud dataplex environments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update)*

**NAME**

: **gcloud dataplex environments update - update a Dataplex Environment with the given configurations**

**SYNOPSIS**

: **`gcloud dataplex environments update` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#ENVIRONMENT)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--validate-only)`] [`[--compute-disk-size-gb](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--compute-disk-size-gb)`=`COMPUTE_DISK_SIZE_GB` `[--compute-max-node-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--compute-max-node-count)`=`COMPUTE_MAX_NODE_COUNT` `[--compute-node-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--compute-node-count)`=`COMPUTE_NODE_COUNT` `[--os-image-java-libraries](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--os-image-java-libraries)`=[`OS_IMAGE_JAVA_LIBRARIES`,…] `[--os-image-properties](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--os-image-properties)`=[`OS_IMAGE_PROPERTIES`,…] `[--os-image-python-packages](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--os-image-python-packages)`=[`OS_IMAGE_PYTHON_PACKAGES`,…] `[--os-image-version](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--os-image-version)`=`OS_IMAGE_VERSION`] [`[--session-enable-fast-startup](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--session-enable-fast-startup)` `[--session-max-idle-duration](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#--session-max-idle-duration)`=`SESSION_MAX_IDLE_DURATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/environments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex Environment with the given configurations.

**EXAMPLES**

: To update a Dataplex environment `test-environment` within lake
`test-lake` in location `us-central1` and change the
description to `Updated Description`, run:

```
gcloud dataplex environments update test-environment --project=test-project --location=us-central1 --lake=test-lake --description='Updated Description'
```

**POSITIONAL ARGUMENTS**

: **Environments resource - The Environment to update a Environment to. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENVIRONMENT`**:
ID of the environments or fully qualified identifier for the environments.
To set the `environment` attribute:

- provide the argument `environment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--description**:
Description of the Environment

**--display-name**:
Display Name of the Environment

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

**--compute-disk-size-gb**

**--session-enable-fast-startup**

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

: This variant is also available:

```
gcloud alpha dataplex environments update
```