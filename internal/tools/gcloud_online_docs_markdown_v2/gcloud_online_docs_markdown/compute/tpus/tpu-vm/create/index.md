# gcloud compute tpus tpu-vm create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create)*

**NAME**

: **gcloud compute tpus tpu-vm create - create a new Cloud TPU VM node**

**SYNOPSIS**

: **`gcloud compute tpus tpu-vm create` (`[TPU](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#TPU)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--zone)`=`ZONE`) `[--version](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--version)`=`VERSION` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--async)`] [`[--data-disk](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--data-disk)`=[`mode`=`MODE`],[`source`=`SOURCE`]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--description)`=`DESCRIPTION`] [`[--internal-ips](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--internal-ips)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--metadata)`=[`KEY`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--metadata-from-file)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--network)`=`NETWORK`; default="default"] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--preemptible)`] [`[--queue-count](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--queue-count)`=`QUEUE_COUNT`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--range)`=`RANGE`] [`[--reserved](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--reserved)`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--scopes)`=[`SCOPES`,…]] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--shielded-secure-boot)`] [`[--spot](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--spot)`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--subnetwork)`=`SUBNETWORK`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--tags)`=[`TAGS`,…]] [`[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--accelerator-type)`=`ACCELERATOR_TYPE`; default="v2-8"     | `[--topology](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--topology)`=`TOPOLOGY` `[--type](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#--type)`=`TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Cloud TPU VM node.

**EXAMPLES**

: To create a TPU VM node with ID `my-tpu` in the default user project,
network and compute/zone (with other defaults supplied by API), run:

```
gcloud compute tpus tpu-vm create my-tpu
```

To create a TPU VM node in a specific network, run:

```
gcloud compute tpus tpu-vm create my-tpu --zone=us-central1-a --network=my-tf-network --description='My TPU VM' --version='v2-alpha'
```

To create a small TPU VM v2 pod, run:

```
gcloud compute tpus tpu-vm create my-tpu --zone=us-central1-a --accelerator-type='v2-32' --description='My TPU VM' --version='v2-alpha'
```

**POSITIONAL ARGUMENTS**

: **Tpu resource - Name of the Cloud TPU VM node to create. The arguments in this
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

**REQUIRED FLAGS**

: **--version**:
Runtime version for the TPU, such as `2.3`.
For a list of available versions run:
`[gcloud
compute tpus tpu-vm versions list](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/versions/list)`

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--data-disk**:
Additional data disks for the TPU VM.
This flag must be repeated to provide multiple data disks. For example:

```
gcloud compute tpus tpu-vm create --data-disk source=projects/my-project/zones/us-central1-c/disks/my-disk,mode=read-only
```

The following keys are allowed:

**`source`**:
Specifies the full path to an existing disk. Required. The disk must be in the
same zone.

**`mode`**:
Specifies the mode in which to attach this disk. Valid options are 'read-write',
'read-only'. If not specified, the default is 'read-write'.

**--description**:
Text description of the TPU.

**--internal-ips**:
Indicate that the IP addresses for the node should be internal. The default is
that external IP addresses will be associated with the TPU workers.

**--labels**:
Resource labels to represent user-provided metadata. See [https://cloud.google.com/compute/docs/labeling-resources](https://cloud.google.com/compute/docs/labeling-resources)
for details.

**--metadata**:
List of comma-separated metadata key-value pairs for the Cloud TPU VM node.
Example: `--metadata='key1=value1,key2=value2'`

**--metadata-from-file**:
Same as `--metadata` except the value for the entry will be read from
a local file. Example: `--metadata-from-file='key1=value1.txt'`

**--network**:
Network that this TPU will be a part of.

**--preemptible**:
If provided, the TPU will be preemptible and time-limited. It may be preempted
to free up resources for standard TPUs, and will only be able to run for a
limited amount of time.
Preemptible TPUs cannot be restarted.

**--queue-count**:
Specifies the networking queue count for TPU VM instances. Both Rx and Tx queues
will be set to this number. If it's not specified, a default queue count will be
assigned. For Virtio-net, each interface will get min(floor(#vCPU / #vNIC), 32)
queues. For gVNIC, each interface will get min(floor(#vCPU / #vNIC / 2), 16)
queues.

**--range**:
CIDR Range for the TPU.
The IP range that the TPU will select an IP address from. Must be in CIDR
notation and a `/29` range, for example `192.168.0.0/29`.
Errors will occur if the CIDR range has already been used for a currently
existing TPU, the CIDR range conflicts with any networks in the user's provided
network, or the provided network is peered with another network that is using
that CIDR range.

**--reserved**:
When specified, will attempt to create the TPU node under reservations made in
the current project. The reservations can be made separately but used in
aggregated form. i.e., the user can make a reservation of 128 V2 TPUs and later
on make another reservation of 128 V2 TPUs then creates a v2-256 TPU instance.
If there exists no reservation or not sufficient amount of reserved cores under
the project, the request will fail due to lack of capacity.

**--scopes**:
List of comma-separated scopes to be made available for the service account.

**--service-account**:
Email address of the service account. If empty, default Google Compute Engine
service account will be used.

**--shielded-secure-boot**:
Specifies that the TPU instances are created with secure boot enabled. This
implicitly makes them Shielded VM instances.

**--spot**:
If specified, create this VM as a spot VM. Spot VMs make unused capacity
available at highly discounted rates. Spot VMs may be preempted at any time if
the capacity is needed, but unless preempted there is no limit on runtime
duration. Spot VM TPUs cannot be restarted, and must be recreated again.

**--subnetwork**:
Subnetwork that this TPU will be a part of.

**--tags**:
Tags to apply to the TPU Node. Tags are used to identify valid sources or
targets for network firewalls. See [https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)
for more details.

**--accelerator-type**

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
gcloud alpha compute tpus tpu-vm create
```