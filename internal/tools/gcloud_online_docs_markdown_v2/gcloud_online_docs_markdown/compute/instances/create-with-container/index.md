# gcloud compute instances create-with-container  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container)*

**NAME**

: **gcloud compute instances create-with-container - creates Compute Engine virtual machine instances running     container images**

**SYNOPSIS**

: **`gcloud compute instances create-with-container` `[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#INSTANCE_NAMES)` [`[INSTANCE_NAMES](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#INSTANCE_NAMES)` …] [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--no-boot-disk-auto-delete](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-auto-delete)`] [`[--boot-disk-device-name](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-device-name)`=`BOOT_DISK_DEVICE_NAME`] [`[--boot-disk-interface](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-interface)`=`BOOT_DISK_INTERFACE`] [`[--boot-disk-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-provisioned-iops)`=`BOOT_DISK_PROVISIONED_IOPS`] [`[--boot-disk-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-provisioned-throughput)`=`BOOT_DISK_PROVISIONED_THROUGHPUT`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-size)`=`BOOT_DISK_SIZE`] [`[--boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--boot-disk-type)`=`BOOT_DISK_TYPE`] [`[--can-ip-forward](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--can-ip-forward)`] [`[--container-arg](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-arg)`=`CONTAINER_ARG`] [`[--container-command](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-command)`=`CONTAINER_COMMAND`] [`[--container-env](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-env)`=[`KEY`=`VALUE`, …,…]] [`[--container-env-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-env-file)`=`CONTAINER_ENV_FILE`] [`[--container-image](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-image)`=`CONTAINER_IMAGE`] [`[--container-mount-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-mount-disk)`=[`mode`=`MODE`],[`mount-path`=`MOUNT-PATH`],[`name`=`NAME`],[`partition`=`PARTITION`]] [`[--container-mount-host-path](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-mount-host-path)`=[`host-path`=`HOSTPATH`,`mount-path`=`MOUNTPATH`[,`mode`=`MODE`],…]] [`[--container-mount-tmpfs](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-mount-tmpfs)`=[`mount-path`=`MOUNTPATH`,…]] [`[--container-privileged](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-privileged)`] [`[--container-restart-policy](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-restart-policy)`=`POLICY`; default="always"] [`[--container-stdin](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-stdin)`] [`[--container-tty](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--container-tty)`] [`[--create-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--create-disk)`=[`PROPERTY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--description)`=`DESCRIPTION`] [`[--discard-local-ssds-at-termination-timestamp](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--discard-local-ssds-at-termination-timestamp)`=`DISCARD_LOCAL_SSDS_AT_TERMINATION_TIMESTAMP`] [`[--disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--disk)`=[`auto-delete`=`AUTO-DELETE`],[`boot`=`BOOT`],[`device-name`=`DEVICE-NAME`],[`force-attach`=`FORCE-ATTACH`],[`interface`=`INTERFACE`],[`mode`=`MODE`],[`name`=`NAME`],[`scope`=`SCOPE`]] [`[--[no-]enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--[no-]enable-nested-virtualization)`] [`[--external-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--external-ipv6-address)`=`EXTERNAL_IPV6_ADDRESS`] [`[--external-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--external-ipv6-prefix-length)`=`EXTERNAL_IPV6_PREFIX_LENGTH`] [`[--host-error-timeout-seconds](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--host-error-timeout-seconds)`=`HOST_ERROR_TIMEOUT_SECONDS`] [`[--instance-termination-action](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--instance-termination-action)`=`INSTANCE_TERMINATION_ACTION`] [`[--internal-ipv6-address](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--internal-ipv6-address)`=`INTERNAL_IPV6_ADDRESS`] [`[--internal-ipv6-prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--internal-ipv6-prefix-length)`=`INTERNAL_IPV6_PREFIX_LENGTH`] [`[--ipv6-network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--ipv6-network-tier)`=`IPV6_NETWORK_TIER`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--labels)`=[`KEY`=`VALUE`,…]] [`[--local-ssd-recovery-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--local-ssd-recovery-timeout)`=`LOCAL_SSD_RECOVERY_TIMEOUT`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--machine-type)`=`MACHINE_TYPE`] [`[--maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--maintenance-policy)`=`MAINTENANCE_POLICY`] [`[--max-run-duration](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--max-run-duration)`=`MAX_RUN_DURATION`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--min-cpu-platform)`=`PLATFORM`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--network)`=`NETWORK`] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--network-interface)`=[`PROPERTY`=`VALUE`,…]] [`[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--network-performance-configs)`=[`PROPERTY`=`VALUE`,…]] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--network-tier)`=`NETWORK_TIER`] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--preemptible)`] [`[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`] [`[--private-network-ip](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--private-network-ip)`=`PRIVATE_NETWORK_IP`] [`[--provisioning-model](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--provisioning-model)`=`PROVISIONING_MODEL`] [`[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--resource-policies)`=[`RESOURCE_POLICY`,…]] [`[--no-restart-on-failure](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--restart-on-failure)`] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--shielded-vtpm)`] [`[--source-instance-template](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--source-instance-template)`=`SOURCE_INSTANCE_TEMPLATE`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--stack-type)`=`STACK_TYPE`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--subnet)`=`SUBNET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#TAG)`,…]] [`[--termination-time](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--termination-time)`=`TERMINATION_TIME`] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--threads-per-core)`=`THREADS_PER_CORE`] [`[--visible-core-count](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--visible-core-count)`=`VISIBLE_CORE_COUNT`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--zone)`=`ZONE`] [`[--address](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--address)`=`ADDRESS`     | `[--no-address](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--address)`] [`[--confidential-compute](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--confidential-compute)`     | `[--confidential-compute-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--confidential-compute-type)`=`CONFIDENTIAL_COMPUTE_TYPE`] [`[--custom-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--custom-cpu)`=`CUSTOM_CPU` `[--custom-memory](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--custom-memory)`=`CUSTOM_MEMORY` : `[--custom-extensions](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--custom-extensions)` `[--custom-vm-type](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--custom-vm-type)`=`CUSTOM_VM_TYPE`] [`[--image-project](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--image-project)`=`IMAGE_PROJECT` `[--image](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--image)`=`IMAGE`     | `[--image-family](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--image-family)`=`IMAGE_FAMILY`] [`[--public-ptr](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--public-ptr)`     | `[--no-public-ptr](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--public-ptr)`] [`[--public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--public-ptr-domain)`=`PUBLIC_PTR_DOMAIN`     | `[--no-public-ptr-domain](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--public-ptr-domain)`] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--reservation-affinity)`=`RESERVATION_AFFINITY`; default="any"] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--scopes)`=[`SCOPE`,…]     | `[--no-scopes](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--scopes)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--service-account)`=`SERVICE_ACCOUNT`     | `[--no-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#--service-account)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances create-with-container` creates Compute
Engine virtual machines that runs a Docker image. For example:

