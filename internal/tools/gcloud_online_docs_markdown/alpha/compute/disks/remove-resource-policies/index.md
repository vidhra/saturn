# gcloud alpha compute disks remove-resource-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies)*

**NAME**

: **gcloud alpha compute disks remove-resource-policies - remove resource policies from a Compute Engine disk**

**SYNOPSIS**

: **`gcloud alpha compute disks remove-resource-policies` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies#DISK_NAME)` `[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies#--resource-policies)`=[`RESOURCE_POLICY`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/remove-resource-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Remove resource policies from a Compute Engine disk.
`gcloud alpha compute disks remove-resource-policies` removes
resource policies from a Compute Engine disk.

**EXAMPLES**

: The following command removes one resource policy from a Compute Engine disk.

```
gcloud alpha compute disks remove-resource-policies my-disk --zone=ZONE --resource-policies=POLICY
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to remove resource policies from.

**REQUIRED FLAGS**

: **--resource-policies**:
A list of resource policy names to be removed from the disk. The policies must
exist in the same region as the disk.

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
gcloud compute disks remove-resource-policies
```

```
gcloud beta compute disks remove-resource-policies
```