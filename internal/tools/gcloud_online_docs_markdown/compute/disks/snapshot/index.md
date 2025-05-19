# gcloud compute disks snapshot  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot)*

**NAME**

: **gcloud compute disks snapshot - create snapshots of Compute Engine persistent disks**

**SYNOPSIS**

: **`gcloud compute disks snapshot` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#DISK_NAME)` [`[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#DISK_NAME)` …] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--async)`] [`[--chain-name](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--chain-name)`=`CHAIN_NAME`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--csek-key-file)`=`FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--description)`=`DESCRIPTION`] [`[--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--guest-flush)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--labels)`=[`KEY`=`VALUE`,…]] [`[--snapshot-names](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--snapshot-names)`=`SNAPSHOT_NAME`,[…]] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--storage-location)`=`LOCATION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks snapshot` creates snapshots of persistent
disks. Snapshots are useful for backing up data, copying a persistent disk, and
even, creating a custom image. Snapshots can be created from persistent disks
even while they are attached to running instances. Once created, snapshots may
be managed (listed, deleted, etc.) via `[gcloud compute
snapshots](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots)`.
Refer to the Snapshot best practices guide. [https://cloud.google.com/compute/docs/disks/snapshot-best-practices](https://cloud.google.com/compute/docs/disks/snapshot-best-practices)
gcloud compute disks snapshot waits until the operation returns a status of
`READY` or `FAILED`, or reaches the maximum timeout, and
returns the last known details of the snapshot.
Note: To create snapshots, the following IAM permissions are necessary
``compute.disks.createSnapshot``,
``compute.snapshots.create``,
``compute.snapshots.get``, and
``compute.zoneOperations.get``.

**EXAMPLES**

: To create a snapshot named `snapshot-test` of a persistent disk named
`test` in zone `us-central1-a`, run:

```
gcloud compute disks snapshot test --zone=us-central1-a --snapshot-names=snapshot-test --description="This is an example snapshot"
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME` [`DISK_NAME` …]**:
Names of the disks to operate on.

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
Text to describe the snapshots being created.

**--guest-flush**:
Create an application-consistent snapshot by informing the OS to prepare for the
snapshot process.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--snapshot-names**:
Names to assign to the created snapshots. Without this option, the name of each
snapshot will be a random 12-character alphanumeric string that starts with a
letter. The values of this option run parallel to the disks specified. For
example,

```
gcloud compute disks snapshot my-disk-1 my-disk-2 my-disk-3 --snapshot-names snapshot-1,snapshot-2,snapshot-3
```

will result in `my-disk-1` being snapshotted as
`snapshot-1`, `my-disk-2` as `snapshot-2`, and
so on. The name must match the
`(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?)` regular expression, which
means it must start with an alphabetic character followed by one or more
alphanumeric characters or dashes. The name must not exceed 63 characters and
must not contain special symbols. All characters must be lowercase.

**--storage-location**:
Google Cloud Storage location, either regional or multi-regional, where snapshot
content is to be stored. If absent, a nearby regional or multi-regional location
is chosen automatically.

**--region**

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
gcloud alpha compute disks snapshot
```

```
gcloud beta compute disks snapshot
```