```
gcloud compute instances create-with-container instance-1 --zone us-central1-a             --container-image=gcr.io/google-containers/busybox
```

creates an instance called instance-1, in the us-central1-a zone, running the
'busybox' image.
For more examples, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To run the gcr.io/google-containers/busybox image on an instance named
'instance-1' that executes 'echo "Hello world"' as a run command, run:

```
gcloud compute instances create-with-container instance-1 --container-image=gcr.io/google-containers/busybox --container-command='echo "Hello world"'
```

To run the gcr.io/google-containers/busybox image in privileged mode, run:

```
gcloud compute instances create-with-container instance-1 --container-image=gcr.io/google-containers/busybox --container-privileged
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAMES` [`INSTANCE_NAMES` …]**:
Names of the instances to create. For details on valid instance names, refer to
the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

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

**--container-arg**:
Argument to append to container entrypoint or to override container CMD. Each
argument must have a separate flag. Arguments are appended in the order of
flags. Example:
Assuming the default entry point of the container (or an entry point overridden
with --container-command flag) is a Bourne shell-compatible executable, in order
to execute 'ls -l' command in the container, the user could use:
`--container-arg="-c" --container-arg="ls -l"`
Caveat: due to the nature of the argument parsing, it's impossible to provide
the flag value that starts with a dash (`-`) without the
`=` sign (that is, `--container-arg "-c"` will not work
correctly).
Default: None. (no arguments appended)

