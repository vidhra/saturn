# gcloud alpha compute disks add-resource-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies)*

**NAME**

: **gcloud alpha compute disks add-resource-policies - add resource policies to a Compute Engine disk**

**SYNOPSIS**

: **`gcloud alpha compute disks add-resource-policies` `[DISK_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies#DISK_NAME)` `[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies#--resource-policies)`=[`RESOURCE_POLICY`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/add-resource-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Add resource policies to a Compute Engine disk.
`gcloud alpha compute disks add-resource-policies` adds resource
policies to a Compute Engine disk. These policies define a schedule for taking
snapshots and a retention period for these snapshots.
For information on how to create resource policies, see: $ [gcloud beta
compute resource-policies create](https://cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/create) --help

**EXAMPLES**

: The following command adds two resource policies to a Compute Engine disk.

```
gcloud alpha compute disks add-resource-policies my-disk --zone=ZONE --resource-policies=policy-1,policy-2
```

**POSITIONAL ARGUMENTS**

: **`DISK_NAME`**:
Name of the disk to add resource policies to.

**REQUIRED FLAGS**

: **--resource-policies**:
A list of resource policy names to be added to the disk. The policies must exist
in the same region as the disk.

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
gcloud compute disks add-resource-policies
```

```
gcloud beta compute disks add-resource-policies
```