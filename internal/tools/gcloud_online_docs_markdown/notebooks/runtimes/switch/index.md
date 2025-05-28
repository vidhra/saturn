# gcloud notebooks runtimes switch  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch)*

**NAME**

: **gcloud notebooks runtimes switch - request for switching runtimes**

**SYNOPSIS**

: **`gcloud notebooks runtimes switch` (`[RUNTIME](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#RUNTIME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#--async)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#--machine-type)`=`MACHINE_TYPE`] [`[--accelerator-core-count](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#--accelerator-core-count)`=`ACCELERATOR_CORE_COUNT` `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#--accelerator-type)`=`ACCELERATOR_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/switch#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for switching notebook runtimes.

**EXAMPLES**

: To switch a runtime, run:

```
gcloud notebooks runtimes switch example-runtime --machine-type=n1-standard-4
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--machine-type**:
machine type

**--accelerator-core-count**:
Count of cores of this accelerator.

**--accelerator-type**:
Type of this accelerator. `ACCELERATOR_TYPE` must be one
of: `NVIDIA_TESLA_A100`, `NVIDIA_TESLA_K80`,
`NVIDIA_TESLA_P100`, `NVIDIA_TESLA_V100`,
`NVIDIA_TESLA_P4`, `NVIDIA_TESLA_T4`,
`NVIDIA_TESLA_T4_VWS`, `NVIDIA_TESLA_P100_VWS`,
`NVIDIA_TESLA_P4_VWS`, `TPU_V2`, `TPU_V3`.

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