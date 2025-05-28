# gcloud workbench instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update)*

**NAME**

: **gcloud workbench instances update - updates a workbench instance**

**SYNOPSIS**

: **`gcloud workbench instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--machine-type)`=`MACHINE_TYPE` `[--metadata](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--metadata)`=[`KEY`=`VALUE`,…] `[--tags](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--tags)`=[`TAGS`,…] `[--accelerator-core-count](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--accelerator-core-count)`=`ACCELERATOR_CORE_COUNT` `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--accelerator-type)`=`ACCELERATOR_TYPE` [`[--container-repository](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--container-repository)`=`CONTAINER_REPOSITORY` : `[--container-tag](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--container-tag)`=`CONTAINER_TAG`] `[--custom-gpu-driver-path](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--custom-gpu-driver-path)`=`CUSTOM_GPU_DRIVER_PATH` `[--install-gpu-driver](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--install-gpu-driver)`=`INSTALL_GPU_DRIVER` `[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--shielded-integrity-monitoring)`=`SHIELDED_INTEGRITY_MONITORING` `[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--shielded-secure-boot)`=`SHIELDED_SECURE_BOOT` `[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#--shielded-vtpm)`=`SHIELDED_VTPM`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a workbench instance.

**EXAMPLES**

: To update machine type for an instance, run:

```
gcloud workbench instances update example-instance --machine-type=n1-standard-8 --location=us-central1-a
```

To update labels for an instance, run:

```
gcloud workbench instances update example-instance --labels=k1=v1,k2=v2 --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **Instance resource - User-defined unique name of this instance. The instance name
must be 1 to 63 characters long and contain only lowercase letters, numeric
characters, and dashes. The first character must be a lowercase letter and the
last character cannot be a dash. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location of this environment [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `notebooks/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--labels**:
Labels to apply to this instance. These can be later modified by the setLabels
method.

**--machine-type**

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