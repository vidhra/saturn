# gcloud compute tpus  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus](https://cloud.google.com/sdk/gcloud/reference/compute/tpus)*

**NAME**

: **gcloud compute tpus - list, create, and delete Cloud TPUs**

**SYNOPSIS**

: **`gcloud compute tpus` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/tpus#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/tpus#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List, create, and delete Cloud TPUs.
For more information about Cloud TPUs, see the [Cloud TPUs documentation](https://cloud.google.com/tpu/docs/tpus).
See also: [Cloud TPUs
API](https://cloud.google.com/tpu/docs/reference/rest/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[accelerator-types](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/accelerator-types)`**:
List or Describe Available Cloud TPU accelerator types.

**`[execution-groups](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups)`**:
Command group that helps create and manage Cloud TPUs and Compute VMs.

**`[locations](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/locations)`**:
List or Describe Available Cloud TPU Locations.

**`[queued-resources](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources)`**:
List, create, delete, and manage Queued Resources.

**`[topologies](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/topologies)`**:
List available Cloud TPU topologies.

**`[tpu-vm](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm)`**:
List, create, and manage Cloud TPU VM nodes.

**`[versions](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/versions)`**:
Explore Available Tensorflow versions for Cloud TPUs.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/create)`**:
Create a new Cloud TPU.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/delete)`**:
Deletes a Cloud TPU.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/describe)`**:
Describe a Cloud TPU.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/list)`**:
List Cloud TPUs.

**`[reimage](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/reimage)`**:
Reimages the OS on a Cloud TPU.

**`[start](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/start)`**:
Start a Cloud TPU.

**`[stop](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/stop)`**:
Stop a Cloud TPU.

**NOTES**

: These variants are also available:

```
gcloud alpha compute tpus
```

```
gcloud beta compute tpus
```