**--container-command**:
Specifies what executable to run when the container starts (overrides default
entrypoint), eg. `nc`.
Default: None (default container entrypoint is used)

**--container-env**:
Declare environment variables KEY with value VALUE passed to container. Only the
last value of KEY is taken when KEY is repeated more than once.
Values, declared with --container-env flag override those with the same KEY from
file, provided in --container-env-file.

**--container-env-file**:
Declare environment variables in a file. Values, declared with --container-env
flag override those with the same KEY from file.
File with environment variables in format used by docker (almost). This means:

- Lines are in format KEY=VALUE.
- Values must contain equality signs.
- Variables without values are not supported (this is different from docker
format).
- If `#` is first non-whitespace character in a line the line is
ignored as a comment.
- Lines with nothing but whitespace are ignored.

**--container-image**:
Full container image name, which should be pulled onto VM instance, eg.
`docker.io/tomcat`.

**--container-mount-disk**:
Mounts a disk to the specified mount path in the container. Multiple ' flags are
allowed. Must be used with `--disk` or `--create-disk`.

**`name`**:
Name of the disk. If exactly one additional disk is attached to the instance
using `--disk` or `--create-disk`, specifying disk name
here is optional. The name of the single additional disk will be used by
default.

**`mount-path`**:
Path on container to mount to. Mount paths with spaces and commas (and other
special characters) are not supported by this command.

**`partition`**:
Optional. The partition of the disk to mount. Multiple partitions of a disk can
be mounted. Can't be used with --create-disk.

**`mode`**:
Volume mount mode: `rw` (read/write) or `ro` (read-only).
Defaults to `rw`. Fails if the disk mode is `ro` and
volume mount mode is `rw`.

**--container-mount-host-path**:
Mounts a volume by using host-path.

**`host-path`**:
Path on host to mount from.

**`mount-path`**:
Path on container to mount to. Mount paths with spaces and commas (and other
special characters) are not supported by this command.

**`mode`**:
Volume mount mode: rw (read/write) or ro (read-only).
Default: rw.

**--container-mount-tmpfs**:
Mounts empty tmpfs into container at MOUNTPATH.

**`mount-path`**:
Path on container to mount to. Mount paths with spaces and commas (and other
special characters) are not supported by this command.

**--container-privileged**:
Specify whether to run container in privileged mode.
Default: `--no-container-privileged`.

**--container-restart-policy**:
Specify whether to restart a container on exit. `POLICY`
must be one of: `never`, `on-failure`,
`always`.

**--container-stdin**:
Keep container STDIN open even if not attached.
Default: `--no-container-stdin`.

**--container-tty**:
Allocate a pseudo-TTY for the container.
Default: `--no-container-tty`.

**--create-disk**:
Creates and attaches persistent disks to the instances.

**`name`**:
Specifies the name of the disk. This option cannot be specified if more than one
instance is being created. Must specify this option if attaching the disk to a
container with `--container-mount-disk`.

**`description`**:
Optional textual description for the disk being created.

