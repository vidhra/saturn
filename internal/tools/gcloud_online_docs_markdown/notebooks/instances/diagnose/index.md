# gcloud notebooks instances diagnose  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose)*

**NAME**

: **gcloud notebooks instances diagnose - request for diagnose instances**

**SYNOPSIS**

: **`gcloud notebooks instances diagnose` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--location)`=`LOCATION`) `[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--gcs-bucket)`=`GCS_BUCKET` [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--async)`] [`[--enable-copy-home-files](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--enable-copy-home-files)`] [`[--enable-packet-capture](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--enable-packet-capture)`] [`[--enable-repair](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--enable-repair)`] [`[--relative-path](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--relative-path)`=`RELATIVE_PATH`] [`[--timeout-minutes](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#--timeout-minutes)`=`TIMEOUT_MINUTES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/diagnose#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for diagnose notebook instances.

**EXAMPLES**

: To diagnose an instance, run:

```
gcloud notebooks instances diagnose example-instance --location=us-west1-b --gcs-bucket=gs://example-bucket
```

To diagnose an instance with a relative path:

```
gcloud notebooks instances diagnose example-instance --location=us-west1-b --gcs-bucket=gs://example-bucket --relative-path=logs
```

To diagnose an instance, with packet capture:

```
gcloud notebooks instances diagnose example-instance --location=us-west1-b --gcs-bucket=gs://example-bucket --enable-packet-capture
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
Enables flag to capture packets from the instance for 30 seconds

**--enable-repair**:
Enables flag to repair service for instance

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

**NOTES**

: These variants are also available:

```
gcloud alpha notebooks instances diagnose
```

```
gcloud beta notebooks instances diagnose
```