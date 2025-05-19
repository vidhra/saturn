# gcloud alpha compute disks add-labels  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels)*

**NAME**

: **gcloud alpha compute disks add-labels - add labels to Google Compute Engine persistent disks**

**SYNOPSIS**

: **`gcloud alpha compute disks add-labels` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels#DISK_NAME)` `[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels#--labels)`=[`KEY`=`VALUE`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-labels#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute disks add-labels` adds
labels to a Google Compute Engine persistent disk.

**EXAMPLES**

: To add key-value pairs
``k0``=``v0``
and
``k1``=``v1``
to 'example-disk'

```
gcloud alpha compute disks add-labels example-disk --labels=k0=v0,k1=v1
```

Labels can be used to identify the disk and to filter them. To find a disk
labeled with key-value pair ``k1``,
``v2``

```
gcloud alpha compute disks list --filter='labels.k1:v2'
```

To list only the labels when describing a resource, use --format

```
gcloud alpha compute disks describe example-disk --format='default(labels)'
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**REQUIRED FLAGS**

: **--labels**:
A list of labels to add.

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
gcloud compute disks add-labels
```

```
gcloud beta compute disks add-labels
```