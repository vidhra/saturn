# gcloud compute disks convert  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert)*

**NAME**

: **gcloud compute disks convert - convert a Compute Engine Persistent Disk volume to a Hyperdisk volume**

**SYNOPSIS**

: **`gcloud compute disks convert` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#DISK_NAME)` `[--target-disk-type](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--target-disk-type)`=`TARGET_DISK_TYPE` [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--kms-project)`=`KMS_PROJECT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Convert Compute Engine Persistent Disk volumes to Hyperdisk volumes.
`gcloud compute disks convert` converts a Compute Engine Persistent
Disk volume to a Hyperdisk volume. For a comprehensive guide, refer to: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert](https://cloud.google.com/sdk/gcloud/reference/compute/disks/convert).

**EXAMPLES**

: The following command converts a Persistent Disk volume to a Hyperdisk Balanced
volume:

```
gcloud compute disks convert my-disk-1 --zone=ZONE --target-disk-type=hyperdisk-balanced
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to operate on.

**REQUIRED FLAGS**

: **--target-disk-type**:
Specifies the type of Hyperdisk to convert to, for example, to convert a
Hyperdisk Balanced volume, specify `hyperdisk-balanced`. To get a
list of available disk types, run `[gcloud compute disk-types
list](https://cloud.google.com/sdk/gcloud/reference/compute/disk-types/list)`.

**OPTIONAL FLAGS**

: **--kms-key**

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
gcloud alpha compute disks convert
```

```
gcloud beta compute disks convert
```