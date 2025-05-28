# gcloud alpha compute disks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create)*

**NAME**

: **gcloud alpha compute disks create - create Compute Engine persistent disks**

**SYNOPSIS**

: **`gcloud alpha compute disks create` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#DISK_NAME)` [`[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#DISK_NAME)` …] [`[--access-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--access-mode)`=`ACCESS_MODE`] [`[--architecture](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--architecture)`=`ARCHITECTURE`] [`[--confidential-compute](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--confidential-compute)`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--csek-key-file)`=`FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--description)`=`DESCRIPTION`] [`[--erase-windows-vss-signature](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--erase-windows-vss-signature)`] [`[--guest-os-features](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--guest-os-features)`=[`GUEST_OS_FEATURE`,…]] [`[--interface](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--interface)`=`INTERFACE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--licenses)`=[`LICENSE`,…]] [`[--multi-writer](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--multi-writer)`] [`[--physical-block-size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--physical-block-size)`=`PHYSICAL_BLOCK_SIZE`; default="4096"] [`[--primary-disk-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--primary-disk-project)`=`PRIMARY_DISK_PROJECT`] [`[--provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--provisioned-iops)`=`PROVISIONED_IOPS`] [`[--provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--provisioned-throughput)`=`PROVISIONED_THROUGHPUT`] [`[--replica-zones](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--replica-zones)`=`ZONE`,`[ZONE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#ZONE)`] [`[--no-require-csek-key-create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--require-csek-key-create)`] [`[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--resource-policies)`=[`RESOURCE_POLICY`,…]] [`[--size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--size)`=`SIZE`] [`[--storage-pool](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--storage-pool)`=`STORAGE_POOL`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--type)`=`TYPE`] [`[--user-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--user-licenses)`=[`LICENSE`,…]] [`[--global-source-snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--global-source-snapshot)`     | `[--source-snapshot-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-snapshot-region)`=`SOURCE_SNAPSHOT_REGION`] [`[--image-family-scope](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--image-family-scope)`=`IMAGE_FAMILY_SCOPE` `[--image-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--image-project)`=`IMAGE_PROJECT` `[--image](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--image)`=`IMAGE`     | `[--image-family](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--image-family)`=`IMAGE_FAMILY`     | `[--primary-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--primary-disk)`=`PRIMARY_DISK`     | `[--source-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-disk)`=`SOURCE_DISK`     | `[--source-instant-snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-instant-snapshot)`=`SOURCE_INSTANT_SNAPSHOT`     | `[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-snapshot)`=`SOURCE_SNAPSHOT`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--kms-project)`=`KMS_PROJECT`] [`[--primary-disk-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--primary-disk-region)`=`PRIMARY_DISK_REGION`     | `[--primary-disk-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--primary-disk-zone)`=`PRIMARY_DISK_ZONE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--zone)`=`ZONE`] [`[--source-disk-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-disk-region)`=`SOURCE_DISK_REGION`     | `[--source-disk-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#--source-disk-zone)`=`SOURCE_DISK_ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks create` creates one
or more Compute Engine persistent disks. When creating virtual machine
instances, disks can be attached to the instances through the `[gcloud compute instances
create](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create)` command. Disks can also be attached to instances that are
already running using `[gcloud compute
instances attach-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk)`.
Disks are zonal resources, so they reside in a particular zone for their entire
lifetime. The contents of a disk can be moved to a different zone by
snapshotting the disk (using `[gcloud compute disks
snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot)`) and creating a new disk using
`--source-snapshot` in the desired zone. The contents of a disk can
also be moved across project or zone by creating an image (using `[gcloud compute images
create](https://cloud.google.com/sdk/gcloud/reference/compute/images/create)`) and creating a new disk using `--image` in the
desired project and/or zone.
For a comprehensive guide, including details on minimum and maximum disk size,
refer to: [https://cloud.google.com/compute/docs/disks](https://cloud.google.com/compute/docs/disks)

**EXAMPLES**

: When creating disks, be sure to include the `--zone` option. To
create disks 'my-disk-1' and 'my-disk-2' in zone us-east1-a:

```
gcloud alpha compute disks create my-disk-1 my-disk-2 --zone=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME` [`DISK_NAME` …]**:
Names of the disks to create. For details on the naming convention for this
resource, refer to: [https://cloud.google.com/compute/docs/naming-resources](https://cloud.google.com/compute/docs/naming-resources)

**FLAGS**

: **--access-mode**:
Specifies how VMs attached to the disk can access the data on the disk. To grant
read-only access to multiple VMs attached to the disk, set access-mode to
READ_ONLY_MANY. To grant read-write access to only one VM attached to the disk,
use READ_WRITE_SINGLE. READ_WRITE_SINGLE is used if omitted.
`ACCESS_MODE` must be one of: `READ_ONLY_MANY`,
`READ_WRITE_MANY`, `READ_WRITE_SINGLE`.

**--architecture**:
Specifies the architecture or processor type that this disk can support. For
available processor types on Compute Engine, see [https://cloud.google.com/compute/docs/cpu-platforms](https://cloud.google.com/compute/docs/cpu-platforms).
`ARCHITECTURE` must be one of: `ARM64`,
`X86_64`.

**--confidential-compute**:
Creates the disk with confidential compute mode enabled. Encryption with a Cloud
KMS key is required to enable this option.

**--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine resources to user managed keys to be used when creating, mounting, or
taking snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--description**:
An optional, textual description for the disks being created.

**--erase-windows-vss-signature**:
Specifies whether the disk restored from a source snapshot should erase Windows
specific VSS signature. See [https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--guest-flush)

**--guest-os-features**:
Enables one or more features for VM instances that use the image for their boot
disks. See the descriptions of supported features at: [https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).
`GUEST_OS_FEATURE` must be one of:
`BARE_METAL_LINUX_COMPATIBLE`, `GVNIC`, `IDPF`,
`MULTI_IP_SUBNET`, `SEV_CAPABLE`,
`SEV_LIVE_MIGRATABLE`, `SEV_LIVE_MIGRATABLE_V2`,
`SEV_SNP_CAPABLE`, `SNP_SVSM_CAPABLE`,
`TDX_CAPABLE`, `UEFI_COMPATIBLE`,
`VIRTIO_SCSI_MULTIQUEUE`, `WINDOWS`.

**--interface**:
Specifies the disk interface to use for attaching this disk. Valid values are
`SCSI` and `NVME`. The default is `SCSI`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--licenses**:
A list of URIs to license resources. The provided licenses will be added onto
the created disks to indicate the licensing and billing policies.

**--multi-writer**:
Create the disk in multi-writer mode so that it can be attached with read-write
access to two VMs. The multi-writer feature requires specialized filesystems,
among other restrictions. For more information, see [https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

**--physical-block-size**:
Physical block size of the persistent disk in bytes. Valid values are
4096(default) and 16384. `PHYSICAL_BLOCK_SIZE` must be one
of: `4096`, `16384`.

**--primary-disk-project**:
Project of the primary disk for asynchronous replication.

**--provisioned-iops**:
Provisioned IOPS of disk to create. Only for use with disks of type pd-extreme
and hyperdisk-extreme.

**--provisioned-throughput**:
Provisioned throughput of disk to create. The throughput unit is MB per sec.
Only for use with disks of type hyperdisk-throughput.

**--replica-zones**:
A comma-separated list of exactly 2 zones that a regional disk will be
replicated to. Required when creating regional disk. The zones must be in the
same region as specified in the `--region` flag. See available zones
with `[gcloud compute
zones list](https://cloud.google.com/sdk/gcloud/reference/compute/zones/list)`.

**--require-csek-key-create**:
Refuse to create resources not protected by a user managed key in the key file
when --csek-key-file is given. This behavior is enabled by default to prevent
incorrect gcloud invocations from accidentally creating resources with no user
managed key. Disabling the check allows creation of some resources without a
matching Customer-Supplied Encryption Key in the supplied --csek-key-file. See
[https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details. Enabled by default, use
`--no-require-csek-key-create` to disable.

**--resource-policies**:
A list of resource policy names to be added to the disk. The policies must exist
in the same region as the disk.

**--size**:
Size of the disks. The value must be a whole number followed by a size unit of
``GB`` for gigabyte, or
``TB`` for terabyte. If no size unit is
specified, GB is assumed. For example, ``10GB``
will produce 10 gigabyte disks. Disk size must be a multiple of 1 GB. If disk
size is not specified, the default size of 500GB for pd-standard disks, 100GB
for pd-balanced disks, 100GB for pd-ssd disks, and 1000GB for pd-extreme will be
used. For details about disk size limits, refer to: [https://cloud.google.com/compute/docs/disks](https://cloud.google.com/compute/docs/disks)

**--storage-pool**:
Specifies the URI of the storage pool in which the disk is created.

**--type**:
Specifies the type of disk to create. To get a list of available disk types, run
`[gcloud compute
disk-types list](https://cloud.google.com/sdk/gcloud/reference/compute/disk-types/list)`. The default disk type is pd-standard.

**--user-licenses**:
List of URIs to license resources. User-provided licenses can be edited after
disk is created.

**--global-source-snapshot**

**--image-family-scope**:
Sets the scope for the `--image-family` flag. By default, when
specifying an image family in a public image project, the zonal image family
scope is used. All other projects default to the global image. Use this flag to
override this behavior. `IMAGE_FAMILY_SCOPE` must be one
of: `zonal`, `global`.

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

**--kms-key**

**--primary-disk-region**

**--region**

**--source-disk-region**

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
gcloud compute disks create
```

```
gcloud beta compute disks create
```