# gcloud compute disks delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete)*

**NAME**

: **gcloud compute disks delete - delete a Compute Engine disk**

**SYNOPSIS**

: **`gcloud compute disks delete` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete#DISK_NAME)` [`[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete#DISK_NAME)` …] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks delete` deletes a Compute Engine disk. A disk
can be deleted only if it is not attached to any virtual machine instances.

**EXAMPLES**

: To delete the disk 'my-disk' in zone 'us-east1-a', run:

```
gcloud compute disks delete my-disk --zone=us-east1-a
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME` [`DISK_NAME` …]**:
Names of the disks to delete.

**FLAGS**

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
gcloud alpha compute disks delete
```

```
gcloud beta compute disks delete
```