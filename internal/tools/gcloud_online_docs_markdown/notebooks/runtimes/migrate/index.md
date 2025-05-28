# gcloud notebooks runtimes migrate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate)*

**NAME**

: **gcloud notebooks runtimes migrate - request for migrating runtimes**

**SYNOPSIS**

: **`gcloud notebooks runtimes migrate` (`[RUNTIME](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#RUNTIME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--async)`] [`[--post-startup-script-option](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--post-startup-script-option)`=`POST_STARTUP_SCRIPT_OPTION`; default=`"POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED"`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--service-account)`=`SERVICE_ACCOUNT`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--network)`=`NETWORK` [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--subnet)`=`SUBNET` : `[--subnet-region](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#--subnet-region)`=`SUBNET_REGION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/migrate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for migrating notebook runtimes.

**EXAMPLES**

: To migrate a runtime, run:

```
gcloud notebooks runtimes migrate example-runtime --location=us-central1
```

To migrate a runtime with a new custom network, run:

```
gcloud notebooks runtimes migrate example-runtime --location=us-central1 --network=projects/example-project/global/networks/example-network --subnet=projects/example-project/regions/us-central1/subnetworks/example-subnetwork
```

To migrate a runtime and reuse the post-startup script, run:

```
gcloud notebooks runtimes migrate example-runtime --location=us-central1 --post-startup-script-option=POST_STARTUP_SCRIPT_OPTION_RERUN
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

**--post-startup-script-option**:
Specifies the behavior of post startup script during migration.
`POST_STARTUP_SCRIPT_OPTION` must be one of:
`POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED`,
`POST_STARTUP_SCRIPT_OPTION_SKIP`,
`POST_STARTUP_SCRIPT_OPTION_RERUN`.

**--service-account**:
The service account to be included in the Compute Engine instance of the new
Workbench Instance when the Runtime uses single user only mode for permission.
If not specified, the [Compute
Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. When the Runtime uses service
account mode for permission, it will reuse the same service account, and this
field must be empty.

**Network configs.

**Network resource - The name of the VPC that this instance is in. Format:
projects/`{project_id}`/global/networks/`{network_id}`.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `--network` on the command line.**

**Subnetwork resource - The name of the subnet that this instance is in. Format:
projects/`{project_id}`/regions/`{region}`/subnetworks/`{subnetwork_id}`.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--subnet` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--subnet**:
ID of the subnetwork or fully qualified identifier for the subnetwork.
To set the `subnet` attribute:

- provide the argument `--subnet` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--subnet-region**:
Google Cloud region of this subnetwork [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `subnet-region` attribute:

- provide the argument `--subnet` on the command line with a fully
specified name;
- provide the argument `--subnet-region` on the command line.****

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