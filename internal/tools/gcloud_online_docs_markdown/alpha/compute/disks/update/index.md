# gcloud alpha compute disks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update)*

**NAME**

: **gcloud alpha compute disks update - update a Compute Engine persistent disk**

**SYNOPSIS**

: **`gcloud alpha compute disks update` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#DISK_NAME)` [`[--access-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--access-mode)`=`ACCESS_MODE`] [`[--add-guest-os-features](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--add-guest-os-features)`=`ADD_GUEST_OS_FEATURES`] [`[--provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--provisioned-iops)`=`PROVISIONED_IOPS`] [`[--provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--provisioned-throughput)`=`PROVISIONED_THROUGHPUT`] [`[--size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--size)`=`SIZE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--append-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--append-licenses)`=[`LICENSE`,`[LICENSE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#LICENSE)`…,…] `[--remove-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--remove-licenses)`=[`LICENSE`,`[LICENSE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#LICENSE)`…,…] `[--replace-license](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--replace-license)`=`OLD_LICENSE`,`[NEW_LICENSE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#NEW_LICENSE)`,…,[…]] [`[--clear-architecture](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--clear-architecture)`     | `[--update-architecture](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--update-architecture)`=`UPDATE_ARCHITECTURE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--remove-labels)`=[`KEY`,…]] [`[--clear-user-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--clear-user-licenses)`     | `[--update-user-licenses](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--update-user-licenses)`=[`LICENSE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks update` updates a
Compute Engine persistent disk.

**EXAMPLES**

: To update labels 'k0' and 'k1' and remove label 'k3' of a disk, run:

```
gcloud alpha compute disks update example-disk --zone=us-central1-a --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

```
`_k0_` and `_k1_` are added as new labels if not already present.
```

Labels can be used to identify the disk. To list disks with the 'k1:value2'
label, run:

```
gcloud alpha compute disks list --filter='labels.k1:value2'
```

To list only the labels when describing a resource, use --format to filter the
result:

```
gcloud alpha compute disks describe example-disk --format="default(labels)"
```

To append licenses to the disk, run:

```
gcloud alpha compute disks update example-disk --zone=us-central1-a --append-licenses=projects/license-project/global/licenses/license-1,projects/license-project/global/licenses/license-2
```

To remove licenses from the disk, run:

```
gcloud alpha compute disks update example-disk --zone=us-central1-a --replace-licenses=projects/license-project/global/licenses/license-1,projects/license-project/global/licenses/license-2
```

To replace a license on the disk, run:

```
gcloud alpha compute disks update example-disk --zone=us-central1-a --replace-license=projects/license-project/global/licenses/old-license,projects/license-project/global/licenses/new-license
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

**--add-guest-os-features**:
Specifies guest OS features to add to the disk. Refer to [https://cloud.google.com/compute/docs/images/create-custom#guest-os-features](https://cloud.google.com/compute/docs/images/create-custom#guest-os-features)
for a list of available options. `ADD_GUEST_OS_FEATURES`
must be (only one value is supported): `GVNIC`.

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

**--append-licenses**:
"A list of license URIs or license codes. These licenses will be appended to the
existing licenses on the disk. Provided licenses can be either license URIs or
license codes but not a mix of both.

**--remove-licenses**:
A list of license URIs or license codes. If present in the set of existing
licenses, these licenses will be removed. If not present, this is a no-op.
Provided licenses can be either license URIs or license codes but not a mix of
both.

**--replace-license**:
A list of license URIs or license codes. The first license is the license to be
replaced and the second license is the replacement license. Provided licenses
can be either license URIs or license codes but not a mix of both.

**--clear-architecture**

**--clear-labels**

**--clear-user-licenses**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute disks update
```

```
gcloud beta compute disks update
```