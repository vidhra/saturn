# gcloud compute tpus tpu-vm update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update)*

**NAME**

: **gcloud compute tpus tpu-vm update - update a Cloud TPU VM node**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm update` (`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#TPU)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--zone)`=`ZONE`) [`[--add-tags](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--add-tags)`=[`TAGS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--description)`=`DESCRIPTION`] [`[--internal-ips](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--internal-ips)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--attach-disk](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--attach-disk)`=[`SOURCE`=`DATA_DISK`,…]     | `[--detach-disk](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--detach-disk)`=`DATA_DISK`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--remove-labels)`=[`KEY`,…]] [`[--clear-tags](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--clear-tags)`     | `[--remove-tags](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--remove-tags)`=[`TAG`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--metadata-from-file)`=[`KEY`=`VALUE`,…]     | `[--update-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--update-metadata)`=[`KEY`=`VALUE`,…] `[--clear-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--clear-metadata)`     | `[--remove-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#--remove-metadata)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud TPU VM node.

**EXAMPLES**

: To modify a TPU VM node with ID `my-tpu` in the default user project
and compute/zone by updating the description to "A new description", run:

```
gcloud compute tpus tpu-vm update my-tpu --description="A new description"
```

To modify a TPU VM node with ID `my-tpu` in the default user project,
network and compute/zone (with other defaults supplied by API) by adding labels
`k0`, with value `value0` and label `k1` with
value `value1` and removing labels with key `k2`, run:

```
gcloud compute tpus tpu-vm update my-tpu --update-labels=k0=value0,k1=value1 --remove-labels=k2
```

Labels can be used to identify the TPU VM node. To list TPU VM nodes with the
`k1:value1` label, run:

```
gcloud compute tpus tpu-vm list --filter='labels.k1=value1'
```

To list only the labels when describing a resource, use `--format` to
filter the result:

```
gcloud compute tpus tpu-vm describe my-tpu --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **Tpu resource - Name of the Cloud TPU VM node to update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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
Zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `tpu` on the command line with a fully specified
name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--add-tags**:
Tags to add to the TPU Node. Tags are used to identify valid sources or targets
for network firewalls. See [https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)
for more details.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Text description of the TPU.

**--internal-ips**:
Indicate that the IP addresses for the node should be internal. The default is
that external IP addresses will be associated with the TPU workers.

**--update-labels**:
Resource labels to update that represent user-provided metadata. If a label
exists, its value is modified. Otherwise, a new label is created. See [https://cloud.google.com/compute/docs/labeling-resources](https://cloud.google.com/compute/docs/labeling-resources)
for details.

**--attach-disk**

**--clear-labels**

**--clear-tags**

**--metadata-from-file**

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
gcloud alpha compute tpus tpu-vm update
```