# gcloud compute instances attach-disk  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk)*

**NAME**

: **gcloud compute instances attach-disk - attach a disk to an instance**

**SYNOPSIS**

: **`gcloud compute instances attach-disk` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#INSTANCE_NAME)` `[--disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--disk)`=`DISK` [`[--boot](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--boot)`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--csek-key-file)`=`FILE`] [`[--device-name](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--device-name)`=`DEVICE_NAME`] [`[--disk-scope](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--disk-scope)`=`DISK_SCOPE`; default="zonal"] [`[--force-attach](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--force-attach)`] [`[--interface](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--interface)`=`INTERFACE`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--mode)`=`MODE`; default="rw"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances attach-disk` is used to attach a disk to an
instance. For example,

```
gcloud compute instances attach-disk example-instance --disk DISK --zone us-central1-a
```

attaches the disk named 'DISK' to the instance named 'example-instance' in zone
``us-central1-a``.
After you create and attach a new disk to an instance, you must [format
and mount](https://cloud.google.com/compute/docs/disks/add-persistent-disk#formatting) the disk so that the operating system can use the available
storage space. You can attach an existing non-boot disk to more than one
instance. For more information, see [Share a disk
between VMs](https://cloud.google.com/sdk/gcloud/reference/compute/instances/compute/docs/disks/add-persistent-disk#use_multi_instances).

**EXAMPLES**

: To attach a disk named 'my-disk' as a boot disk to an instance named
'my-instance', run:

```
gcloud compute instances attach-disk my-instance --disk=my-disk --boot
```

To attach a device named 'my-device' for read-only access to an instance named
'my-instance', run:

```
gcloud compute instances attach-disk my-instance --device-name=my-device --mode=ro
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--disk**:
The name of the disk to attach to the instance.

**OPTIONAL FLAGS**

: **--boot**:
Attach the disk to the instance as a boot disk.

**--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine resources to user managed keys to be used when creating, mounting, or
taking snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--device-name**:
An optional name that indicates the disk name the guest operating system will
see. (Note: Device name does not correspond to mounted volume name). Must match
the disk name if the disk is going to be mounted to a container with
--container-mount-disk (alpha feature).

**--disk-scope**:
The scope of the disk. `DISK_SCOPE` must be one of:

**`regional`**:
The disk specified in --disk is interpreted as a regional disk in the same
region as the instance. Ignored if a full URI is provided to the
`--disk` flag.

**`zonal`**:
The disk specified in --disk is interpreted as a zonal disk in the same zone as
the instance. Ignored if a full URI is provided to the `--disk` flag.

**--force-attach**:
Attach the disk to the instance even if it is currently attached to another
instance. The attachment will succeed even if detaching from the previous
instance fails at first. The server will continue trying to detach the disk from
the previous instance in the background.

**--interface**:
The interface of the disk. `INTERFACE` must be one of:

**`NVME`**:
NVME

**`SCSI`**:
SCSI

**--mode**:
Specifies the mode of the disk. `MODE` must be one of:

**`ro`**:
Read-only.

**`rw`**:
Read-write.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
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
gcloud alpha compute instances attach-disk
```

```
gcloud beta compute instances attach-disk
```