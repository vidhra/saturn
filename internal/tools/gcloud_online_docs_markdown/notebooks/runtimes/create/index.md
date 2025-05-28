# gcloud notebooks runtimes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create)*

**NAME**

: **gcloud notebooks runtimes create - request for creating an runtime**

**SYNOPSIS**

: **`gcloud notebooks runtimes create` (`[RUNTIME](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#RUNTIME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--location)`=`LOCATION`) (`[--runtime-access-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--runtime-access-type)`=`RUNTIME_ACCESS_TYPE` `[--runtime-owner](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--runtime-owner)`=`RUNTIME_OWNER`) (`[--runtime-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--runtime-type)`=`RUNTIME_TYPE`     | [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--machine-type)`=`MACHINE_TYPE` : `[--interface](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--interface)`=`INTERFACE` `[--mode](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--mode)`=`MODE` `[--source](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--source)`=`SOURCE` `[--type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--type)`=`TYPE`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--async)`] [`[--custom-gpu-driver-path](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--custom-gpu-driver-path)`=`CUSTOM_GPU_DRIVER_PATH` `[--idle-shutdown-timeout](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--idle-shutdown-timeout)`=`IDLE_SHUTDOWN_TIMEOUT` `[--install-gpu-driver](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--install-gpu-driver)`=`INSTALL_GPU_DRIVER` `[--post-startup-script](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--post-startup-script)`=`POST_STARTUP_SCRIPT` `[--post-startup-script-behavior](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#--post-startup-script-behavior)`=`POST_STARTUP_SCRIPT_BEHAVIOR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for creating notebook runtimes.

**EXAMPLES**

: To create a runtime, run:

```
gcloud notebooks runtimes create example-runtime --runtime-access-type=SINGLE_USER --runtime-owner=example@google.com --machine-type=n1-standard-4 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Runtime resource - User-defined unique name of this runtime. The runtime name
must be 1 to 63 characters long and contain only lowercase letters, numeric
characters, and dashes. The first character must be a lowercase letter and the
last character cannot be a dash. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `runtime` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RUNTIME`**:
ID of the runtime or fully qualified identifier for the runtime.
To set the `runtime` attribute:

- provide the argument `runtime` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location of this runtime [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `location` attribute:

- provide the argument `runtime` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `notebooks/location`.**

**REQUIRED FLAGS**

: **--runtime-access-type**

**--runtime-type**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--custom-gpu-driver-path**:
custom gpu driver path

**--idle-shutdown-timeout**:
idle shutdown timeout

**--install-gpu-driver**:
install gpu driver

**--post-startup-script**:
post startup script

**--post-startup-script-behavior**:
post startup script behavior

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