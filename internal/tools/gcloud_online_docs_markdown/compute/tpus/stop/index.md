# gcloud compute tpus stop  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop)*

**NAME**

: **gcloud compute tpus stop - stop a Cloud TPU**

**SYNOPSIS**

: **`gcloud compute tpus stop` (`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop#TPU)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Stop a Cloud TPU.

**EXAMPLES**

: The following command stops a TPU with ID `my-tpu` in zone
`us-central1-b`:

```
gcloud compute tpus stop my-tpu --zone=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **Tpu resource - The Cloud TPU to stop. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `tpu` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TPU`**:
ID of the tpu or fully qualified identifier for the tpu.
To set the `tpu` attribute:

- provide the argument `tpu` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The compute/zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `tpu` on the command line with a fully specified
name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

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

**API REFERENCE**

: This command uses the `tpu/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/tpu/](https://cloud.google.com/tpu/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute tpus stop
```

```
gcloud beta compute tpus stop
```