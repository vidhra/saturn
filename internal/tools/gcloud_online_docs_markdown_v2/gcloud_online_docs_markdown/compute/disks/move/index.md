# gcloud compute disks move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/move](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move)*

**NAME**

: **gcloud compute disks move - move a disk between zones**

**SYNOPSIS**

: **`gcloud compute disks move` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move#DISK_NAME)` `[--destination-zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move#--destination-zone)`=`DESTINATION_ZONE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move#--async)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/move#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks move` facilitates moving a Compute Engine disk
volume from one zone to another. You cannot move a disk if it is attached to a
running or stopped instance; use the gcloud compute instances move command
instead.
The `gcloud compute disks move` command does not support regional
persistent disks. See [https://cloud.google.com/compute/docs/disks/regional-persistent-disk](https://cloud.google.com/compute/docs/disks/regional-persistent-disk)
for more details.

**EXAMPLES**

: To move the disk called example-disk-1 from us-central1-b to us-central1-f, run:

```
gcloud compute disks move example-disk-1 --zone=us-central1-b --destination-zone=us-central1-f
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**REQUIRED FLAGS**

: **--destination-zone**:
The zone to move the disk to.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--zone**:
Zone of the disk to operate on. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
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
gcloud alpha compute disks move
```

```
gcloud beta compute disks move
```