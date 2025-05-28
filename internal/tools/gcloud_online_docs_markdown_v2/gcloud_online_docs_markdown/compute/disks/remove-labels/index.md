# gcloud compute disks remove-labels  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels)*

**NAME**

: **gcloud compute disks remove-labels - remove labels from Google Compute Engine persistent disks**

**SYNOPSIS**

: **`gcloud compute disks remove-labels` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#DISK_NAME)` (`[--all](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#--all)`     | `[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#--labels)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#KEY)`,…]) [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/remove-labels#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks remove-labels` removes labels from a Google
Compute Engine persistent disk.

**EXAMPLES**

: To remove existing labels with key ``k0`` and
``k1`` from 'example-disk'

```
gcloud compute disks remove-labels example-disk --labels=k0,k1
```

Labels can be used to identify the disk and to filter them. To find a disk
labeled with key-value pair ``k1``,
``v2``

```
gcloud compute disks list --filter='labels.k1:v2'
```

To list only the labels when describing a resource, use --format

```
gcloud compute disks describe example-disk --format='default(labels)'
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**REQUIRED FLAGS**

: **--all**

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

: These variants are also available:

```
gcloud alpha compute disks remove-labels
```

```
gcloud beta compute disks remove-labels
```