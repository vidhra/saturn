# gcloud compute instances detach-disk  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk)*

**NAME**

: **gcloud compute instances detach-disk - detach disks from Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud compute instances detach-disk` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#INSTANCE_NAME)` (`[--device-name](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--device-name)`=`DEVICE_NAME`     | `[--disk](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--disk)`=`DISK`) [`[--disk-scope](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--disk-scope)`=`DISK_SCOPE`; default="zonal"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances detach-disk` is used to detach disks from
virtual machines.
Detaching a disk without first unmounting it may result in incomplete I/O
operations and data corruption. To unmount a persistent disk on a Linux-based
image, ssh into the instance and run:

```
sudo umount /dev/disk/by-id/google-DEVICE_NAME
```

**EXAMPLES**

: To detach a disk named 'my-disk' from an instance named 'my-instance', run:

```
gcloud compute instances detach-disk my-instance --disk=my-disk
```

To detach a device named 'my-device' from an instance named 'my-instance', run:

```
gcloud compute instances detach-disk my-instance --device-name=my-device
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--device-name**

**OPTIONAL FLAGS**

: **--disk-scope**:
The scope of the disk. `DISK_SCOPE` must be one of:

**`regional`**:
The disk specified in --disk is interpreted as a regional disk in the same
region as the instance. Ignored if a full URI is provided to the
`--disk` flag.

**`zonal`**:
The disk specified in --disk is interpreted as a zonal disk in the same zone as
the instance. Ignored if a full URI is provided to the `--disk` flag.

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
gcloud alpha compute instances detach-disk
```

```
gcloud beta compute instances detach-disk
```