# gcloud compute tpus create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create)*

**NAME**

: **gcloud compute tpus create - create a new Cloud TPU**

**SYNOPSIS**

: **`gcloud compute tpus create` (`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#TPU)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--zone)`=`ZONE`) `[--version](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--version)`=`VERSION` [`[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--accelerator-type)`=`ACCELERATOR_TYPE`; default="v2-8"] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--description)`=`DESCRIPTION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--network)`=`NETWORK`; default="default"] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--preemptible)`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#--range)`=`RANGE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Cloud TPU.

**EXAMPLES**

: The following command creates a TPU with ID `my-tpu` in the default
user project, network and compute/region (with other defaults supplied by API):

```
gcloud compute tpus create my-tpu
```

The following command creates a TPU with ID `my-tpu` with explicit
values for all required and optional parameters:

```
gcloud compute tpus create my-tpu --zone=us-central1-a --range='10.240.0.0/29' --accelerator-type='v2-8' --network=my-tf-network --description='My TF Node' --version='1.1'
```

**POSITIONAL ARGUMENTS**

: **Tpu resource - The Cloud TPU you want to create. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--version**:
TensorFlow version for the TPU, such as `1.14`. For a list of
available TensorFlow versions please see [https://www.tensorflow.org/versions/](https://www.tensorflow.org/versions/).

**OPTIONAL FLAGS**

: **--accelerator-type**:
TPU accelerator type for the TPU. If not specified, this defaults to
`v2-8`.
For a list of available accelerator types run:
`[gcloud
compute tpus accelerator-types list](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/accelerator-types/list)`

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Specifies a text description of the TPU.

**--network**:
Specifies the network that this TPU will be a part of.

**--preemptible**:
If provided, the TPU will be preemptible and time-limited. It may be preempted
to free up resources for standard TPUs, and will only be able to run for a
limited amount of time.
Preemptible TPUs cannot be restarted.

**--range**:
CIDR Range for the TPU.
The IP range that the TPU will select an IP address from. Must be in CIDR
notation and a `/29` range, for example `192.168.0.0/29`.
Errors will occur if the CIDR range has already been used for a currently
existing TPU, the CIDR range conflicts with any networks in the user's provided
network, or the provided network is peered with another network that is using
that CIDR range.

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
gcloud alpha compute tpus create
```

```
gcloud beta compute tpus create
```