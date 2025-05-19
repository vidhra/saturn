# gcloud compute tpus queued-resources create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create)*

**NAME**

: **gcloud compute tpus queued-resources create - create a Queued Resource**

**SYNOPSIS**

: **`gcloud compute tpus queued-resources create` (`[QUEUED_RESOURCE](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#QUEUED_RESOURCE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--zone)`=`ZONE`) `[--runtime-version](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--runtime-version)`=`RUNTIME_VERSION` (`[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--accelerator-type)`=`ACCELERATOR_TYPE`     | `[--topology](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--topology)`=`TOPOLOGY` `[--type](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--type)`=`TYPE`) (`[--node-id](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--node-id)`=`NODE_ID`     | [`[--node-count](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--node-count)`=`NODE_COUNT` : `[--node-prefix](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--node-prefix)`=`NODE_PREFIX`]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--async)`] [`[--data-disk](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--data-disk)`=[`mode`=`MODE`],[`source`=`SOURCE`]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--description)`=`DESCRIPTION`] [`[--guaranteed](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--guaranteed)`] [`[--internal-ips](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--internal-ips)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--metadata)`=[`KEY`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--metadata-from-file)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--network)`=`NETWORK`; default="default"] [`[--range](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--range)`=`RANGE`] [`[--reserved](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--reserved)`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--scopes)`=[`SCOPES`,…]] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--shielded-secure-boot)`] [`[--spot](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--spot)`] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--subnetwork)`=`SUBNETWORK`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--tags)`=[`TAGS`,…]] [`[--valid-after-duration](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--valid-after-duration)`=`VALID_AFTER_DURATION`] [`[--valid-after-time](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--valid-after-time)`=`VALID_AFTER_TIME`] [`[--valid-until-duration](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--valid-until-duration)`=`VALID_UNTIL_DURATION`] [`[--valid-until-time](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--valid-until-time)`=`VALID_UNTIL_TIME`] [`[--reservation-host-folder](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--reservation-host-folder)`=`RESERVATION_HOST_FOLDER` `[--reservation-host-organization](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--reservation-host-organization)`=`RESERVATION_HOST_ORGANIZATION` `[--reservation-host-project](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#--reservation-host-project)`=`RESERVATION_HOST_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Queued Resource with the specified attributes.

**EXAMPLES**

: To create a Queued Resource with ID `my-queued-resource` in zone
`us-central2-b` and project `my-project`, run:

```
gcloud compute tpus queued-resources create my-queued-resource --accelerator-type=v4-8 --runtime-version=v2-alpha-tpuv4 --node-id=my-node-001 --zone=us-central2-b --project=my-project
```

To create a Queued Resource with multiple nodes, run:

```
gcloud compute tpus queued-resources create my-queued-resource --accelerator-type=v4-8 --runtime-version=v2-alpha-tpuv4 --node-count=2 --zone=us-central2-b --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Queued resource resource - The Queued Resource you want to create. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `queued_resource` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`QUEUED_RESOURCE`**:
ID of the queued_resource or fully qualified identifier for the queued_resource.
To set the `queued_resource` attribute:

- provide the argument `queued_resource` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The compute/zone of the Cloud TPU.
If not specified, will use `default` compute/zone.
To set the `zone` attribute:

- provide the argument `queued_resource` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**REQUIRED FLAGS**

: **--runtime-version**:
Runtime version for the TPU, such as `tpu-ubuntu2204-base`.

**--accelerator-type**

**--node-id**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--data-disk**:
Additional data disks for the TPU VM.
This flag must be repeated to provide multiple data disks. For example:

```
gcloud compute tpus queued-resources create --data-disk source=projects/my-project/zones/us-central1-c/disks/my-disk,mode=read-only
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

**--guaranteed**:
If provided, the Node requested here will only be scheduled at the 'guaranteed'
tier.

**--internal-ips**:
Indicates that the IP addresses for the node should be internal. The default is
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

**--range**:
CIDR range for the TPU.
The IP range that the TPU will select an IP address from. Must be in CIDR
notation and a `/29` range, for example `192.168.0.0/29`.
Errors will occur if the CIDR range has already been used for a currently
existing TPU, the CIDR range conflicts with any networks in the user's provided
network, or the provided network is peered with another network that is using
that CIDR range.

**--reserved**:
Specifies the request should be scheduled on reserved capacity.
If `--reservation-host-project`,
`--reservation-host-folder`, or
`--reservation-host-organization` are present then this flag has no
effect.

**--scopes**:
List of comma-separated scopes to be made available for the service account.

**--service-account**:
Email address of the service account. If empty, default Google Compute Engine
service account will be used.

**--shielded-secure-boot**:
Specifies that the TPU instances are created with secure boot enabled. This
implicitly makes them Shielded VM instances.

**--spot**:
If provided, the Node requested here will be created as Spot VMs.

**--subnetwork**:
Subnetwork that this TPU will be a part of.

**--tags**:
Tags to apply to the TPU Node. Tags are used to identify valid sources or
targets for network firewalls. See [https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)
for more details.

**--valid-after-duration**:
A duration before which the TPU must not be provisioned, relative to the current
time. See $ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.

**--valid-after-time**:
An absolute time before which the TPU must not be provisioned. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--valid-until-duration**:
A duration after which the TPU must not be provisioned, relative to the current
time. See $ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.

**--valid-until-time**:
An absolute time after which resources must not be created. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--reservation-host-folder**:
The folder hosting the reservation that the TPU should use. Only one reservation
host entity may be specified.

**--reservation-host-organization**:
The organization hosting the reservation that the TPU should use. Only one
reservation host entity may be specified.

**--reservation-host-project**:
The project hosting the reservation that the TPU should use. Only one
reservation host entity may be specified.

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
gcloud alpha compute tpus queued-resources create
```