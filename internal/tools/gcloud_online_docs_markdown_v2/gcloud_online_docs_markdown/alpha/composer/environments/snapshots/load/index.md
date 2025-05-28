# gcloud alpha composer environments snapshots load  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load)*

**NAME**

: **gcloud alpha composer environments snapshots load - load a snapshot into the environment**

**SYNOPSIS**

: **`gcloud alpha composer environments snapshots load` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--location)`=`LOCATION`) `[--snapshot-path](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--snapshot-path)`=`SNAPSHOT_PATH` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--async)`] [`[--skip-airflow-overrides-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--skip-airflow-overrides-setting)`] [`[--skip-environment-variables-setting](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--skip-environment-variables-setting)`] [`[--skip-gcs-data-copying](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--skip-gcs-data-copying)`] [`[--skip-pypi-packages-installation](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#--skip-pypi-packages-installation)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots/load#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Load a snapshot into the environment.

**EXAMPLES**

: To load a snapshot into the environment named env-1, run:

```
gcloud alpha composer environments snapshots load env-1 --snapshot-path=gs://my-bucket/path-to-the-specific-snapshot
```

**POSITIONAL ARGUMENTS**

: **Environment resource - The environment where to load a snapshot. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
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
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

**REQUIRED FLAGS**

: **--snapshot-path**:
The Cloud Storage path to load the snapshot from. It must start with prefix
gs:// and one needs to specify a single snapshot that should be loaded.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--skip-airflow-overrides-setting**:
When specified, skips setting Airflow overrides from the snapshot.

**--skip-environment-variables-setting**:
When specified, skips setting environment variables from the snapshot.

**--skip-gcs-data-copying**:
When specified, skips copying dags, plugins and data folders from the snapshot.

**--skip-pypi-packages-installation**:
When specified, skips the installation of custom PyPI packages from the
snapshot.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud composer environments snapshots load
```

```
gcloud beta composer environments snapshots load
```