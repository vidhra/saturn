# gcloud compute instance-templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create)*

**NAME**

: **gcloud compute instance-templates create - create a Compute Engine virtual machine instance template**

**SYNOPSIS**

: **`gcloud compute instance-templates create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#NAME)` [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--no-boot-disk-auto-delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-auto-delete)`] [`[--boot-disk-device-name](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-device-name)`=`BOOT_DISK_DEVICE_NAME`] [`[--boot-disk-interface](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-interface)`=`BOOT_DISK_INTERFACE`] [`[--boot-disk-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-provisioned-iops)`=`BOOT_DISK_PROVISIONED_IOPS`] [`[--boot-disk-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-provisioned-throughput)`=`BOOT_DISK_PROVISIONED_THROUGHPUT`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-size)`=`BOOT_DISK_SIZE`] [`[--boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-type)`=`BOOT_DISK_TYPE`] [`[--can-ip-forward](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--can-ip-forward)`] [`[--configure-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--configure-disk)`=[`PROPERTY`=`VALUE`,…]] [`[--create-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--create-disk)`=[`PROPERTY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--description)`=`DESCRIPTION`] [`[--discard-local-ssds-at-termination-timestamp](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--discard-local-ssds-at-termination-timestamp)`=`DISCARD_LOCAL_SSDS_AT_TERMINATION_TIMESTAMP`] [`[--disk](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--disk)`=[`auto-delete`=`AUTO-DELETE`],[`boot`=`BOOT`],[`device-name`=`DEVICE-NAME`],[`interface`=`INTERFACE`],[`mode`=`MODE`],[`name`=`NAME`]] [`[--[no-]enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--[no-]enable-nested-virtualization)`] [`[--[no-]enable-uefi-networking](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--[no-]enable-uefi-networking)`] [`[--external-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--external-ipv6-address)`=`EXTERNAL_IPV6_ADDRESS`] [`[--external-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--external-ipv6-prefix-length)`=`EXTERNAL_IPV6_PREFIX_LENGTH`] [`[--host-error-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--host-error-timeout-seconds)`=`HOST_ERROR_TIMEOUT_SECONDS`] [`[--instance-template-region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--instance-template-region)`=`INSTANCE_TEMPLATE_REGION`] [`[--instance-termination-action](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--instance-termination-action)`=`INSTANCE_TERMINATION_ACTION`] [`[--internal-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--internal-ipv6-address)`=`INTERNAL_IPV6_ADDRESS`] [`[--internal-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--internal-ipv6-prefix-length)`=`INTERNAL_IPV6_PREFIX_LENGTH`] [`[--ipv6-network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--ipv6-network-tier)`=`IPV6_NETWORK_TIER`] [`[--key-revocation-action-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--key-revocation-action-type)`=`POLICY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--local-ssd](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--local-ssd)`=[`device-name`=`DEVICE-NAME`],[`interface`=`INTERFACE`],[`size`=`SIZE`]] [`[--local-ssd-recovery-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--local-ssd-recovery-timeout)`=`LOCAL_SSD_RECOVERY_TIMEOUT`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--machine-type)`=`MACHINE_TYPE`] [`[--maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--maintenance-policy)`=`MAINTENANCE_POLICY`] [`[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--max-run-duration)`=`MAX_RUN_DURATION`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--min-cpu-platform)`=`PLATFORM`] [`[--min-node-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--min-node-cpu)`=`MIN_NODE_CPU`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--network)`=`NETWORK`] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--network-interface)`=[`PROPERTY`=`VALUE`,…]] [`[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--network-performance-configs)`=[`PROPERTY`=`VALUE`,…]] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--network-tier)`=`NETWORK_TIER`] [`[--performance-monitoring-unit](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--performance-monitoring-unit)`=`PERFORMANCE_MONITORING_UNIT`] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--preemptible)`] [`[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`] [`[--private-network-ip](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--private-network-ip)`=`PRIVATE_NETWORK_IP`] [`[--provisioning-model](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--provisioning-model)`=`PROVISIONING_MODEL`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--region)`=`REGION`] [`[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--resource-policies)`=[`RESOURCE_POLICY`,…]] [`[--no-restart-on-failure](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--restart-on-failure)`] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--shielded-vtpm)`] [`[--source-instance](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--source-instance)`=`SOURCE_INSTANCE`] [`[--source-instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--source-instance-zone)`=`SOURCE_INSTANCE_ZONE`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--stack-type)`=`STACK_TYPE`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--subnet)`=`SUBNET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#TAG)`,…]] [`[--termination-time](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--termination-time)`=`TERMINATION_TIME`] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--threads-per-core)`=`THREADS_PER_CORE`] [`[--turbo-mode](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--turbo-mode)`=`TURBO_MODE`] [`[--visible-core-count](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--visible-core-count)`=`VISIBLE_CORE_COUNT`] [`[--address](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--address)`=`ADDRESS`     | `[--no-address](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--address)`] [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY` : `[--boot-disk-kms-keyring](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-kms-keyring)`=`BOOT_DISK_KMS_KEYRING` `[--boot-disk-kms-location](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-kms-location)`=`BOOT_DISK_KMS_LOCATION` `[--boot-disk-kms-project](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--boot-disk-kms-project)`=`BOOT_DISK_KMS_PROJECT`] [`[--confidential-compute](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--confidential-compute)`     | `[--confidential-compute-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--confidential-compute-type)`=`CONFIDENTIAL_COMPUTE_TYPE`] [`[--custom-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--custom-cpu)`=`CUSTOM_CPU` `[--custom-memory](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--custom-memory)`=`CUSTOM_MEMORY` : `[--custom-extensions](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--custom-extensions)` `[--custom-vm-type](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--custom-vm-type)`=`CUSTOM_VM_TYPE`] [`[--image-project](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--image-project)`=`IMAGE_PROJECT` `[--image](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--image)`=`IMAGE`     | `[--image-family](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--image-family)`=`IMAGE_FAMILY`] [`[--node](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--node)`=`NODE`     | `[--node-affinity-file](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--node-affinity-file)`=`PATH_TO_FILE`     | `[--node-group](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--node-group)`=`NODE_GROUP`] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--reservation-affinity)`=`RESERVATION_AFFINITY`; default="any"] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--scopes)`=[`SCOPE`,…]     | `[--no-scopes](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--scopes)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--service-account)`=`SERVICE_ACCOUNT`     | `[--no-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--service-account)`] [`[--service-proxy](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--service-proxy)`=[`enabled`],[`access-log`=`ACCESS-LOG`],[`network`=`NETWORK`],[`proxy-port`=`PROXY-PORT`],[`serving-ports`=`SERVING-PORTS`],[`tracing`=`TRACING`] `[--service-proxy-labels](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--service-proxy-labels)`=[`KEY`=`VALUE`, …,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-templates create` facilitates the creation
of Compute Engine virtual machine instance templates. Instance templates are
global resources, and can be used to create instances in any zone.

**EXAMPLES**

: To create an instance template named 'INSTANCE-TEMPLATE' with the 'n2' vm type,
'9GB' memory, and 2 CPU cores, run:

```
gcloud compute instance-templates create INSTANCE-TEMPLATE --custom-vm-type=n2 --custom-cpu=2 --custom-memory=9GB
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance template to create.

**FLAGS**

: **--accelerator**:
Attaches accelerators (e.g. GPUs) to the instances.

**`type`**:
The specific type (e.g. nvidia-tesla-t4 for NVIDIA T4) of accelerator to attach
to the instances. Use 'gcloud compute accelerator-types list' to learn about all
available accelerator types.

**`count`**:
Number of accelerators to attach to each instance. The default value is 1.

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

**--configure-disk**:
This option has effect only when used with `--source-instance`. It
allows you to override how the source-instance's disks are defined in the
template.

**`device-name`**:
Name of the device for which the configuration is being overridden.

**`auto-delete`**:
If `true`, this persistent disk will be automatically deleted when
the instance is deleted. However, if the disk is detached from the instance,
this option won't apply. If not provided, the setting is copied from the source
instance. Allowed values of the flag are: `false`, `no`,
`true`, and `yes`.

**`instantiate-from`**:
Specifies whether to include the disk and which image to use. Valid values are:
attach-read-only, blank, custom-image, do-not-include, source-image,
source-image-family

**`custom-image`**:
The custom image to use if custom-image is specified for instantiate-from.

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

**`replica-zones`**:
Required for each regional disk associated with the instance. Specify the URLs
of the zones where the disk should be replicated to. You must provide exactly
two replica zones, and one zone must be the same as the instance zone.

**--description**:
Specifies a textual description for the instance template.

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
Attaches an existing disk to the instances.

**`name`**:
The disk to attach to the instances. If you create more than one instance, you
can only attach a disk in read-only mode. By default, you attach a zonal disk
located in the same zone of the instance. If you want to attach a regional disk,
you must specify the disk using its URI; for example,
``projects/myproject/regions/us-central1/disks/my-regional-disk``.

**`mode`**:
The mode of the disk. Supported options are
``ro`` for read-only mode and
``rw`` for read-write mode. If omitted,
``rw`` is used as a default value. If you use
``rw`` when creating more than one instance,
you encounter errors.

**`boot`**:
If set to ``yes``, you attach a boot disk. The
virtual machine then uses the first partition of the disk for the root file
systems. The default value for this is ``no``.

**`device-name`**:
An optional name to display the disk name in the guest operating system. If
omitted, a device name of the form `persistent-disk-N` is used.

**`auto-delete`**:
If set to ``yes``, the persistent disk is
automatically deleted when the instance is deleted. However, if you detach the
disk from the instance, deleting the instance doesn't delete the disk. The
default value is ``yes``.

**`interface`**:
The interface to use for the disk. The value must be one of the following:

- SCSI
- NVME

**--[no-]enable-nested-virtualization**:
If set to true, enables nested virtualization for the instance. Use
`--enable-nested-virtualization` to enable and
`--no-enable-nested-virtualization` to disable.

**--[no-]enable-uefi-networking**:
If set to true, enables UEFI networking for the instance creation. Use
`--enable-uefi-networking` to enable and
`--no-enable-uefi-networking` to disable.

**--external-ipv6-address**:
Assigns the given external IPv6 address to the instance that is created. The
address must be the first IP address in the range. This option can be used only
when creating a single instance.

**--external-ipv6-prefix-length**:
The prefix length of the external IPv6 address range. This field should be used
together with `--external-ipv6-address`. Only the /96 IP address
range is supported, and the default value is 96.

**--host-error-timeout-seconds**:
The timeout in seconds for host error detection. The value must be set with 30
second increments, with a range of 90 to 330 seconds. If unset, the default
behavior of the host error recovery is used.

**--instance-template-region**:
Specifies the region of the regional instance template.

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

**--internal-ipv6-address**:
Assigns the given internal IPv6 address or range to the instance that is
created. The address must be the first IP address in the range or from a /96 IP
address range. This option can be used only when creating a single instance.

**--internal-ipv6-prefix-length**:
Optional field that indicates the prefix length of the internal IPv6 address
range. It should be used together with --internal-ipv6-address. Only /96 IP
address range is supported and the default value is 96. If not set, either the
prefix length from --internal-ipv6-address will be used or the default value of
96 will be assigned.

**--ipv6-network-tier**:
Specifies the IPv6 network tier that will be used to configure the instance
network interface IPv6 access config. `IPV6_NETWORK_TIER`
must be (only one value is supported):

**`PREMIUM`**:
High quality, Google-grade network tier.

**--key-revocation-action-type**:
Specifies the behavior of the instance when the KMS key of one of its attached
disks is revoked. The default is none. `POLICY` must be
one of:

**`none`**:
No operation is performed.

**`stop`**:
The instance is stopped when the KMS key of one of its attached disks is
revoked.

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

**--machine-type**:
Specifies the machine type used for the instances. To get a list of available
machine types, run 'gcloud compute machine-types list'. If unspecified, the
default type is n1-standard-1.

**--maintenance-policy**:
Specifies the behavior of the VMs when their host machines undergo maintenance.
The default is MIGRATE. For more information, see [https://cloud.google.com/compute/docs/instances/host-maintenance-options](https://cloud.google.com/compute/docs/instances/host-maintenance-options).
`MAINTENANCE_POLICY` must be one of:

**`MIGRATE`**:
The instances should be migrated to a new host. This will temporarily impact the
performance of instances during a migration event.

**`TERMINATE`**:
The instances should be terminated.

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

**--min-cpu-platform**:
When specified, the VM will be scheduled on host with specified CPU architecture
or a newer one. To list available CPU platforms in given zone, run:

```
gcloud compute zones describe ZONE --format="value(availableCpuPlatforms)"
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
flags: `--address`, `--network`,
`--network-tier`, `--subnet`,
`--private-network-ip`, `--stack-type`,
`--ipv6-network-tier`, `--internal-ipv6-address`,
`--internal-ipv6-prefix-length`, `--ipv6-address`,
`--ipv6-prefix-length`, `--external-ipv6-address`,
`--external-ipv6-prefix-length`,
`--ipv6-public-ptr-domain`. This flag can be repeated to specify
multiple network interfaces.
The following keys are allowed:

**`address`**:
Assigns the given external address to the instance that is created. Specifying
an empty string will assign an ephemeral IP. Mutually exclusive with no-address.
If neither key is present the instance will get an ephemeral IP.

**`network`**:
Specifies the network that the interface will be part of. If subnet is also
specified it must be subnetwork of this network. If neither is specified, this
defaults to the "default" network.

**`no-address`**:
If specified the interface will have no external IP. Mutually exclusive with
address. If neither key is present the instance will get an ephemeral IP.

**`network-tier`**:
Specifies the network tier of the interface.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

**`private-network-ip`**:
Assigns the given RFC1918 IP address to the interface.

**`subnet`**:
Specifies the subnet that the interface will be part of. If network key is also
specified this must be a subnetwork of the specified network.

**`nic-type`**:
Specifies the Network Interface Controller (NIC) type for the interface.
``NIC_TYPE`` must be one of:
`GVNIC`, `VIRTIO_NET`.

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

**`ipv6-network-tier`**:
Specifies the IPv6 network tier that will be used to configure the instance
network interface IPv6 access config.
``IPV6_NETWORK_TIER`` must be
`PREMIUM` (currently only one value is supported).

**`internal-ipv6-address`**:
Assigns the given internal IPv6 address or range to the instance that is
created. The address must be the first IP address in the range or from a /96 IP
address range. This option can be used only when creating a single instance.

**`internal-ipv6-prefix-length`**:
Optional field that indicates the prefix length of the internal IPv6 address
range. It should be used together with internal-ipv6-address. Only /96 IP
address range is supported and the default value is 96. If not set, either the
prefix length from --internal-ipv6-address will be used or the default value of
96 will be assigned.

**`external-ipv6-address`**:
Assigns the given external IPv6 address to the instance that is created. The
address must be the first IP address in the range. This option can be used only
when creating a single instance.

**`external-ipv6-prefix-length`**:
The prefix length of the external IPv6 address range. This field should be used
together with external-ipv6-address. Only the /96 IP address range is supported,
and the default value is 96.

**`ipv6-public-ptr-domain`**:
Assigns a custom PTR domain for the external IPv6 in the IPv6 access
configuration of instance. If its value is not specified, the default PTR record
will be used. This option can only be specified for the default network
interface, `nic0`.

**`aliases`**:
Specifies the IP alias ranges to allocate for this interface. If there are
multiple IP alias ranges, they are separated by semicolons.
For example:

```
--aliases="10.128.1.0/24;range1:/32"
```

Each IP alias range consists of a range name and a CIDR netmask (e.g.
`/24`) separated by a colon or just the netmask. The range name is
the name of the range within the network interface's subnet from which to
allocate an IP alias range. If unspecified, it defaults to the primary IP range
of the subnet. The IP allocator will pick an available range with the specified
netmask and allocate it to this network interface.

**`network-attachment`**:
Specifies the network attachment that this interface should connect to. Mutually
exclusive with `--network` and `--subnet` flags.

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

**--performance-monitoring-unit**:
The type of performance monitoring counters (PMCs) to enable in the instance.
`PERFORMANCE_MONITORING_UNIT` must be one of:

**`architectural`**:
This enables architecturally defined non-last level cache (LLC) events.

**`enhanced`**:
This enables most documented core/L2 and LLC events.

**`standard`**:
This enables most documented core/L2 events.

**--preemptible**:
If provided, instances will be preemptible and time-limited. Instances might be
preempted to free up resources for standard VM instances, and will only be able
to run for a limited amount of time. Preemptible instances can not be restarted
and will not migrate.

**--private-ipv6-google-access-type**:
The private IPv6 Google access type for the VM.
`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE` must be one of:
`enable-bidirectional-access`,
`enable-outbound-vm-access`, `inherit-subnetwork`.

**--private-network-ip**:
Specifies the RFC1918 IP to assign to the instance. The IP should be in the
subnet or legacy network IP range.

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

**--region**:
Region of the subnetwork to attach. If not specified, you might be prompted to
select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--resource-manager-tags**:
Specifies a list of resource manager tags to apply to the instance.

**--resource-policies**:
A list of resource policy names (not URLs) to be added to each instance created
using this instance template. If you attach any resource policies to an instance
template, you can only use that instance template to create instances that are
in the same region as the resource policies. Do not include resource policies
that are located in different regions in the same instance template.

**--restart-on-failure**:
The instances will be restarted if they are terminated by Compute Engine. This
does not affect terminations performed by the user. Enabled by default, use
`--no-restart-on-failure` to disable.

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

**--source-instance**:
The name of the source instance that the instance template will be created from.

**--source-instance-zone**:
Zone of the instance to operate on. Overrides the default
`compute/zone` property value for this command invocation.

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

**--address**

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

**--node**

**--reservation**

**--scopes**

**--service-account**

**--service-proxy**:
Controls whether the Traffic Director service proxy (Envoy) and agent are
installed and configured on the VM. "cloud-platform" scope is enabled
automatically to allow connections to the Traffic Director API. Do not use the
--no-scopes flag.

**`enabled`**:
If specified, the service-proxy software will be installed when the instance is
created. The instance is configured to work with Traffic Director.

**`serving-ports`**:
Semi-colon-separated (;) list of the ports, specified inside quotation marks
("), on which the customer's application/workload is serving.
For example:

```
serving-ports="80;8080"
```

The service proxy will intercept inbound traffic, then forward it to the
specified serving port(s) on localhost. If not provided, no incoming traffic is
intercepted.

**`proxy-port`**:
The port on which the service proxy listens. The VM intercepts traffic and
redirects it to this port to be handled by the service proxy. If omitted, the
default value is '15001'.

**`tracing`**:
Enables the service proxy to generate distributed tracing information. If set to
ON, the service proxy's control plane generates a configuration that enables
request ID-based tracing. For more information, refer to the
`generate_request_id` documentation for the Envoy proxy. Allowed
values are `ON` and `OFF`.

**`access-log`**:
The filepath for access logs sent to the service proxy by the control plane. All
incoming and outgoing requests are recorded in this file. For more information,
refer to the file access log documentation for the Envoy proxy.

**`network`**:
The name of a valid VPC network. The Google Cloud Platform VPC network used by
the service proxy's control plane to generate dynamic configuration for the
service proxy.

**--service-proxy-labels**:
Labels that you can apply to your service proxy. These will be reflected in your
Envoy proxy's bootstrap metadata. These can be any `key=value` pairs
that you want to set as proxy metadata (for example, for use with config
filtering). You might use these flags for application and version labels:
`app=review` and/or `version=canary`.

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
gcloud alpha compute instance-templates create
```

```
gcloud beta compute instance-templates create
```