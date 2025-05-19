# gcloud alpha compute instances bulk create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create)*

**NAME**

: **gcloud alpha compute instances bulk create - create multiple Compute Engine virtual machines**

**SYNOPSIS**

: **`gcloud alpha compute instances bulk create` (`[--name-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--name-pattern)`=`NAME_PATTERN`     | `[--predefined-names](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--predefined-names)`=[`INSTANCE_NAME`,…]) (`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--zone)`=`ZONE`) [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--no-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--address)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--async)`] [`[--no-boot-disk-auto-delete](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-auto-delete)`] [`[--boot-disk-device-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-device-name)`=`BOOT_DISK_DEVICE_NAME`] [`[--boot-disk-interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-interface)`=`BOOT_DISK_INTERFACE`] [`[--boot-disk-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-provisioned-iops)`=`BOOT_DISK_PROVISIONED_IOPS`] [`[--boot-disk-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-provisioned-throughput)`=`BOOT_DISK_PROVISIONED_THROUGHPUT`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-size)`=`BOOT_DISK_SIZE`] [`[--boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-type)`=`BOOT_DISK_TYPE`] [`[--can-ip-forward](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--can-ip-forward)`] [`[--count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--count)`=`COUNT`] [`[--create-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--create-disk)`=[`PROPERTY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--description)`=`DESCRIPTION`] [`[--discard-local-ssds-at-termination-timestamp](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--discard-local-ssds-at-termination-timestamp)`=`DISCARD_LOCAL_SSDS_AT_TERMINATION_TIMESTAMP`] [`[--disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--disk)`=[`boot`=`BOOT`],[`device-name`=`DEVICE-NAME`],[`name`=`NAME`],[`scope`=`SCOPE`]] [`[--enable-display-device](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--enable-display-device)`] [`[--[no-]enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--[no-]enable-nested-virtualization)`] [`[--[no-]enable-uefi-networking](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--[no-]enable-uefi-networking)`] [`[--enable-watchdog-timer](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--enable-watchdog-timer)`] [`[--erase-windows-vss-signature](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--erase-windows-vss-signature)`] [`[--graceful-shutdown](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--graceful-shutdown)`] [`[--graceful-shutdown-max-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--graceful-shutdown-max-duration)`=`GRACEFUL_SHUTDOWN_MAX_DURATION`] [`[--host-error-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--host-error-timeout-seconds)`=`HOST_ERROR_TIMEOUT_SECONDS`] [`[--instance-termination-action](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--instance-termination-action)`=`INSTANCE_TERMINATION_ACTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--local-ssd)`=[`device-name`=`DEVICE-NAME`],[`interface`=`INTERFACE`],[`size`=`SIZE`]] [`[--local-ssd-recovery-timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--local-ssd-recovery-timeout)`=`LOCAL_SSD_RECOVERY_TIMEOUT`] [`[--location-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--location-policy)`=[`ZONE`=`POLICY`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--machine-type)`=`MACHINE_TYPE`] [`[--maintenance-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--maintenance-interval)`=`MAINTENANCE_INTERVAL`] [`[--max-count-per-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--max-count-per-zone)`=[`ZONE`=`MAX_COUNT_PER_ZONE`,…]] [`[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--max-run-duration)`=`MAX_RUN_DURATION`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[--min-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--min-count)`=`MIN_COUNT`] [`[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--min-cpu-platform)`=`PLATFORM`] [`[--min-node-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--min-node-cpu)`=`MIN_NODE_CPU`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--network)`=`NETWORK`] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--network-interface)`=[`PROPERTY`=`VALUE`,…]] [`[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--network-performance-configs)`=[`PROPERTY`=`VALUE`,…]] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--network-tier)`=`NETWORK_TIER`] [`[--numa-node-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--numa-node-count)`=`NUMA_NODE_COUNT`] [`[--per-instance-hostnames](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--per-instance-hostnames)`=[`INSTANCE_NAME`=`INSTANCE_HOSTNAME`,…]] [`[--performance-monitoring-unit](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--performance-monitoring-unit)`=`PERFORMANCE_MONITORING_UNIT`] [`[--post-key-revocation-action-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--post-key-revocation-action-type)`=`POLICY`] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--preemptible)`] [`[--provisioning-model](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--provisioning-model)`=`PROVISIONING_MODEL`] [`[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--resource-policies)`=[`RESOURCE_POLICY`,…]] [`[--no-restart-on-failure](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--restart-on-failure)`] [`[--secure-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--secure-tags)`=`SECURE_TAG`,[`[SECURE_TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#SECURE_TAG)`,…]] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--shielded-vtpm)`] [`[--source-instance-template](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--source-instance-template)`=`SOURCE_INSTANCE_TEMPLATE`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--stack-type)`=`STACK_TYPE`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--subnet)`=`SUBNET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#TAG)`,…]] [`[--target-distribution-shape](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--target-distribution-shape)`=`SHAPE`] [`[--termination-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--termination-time)`=`TERMINATION_TIME`] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--threads-per-core)`=`THREADS_PER_CORE`] [`[--turbo-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--turbo-mode)`=`TURBO_MODE`] [`[--visible-core-count](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--visible-core-count)`=`VISIBLE_CORE_COUNT`] [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY` : `[--boot-disk-kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-kms-keyring)`=`BOOT_DISK_KMS_KEYRING` `[--boot-disk-kms-location](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-kms-location)`=`BOOT_DISK_KMS_LOCATION` `[--boot-disk-kms-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--boot-disk-kms-project)`=`BOOT_DISK_KMS_PROJECT`] [`[--confidential-compute](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--confidential-compute)`     | `[--confidential-compute-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--confidential-compute-type)`=`CONFIDENTIAL_COMPUTE_TYPE`] [`[--custom-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--custom-cpu)`=`CUSTOM_CPU` `[--custom-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--custom-memory)`=`CUSTOM_MEMORY` : `[--custom-extensions](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--custom-extensions)` `[--custom-vm-type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--custom-vm-type)`=`CUSTOM_VM_TYPE`] [`[--image-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--image-project)`=`IMAGE_PROJECT` `[--image](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--image)`=`IMAGE`     | `[--image-family](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--image-family)`=`IMAGE_FAMILY`     | `[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--source-snapshot)`=`SOURCE_SNAPSHOT`] [`[--maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--maintenance-policy)`=`MAINTENANCE_POLICY`     | `[--on-host-maintenance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--on-host-maintenance)`=`MAINTENANCE_POLICY`] [`[--public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--public-dns)`     | `[--no-public-dns](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--public-dns)`] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--reservation-affinity)`=`RESERVATION_AFFINITY`; default="any"] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--scopes)`=[`SCOPE`,…]     | `[--no-scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--scopes)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--service-account)`=`SERVICE_ACCOUNT`     | `[--no-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#--service-account)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/bulk/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instances bulk create`
facilitates the creation of multiple Compute Engine virtual machines with a
single command. They offer a number of advantages compared to the single
instance creation command. This includes the ability to automatically pick a
zone in which to create instances based on resource availability, the ability to
specify that the request be atomic or best-effort, and a faster rate of instance
creation.

