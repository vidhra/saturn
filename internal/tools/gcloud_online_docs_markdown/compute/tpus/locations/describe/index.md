# gcloud compute tpus locations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/locations/describe](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/locations/describe)*

**NAME**

: **gcloud compute tpus locations describe - describe a Cloud TPU Location**

**SYNOPSIS**

: **`gcloud compute tpus locations describe` [`[ZONE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/locations/describe#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/locations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud TPU Location.
To get a list of available locations for your project run:

```
gcloud compute tpus locations list
```

**EXAMPLES**

: The following command describes the TPUs running in zone
`us-central1-b`:

```
gcloud compute tpus locations describe us-central1-b
```

**POSITIONAL ARGUMENTS**

: **Location resource - The Cloud TPU Location you want to describe. This represents
a Cloud resource. (NOTE) Some attributes are not given arguments in this group
but can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- set the property `compute/zone` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`ZONE`]**:
ID of the location or fully qualified identifier for the location.
To set the `zone` attribute:

- provide the argument `zone` on the command line;
- set the property `compute/zone`.**

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

**API REFERENCE**

: This command uses the `tpu/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/tpu/](https://cloud.google.com/tpu/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute tpus locations describe
```

```
gcloud beta compute tpus locations describe
```