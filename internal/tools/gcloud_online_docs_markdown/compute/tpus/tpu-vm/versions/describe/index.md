# gcloud compute tpus tpu-vm versions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/describe](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/describe)*

**NAME**

: **gcloud compute tpus tpu-vm versions describe - describe a runtime version available for Cloud TPU VM nodes**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm versions describe` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/describe#VERSION)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/describe#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get details on a runtime version.

**EXAMPLES**

: To describe the TensorFlow `1.15` runtime version in zone
`us-central1-b`, run:

```
gcloud compute tpus tpu-vm versions describe 1.15 --zone=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **Runtime version resource - Name of the runtime version to describe. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VERSION`**:
ID of the runtime_version or fully qualified identifier for the runtime_version.
To set the `version` attribute:

- provide the argument `version` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
Zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
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

: This command uses the `tpu/v2` API. The full documentation for this
API can be found at: [https://cloud.google.com/tpu/](https://cloud.google.com/tpu/)

**NOTES**

: This variant is also available:

```
gcloud alpha compute tpus tpu-vm versions describe
```