**`mode`**:
Specifies the mode of the disk. Supported options are
``ro`` for read-only and
``rw`` for read-write. If omitted,
``rw`` is used as a default. It is an error to
create a disk in `ro` mode if attaching it to a container with
`--container-mount-disk`.

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
An optional name to display the disk name in the guest operating system. Must be
the same as `name` if used with `--container-mount-disk`.
If omitted, a device name of the form `persistent-disk-N` is used. If
omitted and used with `--container-mount-disk` (where the
`name` of the container mount disk is the same as in this flag), a
device name equal to disk `name` is used.

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
An optional name to display the disk name in the guest operating system. Must be
the same as `name` if used with `--container-mount-disk`.
If omitted, a device name of the form `persistent-disk-N` is used. If
omitted and used with `--container-mount-disk` (where the
`name` of the container mount disk is the same as in this flag), a
device name equal to disk `name` is used.

**`auto-delete`**:
If set to ``yes``, the persistent disk is
automatically deleted when the instance is deleted. However, if you detach the
disk from the instance, deleting the instance doesn't delete the disk. The
default value is ``yes``.

**`interface`**:
The interface to use for the disk. The value must be one of the following:

- SCSI
- NVME

**`scope`**:
Can be `zonal` or `regional`. If
``zonal``, the disk is interpreted as a zonal
disk in the same zone as the instance (default). If
``regional``, the disk is interpreted as a
regional disk in the same region as the instance. The default value for this is
``zonal``.

**`force-attach`**:
If ``yes``, this persistent disk will
force-attached to the instance even it is already attached to another instance.
The default value is 'no'.

**--[no-]enable-nested-virtualization**:
If set to true, enables nested virtualization for the instance. Use
`--enable-nested-virtualization` to enable and
`--no-enable-nested-virtualization` to disable.

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

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
`--external-ipv6-prefix-length`. This flag can be repeated to specify
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

**`aliases`**:
Specifies the IP alias ranges to allocate for this interface. If there are
multiple IP alias ranges, they are separated by semicolons.
For example:

```
--aliases="10.128.1.0/24;range1:/32"
```

Each IP alias range consists of a range name and an IP range separated by a
colon, or just the IP range. The range name is the name of the range within the
network interface's subnet from which to allocate an IP alias range. If
unspecified, it defaults to the primary IP range of the subnet. The IP range can
be a CIDR range (e.g. `192.168.100.0/24`), a single IP address (e.g.
`192.168.100.1`), or a netmask in CIDR format (e.g.
`/24`). If the IP range is specified by CIDR range or single IP
address, it must belong to the CIDR range specified by the range name on the
subnet. If the IP range is specified by netmask, the IP allocator will pick an
available range with the specified netmask and allocate it to this network
interface.

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

**--resource-policies**:
A list of resource policy names to be added to the instance. The policies must
exist in the same region as the instance.

**--restart-on-failure**:
The instances will be restarted if they are terminated by Compute Engine. This
does not affect terminations performed by the user. Enabled by default, use
`--no-restart-on-failure` to disable.

**--shielded-integrity-monitoring**:
Enables monitoring and attestation of the boot integrity of the instance. The
attestation is performed against the integrity policy baseline. This baseline is
initially derived from the implicitly trusted boot image when the instance is
created. This baseline can be updated by using `gcloud compute instances
update-container --shielded-learn-integrity-policy`. On Shielded VM
instances, integrity monitoring is enabled by default. For information about how
to modify Shielded VM options, see [https://cloud.google.com/compute/docs/instances/modifying-shielded-vm](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).
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
The name of the instance template that the instance will be created from. An
instance template can be a global/regional resource.
Users can override instance properties using other flags.

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

**--visible-core-count**:
The number of physical cores to expose to the instance's guest operating system.
The number of virtual CPUs visible to the instance's guest operating system is
this number of cores multiplied by the instance's count of visible threads per
physical core.

**--zone**:
Zone of the instances to create. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

**--address**

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

**--public-ptr**

**--public-ptr-domain**

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

: These variants are also available:

```
gcloud alpha compute instances create-with-container
```

```
gcloud beta compute instances create-with-container
```