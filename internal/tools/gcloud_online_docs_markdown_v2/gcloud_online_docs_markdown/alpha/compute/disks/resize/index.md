# gcloud alpha compute disks resize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize)*

**NAME**

: **gcloud alpha compute disks resize - resize a disk or disks**

**SYNOPSIS**

: **`gcloud alpha compute disks resize` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#DISK_NAME)` [`[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#DISK_NAME)` …] `[--size](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#--size)`=`SIZE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/resize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks resize` resizes a
Compute Engine disk(s).
Only increasing disk size is supported. Disks can be resized regardless of
whether they are attached.

**EXAMPLES**

: To resize a disk called example-disk-1 to new size 6TB, run:

```
gcloud alpha compute disks resize example-disk-1 --size=6TB
```

To resize two disks called example-disk-2 and example-disk-3 to new size 6TB,
run:

```
gcloud alpha compute disks resize example-disk-2 example-disk-3 --size=6TB
```

This assumes that original size of each of these disks is 6TB or less.

**POSITIONAL ARGUMENTS**

: **`DISK_NAME` [`DISK_NAME` …]**:
Names of the disks to operate on.

**REQUIRED FLAGS**

: **--size**:
Indicates the new size of the disks. The value must be a whole number followed
by a size unit of ``GB`` for gigabyte, or
``TB`` for terabyte. If no size unit is
specified, GB is assumed. For example, ``10GB``
will produce 10 gigabyte disks. Disk size must be a multiple of 1 GB.

**OPTIONAL FLAGS**

: **--region**

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
gcloud compute disks resize
```

```
gcloud beta compute disks resize
```