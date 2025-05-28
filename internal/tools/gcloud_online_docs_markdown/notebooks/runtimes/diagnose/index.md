# gcloud notebooks runtimes diagnose  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose)*

**NAME**

: **gcloud notebooks runtimes diagnose - request for diagnose runtimes**

**SYNOPSIS**

: **`gcloud notebooks runtimes diagnose` (`[RUNTIME](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#RUNTIME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--location)`=`LOCATION`) `[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--gcs-bucket)`=`GCS_BUCKET` [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--async)`] [`[--enable-copy-home-files](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--enable-copy-home-files)`] [`[--enable-packet-capture](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--enable-packet-capture)`] [`[--enable-repair](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--enable-repair)`] [`[--relative-path](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--relative-path)`=`RELATIVE_PATH`] [`[--timeout-minutes](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#--timeout-minutes)`=`TIMEOUT_MINUTES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/runtimes/diagnose#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for diagnose notebook runtimes.

**EXAMPLES**

: To diagnose an runtime, run:

```
gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket
```

To diagnose an runtime with a relative path:

```
gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket --relative-path=logs
```

To diagnose an runtime, with packet capture:

```
gcloud notebooks runtimes diagnose example-runtime --location=us-central1 --gcs-bucket=gs://example-bucket --enable-packet-capture
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

: **--gcs-bucket**:
The Cloud Storage bucket where the log files generated from the diagnose command
will be stored. storage.buckets.writer permissions must be given to project's
service account or user credential. Format: gs://`{gcs_bucket}`

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-copy-home-files**:
Enables flag to copy all `/home/jupyter` folder contents

**--enable-packet-capture**:
Enables flag to capture packets from the runtime for 30 seconds

**--enable-repair**:
Enables flag to repair service for runtime

**--relative-path**:
Defines the relative storage path in the Cloud Storage bucket where the
diagnostic logs will be written. Default path will be the root directory of the
Cloud Storage bucketFormat of full path:
gs://`{gcs_bucket}`/`{relative_path}`/

**--timeout-minutes**:
Maximum amount of time in minutes before the operation times out

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