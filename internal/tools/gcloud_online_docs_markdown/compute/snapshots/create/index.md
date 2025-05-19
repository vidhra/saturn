# gcloud compute snapshots create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create)*

**NAME**

: **gcloud compute snapshots create - create Compute Engine snapshots**

**SYNOPSIS**

: **`gcloud compute snapshots create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--async)`] [`[--chain-name](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--chain-name)`=`CHAIN_NAME`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--csek-key-file)`=`FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--description)`=`DESCRIPTION`] [`[--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--guest-flush)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--snapshot-type](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--snapshot-type)`=`SNAPSHOT_TYPE`] [`[--source-disk](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk)`=`SOURCE_DISK`] [`[--source-disk-for-recovery-checkpoint](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk-for-recovery-checkpoint)`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT`] [`[--source-disk-for-recovery-checkpoint-region](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk-for-recovery-checkpoint-region)`=`SOURCE_DISK_FOR_RECOVERY_CHECKPOINT_REGION`] [`[--source-disk-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk-key-file)`=`FILE`] [`[--source-instant-snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-instant-snapshot)`=`SOURCE_INSTANT_SNAPSHOT`] [`[--source-instant-snapshot-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-instant-snapshot-key-file)`=`FILE`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--storage-location)`=`LOCATION`] [`[--source-disk-region](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk-region)`=`SOURCE_DISK_REGION`     | `[--source-disk-zone](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-disk-zone)`=`SOURCE_DISK_ZONE`] [`[--source-instant-snapshot-region](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-instant-snapshot-region)`=`SOURCE_INSTANT_SNAPSHOT_REGION`     | `[--source-instant-snapshot-zone](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#--source-instant-snapshot-zone)`=`SOURCE_INSTANT_SNAPSHOT_ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute snapshots create` creates snapshot of persistent
disk. Snapshots are useful for backing up persistent disk data and for creating
custom images. For more information, see [https://cloud.google.com/compute/docs/disks/create-snapshots](https://cloud.google.com/compute/docs/disks/create-snapshots).

**EXAMPLES**

: To create a snapshot 'my-snap' from a disk 'my-disk' in zone 'us-east1-a', run:

```
gcloud compute snapshots create my-snap --source-disk=my-disk --source-disk-zone=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the snapshot.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--chain-name**:
Create the new snapshot in the snapshot chain labeled with the specified name.
The chain name must be 1-63 characters long and comply with RFC1035. Use this
flag only if you are an advanced service owner who needs to create separate
snapshot chains, for example, for chargeback tracking. When you describe your
snapshot resource, this field is visible only if it has a non-empty value.

**--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine resources to user managed keys to be used when creating, mounting, or
taking snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--description**:
Text to describe the new snapshot.

**--guest-flush**:
Create an application-consistent snapshot by informing the OS to prepare for the
snapshot process. Currently only supported for creating snapshots of disks
attached to Windows instances.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--snapshot-type**:
Type of snapshot. If a snapshot type is not specified, a STANDARD snapshot will
be created. `SNAPSHOT_TYPE` must be one of:
`ARCHIVE`, `STANDARD`.

**--source-disk**:
Source disk used to create the snapshot. To create a snapshot from a source disk
in a different project, specify the full path to the source disk. For example:
[https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/disks/MY-DISK](https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/disks/MY-DISK)

**--source-disk-for-recovery-checkpoint**:
Source disk whose recovery checkpoint used to create the snapshot. To create a
snapshot from the recovery checkpoint of a source disk in a different project,
specify the full path to the source disk. For example:
projects/MY-PROJECT/regions/MY-REGION/disks/MY-DISK

**--source-disk-for-recovery-checkpoint-region**:
Region of the source disk for recovery checkpoint to operate on. Overrides the
default `compute/region` property value for this command invocation.

**--source-disk-key-file**:
Path to the customer-supplied encryption key of the source disk. Required if the
source disk is protected by a customer-supplied encryption key.

**--source-instant-snapshot**:
The name or URL of the source instant snapshot. If the name is provided, the
instant snapshot's zone or region must be specified with
--source-instant-snapshot-zone or --source-instant-snapshot-region accordingly.
To create a snapshot from an instant snapshot in a different project, specify
the full path to the instant snapshot. If the URL is provided, format should be:
[https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/instantSnapshots/MY-INSTANT-SNAPSHOT](https://www.googleapis.com/compute/v1/projects/MY-PROJECT/zones/MY-ZONE/instantSnapshots/MY-INSTANT-SNAPSHOT)

**--source-instant-snapshot-key-file**:
Path to the customer-supplied encryption key of the source instant snapshot.
Required if the source instant snapshot is protected by a customer-supplied
encryption key.

**--storage-location**:
Google Cloud Storage location, either regional or multi-regional, where snapshot
content is to be stored. If absent, a nearby regional or multi-regional location
is chosen automatically.

**--source-disk-region**

**--source-instant-snapshot-region**

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
gcloud alpha compute snapshots create
```

```
gcloud beta compute snapshots create
```