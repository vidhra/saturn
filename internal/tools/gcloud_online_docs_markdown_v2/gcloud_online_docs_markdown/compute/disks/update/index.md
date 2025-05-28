# gcloud compute disks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/update](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update)*

**NAME**

: **gcloud compute disks update - update a Compute Engine persistent disk**

**SYNOPSIS**

: **`gcloud compute disks update` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#DISK_NAME)` [`[--access-mode](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--access-mode)`=`ACCESS_MODE`] [`[--provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--provisioned-iops)`=`PROVISIONED_IOPS`] [`[--provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--provisioned-throughput)`=`PROVISIONED_THROUGHPUT`] [`[--size](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--size)`=`SIZE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-architecture](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--clear-architecture)`     | `[--update-architecture](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--update-architecture)`=`UPDATE_ARCHITECTURE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--remove-labels)`=[`KEY`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks update` updates a Compute Engine persistent
disk.

**EXAMPLES**

: To update labels 'k0' and 'k1' and remove label 'k3' of a disk, run:

```
gcloud compute disks update example-disk --zone=us-central1-a --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

```
`_k0_` and `_k1_` are added as new labels if not already present.
```

Labels can be used to identify the disk. To list disks with the 'k1:value2'
label, run:

```
gcloud compute disks list --filter='labels.k1:value2'
```

To list only the labels when describing a resource, use --format to filter the
result:

```
gcloud compute disks describe example-disk --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to update.

**FLAGS**

: **--access-mode**:
Specifies how VMs attached to the disk can access the data on the disk. To grant
read-only access to multiple VMs attached to the disk, set access-mode to
READ_ONLY_MANY. To grant read-write access to only one VM attached to the disk,
use READ_WRITE_SINGLE. READ_WRITE_SINGLE is used if omitted.
`ACCESS_MODE` must be one of: `READ_ONLY_MANY`,
`READ_WRITE_MANY`, `READ_WRITE_SINGLE`.

**--provisioned-iops**:
Provisioned IOPS of disk to update. Only for use with disks of type
hyperdisk-extreme.

**--provisioned-throughput**:
Provisioned throughput of disk to update. The throughput unit is MB per sec.

**--size**:
Size of the disks. The value must be a whole number followed by a size unit of
``GB`` for gigabyte, or
``TB`` for terabyte. If no size unit is
specified, GB is assumed. For details about disk size limits, refer to: [https://cloud.google.com/compute/docs/disks](https://cloud.google.com/compute/docs/disks)

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-architecture**

**--clear-labels**

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
gcloud alpha compute disks update
```

```
gcloud beta compute disks update
```