# gcloud notebooks instances delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete)*

**NAME**

: **gcloud notebooks instances delete - request for deleting instances**

**SYNOPSIS**

: **`gcloud notebooks instances delete` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for deleting notebook instances.

**EXAMPLES**

: To delete an instance, run:

```
gcloud notebooks instances delete example-instance --location=us-central1-b
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
gcloud alpha notebooks instances delete
```

```
gcloud beta notebooks instances delete
```