**EXAMPLES**

: To create instances called 'example-instance-1', 'example-instance-2', and
'example-instance-3' in the 'us-central1-a' zone, run:

```
gcloud alpha compute instances bulk create --predefined-names=example-instance-1,example-instance-2,example-instance-3 --zone=us-central1-a
```

**REQUIRED FLAGS**

: **--name-pattern**

**--region**

**OPTIONAL FLAGS**

: **--accelerator**:
Attaches accelerators (e.g. GPUs) to the instances.

**`type`**:
The specific type (e.g. nvidia-tesla-t4 for NVIDIA T4) of accelerator to attach
to the instances. Use 'gcloud compute accelerator-types list' to learn about all
available accelerator types.

**`count`**:
Number of accelerators to attach to each instance. The default value is 1.

**--no-address**:
If provided, the instances are not assigned external IP addresses. To pull
container images, you must configure private Google access if using Container
Registry or configure Cloud NAT for instances to access container images
directly. For more information, see:

- [https://cloud.google.com/vpc/docs/configure-private-google-access](https://cloud.google.com/vpc/docs/configure-private-google-access)
- [https://cloud.google.com/nat/docs/using-nat](https://cloud.google.com/nat/docs/using-nat)

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--boot-disk-auto-delete**:
Automatically delete boot disks when their instances are deleted. Enabled by
default, use `--no-boot-disk-auto-delete` to disable.

**--boot-disk-device-name**:
The name the guest operating system will see for the boot disk. This option can
only be specified if a new boot disk is being created (as opposed to mounting an
existing persistent disk).

**--boot-disk-interface**:
Indicates the interface to use for the boot disk. The value must be one of the
following:

- SCSI
- NVME

**--boot-disk-provisioned-iops**:
Indicates how many IOPS to provision for the disk. This sets the number of I/O
operations per second that the disk can handle. Value must be between 10,000 and
120,000.

**--boot-disk-provisioned-throughput**:
Indicates how much throughput to provision for the disk. This sets the number of
throughput mb per second that the disk can handle.

**--boot-disk-size**:
The size of the boot disk. This option can only be specified if a new boot disk
is being created (as opposed to mounting an existing persistent disk). The value
must be a whole number followed by a size unit of
``KB`` for kilobyte,
``MB`` for megabyte,
``GB`` for gigabyte, or
``TB`` for terabyte. For example,
``10GB`` will produce a 10 gigabyte disk. Disk
size must be a multiple of 1 GB. Default size unit is
``GB``.

**--boot-disk-type**:
The type of the boot disk. This option can only be specified if a new boot disk
is being created (as opposed to mounting an existing persistent disk). To get a
list of available disk types, run `$ [gcloud compute disk-types
list](https://cloud.google.com/sdk/gcloud/reference/compute/disk-types/list)`.

**--can-ip-forward**:
If provided, allows the instances to send and receive packets with non-matching
destination or source IP addresses.

**--count**:
Number of Compute Engine virtual machines to create. If specified, and
`--predefined-names` is specified, count must equal the amount of
names provided to `--predefined-names`. If not specified, the number
of virtual machines created will equal the number of names provided to
`--predefined-names`.

**--create-disk**:
Creates and attaches persistent disks to the instances.

**`name`**:
Specifies the name of the disk. This option cannot be specified if more than one
instance is being created.

**`description`**:
Optional textual description for the disk being created.

**`mode`**:
Specifies the mode of the disk. Supported options are
``ro`` for read-only and
``rw`` for read-write. If omitted,
``rw`` is used as a default.

**`image`**:
Specifies the name of the image that the disk will be initialized with. A new
disk will be created based on the given image. To view a list of public images
and projects, run `$ [gcloud compute images
list](https://cloud.google.com/sdk/gcloud/reference/compute/images/list)`. It is best practice to use image when a specific version of an
image is needed. If both image and image-family flags are omitted a blank disk
will be created.

**`image-family`**:
The image family for the operating system that the boot disk will be initialized
with. Compute Engine offers multiple Linux distributions, some of which are
available as both regular and Shielded VM images. When a family is specified
instead of an image, the latest non-deprecated image associated with that family
is used. It is best practice to use --image-family when the latest version of an
image is needed.

**`image-project`**:
The Google Cloud project against which all image and image family references
will be resolved. It is best practice to define image-project. A full list of
available image projects can be generated by running `[gcloud compute images
list](https://cloud.google.com/sdk/gcloud/reference/compute/images/list)`.

- If specifying one of our public images, image-project must be provided.
- If there are several of the same image-family value in multiple projects,
image-project must be specified to clarify the image to be used.
- If not specified and either image or image-family is provided, the current
default project is used.

**`size`**:
The size of the disk. The value must be a whole number followed by a size unit
of ``KB`` for kilobyte,
``MB`` for megabyte,
``GB`` for gigabyte, or
``TB`` for terabyte. For example,
``10GB`` will produce a 10 gigabyte disk. Disk
size must be a multiple of 1 GB. If not specified, the default image size will
be used for the new disk.

**`type`**:
The type of the disk. To get a list of available disk types, run $ [gcloud compute disk-types
list](https://cloud.google.com/sdk/gcloud/reference/compute/disk-types/list). The default disk type is
``pd-standard``.

**`device-name`**:
An optional name to display the disk name in the guest operating system. If
omitted, a device name of the form `persistent-disk-N` is used.

**`provisioned-iops`**:
Indicates how many IOPS to provision for the disk. This sets the number of I/O
operations per second that the disk can handle. Value must be between 10,000 and
120,000.

**`provisioned-throughput`**:
Indicates how much throughput to provision for the disk. This sets the number of
throughput mb per second that the disk can handle.

**`disk-resource-policy`**:
Resource policy to apply to the disk. Specify a full or partial URL. For
example:

- ``https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/resourcePolicies/my-resource-policy``
- ``projects/my-project/regions/us-central1/resourcePolicies/my-resource-policy``

For more information, see the following docs:

- [https://cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/](https://cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/)
- [https://cloud.google.com/compute/docs/disks/scheduled-snapshots](https://cloud.google.com/compute/docs/disks/scheduled-snapshots)

**`auto-delete`**:
If ``yes``, this persistent disk will be
automatically deleted when the instance is deleted. However, if the disk is
later detached from the instance, this option won't apply. The default value for
this is ``yes``.

**`architecture`**:
Specifies the architecture or processor type that this disk can support. For
available processor types on Compute Engine, see [https://cloud.google.com/compute/docs/cpu-platforms](https://cloud.google.com/compute/docs/cpu-platforms).

**`storage-pool`**:
The name of the storage pool in which the new disk is created. The new disk and
the storage pool must be in the same location.

**`interface`**:
The interface to use with the disk. The value must be one of the following:

- SCSI
- NVME

**`boot`**:
If ``yes``, indicates that this is a boot disk.
The instance will use the first partition of the disk for its root file system.
The default value for this is ``no``.

**`kms-key`**:
Fully qualified Cloud KMS cryptokey name that will protect the disk.
This can either be the fully qualified path or the name.
The fully qualified Cloud KMS cryptokey name format is:
``projects/<kms-project>/locations/<kms-location>/keyRings/<kms-keyring>/
cryptoKeys/<key-name>``.
If the value is not fully qualified then kms-location, kms-keyring, and
optionally kms-project are required.
See [https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)
for more details.

**`kms-project`**:
Project that contains the Cloud KMS cryptokey that will protect the disk.
If the project is not specified then the project where the disk is being created
will be used.
If this flag is set then key-location, kms-keyring, and kms-key are required.
See [https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)
for more details.

**`kms-location`**:
Location of the Cloud KMS cryptokey to be used for protecting the disk.
All Cloud KMS cryptokeys are reside in a 'location'. To get a list of possible
locations run 'gcloud kms locations list'. If this flag is set then kms-keyring
and kms-key are required. See [https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)
for more details.

**`kms-keyring`**:
The keyring which contains the Cloud KMS cryptokey that will protect the disk.
If this flag is set then kms-location and kms-key are required.
See [https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)
for more details.

**`source-snapshot`**:
The source disk snapshot that will be used to create the disk. You can provide
this as a full URL to the snapshot or just the snapshot name. For example, the
following are valid values:

- [https://compute.googleapis.com/compute/v1/projects/myproject/global/snapshots/snapshot](https://compute.googleapis.com/compute/v1/projects/myproject/global/snapshots/snapshot)
- snapshot

**`image-csek-required`**:
Specifies the name of the CSK protected image that the disk will be initialized
with. A new disk will be created based on the given image. To view a list of
public images and projects, run `$ [gcloud compute images
list](https://cloud.google.com/sdk/gcloud/reference/compute/images/list)`. It is best practice to use image when a specific version of an
image is needed. If both image and image-family flags are omitted a blank disk
will be created. Must be specified with `image-csek-key-file`.

**`image-csek-key-file`**:
Path to a Customer-Supplied Encryption Key (CSEK) key file for the image. Must
be specified with `image-csek-required`.

**`replica-zones`**:
Required for each regional disk associated with the instance. Specify the URLs
of the zones where the disk should be replicated to. You must provide exactly
two replica zones, and one zone must be the same as the instance zone.

**--description**:
Specifies a textual description of the instances.

**--discard-local-ssds-at-termination-timestamp**:
Required to be set to `true` and only allowed for VMs that have one
or more local SSDs, use --instance-termination-action=STOP, and use either
--max-run-duration or --termination-time.
This flag indicates the value that you want Compute Engine to use for the
`--discard-local-ssd` flag in the automatic `[gcloud compute instances
stop](https://cloud.google.com/sdk/gcloud/reference/compute/instances/stop)` command. This flag only supports the `true` value,
which discards local SSD data when automatically stopping this VM during its
`terminationTimestamp`.
For more information about the `--discard-local-ssd` flag, see [https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance](https://cloud.google.com/compute/docs/disks/local-ssd#stop_instance).

**--disk**:
Attaches persistent disks to the instances. The disks specified must already
exist.

**`name`**:
The disk to attach to the instances.

**`boot`**:
If ``yes``, indicates that this is a boot disk.
The virtual machines will use the first partition of the disk for their root
file systems. The default value for this is
``no``.

**`device-name`**:
An optional name to display the disk name in the guest operating system. If
omitted, a device name of the form `persistent-disk-N` is used.

**`scope`**:
Can be `zonal` or `regional`. If
``zonal``, the disk is interpreted as a zonal
disk in the same zone as the instance (default). If
``regional``, the disk is interpreted as a
regional disk in the same region as the instance. The default value for this is
``zonal``.

**--enable-display-device**:
Enable a display device on VM instances. Disabled by default.

**--[no-]enable-nested-virtualization**:
If set to true, enables nested virtualization for the instance. Use
`--enable-nested-virtualization` to enable and
`--no-enable-nested-virtualization` to disable.

**--[no-]enable-uefi-networking**:
If set to true, enables UEFI networking for the instance creation. Use
`--enable-uefi-networking` to enable and
`--no-enable-uefi-networking` to disable.

**--enable-watchdog-timer**:
Enable a watchdog timer device on VM instances. Disabled by default.

**--erase-windows-vss-signature**:
Specifies whether the disk restored from source snapshots or source machine
image should erase Windows specific VSS signature. See [https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--guest-flush)

**--graceful-shutdown**:
Enables graceful shutdown for the instance.

**--graceful-shutdown-max-duration**:
Specifies the maximum time for the graceful shutdown. After this time, the
instance is set to STOPPING even if tasks are still running. Specify the time as
the number of hours, minutes, or seconds followed by h, m, and s respectively.
For example, specify 30m for 30 minutes or 20m10s for 20 minutes and 10 seconds.
The value must be between 1 second and 1 hour.

**--host-error-timeout-seconds**:
The timeout in seconds for host error detection. The value must be set with 30
second increments, with a range of 90 to 330 seconds. If unset, the default
behavior of the host error recovery is used.

**--instance-termination-action**:
Specifies the termination action that will be taken upon VM preemption
(--provisioning-model=SPOT) or automatic instance termination
(--max-run-duration or --termination-time).
`INSTANCE_TERMINATION_ACTION` must be one of:

**`DELETE`**:
Permanently delete the VM.

**`STOP`**:
Default only for Spot VMs. Stop the VM without preserving memory. The VM can be
restarted later.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--local-ssd**:
Attaches a local SSD to the instances.

**`device-name`**:
Optional. A name that indicates the disk name the guest operating system will
see. Can only be specified if `interface` is `SCSI`. If
omitted, a device name of the form
``local-ssd-N`` will be used.

**`interface`**:
Optional. The kind of disk interface exposed to the VM for this SSD. Valid
values are ``SCSI`` and
``NVME``. SCSI is the default and is supported
by more guest operating systems. NVME might provide higher performance.

**`size`**:
Optional. The only valid value is ``375GB``.
Specify the ``--local-ssd`` flag multiple times
if you need multiple ``375GB`` local SSD
partitions. You can specify a maximum of 24 local SSDs for a maximum of
``9TB`` attached to an instance.

**--local-ssd-recovery-timeout**:
Specifies the maximum amount of time a Local Ssd Vm should wait while recovery
of the Local Ssd state is attempted. Its value should be in between 0 and 168
hours with hour granularity and the default value being 1 hour.

**--location-policy**:
Policy for which zones to include or exclude during bulk instance creation
within a region. Policy is defined as a list of key-value pairs, with the key
being the zone name, and value being the applied policy. Available policies are
`allow` and `deny`. Default for zones if left unspecified
is `allow`.
Example:

```
gcloud compute instances bulk create --name-pattern=example-###
  --count=5 --region=us-east1
  --location-policy=us-east1-b=allow,us-east1-c=deny
```

**--machine-type**:
Specifies the machine type used for the instances. To get a list of available
machine types, run 'gcloud compute machine-types list'. If unspecified, the
default type is n1-standard-1.

**--maintenance-interval**:
Specifies how infrastructure upgrades should be applied to the VM.
`MAINTENANCE_INTERVAL` must be one of:

**`PERIODIC`**:
VMs receive infrastructure and hypervisor updates on a periodic basis,
minimizing the number of maintenance operations (live migrations or
terminations) on an individual VM. Security updates will still be applied as
soon as they are available.

**`RECURRENT`**:
VMs receive infrastructure and hypervisor updates on a periodic basis,
minimizing the number of maintenance operations (live migrations or
terminations) on an individual VM. This may mean a VM will take longer to
receive an update than if it was configured for AS_NEEDED. Security updates will
still be applied as soonas they are available. RECURRENT is used for GEN3 and
Sliceof Hardware VMs.

**--max-count-per-zone**:
Maximum number of instances per zone specified as key-value pairs. The zone name
is the key and the max count per zone is the value in that zone.
Example:

```
gcloud compute instances bulk create --name-pattern=example-###
  --count=5 --region=us-east1
  --max-count-per-zone=us-east1-b=2,us-east-1-c=1
```

**--max-run-duration**:
Limits how long this VM instance can run, specified as a duration relative to
the last time when the VM began running. Format the duration, MAX_RUN_DURATION,
as the number of days, hours, minutes, and seconds followed by d, h, m, and s
respectively. For example, specify `30m` for a duration of 30 minutes
or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes,
and 4 seconds. Alternatively, to specify a timestamp, use --termination-time
instead.
If neither --max-run-duration nor --termination-time is specified (default), the
VM instance runs until prompted by a user action or system event. If either is
specified, the VM instance is scheduled to be automatically terminated at the
VM's termination timestamp (`terminationTimestamp`) using the action
specified by --instance-termination-action.
Note: The `terminationTimestamp` is removed whenever the VM is
stopped or suspended and redefined whenever the VM is rerun. For
--max-run-duration specifically, the `terminationTimestamp` is the
sum of MAX_RUN_DURATION and the time when the VM last entered the
`RUNNING` state, which changes whenever the VM is rerun.

**--metadata**:
Metadata to be made available to the guest operating system running on the
instances. Each metadata entry is a key/value pair separated by an equals sign.
Each metadata key must be unique and have a max of 128 bytes in length. Each
value must have a max of 256 KB in length. Multiple arguments can be passed to
this flag, e.g., ``--metadata
key-1=value-1,key-2=value-2,key-3=value-3``. The combined
total size for all metadata entries is 512 KB.
In images that have Compute Engine tools installed on them, such as the [official images](https://cloud.google.com/compute/docs/images), the
following metadata keys have special meanings:

**`startup-script`**:
Specifies a script that will be executed by the instances once they start
running. For convenience,
``--metadata-from-file`` can be used to pull
the value from a file.

**`startup-script-url`**:
Same as ``startup-script`` except that the
script contents are pulled from a publicly-accessible location on the web.
For startup scripts on Windows instances, the following metadata keys have
special meanings:
``windows-startup-script-url``,
``windows-startup-script-cmd``,
``windows-startup-script-bat``,
``windows-startup-script-ps1``,
``sysprep-specialize-script-url``,
``sysprep-specialize-script-cmd``,
``sysprep-specialize-script-bat``, and
``sysprep-specialize-script-ps1``. For more
information, see [Running startup
scripts](https://cloud.google.com/compute/docs/startupscript).

**--metadata-from-file**:
Same as ``--metadata`` except that the value
for the entry will be read from a local file. This is useful for values that are
too large such as ``startup-script`` contents.

**--min-count**:
The minimum number of Compute Engine virtual machines that must be successfully
created for the operation to be considered a success. If the operation
successfully creates as many virtual machines as specified here they will be
persisted, otherwise the operation rolls back and deletes all created virtual
machines. If not specified, this value is equal to `--count`.

**--min-cpu-platform**:
When specified, the VM will be scheduled on host with specified CPU architecture
or a newer one. To list available CPU platforms in given zone, run:

```
gcloud alpha compute zones describe ZONE --format="value(availableCpuPlatforms)"
```

Default setting is "AUTOMATIC".
CPU platform selection is available only in selected zones.
You can find more information on-line: [https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)

**--min-node-cpu**:
Minimum number of virtual CPUs this instance will consume when running on a
sole-tenant node.

**--network**:
Specifies the network that the VM instances are a part of. If
`--subnet` is also specified, subnet must be a subnetwork of the
network specified by this `--network` flag. If neither is specified,
the default network is used.

**--network-interface**:
Adds a network interface to the instance. Mutually exclusive with any of these
flags: `--network`, `--network-tier`,
`--no-address`, `--subnet`, `--stack-type`.
This flag can be repeated to specify multiple network interfaces.

**`network`**:
Specifies the network that the interface will be part of. If subnet is also
specified it must be subnetwork of this network. If neither is specified, this
defaults to the "default" network.

**`network-tier`**:
Specifies the network tier of the interface.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

**`subnet`**:
Specifies the subnet that the interface will be part of. If network key is also
specified this must be a subnetwork of the specified network.

**`nic-type`**:
Specifies the Network Interface Controller (NIC) type for the interface.
``NIC_TYPE`` must be one of:
`GVNIC`, `VIRTIO_NET`.

**`no-address`**:
If specified the interface will have no external IP. If not specified instances
will get ephemeral IPs.

**`queue-count`**:
Specifies the networking queue count for this interface. Both Rx and Tx queues
will be set to this number. If it's not specified, a default queue count will be
assigned. See [https://cloud.google.com/compute/docs/network-bandwidth#rx-tx](https://cloud.google.com/compute/docs/network-bandwidth#rx-tx)
for more details.

**`stack-type`**:
Specifies whether IPv6 is enabled on the interface.
``STACK_TYPE`` must be one of:
`IPV4_ONLY`, `IPV4_IPV6`, `IPV6_ONLY`. The
default value is `IPV4_ONLY`.

**`igmp-query`**:
Determines if the Compute Engine Instance can receive and respond to IGMP query
packets on the specified network interface.
``IGMP_QUERY`` must be one of:
`IGMP_QUERY_V2`, `IGMP_QUERY_DISABLED`. It is disabled by
default.

**--network-performance-configs**:
Configures network performance settings for the instance. If this flag is not
specified, the instance will be created with its default network performance
configuration.

**`total-egress-bandwidth-tier`**:
Total egress bandwidth is the available outbound bandwidth from a VM, regardless
of whether the traffic is going to internal IP or external IP destinations. The
following tier values are allowed: [DEFAULT,TIER_1]

**--network-tier**:
Specifies the network tier that will be used to configure the instance.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

**--numa-node-count**:
The number of virtual NUMA nodes for the instance. Valid values are: 0, 1, 2, 4
or 8. Setting NUMA node count to 0 means using the default setting.

**--per-instance-hostnames**:
Specify the hostname of the instance to be created. The specified hostname must
be RFC1035 compliant. If hostname is not specified, the default hostname is
[INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and
[INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS.

**--performance-monitoring-unit**:
The type of performance monitoring counters (PMCs) to enable in the instance.
`PERFORMANCE_MONITORING_UNIT` must be one of:

**`architectural`**:
This enables architecturally defined non-last level cache (LLC) events.

**`enhanced`**:
This enables most documented core/L2 and LLC events.

**`standard`**:
This enables most documented core/L2 events.

**--post-key-revocation-action-type**:
Specifies the behavior of the instance when the KMS key of one of its attached
disks is revoked. The default is noop. `POLICY` must be
one of:

**`noop`**:
No operation is performed.

**`shutdown`**:
The instance is shut down when the KMS key of one of its attached disks is
revoked.

**--preemptible**:
If provided, instances will be preemptible and time-limited. Instances might be
preempted to free up resources for standard VM instances, and will only be able
to run for a limited amount of time. Preemptible instances can not be restarted
and will not migrate.

**--provisioning-model**:
Specifies the provisioning model for your VM instances. This choice affects the
price, availability, and how long your VM instances can run.
`PROVISIONING_MODEL` must be one of:

**`RESERVATION_BOUND`**:
The VM instances run for the entire duration of their associated reservation.
You can only specify this provisioning model if you want your VM instances to
consume a specific reservation with either a calendar reservation mode or a
dense deployment type.

**`SPOT`**:
Compute Engine may stop a Spot VM instance whenever it needs capacity. Because
Spot VM instances don't have a guaranteed runtime, they come at a discounted
price.

**`STANDARD`**:
The default option. The STANDARD provisioning model gives you full control over
your VM instances' runtime.

**--resource-manager-tags**:
Specifies a list of resource manager tags to apply to the instance.

**--resource-policies**:
A list of resource policy names to be added to the instance. The policies must
exist in the same region as the instance.

**--restart-on-failure**:
The instances will be restarted if they are terminated by Compute Engine. This
does not affect terminations performed by the user. Enabled by default, use
`--no-restart-on-failure` to disable.

**--secure-tags**:
Specifies a list of secure tags to apply to the instance. These tags allow
network firewall rules and routes to be applied to specified VM instances. See
`[gcloud
compute network firewall-policies rules create](https://cloud.google.com/sdk/gcloud/reference/compute/network/firewall-policies/rules/create)`(1) for more details.

**--shielded-integrity-monitoring**:
Enables monitoring and attestation of the boot integrity of the instance. The
attestation is performed against the integrity policy baseline. This baseline is
initially derived from the implicitly trusted boot image when the instance is
created. This baseline can be updated by using `gcloud compute instances
update --shielded-learn-integrity-policy`. On Shielded VM instances,
integrity monitoring is enabled by default. For information about how to modify
Shielded VM options, see [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).
For information about monitoring integrity on Shielded VM instances, see
https://cloud.google.com/compute/docs/instances/integrity-monitoring."

**--shielded-secure-boot**:
The instance boots with secure boot enabled. On Shielded VM instances, Secure
Boot is not enabled by default. For information about how to modify Shielded VM
options, see [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).

**--shielded-vtpm**:
The instance boots with the TPM (Trusted Platform Module) enabled. A TPM is a
hardware module that can be used for different security operations such as
remote attestation, encryption, and sealing of keys. On Shielded VM instances,
vTPM is enabled by default. For information about how to modify Shielded VM
options, see [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).

**--source-instance-template**:
The name of the instance template that the instance will be created from. Users
can override fields by specifying other flags.

**--stack-type**:
Specifies whether IPv6 is enabled on the default network interface. If not
specified, IPV4_ONLY will be used. `STACK_TYPE` must be
one of:

**`IPV4_IPV6`**:
The network interface can have both IPv4 and IPv6 addresses

**`IPV4_ONLY`**:
The network interface will be assigned IPv4 addresses

**`IPV6_ONLY`**:
The network interface will be assigned IPv6 addresses

**--subnet**:
Specifies the subnet that the VM instances are a part of. If
`--network` is also specified, subnet must be a subnetwork of the
network specified by the `--network` flag.

**--tags**:
Specifies a list of tags to apply to the instance. These tags allow network
firewall rules and routes to be applied to specified VM instances. See `[gcloud compute
firewall-rules create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)`(1) for more details.
To read more about configuring network tags, read this guide: [https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)
To list instances with their respective status and tags, run:

```
gcloud compute instances list --format='table(name,status,tags.list())'
```

To list instances tagged with a specific tag, `tag1`, run:

```
gcloud compute instances list --filter='tags:tag1'
```

**--target-distribution-shape**:
Specifies whether and how to distribute VMs across multiple zones in a region or
to enforce placement of VMs in a single zone. The default shape is
`ANY_SINGLE_ZONE`. `SHAPE` must be one of:

**`ANY`**:
Allows creating VMs in multiple zones if one zone cannot accommodate all the
requested VMs. The resulting distribution shapes can vary.

**`ANY_SINGLE_ZONE`**:
Enforces VM placement in one allowed zone. Use this to avoid cross-zone network
egress or to reduce network latency. This is the default value.

**`BALANCED`**:
Allows distribution of VMs in zones where resources are available while
distributing VMs as evenly as possible across selected zones to minimize the
impact of zonal failures. Recommended for highly available serving or batch
workloads.

**--termination-time**:
Limits how long this VM instance can run, specified as a time. Format the time,
TERMINATION_TIME, as a RFC 3339 timestamp. For more information, see [https://tools.ietf.org/html/rfc3339](https://tools.ietf.org/html/rfc3339).
Alternatively, to specify a duration, use --max-run-duration instead.
If neither --termination-time nor --max-run-duration is specified (default), the
VM instance runs until prompted by a user action or system event. If either is
specified, the VM instance is scheduled to be automatically terminated at the
VM's termination timestamp (`terminationTimestamp`) using the action
specified by --instance-termination-action.
Note: The `terminationTimestamp` is removed whenever the VM is
stopped or suspended and redefined whenever the VM is rerun. For
--termination-time specifically, the `terminationTimestamp` remains
the same whenever the VM is rerun, but any requests to rerun the VM fail if the
specified timestamp is in the past.

**--threads-per-core**:
The number of visible threads per physical core. To disable simultaneous
multithreading (SMT) set this to 1. Valid values are: 1 or 2.
For more information about configuring SMT, see: [https://cloud.google.com/compute/docs/instances/configuring-simultaneous-multithreading](https://cloud.google.com/compute/docs/instances/configuring-simultaneous-multithreading).

**--turbo-mode**:
Turbo mode to use for the instance. Supported modes include:

- ALL_CORE_MAX

To achieve all-core-turbo frequency for more consistent CPU performance, set the
field to ALL_CORE_MAX. The field is unset by default, which results in maximum
performance single-core boosting.

**--visible-core-count**:
The number of physical cores to expose to the instance's guest operating system.
The number of virtual CPUs visible to the instance's guest operating system is
this number of cores multiplied by the instance's count of visible threads per
physical core.

**--boot-disk-kms-key**

**--confidential-compute**

**--custom-cpu**

**--image-project**:
The Google Cloud project against which all image and image family references
will be resolved. It is best practice to define image-project. A full list of
available projects can be generated by running `[gcloud projects list](https://cloud.google.com/sdk/gcloud/reference/projects/list)`.

- If specifying one of our public images, image-project must be provided.
- If there are several of the same image-family value in multiple projects,
image-project must be specified to clarify the image to be used.
- If not specified and either image or image-family is provided, the current
default project is used.

**--image**

**--maintenance-policy**

**--public-dns**

**--reservation**

**--scopes**

**--service-account**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instances bulk create
```

```
gcloud beta compute instances bulk create
```