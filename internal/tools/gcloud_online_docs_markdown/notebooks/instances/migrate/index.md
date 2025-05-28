# gcloud notebooks instances migrate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate)*

**NAME**

: **gcloud notebooks instances migrate - request for migrating instances**

**SYNOPSIS**

: **`gcloud notebooks instances migrate` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate#--async)`] [`[--post-startup-script-option](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate#--post-startup-script-option)`=`POST_STARTUP_SCRIPT_OPTION`; default=`"POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED"`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/migrate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for migrating notebook instances.

**EXAMPLES**

: To migrate an instance, run:

```
gcloud notebooks instances migrate example-instance --location=us-central1
```

To migrate an instance and reuse the post-startup script, run:

```
gcloud notebooks instances migrate example-instance --location=us-central1 --post-startup-script-option=POST_STARTUP_SCRIPT_OPTION_RERUN
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

**--post-startup-script-option**:
// Specifies the behavior of post startup script during migration.
`POST_STARTUP_SCRIPT_OPTION` must be one of:
`POST_STARTUP_SCRIPT_OPTION_UNSPECIFIED`,
`POST_STARTUP_SCRIPT_OPTION_SKIP`,
`POST_STARTUP_SCRIPT_OPTION_RERUN`.

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