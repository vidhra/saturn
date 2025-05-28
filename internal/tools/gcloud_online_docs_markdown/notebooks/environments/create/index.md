# gcloud notebooks environments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create)*

**NAME**

: **gcloud notebooks environments create - request for creating environments**

**SYNOPSIS**

: **`gcloud notebooks environments create` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--location)`=`LOCATION`) ([`[--container-repository](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--container-repository)`=`CONTAINER_REPOSITORY` : `[--container-tag](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--container-tag)`=`CONTAINER_TAG`]     | [(`[--vm-image-family](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--vm-image-family)`=`VM_IMAGE_FAMILY`; default="common-cpu" | `[--vm-image-name](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--vm-image-name)`=`VM_IMAGE_NAME`) : `[--vm-image-project](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--vm-image-project)`=`VM_IMAGE_PROJECT`; default="deeplearning-platform-release"]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--display-name)`=`DISPLAY_NAME`] [`[--post-startup-script](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#--post-startup-script)`=`POST_STARTUP_SCRIPT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/environments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for creating environments.

**EXAMPLES**

: To create an environment with id 'example-environment' in location
'us-central1-a' using a container repository, run:

```
gcloud notebooks environments create example-environment --location=us-central1-a --container-repository=gcr.io/deeplearning-platform-release/base-cpu --container-tag=test-tag --description=test-description --post-startup-script=gs://path-to-file/file-name --display-name=test-display-name --async
```

To create an environment with id 'example-environment' in location
'us-central1-a' using a VM Image Family, run:

```
gcloud notebooks environments create example-environment --vm-image-project=deeplearning-platform-release --vm-image-family=caffe1-latest-cpu-experimental
```

To create an environment with id 'example-environment' in location
'us-central1-a' using a VM Image, run:

```
gcloud notebooks environments create example-environment --location=us-central1-a --vm-image-project=deeplearning-platform-release --vm-image-name=tf2-2-1-cu101-notebooks-20200110
```

**POSITIONAL ARGUMENTS**

: **Environment resource - User-defined unique name of this environment. The
environment name must be 1 to 63 characters long and contain only lowercase
letters, numeric characters, and dashes. The first character must be a
lowercaseletter and the last character cannot be a dash. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENVIRONMENT`**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `environment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location of this environment [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `location` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `notebooks/location`.**

**REQUIRED FLAGS**

: **--container-repository**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A brief description of this environment.

**--display-name**:
Name to display on the UI.

**--post-startup-script**:
Path to a Bash script that automatically runs after a notebook instance fully
boots up. The path must be a URL or Cloud Storage
path(gs://`path-to-file/`file-name`).`

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

: These variants are also available:

```
gcloud alpha notebooks environments create
```

```
gcloud beta notebooks environments create
```